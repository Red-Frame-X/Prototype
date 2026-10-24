from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_adguard_filter_integrity.py"
FILTERS = (
    (
        ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt",
        "! Title: AdGuard Custom Rules - Red Frame X",
    ),
    (
        ROOT / "AdGuard Custom Rules" / "AdGuard DNS Custom Rules - Red Frame X.txt",
        "! Title: AdGuard DNS Custom Rules - Red Frame X",
    ),
)


def run_check() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def replace_title_line(text: str, replacement: str) -> str:
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("! Title:"):
            newline = "\n" if line.endswith("\n") else ""
            lines[index] = f"{replacement}{newline}"
            return "".join(lines)
    raise AssertionError("! Titleメタデータが見つかりません")


class AdGuardFilterIntegrityTests(unittest.TestCase):
    def test_integrity_check_accepts_current_filters(self) -> None:
        result = run_check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_current_filters_have_exact_titles(self) -> None:
        for path, expected_title in FILTERS:
            with self.subTest(path=path.name):
                first_line = path.read_text(encoding="utf-8-sig").splitlines()[0]
                self.assertEqual(first_line, expected_title)

    def test_integrity_check_rejects_unexpected_titles(self) -> None:
        for path, _ in FILTERS:
            original = path.read_text(encoding="utf-8-sig")
            try:
                updated = replace_title_line(original, "! Title: 一時的な表示名")
                path.write_text(updated, encoding="utf-8")
                result = run_check()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("! Title:", result.stderr)
            finally:
                path.write_text(original, encoding="utf-8")

    def test_integrity_check_rejects_empty_title(self) -> None:
        path, _ = FILTERS[0]
        original = path.read_text(encoding="utf-8-sig")
        try:
            updated = replace_title_line(original, "! Title:   ")
            path.write_text(updated, encoding="utf-8")
            result = run_check()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("! Title:", result.stderr)
        finally:
            path.write_text(original, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
