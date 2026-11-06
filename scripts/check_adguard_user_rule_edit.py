#!/usr/bin/env python3
"""標準AdGuardユーザールール編集前の安全チェックを行う。"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"
APPROVALS = ROOT / "config" / "adguard-rule-removal-approvals.json"


def rules_sha256(text: str) -> str:
    return hashlib.sha256("\n".join(sorted(active_rules(text))).encode("utf-8")).hexdigest()


def parse_approvals(raw: str) -> dict[str, list[str]]:
    try:
        data = json.loads(raw)
        if not isinstance(data, dict) or type(data.get("version")) is not int or data["version"] != 1 or not isinstance(data.get("approvals"), list):
            raise ValueError("version: 1 と approvals 配列が必要です")
        entries = {}
        for entry in data["approvals"]:
            if not isinstance(entry, dict):
                raise ValueError("承認はオブジェクトで指定してください")
            stamp = entry.get("rules_sha256")
            rules = entry.get("rules")
            if not isinstance(stamp, str) or len(stamp) != 64 or any(c not in "0123456789abcdef" for c in stamp):
                raise ValueError("rules_sha256 は64桁の小文字16進数で指定してください")
            if not isinstance(rules, list) or not rules or any(
                not isinstance(rule, str) or active_rules(rule) != [rule] for rule in rules
            ):
                raise ValueError("rules は削除対象の有効ルールを正確に指定してください")
            if any(not isinstance(entry.get(key), str) or not entry[key].strip() for key in ("reason", "reference")):
                raise ValueError("reason と reference が必要です")
            if stamp in entries:
                raise ValueError("同じ rules_sha256 に複数の承認があります")
            entries[stamp] = rules
        return entries
    except (ValueError, TypeError) as exc:
        fail(f"AdGuardルール削除承認が不正です: {exc}")


def approved_removals(base_ref: str, base: str) -> list[str]:
    # PR側のファイルではなく、比較元に収録された承認だけを参照する。
    raw = git_show(base_ref, APPROVALS)
    return parse_approvals(raw).get(rules_sha256(base), []) if raw is not None else []


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
    parser.add_argument("--print-rules-sha256", action="store_true", help="有効ルール群の承認用SHA-256を表示します")
    parser.add_argument(
        "--allow-rule-removal",
        action="append",
        default=[],
        metavar="RULE",
        help="削除する有効ルールを正確に1件指定して明示的に許可します。複数件は繰り返し指定します。",
    )
    args = parser.parse_args()

    text = read(FILTER)
    current_approvals = parse_approvals(read(APPROVALS)) if APPROVALS.exists() else {}
    lines = text.splitlines()

    trailing = [i for i, line in enumerate(lines, 1) if line.rstrip() != line]
    if trailing:
        fail(f"末尾に空白がある行: {', '.join(map(str, trailing[:10]))}")

    rules = active_rules(text)
    duplicates = sorted(rule for rule, count in Counter(rules).items() if count > 1)
    if duplicates:
        sample = "\n".join(f"  {rule}" for rule in duplicates[:10])
        fail(f"有効ルールの重複を検出しました:\n{sample}")

    if args.print_rules_sha256:
        print(rules_sha256(text))
        return 0

    if args.base_ref:
        base = git_show(args.base_ref, FILTER)
        if base is None:
            fail(f"比較元の標準フィルターを取得できません: {args.base_ref}")
        if base is not None:
            if base.endswith("\n") and not text.endswith("\n"):
                fail("編集により標準フィルターの末尾改行が削除されました")

            before = active_rules(base)
            before_counts = Counter(before)
            after_counts = Counter(rules)
            removed_counts = before_counts - after_counts
            removed_rules = sorted(removed_counts.elements())

            recorded = approved_removals(args.base_ref, base)
            allowed_counts = Counter(args.allow_rule_removal)
            if removed_counts:
                # 承認登録だけのPRは許可し、実際の削除では承認対象の完全一致を要求する。
                allowed_counts |= Counter(recorded)
                if recorded and rules_sha256(base) in current_approvals:
                    fail("使用した削除承認を同じ変更内で削除してください。承認の再利用は許可しません")
            unauthorized = sorted((removed_counts - allowed_counts).elements())
            overauthorized = sorted((allowed_counts - removed_counts).elements())

            if unauthorized:
                sample = "\n".join(f"  {rule}" for rule in unauthorized[:10])
                fail(
                    "対象を正確に指定した明示的な承認がないAdGuard有効ルールの削除を検出しました "
                    f"({len(unauthorized)}件）。意図しない内容消失の可能性があります:\n{sample}\n"
                    "依頼されたルールの削除だけを許可するには、繰り返し指定する"
                    "--allow-rule-removal RULE引数で対象を正確に指定してください。\n"
                    "CIでの削除には、比較元のconfig/adguard-rule-removal-approvals.jsonへ"
                    "先に承認を記録してください。手順はAdGuard Custom Rules/README.mdを参照してください。"
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
