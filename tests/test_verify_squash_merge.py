"""一時Repositoryでマージ後検証の成功条件と停止条件を確認する。"""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_squash_merge.py"


class VerifySquashMergeTest(unittest.TestCase):
    def test_squash_after_unrelated_main_update(self):
        with tempfile.TemporaryDirectory() as directory:
            def git(*args):
                return subprocess.check_output(["git", *args], cwd=directory).decode().strip()

            def commit(name):
                Path(directory, name).write_text(name)
                git("add", name)
                git("commit", "-qm", name)
                return git("rev-parse", "HEAD")

            def verify(head, merged, main):
                return subprocess.run(
                    [sys.executable, SCRIPT, base, head, merged, main],
                    cwd=directory, capture_output=True, check=False,
                ).returncode

            git("init", "-q", "-b", "main")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            base = commit("base")
            git("switch", "-qc", "topic")
            head = commit("feature")
            git("switch", "-q", "main")
            other = commit("independent")
            git("merge", "--squash", "topic")
            git("commit", "-qm", "squash")
            merged = git("rev-parse", "HEAD")
            main = commit("later")
            self.assertEqual(verify(head, merged, main), 0)
            self.assertNotEqual(verify(head, other, main), 0)
            self.assertNotEqual(verify(head, merged, other), 0)
            self.assertNotEqual(verify(base, merged, main), 0)
