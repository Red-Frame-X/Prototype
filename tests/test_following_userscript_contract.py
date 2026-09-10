import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "UserScript"
    / "x-auto-select-following-latest-sort.user.js"
)


class FollowingLatestUserScriptContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCRIPT.read_text(encoding="utf-8")

    def test_supports_japanese_and_english_latest_labels(self):
        self.assertIn("new Set(['最新', 'Latest'])", self.source)

    def test_accepts_menuitem_role_variants(self):
        self.assertIn("querySelectorAll('[role^=\"menuitem\"]')", self.source)

    def test_honors_aria_checked_selected_state(self):
        self.assertIn("getAttribute('aria-checked') === 'true'", self.source)

    def test_keeps_svg_selected_state_fallback(self):
        self.assertIn("querySelector('svg') !== null", self.source)


if __name__ == "__main__":
    unittest.main()
