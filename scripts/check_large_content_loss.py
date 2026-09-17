#!/usr/bin/env python3
"""Fail CI when tracked text is deleted without explicit authorization."""
from __future__ import annotations

import argparse
import subprocess
import sys

DEFAULT_MAX_DELETIONS = 200
DEFAULT_MAX_NET_LOSS = 120
DEFAULT_MIN_RETAINED_RATIO = 0.25
PROTECTED_SUFFIXES = (".md", ".txt", ".js", ".py", ".yml", ".yaml", ".json")


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


def changed_text_files(base_ref: str) -> list[tuple[int, int, str]]:
    diff = run_git(
        "diff",
        "--numstat",
        f"{base_ref}...HEAD",
        "--",
        "*.md",
        "*.txt",
        "*.js",
        "*.py",
        "*.yml",
        "*.yaml",
        "*.json",
    )
    return list(parse_numstat(diff))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--max-deletions", type=int, default=DEFAULT_MAX_DELETIONS)
    parser.add_argument("--max-net-loss", type=int, default=DEFAULT_MAX_NET_LOSS)
    parser.add_argument("--min-retained-ratio", type=float, default=DEFAULT_MIN_RETAINED_RATIO)
    parser.add_argument(
        "--allow-deletion-in",
        action="append",
        default=[],
        metavar="PATH",
        help="Explicitly authorize deletions in one exact tracked text path. Repeat as needed.",
    )
    args = parser.parse_args()

    allowed_paths = set(args.allow_deletion_in)
    changes = changed_text_files(args.base_ref)
    failures: list[str] = []

    for added, deleted, path in changes:
        if not path.endswith(PROTECTED_SUFFIXES):
            continue

        if deleted > 0 and path not in allowed_paths:
            failures.append(
                f"{path}: +{added}/-{deleted}; tracked text deletion is not explicitly authorized. "
                "Add --allow-deletion-in with this exact path only for a user-requested deletion."
            )
            continue

        net_loss = deleted - added
        if net_loss >= args.max_net_loss:
            failures.append(
                f"{path}: +{added}/-{deleted} (net loss {net_loss}); "
                f"net loss reaches the review threshold {args.max_net_loss}. "
                "Large content removal requires explicit review instead of automatic merging."
            )
            continue

        if deleted < args.max_deletions and net_loss < args.max_net_loss:
            continue

        before_lines = line_count(args.base_ref, path)
        after_lines = line_count("HEAD", path)
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

    stale_authorizations = sorted(
        path for path in allowed_paths
        if not any(changed_path == path and deleted > 0 for _, deleted, changed_path in changes)
    )
    if stale_authorizations:
        failures.append(
            "Deletion authorization does not match the actual diff: "
            + ", ".join(stale_authorizations)
        )

    if failures:
        print("Potential unintended content loss detected:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Content-loss guard passed: no unapproved tracked text deletions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
