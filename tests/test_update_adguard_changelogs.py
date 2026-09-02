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
BROWSER_UNRELEASED = b"# Changelog\n\n## Unreleased 5.5.2\n\n- MV3 filtering engine fix.\n\n## [5.5.1.0]\n\n- Previous release.\n"
BROWSER_RELEASES_JSON = json.dumps([
    {
        "name": "AdGuard Browser Extension v5.5.2.3",
        "tag_name": "v5.5.2.3",
        "published_at": "2026-08-26T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.5.2.3",
        "body": "Updated MV3 filtering engine behavior.",
        "draft": False,
        "prerelease": False,
    },
    {
        "name": "AdGuard Browser Extension v5.6.0-beta.1",
        "tag_name": "v5.6.0-beta.1",
        "published_at": "2026-08-27T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.6.0-beta.1",
        "body": "Beta Scriptlets update.",
        "draft": False,
        "prerelease": True,
    },
]).encode()
ANDROID_JSON = json.dumps([{
    "name": "AdGuard for Android v4.13.1",
    "tag_name": "v4.13.1",
    "published_at": "2026-08-03T00:00:00Z",
    "html_url": "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.1",
    "body": "CoreLibs and Scriptlets were updated.",
    "draft": False,
    "prerelease": False,
}]).encode()

BROWSER_RELEASES_NO_RELEVANT = json.dumps([
    {
        "name": "AdGuard Browser Extension v5.5.2.3",
        "tag_name": "v5.5.2.3",
        "published_at": "2026-08-26T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.5.2.3",
        "body": "UI colors and translations were updated.",
        "draft": False,
        "prerelease": False,
    }
]).encode()

ANDROID_RELEASES_WITH_HISTORY = json.dumps([
    {
        "name": "AdGuard for Android v4.14.0-beta.1",
        "tag_name": "v4.14.0-beta.1",
        "published_at": "2026-08-30T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.14.0-beta.1",
        "body": "Beta Scriptlets changes.",
        "draft": False,
        "prerelease": True,
    },
    {
        "name": "AdGuard for Android v4.13.2",
        "tag_name": "v4.13.2",
        "published_at": "2026-08-26T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.2",
        "body": "UI stability improvements.",
        "draft": False,
        "prerelease": False,
    },
    {
        "name": "AdGuard for Android v4.13.1",
        "tag_name": "v4.13.1",
        "published_at": "2026-08-03T00:00:00Z",
        "html_url": "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.1",
        "body": "Updated CoreLibs and Scriptlets.",
        "draft": False,
        "prerelease": False,
    },
]).encode()


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

    def test_browser_latest_stable_release_comes_from_github_releases(self):
        release = module.latest_stable_release(BROWSER_RELEASES_JSON, "Browser Extension")
        self.assertEqual(release["version"], "5.5.2.3")
        self.assertEqual(release["body"], "Updated MV3 filtering engine behavior.")
        self.assertEqual(
            release["release_url"],
            "https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.5.2.3",
        )

    def test_browser_release_detection_ignores_unreleased_changelog_heading(self):
        self.assertEqual(module.latest_version(BROWSER_UNRELEASED.decode()), "5.5.1.0")
        release = module.latest_stable_release(BROWSER_RELEASES_JSON, "Browser Extension")
        self.assertEqual(release["version"], "5.5.2.3")

    def test_relevant_entries_are_flagged(self):
        self.assertEqual(len(module.relevant_lines(BROWSER.decode())), 1)
        self.assertEqual(module.relevant_lines("UI colors changed"), [])

    @patch.object(module, "fetch")
    def test_update_is_deterministic_when_sources_do_not_change(self, mocked_fetch):
        mocked_fetch.side_effect = [
            BROWSER,
            BROWSER_RELEASES_JSON,
            ANDROID_JSON,
            BROWSER,
            BROWSER_RELEASES_JSON,
            ANDROID_JSON,
        ]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            first = datetime(2026, 8, 21, tzinfo=timezone.utc)
            second = datetime(2026, 8, 22, tzinfo=timezone.utc)
            self.assertTrue(module.update(output, "browser", "android", first, browser_releases_source="browser-releases"))
            before = (output / "metadata.json").read_text(encoding="utf-8")
            self.assertFalse(module.update(output, "browser", "android", second, browser_releases_source="browser-releases"))
            self.assertEqual((output / "metadata.json").read_text(encoding="utf-8"), before)

    @patch.object(module, "fetch")
    def test_update_uses_release_version_when_changelog_is_still_unreleased(self, mocked_fetch):
        mocked_fetch.side_effect = [BROWSER_UNRELEASED, BROWSER_RELEASES_JSON, ANDROID_JSON]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            module.update(output, "browser", "android", browser_releases_source="browser-releases")
            data = json.loads((output / "metadata.json").read_text(encoding="utf-8"))
            browser = data["products"][0]
            self.assertEqual(browser["latest_version"], "5.5.2.3")
            self.assertEqual(
                browser["release_url"],
                "https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.5.2.3",
            )

    @patch.object(module, "fetch")
    def test_review_entries_only_use_latest_stable_release_body(self, mocked_fetch):
        mocked_fetch.side_effect = [
            BROWSER,
            BROWSER_RELEASES_NO_RELEVANT,
            ANDROID_RELEASES_WITH_HISTORY,
        ]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            module.update(output, "browser", "android", browser_releases_source="browser-releases")
            data = json.loads((output / "metadata.json").read_text(encoding="utf-8"))
            browser, android = data["products"]

            # The Browser changelog contains MV3/filtering keywords, but the
            # latest stable release body does not, so historical entries must
            # not be attributed to v5.5.2.3.
            self.assertEqual(browser["latest_version"], "5.5.2.3")
            self.assertEqual(browser["converter_relevant_entries"], [])

            # A newer beta and an older stable contain Scriptlets/CoreLibs, but
            # the latest stable v4.13.2 does not. Neither may leak into 4.13.2.
            self.assertEqual(android["latest_version"], "4.13.2")
            self.assertEqual(android["converter_relevant_entries"], [])
            self.assertEqual(
                android["release_url"],
                "https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.2",
            )

    @patch.object(module, "fetch")
    def test_update_separates_changelogs_from_review_metadata(self, mocked_fetch):
        mocked_fetch.side_effect = [BROWSER, BROWSER_RELEASES_JSON, ANDROID_JSON]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            review_dir = root / "upstream"
            changelog_dir = root / "ChangeLog"
            module.update(
                review_dir,
                "browser",
                "android",
                changelog_dir=changelog_dir,
                browser_releases_source="browser-releases",
            )
            self.assertTrue((changelog_dir / "adguard-browser-extension-CHANGELOG.source.md").exists())
            self.assertTrue((changelog_dir / "adguard-for-android-CHANGELOG.source.md").exists())
            self.assertTrue((review_dir / "metadata.json").exists())
            self.assertTrue((review_dir / "converter-review.md").exists())
            self.assertFalse((review_dir / "adguard-browser-extension-CHANGELOG.source.md").exists())

    def test_invalid_release_payload_is_rejected(self):
        with self.assertRaises(ValueError):
            module.android_releases_to_markdown(b"[]")
        with self.assertRaises(ValueError):
            module.latest_stable_release(b"[]", "Browser Extension")


if __name__ == "__main__":
    unittest.main()
