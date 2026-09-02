#!/usr/bin/env python3
"""Preflight checks for edits to the canonical AdGuard user-rule filter."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def active_rules(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith(("!", "["))
    ]


def read(path: Path) -> str:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")

    # Check the raw bytes before Python's universal-newline translation can
    # normalize CRLF or CR into LF and hide the original line-ending format.
    if b"\r" in raw:
        fail("CR characters detected; canonical filter must use LF line endings")

    try:
        return raw.decode("utf-8-sig")
    except UnicodeError as exc:
        fail(f"cannot decode {path} as UTF-8: {exc}")


def git_show(ref: str, path: Path) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    proc = subprocess.run(
        ["git", "show", f"{ref}:{rel}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return proc.stdout if proc.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default=None)
    args = parser.parse_args()

    text = read(FILTER)

    # Do not fail solely on a legacy missing final newline. When comparing a PR,
    # only reject if the base had a final newline and the edit removed it.
    lines = text.splitlines()
    trailing = [i for i, line in enumerate(lines, 1) if line.rstrip() != line]
    if trailing:
        fail(f"trailing whitespace found on line(s): {', '.join(map(str, trailing[:10]))}")

    rules = active_rules(text)
    duplicates = sorted(rule for rule, count in Counter(rules).items() if count > 1)
    if duplicates:
        sample = "\n".join(f"  {rule}" for rule in duplicates[:10])
        fail(f"duplicate active rule(s) detected:\n{sample}")

    if args.base_ref:
        base = git_show(args.base_ref, FILTER)
        if base is not None:
            if base.endswith("\n") and not text.endswith("\n"):
                fail("edit removed the canonical filter's final newline")

            before = active_rules(base)
            removed = len(before) - len(rules)
            if removed > max(10, len(before) // 4):
                fail(
                    "suspiciously large active-rule reduction detected "
                    f"({len(before)} -> {len(rules)}); possible whole-file replacement"
                )

            header_before = base.splitlines()[:9]
            header_after = lines[:9]
            stable_prefixes = (
                "! Title:",
                "! Description:",
                "! Syntax:",
                "! Expires:",
                "! Homepage:",
                "! License:",
                "! Note:",
            )
            for prefix in stable_prefixes:
                old = next((x for x in header_before if x.startswith(prefix)), None)
                new = next((x for x in header_after if x.startswith(prefix)), None)
                if old != new:
                    fail(f"protected metadata changed unexpectedly: {prefix}")

    print(f"AdGuard edit preflight OK: {len(rules)} active rules, no duplicates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
