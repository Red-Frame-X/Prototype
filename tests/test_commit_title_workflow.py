"""検証用MergeをCheckoutした状態で、CIのCommit title検査を再現する。"""
import os
import shutil
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
        self.git("commit", "--allow-empty", "-qm", "Initial commit")
        self.git("checkout", "-qb", "topic")

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, stderr=subprocess.PIPE
        ).strip()

    def prepare_merge(self, title):
        self.git("commit", "--allow-empty", "-qm", title)
        head = self.git("rev-parse", "HEAD")
        self.git("checkout", "-q", "main")
        self.git("commit", "--allow-empty", "-qm", "Update base Branch")
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
        command = step["run"].replace(
            "python scripts/check_commit_titles.py", f'"{sys.executable}" "{SCRIPT}"'
        )
        return subprocess.run(
            ["bash", "-e", "-c", command], cwd=self.repo,
            env={**os.environ, "BASE_REF": base, "HEAD_REF": head},
            capture_output=True, text=True,
        )

    def test_pr_canonical_title_passes_with_real_synthetic_merge(self):
        base, head = self.prepare_merge("Update Markdown Notes")
        result = self.run_workflow(base, head)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_pr_earlier_noncanonical_title_is_rejected(self):
        self.git("commit", "--allow-empty", "-qm", "Markdownメモを更新")
        base, head = self.prepare_merge("Update Markdown Notes")
        result = self.run_workflow(base, head)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Markdownメモ", result.stdout)
        self.assertNotIn("Merge ", result.stdout)

    def test_push_english_merge_title_is_allowed(self):
        self.prepare_merge("Update Markdown Notes")
        result = self.run_workflow("", self.git("rev-parse", "HEAD"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def prepare_force_push(self, earlier_title):
        # 旧mainを保持するRemoteから、新mainの履歴だけをCheckoutする。
        self.git("commit", "--allow-empty", "-qm", "旧mainの変更")
        before = self.git("rev-parse", "HEAD")
        self.git("checkout", "-q", "main")
        self.git("commit", "--allow-empty", "-qm", earlier_title)
        self.git("commit", "--allow-empty", "-qm", "READMEの説明を更新")
        head = self.git("rev-parse", "HEAD")
        remote = self.repo.parent / (self.repo.name + "-remote.git")
        checkout = self.repo.parent / (self.repo.name + "-checkout")
        self.addCleanup(shutil.rmtree, remote, True)
        self.addCleanup(shutil.rmtree, checkout, True)
        self.git("clone", "--bare", str(self.repo), str(remote))
        self.git("clone", "--no-local", "--single-branch", "--branch", "main",
                 str(remote), str(checkout))
        self.git("--git-dir", str(remote), "update-ref", "-d", "refs/heads/topic")
        self.repo = checkout
        missing = subprocess.run(
            ["git", "cat-file", "-e", before], cwd=self.repo,
            capture_output=True,
        )
        self.assertNotEqual(missing.returncode, 0)
        return before, head

    def test_force_push_fetches_missing_before_commit(self):
        before, head = self.prepare_force_push("Markdown Notes のリンクを更新")
        result = self.run_workflow(before, head)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.git("cat-file", "-e", before)

    def test_force_push_checks_earlier_titles_not_only_head(self):
        before, head = self.prepare_force_push("Markdownメモを更新")
        result = self.run_workflow(before, head)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Markdownメモ", result.stdout)

    def test_missing_before_fetch_failure_does_not_pass(self):
        result = self.run_workflow("f" * 40, self.git("rev-parse", "HEAD"))
        self.assertNotEqual(result.returncode, 0)

    def test_title_failure_is_not_hidden_and_other_checks_run(self):
        steps = self.workflow()["jobs"]["quality"]["steps"]
        title_step = next(s for s in steps if s.get("id") == "commit-title-check")
        self.assertNotIn("continue-on-error", title_step)

        for name in (
            "Python Testの実行",
            "Markdownlintの実行",
            "UserScriptの構文検査",
            "AGLintの実行",
        ):
            step = next(s for s in steps if s.get("name") == name)
            self.assertEqual(step.get("if"), "${{ !cancelled() }}")

        final_step = next(
            s for s in steps if s.get("name") == "Commit title検査の最終判定"
        )
        self.assertEqual(
            final_step.get("if"),
            "always() && steps.commit-title-check.outcome == 'failure'",
        )
        self.assertIn("exit 1", final_step.get("run", ""))


if __name__ == "__main__":
    unittest.main()
