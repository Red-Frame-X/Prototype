"""配布・同期のAGLint実行環境で既知のprototype操作を拒否する。"""
import json
import shlex
import subprocess
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROBE = r'''
const assert = require('node:assert/strict');
const merge = require('deepmerge');
assert.throws(() => merge(JSON.parse('{"__proto__":{"poisoned":true}}'), {}),
              {code: 'ERR_PROTO_ACCESS'});
assert.deepEqual(merge({rules: {first: 'error'}}, {rules: {second: 'warn'}}),
                 {rules: {first: 'error', second: 'warn'}});
'''


class AGLintRuntimeSecurityTests(unittest.TestCase):
    def test_configured_runtimes_reject_poisoning_and_preserve_normal_merge(self):
        package = json.loads((ROOT / 'package.json').read_text())
        workflow = yaml.load((ROOT / '.github/workflows/sync.yml').read_text(), Loader=yaml.BaseLoader)
        commands = [package['scripts']['lint:adguard']]
        for step in workflow['jobs']['build']['steps']:
            commands.extend(line.strip() for line in step.get('run', '').splitlines()
                            if 'index.cli.js' in line and not line.lstrip().startswith('#'))
        self.assertEqual(len(commands), 2)
        for command in commands:
            with self.subTest(command=command):
                args = shlex.split(command)
                entrypoint = args.index('node_modules/@adguard/aglint/dist/index.cli.js')
                result = subprocess.run([*args[:entrypoint], '-e', PROBE], cwd=ROOT,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
