import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_large_content_loss.py"


class LargeContentLossGuardTests(unittest.TestCase):
    def run_guard(
        self,
        original_lines: int,
        replacement_lines: int | None,
        *,
        allow_deletion: bool = False,
        replacement_text: str | None = None,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
            path = repo / "doc.md"
            path.write_text("\n".join(f"line {i}" for i in range(original_lines)) + "\n", encoding="utf-8")
            subprocess.run(["git", "add", "doc.md"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "base"], cwd=repo, check=True, capture_output=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            if replacement_lines is None:
                path.unlink()
            else:
                path.write_text(
                    replacement_text if replacement_text is not None else
                    "\n".join(f"new {i}" for i in range(replacement_lines)) + "\n",
                    encoding="utf-8",
                )
            subprocess.run(["git", "add", "doc.md"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "change"], cwd=repo, check=True, capture_output=True)
            command = ["python", str(SCRIPT), "--base-ref", base]
            if allow_deletion:
                command.extend(["--allow-deletion-in", "doc.md"])
            return subprocess.run(
                command,
                cwd=repo,
                text=True,
                capture_output=True,
            )

    def test_allows_small_rewrite_without_explicit_authorization(self):
        result = self.run_guard(100, 95)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_output_truncation_below_loss_threshold(self):
        for marker in (
            "…5306 tokens truncated…",
            "...5306 tokens truncated...",
            "…120 characters truncated…",
            "Warning: truncated output (original token count: 4992)",
            "前の文章 …5306 tokens truncated… 後の文章",
            "> …5306 tokens truncated…",
            "* …5306 tokens truncated…",
        ):
            with self.subTest(marker=marker):
                # 行数の保護で失敗しただけでは検出の回帰を保証できない。
                text = "本文\n" * 9 + marker + "\n"
                result = self.run_guard(10, 10, replacement_text=text)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("出力の省略表示が混入", result.stderr)

    def test_deletion_authorization_does_not_allow_output_truncation(self):
        result = self.run_guard(
            10, 10, allow_deletion=True,
            replacement_text="本文\n" * 9 + "> …5306 tokens truncated…\n",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("出力の省略表示が混入", result.stderr)

    def test_allows_ordinary_ellipsis_and_marker_explanation(self):
        result = self.run_guard(
            10, 10, replacement_text=(
                "# Guide\n例：途中…続き\n"
                "`…5306 tokens truncated…` は出力の省略表示です。\n"
            ),
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_allows_authorized_small_edit(self):
        result = self.run_guard(100, 95, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_half_of_short_document_being_lost(self):
        result = self.run_guard(200, 100)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("純減率 50.0%", result.stderr)

    def test_relative_loss_boundary(self):
        for before, after, expected in ((80, 60, 1), (80, 61, 0), (100, 76, 0), (100, 75, 1)):
            with self.subTest(before=before, after=after):
                result = self.run_guard(before, after)
                self.assertEqual(result.returncode, expected, result.stderr)

    def test_allows_reviewed_relative_loss(self):
        result = self.run_guard(200, 100, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_large_loss_even_when_more_than_quarter_remains(self):
        result = self.run_guard(1200, 350)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("純減 850", result.stderr)

    def test_allows_reviewed_large_loss_when_retained_ratio_is_safe(self):
        result = self.run_guard(1200, 350, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_allows_large_rewrite_with_small_net_loss(self):
        result = self.run_guard(1200, 1195)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_allows_loss_just_below_threshold(self):
        result = self.run_guard(1200, 1081)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_loss_at_threshold(self):
        result = self.run_guard(1200, 1080)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("純減 120", result.stderr)

    def test_rejects_unapproved_file_deletion(self):
        result = self.run_guard(1200, None)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("保護対象ファイルの削除は明示的に承認されていません", result.stderr)

    def test_allows_explicitly_authorized_file_deletion(self):
        result = self.run_guard(1200, None, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_extreme_content_loss_even_when_authorized(self):
        result = self.run_guard(1200, 100, allow_deletion=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("意図しない内容消失の可能性を検出しました", result.stderr)
        self.assertIn("保持行数 100/1200行", result.stderr)


if __name__ == "__main__":
    unittest.main()
