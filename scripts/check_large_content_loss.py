#!/usr/bin/env python3
"""Fail CI when a change removes an unusually large amount of tracked text."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_MAX_DELETIONS = 200
DEFAULT_MAX_NET_LOSS = 120


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def parse_numstat(text: str):
    for line in text.splitlines():
        added, deleted, path = line.split("\t", 2)
        if added == "-" or deleted == "-":
            continue
        yield int(added), int(deleted), path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--max-deletions", type=int, default=DEFAULT_MAX_DELETIONS)
    parser.add_argument("--max-net-loss", type=int, default=DEFAULT_MAX_NET_LOSS)
    args = parser.parse_args()

    diff = run_git("diff", "--numstat", f"{args.base_ref}...HEAD", "--", "*.md", "*.txt", "*.js", "*.py", "*.yml", "*.yaml", "*.json")
    failures: list[str] = []
    for added, deleted, path in parse_numstat(diff):
        net_loss = deleted - added
        if deleted >= args.max_deletions or net_loss >= args.max_net_loss:
            failures.append(
                f"{path}: +{added}/-{deleted} (net loss {net_loss}). "
                "Large content removal requires explicit review instead of automatic merging."
            )

    if failures:
        print("Potential large content loss detected:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Large-content-loss guard passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
