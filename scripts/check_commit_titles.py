#!/usr/bin/env python3
"""Commit titleが空でなく、固定名称を不自然な日本語訳へ置換していないことを検査する。"""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

# Repositoryで正式な英語表記を固定する名称。
# 左辺の日本語訳がCommit titleに含まれていた場合は、右辺の正式表記を案内する。
NON_CANONICAL_NAMES = {
    "AdGuardカスタムルール": "AdGuard Custom Rules",
    "AdGuard向け最適化フィルタ": "uB-filter-by-kdroidwin (AdGuard Optimized)",
    "ユーザースクリプト": "UserScript",
    "ChMate用NGワード正規表現": "NG Word Regex for ChMate",
    "Markdownメモ": "Markdown Notes",
}


def invalid_names(title: str) -> list[tuple[str, str]]:
    return [
        (non_canonical, canonical)
        for non_canonical, canonical in NON_CANONICAL_NAMES.items()
        if non_canonical in title
    ]


def valid_title(title: str) -> bool:
    return bool(title.strip()) and not invalid_names(title)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--message-file", type=Path)
    group.add_argument("--base-ref")
    parser.add_argument("--head-ref", default="HEAD", help="検査範囲の終点となるCommit・参照")
    args = parser.parse_args()
    if args.message_file:
        lines = args.message_file.read_text(encoding="utf-8-sig").splitlines()
        entries = [("commit-msg", lines[0] if lines else "")]
    else:
        revision = f"{args.base_ref}..{args.head_ref}" if args.base_ref else args.head_ref
        command = ["git", "log", "--format=%H%x00%s", revision]
        if not args.base_ref:
            command.append("-1")
        output = subprocess.check_output(command, text=True, encoding="utf-8")
        entries = [line.split("\0", 1) for line in output.splitlines()]
    failed = False
    for commit, title in entries:
        if not title.strip():
            print(f"{commit}: Commit titleを空にしないでください")
            failed = True
            continue
        for non_canonical, canonical in invalid_names(title):
            print(
                f"{commit}: {non_canonical!r} ではなく正式表記 {canonical!r} を使用してください: {title!r}"
            )
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
