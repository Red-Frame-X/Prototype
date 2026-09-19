import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/update_version_timestamps.py"
WORKFLOW = ROOT / ".github/workflows/update-version-timestamps.yml"


class VersionHistoryTests(unittest.TestCase):
    def test_multi_commit_push_updates_document_changed_in_first_commit(self):
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        steps = workflow["jobs"]["update-version-timestamps"]["steps"]
        checkout = next(step for step in steps if step.get("uses", "").startswith("actions/checkout@"))
        depth = int(checkout.get("with", {}).get("fetch-depth", 1))

        def git(cwd, *args):
            return subprocess.check_output(["git", *args], cwd=cwd, text=True, stderr=subprocess.PIPE).strip()

        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            source.mkdir()
            git(source, "init")
            git(source, "config", "user.name", "Test")
            git(source, "config", "user.email", "test@example.com")
            document = Path("Markdown Notes/example.md")
            (source / document).parent.mkdir()
            original = "| **Version** | 20000101 |\n\nKeep this paragraph.\n"
            (source / document).write_text(original, encoding="utf-8")
            git(source, "add", ".")
            git(source, "commit", "-m", "base")
            before = git(source, "rev-parse", "HEAD")
            edited = original + "Verified addition.\n"
            (source / document).write_text(edited, encoding="utf-8")
            git(source, "add", ".")
            git(source, "commit", "-m", "edit document")
            (source / "unrelated.txt").write_text("unrelated\n", encoding="utf-8")
            git(source, "add", ".")
            git(source, "commit", "-m", "unrelated change")

            # Use the workflow's actual depth; restoring depth=2 must fail here.
            clone = Path(tmp) / "checkout"
            options = [f"--depth={depth}"] if depth else []
            git(Path(tmp), "clone", *options, source.as_uri(), str(clone))
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--base", before, "--head", "HEAD"],
                cwd=clone, text=True, capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            actual = (clone / document).read_text(encoding="utf-8")
            self.assertRegex(actual, r"\| \*\*Version\*\* \| \d{12} \|")
            self.assertEqual(re.sub(r"\d{12}", "20000101", actual, count=1), edited)
            self.assertEqual(git(clone, "diff", "--name-only"), document.as_posix())
