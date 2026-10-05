import contextlib
import io
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from scripts import check_adguard_version_timestamp as validator
from scripts.update_version_timestamps import update_file

ROOT = Path(__file__).resolve().parents[1]


def git(cwd, *args):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True, stderr=subprocess.PIPE).strip()


def init_repo(root):
    git(root, 'init', '-q', '-b', 'main')
    git(root, 'config', 'user.name', 'Test')
    git(root, 'config', 'user.email', 'test@example.invalid')


class MetadataScopeTests(unittest.TestCase):
    def test_real_markdown_keeps_userscript_example(self):
        source = ROOT / 'Markdown Notes/Distributing Filters and UserScripts with GitHub Gist.md'
        before = source.read_text()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / source.name
            path.write_text(before)
            self.assertTrue(update_file(path, '202610050950'))
            self.assertEqual(path.read_text(), re.sub(
                r'(?m)^\| \*\*Version\*\* \| \d{12} \|$',
                '| **Version** | 202610050950 |', before, count=1))

    def test_code_fences_do_not_supply_document_metadata(self):
        for fence in ('```', '~~~'):
            with self.subTest(fence=fence), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'example.md'
                before = f'# Example\n{fence}\n| **Version** | 202609040000 |\n{fence}\n'
                path.write_text(before)
                self.assertFalse(update_file(path, '202610050950'))
                self.assertEqual(path.read_text(), before)

    def test_userscript_body_and_blank_lines_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'example.user.js'
            before = ('// ==UserScript==\n// @version 1.0.0\n\n// ==/UserScript==\n'
                      '// @version example-in-body\n')
            path.write_text(before)
            self.assertTrue(update_file(path, '202610050950'))
            self.assertEqual(path.read_text(), before.replace('1.0.0', '202610050950', 1))

    def test_filter_body_metadata_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'filter.txt'
            before = '! Version: 202609040000\n||example.org^\n! Version: 202609040001\n'
            path.write_text(before)
            self.assertTrue(update_file(path, '202610050950'))
            self.assertEqual(path.read_text(), before.replace('202609040000', '202610050950', 1))


class PerCommitVersionTests(unittest.TestCase):
    def check_history(self, separate):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_repo(root)
            path = root / validator.TARGETS[0]
            path.parent.mkdir()
            path.write_text('! Version: 202610050900\n||old.example^\n')
            git(root, 'add', '.')
            git(root, 'commit', '-qm', 'base')
            base = git(root, 'rev-parse', 'HEAD')
            path.write_text(path.read_text() + '||new.example^\n')
            if separate:
                git(root, 'commit', '-qam', 'rule only')
            path.write_text(path.read_text().replace('202610050900', '202610050901'))
            git(root, 'commit', '-qam', 'update version')
            with patch.object(validator, 'ROOT', root), patch.object(
                sys, 'argv', ['check', '--base', base, '--head', 'HEAD']
            ), contextlib.redirect_stdout(io.StringIO()):
                return validator.main()

    def test_rejects_version_fixed_in_a_later_commit(self):
        self.assertEqual(self.check_history(separate=True), 1)

    def test_accepts_rule_and_version_in_same_commit(self):
        self.assertEqual(self.check_history(separate=False), 0)


class TimestampPublicationTests(unittest.TestCase):
    def test_actual_workflow_retries_push_and_keeps_concurrent_edit(self):
        workflow = yaml.load((ROOT / '.github/workflows/update-version-timestamps.yml').read_text(), Loader=yaml.BaseLoader)
        command = next(s['run'] for s in workflow['jobs']['update-version-timestamps']['steps'] if 'run' in s)
        command = command.replace('${{ github.event_name }}', 'push')
        real_git = shutil.which('git')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            source.mkdir()
            init_repo(source)
            for name in ('AdGuard Custom Rules', 'Markdown Notes', 'NG Word Regex for ChMate', 'UserScript', 'scripts'):
                (source / name).mkdir()
                (source / name / 'README.md').write_text('Fixture\n')
            shutil.copy(ROOT / 'scripts/update_version_timestamps.py', source / 'scripts')
            rel = 'Markdown Notes/note.md'
            path = source / rel
            path.write_text('| **Version** | 200001010000 |\nOriginal body.\n')
            git(source, 'add', '.')
            git(source, 'commit', '-qm', 'base')
            base = git(source, 'rev-parse', 'HEAD')
            path.write_text(path.read_text() + 'Event edit.\n')
            git(source, 'commit', '-qam', 'event')
            remote = root / 'remote.git'
            git(root, 'clone', '--bare', str(source), str(remote))
            checkout = root / 'checkout'
            competitor = root / 'competitor'
            git(root, 'clone', str(remote), str(checkout))
            git(root, 'clone', str(remote), str(competitor))
            git(competitor, 'config', 'user.name', 'Test')
            git(competitor, 'config', 'user.email', 'test@example.invalid')
            wrapper_dir = root / 'bin'
            wrapper_dir.mkdir()
            marker = root / 'injected'
            wrapper = wrapper_dir / 'git'
            wrapper.write_text(f'''#!{sys.executable}
import os, subprocess, sys
from pathlib import Path
real = {real_git!r}
other = {str(competitor)!r}
marker = Path({str(marker)!r})
if sys.argv[1:2] == ['push'] and not marker.exists():
    marker.write_text('once')
    path = Path(other) / {rel!r}
    path.write_text(path.read_text().replace('200001010000', '200001010001') + 'Concurrent body edit.\\n')
    subprocess.run([real, 'commit', '-qam', 'concurrent'], cwd=other, check=True)
    subprocess.run([real, 'push', 'origin', 'HEAD:main'], cwd=other, check=True)
os.execv(real, [real, *sys.argv[1:]])
''')
            wrapper.chmod(0o755)
            env = dict(os.environ, BEFORE_SHA=base, PATH=str(wrapper_dir) + os.pathsep + os.environ['PATH'])
            result = subprocess.run(['bash', '-c', command], cwd=checkout, env=env, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(marker.exists())
            self.assertIn('[rejected]', result.stderr)
            published = git(root, '--git-dir', str(remote), 'show', f'main:{rel}')
            self.assertRegex(published, r'^\| \*\*Version\*\* \| \d{12} \|')
            self.assertIn('Original body.\nEvent edit.\nConcurrent body edit.', published)
            self.assertNotIn('200001010001', published)
            self.assertEqual(git(checkout, 'status', '--porcelain'), '')


if __name__ == '__main__':
    unittest.main()
