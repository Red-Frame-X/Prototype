#!/usr/bin/env python3
"""標準AdGuardフィルタの構造破損を早期検出する。"""

from __future__ import annotations

from pathlib import Path
import re
import sys

FILTER_PATH = (
    Path(__file__).resolve().parents[1]
    / "AdGuard Custom Rules"
    / "AdGuard Custom Rules - Red Frame X.txt"
)

REQUIRED_METADATA = {
    "Title": "AdGuard Custom Rules - Red Frame X",
    "Syntax": "AdGuard",
}
# 全置換や切り詰め事故を検出するため、最低限の有効ルール数を要求する。
MIN_NONCOMMENT_RULES = 25
# VersionはYYYYMMDDHHMM形式に固定する。
VERSION_RE = re.compile(r"^! Version:\s*\d{12}$", re.MULTILINE)


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        text = FILTER_PATH.read_text(encoding="utf-8-sig")
    except OSError as error:
        return fail(f"cannot read {FILTER_PATH}: {error}")

    lines = text.splitlines()
    if len(lines) < 50:
        return fail(
            f"canonical filter is unexpectedly short ({len(lines)} lines); "
            "possible truncation or whole-file replacement"
        )

    for key, expected in REQUIRED_METADATA.items():
        marker = f"! {key}: {expected}"
        if marker not in lines[:20]:
            return fail(f"missing or invalid required metadata: {marker}")

    if not VERSION_RE.search(text):
        return fail("missing or invalid ! Version metadata (expected YYYYMMDDHHMM)")

    rules = [
        line.strip()
        for line in lines
        if line.strip() and not line.lstrip().startswith("!")
        and (not line.lstrip().startswith("[") or line.lstrip().startswith("[$"))
    ]
    if len(rules) < MIN_NONCOMMENT_RULES:
        return fail(
            f"canonical filter contains only {len(rules)} active rules; "
            f"expected at least {MIN_NONCOMMENT_RULES}"
        )

    print(
        f"AdGuard filter integrity OK: {len(lines)} lines, "
        f"{len(rules)} active rules"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
