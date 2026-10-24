#!/usr/bin/env python3
"""ルール変更コミットのAdGuardフィルターのVersionメタデータを検証する。"""
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
JST = ZoneInfo("Asia/Tokyo")
TARGETS = (
    Path("AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt"),
    Path("AdGuard Custom Rules/AdGuard DNS Custom Rules - Red Frame X.txt"),
)
VERSION_RE = re.compile(r"(?m)^! Version:\s*(\d{12})\s*$")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8")


def show(ref: str, path: Path) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path.as_posix()}"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return proc.stdout if proc.returncode == 0 else None


def version(text: str, path: Path) -> str:
    matches = VERSION_RE.findall(text)
    if len(matches) != 1:
        raise ValueError(f"{path}: ! Version: YYYYMMDDHHMMヘッダーが正確に1つ必要です")
    stamp = matches[0]
    try:
        datetime.strptime(stamp, "%Y%m%d%H%M").replace(tzinfo=JST)
    except ValueError as exc:
        raise ValueError(f"{path}: 日本標準時のVersion日時が不正です: {stamp}") from exc
    return stamp


def rules_without_version(text: str) -> str:
    return VERSION_RE.sub("! Version: <VERSION>", text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    # 範囲の最終差分だけでなく、各コミットと第一親を比較する。
    # パスによる履歴簡略化を避け、途中の違反が後続コミットで隠れないようにする。
    commits = git("rev-list", "--reverse", f"{args.base}..{args.head}").splitlines()
    failed = False
    for commit in commits:
        for path in TARGETS:
            before = show(f"{commit}^", path)
            after = show(commit, path)
            if before is None or after is None or before == after:
                continue

            try:
                old_version = version(before, path)
                new_version = version(after, path)
            except ValueError as exc:
                print(f"エラー: {exc}")
                failed = True
                continue

            rules_changed = rules_without_version(before) != rules_without_version(after)
            if rules_changed and old_version == new_version:
                print(
                    f"エラー: {commit[:12]}: {path}: ルールが変更されていますが、! Version:が更新されていません "
                    f"（同じコミット内での更新が必要: {old_version})"
                )
                failed = True
            elif rules_changed:
                print(f"正常: {path}: ルールとVersionが同時に変更されています（{old_version} -> {new_version})")
            else:
                print(f"正常: {path}: Versionメタデータだけが変更されています")

    # 各コミット検査に加え、範囲全体の最終状態も比較する。
    # 途中で Version を更新した後、後続コミットで Version だけ古い値へ戻すケースを見逃さない。
    for path in TARGETS:
        before = show(args.base, path)
        after = show(args.head, path)
        if before is None or after is None or before == after:
            continue

        try:
            old_version = version(before, path)
            new_version = version(after, path)
        except ValueError as exc:
            print(f"エラー: {exc}")
            failed = True
            continue

        rules_changed = rules_without_version(before) != rules_without_version(after)
        if rules_changed and old_version == new_version:
            print(
                f"エラー: {path}: 次の範囲でルールが異なります: {args.base}と{args.head}。"
                f"! Version:が変更されていません（{old_version})"
            )
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
