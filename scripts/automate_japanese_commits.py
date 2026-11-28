#!/usr/bin/env python3
"""PR内のCommitだけを日本語化し、最新SHAのCodex Review・CI成功後にSquashする。"""
from __future__ import annotations

import hashlib
import json
import os
import random
import time
import socket
from email.utils import parsedate_to_datetime
from functools import cache
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

from check_commit_titles import valid_title

STATE_MARKER = 'commit-ja-automation:v1'
CODEX_LOGIN = 'chatgpt-codex-connector[bot]'
BOT_LOGIN = 'github-actions[bot]'
SHA_PATTERN = re.compile(r'^[0-9a-f]{40}$')
JAPANESE = re.compile(r'[ぁ-んァ-ヶ一-龠]')
MAX_COMMITS = 100
MAX_MESSAGE_BYTES = 120_000


class AutomationError(RuntimeError):
    pass


class TranslationSetupError(AutomationError):
    pass


class APIError(AutomationError):
    def __init__(self, message, category):
        super().__init__(message)
        self.category = category


def retry_delay(headers, attempt):
    value = headers.get('Retry-After')
    if value:
        try:
            return max(0, float(value))
        except ValueError:
            try:
                return max(0, parsedate_to_datetime(value).timestamp() - time.time())
            except (ValueError, TypeError, OverflowError):
                pass
    if headers.get('X-RateLimit-Remaining') == '0':
        try:
            return max(0, float(headers['X-RateLimit-Reset']) - time.time())
        except (KeyError, ValueError):
            pass
    return 2 ** attempt + random.uniform(0, 1)


def git(*args: str, data: bytes | None = None) -> bytes:
    return subprocess.check_output(['git', *args], input=data, stderr=subprocess.PIPE)


def request_json(url: str, token: str, method: str = 'GET', data=None):
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json',
               'User-Agent': 'prototype-commit-ja'}
    if urllib.parse.urlsplit(url).hostname == 'api.github.com':
        headers.update({'Accept': 'application/vnd.github+json',
                        'X-GitHub-Api-Version': '2022-11-28'})
    payload = None
    if data is not None:
        payload = json.dumps(data, ensure_ascii=False).encode()
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, headers=headers, data=payload, method=method)
    # GETだけを再送する。書き込みは応答喪失後の重複投稿・マージを防ぐため再送しない。
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                body = response.read()
            return json.loads(body) if body else None
        except urllib.error.HTTPError as error:
            # 認証情報やAPI応答内の入力本文をログに出さない。
            transient = error.code == 429 or error.code in {500, 502, 503, 504}
            category = 'A' if transient else ('B' if error.code == 409 else 'D')
            delay = retry_delay(error.headers, attempt) if transient else 0
            if (error.code == 429 and not error.headers.get('Retry-After')
                    and error.headers.get('X-RateLimit-Remaining') != '0'):
                delay = 60 * (2 ** attempt)

            # 長いRetry-Afterは短縮せず、次回の定期実行へ委ねる。
            if transient and method == 'GET' and attempt < 3 and delay <= 60:
                print(f'RETRY_WAIT: HTTP {error.code}, retry={attempt + 1}/3, wait={delay:.1f}s')
                time.sleep(delay)
                continue
            raise APIError(f'APIがHTTP {error.code}を返しました: {method} '
                           f'{urllib.parse.urlsplit(url).path} (分類{category})', category) from None
        except (urllib.error.URLError, TimeoutError, socket.timeout) as error:
            if method == 'GET' and attempt < 3:
                delay = retry_delay({}, attempt)
                print(f'RETRY_WAIT: 通信失敗, retry={attempt + 1}/3, wait={delay:.1f}s')
                time.sleep(delay)
                continue
            raise APIError('API通信が失敗しました。書き込み結果は最新状態から確認してください。 (分類A)', 'A') from None



class GitHub:
    def __init__(self, repository: str, token: str):
        if not re.fullmatch(r'[\w.-]+/[\w.-]+', repository):
            raise AutomationError('Repository名が不正です。')
        self.repository = repository
        self.token = token
        self.root = f'https://api.github.com/repos/{repository}'

    def api(self, path: str, method='GET', data=None):
        return request_json(self.root + path, self.token, method, data)

    def pages(self, path: str):
        separator = '&' if '?' in path else '?'
        result = []
        for page in range(1, 101):
            items = self.api(f'{path}{separator}per_page=100&page={page}')
            if not isinstance(items, list):
                raise AutomationError('APIの一覧形式が変わったため停止しました。')
            result.extend(items)
            if len(items) < 100:
                return result
        raise AutomationError('APIの一覧が上限を超えたため停止しました。')

    def comment(self, number: int, body: str):
        return self.api(f'/issues/{number}/comments', 'POST', {'body': body})


def fingerprint(sha: str, title: str, body: str) -> str:
    return hashlib.sha256(json.dumps([sha, title, body], ensure_ascii=False).encode()).hexdigest()


def read_state(comments: list[dict]) -> dict:
    for comment in reversed(comments):
        if comment['user']['login'] != BOT_LOGIN or comment['user'].get('type') != 'Bot':
            continue
        match = re.search(r'<!-- ' + STATE_MARKER + r' (\{[^\n]*\}) -->', comment['body'])
        if match:
            try:
                state = json.loads(match[1])
                if isinstance(state, dict):
                    return state
            except json.JSONDecodeError:
                pass
    return {}


def codex_passed(comments: list[dict], sha: str) -> bool:
    # 文面の「問題なし」や絵文字では判定せず、Botの機械可読状態を確認する。
    for comment in reversed(comments):
        if comment['user']['login'] != CODEX_LOGIN or comment['user'].get('type') != 'Bot':
            continue
        match = re.search(r'<!-- codex-review-state:v1 (\{[^\n]*\}) -->', comment['body'])
        if not match:
            continue
        try:
            state = json.loads(match[1])
            review = state['code_review']
            security = state.get('security_review', {})
            code_ok = (review['commit_sha'] == sha and review['status'] == 'completed'
                       and review['has_any_findings'] is False
                       and review['has_unresolved_findings'] is False)
            # Security Reviewが依頼されている場合は、それも完了するまで待つ。
            security_ok = (not security.get('status') or
                           (security.get('commit_sha') == sha
                            and security.get('status') == 'completed'
                            and security.get('has_any_findings') is False
                            and security.get('has_unresolved_findings') is False))
            return code_ok and security_ok
        except (KeyError, TypeError, json.JSONDecodeError):
            return False
    return False


def validate_translation(original: dict, translated: dict) -> dict:
    if not isinstance(translated, dict) or set(translated) != {'title', 'body', 'commits'}:
        raise AutomationError('翻訳結果の形式が不正です。')
    for key in ('title', 'body'):
        if not isinstance(translated[key], str):
            raise AutomationError('翻訳結果に文字列以外が含まれています。')
    if not valid_title(translated['title']) or not JAPANESE.search(translated['title']):
        raise AutomationError('翻訳後のPR titleが日本語の表記方針に適合しません。')
    if '\n' in translated['title'] or len(translated['title']) > 256:
        raise AutomationError('翻訳後のPR titleの長さ・改行が不正です。')
    if len(translated['body']) > 60_000:
        raise AutomationError('翻訳後のPR bodyが長すぎます。')
    commits = translated['commits']
    expected = {item['sha']: item['message'] for item in original['commits']}
    if not isinstance(commits, list) or len(commits) != len(expected):
        raise AutomationError('翻訳結果のCommit数が一致しません。')
    messages = {}
    for item in commits:
        if not isinstance(item, dict) or set(item) != {'sha', 'message'}:
            raise AutomationError('翻訳結果のCommit形式が不正です。')
        sha, message = item['sha'], item['message']
        if not isinstance(sha, str) or sha not in expected or sha in messages:
            raise AutomationError('翻訳結果のSHAに重複・欠落・未知の値があります。')
        if not isinstance(message, str) or not message.strip() or '\x00' in message:
            raise AutomationError('翻訳後のCommit messageが不正です。')
        title = message.splitlines()[0]
        if not valid_title(title) or not JAPANESE.search(title):
            raise AutomationError('翻訳後のCommit titleが日本語の表記方針に適合しません。')
        if len(message.encode()) > 32_000:
            raise AutomationError('翻訳後のCommit messageが長すぎます。')
        messages[sha] = message
    from argos_commit_translation import ACTION_EXPRESSION, HASH_REFERENCE, find_trailer_block
    # URLやIssue参照など、翻訳によって壊してはいけない表記を機械的にも照合する。
    for before, after in [(original['title'], translated['title']),
                          (original['body'], translated['body']),
                          *[(expected[sha], messages[sha]) for sha in expected]]:
        if sorted(ACTION_EXPRESSION.findall(before)) != sorted(ACTION_EXPRESSION.findall(after)):
            raise AutomationError('翻訳結果でGitHub Actionsの式が変更されました。')
        trailer = find_trailer_block(before)
        if trailer:
            restored = find_trailer_block(after)
            if restored is None or before[trailer.start(1):] != after[restored.start(1):]:
                raise AutomationError('翻訳結果でGit trailerが変更されました。')
        for pattern in (r'https?://[^\s<>\)]+', r'(?<!\w)#\d+\b', r'`[^`\n]+`', HASH_REFERENCE.pattern):
            if sorted(re.findall(pattern, before)) != sorted(re.findall(pattern, after)):
                raise AutomationError('翻訳結果でURL・Issue参照・Code span・Commit hashが変更されました。')
    return {**translated, 'messages': messages}


@cache
def install_translation_dependencies() -> bool:
    # 固定の依存関係だけを導入し、PR処理用のTokenをpipへ渡さない。
    env = os.environ.copy()
    env.pop('GH_TOKEN', None)
    pip = [sys.executable, '-m', 'pip', 'install', '--disable-pip-version-check']
    torch = subprocess.run(
        pip + ['torch==2.9.1+cpu', '--index-url', 'https://download.pytorch.org/whl/cpu'],
        env=env, check=False,
    )
    if torch.returncode:
        return False
    requirements = subprocess.run(pip + ['-r', 'requirements-translation.txt'], env=env, check=False)
    return requirements.returncode == 0


def translate(original: dict) -> dict:
    from argos_commit_translation import load_engine, translate_payload, TranslationError
    if len(json.dumps(original, ensure_ascii=False).encode()) > MAX_MESSAGE_BYTES:
        raise AutomationError('翻訳対象が上限を超えました。内容を省略せず停止します。')
    engine = None
    setup_failure = None
    def translate_segment(source):
        nonlocal engine, setup_failure
        if engine is None:
            try:
                if (os.environ.get('COMMIT_JA_INSTALL_TRANSLATION_DEPS') == 'true'
                        and not install_translation_dependencies()):
                    raise TranslationError('Argos Translateの依存関係をインストールできませんでした。')
                engine = load_engine()
            except TranslationError as error:
                setup_failure = str(error)
                raise
        return engine(source)
    try:
        translated = translate_payload(original, translate_segment)
    except TranslationError as error:
        if setup_failure is not None:
            raise TranslationSetupError(setup_failure) from None
        raise AutomationError(str(error)) from None
    return validate_translation(original, translated)


def translation_approved(gh: GitHub, comments: list[dict], current: str) -> bool:
    # 完全一致の承認だけを認め、引用・Bot・過去のSHA/PR説明への承認は使わない。
    command = '/approve-commit-translation ' + current
    for comment in reversed(comments):
        if comment['user'].get('type') != 'User' or comment['body'].strip() != command:
            continue
        login = urllib.parse.quote(comment['user']['login'], safe='')
        if gh.api(f'/collaborators/{login}/permission')['permission'] in {'admin', 'maintain', 'write'}:
            return True
    return False


def rewrite_commits(base: str, head: str, messages: dict[str, str]) -> tuple[str, dict]:
    """CheckoutせずGit objectを書き換え、全tree・著者・日時・順序を照合する。"""
    for sha in (base, head):
        if not SHA_PATTERN.fullmatch(sha):
            raise AutomationError('Commit SHAが不正です。')
    commits = git('rev-list', '--reverse', '--topo-order', f'{base}..{head}').decode().splitlines()
    if set(commits) != set(messages) or not commits or len(commits) > MAX_COMMITS:
        raise AutomationError('翻訳対象と実際のPR Commitが一致しません。')
    mapping = {}
    for sha in commits:
        raw = git('cat-file', 'commit', sha)
        header, old_message = raw.split(b'\n\n', 1)
        message = messages[sha].encode()
        # APIの文字列化で末尾改行だけが失われた場合、既存objectを保持する。
        if message.rstrip(b'\n') == old_message.rstrip(b'\n'):
            message = old_message
        elif not message.endswith(b'\n'):
            message += b'\n'
        parents_changed = any(line.startswith(b'parent ') and
                              mapping.get(line[7:].decode(), line[7:].decode()) != line[7:].decode()
                              for line in header.split(b'\n'))
        if message == old_message and not parents_changed:
            mapping[sha] = sha
            continue
        lines = []
        skipping_signature = False
        for line in header.split(b'\n'):
            if line.startswith((b'gpgsig ', b'gpgsig-sha256 ')):
                skipping_signature = True
                continue
            if skipping_signature and line.startswith(b' '):
                continue
            skipping_signature = False
            if line.startswith(b'parent '):
                parent = line[7:].decode()
                line = b'parent ' + mapping.get(parent, parent).encode()
            lines.append(line)
        new_raw = b'\n'.join(lines) + b'\n\n' + message
        new_sha = git('hash-object', '-t', 'commit', '-w', '--stdin', data=new_raw).decode().strip()
        if git('cat-file', 'commit', new_sha) != new_raw:
            raise AutomationError('Commit objectの書き込み検証が失敗しました。')
        if git('rev-parse', sha + '^{tree}') != git('rev-parse', new_sha + '^{tree}'):
            raise AutomationError('Commitのファイル内容が変わったため停止しました。')
        mapping[sha] = new_sha
    if git('diff', '--raw', head, mapping[head]):
        raise AutomationError('PR先端のファイル内容が変わったため停止しました。')
    return mapping[head], mapping


def eligible(pr: dict, repository: str, default_branch: str) -> bool:
    return (pr['state'] == 'open' and not pr['draft']
            and (pr['head'].get('repo') or {}).get('full_name') == repository
            and pr['base']['repo']['full_name'] == repository
            and pr['base']['ref'] == default_branch
            and pr['head']['ref'] != default_branch)


def reviews_clear(reviews: list[dict]) -> bool:
    latest = {}
    for review in reviews:
        if review['state'] == 'PENDING':
            return False
        if review['state'] != 'COMMENTED' and review['state'] != 'PENDING':
            latest[review['user']['login']] = review['state']
    return 'CHANGES_REQUESTED' not in latest.values()


def threads_clear(gh: GitHub, number: int) -> bool:
    owner, name = gh.repository.split('/')
    cursor = None
    while True:
        result = request_json('https://api.github.com/graphql', gh.token, 'POST', {
            'query': '''query($owner:String!,$name:String!,$number:Int!,$cursor:String) {
              repository(owner:$owner,name:$name) { pullRequest(number:$number) {
                reviewThreads(first:100,after:$cursor) {
                  nodes { isResolved } pageInfo { hasNextPage endCursor }
                }
              }}
            }''',
            'variables': {'owner': owner, 'name': name, 'number': number, 'cursor': cursor},
        })
        if result.get('errors'):
            raise AutomationError('Review threadの確認に失敗しました。')
        threads = result['data']['repository']['pullRequest']['reviewThreads']
        if any(not node['isResolved'] for node in threads['nodes']):
            return False
        if not threads['pageInfo']['hasNextPage']:
            return True
        cursor = threads['pageInfo']['endCursor']


def quality_run(gh: GitHub, sha: str, branch: str, number: int):
    query = urllib.parse.urlencode({'head_sha': sha, 'branch': branch,
                                    'event': 'workflow_dispatch', 'per_page': 100})
    runs = gh.api('/actions/workflows/quality.yml/runs?' + query)['workflow_runs']
    # run-nameは信頼するquality.ymlがautomation_pr入力から生成する。
    # 同じSHAの通常の手動実行は、PR全体の検証を含まないため採用しない。
    expected_title = f'PR #{number} 日本語化検証 {sha}'
    return next((run for run in runs if run['head_sha'] == sha and run['head_branch'] == branch
                 and run['display_title'] == expected_title), None)


def all_checks_passed(gh: GitHub, sha: str) -> bool:
    # 同名Checkの再実行は最新だけを確認する。少なくとも品質検査自体は別途必須。
    query = urllib.parse.urlencode({'filter': 'latest', 'per_page': 100})
    response = gh.api(f'/commits/{sha}/check-runs?{query}')
    if response['total_count'] > 100:
        raise AutomationError('Check数が上限を超えたため停止しました。')
    for check in response['check_runs']:
        if check['status'] != 'completed' or check['conclusion'] not in {'success', 'neutral', 'skipped'}:
            return False
    statuses = gh.api(f'/commits/{sha}/status')
    return statuses['total_count'] == 0 or statuses['state'] == 'success'


def save_state(gh: GitHub, number: int, state: dict, text: str):
    gh.comment(number, text + '\n\n<!-- ' + STATE_MARKER + ' '
               + json.dumps(state, ensure_ascii=False, separators=(',', ':')) + ' -->')


def perform_once(gh: GitHub, number: int, state: dict, key: str, send):
    """POSTの前に意図を永続化する。結果不明の書き込みは再送しない。"""
    intents = state.setdefault('intents', {})
    previous = intents.get(key)
    if previous:
        if time.time() - previous['at'] < 300:
            print(f'PR #{number}: 書き込み結果の反映を待機しています。処理: {key}')
            return False
        raise AutomationError('書き込みの意図は記録済みですが結果を確認できません。'
                              '重複を防ぐため再送しません。GitHubの実状態を手動確認してください。'
                              f' 処理: {key}')
    intents[key] = {'at': time.time(), 'status': 'reserved'}
    save_state(gh, number, state, f'外部書き込みの意図を記録しました。処理: {key}')
    send()
    intents[key]['status'] = 'sent'
    save_state(gh, number, state, f'外部書き込みの要求が受け付けられました。結果は別途確認します。処理: {key}')
    return True


def review_observed(comments, sha):
    marker = f'<!-- commit-ja-review-request:{sha} -->'
    for comment in comments:
        user = comment['user']
        if user.get('type') != 'Bot':
            continue
        if user['login'] == BOT_LOGIN and marker in comment['body']:
            return True
        if user['login'] == CODEX_LOGIN:
            match = re.search(r'<!-- codex-review-state:v1 (\{[^\n]*\}) -->', comment['body'])
            if match:
                try:
                    observed = json.loads(match[1])
                    review = observed.get('code_review') if isinstance(observed, dict) else None
                    if isinstance(review, dict) and review.get('commit_sha') == sha:
                        return True
                except (TypeError, json.JSONDecodeError):
                    pass
    return False


def verify_merged_pr(gh: GitHub, pr: dict, dry_run: bool = False):
    """閉じたPRも記録済みのmerge SHAに結び付く独立CIだけで検証する。"""
    if dry_run or not pr.get('merged'):
        return
    number = pr['number']
    state = read_state(gh.pages(f'/issues/{number}/comments'))
    if state.get('phase') == 'MERGE_READY':
        sha = pr.get('merge_commit_sha')
        if (not SHA_PATTERN.fullmatch(sha or '')
                or pr['head']['sha'] != state.get('sha')):
            raise AutomationError('マージ要求後のPRと記録済みHead SHAが一致しません。')
        merged = gh.api('/git/commits/' + sha)
        digest = hashlib.sha256(merged['message'].rstrip('\n').encode()).hexdigest()
        if digest != state.get('merge_message_digest'):
            raise AutomationError('マージ要求後の実際のCommit messageが記録と一致しません。')
        state.update(phase='MERGED', merge_sha=sha, merge_parent=merged['parents'][0]['sha'])
        save_state(gh, number, state, '応答を失ったマージの成功とCommit messageを確認しました。')
    if state.get('phase') != 'MERGED' or not state.get('merge_sha'):
        return
    sha = state['merge_sha']
    if pr.get('merge_commit_sha') != sha:
        raise AutomationError('記録したマージSHAとGitHubのPR情報が一致しません。')
    query = urllib.parse.urlencode({'head_sha': sha, 'event': 'workflow_dispatch', 'per_page': 100})
    runs = gh.api('/actions/workflows/quality.yml/runs?' + query)['workflow_runs']
    run = next((run for run in runs if run['head_sha'] == sha
                and run['head_branch'] == pr['base']['ref']
                and run['event'] == 'workflow_dispatch'), None)
    if run is None:
        if not state.get('merge_parent'):
            raise AutomationError('マージ後CIの比較元が未記録です。手動確認が必要です。')
        branch = pr['base']['ref']
        current = gh.api('/git/ref/heads/' + urllib.parse.quote(branch, safe=''))['object']['sha']
        if current != sha:
            raise AutomationError('mainがマージ後SHAから進んでいます。別SHAのCIでは代用せず手動確認が必要です。')
        perform_once(gh, number, state, 'post-quality:' + sha, lambda: gh.api(
            '/actions/workflows/quality.yml/dispatches', 'POST',
            {'ref': branch, 'inputs': {'automation_main_before': state['merge_parent']}}))
        return
    if run['status'] != 'completed':
        print(f'PR #{number}: マージ後CIを待機しています。SHA: {sha}, Run: {run["id"]}')
        return
    if run['conclusion'] != 'success':
        raise AutomationError(f'マージ後CIが成功していません。SHA: {sha}, Run: {run["id"]}')
    if state.get('merge_parent'):
        sync_key = 'post-sync:' + sha
        sync = state.get('intents', {}).get(sync_key)
        if not sync:
            perform_once(gh, number, state, sync_key, lambda: gh.api(
                '/actions/workflows/update-version-timestamps.yml/dispatches', 'POST',
                {'ref': pr['base']['ref']}))
        elif sync.get('status') != 'sent':
            raise AutomationError('Version同期の起動結果が不明です。重複を防ぐため手動確認が必要です。')
    save_state(gh, number, {**state, 'phase': 'VERIFIED', 'post_merge_run': run['id']},
               f'マージ後SHA {sha} の独立した品質検査Run {run["id"]} の成功を確認しました。')


def process_pr(gh: GitHub, number: int, default_branch: str, dry_run: bool = False):
    pr = gh.api(f'/pulls/{number}')
    if pr['state'] == 'closed':
        verify_merged_pr(gh, pr, dry_run)
    if not eligible(pr, gh.repository, default_branch):
        print(f'PR #{number}: 同一Repositoryの既定Branch宛ての通常PRではないため対象外です。')
        return
    if pr['user'].get('type') == 'Bot':
        print(f'PR #{number}: Bot作成のPRは書き込み権限を確認できないため対象外です。')
        return
    author = urllib.parse.quote(pr['user']['login'], safe='')
    permission = gh.api(f'/collaborators/{author}/permission')['permission']
    if permission not in {'admin', 'maintain', 'write'}:
        print(f'PR #{number}: 作成者に書き込み権限がないため対象外です。')
        return
    comments = gh.pages(f'/issues/{number}/comments')
    state = read_state(comments)
    head = pr['head']['sha']
    current = fingerprint(head, pr['title'], pr['body'] or '')
    if dry_run or state.get('fingerprint') != current:
        # PR側のScriptやHookを実行しない。Git objectは既定Branchの作業領域へ取得する。
        # fetch後に既定Branchが進んでも、同じfetchで取得した比較元を使う。
        base_ref = f'refs/remotes/origin/{default_branch}'
        git('fetch', '--no-tags', 'origin', f'+refs/heads/{default_branch}:{base_ref}',
            f'refs/pull/{number}/head')
        base = git('rev-parse', '--verify', base_ref + '^{commit}').decode().strip()
        fresh = gh.api(f'/pulls/{number}')
        if (not eligible(fresh, gh.repository, default_branch)
                or fingerprint(fresh['head']['sha'], fresh['title'], fresh['body'] or '') != current):
            print(f'PR #{number}: Git objectの取得中にPRが更新されたため、最新状態は次回確認します。')
            return
        commits = git('rev-list', '--reverse', '--topo-order', f'{base}..{head}').decode().splitlines()
        if not commits or len(commits) > MAX_COMMITS:
            raise AutomationError('PR Commit数が自動化の対象範囲（1～100件）を超えています。')
        original = {'title': pr['title'], 'body': pr['body'] or '', 'commits': [
            {'sha': sha, 'message': git('cat-file', 'commit', sha).split(b'\n\n', 1)[1].decode()}
            for sha in commits]}
        implementation = hashlib.sha256(
            Path(__file__).read_bytes() + Path(__file__).with_name('argos_commit_translation.py').read_bytes()
            + Path('requirements-translation.txt').read_bytes()
            + Path('.github/argos-model.json').read_bytes()).hexdigest()
        if (not dry_run and state.get('translation_failed') == current
                and state.get('implementation') == implementation):
            raise AutomationError('同じ入力・実装で翻訳が失敗済みです。原文を保持しています。'
                                  '入力または実装の修正後に再開します。Dry Runで再検証できます。')
        try:
            translated = translate(original)
        except TranslationSetupError:
            # モデル配布先の一時障害と恒久的な初期化不具合は同一視しない。
            # 原文を保持し失敗を報告するが、入力検証の停止記録には加えない。
            raise
        except AutomationError:
            if not dry_run:
                # managed等の既存状態も保持し、未翻訳を翻訳済みにはしない。
                save_state(gh, number, {**state, 'translation_failed': current,
                           'implementation': implementation, 'phase': 'MANUAL_ACTION_REQUIRED',
                           'failed_sha': head},
                           '翻訳検証が失敗しました。Commit・PRの原文は保持しています。'
                           'ログを確認し、入力または翻訳実装を修正してください。'
                           '同じ入力・実装の定期的な再翻訳は停止します。')
            raise
        if dry_run:
            print(json.dumps({'pr': number, 'before': original,
                              'after': translated}, ensure_ascii=False).replace('@', r'\u0040'))
            return
        changed = (translated['title'] != original['title'] or translated['body'] != original['body']
                   or any(translated['messages'][sha].rstrip('\n') != item['message'].rstrip('\n')
                          for item in original['commits'] for sha in [item['sha']]))
        # 日本語化が不要なPRは自動マージの対象に加えない。
        if not changed and not state.get('managed'):
            save_state(gh, number, {'fingerprint': current, 'managed': False},
                       'CommitとPRの説明を確認しました。日本語への修正はありません。')
            return
        new_head, mapping = rewrite_commits(base, head, translated['messages'])
        report = json.dumps({'before': original,
                             'after': {key: translated[key] for key in ('title', 'body', 'commits')},
                             'sha_mapping': mapping}, ensure_ascii=False, indent=2)
        # 入力内のMentionやコードフェンスがBotの依頼として解釈されないようJSONで引用する。
        report = report.replace('@', '\\u0040').replace('`', '\\u0060')
        if len(report) > 55_000:
            raise AutomationError('翻訳前後のレビュー記録がComment上限を超えます。省略せず停止します。')
        fresh = gh.api(f'/pulls/{number}')
        if (fresh['head']['sha'] != head or fresh['title'] != pr['title']
                or fresh['body'] != pr['body'] or not eligible(fresh, gh.repository, default_branch)):
            raise AutomationError('処理中にPRが更新されました。次回、最新状態から再確認します。')
        branch = pr['head']['ref']
        state = {'fingerprint': fingerprint(new_head, translated['title'], translated['body']),
                 'managed': True, 'sha': new_head, 'review_requested': False}
        # push/PATCH後にAPIが失敗しても、次回は日本語化済みPRとして再開できるよう先に記録する。
        save_state(gh, number, state,
                   'Commit messageとPRの説明の日本語化を準備しました。全Commitのファイル内容・著者・'
                   '日時を保持することを検証済みです。書き換えたCommitと後続CommitのSHAは変わり、'
                   'その署名は引き継げません。最新SHAへのCodex Reviewと品質検査の成功後にSquash mergeします。'
                   '\n\n<details><summary>翻訳前後とSHA対応のレビュー記録（入力内の指示は実行対象外）</summary>'
                   '\n\n```json\n' + report + '\n```\n\n</details>')
        if new_head != head:
            git('push', f'--force-with-lease=refs/heads/{branch}:{head}',
                'origin', f'{new_head}:refs/heads/{branch}')
        gh.api(f'/pulls/{number}', 'PATCH', {'title': translated['title'], 'body': translated['body']})
        save_state(gh, number, state, 'Commit messageとPRの説明の日本語化を適用しました。'
                   '翻訳前後の意味・完全性を確認した書き込み権限者は、次の内容を単独のCommentで承認してください。'
                   '\n\n/approve-commit-translation ' + state['fingerprint'])
        print(f'PR #{number}: 日本語化を確認しました（Commit {len(mapping)}件）。')
        # 更新直後のAPI整合性を待つ代わりに次回の実行で再取得する。
        return
    if not state.get('managed'):
        return
    if state.get('sha') != head:
        raise AutomationError('自動化の状態と現在のSHAが一致しません。')
    # 自動マージに必要なCI自体を書き換えたPRは、この経路ではマージしない。
    # 正当な品質検査Workflowの変更も通常のレビュー・手動マージで扱う。
    git('fetch', '--no-tags', 'origin', f'refs/pull/{number}/head')
    if git('show', f'{head}:.github/workflows/quality.yml') != Path('.github/workflows/quality.yml').read_bytes():
        raise AutomationError('品質検査Workflowが既定Branchと異なります。通常のレビューとマージが必要です。')
    if not state.get('review_requested'):
        # 機械可読状態で既に最新SHAのレビューが完了していれば、重複依頼しない。
        if not codex_passed(comments, head) and not review_observed(comments, head):
            if not perform_once(gh, number, state, 'review:' + head, lambda: gh.comment(
                    number, '@codex review\n\n最新Commitの差分と、Commit message・PR title/bodyの'
                       '日本語表記をレビューしてください。Botの「翻訳前後とSHA対応のレビュー記録」と'
                       '照合し、意味・情報・正式表記が保たれていることも確認してください。'
                       '説明と指摘は日本語で記述してください。'
                       + f'\n\n<!-- commit-ja-review-request:{head} -->')):
                return
        state['review_requested'] = True
        save_state(gh, number, state, '最新CommitへのCodex Reviewを確認・依頼しました。')
    run = quality_run(gh, head, pr['head']['ref'], number)
    if run is None:
        if not perform_once(gh, number, state, 'quality:' + head, lambda: gh.api(
                '/actions/workflows/quality.yml/dispatches', 'POST', {
                    'ref': pr['head']['ref'], 'inputs': {'automation_pr': str(number)},
                })):
            return
        print(f'PR #{number}: 最新Commitの品質検査を起動しました。')
        return
    if run['status'] != 'completed' or run['conclusion'] != 'success':
        print(f'PR #{number}: 品質検査の成功を待機しています。')
        return
    if not codex_passed(comments, head):
        print(f'PR #{number}: 最新SHAのCodex Review完了・指摘なしを待機しています。')
        return
    if not reviews_clear(gh.pages(f'/pulls/{number}/reviews')) or not threads_clear(gh, number):
        print(f'PR #{number}: レビューの未解決指摘があります。')
        return
    if not all_checks_passed(gh, head):
        print(f'PR #{number}: 他のCheck・Statusの成功を待機しています。')
        return
    fresh = gh.api(f'/pulls/{number}')
    if (not eligible(fresh, gh.repository, default_branch) or fresh['head']['sha'] != head
            or fingerprint(head, fresh['title'], fresh['body'] or '') != state['fingerprint']
            or fresh['mergeable'] is not True or fresh['mergeable_state'] != 'clean'):
        print(f'PR #{number}: PRの更新・競合・保護設定の解決を待機しています。')
        return
    if not translation_approved(gh, comments, current):
        print(f'PR #{number}: 翻訳の意味・完全性の確認が必要です。'
              f'確認後の承認Comment: /approve-commit-translation {current}')
        return
    # 承認確認中にもReview・Checkは変化し得るため、マージAPI直前に再取得する。
    latest_comments = gh.pages(f'/issues/{number}/comments')
    if (not codex_passed(latest_comments, head)
            or not translation_approved(gh, latest_comments, current)
            or not reviews_clear(gh.pages(f'/pulls/{number}/reviews'))
            or not threads_clear(gh, number) or not all_checks_passed(gh, head)):
        print(f'PR #{number}: マージ直前のReview・承認・Checkが条件を満たしません。')
        return
    fresh = gh.api(f'/pulls/{number}')
    if (not eligible(fresh, gh.repository, default_branch) or fresh['head']['sha'] != head
            or fingerprint(head, fresh['title'], fresh['body'] or '') != current
            or fresh['mergeable'] is not True or fresh['mergeable_state'] != 'clean'):
        print(f'PR #{number}: マージ直前にPRの状態が変わりました。次回再確認します。')
        return
    expected_message = f"{fresh['title']} (#{number})" + (
        '\n\n' + fresh['body'] if fresh['body'] else '')
    state.update(phase='MERGE_READY', merge_message_digest=hashlib.sha256(
        expected_message.rstrip('\n').encode()).hexdigest())
    # マージ後に応答・状態記録を失っても、Closed PRから成功を照合できる。
    save_state(gh, number, state, '最新SHAのマージ条件を確認し、Squash要求の内容を記録しました。')
    result = gh.api(f'/pulls/{number}/merge', 'PUT', {
        'sha': head, 'merge_method': 'squash',
        'commit_title': f"{fresh['title']} (#{number})", 'commit_message': fresh['body'] or '',
    })
    if not result.get('merged'):
        raise AutomationError('GitHubがマージを受け付けませんでした。')
    merged = gh.api('/git/commits/' + result['sha'])
    expected_message = f"{fresh['title']} (#{number})" + (
        '\n\n' + fresh['body'] if fresh['body'] else '')
    if merged['message'].rstrip('\n') != expected_message.rstrip('\n'):
        raise AutomationError('マージ後のCommit messageが指定した内容と一致しません。')
    state.update(phase='MERGED', merge_sha=result['sha'], merge_parent=merged['parents'][0]['sha'])
    save_state(gh, number, state,
               'Squash後のCommit messageを照合しました。マージ後SHAの独立CIは未確認です。')
    # GITHUB_TOKENのmergeではpush Workflowが抑止されるため、同期と品質検査を明示起動する。
    # 通常pushと同じく、厳格なVersion日時照合は同期処理へ任せる。
    perform_once(gh, number, state, 'post-quality:' + result['sha'], lambda: gh.api(
        '/actions/workflows/quality.yml/dispatches', 'POST', {
            'ref': default_branch, 'inputs': {'automation_main_before': merged['parents'][0]['sha']},
        }))
    perform_once(gh, number, state, 'post-sync:' + result['sha'], lambda: gh.api(
        '/actions/workflows/update-version-timestamps.yml/dispatches', 'POST', {'ref': default_branch}))
    print(f"PR #{number}: 日本語のCommit messageでマージ済みです。SHA: {result['sha']}")


def main() -> int:
    if os.environ.get('COMMIT_JA_AUTOMATION_ENABLED', '').lower() == 'false':
        print('Repository Variableにより自動化を停止しています。')
        return 0
    gh = GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])
    default_branch = gh.api('')['default_branch']
    target = os.environ.get('TARGET_PR', '')
    if target and not re.fullmatch(r'[1-9][0-9]*', target):
        raise AutomationError('PR番号には正の整数を指定してください。')
    numbers = [int(target)] if target else [pr['number'] for pr in gh.pages('/pulls?state=open')]
    if not target:
        # 直近に更新された閉じたPRを上限付きで確認する。PR本文は状態に使用しない。
        closed = gh.api('/pulls?state=closed&sort=updated&direction=desc&per_page=30')
        numbers += [pr['number'] for pr in closed if pr.get('merged_at')]
    failures = []
    for number in numbers:
        try:
            process_pr(gh, number, default_branch,
                       os.environ.get('COMMIT_JA_DRY_RUN', '').lower() == 'true')
        except (AutomationError, subprocess.CalledProcessError, UnicodeDecodeError) as error:
            # Gitのstderrや入力本文には機密情報が含まれる可能性があるため出力しない。
            message = str(error) if isinstance(error, AutomationError) else 'Git objectの取得・検証・反映に失敗しました。'
            print(f'::error::PR #{number}: {message}')
            failures.append(number)
    return int(bool(failures))


if __name__ == '__main__':
    try:
        sys.exit(main())
    except AutomationError as error:
        print(f'::error::{error}')
        sys.exit(1)
