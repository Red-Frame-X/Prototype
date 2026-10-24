import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.check_commit_titles import valid_title

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_commit_titles.py"


class CommitTitleTests(unittest.TestCase):
    def test_japanese_description_with_identifiers(self):
        self.assertTrue(valid_title("fix: AdGuardのVersion更新を修正 (#123)"))
        self.assertTrue(valid_title("プルリクエスト #123 をマージ"))

    def test_english_and_empty_titles_are_rejected(self):
        for title in ("", "fix: update Version", "Merge pull request #123"):
            with self.subTest(title=title):
                self.assertFalse(valid_title(title))

    def test_japanese_body_does_not_make_english_title_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            message = Path(directory) / "COMMIT_EDITMSG"
            message.write_text("fix: update Version\n\n日本語の本文\n", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--message-file", str(message)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)

    def test_range_checks_each_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            def git(*args):
                return subprocess.check_output(["git", *args], cwd=directory, text=True).strip()
            git("init", "-q")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.com")
            git("commit", "--allow-empty", "-qm", "初回コミット")
            base = git("rev-parse", "HEAD")
            git("commit", "--allow-empty", "-qm", "English title")
            git("commit", "--allow-empty", "-qm", "日本語のコミット")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--base-ref", base], cwd=directory,
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("English title", result.stdout)


if __name__ == "__main__":
    unittest.main()
