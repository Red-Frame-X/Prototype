"""実際のGit履歴とAPIの状態遷移で日本語化・自動マージの境界を検証する。"""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import automate_japanese_commits as automation

SHA = 'a' * 40
BASE = 'b' * 40
REPO = 'owner/repo'


def comment(login, body, kind='Bot'):
    return {'user': {'login': login, 'type': kind}, 'body': body}


def codex_comment(sha=SHA, **overrides):
    review = {'commit_sha': sha, 'status': 'completed',
              'has_any_findings': False, 'has_unresolved_findings': False}
    review.update(overrides)
    state = {'code_review': review, 'security_review': {'status': None}}
    return comment(automation.CODEX_LOGIN, '<!-- codex-review-state:v1 '
                   + json.dumps(state) + ' -->')


def pull_request():
    return {'number': 1, 'state': 'open', 'draft': False, 'title': 'READMEの説明を更新',
            'body': '変更の理由を追記します。', 'user': {'login': 'owner', 'type': 'User'},
            'head': {'sha': SHA, 'ref': 'topic', 'repo': {'full_name': REPO}},
            'base': {'ref': 'main', 'repo': {'full_name': REPO}},
            'mergeable': True, 'mergeable_state': 'clean'}


class ReviewGateTests(unittest.TestCase):
    def test_requires_exact_sha_and_no_findings(self):
        self.assertTrue(automation.codex_passed([codex_comment()], SHA))
        for item in [codex_comment('c' * 40), codex_comment(status='in_progress'),
                     codex_comment(has_any_findings=True),
                     codex_comment(has_unresolved_findings=True)]:
            with self.subTest(item=item):
                self.assertFalse(automation.codex_passed([item], SHA))

    def test_new_running_state_invalidates_previous_success(self):
        self.assertFalse(automation.codex_passed(
            [codex_comment(), codex_comment(status='in_progress')], SHA))

    def test_human_spoof_and_friendly_text_do_not_pass(self):
        fake = codex_comment()
        fake['user'] = {'login': 'owner', 'type': 'User'}
        self.assertFalse(automation.codex_passed([fake], SHA))
        self.assertFalse(automation.codex_passed(
            [comment(automation.CODEX_LOGIN, '問題はありません。👍')], SHA))

    def test_missing_or_malformed_state_fails_closed(self):
        for body in ('<!-- codex-review-state:v1 {} -->',
                     '<!-- codex-review-state:v1 {broken} -->'):
            self.assertFalse(automation.codex_passed([comment(automation.CODEX_LOGIN, body)], SHA))

    def test_pending_security_review_blocks_merge(self):
        state = {'code_review': {'commit_sha': SHA, 'status': 'completed',
                                'has_any_findings': False, 'has_unresolved_findings': False},
                 'security_review': {'commit_sha': SHA, 'status': 'in_progress'}}
        item = comment(automation.CODEX_LOGIN, '<!-- codex-review-state:v1 '
                       + json.dumps(state) + ' -->')
        self.assertFalse(automation.codex_passed([item], SHA))

    def test_changes_requested_cannot_be_cleared_by_comment_only(self):
        reviews = [{'user': {'login': 'reviewer'}, 'state': 'CHANGES_REQUESTED'},
                   {'user': {'login': 'reviewer'}, 'state': 'COMMENTED'}]
        self.assertFalse(automation.reviews_clear(reviews))
        reviews.append({'user': {'login': 'reviewer'}, 'state': 'APPROVED'})
        self.assertTrue(automation.reviews_clear(reviews))

    def test_forks_drafts_and_main_are_not_rewritten(self):
        for change in ('fork', 'deleted_repo', 'draft', 'main', 'other_base', 'closed'):
            pr = pull_request()
            if change == 'fork':
                pr['head']['repo']['full_name'] = 'other/fork'
            elif change == 'deleted_repo':
                pr['head']['repo'] = None
            elif change == 'draft':
                pr['draft'] = True
            elif change == 'main':
                pr['head']['ref'] = 'main'
            elif change == 'other_base':
                pr['base']['ref'] = 'release'
            else:
                pr['state'] = 'closed'
            with self.subTest(change=change):
                self.assertFalse(automation.eligible(pr, REPO, 'main'))


class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.original = {'title': 'Update README', 'body': 'See #12 and `README.md`.',
                         'commits': [{'sha': SHA, 'message': 'Update README\n\nSee https://example.com/a'}]}
        self.translated = {'title': 'READMEの説明を更新', 'body': '#12 と `README.md` を参照。',
                           'commits': [{'sha': SHA, 'message': 'READMEの説明を更新\n\nhttps://example.com/a を参照'}]}

    def test_valid_translation_keeps_identifiers(self):
        result = automation.validate_translation(self.original, self.translated)
        self.assertEqual(result['messages'][SHA], self.translated['commits'][0]['message'])

    def test_missing_duplicate_or_unknown_sha_is_rejected(self):
        for commits in ([], self.translated['commits'] * 2,
                        [{'sha': BASE, 'message': 'READMEの説明を更新'}]):
            translated = {**self.translated, 'commits': commits}
            with self.subTest(commits=commits), self.assertRaises(automation.AutomationError):
                automation.validate_translation(self.original, translated)

    def test_english_and_vague_titles_are_rejected(self):
        for key, value in (('title', 'Update README'), ('title', '修正'),
                           ('title', 'READMEの説明を更新\n別の行')):
            with self.subTest(value=value), self.assertRaises(automation.AutomationError):
                automation.validate_translation(self.original, {**self.translated, key: value})
        self.translated['commits'][0]['message'] = 'Update README'
        with self.assertRaises(automation.AutomationError):
            automation.validate_translation(self.original, self.translated)

    def test_removed_url_issue_or_code_identifier_is_rejected(self):
        for before, after in (('#12', '#13'), ('`README.md`', '`OTHER.md`')):
            translated = copy.deepcopy(self.translated)
            translated['body'] = translated['body'].replace(before, after)
            with self.subTest(before=before), self.assertRaises(automation.AutomationError):
                automation.validate_translation(self.original, translated)
        self.translated['commits'][0]['message'] = 'READMEの説明を更新'
        with self.assertRaises(automation.AutomationError):
            automation.validate_translation(self.original, self.translated)

    def test_changed_naked_commit_hash_is_rejected(self):
        for sha in ('c77ede4b', 'a1' * 20):
            original = copy.deepcopy(self.original)
            translated = copy.deepcopy(self.translated)
            original['body'] += ' ' + sha
            translated['body'] += ' ' + sha
            automation.validate_translation(original, translated)
            translated['body'] = translated['body'].replace(sha, 'b2' * 20)
            with self.subTest(sha=sha), self.assertRaises(automation.AutomationError):
                automation.validate_translation(original, translated)

    def test_truncated_argos_output_is_rejected(self):
        with patch('argos_commit_translation.load_engine', return_value=lambda text: ''):
            with self.assertRaises(automation.AutomationError):
                automation.translate(self.original)

    def test_model_failure_never_calls_paid_api(self):
        from argos_commit_translation import TranslationError
        with patch('argos_commit_translation.load_engine', side_effect=TranslationError('取得失敗')):
            with patch.object(automation, 'request_json') as api:
                with self.assertRaises(automation.AutomationError):
                    automation.translate(self.original)
                api.assert_not_called()


class QualityRunTests(unittest.TestCase):
    def test_normal_manual_run_cannot_replace_failed_pr_validation(self):
        gh = Mock()
        normal = {'id': 30, 'head_sha': SHA, 'head_branch': 'topic',
                  'display_title': 'Repositoryの品質検査', 'conclusion': 'success'}
        other_pr = {**normal, 'id': 20, 'display_title': f'PR #2 日本語化検証 {SHA}'}
        actual = {**normal, 'id': 10, 'display_title': f'PR #1 日本語化検証 {SHA}',
                  'conclusion': 'failure'}
        gh.api.return_value = {'workflow_runs': [normal, other_pr, actual]}
        self.assertEqual(automation.quality_run(gh, SHA, 'topic', 1), actual)

    def test_only_normal_manual_run_requires_new_pr_validation(self):
        gh = Mock()
        gh.api.return_value = {'workflow_runs': [
            {'head_sha': SHA, 'head_branch': 'topic', 'display_title': 'Repositoryの品質検査'}]}
        self.assertIsNone(automation.quality_run(gh, SHA, 'topic', 1))


class GitRewriteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        previous = Path.cwd()
        self.addCleanup(os.chdir, previous)
        os.chdir(self.temp.name)
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'Original Author')
        self.git('config', 'user.email', 'author@example.invalid')
        Path('file.txt').write_text('keep all content\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'base')
        self.base = self.git('rev-parse', 'HEAD')

    def git(self, *args):
        return automation.git(*args).decode().strip()

    def commit(self, text, title):
        Path('file.txt').write_text(text)
        self.git('commit', '-qam', title)
        return self.git('rev-parse', 'HEAD')

    def test_multiple_commits_keep_each_tree_author_time_and_parent_chain(self):
        first = self.commit('first contents\n', 'Update first entry')
        second = self.commit('second contents\n', '既存の日本語Commit')
        head, mapping = automation.rewrite_commits(self.base, second, {
            first: '最初の項目を更新', second: '既存の日本語Commit',
        })
        self.assertNotEqual(head, second)
        self.assertEqual(self.git('show', '-s', '--format=%P', mapping[first]), self.base)
        self.assertEqual(self.git('show', '-s', '--format=%P', head), mapping[first])
        for before, after in mapping.items():
            self.assertEqual(self.git('show', '-s', '--format=%T %an %ae %aI %cn %ce %cI', before),
                             self.git('show', '-s', '--format=%T %an %ae %aI %cn %ce %cI', after))
        self.assertEqual(self.git('diff', second, head), '')
        self.assertEqual(self.git('show', '-s', '--format=%B', head), '既存の日本語Commit')
        # 作業Branch・作業ファイルは変更しない。
        self.assertEqual(self.git('rev-parse', 'HEAD'), second)
        self.assertEqual(Path('file.txt').read_text(), 'second contents\n')

    def test_unchanged_messages_keep_original_sha(self):
        head = self.commit('content\n', 'READMEの説明を更新')
        new, _ = automation.rewrite_commits(self.base, head, {head: 'READMEの説明を更新'})
        self.assertEqual(new, head)

    def test_merge_parent_order_and_both_histories_are_preserved(self):
        self.git('checkout', '-qb', 'side')
        Path('side.txt').write_text('side\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'Add side file')
        side = self.git('rev-parse', 'HEAD')
        self.git('checkout', '-q', 'main')
        first = self.commit('main change\n', 'Update main entry')
        self.git('merge', '--no-ff', 'side', '-qm', 'Merge side branch')
        merge = self.git('rev-parse', 'HEAD')
        new, mapping = automation.rewrite_commits(self.base, merge, {
            side: '別のファイルを追加', first: '本文を更新', merge: 'sideの変更を統合',
        })
        self.assertEqual(self.git('show', '-s', '--format=%P', new),
                         mapping[first] + ' ' + mapping[side])
        self.assertEqual(self.git('diff', merge, new), '')

    def test_missing_translation_stops_before_rewrite(self):
        head = self.commit('content\n', 'Update content')
        with self.assertRaises(automation.AutomationError):
            automation.rewrite_commits(self.base, head, {})

    def test_rewritten_signature_is_removed_but_metadata_is_preserved(self):
        head = self.commit('content\n', 'Update content')
        raw = automation.git('cat-file', 'commit', head)
        header, message = raw.split(b'\n\n', 1)
        signed = automation.git('hash-object', '-t', 'commit', '-w', '--stdin', data=(
            header + b'\ngpgsig -----BEGIN PGP SIGNATURE-----\n test-signature\n'
            b' -----END PGP SIGNATURE-----\n\n' + message)).decode().strip()
        rewritten, _ = automation.rewrite_commits(self.base, signed, {signed: '本文を更新'})
        result = automation.git('cat-file', 'commit', rewritten)
        self.assertNotIn(b'gpgsig ', result)
        self.assertEqual(result.split(b'\n\n', 1)[0], header)

    def test_force_with_lease_rejects_concurrent_push(self):
        remote = Path(self.temp.name) / 'remote.git'
        self.git('clone', '--bare', '.', str(remote))
        self.git('remote', 'add', 'origin', str(remote))
        head = self.commit('content\n', 'Update content')
        self.git('push', 'origin', 'HEAD:main')
        with self.assertRaises(subprocess.CalledProcessError):
            automation.git('push', f'--force-with-lease=refs/heads/main:{self.base}',
                           'origin', f'{self.base}:refs/heads/main')
        self.assertEqual(self.git('--git-dir', str(remote), 'rev-parse', 'main'), head)


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.pr = pull_request()
        self.gh = Mock(repository=REPO)
        self.gh.token = 'fake-token'
        self.state = {'fingerprint': automation.fingerprint(SHA, self.pr['title'], self.pr['body']),
                      'managed': True, 'sha': SHA, 'review_requested': True}
        body = '<!-- ' + automation.STATE_MARKER + ' ' + json.dumps(self.state) + ' -->'
        self.comments = [comment('owner', '/approve-commit-translation ' + self.state['fingerprint'], 'User'),
                         comment(automation.BOT_LOGIN, body), codex_comment()]
        self.gh.pages.side_effect = lambda path: self.comments if 'comments' in path else []
        self.merged = False
        self.changes = []
        def api(path, method='GET', data=None):
            if method != 'GET':
                self.changes.append((path, method, data))
            if path == '/pulls/1' and method == 'GET':
                return self.pr
            if path.endswith('/permission'):
                return {'permission': 'write'}
            if path == '/pulls/1/merge':
                self.merged = True
                return {'merged': True, 'sha': 'c' * 40}
            if path.startswith('/git/commits/'):
                return {'message': self.pr['title'] + ' (#1)\n\n' + self.pr['body'],
                        'parents': [{'sha': BASE}]}
            if path.endswith('/dispatches'):
                return None
            raise AssertionError((path, method, data))
        self.gh.api.side_effect = api
        self.stack = []
        for name, value in [('git', Path(__file__).read_bytes()),
                            ('quality_run', {'status': 'completed', 'conclusion': 'success'}),
                            ('threads_clear', True), ('all_checks_passed', True)]:
            patcher = patch.object(automation, name, return_value=value)
            self.stack.append(patcher.start())
            self.addCleanup(patcher.stop)
        # trusted quality.ymlの実際の内容と照合する。
        self.stack[0].return_value = (Path(__file__).resolve().parents[1]
                                      / '.github/workflows/quality.yml').read_bytes()

    def run_pr(self):
        automation.process_pr(self.gh, 1, 'main')

    def test_closed_or_merged_pr_is_not_processed_even_on_repeated_runs(self):
        for merged in (False, True):
            with self.subTest(merged=merged):
                self.pr['state'] = 'closed'
                self.pr['merged'] = merged
                self.run_pr()
                self.run_pr()
                self.assertFalse(self.merged)
                self.assertEqual(self.changes, [])
                self.gh.comment.assert_not_called()
                self.stack[0].assert_not_called()

    def test_pr_closed_during_review_never_merges(self):
        before = copy.deepcopy(self.pr)
        after = {**before, 'state': 'closed', 'merged': True}
        previous_api = self.gh.api.side_effect
        responses = iter((before, after))
        self.gh.api.side_effect = lambda path, *args: (
            next(responses) if path == '/pulls/1' else previous_api(path, *args))
        self.run_pr()
        self.assertFalse(self.merged)
        self.assertEqual(self.changes, [])

    def test_repeated_unmanaged_pr_skips_translation_review_and_merge(self):
        self.state['managed'] = False
        self.comments = [comment(automation.BOT_LOGIN, '<!-- ' + automation.STATE_MARKER
                                 + ' ' + json.dumps(self.state) + ' -->')]
        with patch.object(automation, 'translate') as translate:
            self.run_pr()
            self.run_pr()
            translate.assert_not_called()
        self.assertFalse(self.merged)
        self.assertEqual(self.changes, [])
        self.gh.comment.assert_not_called()
        self.stack[0].assert_not_called()

    def test_japanese_pr248_never_updates_branch_pr_or_merges(self):
        original = json.loads((Path(__file__).parent / 'fixtures/pr248-japanese-translation.json').read_text())
        self.pr['title'], self.pr['body'] = original['title'], original['body']
        self.comments = []
        before = copy.deepcopy(self.pr)
        previous_api = self.gh.api.side_effect
        self.gh.api.side_effect = lambda path, *args: (
            {'object': {'sha': BASE}} if path.startswith('/git/ref/') else previous_api(path, *args))
        def objects(*args, **kwargs):
            if args[0] == 'rev-list':
                return (SHA + '\n').encode()
            if args[:2] == ('cat-file', 'commit'):
                return b'tree dummy\n\n' + original['commits'][0]['message'].encode()
            if args[0] in {'fetch', 'cat-file'}:
                return b''
            raise AssertionError('翻訳不要のPRでGitを更新しています: ' + str(args))
        engine = Mock(side_effect=AssertionError('翻訳不要のPRで翻訳器を呼び出しています。'))
        with patch.object(automation, 'git', side_effect=objects), \
                patch('argos_commit_translation.load_engine', return_value=engine):
            self.run_pr()
        self.assertEqual(self.pr, before)
        self.assertEqual(self.changes, [])
        self.assertFalse(self.merged)
        self.gh.comment.assert_called_once()
        state = automation.read_state([comment(automation.BOT_LOGIN, self.gh.comment.call_args[0][1])])
        self.assertIs(state['managed'], False)

    def test_unconfirmed_meaning_never_merges(self):
        self.comments.pop(0)
        self.run_pr()
        self.assertFalse(self.merged)
        self.assertEqual(self.changes, [])

    def test_stale_or_bot_approval_never_merges(self):
        for approval in [comment('owner', '/approve-commit-translation ' + BASE, 'User'),
                         comment(automation.BOT_LOGIN, '/approve-commit-translation '
                                 + self.state['fingerprint'])]:
            self.comments[0] = approval
            self.run_pr()
            self.assertFalse(self.merged)

    def test_dry_run_never_mutates_or_merges(self):
        original = {'title': self.pr['title'], 'body': self.pr['body'],
                    'commits': [{'sha': SHA, 'message': '既存Commitの説明'}]}
        def objects(*args, **kwargs):
            if args[0] == 'rev-list':
                return (SHA + '\n').encode()
            return 'tree dummy\n\n既存Commitの説明'.encode()
        previous_api = self.gh.api.side_effect
        self.gh.api.side_effect = lambda path, *args: (
            {'object': {'sha': BASE}} if path.startswith('/git/ref/') else previous_api(path, *args))
        with patch.object(automation, 'git', side_effect=objects), \
                patch.object(automation, 'translate', return_value=original):
            automation.process_pr(self.gh, 1, 'main', dry_run=True)
        self.assertFalse(self.merged)
        self.assertEqual(self.changes, [])
        self.gh.comment.assert_not_called()

    def test_clean_latest_review_and_ci_merge_with_sha_and_japanese_message(self):
        self.run_pr()
        self.assertTrue(self.merged)
        merge = next(data for path, method, data in self.changes if path.endswith('/merge'))
        self.assertEqual(merge, {'sha': SHA, 'merge_method': 'squash',
                                'commit_title': self.pr['title'] + ' (#1)',
                                'commit_message': self.pr['body']})
        self.assertIn(('/actions/workflows/quality.yml/dispatches', 'POST',
                       {'ref': 'main', 'inputs': {'automation_main_before': BASE}}), self.changes)
        self.assertIn(('/actions/workflows/update-version-timestamps.yml/dispatches', 'POST',
                       {'ref': 'main'}), self.changes)

    def test_failed_ci_stale_review_or_conflict_never_merge(self):
        for condition in ('ci', 'review', 'conflict', 'checks', 'threads', 'draft'):
            with self.subTest(condition=condition):
                self.pr = pull_request()
                self.comments[-1] = codex_comment()
                self.stack[1].return_value = {'status': 'completed', 'conclusion': 'success'}
                self.stack[2].return_value = True
                self.stack[3].return_value = True
                if condition == 'ci':
                    self.stack[1].return_value['conclusion'] = 'failure'
                elif condition == 'review':
                    self.comments[-1] = codex_comment(BASE)
                elif condition == 'conflict':
                    self.pr['mergeable_state'] = 'dirty'
                elif condition == 'checks':
                    self.stack[3].return_value = False
                elif condition == 'threads':
                    self.stack[2].return_value = False
                else:
                    self.pr['draft'] = True
                self.run_pr()
                self.assertFalse(self.merged)

    def test_missing_quality_run_is_dispatched_and_not_treated_as_success(self):
        self.stack[1].return_value = None
        self.run_pr()
        self.assertFalse(self.merged)
        self.assertEqual(self.changes, [('/actions/workflows/quality.yml/dispatches', 'POST',
                                        {'ref': 'topic', 'inputs': {'automation_pr': '1'}})])

    def test_modified_quality_workflow_never_auto_merges(self):
        self.stack[0].return_value = b'weakened workflow'
        with self.assertRaises(automation.AutomationError):
            self.run_pr()
        self.assertFalse(self.merged)


if __name__ == '__main__':
    unittest.main()
