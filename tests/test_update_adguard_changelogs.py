import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_adguard_changelogs.py"
SPEC = importlib.util.spec_from_file_location("adguard_changelogs", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)

BROWSER = b"# Changelog\n\n## [5.2.0] - 2026-08-21\n\n- MV3 filtering engine supports a new modifier.\n"
ANDROID_JSON = json.dumps([{"name": "AdGuard for Android v4.13.1", "tag_name": "v4.13.1", "published_at": "2026-08-03T00:00:00Z", "html_url": "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.1", "body": "CoreLibs and Scriptlets were updated."}]).encode()


class ChangelogUpdaterTests(unittest.TestCase):
    def test_fetch_retries_transient_network_failure(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = BROWSER
        with (
            patch.object(
                module.urllib.request,
                "urlopen",
                side_effect=[module.URLError("temporary"), response],
            ) as mocked_open,
            patch.object(module.time, "sleep") as mocked_sleep,
        ):
            self.assertEqual(module.fetch("https://example.test/changelog"), BROWSER)
        self.assertEqual(mocked_open.call_count, 2)
        mocked_sleep.assert_called_once_with(1)

    def test_android_release_conversion_and_version(self):
        result = module.android_releases_to_markdown(ANDROID_JSON).decode()
        self.assertIn("## AdGuard for Android v4.13.1", result)
        self.assertEqual(module.latest_version(result), "4.13.1")

    def test_browser_keep_a_changelog_heading(self):
        self.assertEqual(module.latest_version(BROWSER.decode()), "5.2.0")

    def test_relevant_entries_are_flagged(self):
        self.assertEqual(len(module.relevant_lines(BROWSER.decode())), 1)
        self.assertEqual(module.relevant_lines("UI colors changed"), [])

    @patch.object(module, "fetch")
    def test_update_is_deterministic_when_sources_do_not_change(self, mocked_fetch):
        mocked_fetch.side_effect = [BROWSER, ANDROID_JSON, BROWSER, ANDROID_JSON]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            first = datetime(2026, 8, 21, tzinfo=timezone.utc)
            second = datetime(2026, 8, 22, tzinfo=timezone.utc)
            self.assertTrue(module.update(output, "browser", "android", first))
            before = (output / "metadata.json").read_text(encoding="utf-8")
            self.assertFalse(module.update(output, "browser", "android", second))
            self.assertEqual((output / "metadata.json").read_text(encoding="utf-8"), before)

    @patch.object(module, "fetch")
    def test_update_separates_changelogs_from_review_metadata(self, mocked_fetch):
        mocked_fetch.side_effect = [BROWSER, ANDROID_JSON]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            review_dir = root / "upstream"
            changelog_dir = root / "ChangeLog"
            module.update(
                review_dir,
                "browser",
                "android",
                changelog_dir=changelog_dir,
            )
            self.assertTrue((changelog_dir / "adguard-browser-extension-CHANGELOG.source.md").exists())
            self.assertTrue((changelog_dir / "adguard-for-android-CHANGELOG.source.md").exists())
            self.assertTrue((review_dir / "metadata.json").exists())
            self.assertTrue((review_dir / "converter-review.md").exists())
            self.assertFalse((review_dir / "adguard-browser-extension-CHANGELOG.source.md").exists())

    def test_invalid_release_payload_is_rejected(self):
        with self.assertRaises(ValueError):
            module.android_releases_to_markdown(b"[]")


if __name__ == "__main__":
    unittest.main()
