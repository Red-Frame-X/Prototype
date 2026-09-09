import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = REPOSITORY_ROOT / ".github" / "workflows"
WRITER_WORKFLOWS = {
    "build-ubol.yml": 'python "uBOL Filter Converter/converter.py"',
    "sync.yml": "python scripts/convert.py",
    "update-adguard-changelogs.yml": "python scripts/update_adguard_changelogs.py",
    "update-ubol-changelog.yml": 'python "uBOL Filter Converter/update_ubol_metadata.py"',
}
EXPECTED_GROUP = "${{ github.workflow }}-${{ github.ref }}"


class WriterWorkflowTests(unittest.TestCase):
    def _load(self, name: str) -> tuple[dict, str]:
        text = (WORKFLOW_DIR / name).read_text(encoding="utf-8")
        data = yaml.load(text, Loader=yaml.BaseLoader)
        self.assertIsInstance(data, dict)
        return data, text

    def test_writer_workflows_keep_separate_concurrency_groups(self):
        for name in WRITER_WORKFLOWS:
            with self.subTest(workflow=name):
                workflow, _ = self._load(name)
                concurrency = workflow.get("concurrency")
                self.assertIsInstance(concurrency, dict)
                self.assertEqual(concurrency.get("group"), EXPECTED_GROUP)
                self.assertEqual(concurrency.get("cancel-in-progress"), "false")

    def test_writer_workflows_regenerate_from_latest_main_before_each_push(self):
        for name, generator_command in WRITER_WORKFLOWS.items():
            with self.subTest(workflow=name):
                _, text = self._load(name)
                loop_index = text.index("for attempt in 1 2 3 4 5; do")
                fetch_index = text.index("git fetch --no-tags origin main", loop_index)
                reset_index = text.index("git reset --hard origin/main", fetch_index)
                generate_index = text.index(generator_command, reset_index)
                push_index = text.index("git push origin HEAD:main", generate_index)
                self.assertLess(loop_index, fetch_index)
                self.assertLess(fetch_index, reset_index)
                self.assertLess(reset_index, generate_index)
                self.assertLess(generate_index, push_index)

    def test_writer_workflows_do_not_rebase_finished_generated_commits(self):
        for name in WRITER_WORKFLOWS:
            with self.subTest(workflow=name):
                _, text = self._load(name)
                self.assertNotIn("git pull --rebase origin main", text)
                self.assertNotIn("repository-writer-${{ github.ref }}", text)


if __name__ == "__main__":
    unittest.main()
