#!/usr/bin/env python3
"""標準AdGuardユーザールール編集前の安全チェックを行う。"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"


def fail(message: str) -> None:
    print(f"エラー: {message}", file=sys.stderr)
    raise SystemExit(1)


def active_rules(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("!")
        and (not line.lstrip().startswith("[") or line.lstrip().startswith("[$"))
    ]


def read(path: Path) -> str:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        fail(f"読み取れません: {path}: {exc}")

    if b"\r" in raw:
        fail("CR文字を検出しました。標準フィルターの改行はLFにしてください")

    try:
        return raw.decode("utf-8-sig")
    except UnicodeError as exc:
        fail(f"デコードできません: {path}（UTF-8）: {exc}")


def git_show(ref: str, path: Path) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    proc = subprocess.run(
        ["git", "show", f"{ref}:{rel}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return proc.stdout if proc.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", default=None)
    parser.add_argument(
        "--allow-rule-removal",
        action="append",
        default=[],
        metavar="RULE",
        help="削除する有効ルールを正確に1件指定して明示的に許可します。複数件は繰り返し指定します。",
    )
    args = parser.parse_args()

    text = read(FILTER)
    lines = text.splitlines()

    trailing = [i for i, line in enumerate(lines, 1) if line.rstrip() != line]
    if trailing:
        fail(f"末尾に空白がある行: {', '.join(map(str, trailing[:10]))}")

    rules = active_rules(text)
    duplicates = sorted(rule for rule, count in Counter(rules).items() if count > 1)
    if duplicates:
        sample = "\n".join(f"  {rule}" for rule in duplicates[:10])
        fail(f"有効ルールの重複を検出しました:\n{sample}")

    if args.base_ref:
        base = git_show(args.base_ref, FILTER)
        if base is not None:
            if base.endswith("\n") and not text.endswith("\n"):
                fail("編集により標準フィルターの末尾改行が削除されました")

            before = active_rules(base)
            before_counts = Counter(before)
            after_counts = Counter(rules)
            removed_counts = before_counts - after_counts
            removed_rules = sorted(removed_counts.elements())

            allowed_counts = Counter(args.allow_rule_removal)
            unauthorized = sorted((removed_counts - allowed_counts).elements())
            overauthorized = sorted((allowed_counts - removed_counts).elements())

            if unauthorized:
                sample = "\n".join(f"  {rule}" for rule in unauthorized[:10])
                fail(
                    "対象を正確に指定した明示的な承認がないAdGuard有効ルールの削除を検出しました "
                    f"({len(unauthorized)}件）。意図しない内容消失の可能性があります:\n{sample}\n"
                    "依頼されたルールの削除だけを許可するには、繰り返し指定する"
                    "--allow-rule-removal RULE引数で対象を正確に指定してください。"
                )

            if overauthorized:
                sample = "\n".join(f"  {rule}" for rule in overauthorized[:10])
                fail(
                    "ルール削除の承認が実際の差分と一致しません:\n"
                    f"{sample}\n"
                    "対象が広すぎる、または古い削除承認は受け付けません。"
                )

            if removed_rules and len(removed_rules) > max(10, len(before) // 4):
                fail(
                    "不審な有効ルールの大量減少を検出しました "
                    f"({len(before)} -> {len(rules)}）。ファイル全体の置換の可能性があります"
                )

            header_before = base.splitlines()[:9]
            header_after = lines[:9]
            stable_prefixes = (
                "! Title:",
                "! Description:",
                "! Syntax:",
                "! Expires:",
                "! Homepage:",
                "! License:",
                "! Note:",
            )
            for prefix in stable_prefixes:
                old = next((x for x in header_before if x.startswith(prefix)), None)
                new = next((x for x in header_after if x.startswith(prefix)), None)
                if old != new:
                    fail(f"保護対象のMetadataに想定外の変更があります: {prefix}")

    print(f"AdGuard編集前検査に合格: {len(rules)}件の有効ルール、重複なし")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
