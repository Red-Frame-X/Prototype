"""検証用マージをチェックアウトした状態で、CIのタイトル検査を再現する。"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_commit_titles.py"


class CommitTitleWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("commit", "--allow-empty", "-qm", "初回コミット")
        self.git("checkout", "-qb", "topic")

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, stderr=subprocess.PIPE
        ).strip()

    def prepare_merge(self, title):
        self.git("commit", "--allow-empty", "-qm", title)
        head = self.git("rev-parse", "HEAD")
        self.git("checkout", "-q", "main")
        self.git("commit", "--allow-empty", "-qm", "基準ブランチの更新")
        base = self.git("rev-parse", "HEAD")
        self.git("merge", "--no-ff", "topic", "-qm", f"Merge {head} into {base}")
        return base, head

    def workflow(self):
        return yaml.safe_load(
            (ROOT / ".github/workflows/quality.yml").read_text(encoding="utf-8")
        )

    def run_workflow(self, base, head):
        steps = self.workflow()["jobs"]["quality"]["steps"]
        step = next(s for s in steps if "check_commit_titles.py" in s.get("run", ""))
        self.assertEqual(
            step["env"]["HEAD_REF"],
            "${{ github.event.pull_request.head.sha || github.sha }}",
        )
        self.assertIn("github.event_name == 'pull_request'", step["env"]["BASE_REF"])
        self.assertIn("github.base_ref", step["env"]["BASE_REF"])
        # CIのシェル処理をそのまま実行し、スクリプトの場所だけ絶対パスにする。
        command = step["run"].replace(
            "python scripts/check_commit_titles.py", f'"{sys.executable}" "{SCRIPT}"'
        )
        return subprocess.run(
            ["bash", "-e", "-c", command], cwd=self.repo,
            env={**os.environ, "BASE_REF": base, "HEAD_REF": head},
            capture_output=True, text=True,
        )

    def test_pr_japanese_title_passes_with_real_synthetic_merge(self):
        base, head = self.prepare_merge("日本語の変更")
        # 原因となった旧動作が実際に失敗することも確認する。
        old = subprocess.run(
            [sys.executable, str(SCRIPT), "--base-ref", base],
            cwd=self.repo, capture_output=True, text=True,
        )
        self.assertEqual(old.returncode, 1)
        self.assertIn("Merge ", old.stdout)
        result = self.run_workflow(base, head)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_pr_earlier_english_title_is_still_rejected(self):
        self.git("commit", "--allow-empty", "-qm", "English change")
        base, head = self.prepare_merge("後続の日本語の変更")
        result = self.run_workflow(base, head)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("English change", result.stdout)
        self.assertNotIn("Merge ", result.stdout)

    def test_push_english_merge_title_is_still_rejected(self):
        self.prepare_merge("日本語の変更")
        result = self.run_workflow("", self.git("rev-parse", "HEAD"))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Merge ", result.stdout)

    def test_only_title_failure_is_deferred_until_final_step(self):
        steps = self.workflow()["jobs"]["quality"]["steps"]
        title_step = next(s for s in steps if s.get("id") == "commit-title-check")
        self.assertTrue(title_step.get("continue-on-error"))

        for name in (
            "Pythonテストの実行",
            "Markdownlintの実行",
            "UserScriptの構文検査",
            "AGLintの実行",
        ):
            step = next(s for s in steps if s.get("name") == name)
            self.assertNotIn("if", step)

        final_step = next(
            s for s in steps if s.get("name") == "コミットタイトル検査の最終判定"
        )
        self.assertEqual(
            final_step.get("if"),
            "always() && steps.commit-title-check.outcome == 'failure'",
        )
        self.assertIn("exit 1", final_step.get("run", ""))


if __name__ == "__main__":
    unittest.main()
