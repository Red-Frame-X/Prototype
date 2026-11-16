"""依存不足・不完全なNode.js導入を全Test実行前に検出する。"""

from importlib import metadata
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts import check_local_validation_environment as check


class LocalValidationEnvironmentTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        importer = patch.object(check, "import_module")
        self.importer = importer.start()
        self.addCleanup(importer.stop)
        (self.root / "requirements-ci.txt").write_text(
            "# CI依存\nPyYAML==6.0.2\nmarkdown-it-py==4.2.0\n", encoding="utf-8",
        )
        (self.root / "package.json").write_text(json.dumps({
            "devDependencies": {"@adguard/aglint": "3.0.2"},
        }), encoding="utf-8")
        (self.root / "package-lock.json").write_text(json.dumps({
            "packages": {"node_modules/@adguard/aglint": {"version": "3.0.2"}},
        }), encoding="utf-8")

    def install_node_manifest(self, version="3.0.2"):
        path = self.root / "node_modules/@adguard/aglint/package.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"version": version}), encoding="utf-8")

    def test_collects_python_and_node_failures_without_starting_aglint(self):
        with patch.object(check.metadata, "version", side_effect=metadata.PackageNotFoundError), \
                patch.object(check.shutil, "which", return_value=None), \
                patch.object(check.subprocess, "run") as run:
            errors = check.check_environment(self.root)
        self.assertTrue(any("PyYAML" in error for error in errors))
        self.assertTrue(any("markdown-it-py" in error for error in errors))
        self.assertTrue(any("@adguard/aglint" in error for error in errors))
        self.assertTrue(any("Node.jsが見つかりません" in error for error in errors))
        run.assert_not_called()
        self.importer.assert_not_called()

    def test_python_metadata_does_not_hide_missing_modules_or_transitive_dependencies(self):
        self.install_node_manifest()
        self.importer.side_effect = [
            ModuleNotFoundError("No module named 'yaml'"),
            ModuleNotFoundError("No module named 'mdurl'"),
        ]
        with patch.object(check.metadata, "version", side_effect=["6.0.2", "4.2.0"]), \
                patch.object(check.shutil, "which", return_value="node"), \
                patch.object(check.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)):
            errors = check.check_environment(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("yaml" in error for error in errors))
        self.assertTrue(any("markdown_it" in error and "mdurl" in error for error in errors))

    def test_existing_manifests_do_not_hide_missing_transitive_dependencies(self):
        self.install_node_manifest()
        with patch.object(check.metadata, "version", side_effect=["6.0.2", "4.2.0"]), \
                patch.object(check.shutil, "which", return_value="node"), \
                patch.object(check.subprocess, "run", return_value=subprocess.CompletedProcess(
                    [], 1, stderr="Cannot find module 'deepmerge'",
                )) as run:
            errors = check.check_environment(self.root)
        self.assertTrue(any("推移的依存" in error for error in errors))
        self.assertEqual(run.call_args.kwargs["cwd"], self.root)
        self.assertIn("--disable-proto=throw", run.call_args.args[0])

    def test_reports_versions_of_the_selected_environment(self):
        self.install_node_manifest("0.0.0")
        with patch.object(check.metadata, "version", side_effect=["6.0.1", "4.2.0"]), \
                patch.object(check.shutil, "which", return_value="node"), \
                patch.object(check.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)):
            errors = check.check_environment(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("6.0.1" in error for error in errors))
        self.assertTrue(any("0.0.0" in error for error in errors))

    def test_prepared_environment_passes(self):
        self.install_node_manifest()
        with patch.object(check.metadata, "version", side_effect=["6.0.2", "4.2.0"]), \
                patch.object(check.shutil, "which", return_value="node"), \
                patch.object(check.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)):
            self.assertEqual(check.check_environment(self.root), [])


if __name__ == "__main__":
    unittest.main()
