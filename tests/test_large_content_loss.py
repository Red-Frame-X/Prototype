import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_large_content_loss.py"


class LargeContentLossGuardTests(unittest.TestCase):
    def run_guard(self, added: int, deleted: int) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
            path = repo / "doc.md"
            path.write_text("\n".join(f"line {i}" for i in range(deleted + 20)) + "\n", encoding="utf-8")
            subprocess.run(["git", "add", "doc.md"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "base"], cwd=repo, check=True, capture_output=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            path.write_text("\n".join(f"new {i}" for i in range(added + 20)) + "\n", encoding="utf-8")
            subprocess.run(["git", "add", "doc.md"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "change"], cwd=repo, check=True, capture_output=True)
            return subprocess.run(
                ["python", str(SCRIPT), "--base-ref", base],
                cwd=repo,
                text=True,
                capture_output=True,
            )

    def test_allows_small_edit(self):
        result = self.run_guard(30, 30)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_large_deletion(self):
        result = self.run_guard(5, 250)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Potential large content loss detected", result.stderr)


if __name__ == "__main__":
    unittest.main()
