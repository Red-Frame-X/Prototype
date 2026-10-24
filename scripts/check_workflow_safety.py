#!/usr/bin/env python3
"""Pull Request検証用GitHub Actionsを読み取り専用に保つ。"""

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
        raise ValueError(f"WorkflowのYAMLが不正です: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("Workflow YAMLの最上位はマッピングである必要があります")
    return data


def _declared_events(workflow: dict[str, Any]) -> set[str]:
    """Workflow最上位の``on``で宣言されたイベント名を返す。"""
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
    """WorkflowまたはJobに書き込み権限があるか判定する。"""
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
    """WorkflowがPR安全ポリシーに違反する場合はTrueを返す。"""
    workflow = _parse_workflow(text)
    events = _declared_events(workflow)

    # pull_request_targetはベースRepositoryの権限コンテキストで実行されるため禁止する。
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
        print(f"Workflowの安全性検査に失敗しました: {error}", file=sys.stderr)
        return 1

    if unsafe:
        print(
            "安全でないPR Workflowを検出しました。pull_request Workflowは"
            "読み取り専用とし、pull_request_targetは使用しないでください。",
            file=sys.stderr,
        )
        for path in unsafe:
            print(f" - {path}", file=sys.stderr)
        print(
            "Repositoryへの書き込み処理はpush/schedule/workflow_dispatchに移し、"
            "PR検証を明示的に読み取り専用にしてください。",
            file=sys.stderr,
        )
        return 1
    print("Workflowの安全性検査に合格しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
