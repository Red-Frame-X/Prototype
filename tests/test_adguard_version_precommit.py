from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    'AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt',
    'AdGuard Custom Rules/AdGuard DNS Custom Rules - Red Frame X.txt',
)


class VersionPrecommitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('scripts/check_chmate_version.py', 'scripts/update_version_timestamps.py', 'scripts/check_adguard_version_timestamp.py', 'scripts/check_adguard_user_rule_edit.py', '.githooks/pre-commit'):
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, dest)
        # Markdown検査の依存を分離し、実際のHookによるVersion判定を検証する。
        (self.root / 'node_modules').mkdir()
        tools = self.root / 'test-bin'
        tools.mkdir()
        npm = tools / 'npm'
        npm.write_text('#!/bin/sh\nexit 0\n')
        npm.chmod(0o755)
        self.env = dict(os.environ, PATH=str(tools) + os.pathsep + os.environ['PATH'])
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.com')
        for name in TARGETS:
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text('! Version: 202611080900\nexample.com##.old\n')
        self.git('add', '.')
        self.git('commit', '-qm', '初期状態')
        self.git('config', 'core.hooksPath', '.githooks')

    def git(self, *args, check=True):
        return subprocess.run(['git', *args], cwd=self.root, text=True,
                              capture_output=True, check=check, env=self.env)

    def edit(self, name, stamp='202611080900'):
        (self.root / name).write_text(f'! Version: {stamp}\nexample.com##.old\nexample.com##.new\n')

    def test_hook_rejects_rule_changes_without_version_for_both_filters(self):
        for name in TARGETS:
            with self.subTest(name=name):
                self.edit(name)
                self.git('add', name)
                result = self.git('commit', '-qm', 'ルールを変更', check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('ステージ済みのルール変更にVersion更新がありません', result.stdout + result.stderr)
                self.git('reset', '--hard', 'HEAD')

    def test_unstaged_version_update_cannot_bypass_hook(self):
        self.edit(TARGETS[0])
        self.git('add', TARGETS[0])
        self.edit(TARGETS[0], '202611080901')
        result = self.git('commit', '-qm', 'ルールを変更', check=False)
        self.assertNotEqual(result.returncode, 0)

    def test_hook_accepts_rule_and_version_in_same_commit(self):
        self.edit(TARGETS[0], '202611080901')
        self.git('add', TARGETS[0])
        self.git('commit', '-qm', 'ルールとVersionを更新')

    def test_hook_rejects_unapproved_removal_with_version_update(self):
        (self.root / TARGETS[0]).write_text('! Version: 202611080901\n')
        self.git('add', TARGETS[0])
        result = self.git('commit', '-qm', 'ルールを削除', check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('明示的な承認がない', result.stdout + result.stderr)

    def test_hook_accepts_unrelated_commit(self):
        (self.root / 'other.txt').write_text('無関係な変更\n')
        self.git('add', 'other.txt')
        self.git('commit', '-qm', '別のファイルを更新')

    def test_hook_rejects_invalid_version(self):
        self.edit(TARGETS[0], '202613080901')
        self.git('add', TARGETS[0])
        self.assertNotEqual(self.git('commit', '-qm', '不正な日時', check=False).returncode, 0)


if __name__ == '__main__':
    unittest.main()
