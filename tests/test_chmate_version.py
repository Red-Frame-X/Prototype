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
        checker.check(BEFORE, after, NOW, '{}')
        checker.check(BEFORE, BEFORE, NOW, checkpoint)

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
