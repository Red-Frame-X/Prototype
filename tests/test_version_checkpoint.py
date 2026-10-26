import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from unittest.mock import patch

from scripts.update_version_timestamps import JST, STATE_FILE, main, pending_files, update_file

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/update_version_timestamps.py'


class VersionCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.previous = Path.cwd()
        os.chdir(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(os.chdir, self.previous)
        self.git('init', '-q')
        # Git 2.55では少量のobjectでも自動保守が起動する。一時Repositoryの
        # 削除後まで書き込みが続かないよう、このfixture内だけ自動起動を止める。
        # https://github.com/git/git/blob/v2.55.0/Documentation/config/maintenance.adoc
        self.git('config', '--local', 'maintenance.auto', 'false')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.files = {
            Path('Markdown Notes/note.md'): '| **Version** | 200001010000 |\nBody.\n',
            Path('AdGuard Custom Rules/filter.txt'): '! Version: 200001010000\n||example.org^\n',
            Path('UserScript/test.user.js'): '// ==UserScript==\n// @version 200001010000\n// ==/UserScript==\nvoid 0;\n',
            Path('NG Word Regex for ChMate/words.txt'): '! Version: 200001010000\nword\n',
        }
        for path, text in self.files.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        self.commit('base')
        self.sync()
        self.commit('initial synchronization')

    def git(self, *args):
        return subprocess.check_output(['git', *args], text=True, stderr=subprocess.PIPE).strip()

    def commit(self, message):
        self.git('add', '.')
        self.git('commit', '-qm', message)

    def sync(self, mode='--pending'):
        subprocess.run([sys.executable, str(SCRIPT), mode], check=True, capture_output=True, text=True)

    def test_commits_and_sync_do_not_start_automatic_maintenance(self):
        # 古いGitでも確実に保守対象になるよう、loose objectの閾値を下げる。
        self.git('config', 'maintenance.loose-objects.enabled', 'true')
        self.git('config', 'maintenance.loose-objects.auto', '1')
        self.git('config', 'maintenance.gc.enabled', 'false')
        path = next(iter(self.files))
        path.write_text(path.read_text() + 'Maintenance regression.\n')
        trace = Path('.git/maintenance-trace.json').resolve()
        with patch.dict(os.environ, GIT_TRACE2_EVENT=str(trace)):
            self.commit('edit before maintenance check')
            self.sync()
            self.commit('synchronize before maintenance check')
        events = [json.loads(line) for line in trace.read_text().splitlines()]
        self.assertFalse(any(event.get('event') == 'child_start'
                             and 'maintenance' in event.get('argv', []) for event in events))
        self.assertEqual(pending_files(), [])
        self.assertIn('Maintenance regression.', path.read_text())
        packs = Path('.git/objects/pack')
        self.assertEqual(list(packs.glob('*.pack')), [])

        # 同じRepositoryで自動起動を有効にすると実際にpackが作られることも確認。
        # 正の対照では同期実行し、Test自身がバックグラウンド処理を残さない。
        self.git('-c', 'maintenance.auto=true', '-c', 'maintenance.autoDetach=false',
                 'commit', '--allow-empty', '-qm', 'maintenance positive control')
        self.assertTrue(list(packs.glob('*.pack')))
        self.git('fsck', '--no-dangling')

    def test_web_and_api_edits_multiple_files_and_bot_body_are_recovered(self):
        for actor in ('GitHub', 'ChatGPT API', 'github-actions[bot]'):
            with self.subTest(actor=actor):
                self.git('config', 'user.name', actor)
                before = {}
                for path in self.files:
                    update_file(path, '200001010000')
                    path.write_text(path.read_text() + f'Comment by {actor}.\n')
                    before[path] = path.read_text()
                self.commit('chore: sync Version timestamps (JST)')
                self.assertEqual(set(pending_files()), set(self.files))
                self.sync()
                for path in self.files:
                    self.assertNotEqual(path.read_text(), before[path])
                    self.assertIn(f'Comment by {actor}.', path.read_text())
                self.commit('synchronized')
                self.assertEqual(pending_files(), [])
                self.sync()
                self.assertEqual(self.git('status', '--porcelain'), '')

    def test_missed_edit_survives_later_version_only_commit_and_dispatch(self):
        path = next(iter(self.files))
        path.write_text(path.read_text() + 'Missed edit.\n')
        self.commit('first edit with no workflow')
        path.write_text(path.read_text() + 'Latest edit.\n')
        self.commit('second edit with cancelled workflow')
        update_file(path, '200001010001')
        self.commit('Version only, not a content checkpoint')
        self.assertEqual(pending_files(), [path])
        self.sync()
        self.assertIn('Missed edit.\nLatest edit.', path.read_text())
        self.assertNotIn('200001010001', path.read_text())
        self.commit('fallback synchronization')
        self.assertEqual(pending_files(), [])

    def test_only_real_header_is_normalized_and_same_minute_is_checkpointed(self):
        path = next(iter(self.files))
        path.write_text(path.read_text() + '```\n| **Version** | 200001010000 |\n```\n')
        self.commit('add example')
        self.sync()
        self.commit('sync example')
        path.write_text(path.read_text().replace('200001010000', '200001010001'))
        self.commit('edit example version')
        self.assertEqual(pending_files(), [path])
        self.sync()
        self.commit('checkpoint, even if metadata minute did not change')
        self.assertEqual(pending_files(), [])
        self.assertIn('| **Version** | 200001010001 |\n```', path.read_text())

    def test_manual_version_only_no_repeat_new_deleted_and_excluded(self):
        for path in self.files:
            update_file(path, '200001010001')
        self.commit('manual metadata only')
        self.assertEqual(pending_files(), [])
        path = Path('Markdown Notes/new.md')
        path.write_text('| **Version** | 200001010000 |\nNew.\n')
        excluded = Path('Markdown Notes/Header Template.md')
        excluded.write_text(path.read_text())
        binary = Path('Markdown Notes/binary.md')
        binary.write_bytes(b'\xff\x00')
        deleted = next(iter(self.files))
        deleted.unlink()
        self.commit('new, removed, excluded, binary')
        self.assertEqual(pending_files(), [path])
        self.sync()
        state = json.loads(STATE_FILE.read_text())
        self.assertNotIn(str(deleted), state)
        self.assertIn(str(path), state)
        self.assertNotIn(str(excluded), state)
        self.assertFalse(deleted.exists())
        self.assertIn('200001010000', excluded.read_text())
        self.commit('sync creation and deletion')
        self.assertEqual(pending_files(), [])

    def test_same_minute_edit_publishes_checkpoint_without_rewriting_metadata(self):
        fixed = datetime(2026, 10, 21, 23, 30, tzinfo=JST)
        with patch('scripts.update_version_timestamps.datetime') as clock, patch.object(sys, 'argv', ['update', '--pending']):
            clock.now.return_value = fixed
            path = next(iter(self.files))
            path.write_text(path.read_text() + 'First edit.\n')
            self.commit('first')
            main()
            self.commit('sync first')
            path.write_text(path.read_text() + 'Second edit.\n')
            self.commit('second in the same minute')
            self.assertEqual(pending_files(), [path])
            before = path.read_text()
            main()
            self.assertEqual(path.read_text(), before)
            self.assertEqual(self.git('diff', '--name-only'), STATE_FILE.as_posix())
            self.commit('sync second checkpoint')
            self.assertEqual(pending_files(), [])
            main()
            self.assertEqual(self.git('status', '--porcelain'), '')

    def test_jst_date_boundary_is_used_instead_of_utc(self):
        fixed = datetime(2026, 10, 25, 0, 30, tzinfo=JST)
        path = Path('AdGuard Custom Rules/filter.txt')
        path.write_text(path.read_text() + 'JST boundary edit.\n')
        self.commit('edit across UTC date boundary')
        with patch('scripts.update_version_timestamps.datetime') as clock, patch.object(sys, 'argv', ['update', '--pending']):
            clock.now.return_value = fixed
            main()
        self.assertIn('! Version: 202610250030', path.read_text())


if __name__ == '__main__':
    unittest.main()
