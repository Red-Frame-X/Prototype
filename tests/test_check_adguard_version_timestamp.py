from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import check_adguard_version_timestamp as check


def filter_text(version: str, rule: str) -> str:
    return f"! Title: test\n! Version: {version}\n{rule}\n"


class AdGuardVersionTimestampTests(unittest.TestCase):
    def test_final_range_check_rejects_version_reverted_after_rule_change(self) -> None:
        target = check.TARGETS[0]
        snapshots = {
            ("commit-one^", target): filter_text("202610051200", "||old.example^"),
            ("commit-one", target): filter_text("202610051201", "||new.example^"),
            ("commit-two^", target): filter_text("202610051201", "||new.example^"),
            ("commit-two", target): filter_text("202610051200", "||new.example^"),
            ("base", target): filter_text("202610051200", "||old.example^"),
            ("head", target): filter_text("202610051200", "||new.example^"),
        }

        def fake_show(ref: str, path: Path) -> str | None:
            return snapshots.get((ref, path))

        with (
            patch.object(check, "git", return_value="commit-one\ncommit-two\n"),
            patch.object(check, "show", side_effect=fake_show),
            patch.object(sys, "argv", ["check", "--base", "base", "--head", "head"]),
        ):
            self.assertEqual(check.main(), 1)

    def test_final_range_check_accepts_updated_version(self) -> None:
        target = check.TARGETS[0]
        snapshots = {
            ("commit-one^", target): filter_text("202610051200", "||old.example^"),
            ("commit-one", target): filter_text("202610051201", "||new.example^"),
            ("base", target): filter_text("202610051200", "||old.example^"),
            ("head", target): filter_text("202610051201", "||new.example^"),
        }

        def fake_show(ref: str, path: Path) -> str | None:
            return snapshots.get((ref, path))

        with (
            patch.object(check, "git", return_value="commit-one\n"),
            patch.object(check, "show", side_effect=fake_show),
            patch.object(sys, "argv", ["check", "--base", "base", "--head", "head"]),
        ):
            self.assertEqual(check.main(), 0)


if __name__ == "__main__":
    unittest.main()
