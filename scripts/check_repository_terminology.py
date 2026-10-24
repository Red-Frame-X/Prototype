#!/usr/bin/env python3
"""Repository内の固定名称を検査する。公式UI名と検証用の旧表記は保持する。"""
from __future__ import annotations

from pathlib import Path
import subprocess

try:
    from .check_commit_titles import invalid_names
except ImportError:
    from check_commit_titles import invalid_names

ROOT = Path(__file__).resolve().parents[1]
# 旧表記を拒否するための定義・Regression Testには、その入力文字列が必要。
NEGATIVE_FIXTURES = {
    "scripts/check_commit_titles.py",
    "scripts/check_repository_terminology.py",
    "tests/test_commit_titles.py",
    "tests/test_commit_title_workflow.py",
    "tests/test_repository_terminology.py",
}
UI_DOCUMENT = "Markdown Notes/ChromeOS & Android Optimization Guide.md"
OFFICIAL_UI_LABEL = "ユーザースクリプトを許可する"


def violations(path: str, text: str) -> list[tuple[int, str, str]]:
    if path in NEGATIVE_FIXTURES or path.endswith(".source.md") or path == "LICENSE":
        return []
    result = []
    for number, line in enumerate(text.splitlines(), 1):
        if path == UI_DOCUMENT:
            line = line.replace(OFFICIAL_UI_LABEL, "")
        result.extend((number, old, canonical) for old, canonical in invalid_names(line))
    return result


def main() -> int:
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    failed = False
    for relative in filter(None, paths):
        path = ROOT / relative
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        for number, old, canonical in violations(relative, text):
            print(f"{relative}:{number}: {old!r} は正式表記 {canonical!r} に揃えてください")
            failed = True
    if not failed:
        print("Repositoryの固定名称検査に合格しました。")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
