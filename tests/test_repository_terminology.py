import json
import shlex
import subprocess
import unittest
from pathlib import Path

import yaml

from scripts.check_commit_titles import NON_CANONICAL_NAMES, valid_title
from scripts.check_repository_terminology import OFFICIAL_UI_LABEL, UI_DOCUMENT, violations
from scripts.update_adguard_changelogs import build_review

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTerminologyTests(unittest.TestCase):
    def test_fixed_names_are_accepted_and_old_names_rejected_in_prose(self):
        for old, canonical in NON_CANONICAL_NAMES.items():
            with self.subTest(name=old):
                self.assertEqual(violations("README.md", f"説明\n{old}を更新"), [(2, old, canonical)])
                self.assertEqual(violations("README.md", f"{canonical}を更新"), [])

    def test_official_ui_exception_is_limited_to_the_exact_label_and_document(self):
        self.assertEqual(violations(UI_DOCUMENT, OFFICIAL_UI_LABEL), [])
        self.assertTrue(violations("README.md", OFFICIAL_UI_LABEL))
        self.assertTrue(violations(UI_DOCUMENT, OFFICIAL_UI_LABEL + " / ユーザースクリプトの説明"))

    def test_tracked_repository_uses_canonical_names(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts/check_repository_terminology.py")],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_all_writer_commit_messages_match_the_policy(self):
        expected = {
            "sync.yml": ["uB-filter-by-kdroidwin (AdGuard Optimized) を自動更新"],
            "update-adguard-changelogs.yml": ["AdGuardの変更履歴を自動更新"],
            "update-chmate-ng-version.yml": ["NG Word Regex for ChMate のVersionを更新"],
            "update-version-timestamps.yml": ["chore: Versionの日時を日本標準時で同期"],
        }
        actual = {}
        for path in sorted((ROOT / ".github/workflows").glob("*.yml")):
            workflow = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
            titles = []
            for job in workflow["jobs"].values():
                for step in job.get("steps", []):
                    for line in step.get("run", "").splitlines():
                        if not line.strip().startswith("git commit "):
                            continue
                        tokens = shlex.split(line, comments=True)
                        if tokens[:2] == ["git", "commit"]:
                            self.assertIn("-m", tokens, path.name)
                            title = tokens[tokens.index("-m") + 1]
                            self.assertTrue(valid_title(title), title)
                            titles.append(title)
            if titles:
                actual[path.name] = titles
        self.assertEqual(actual, expected)

    def test_generated_review_matches_its_source_and_keeps_upstream_quotes(self):
        products = json.loads((ROOT / "upstream/adguard/metadata.json").read_text())["products"]
        generated = build_review(products)
        self.assertEqual(generated, (ROOT / "upstream/adguard/converter-review.md").read_bytes())
        self.assertIn("Review済みのPull Request", generated.decode())
        for product in products:
            for entry in product["converter_relevant_entries"]:
                self.assertIn(entry, generated.decode())
