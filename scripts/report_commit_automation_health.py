#!/usr/bin/env python3
"""定期実行の実測と、失敗時の重複しない保守引き継ぎ。コードは変更しない。"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

from automate_japanese_commits import AutomationError, GitHub

WORKFLOW = '.github/workflows/japanese-commits.yml'
MARKER = 'commit-ja-maintenance:v1'
SOURCE_FILES = (
    WORKFLOW, 'scripts/automate_japanese_commits.py',
    'scripts/argos_commit_translation.py', 'scripts/check_argos_model_cache.py',
    'scripts/report_commit_automation_health.py', 'requirements-ci.txt',
    'requirements-translation.txt', '.github/argos-model.json',
)


def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')).timestamp()


def cadence_report(runs, branch, now):
    # 再実行で成功した結果を、自然な定期実行での復旧と混同しない。
    samples = {}
    for run in runs:
        if (run['event'] == 'schedule' and run['path'] == WORKFLOW
                and run['head_branch'] == branch and run['run_attempt'] == 1
                and now - 86400 <= timestamp(run['created_at']) <= now):
            samples[run['id']] = run
    ordered = sorted(samples.values(), key=lambda run: (run['created_at'], run['id']))
    intervals = [timestamp(right['created_at']) - timestamp(left['created_at'])
                 for left, right in zip(ordered, ordered[1:])]
    age = now - timestamp(ordered[-1]['created_at']) if ordered else None
    state = 'INSUFFICIENT_SAMPLES'
    if len(ordered) >= 3:
        state = 'OBSERVED' if max(intervals) <= 600 and age <= 600 else 'DELAYED'
    if age is not None and age > 600:
        state = 'DELAYED'
    return {'state': state, 'configured_interval_seconds': 300,
            'observation_window_seconds': 86400, 'warning_threshold_seconds': 600,
            'sample_count': len(ordered), 'interval_seconds': intervals,
            'latest_age_seconds': age,
            'runs': [{'id': run['id'], 'sha': run['head_sha'],
                      'created_at': run['created_at'], 'status': run['status'],
                      'conclusion': run['conclusion']} for run in ordered]}


def collect_cadence(gh, now):
    repo = gh.api('')
    response = gh.api('/actions/workflows/japanese-commits.yml/runs?event=schedule&per_page=100')
    report = cadence_report(response['workflow_runs'], repo['default_branch'], now)
    # 取得範囲を隠さず、100件の外まで調べたと主張しない。
    report['history_truncated'] = response['total_count'] > len(response['workflow_runs'])
    return report


def maintenance_fingerprint(root):
    digest = hashlib.sha256()
    for name in SOURCE_FILES:
        digest.update(name.encode() + b'\0' + (root / name).read_bytes() + b'\0')
    return digest.hexdigest()


def maintenance_issue(gh, root, run_id, source_sha, diagnostic_result):
    if not re.fullmatch(r'[1-9][0-9]*', run_id):
        raise AutomationError('Run IDが不正です。')
    if not re.fullmatch(r'[0-9a-f]{40}', source_sha):
        raise AutomationError('診断対象SHAが不正です。')
    if diagnostic_result not in {'success', 'failure', 'cancelled', 'skipped'}:
        raise AutomationError('診断状態が不正です。')
    if gh.api('')['private'] is not False:
        raise AutomationError('追加料金を避けるため、公開Repository以外では引き継ぎを停止します。')
    key = maintenance_fingerprint(root)
    marker = f'<!-- {MARKER} {key} -->'
    # Closedも確認し、解決済みの同じ実装でIssueを再作成しない。
    # 全件取得不能・API失敗時には作成せず停止する。POSTは自動再送しない。
    issues = gh.pages('/issues?state=all&creator=github-actions%5Bbot%5D')
    for issue in issues:
        if (not issue.get('pull_request') and marker in (issue.get('body') or '')
                and issue['user']['login'] == 'github-actions[bot]'
                and issue['user']['type'] == 'Bot'):
            return {'state': 'EXISTING', 'number': issue['number'], 'url': issue['html_url']}
    url = f'https://github.com/{gh.repository}/actions/runs/{run_id}'
    body = (f'{marker}\n\nCommit日本語化の自動処理が失敗しました。\n\n'
            f'- Run: {url}\n- 診断対象SHA: `{source_sha}`\n'
            f'- 保守診断Jobの結果: `{diagnostic_result}`\n\n'
            '診断成功は元の障害の解消を意味しません。診断失敗もコード不具合と断定せず、'
            '依存導入・通信・構文・TestのどのStepが失敗したかを確認してください。\n\n'
            '再現手順: `python -m pip install -r requirements-ci.txt`、'
            '`python -m py_compile scripts/automate_japanese_commits.py '
            'scripts/argos_commit_translation.py`、'
            '`python -m unittest discover -s tests -p "test_*commit*.py" -v`。\n\n'
            '元のRunの失敗ログと診断Artifactを確認し、原因を分類してください。'
            '一時障害は既存の上限付きRetryと次回の状態再評価に委ねます。'
            '権限・Review・競合は回避せず停止します。コード修正が必要なら最小修正と'
            '回帰Testを通常のPRへ提出し、Review・最新SHAのCI・Squash Merge・'
            'マージ後の独立CIを確認してください。\n\n'
            'このIssueは修復作業への引き継ぎです。有料AI、コードの自動生成・実行、'
            '自動再実行、無検証のマージは起動しません。'
            '同じ実装ではIssueを重複作成せず、Closedでも再作成しません。')
    issue = gh.api('/issues', 'POST', {
        'title': f'Commit日本語化の失敗を調査・修復する（{key[:12]}）', 'body': body})
    return {'state': 'CREATED', 'number': issue['number'], 'url': issue['html_url']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('cadence', 'maintenance'))
    parser.add_argument('--diagnostic-result', default='skipped')
    args = parser.parse_args()
    gh = GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])
    if args.mode == 'cadence':
        report = collect_cadence(gh, datetime.now(timezone.utc).timestamp())
    else:
        root = Path(__file__).resolve().parents[1]
        sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        report = maintenance_issue(gh, root, os.environ['GITHUB_RUN_ID'], sha,
                                   args.diagnostic_result)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output)
    if summary := os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write(f'### Commit日本語化: {args.mode}\n\n```json\n{output}\n```\n')
    if args.mode == 'cadence' and report['state'] != 'OBSERVED':
        print('::warning::定期実行の実測が不足、または10分超の遅延があります。5分間隔の正常動作とは扱いません。')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
