#!/usr/bin/env python3
"""コミットのタイトルに日本語が含まれていることを検査する。"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess

JAPANESE = re.compile(r"[ぁ-ゖァ-ヺ一-鿿]")


def valid_title(title: str) -> bool:
    return bool(JAPANESE.search(title))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--message-file", type=Path)
    group.add_argument("--base-ref")
    parser.add_argument("--head-ref", default="HEAD", help="検査範囲の終点となるコミット・参照")
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
        if not valid_title(title):
            print(f"{commit}: コミットタイトルを日本語で記述してください: {title!r}")
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
