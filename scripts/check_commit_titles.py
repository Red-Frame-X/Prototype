#!/usr/bin/env python3
"""Commit titleが空でなく、固定名称を不自然な日本語訳へ置換していないことを検査する。"""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import re

# Repositoryで正式な英語表記を固定する名称。
# 左辺の日本語訳がCommit titleに含まれていた場合は、右辺の正式表記を案内する。
NON_CANONICAL_NAMES = {
    "AdGuardカスタムルール": "AdGuard Custom Rules",
    "AdGuard向け最適化フィルタ": "uB-filter-by-kdroidwin (AdGuard Optimized)",
    "ユーザースクリプト": "UserScript",
    "ChMate用NGワード正規表現": "NG Word Regex for ChMate",
    "ChMate NG Word Regex": "NG Word Regex for ChMate",
    "Markdownメモ": "Markdown Notes",
    "uB-filter-by-kdroidwin（AdGuard Optimized）": "uB-filter-by-kdroidwin (AdGuard Optimized)",
}


def invalid_names(title: str) -> list[tuple[str, str]]:
    return [
        (non_canonical, canonical)
        for non_canonical, canonical in NON_CANONICAL_NAMES.items()
        if non_canonical in title
    ]


# 言語判定ではなく、対象も変更内容もない定型的な入力だけを拒否する。
VAGUE_TITLE = re.compile(
    r"(?:update|fix|change|changes|test|wip|更新|修正|変更|テスト|作業中)[.!。！]*",
    re.IGNORECASE,
)


def vague_title(title: str) -> bool:
    subject = re.sub(r"^[a-z]+(?:\([^\n()]+\))?!?:\s*", "", title.strip())
    return bool(VAGUE_TITLE.fullmatch(subject))


def valid_title(title: str) -> bool:
    return bool(title.strip()) and not invalid_names(title) and not vague_title(title)


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
        if vague_title(title):
            print(f"{commit}: 変更対象と内容を具体的に記述してください: {title!r}")
            print("例: Markdown Notes のリンク表記を修正 / Update Markdown Notes Version")
            failed = True
        for non_canonical, canonical in invalid_names(title):
            print(
                f"{commit}: {non_canonical!r} ではなく正式表記 {canonical!r} を使用してください: {title!r}"
            )
            failed = True
    if failed:
        print("作成前: Web UIのCommit欄、CLIの-m、クライアント/APIのmessageを修正してください。")
        print("共有済み履歴は書き換えず、PRでは適切なtitleでSquashする方法を管理者と確認してください。")
        print("mainに記録済みの場合は履歴を保持し、次回から修正してください。詳細: CONTRIBUTING.md")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
