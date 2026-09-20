"""Exercise quoted-path regressions against actual Git output and script CLIs."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
FILENAMES = (
    "注意事項.md",
    "Handling and Reporting GitHub CI Failures (✕).md",
    'tabs\tquotes"and\nnewlines.md',
)


class GitPathHandlingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "core.quotePath", "true")
        (self.repo / "Markdown Notes").mkdir()
        self.template = self.repo / "Markdown Notes/Header Template.md"
        self.template.write_text("| **Version** | yyyymmdd |\n", encoding="utf-8")
        self.paths = [Path("Markdown Notes") / name for name in FILENAMES]
        for path in self.paths:
            self.write(path, 1200)
        self.commit("base")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], cwd=self.repo, text=True, encoding="utf-8",
            stderr=subprocess.PIPE,
        )

    def commit(self, message):
        self.git("add", ".")
        subprocess.run(
            ["git", "commit", "-qm", message], cwd=self.repo, check=True,
            env=os.environ | {
                "GIT_AUTHOR_DATE": "2026-09-20T12:34:00+09:00",
                "GIT_COMMITTER_DATE": "2026-09-20T12:34:00+09:00",
            },
        )

    def write(self, path, lines, stamp="200001010000"):
        text = f"| **Version** | {stamp} |\n"
        text += "".join(f"line {i}\n" for i in range(lines - 1))
        (self.repo / path).write_text(text, encoding="utf-8")
        return text

    def run_script(self, name, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / name), *args], cwd=self.repo,
            text=True, encoding="utf-8", capture_output=True,
        )

    def guard(self, *args):
        return self.run_script("check_large_content_loss.py", "--base-ref", self.base, *args)

    def test_large_net_loss_is_rejected_for_each_unusual_path(self):
        for path in self.paths:
            self.write(path, 350)
        self.commit("large loss")
        result = self.guard()
        self.assertEqual(result.returncode, 1, result.stderr)
        for path in self.paths:
            self.assertIn(f"{path}: +0/-850 (net loss 850)", result.stderr)

    def test_file_deletion_is_rejected_for_each_unusual_path(self):
        for path in self.paths:
            (self.repo / path).unlink()
        self.commit("delete test fixtures")
        result = self.guard()
        self.assertEqual(result.returncode, 1, result.stderr)
        for path in self.paths:
            self.assertIn(f"{path}: file deleted", result.stderr)

    def test_normal_edits_pass(self):
        for path in self.paths:
            self.write(path, 1195)
        self.commit("small edits")
        result = self.guard()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_exact_path_authorization_still_works(self):
        path = self.paths[0]
        self.write(path, 350)
        self.commit("reviewed loss")
        result = self.guard("--allow-deletion-in", str(path))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rename_preserves_before_path_for_retained_ratio(self):
        old = self.paths[0]
        new = Path("Markdown Notes/改名 ✕.md")
        (self.repo / old).rename(self.repo / new)
        self.write(new, 800)
        self.commit("rename and edit")
        self.assertIn("R", self.git("diff", "--name-status", self.base, "HEAD"))
        result = self.guard("--min-retained-ratio", "0.75", "--max-net-loss", "9999")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("retained 800/1200 lines", result.stderr)

    def test_pure_rename_passes(self):
        (self.repo / self.paths[0]).rename(self.repo / "Markdown Notes/改名 ✕.md")
        self.commit("rename only")
        result = self.guard()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_stale_versions_are_rejected_for_each_unusual_path(self):
        for path in self.paths:
            self.write(path, 1201)
        self.commit("edit without version update")
        result = self.run_script("check_markdown_notes_version.py", "--base-ref", self.base)
        self.assertEqual(result.returncode, 1, result.stderr)
        for path in self.paths:
            self.assertIn(f"{path}: Version is 200001010000; expected 202609201234", result.stderr)

    def test_correct_versions_pass_for_each_unusual_path(self):
        for path in self.paths:
            self.write(path, 1201, "202609201234")
        self.commit("edit and update version")
        result = self.run_script("check_markdown_notes_version.py", "--base-ref", self.base)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_updater_changes_only_metadata_and_preserves_template(self):
        expected = {path: self.write(path, 1201) for path in self.paths}
        # Include the template in the diff to verify its explicit exclusion.
        template = self.template.read_text(encoding="utf-8") + "Template note.\n"
        self.template.write_text(template, encoding="utf-8")
        self.commit("edit documents and template")
        result = self.run_script("update_version_timestamps.py", "--base", self.base)
        self.assertEqual(result.returncode, 0, result.stderr)
        for path, before in expected.items():
            actual = (self.repo / path).read_text(encoding="utf-8")
            self.assertRegex(actual.splitlines()[0], r"^\| \*\*Version\*\* \| \d{12} \|$")
            self.assertNotEqual(actual.splitlines()[0], before.splitlines()[0])
            self.assertEqual(actual.splitlines(keepends=True)[1:], before.splitlines(keepends=True)[1:])
        self.assertEqual(self.template.read_text(encoding="utf-8"), template)

    def test_numstat_parser_consumes_binary_rename_and_special_paths(self):
        spec = importlib.util.spec_from_file_location("content_loss", SCRIPTS / "check_large_content_loss.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        old, new = "旧\t名前.md", "新\n名前.md"
        output = "-\t-\t\0old.bin\0new.bin\0" + f"1\t2\t\0{old}\0{new}\0"
        self.assertEqual(list(module.parse_numstat(output)), [(1, 2, new, old)])
