from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_adguard_user_rule_edit.py"


class AdGuardEditPreflightTests(unittest.TestCase):
    def run_script(self, content: str | bytes):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "AdGuard Custom Rules"
            target.mkdir()
            (root / "scripts").mkdir()
            script = root / "scripts" / SCRIPT.name
            script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
            filter_path = target / "AdGuard Custom Rules - Red Frame X.txt"
            if isinstance(content, bytes):
                filter_path.write_bytes(content)
            else:
                filter_path.write_text(content, encoding="utf-8", newline="\n")
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

    def test_rejects_crlf_line_endings(self):
        content = (
            "! Title: AdGuard Custom Rules - Red Frame X\r\n"
            "! Description: Test\r\n"
            "example.com##.ad\r\n"
        ).encode("utf-8")
        result = self.run_script(content)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CR characters detected", result.stderr)

    def test_rejects_cr_line_endings(self):
        content = (
            "! Title: AdGuard Custom Rules - Red Frame X\r"
            "! Description: Test\r"
            "example.com##.ad\r"
        ).encode("utf-8")
        result = self.run_script(content)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CR characters detected", result.stderr)

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

    def test_rejects_duplicate_non_basic_modifier_rule(self):
        result = self.run_script("[$app=com.example.app]##.ad\n" * 2)
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
