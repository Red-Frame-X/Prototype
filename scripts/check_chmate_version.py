#!/usr/bin/env python3
"""ChMateの内容変更とVersionをindex / Commit日時のJSTで検証する。"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import urllib.request
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
    old_stamp = None
    if before is not None:
        try:
            old_stamp = chmate_version(before)
        except ValueError:
            # mainに入った不正なMetadataを、正常な現在の日時へ修復できるようにする。
            pass
    body_changed = old_stamp is None or normalized != version_text(CHMATE_FILE, before, '<VERSION>')
    if before is not None and body_changed:
        if old_stamp == stamp and stamp != reference.astimezone(JST).strftime('%Y%m%d%H%M'):
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


def synchronized_commit(commit: str) -> bool:
    """Botの同期Commitは、更新後の内容チェックポイントも同時に必要。"""
    if git('show', '-s', '--format=%cn <%ce>', commit).strip() != (
        'github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>'
    ):
        return False
    after = show(commit)
    state = show(commit, STATE_FILE)
    if after is None or state is None:
        return False
    digest = hashlib.sha256(version_text(CHMATE_FILE, after, '<VERSION>').encode()).hexdigest()
    return json.loads(state).get(CHMATE_FILE.as_posix()) == digest


def merged_pr_source(commit: str) -> tuple[str, str] | None:
    """GitHubが記録したMerge SHAと、元PRのTXTが一致する場合だけ元履歴を返す。"""
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Squash元を確認するGITHUB_REPOSITORYが不正です')
    request = urllib.request.Request(
        f'https://api.github.com/repos/{repository}/commits/{commit}/pulls?per_page=100',
        headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                 'Accept': 'application/vnd.github+json'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        prs = json.load(response)
    for pr in prs:
        if (not pr.get('merged_at') or pr.get('merge_commit_sha') != commit
                or pr['base']['repo']['full_name'] != repository):
            continue
        base, head = pr['base']['sha'], pr['head']['sha']
        if not all(re.fullmatch(r'[0-9a-f]{40}', sha) for sha in (base, head)):
            raise ValueError('Squash元PRのSHAが不正です')
        for sha in (base, head):
            git('fetch', '--no-tags', 'origin', sha)
        if show(head) != show(commit):
            raise ValueError('Squash後のTXTが元PRと一致しません')
        parent = git('rev-parse', commit + '^').strip()
        common = git('merge-base', parent, head).strip()
        if show(common) != show(parent):
            raise ValueError('元PRがSquash前のmainのTXT変更を取り込んでいません')
        if head == commit:
            raise ValueError('Squash元と反映後のSHAが同じです')
        return parent, head
    return None


def check_history(base: str, head: str, *, github_provenance: bool = False) -> bool:
    failed = False
    for commit in git('rev-list', '--reverse', f'{base}..{head}').splitlines():
        parents = git('show', '-s', '--format=%P', commit).split()
        if len(parents) > 1 and any(show(commit) == show(parent) for parent in parents):
            continue
        reference = datetime.fromisoformat(git('show', '-s', '--format=%cI', commit).strip())
        try:
            # 許容時間内のSquashでも、元PRの途中の更新漏れを検査する。
            if github_provenance and show(commit + '^') != show(commit):
                source = merged_pr_source(commit)
                if source:
                    if check_history(*source):
                        raise ValueError('Squash元PRのVersion検査に失敗しました')
                    print(f'正常: {commit[:12]}: Squash元PRの内容・全CommitのJST日時を確認しました')
                    continue
            check(show(commit + '^'), show(commit), reference, show(commit + '^', STATE_FILE),
                  automated_sync=synchronized_commit(commit))
        except (ValueError, TypeError, KeyError, OSError, subprocess.CalledProcessError) as error:
            print(f'エラー: {commit[:12]}: {CHMATE_FILE}: {error}。'
                  '内容変更と同じCommitに現在のJSTの ! Version: YYYYMMDDHHMM を含めてください。', file=sys.stderr)
            failed = True
    return failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--base')
    mode.add_argument('--staged', action='store_true')
    parser.add_argument('--head', default='HEAD')
    parser.add_argument('--github-provenance', action='store_true',
                        help='変更CommitをGitHubのマージ済みPRと照合し、Squash元履歴も検査')
    args = parser.parse_args()
    if not args.staged:
        return int(check_history(args.base, args.head, github_provenance=args.github_provenance))
    try:
        check(show('HEAD'), show(''), datetime.now(JST), show('HEAD', STATE_FILE))
    except (ValueError, TypeError) as error:
        print(f'エラー: index: {CHMATE_FILE}: {error}。'
              '現在のJSTのVersionを内容変更と同じCommitに含めてください。', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
