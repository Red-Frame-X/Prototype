"""PR #292で適用した間接依存の安全な固定が維持されることを検証する。"""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DependencyOverrideRegressionTests(unittest.TestCase):
    def test_markdownlint_overrides_match_installed_lockfile(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        lock = json.loads((ROOT / "package-lock.json").read_text(encoding="utf-8"))
        overrides = package["overrides"]["markdownlint-cli2"]
        expected = {
            "markdown-it": "14.3.3",
            "js-yaml": "5.4.1",
            "smol-toml": "1.9.1",
        }
        self.assertEqual(overrides, expected)
        self.assertEqual(
            lock["packages"]["node_modules/markdown-it"]["version"],
            expected["markdown-it"],
        )
        self.assertEqual(
            lock["packages"]["node_modules/markdownlint-cli2/node_modules/js-yaml"]["version"],
            expected["js-yaml"],
        )
        self.assertEqual(
            lock["packages"]["node_modules/smol-toml"]["version"],
            expected["smol-toml"],
        )
        self.assertEqual(
            lock["packages"][""]["devDependencies"],
            package["devDependencies"],
        )


if __name__ == "__main__":
    unittest.main()
