import os
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_markdown_notes_version.py"


class MarkdownNotesVersionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)
        subprocess.run(["git", "init", "-q"], cwd=self.repo, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.repo, check=True)
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=self.repo,
            check=True,
        )
        notes = self.repo / "Markdown Notes"
        notes.mkdir()
        (notes / "Header Template.md").write_text(
            "| **Version** | yyyymmdd |\n",
            encoding="utf-8",
        )
        (notes / "Guide.md").write_text(
            "| **Version** | 20260911 |\n\nInitial\n",
            encoding="utf-8",
        )
        self.commit("base", "2026-09-11T12:00:00+09:00")
        self.base = self.git("rev-parse", "HEAD").strip()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, encoding="utf-8"
        )

    def commit(self, message: str, date: str) -> None:
        subprocess.run(["git", "add", "."], cwd=self.repo, check=True)
        env = os.environ | {"GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date}
        subprocess.run(
            ["git", "commit", "-qm", message], cwd=self.repo, check=True, env=env
        )

    def write_guide(self, version: str, body: str) -> None:
        (self.repo / "Markdown Notes" / "Guide.md").write_text(
            f"| **Version** | {version} |\n\n{body}\n",
            encoding="utf-8",
        )

    def run_check(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python", str(SCRIPT), "--base-ref", self.base],
            cwd=self.repo,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_uses_document_edit_date_not_later_unrelated_commit_date(self) -> None:
        self.write_guide("20260912", "Edited")
        self.commit("edit guide", "2026-09-12T23:50:00+09:00")
        (self.repo / "unrelated.txt").write_text("later\n", encoding="utf-8")
        self.commit("unrelated next day", "2026-09-13T00:10:00+09:00")

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_uses_latest_commit_when_document_is_edited_again(self) -> None:
        self.write_guide("20260912", "First edit")
        self.commit("first guide edit", "2026-09-12T23:50:00+09:00")
        self.write_guide("20260913", "Second edit")
        self.commit("second guide edit", "2026-09-13T00:10:00+09:00")

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_version_that_differs_from_document_edit_date(self) -> None:
        self.write_guide("20260913", "Edited on previous day")
        self.commit("edit guide", "2026-09-12T23:50:00+09:00")

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected 20260912", result.stderr)


if __name__ == "__main__":
    unittest.main()
