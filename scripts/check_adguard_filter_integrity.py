#!/usr/bin/env python3
"""AdGuardフィルタの構造破損と固定メタデータの変更を早期検出する。"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FILTERS = {
    ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt": {
        "Title": "AdGuard Custom Rules - Red Frame X",
        "Syntax": "AdGuard",
        "min_rules": 25,
    },
    ROOT / "AdGuard Custom Rules" / "AdGuard DNS Custom Rules - Red Frame X.txt": {
        "Title": "AdGuard DNS Custom Rules - Red Frame X",
        "Syntax": "AdGuard DNS",
        "min_rules": 1,
    },
}

# VersionはYYYYMMDDHHMM形式に固定する。
VERSION_RE = re.compile(r"^! Version:\s*\d{12}$", re.MULTILINE)


def fail(message: str) -> int:
    print(f"エラー: {message}", file=sys.stderr)
    return 1


def check_filter(path: Path, expected: dict[str, object]) -> tuple[int, int] | int:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as error:
        return fail(f"読み取れません: {path}: {error}")

    lines = text.splitlines()
    if len(lines) < 10:
        return fail(
            f"フィルターが想定より短くなっています（{path}: {len(lines)}行）。"
            "途中切れ、またはファイル全体の置換の可能性があります"
        )

    header = "\n".join(lines[:20])
    for key in ("Title", "Syntax"):
        marker = f"! {key}: {expected[key]}"
        if marker not in lines[:20]:
            return fail(f"必須メタデータがないか、値が不正です: {path}: {marker}")

    if not VERSION_RE.search(header):
        return fail(f"! Versionメタデータがないか、形式が不正です（YYYYMMDDHHMMが必要）: {path}")

    rules = [
        line.strip()
        for line in lines
        if line.strip() and not line.lstrip().startswith("!")
        and (not line.lstrip().startswith("[") or line.lstrip().startswith("[$"))
    ]
    min_rules = int(expected["min_rules"])
    if len(rules) < min_rules:
        return fail(
            f"フィルターの有効ルール数は{len(rules)}件のみです: {path}。"
            f"必要な最小件数: {min_rules}"
        )

    return len(lines), len(rules)


def main() -> int:
    summaries: list[str] = []
    for path, expected in FILTERS.items():
        result = check_filter(path, expected)
        if isinstance(result, int):
            return result
        line_count, rule_count = result
        summaries.append(f"{path.name}: {line_count}行、{rule_count}件の有効ルール")

    print("AdGuardフィルターの整合性検査に合格:")
    for summary in summaries:
        print(f"- {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
