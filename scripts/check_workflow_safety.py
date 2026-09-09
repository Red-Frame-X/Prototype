#!/usr/bin/env python3
"""プルリクエスト検証用GitHub Actionsを読み取り専用に保つ。"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

WORKFLOW_DIR = Path(".github/workflows")


def _parse_workflow(text: str) -> dict[str, Any]:
    """YAML 1.1による``on``の真偽値変換を避けてGitHub Actions YAMLを解析する。"""
    try:
        data = yaml.load(text, Loader=yaml.BaseLoader)
    except yaml.YAMLError as error:
        raise ValueError(f"invalid workflow YAML: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("workflow YAML must contain a top-level mapping")
    return data


def _declared_events(workflow: dict[str, Any]) -> set[str]:
    """ワークフロー最上位の``on``で宣言されたイベント名を返す。"""
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
    """ワークフローまたはジョブに書き込み権限があるか判定する。"""
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
    """ワークフローがPR安全ポリシーに違反する場合はTrueを返す。"""
    workflow = _parse_workflow(text)
    events = _declared_events(workflow)

    # pull_request_targetはベースリポジトリの権限コンテキストで実行されるため禁止する。
    # 導入時は安全性を明示的に再検討できるよう、既定では許可しない。
    if "pull_request_target" in events:
        return True

    # 通常のpull_request検証は読み取り専用トークンだけを許可する。
    # YAMLの書式差で回避されないよう、permissionsを構造として確認する。
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
