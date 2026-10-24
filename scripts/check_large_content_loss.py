#!/usr/bin/env python3
"""保護対象の利用者向けコンテンツが意図せず大幅に減少した場合にCIを失敗させる。"""
from __future__ import annotations

import argparse
import subprocess
import sys

DEFAULT_MAX_DELETIONS = 200
DEFAULT_MAX_NET_LOSS = 120
DEFAULT_MIN_RETAINED_RATIO = 0.25
PROTECTED_SUFFIXES = (".md", ".txt", ".js", ".json")
EXCLUDED_PREFIXES = (".github/", "scripts/", "tests/")


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def parse_numstat(text: str):
    records = iter(text.split("\0"))
    for record in records:
        if not record:
            continue
        added, deleted, path = record.split("\t", 2)
        before_path = path
        # 改名・コピーでは空のパスに続き、NUL区切りのパスが2つ現れる。
        # バイナリー項目でも両方を読み取り、次のレコードとの対応を保つ。
        if not path:
            before_path = next(records)
            path = next(records)
        if added == "-" or deleted == "-":
            continue
        yield int(added), int(deleted), path, before_path


def line_count(ref: str, path: str) -> int | None:
    try:
        content = run_git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None
    return len(content.splitlines())


def changed_text_files(base_ref: str) -> list[tuple[int, int, str, str]]:
    diff = run_git(
        "diff",
        "--numstat",
        "-z",
        f"{base_ref}...HEAD",
        "--",
        "*.md",
        "*.txt",
        "*.js",
        "*.json",
    )
    return list(parse_numstat(diff))


def is_protected_path(path: str) -> bool:
    return path.endswith(PROTECTED_SUFFIXES) and not path.startswith(EXCLUDED_PREFIXES)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--max-deletions", type=int, default=DEFAULT_MAX_DELETIONS)
    parser.add_argument("--max-net-loss", type=int, default=DEFAULT_MAX_NET_LOSS)
    parser.add_argument("--min-retained-ratio", type=float, default=DEFAULT_MIN_RETAINED_RATIO)
    parser.add_argument(
        "--allow-deletion-in",
        action="append",
        default=[],
        metavar="PATH",
        help="レビュー済みの大量削除を、保護対象の正確なパスを指定して明示的に許可します。必要に応じて繰り返し指定します。",
    )
    args = parser.parse_args()

    allowed_paths = set(args.allow_deletion_in)
    changes = changed_text_files(args.base_ref)
    protected_changes = [
        change for change in changes
        if is_protected_path(change[2]) or is_protected_path(change[3])
    ]
    failures: list[str] = []

    for added, deleted, path, before_path in protected_changes:
        net_loss = deleted - added
        before_lines = line_count(args.base_ref, before_path)
        after_lines = line_count("HEAD", path)

        # 通常の編集や書き換えでも既存行は置き換わる。この検査では、
        # 大規模な置換そのものではなく、内容の大幅な純減を防止する。
        # 意図した大量削除には厳密なパス指定による承認を使えるが、
        # その場合も内容の保持率に関する保護は省略しない。
        if after_lines is None:
            if path not in allowed_paths:
                failures.append(
                    f"{path}: ファイルが削除されました（+{added}/-{deleted}）。保護対象ファイルの削除は明示的に承認されていません。"
                    "ユーザーが依頼した削除に限り、--allow-deletion-inにこの正確なパスを指定してください。"
                )
            continue

        if before_lines and after_lines / before_lines < args.min_retained_ratio:
            failures.append(
                f"{path}: +{added}/-{deleted}（純減 {net_loss}）、"
                f"保持行数 {after_lines}/{before_lines}行 "
                f"（{after_lines / before_lines:.1%}）。"
                "大量の内容削除には、自動マージの前に明示的なレビューが必要です。"
            )
            continue

        if path in allowed_paths:
            continue

        if net_loss >= args.max_net_loss:
            failures.append(
                f"{path}: +{added}/-{deleted}（純減 {net_loss}）、"
                f"純減がレビュー基準に達しています: {args.max_net_loss}。"
                "大量の内容削除には、自動マージの前に明示的なレビューが必要です。"
            )

    stale_authorizations = sorted(
        path
        for path in allowed_paths
        if not any(changed_path == path and deleted > 0 for _, deleted, changed_path, _ in protected_changes)
    )
    if stale_authorizations:
        failures.append(
            "削除承認が実際の保護対象コンテンツの削除と一致しません: "
            + ", ".join(stale_authorizations)
        )

    if failures:
        print("意図しない内容消失の可能性を検出しました:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("内容消失防止検査に合格: 保護対象に未承認の大幅な内容減少はありません。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
