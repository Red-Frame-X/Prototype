"""実Git・指定の翻訳器とMock GitHubで、自動化を検証済み状態まで進める。

外部RepositoryやPRは作成・更新しない。CIとReviewの結果は明示的に模擬する。
"""
import copy
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import automate_japanese_commits as automation

ROOT = Path(__file__).resolve().parents[1]


def run_end_to_end(engine):
    previous = Path.cwd()
    git = automation.git
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory) / 'work'
        remote = Path(directory) / 'remote.git'
        merger = Path(directory) / 'merger'
        work.mkdir()
        try:
            os.chdir(work)
            git('init', '-q', '-b', 'main')
            git('config', 'user.name', 'Fixture Author')
            git('config', 'user.email', 'fixture@example.invalid')
            for filename in ('.github/workflows/quality.yml', '.github/argos-model.json',
                             'requirements-translation.txt'):
                target = work / filename
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / filename).read_bytes())
            git('add', '.')
            git('commit', '-qm', '検証用の基準を追加')
            base = git('rev-parse', 'HEAD').decode().strip()
            git('checkout', '-qb', 'topic')
            Path('documentation.txt').write_text('保持する検証用の本文\n')
            git('add', '.')
            git('commit', '-qm', 'Update documentation')
            original = git('rev-parse', 'HEAD').decode().strip()
            git('clone', '--bare', '.', str(remote))
            git('remote', 'add', 'origin', str(remote))

            class MockGitHub:
                repository = 'fixture/repository'
                token = 'no-network-token'

                def __init__(self):
                    self.comments, self.runs, self.writes = [], [], []
                    self.merges = 0
                    self.pr = {'number': 1, 'state': 'open', 'draft': False, 'merged': False,
                               'title': 'Update documentation', 'body': 'Do not remove existing tests.',
                               'user': {'login': 'owner', 'type': 'User'},
                               'head': {'ref': 'topic', 'sha': original,
                                        'repo': {'full_name': self.repository}},
                               'base': {'ref': 'main', 'repo': {'full_name': self.repository}},
                               'mergeable': True, 'mergeable_state': 'clean'}

                def comment(self, number, body):
                    self.comments.append({'user': {'login': automation.BOT_LOGIN, 'type': 'Bot'},
                                          'body': body})

                def pages(self, path):
                    if path == '/issues/1/comments':
                        return copy.deepcopy(self.comments)
                    if path == '/pulls/1/reviews':
                        return []
                    raise AssertionError(path)

                def api(self, path, method='GET', data=None):
                    if method != 'GET':
                        self.writes.append((path, method, data))
                    if path == '/pulls/1' and method == 'GET':
                        self.pr['head']['sha'] = git('--git-dir', str(remote), 'rev-parse',
                                                    'refs/heads/topic').decode().strip()
                        git('--git-dir', str(remote), 'update-ref', 'refs/pull/1/head',
                            self.pr['head']['sha'])
                        return copy.deepcopy(self.pr)
                    if path.endswith('/permission'):
                        return {'permission': 'write'}
                    if path == '/git/ref/heads/main':
                        return {'object': {'sha': git('--git-dir', str(remote), 'rev-parse',
                                                     'refs/heads/main').decode().strip()}}
                    if path == '/pulls/1' and method == 'PATCH':
                        self.pr.update(data)
                        return copy.deepcopy(self.pr)
                    if path.startswith('/actions/workflows/quality.yml/runs?'):
                        return {'workflow_runs': list(reversed(copy.deepcopy(self.runs)))}
                    if path == '/actions/workflows/quality.yml/dispatches':
                        sha = git('--git-dir', str(remote), 'rev-parse',
                                  'refs/heads/' + data['ref']).decode().strip()
                        self.runs.append({'id': len(self.runs) + 1, 'head_sha': sha,
                                          'head_branch': data['ref'], 'event': 'workflow_dispatch',
                                          'display_title': f'PR #1 日本語化検証 {sha}',
                                          'status': 'in_progress', 'conclusion': None})
                        return None
                    if path.endswith('/check-runs?filter=latest&per_page=100'):
                        return {'total_count': 1, 'check_runs': [
                            {'status': 'completed', 'conclusion': 'success'}]}
                    if path.endswith('/status'):
                        return {'total_count': 0, 'state': 'pending'}
                    if path == '/pulls/1/merge':
                        assert data['sha'] == self.pr['head']['sha']
                        assert data['merge_method'] == 'squash'
                        self.merges += 1
                        git('clone', str(remote), str(merger))
                        git('-C', str(merger), 'checkout', 'main')
                        git('-C', str(merger), 'config', 'user.name', 'Fixture Merger')
                        git('-C', str(merger), 'config', 'user.email', 'merger@example.invalid')
                        git('-C', str(merger), 'merge', '--squash', 'origin/topic')
                        message = data['commit_title'] + '\n\n' + data['commit_message']
                        git('-C', str(merger), 'commit', '-qm', message)
                        sha = git('-C', str(merger), 'rev-parse', 'HEAD').decode().strip()
                        git('-C', str(merger), 'push', 'origin', 'HEAD:main')
                        self.pr.update(state='closed', merged=True, merge_commit_sha=sha)
                        return {'merged': True, 'sha': sha}
                    if path.startswith('/git/commits/'):
                        sha = path.rsplit('/', 1)[1]
                        return {'message': git('--git-dir', str(remote), 'show', '-s',
                                               '--format=%B', sha).decode().rstrip('\n'),
                                'parents': [{'sha': parent} for parent in git(
                                    '--git-dir', str(remote), 'show', '-s', '--format=%P', sha
                                ).decode().split()]}
                    if path == '/actions/workflows/update-version-timestamps.yml/dispatches':
                        return None
                    raise AssertionError((path, method))

            def graphql(url, *args, **kwargs):
                assert url == 'https://api.github.com/graphql'
                return {'data': {'repository': {'pullRequest': {'reviewThreads': {
                    'nodes': [], 'pageInfo': {'hasNextPage': False}}}}}}

            gh = MockGitHub()
            with patch('argos_commit_translation.load_engine', return_value=engine), patch.object(
                    automation, 'request_json', side_effect=graphql):
                automation.process_pr(gh, 1, 'main')
                translated = gh.api('/pulls/1')['head']['sha']
                assert translated != original
                assert git('diff', original, translated) == b''
                for before, after in ((original, translated),):
                    assert git('show', '-s', '--format=%an %ae %aI %cn %ce %cI', before) == git(
                        'show', '-s', '--format=%an %ae %aI %cn %ce %cI', after)
                automation.process_pr(gh, 1, 'main')
                automation.process_pr(gh, 1, 'main')
                assert gh.merges == 0
                assert len(gh.runs) == 1
                gh.runs[0].update(status='completed', conclusion='success')
                state = automation.read_state(gh.comments)
                gh.comments.append({'user': {'login': 'owner', 'type': 'User'},
                                    'body': '/approve-commit-translation ' + state['fingerprint']})
                review = {'code_review': {'commit_sha': translated, 'status': 'completed',
                                         'has_any_findings': False, 'has_unresolved_findings': False}}
                gh.comments.append({'user': {'login': automation.CODEX_LOGIN, 'type': 'Bot'},
                                    'body': '<!-- codex-review-state:v1 ' + json.dumps(review) + ' -->'})
                automation.process_pr(gh, 1, 'main')
                assert gh.merges == 1 and len(gh.runs) == 2
                merged = gh.pr['merge_commit_sha']
                assert gh.runs[1]['head_sha'] == merged
                assert gh.runs[0]['head_sha'] != merged
                assert git('--git-dir', str(remote), 'diff', translated, merged) == b''
                assert automation.read_state(gh.comments)['phase'] == 'MERGED'
                automation.process_pr(gh, 1, 'main')
                assert automation.read_state(gh.comments)['phase'] == 'MERGED'
                gh.runs[1].update(status='completed', conclusion='success')
                automation.process_pr(gh, 1, 'main')
                assert automation.read_state(gh.comments)['phase'] == 'VERIFIED'
                automation.process_pr(gh, 1, 'main')
                assert gh.merges == 1 and len(gh.runs) == 2
                assert git('--git-dir', str(remote), 'show', '-s', '--format=%P', merged).decode().strip() == base
                print('実Gitの日本語化・著者保持・Squash・独立CI確認を完了（GitHub API / Review / CIはMock）。')
        finally:
            os.chdir(previous)
