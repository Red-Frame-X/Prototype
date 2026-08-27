from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_adguard_user_rule_edit.py"

class AdGuardEditPreflightTests(unittest.TestCase):
    def run_script(self, text: str):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "AdGuard Custom Rules"
            target.mkdir()
            (root / "scripts").mkdir()
            script = root / "scripts" / SCRIPT.name
            script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
            (target / "AdGuard Custom Rules - Red Frame X.txt").write_text(text, encoding="utf-8")
            return subprocess.run(
                ["python", str(script)],
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def test_accepts_unique_rules(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad
example.org##.promo
"""
        result = self.run_script(text)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_duplicate_active_rule(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad
example.com##.ad
"""
        result = self.run_script(text)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate active rule", result.stderr)

    def test_rejects_trailing_whitespace(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad   
"""
        result = self.run_script(text)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("trailing whitespace", result.stderr)

if __name__ == "__main__":
    unittest.main()
