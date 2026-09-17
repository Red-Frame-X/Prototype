#!/usr/bin/env python3
"""Validate AdGuard filter Version metadata for rule-changing commits."""
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
JST = ZoneInfo("Asia/Tokyo")
TARGETS = (
    Path("AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt"),
    Path("AdGuard Custom Rules/AdGuard DNS Custom Rules - Red Frame X.txt"),
)
VERSION_RE = re.compile(r"(?m)^! Version:\s*(\d{12})\s*$")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8")


def show(ref: str, path: Path) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path.as_posix()}"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return proc.stdout if proc.returncode == 0 else None


def version(text: str, path: Path) -> str:
    matches = VERSION_RE.findall(text)
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one ! Version: YYYYMMDDHHMM header")
    stamp = matches[0]
    try:
        datetime.strptime(stamp, "%Y%m%d%H%M").replace(tzinfo=JST)
    except ValueError as exc:
        raise ValueError(f"{path}: invalid JST Version timestamp {stamp}") from exc
    return stamp


def rules_without_version(text: str) -> str:
    return VERSION_RE.sub("! Version: <VERSION>", text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    failed = False
    for path in TARGETS:
        before = show(args.base, path)
        after = show(args.head, path)
        if before is None or after is None or before == after:
            continue

        try:
            old_version = version(before, path)
            new_version = version(after, path)
        except ValueError as exc:
            print(f"error: {exc}")
            failed = True
            continue

        rules_changed = rules_without_version(before) != rules_without_version(after)
        if rules_changed and old_version == new_version:
            print(
                f"error: {path}: rules changed but ! Version: was not updated "
                f"in the same commit ({old_version})"
            )
            failed = True
        elif rules_changed:
            print(f"OK: {path}: rules and Version changed together ({old_version} -> {new_version})")
        else:
            print(f"OK: {path}: only Version metadata changed")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
