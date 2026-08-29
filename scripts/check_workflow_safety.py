#!/usr/bin/env python3
"""Reject pull-request workflows that can push back into the repository.

A pull-request validation workflow should not mutate its own source branch with
GITHUB_TOKEN. Keeping validation read-only avoids races, duplicate runs, and
state-dependent failures when the branch has already been modified.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")


def _without_comments(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def is_unsafe_pull_request_writer(text: str) -> bool:
    """Return True for PR-triggered workflows that have write access and push."""
    text = _without_comments(text)
    has_pull_request = bool(
        re.search(r"(?m)^\s{0,2}pull_request\s*:", text)
        or re.search(r"(?m)^\s{0,2}on\s*:\s*\[[^\]]*\bpull_request\b", text)
    )
    has_contents_write = bool(
        re.search(r"(?m)^\s*contents\s*:\s*write\s*$", text)
    )
    has_git_push = bool(re.search(r"(?m)^\s*[^#\n]*\bgit\s+push\b", text))
    return has_pull_request and has_contents_write and has_git_push


def find_unsafe_workflows(directory: Path = WORKFLOW_DIR) -> list[Path]:
    unsafe: list[Path] = []
    for pattern in ("*.yml", "*.yaml"):
        for path in sorted(directory.glob(pattern)):
            if is_unsafe_pull_request_writer(path.read_text(encoding="utf-8")):
                unsafe.append(path)
    return unsafe


def main() -> int:
    unsafe = find_unsafe_workflows()
    if unsafe:
        print(
            "Unsafe pull-request workflow(s) detected: PR validation must not "
            "combine contents: write with git push.",
            file=sys.stderr,
        )
        for path in unsafe:
            print(f" - {path}", file=sys.stderr)
        print(
            "Move repository-writing automation to push/schedule/workflow_dispatch "
            "or keep the pull_request workflow read-only.",
            file=sys.stderr,
        )
        return 1
    print("Workflow safety check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
