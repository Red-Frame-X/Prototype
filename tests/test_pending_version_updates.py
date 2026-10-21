import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

import yaml

from scripts.update_version_timestamps import pending_files, update_file

ROOT = Path(__file__).resolve().parents[1]


class PendingVersionTests(unittest.TestCase):
    def test_manual_comment_edits_all_supported_files_and_no_repeat(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, text=True)

            git('init', '-q')
            git('config', 'user.name', 'Test')
            git('config', 'user.email', 'test@example.invalid')
            sources = [
                *ROOT.glob('AdGuard Custom Rules/*.txt'),
                *ROOT.glob('NG Word Regex for ChMate/*.txt'),
                *ROOT.glob('Markdown Notes/*.md'),
                *ROOT.glob('UserScript/*.user.js'),
            ]
            expected = []
            for source in sources:
                relative = source.relative_to(ROOT)
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(source.read_bytes())
                if source.name != 'Header Template.md':
                    expected.append(relative)
            git('add', '.')
            git('commit', '-qm', 'base')
            for relative in expected:
                path = root / relative
                suffix = '\n// Manual comment edit.\n' if path.suffix == '.js' else '\n! Manual comment edit.\n' if path.suffix == '.txt' else '\n<!-- Manual comment edit. -->\n'
                path.write_text(path.read_text() + suffix)
            git('commit', '-qam', 'manual comments only')
            before = {p: (root / p).read_text() for p in expected}
            old = Path.cwd()
            os.chdir(root)
            try:
                self.assertEqual(set(pending_files()), set(expected))
                for path in pending_files():
                    self.assertTrue(update_file(path, '209901010001'), str(path))
                    actual = path.read_text()
                    self.assertIn('Manual comment edit.', actual)
                    pattern = (r"(?m)^(//[ \t]*@version[ \t]+)\S+" if path.suffix == ".js"
                               else r"(?m)^(! Version: )\d+" if path.suffix == ".txt"
                               else r"(?m)^(\| \*\*Version\*\* \| )\d+")
                    self.assertEqual(actual, re.sub(pattern, r"\g<1>209901010001", before[path], count=1))
                git('commit', '-qam', 'chore: sync Version timestamps (JST)')
                self.assertEqual(pending_files(), [])
                # A new comment after synchronization must be picked up again.
                path = expected[0]
                path.write_text(path.read_text() + '! Another comment.\n')
                git('commit', '-qam', 'another manual comment')
                self.assertEqual(pending_files(), [path])
            finally:
                os.chdir(old)


class WebEditWorkflowTests(unittest.TestCase):
    def test_web_push_and_recovery_events_are_enabled(self):
        workflow = yaml.load((ROOT / '.github/workflows/update-version-timestamps.yml').read_text(), Loader=yaml.BaseLoader)
        self.assertEqual(workflow['on']['push']['branches'], ['main'])
        self.assertNotIn('paths', workflow['on']['push'])
        self.assertIn('schedule', workflow['on'])
        self.assertIn('workflow_dispatch', workflow['on'])
        condition = workflow['jobs']['update-version-timestamps']['if']
        self.assertNotIn("github.actor", condition)
        self.assertIn("github.event.workflow_run.event == 'push'", condition)
        self.assertIn("github.event.workflow_run.head_repository.full_name == github.repository", condition)
        self.assertIn("workflow_run", workflow["on"])
