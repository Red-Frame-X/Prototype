#!/usr/bin/env python3
"""ローカルのLint・Test実行前に、現在のPythonとNode.jsの依存を確認する。"""

from __future__ import annotations

from importlib import import_module, metadata
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PYTHON_IMPORTS = {"PyYAML": "yaml", "markdown-it-py": "markdown_it"}


def check_environment(root: Path) -> list[str]:
    errors = []
    for line in (root / "requirements-ci.txt").read_text(encoding="utf-8").splitlines():
        requirement = line.split("#", 1)[0].strip()
        if not requirement:
            continue
        match = re.fullmatch(r"([A-Za-z0-9_.-]+)==([A-Za-z0-9_.+-]+)", requirement)
        if not match:
            errors.append(f"Python依存の固定Versionを確認できません: {requirement}")
            continue
        name, expected = match.groups()
        try:
            actual = metadata.version(name)
        except metadata.PackageNotFoundError:
            errors.append(f"Python依存がありません: {name}=={expected}")
            continue
        if actual != expected:
            errors.append(f"Python依存のVersionが異なります: {name}: {actual}（必要: {expected}）")
        module = PYTHON_IMPORTS[name]
        try:
            import_module(module)
        except Exception as exc:
            # Metadataだけが残った環境や、推移的依存・本体の破損も集約して報告する。
            errors.append(f"Python依存をimportできません: {module}: {type(exc).__name__}: {exc}")

    package = json.loads((root / "package.json").read_text(encoding="utf-8"))
    lock = json.loads((root / "package-lock.json").read_text(encoding="utf-8"))
    for name in package.get("devDependencies", {}):
        expected = lock["packages"][f"node_modules/{name}"]["version"]
        path = root / "node_modules" / name / "package.json"
        if not path.is_file():
            errors.append(f"Node.js依存がありません: {name}@{expected}")
            continue
        actual = json.loads(path.read_text(encoding="utf-8")).get("version")
        if actual != expected:
            errors.append(f"Node.js依存のVersionが異なります: {name}: {actual}（必要: {expected}）")

    node = shutil.which("node")
    if node is None:
        errors.append("Node.jsが見つかりません。CIと同じNode.js 24の環境を準備してください。")
    elif (root / "node_modules/@adguard/aglint/package.json").is_file():
        try:
            result = subprocess.run(
                [node, "--disable-proto=throw",
                 str(root / "node_modules/@adguard/aglint/dist/index.cli.js"), "--version"],
                cwd=root, capture_output=True, text=True, timeout=20,
            )
            if result.returncode:
                errors.append("AGLintを起動できません。推移的依存を含めてnpm ciで再導入してください。")
        except (OSError, subprocess.TimeoutExpired) as exc:
            errors.append(f"AGLintの起動検査を実行できません: {exc}")
    return errors


def main() -> int:
    try:
        errors = check_environment(ROOT)
    except (OSError, ValueError, KeyError) as exc:
        print(f"依存設定を確認できません: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("ローカル検証の準備が不足しています。Lint・Testは開始しません。", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"使用中のPython: {sys.executable}", file=sys.stderr)
        print("RepositoryルートでPython仮想環境を有効にし、次を実行してください。", file=sys.stderr)
        print("  python -m pip install -r requirements-ci.txt", file=sys.stderr)
        print("  npm ci --cache /tmp/prototype-npm-cache", file=sys.stderr)
        return 1
    print("ローカル検証の事前確認に合格: Python依存、Node.js依存、AGLintの起動")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
