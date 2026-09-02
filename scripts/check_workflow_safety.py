#!/usr/bin/env python3
"""Enforce read-only GitHub Actions policy for pull-request validation.

Pull-request validation must not receive repository write permissions, regardless
of the command or API client used later in the workflow. The repository also
forbids pull_request_target because that event runs in the base-repository
security context and can expose privileged credentials to unsafe workflow logic.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")


def _without_comment_only_lines(text: str) -> str:
    """Remove comment-only lines while preserving inline YAML content."""
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def _has_event(text: str, event: str) -> bool:
    """Return whether a workflow declares the given GitHub Actions event."""
    return bool(
        re.search(rf"(?m)^\s{{0,2}}{re.escape(event)}\s*:", text)
        or re.search(
            rf"(?m)^\s{{0,2}}on\s*:\s*\[[^\]]*\b{re.escape(event)}\b",
            text,
        )
    )


def _has_write_permission(text: str) -> bool:
    """Return whether workflow- or job-level permissions grant any write scope."""
    return bool(
        re.search(r"(?m)^\s*permissions\s*:\s*write-all\s*(?:#.*)?$", text)
        or re.search(
            r"(?m)^\s*[A-Za-z][A-Za-z0-9_-]*\s*:\s*write\s*(?:#.*)?$",
            text,
        )
    )


def is_unsafe_pull_request_writer(text: str) -> bool:
    """Return True when a workflow violates the repository PR safety policy."""
    text = _without_comment_only_lines(text)

    # Fail closed on pull_request_target. This event executes in the context of
    # the base repository and is unnecessary for this repository's validation
    # workflows. Requiring a deliberate policy change before introducing it is
    # safer than trying to recognize every possible repository mutation command.
    if _has_event(text, "pull_request_target"):
        return True

    # Ordinary pull_request validation is allowed only with read-only token
    # scopes. Detect write permission directly instead of relying on downstream
    # command matching (git push, gh api, curl, custom actions, and so on).
    return _has_event(text, "pull_request") and _has_write_permission(text)


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
            "Unsafe pull-request workflow(s) detected: pull_request workflows "
            "must remain read-only and pull_request_target is not permitted.",
            file=sys.stderr,
        )
        for path in unsafe:
            print(f" - {path}", file=sys.stderr)
        print(
            "Move repository-writing automation to push/schedule/workflow_dispatch "
            "and keep pull-request validation explicitly read-only.",
            file=sys.stderr,
        )
        return 1
    print("Workflow safety check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
