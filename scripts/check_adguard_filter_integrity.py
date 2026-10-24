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

# 表示名は運用上変更される可能性があるため固定値にはしない。
# 一方、Title自体の欠落・空値は購読時の識別性を損なうため検出する。
# ``\s``は改行も含むため、``\s*``を使うと次のメタデータ行を
# タイトル値として扱う恐れがある。任意の空白は現在行の範囲に限定する。
TITLE_RE = re.compile(r"^! Title:[ \t]*\S[^\r\n]*$", re.MULTILINE)
REQUIRED_METADATA = {
    "Syntax": "AdGuard",
}
# 全置換や切り詰め事故を検出するため、最低限の有効ルール数を要求する。
MIN_NONCOMMENT_RULES = 25
# VersionはYYYYMMDDHHMM形式に固定する。
VERSION_RE = re.compile(r"^! Version:\s*\d{12}$", re.MULTILINE)


def fail(message: str) -> int:
    print(f"エラー: {message}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        text = FILTER_PATH.read_text(encoding="utf-8-sig")
    except OSError as error:
        return fail(f"読み取れません: {FILTER_PATH}: {error}")

    lines = text.splitlines()
    if len(lines) < 50:
        return fail(
            f"標準フィルターが想定より短くなっています（{len(lines)}行）。"
            "途中切れ、またはファイル全体の置換の可能性があります"
        )

    header = "\n".join(lines[:20])
    if not TITLE_RE.search(header):
        return fail("! Titleメタデータがないか、値が空です")

    for key, expected in REQUIRED_METADATA.items():
        marker = f"! {key}: {expected}"
        if marker not in lines[:20]:
            return fail(f"必須メタデータがないか、値が不正です: {marker}")

    if not VERSION_RE.search(header):
        return fail("! Versionメタデータがないか、形式が不正です（YYYYMMDDHHMMが必要）")

    rules = [
        line.strip()
        for line in lines
        if line.strip() and not line.lstrip().startswith("!")
        and (not line.lstrip().startswith("[") or line.lstrip().startswith("[$"))
    ]
    if len(rules) < MIN_NONCOMMENT_RULES:
        return fail(
            f"標準フィルターの有効ルール数は{len(rules)}件のみです。"
            f"必要な最小件数: {MIN_NONCOMMENT_RULES}"
        )

    print(
        f"AdGuardフィルターの整合性検査に合格: {len(lines)}行、"
        f"{len(rules)}件の有効ルール"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
