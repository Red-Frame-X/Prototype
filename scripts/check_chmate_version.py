#!/usr/bin/env python3
"""ChMateの内容変更とVersionをindex / Commit日時のJSTで検証する。"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime

from update_version_timestamps import CHMATE_FILE, JST, STATE_FILE, chmate_version, version_text


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], text=True, encoding='utf-8')


def show(ref: str, path=CHMATE_FILE) -> str | None:
    result = subprocess.run(['git', 'show', f'{ref}:{path.as_posix()}'],
                            capture_output=True, text=True, encoding='utf-8')
    return result.stdout if result.returncode == 0 else None


def check(before: str | None, after: str | None, reference: datetime,
          checkpoint: str | None = None, *, automated_sync: bool = False) -> None:
    if before == after:
        if after is not None:
            chmate_version(after)
        return
    if after is None:
        raise ValueError('対象ファイルが削除されています')
    stamp = chmate_version(after)
    actual = datetime.strptime(stamp, '%Y%m%d%H%M').replace(tzinfo=JST)
    normalized = version_text(CHMATE_FILE, after, '<VERSION>')
    body_changed = before is None or normalized != version_text(CHMATE_FILE, before, '<VERSION>')
    if before is not None and body_changed:
        if chmate_version(before) == stamp and stamp != reference.astimezone(JST).strftime('%Y%m%d%H%M'):
            raise ValueError('内容が変更されていますがVersionが更新されていません')
    if before is not None and not body_changed:
        # チェックポイントの古さだけではVersion単独更新を正当化できない。
        # 同期Script自身が生成したCommitで、かつ未同期ハッシュがある場合だけ許容する。
        state = json.loads(checkpoint) if checkpoint else {}
        digest = hashlib.sha256(normalized.encode('utf-8')).hexdigest()
        if not automated_sync or state.get(CHMATE_FILE.as_posix()) == digest:
            raise ValueError('内容変更のない不要なVersion更新です')
    delta = (reference.astimezone(JST) - actual).total_seconds()
    if not -60 < delta < 300:
        raise ValueError(f'Version {stamp} は更新時刻のJSTと一致しません '
                         f'（基準 {reference.astimezone(JST).isoformat()}、許容5分未満）')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--base')
    mode.add_argument('--staged', action='store_true')
    parser.add_argument('--head', default='HEAD')
    args = parser.parse_args()
    failed = False
    if args.staged:
        comparisons = [('index', 'HEAD', '', datetime.now(JST))]
    else:
        comparisons = []
        for commit in git('rev-list', '--reverse', f'{args.base}..{args.head}').splitlines():
            parents = git('show', '-s', '--format=%P', commit).split()
            if len(parents) > 1 and any(show(commit) == show(parent) for parent in parents):
                continue
            reference = datetime.fromisoformat(git('show', '-s', '--format=%cI', commit).strip())
            comparisons.append((commit[:12], f'{commit}^', commit, reference))
    for label, base, head, reference in comparisons:
        try:
            message = git('show', '-s', '--format=%s', head).strip() if head else ''
            automated_sync = message in {
                'chore: Versionの日時を日本標準時で同期',
                'NG Word Regex for ChMate のVersionを更新',
            }
            check(show(base), show(head), reference, show(base, STATE_FILE),
                  automated_sync=automated_sync)
        except (ValueError, TypeError) as error:
            print(f'エラー: {label}: {CHMATE_FILE}: {error}。'
                  '内容変更と同じCommitに現在のJSTの ! Version: YYYYMMDDHHMM を含めてください。', file=sys.stderr)
            failed = True
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
