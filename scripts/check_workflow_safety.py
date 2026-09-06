#!/usr/bin/env python3
"""Enforce read-only GitHub Actions policy for pull-request validation.

Pull-request validation must not receive repository write permissions, regardless
of the command or API client used later in the workflow. The repository also
forbids pull_request_target because that event runs in the base-repository
security context and can expose privileged credentials to unsafe workflow logic.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

WORKFLOW_DIR = Path(".github/workflows")


def _parse_workflow(text: str) -> dict[str, Any]:
    """Parse GitHub Actions YAML without YAML 1.1 boolean coercion of ``on``."""
    try:
        data = yaml.load(text, Loader=yaml.BaseLoader)
    except yaml.YAMLError as error:
        raise ValueError(f"invalid workflow YAML: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("workflow YAML must contain a top-level mapping")
    return data


def _declared_events(workflow: dict[str, Any]) -> set[str]:
    """Return event names declared by a workflow's top-level ``on`` value."""
    value = workflow.get("on")
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return {item for item in value if isinstance(item, str)}
    if isinstance(value, dict):
        return {key for key in value if isinstance(key, str)}
    return set()


def _permission_value_grants_write(value: Any) -> bool:
    if isinstance(value, str):
        return value == "write-all"
    if isinstance(value, dict):
        return any(
            isinstance(permission, str) and permission == "write"
            for permission in value.values()
        )
    return False


def _has_write_permission(workflow: dict[str, Any]) -> bool:
    """Return whether workflow- or job-level permissions grant any write scope."""
    if _permission_value_grants_write(workflow.get("permissions")):
        return True

    jobs = workflow.get("jobs")
    if not isinstance(jobs, dict):
        return False
    return any(
        isinstance(job, dict)
        and _permission_value_grants_write(job.get("permissions"))
        for job in jobs.values()
    )


def is_unsafe_pull_request_writer(text: str) -> bool:
    """Return True when a workflow violates the repository PR safety policy."""
    workflow = _parse_workflow(text)
    events = _declared_events(workflow)

    # Fail closed on pull_request_target. This event executes in the context of
    # the base repository and is unnecessary for this repository's validation
    # workflows. Requiring a deliberate policy change before introducing it is
    # safer than trying to recognize every possible repository mutation command.
    if "pull_request_target" in events:
        return True

    # Ordinary pull_request validation is allowed only with read-only token
    # scopes. Inspect structured permission mappings so valid YAML formatting
    # cannot bypass the policy check.
    return "pull_request" in events and _has_write_permission(workflow)


def find_unsafe_workflows(directory: Path = WORKFLOW_DIR) -> list[Path]:
    unsafe: list[Path] = []
    for pattern in ("*.yml", "*.yaml"):
        for path in sorted(directory.glob(pattern)):
            if is_unsafe_pull_request_writer(path.read_text(encoding="utf-8")):
                unsafe.append(path)
    return unsafe


def main() -> int:
    try:
        unsafe = find_unsafe_workflows()
    except ValueError as error:
        print(f"Workflow safety check failed: {error}", file=sys.stderr)
        return 1

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
