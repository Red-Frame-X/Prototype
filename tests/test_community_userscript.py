"""遅延追加されたコミュニティメニューの初期処理と手動選択を検証する。"""
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CommunityMenuTests(unittest.TestCase):
    def test_existing_and_late_layers_process_initial_menu_once(self):
        result = subprocess.run(
            ['node', str(ROOT / 'tests/fixtures/community-menu.cjs'),
             str(ROOT / 'UserScript/x-auto-select-community-latest-sort.user.js')],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
