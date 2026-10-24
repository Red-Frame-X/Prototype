#!/usr/bin/env python3
"""編集したMarkdown NotesのVersionメタデータが編集日時と一致することを確認する。"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

VERSION_RE = re.compile(r"^\| \*\*Version\*\* \| (\d{12}) \|$", re.MULTILINE)
NOTES_DIR = Path("Markdown Notes")
INDEX_FILE = NOTES_DIR / "README.md"
HEADER_TEMPLATE = NOTES_DIR / "Header Template.md"
EXCLUDED = {HEADER_TEMPLATE}
HEADER_TEMPLATE_VERSION = "| **Version** | yyyymmdd |"
EDIT_TIMEZONE = ZoneInfo("Asia/Tokyo")


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def changed_markdown_files(base_ref: str) -> list[Path]:
    output = run_git("diff", "--name-only", "-z", f"{base_ref}...HEAD", "--", "Markdown Notes/*.md")
    return [Path(line) for line in output.split("\0") if line]


def file_edit_timestamp_yyyymmddhhmm(base_ref: str, path: Path) -> str:
    """確認対象の変更範囲で``path``を最後に編集したコミットの日時を返す。"""
    raw = run_git(
        "log",
        "-1",
        "--format=%cI",
        f"{base_ref}..HEAD",
        "--",
        str(path),
    ).strip()
    if not raw:
        raise ValueError(f"{base_ref}..HEADに{path}の編集コミットがありません。")
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(EDIT_TIMEZONE).strftime("%Y%m%d%H%M")


def validate_header_template() -> str | None:
    """再利用するHeader Templateのプレースホルダーをリテラルのまま保持する。"""
    if not HEADER_TEMPLATE.exists():
        return f"{HEADER_TEMPLATE}: テンプレートファイルがありません。"
    text = HEADER_TEMPLATE.read_text(encoding="utf-8")
    if HEADER_TEMPLATE_VERSION not in text:
        return f"{HEADER_TEMPLATE}: Versionはプレースホルダーの文字列'yyyymmdd'のままにしてください。"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", required=True)
    args = parser.parse_args()

    failures: list[str] = []

    template_failure = validate_header_template()
    if template_failure:
        failures.append(template_failure)

    for path in changed_markdown_files(args.base_ref):
        if path in EXCLUDED or not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        match = VERSION_RE.search(text)
        if not match:
            failures.append(f"{path}: Versionメタデータがないか、形式が不正です（YYYYMMDDHHMMが必要）。")
            continue
        try:
            expected = file_edit_timestamp_yyyymmddhhmm(args.base_ref, path)
        except ValueError as error:
            failures.append(str(error))
            continue
        actual = match.group(1)
        if actual != expected:
            failures.append(
                f"{path}: Versionは{actual}ですが、この編集の正しい日時は{expected}です "
                f"（{EDIT_TIMEZONE.key}）。"
            )

    if failures:
        print("Markdown NotesのVersion検査に失敗しました:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Markdown NotesのVersion検査に合格（{EDIT_TIMEZONE.key}、YYYYMMDDHHMM）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
