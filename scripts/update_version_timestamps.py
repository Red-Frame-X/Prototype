#!/usr/bin/env python3
"""Update Version metadata in changed repository content using current JST time."""
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

JST = ZoneInfo("Asia/Tokyo")
HEADER_TEMPLATE = Path("Markdown Notes/Header Template.md")
TARGET_PREFIXES = (
    "AdGuard Custom Rules/",
    "Markdown Notes/",
    "NG Word Regex for ChMate/",
    "UserScript/",
)

PATTERNS = (
    (re.compile(r"(?m)^! Version:[ \t]*\d{8,14}$"), lambda stamp: f"! Version: {stamp}"),
    (re.compile(r"(?m)^\| \*\*Version\*\* \| \d{8,14} \|$"), lambda stamp: f"| **Version** | {stamp} |"),
    (re.compile(r"(?m)^(//[ \t]*@version[ \t]+)\S+[ \t]*$"), lambda stamp: rf"\g<1>{stamp}"),
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def changed_files(base: str, head: str) -> list[Path]:
    output = git("diff", "--name-only", "-z", base, head)
    return [Path(line) for line in output.split("\0") if line]


def is_target(path: Path) -> bool:
    if path == HEADER_TEMPLATE:
        return False
    posix = path.as_posix()
    return any(posix.startswith(prefix) for prefix in TARGET_PREFIXES)


def update_file(path: Path, stamp: str) -> bool:
    if not path.is_file():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    # ファイル種別に対応する先頭メタデータだけを更新し、本文のコード例を保持する。
    lines = text.splitlines(keepends=True)
    if path.suffix == ".md":
        pattern, replacement = PATTERNS[1]
        header_end = 0
        for line in lines:
            if line.lstrip().startswith(("```", "~~~")):
                break
            header_end += len(line)
            if pattern.search(line.rstrip("\n")):
                break
    elif path.suffix == ".txt":
        pattern, replacement = PATTERNS[0]
        header_end = 0
        for line in lines:
            if line.strip() and not line.startswith("!"):
                break
            header_end += len(line)
    elif path.name.endswith(".user.js") and text.startswith("// ==UserScript==\n"):
        pattern, replacement = PATTERNS[2]
        marker = "// ==/UserScript=="
        header_end = text.find(marker)
        if header_end < 0:
            return False
    else:
        return False

    header, matches = pattern.subn(replacement(stamp), text[:header_end], count=1)
    updated = header + text[header_end:]

    if matches == 0 or updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Base commit SHA")
    parser.add_argument("--head", default="HEAD", help="Head commit/ref")
    args = parser.parse_args()

    stamp = datetime.now(JST).strftime("%Y%m%d%H%M")
    updated: list[str] = []
    for path in changed_files(args.base, args.head):
        if is_target(path) and update_file(path, stamp):
            updated.append(path.as_posix())

    if updated:
        print(f"Updated Version metadata to {stamp} JST:")
        for path in updated:
            print(f"- {path}")
    else:
        print("No changed files with supported Version metadata required an update.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
