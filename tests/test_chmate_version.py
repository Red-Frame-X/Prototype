import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from unittest.mock import patch

from scripts import update_version_timestamps as updater

ROOT = Path(__file__).resolve().parents[1]
# CLIと同じScript探索パスで読み込む。
with patch.object(sys, 'path', [str(ROOT / 'scripts'), *sys.path]):
    spec = importlib.util.spec_from_file_location('chmate_checker', ROOT / 'scripts/check_chmate_version.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)

BEFORE = '! Title: NG Word Regex for ChMate\n! Version: 202611080030\n! Comment\na|b\n'
NOW = datetime(2026, 11, 8, 0, 31, tzinfo=updater.JST)


class ChmateVersionTests(unittest.TestCase):
    def test_missing_duplicate_bad_date_and_format(self):
        for text in (BEFORE.replace('! Version: 202611080030\n', ''),
                     BEFORE + '! Version: 202611080030\n',
                     BEFORE.replace('202611080030', '202613080030'),
                     BEFORE.replace('202611080030', '20261108'),
                     BEFORE.replace('! Version:', ' ! Version:'),
                     BEFORE.replace('202611080030', '２０２６１１０８００３０')):
            with self.subTest(text=text), self.assertRaises(ValueError):
                updater.chmate_version(text)

    def test_body_and_comment_edits_all_actors_require_jst(self):
        for actor in ('Chat', 'Work', 'Codex', 'GitHub', 'Pull Request', 'GitHub Actions'):
            after = BEFORE + f'! {actor}\n'
            with self.subTest(actor=actor):
                with self.assertRaises(ValueError):
                    checker.check(BEFORE, after.replace('202611080030', '202611071531'), NOW)
                with self.assertRaises(ValueError):
                    checker.check(BEFORE, after, NOW)
                checker.check(BEFORE, after.replace('202611080030', '202611080031'), NOW)
                checker.check(BEFORE, after, NOW.replace(minute=30))
                with self.assertRaises(ValueError):
                    checker.check(BEFORE, after, NOW.replace(minute=40))

    def test_unnecessary_version_only_rejected_but_pending_repair_allowed(self):
        normalized = updater.version_text(updater.CHMATE_FILE, BEFORE, '<VERSION>')
        checkpoint = json.dumps({str(updater.CHMATE_FILE): hashlib.sha256(normalized.encode()).hexdigest()})
        after = BEFORE.replace('202611080030', '202611080031')
        with self.assertRaises(ValueError):
            checker.check(BEFORE, after, NOW, checkpoint)
        with self.assertRaises(ValueError):
            checker.check(BEFORE, after, NOW, '{}')
        checker.check(BEFORE, after, NOW, '{}', automated_sync=True)
        checker.check(BEFORE, BEFORE, NOW, checkpoint)

    def test_invalid_baseline_can_be_repaired_but_bad_replacement_is_rejected(self):
        after = BEFORE.replace('202611080030', '202611080031')
        for before in (BEFORE.replace('! Version: 202611080030\n', ''),
                       BEFORE.replace('202611080030', 'bad'),
                       BEFORE + '! Version: 202611080030\n'):
            with self.subTest(before=before):
                checker.check(before, after, NOW)
                with self.assertRaises(ValueError):
                    checker.check(before, BEFORE, NOW.replace(hour=1))
                with self.assertRaises(ValueError):
                    checker.check(before, after.replace('202611080031', 'bad'), NOW)

    def test_real_file_bytes_are_preserved_except_version(self):
        original = (ROOT / updater.CHMATE_FILE).read_bytes()
        updated = updater.version_text(updater.CHMATE_FILE, original.decode(), '202611080031').encode()
        old_stamp = updater.chmate_version(original.decode()).encode()
        self.assertEqual(updated, original.replace(b'! Version: ' + old_stamp, b'! Version: 202611080031', 1))

    def test_pending_current_jst_checkpoint_and_no_repeat_in_temporary_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            previous = Path.cwd()
            os.chdir(tmp)
            try:
                def git(*args):
                    return subprocess.check_output(['git', *args], text=True, stderr=subprocess.PIPE)
                git('init', '-q')
                git('config', 'user.name', 'Test')
                git('config', 'user.email', 'test@example.invalid')
                path = updater.CHMATE_FILE
                path.parent.mkdir()
                path.write_text(BEFORE)
                git('add', '.')
                git('commit', '-qm', 'base')
                with patch.object(sys, 'argv', ['update', '--pending', '--path', str(path)]), patch.object(updater, 'datetime') as clock:
                    # UTC日付と異なるJSTの実行時刻を使用する。
                    clock.now.return_value = datetime(2026, 11, 7, 15, 31, tzinfo=timezone.utc).astimezone(updater.JST)
                    updater.main()
                    self.assertEqual(clock.now.call_args.args, (updater.JST,))
                    self.assertIn('! Version: 202611080031', path.read_text())
                    git('add', '.')
                    git('commit', '-qm', 'sync')
                    updater.main()
                    self.assertEqual(git('status', '--porcelain'), '')
                    path.write_text(path.read_text() + '! Edited comment\n')
                    self.assertEqual(updater.pending_files(), [path])
                    updater.main()
                    self.assertIn('a|b\n! Edited comment', path.read_text())
                    path.write_text(path.read_text() + '! Version: bad\n')
                    with self.assertRaises(ValueError):
                        updater.main()
            finally:
                os.chdir(previous)

    def test_pr_checks_each_commit_and_does_not_hide_late_fix(self):
        with tempfile.TemporaryDirectory() as tmp:
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=tmp, text=True, stderr=subprocess.PIPE).strip()
            git('init', '-q')
            git('config', 'user.name', 'Test')
            git('config', 'user.email', 'test@example.invalid')
            path = Path(tmp) / updater.CHMATE_FILE
            path.parent.mkdir()
            path.write_text(BEFORE)
            git('add', '.')
            git('commit', '-qm', 'base')
            base = git('rev-parse', 'HEAD')
            path.write_text(BEFORE + '! Missing version update\n')
            git('commit', '-qam', 'edit')
            path.write_text(path.read_text().replace('202611080030', datetime.now(updater.JST).strftime('%Y%m%d%H%M')))
            git('commit', '-qam', 'late fix')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_chmate_version.py'), '--base', base], cwd=tmp, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('JST', result.stderr)


class ChmateMergeHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.previous = Path.cwd()
        os.chdir(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(os.chdir, self.previous)
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('remote', 'add', 'origin', '.')
        updater.CHMATE_FILE.parent.mkdir()
        updater.CHMATE_FILE.write_text(BEFORE)
        self.commit('初期状態', '2026-11-08T00:30:00+09:00')
        self.base = self.git('rev-parse', 'HEAD')
        self.git('switch', '-qc', 'source')

    def git(self, *args):
        return subprocess.check_output(['git', *args], text=True, stderr=subprocess.PIPE).strip()

    def commit(self, title, date):
        self.git('add', '.')
        with patch.dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date):
            self.git('commit', '-qm', title)

    def squash(self, missing=False, merge_date='2026-11-08T00:45:00+09:00'):
        text = BEFORE + '! Dummy edit\n'
        if not missing:
            text = text.replace('202611080030', '202611080031')
        updater.CHMATE_FILE.write_text(text)
        self.commit('本文を編集', '2026-11-08T00:31:00+09:00')
        if missing:
            updater.CHMATE_FILE.write_text(text.replace('202611080030', '202611080031'))
            self.commit('後続Commitで更新', '2026-11-08T00:31:10+09:00')
        self.source = self.git('rev-parse', 'HEAD')
        self.git('switch', '-q', 'main')
        self.git('checkout', 'source', '--', str(updater.CHMATE_FILE))
        self.commit('Squash merge', merge_date)
        self.merged = self.git('rev-parse', 'HEAD')
        return {'merged_at': '2026-11-07T15:45:00Z', 'merge_commit_sha': self.merged,
                'base': {'sha': self.base, 'repo': {'full_name': 'Example/Test'}},
                'head': {'sha': self.source}}

    def verify(self, payload):
        import io
        with patch.dict(os.environ, GITHUB_REPOSITORY='Example/Test', GH_TOKEN='test-placeholder'), patch.object(
            checker.urllib.request, 'urlopen', side_effect=lambda *args, **kwargs: io.BytesIO(json.dumps(payload).encode())
        ):
            return checker.check_history(self.base, self.merged, github_provenance=True)

    def test_delayed_squash_uses_matching_original_history(self):
        pr = self.squash()
        self.assertFalse(checker.check_history(self.base, self.source))
        self.assertTrue(checker.check_history(self.base, self.merged))
        self.assertFalse(self.verify([pr]))

    def test_late_fix_in_original_pr_is_not_hidden_by_squash(self):
        pr = self.squash(missing=True)
        self.assertTrue(self.verify([pr]))

    def test_squash_after_source_incorporates_new_main_target_edit(self):
        pr = self.squash()
        # Squashをまだ行っていないmainと、既存PRのsourceを再現する。
        self.git('reset', '--hard', self.base)
        updater.CHMATE_FILE.write_text(BEFORE.replace('202611080030', '202611080032') + '! Main edit\n')
        self.commit('mainの別編集', '2026-11-08T00:32:00+09:00')
        parent = self.git('rev-parse', 'HEAD')
        self.git('switch', '-q', 'source')
        # Mergeの競合解消後のTreeを作り、両親を記録する。
        updater.CHMATE_FILE.write_text(BEFORE.replace('202611080030', '202611080033') + '! Dummy edit\n! Main edit\n')
        self.git('add', '.')
        tree = self.git('write-tree')
        with patch.dict(os.environ, GIT_AUTHOR_DATE='2026-11-08T00:33:00+09:00', GIT_COMMITTER_DATE='2026-11-08T00:33:00+09:00'):
            source = self.git('commit-tree', tree, '-p', self.source, '-p', parent, '-m', 'mainの変更を統合')
        self.git('reset', '--hard', source)
        self.git('switch', '-q', 'main')
        self.git('checkout', 'source', '--', str(updater.CHMATE_FILE))
        self.commit('Squash merge', '2026-11-08T00:45:00+09:00')
        self.merged = self.git('rev-parse', 'HEAD')
        pr['merge_commit_sha'] = self.merged
        pr['head']['sha'] = source
        # APIのbase SHAがPR作成時のままでも、実際の共通祖先とmainを照合する。
        self.assertFalse(self.verify([pr]))

    def test_fast_squash_also_checks_original_missing_version(self):
        pr = self.squash(missing=True, merge_date='2026-11-08T00:32:00+09:00')
        # Squash後の最終差分だけなら通過しても、元履歴の違反は拒否する。
        self.assertFalse(checker.check_history(self.base, self.merged))
        self.assertTrue(self.verify([pr]))

    def test_open_or_unrelated_pr_and_different_content_do_not_bypass(self):
        pr = self.squash()
        for altered in ({**pr, 'merged_at': None}, {**pr, 'merge_commit_sha': self.source}):
            with self.subTest(pr=altered):
                self.assertTrue(self.verify([altered]))
        updater.CHMATE_FILE.write_text(updater.CHMATE_FILE.read_text() + '! Merge-only edit\n')
        self.commit('追加編集', '2026-11-08T00:46:00+09:00')
        self.merged = self.git('rev-parse', 'HEAD')
        pr['merge_commit_sha'] = self.merged
        self.assertTrue(self.verify([pr]))

    def test_api_error_fails_closed(self):
        self.squash()
        with patch.dict(os.environ, GITHUB_REPOSITORY='Example/Test', GH_TOKEN='test-placeholder'), patch.object(
            checker.urllib.request, 'urlopen', side_effect=OSError('API unavailable')
        ):
            self.assertTrue(checker.check_history(self.base, self.merged, github_provenance=True))

    def test_sync_title_alone_does_not_allow_version_only_commit(self):
        updater.CHMATE_FILE.write_text(BEFORE.replace('202611080030', '202611080031'))
        self.commit('NG Word Regex for ChMate のVersionを更新', '2026-11-08T00:31:00+09:00')
        self.assertTrue(checker.check_history(self.base, 'HEAD'))

    def test_real_bot_sync_requires_matching_new_checkpoint(self):
        updater.CHMATE_FILE.write_text(BEFORE + '! Missed edit\n')
        self.commit('更新漏れ', '2026-11-08T00:31:00+09:00')
        missed = self.git('rev-parse', 'HEAD')
        updater.CHMATE_FILE.write_text(updater.CHMATE_FILE.read_text().replace('202611080030', '202611080032'))
        self.git('config', 'user.name', 'github-actions[bot]')
        self.git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
        self.commit('同期を装ったCommit', '2026-11-08T00:32:00+09:00')
        self.assertTrue(checker.check_history(missed, 'HEAD'))
        digest = hashlib.sha256(updater.version_text(updater.CHMATE_FILE, updater.CHMATE_FILE.read_text(), '<VERSION>').encode()).hexdigest()
        updater.STATE_FILE.parent.mkdir()
        updater.STATE_FILE.write_text(json.dumps({str(updater.CHMATE_FILE): digest}))
        # チェックポイントを同じCommitに含めた正しい同期を別Branchで作る。
        self.git('reset', '--soft', missed)
        self.commit('正しい同期', '2026-11-08T00:32:00+09:00')
        self.assertFalse(checker.check_history(missed, 'HEAD'))
