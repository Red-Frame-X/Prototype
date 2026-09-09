from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_adguard_filter_integrity.py"
FILTER = ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"


def run_check() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_integrity_check_accepts_current_filter() -> None:
    result = run_check()
    assert result.returncode == 0, result.stderr


def test_integrity_check_is_not_coupled_to_exact_title() -> None:
    original = FILTER.read_text(encoding="utf-8-sig")
    try:
        updated = original.replace(
            "! Title: AdGuard Custom Rules - Red Frame X",
            "! Title: 一時的な表示名",
            1,
        )
        FILTER.write_text(updated, encoding="utf-8")
        result = run_check()
        assert result.returncode == 0, result.stderr
    finally:
        FILTER.write_text(original, encoding="utf-8")


def test_integrity_check_rejects_empty_title() -> None:
    original = FILTER.read_text(encoding="utf-8-sig")
    try:
        updated = original.replace(
            "! Title: AdGuard Custom Rules - Red Frame X",
            "! Title:   ",
            1,
        )
        FILTER.write_text(updated, encoding="utf-8")
        result = run_check()
        assert result.returncode != 0
        assert "missing or empty ! Title metadata" in result.stderr
    finally:
        FILTER.write_text(original, encoding="utf-8")
