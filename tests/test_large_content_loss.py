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
                path.write_text("\n".join(f"new {i}" for i in range(replacement_lines)) + "\n", encoding="utf-8")
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

    def test_allows_authorized_small_edit(self):
        result = self.run_guard(100, 95, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_large_loss_even_when_more_than_quarter_remains(self):
        result = self.run_guard(1200, 350)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("net loss 850", result.stderr)

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
        self.assertIn("net loss 120", result.stderr)

    def test_rejects_unapproved_file_deletion(self):
        result = self.run_guard(1200, None)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("protected file deletion is not explicitly authorized", result.stderr)

    def test_allows_explicitly_authorized_file_deletion(self):
        result = self.run_guard(1200, None, allow_deletion=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_extreme_content_loss_even_when_authorized(self):
        result = self.run_guard(1200, 100, allow_deletion=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Potential unintended content loss detected", result.stderr)
        self.assertIn("retained 100/1200 lines", result.stderr)


if __name__ == "__main__":
    unittest.main()
