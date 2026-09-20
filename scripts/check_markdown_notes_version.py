#!/usr/bin/env python3
"""Ensure edited Markdown Notes use the edit timestamp in their Version metadata."""
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
    """Return the last commit timestamp for ``path`` in the reviewed change range."""
    raw = run_git(
        "log",
        "-1",
        "--format=%cI",
        f"{base_ref}..HEAD",
        "--",
        str(path),
    ).strip()
    if not raw:
        raise ValueError(f"No editing commit found for {path} in {base_ref}..HEAD.")
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(EDIT_TIMEZONE).strftime("%Y%m%d%H%M")


def validate_header_template() -> str | None:
    """Keep the reusable Header Template placeholder literal and unchanged."""
    if not HEADER_TEMPLATE.exists():
        return f"{HEADER_TEMPLATE}: template file is missing."
    text = HEADER_TEMPLATE.read_text(encoding="utf-8")
    if HEADER_TEMPLATE_VERSION not in text:
        return f"{HEADER_TEMPLATE}: Version must remain the literal placeholder 'yyyymmdd'."
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
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
            failures.append(f"{path}: Version metadata is missing or malformed (expected YYYYMMDDHHMM).")
            continue
        try:
            expected = file_edit_timestamp_yyyymmddhhmm(args.base_ref, path)
        except ValueError as error:
            failures.append(str(error))
            continue
        actual = match.group(1)
        if actual != expected:
            failures.append(
                f"{path}: Version is {actual}; expected {expected} for this edit "
                f"({EDIT_TIMEZONE.key})."
            )

    if failures:
        print("Markdown Notes Version check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Markdown Notes Version check passed ({EDIT_TIMEZONE.key}, YYYYMMDDHHMM).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
