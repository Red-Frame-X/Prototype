#!/usr/bin/env python3
"""Ensure edited Markdown Notes use the edit date in their Version metadata."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION_RE = re.compile(r"^\| \*\*Version\*\* \| (\d{8}) \|$", re.MULTILINE)
NOTES_DIR = Path("Markdown Notes")
INDEX_FILE = NOTES_DIR / "README.md"
HEADER_TEMPLATE = NOTES_DIR / "Header Template.md"
EXCLUDED = {INDEX_FILE, HEADER_TEMPLATE}
HEADER_TEMPLATE_VERSION = "| **Version** | yyyymmdd |"


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def changed_markdown_files(base_ref: str) -> list[Path]:
    output = run_git("diff", "--name-only", f"{base_ref}...HEAD", "--", "Markdown Notes/*.md")
    return [Path(line) for line in output.splitlines() if line]


def commit_date_yyyymmdd() -> str:
    raw = run_git("show", "-s", "--format=%cI", "HEAD").strip()
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc).strftime("%Y%m%d")


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

    expected = commit_date_yyyymmdd()
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
            failures.append(f"{path}: Version metadata is missing or malformed.")
            continue
        actual = match.group(1)
        if actual != expected:
            failures.append(f"{path}: Version is {actual}; expected {expected} for this edit.")

    if failures:
        print("Markdown Notes Version check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Markdown Notes Version check passed for edit date {expected}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
