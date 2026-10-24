import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.check_commit_titles import valid_title

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_commit_titles.py"


class CommitTitleTests(unittest.TestCase):
    def test_japanese_description_with_canonical_identifiers(self):
        self.assertTrue(valid_title("fix: AdGuard Custom Rules のVersion更新を修正 (#123)"))
        self.assertTrue(valid_title("Pull Request #123 をマージ"))
        self.assertTrue(valid_title("Markdown Notes のVersion自動更新処理を修正"))

    def test_english_titles_are_allowed(self):
        self.assertTrue(valid_title("fix: update Version"))
        self.assertTrue(valid_title("Merge pull request #123"))
        self.assertTrue(valid_title("Update uB-filter-by-kdroidwin (AdGuard Optimized)"))

    def test_empty_and_noncanonical_titles_are_rejected(self):
        for title in (
            "",
            "   ",
            "Update uB-filter-by-kdroidwin（AdGuard Optimized）",
            "AdGuardカスタムルールを更新",
            "AdGuard向け最適化フィルタを更新",
            "ユーザースクリプトを更新",
            "ChMate用NGワード正規表現を更新",
            "Markdownメモを更新",
        ):
            with self.subTest(title=title):
                self.assertFalse(valid_title(title))

    def test_each_canonical_name_is_allowed_in_japanese_and_english_titles(self):
        from scripts.check_commit_titles import NON_CANONICAL_NAMES
        for name in set(NON_CANONICAL_NAMES.values()):
            with self.subTest(name=name):
                self.assertTrue(valid_title(f"{name} を自動更新"))
                self.assertTrue(valid_title(f"Update {name}"))

    def test_body_does_not_fix_noncanonical_title(self):
        with tempfile.TemporaryDirectory() as directory:
            message = Path(directory) / "COMMIT_EDITMSG"
            message.write_text("Markdownメモを更新\n\nMarkdown Notes の説明\n", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--message-file", str(message)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("Markdown Notes", result.stdout)

    def test_range_checks_each_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            def git(*args):
                return subprocess.check_output(["git", *args], cwd=directory, text=True).strip()
            git("init", "-q")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.com")
            git("commit", "--allow-empty", "-qm", "Initial commit")
            base = git("rev-parse", "HEAD")
            git("commit", "--allow-empty", "-qm", "Markdownメモを更新")
            git("commit", "--allow-empty", "-qm", "Update Markdown Notes")
            result = subprocess.run(
                ["python3", str(SCRIPT), "--base-ref", base], cwd=directory,
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("Markdownメモ", result.stdout)


if __name__ == "__main__":
    unittest.main()
