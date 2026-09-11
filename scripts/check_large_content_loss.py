#!/usr/bin/env python3
"""Fail CI when a change removes an unusually large share of tracked text."""
from __future__ import annotations

import argparse
import subprocess
import sys

DEFAULT_MAX_DELETIONS = 200
DEFAULT_MAX_NET_LOSS = 120
DEFAULT_MIN_RETAINED_RATIO = 0.25


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def parse_numstat(text: str):
    for line in text.splitlines():
        added, deleted, path = line.split("\t", 2)
        if added == "-" or deleted == "-":
            continue
        yield int(added), int(deleted), path


def line_count(ref: str, path: str) -> int | None:
    try:
        content = run_git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None
    return len(content.splitlines())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--max-deletions", type=int, default=DEFAULT_MAX_DELETIONS)
    parser.add_argument("--max-net-loss", type=int, default=DEFAULT_MAX_NET_LOSS)
    parser.add_argument("--min-retained-ratio", type=float, default=DEFAULT_MIN_RETAINED_RATIO)
    args = parser.parse_args()

    diff = run_git(
        "diff",
        "--numstat",
        f"{args.base_ref}...HEAD",
        "--",
        "*.md",
        "*.txt",
        "*.js",
        "*.py",
        "*.yml",
        "*.yaml",
        "*.json",
    )
    failures: list[str] = []
    for added, deleted, path in parse_numstat(diff):
        net_loss = deleted - added
        if deleted < args.max_deletions and net_loss < args.max_net_loss:
            continue

        before_lines = line_count(args.base_ref, path)
        after_lines = line_count("HEAD", path)

        # Deleted files and files reduced to a tiny fraction of their previous size
        # are likely accidental content loss. Large rewrites that retain a meaningful
        # body of content are allowed to avoid false positives from intentional edits.
        if after_lines is None:
            failures.append(
                f"{path}: file deleted (+{added}/-{deleted}). "
                "Large content removal requires explicit review instead of automatic merging."
            )
            continue

        if before_lines and after_lines / before_lines < args.min_retained_ratio:
            failures.append(
                f"{path}: +{added}/-{deleted} (net loss {net_loss}); "
                f"retained {after_lines}/{before_lines} lines "
                f"({after_lines / before_lines:.1%}). "
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
