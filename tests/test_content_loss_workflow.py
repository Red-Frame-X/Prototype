"""実際のWorkflowのShellでpush全体・PR・比較元取得失敗を検証する。"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class ContentLossWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.document = self.repo / "doc.md"
        self.write_lines(400)
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, stderr=subprocess.PIPE
        ).strip()

    def write_lines(self, count):
        self.document.write_text("".join(f"line {i}\n" for i in range(count)), encoding="utf-8")

    def run_step(self, event, base, automation_pr=''):
        workflow = yaml.load(
            (ROOT / ".github/workflows/quality.yml").read_text(encoding="utf-8"),
            Loader=yaml.BaseLoader,
        )
        step = next(s for s in workflow["jobs"]["quality"]["steps"]
                    if s.get("name") == "大量の内容消失の防止検査")
        self.assertIn("github.event.before", step["env"]["CONTENT_LOSS_BASE_REF"])
        self.assertIn("github.base_ref", step["env"]["CONTENT_LOSS_BASE_REF"])
        command = step["run"].replace(
            "python scripts/check_large_content_loss.py",
            f'"{sys.executable}" "{ROOT / "scripts/check_large_content_loss.py"}"',
        )
        return subprocess.run(
            ["bash", "-e", "-c", command], cwd=self.repo,
            env={**os.environ, "GITHUB_EVENT_NAME": event, "CONTENT_LOSS_BASE_REF": base,
                 "AUTOMATION_PR": automation_pr},
            text=True, capture_output=True,
        )

    def test_push_rejects_loss_before_last_commit(self):
        self.write_lines(200)
        self.git("commit", "-qam", "loss")
        (self.repo / "other.md").write_text("unrelated\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "unrelated")
        result = self.run_step("push", self.base)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("doc.md", result.stderr)
        self.assertIn("純減 200", result.stderr)

    def test_push_allows_small_changes_across_multiple_commits(self):
        for count in (398, 395):
            self.write_lines(count)
            self.git("commit", "-qam", "small edit")
        result = self.run_step("push", self.base)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_force_push_compares_actual_old_tip(self):
        self.write_lines(800)
        self.git("commit", "-qam", "old main expanded")
        before = self.git("rev-parse", "HEAD")
        self.git("checkout", "-qb", "replacement", self.base)
        self.git("commit", "--allow-empty", "-qm", "new tip")
        result = self.run_step("push", before)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("純減 400", result.stderr)

    def test_pr_uses_merge_base_when_target_advances(self):
        self.git("checkout", "-qb", "target")
        self.write_lines(800)
        self.git("commit", "-qam", "target expanded")
        self.git("checkout", "-qb", "topic", self.base)
        self.write_lines(395)
        self.git("commit", "-qam", "topic small edit")
        result = self.run_step("pull_request", "target")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_dispatched_pr_checks_earlier_loss_in_entire_pr(self):
        self.write_lines(200)
        self.git('commit', '-qam', 'earlier loss')
        self.git('commit', '--allow-empty', '-qm', 'last commit')
        result = self.run_step('workflow_dispatch', self.base, automation_pr='1')
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('純減 200', result.stderr)

    def test_dispatched_pr_uses_merge_base_when_main_advances(self):
        self.git('checkout', '-qb', 'target')
        self.write_lines(800)
        self.git('commit', '-qam', 'target expanded')
        self.git('checkout', '-qb', 'topic', self.base)
        self.write_lines(395)
        self.git('commit', '-qam', 'topic small edit')
        result = self.run_step('workflow_dispatch', 'target', automation_pr='1')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_push_base_cannot_fall_back_to_last_commit(self):
        for base in ("", "0" * 40, "f" * 40):
            with self.subTest(base=base):
                result = self.run_step("push", base)
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_push_fetches_old_tip_when_not_in_checkout(self):
        # 手元にない旧tipをローカルRemoteから取得する実際の経路を通す。
        self.git("checkout", "-qb", "old-tip")
        self.write_lines(800)
        self.git("commit", "-qam", "old tip")
        before = self.git("rev-parse", "HEAD")
        remote = self.repo / "remote.git"
        self.git("clone", "--bare", ".", str(remote))
        self.git("checkout", "-q", "main")
        self.git("branch", "-D", "old-tip")
        self.git("reflog", "expire", "--expire=now", "--all")
        self.git("prune", "--expire=now")
        self.git("remote", "add", "origin", str(remote))
        missing = subprocess.run(["git", "cat-file", "-e", before], cwd=self.repo, capture_output=True)
        self.assertNotEqual(missing.returncode, 0)
        result = self.run_step("push", before)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("純減 400", result.stderr)
        self.git("cat-file", "-e", before)


if __name__ == "__main__":
    unittest.main()
