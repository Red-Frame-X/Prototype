import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "update_ubol_metadata.py"
SPEC = importlib.util.spec_from_file_location("ubol_metadata", MODULE_PATH)
metadata = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = metadata
SPEC.loader.exec_module(metadata)

CHANGELOG = b"""# Changelog

### 2026.700.1000

- New feature

### 2026.621.1813

- Add ability to subscribe to filter lists from remote servers
"""


class MetadataTests(unittest.TestCase):
    def test_extracts_latest_version_and_feature_metadata(self):
        result = metadata.build_metadata(
            CHANGELOG,
            "test.md",
            "2026-08-21T00:00:00+00:00",
        )
        self.assertEqual(result["latest_version"], "2026.700.1000")
        feature = result["tracked_features"]["remote_filter_list_subscriptions"]
        self.assertEqual(feature["supported_since"], "2026.621.1813")
        self.assertFalse(feature["safari_supported"])

    def test_rejects_unexpected_changelog_format(self):
        with self.assertRaises(ValueError):
            metadata.build_metadata(b"No version headings", "test.md", "now")

    def test_unchanged_changelog_does_not_rewrite_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "CHANGELOG.md"
            output = Path(directory) / "metadata.json"
            source.write_bytes(CHANGELOG)
            first_time = datetime(2026, 8, 21, tzinfo=timezone.utc)
            second_time = datetime(2026, 8, 22, tzinfo=timezone.utc)

            self.assertTrue(metadata.update(str(source), output, first_time))
            first = output.read_text(encoding="utf-8")
            self.assertFalse(metadata.update(str(source), output, second_time))
            self.assertEqual(output.read_text(encoding="utf-8"), first)

    def test_changed_changelog_updates_file(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "CHANGELOG.md"
            output = Path(directory) / "metadata.json"
            source.write_bytes(CHANGELOG)
            metadata.update(str(source), output)
            source.write_bytes(
                CHANGELOG.replace(b"2026.700.1000", b"2026.701.1000")
            )

            self.assertTrue(metadata.update(str(source), output))
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["latest_version"], "2026.701.1000")

    def test_writes_source_mirror_for_translation(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "CHANGELOG.md"
            output = Path(directory) / "metadata.json"
            source_output = Path(directory) / "CHANGELOG.source.md"
            source.write_bytes(CHANGELOG)

            self.assertTrue(
                metadata.update(
                    str(source),
                    output,
                    source_output=source_output,
                )
            )
            self.assertEqual(source_output.read_bytes(), CHANGELOG)


if __name__ == "__main__":
    unittest.main()
