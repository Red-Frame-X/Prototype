import unittest
from pathlib import Path

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = REPOSITORY_ROOT / ".github" / "workflows"
WRITER_WORKFLOWS = (
    "build-ubol.yml",
    "sync.yml",
    "update-adguard-changelogs.yml",
    "update-ubol-changelog.yml",
)
EXPECTED_GROUP = "repository-writer-${{ github.ref }}"


class WriterWorkflowTests(unittest.TestCase):
    def _load(self, name: str) -> tuple[dict, str]:
        text = (WORKFLOW_DIR / name).read_text(encoding="utf-8")
        data = yaml.load(text, Loader=yaml.BaseLoader)
        self.assertIsInstance(data, dict)
        return data, text

    def test_all_writer_workflows_share_one_concurrency_group(self):
        for name in WRITER_WORKFLOWS:
            with self.subTest(workflow=name):
                workflow, _ = self._load(name)
                concurrency = workflow.get("concurrency")
                self.assertIsInstance(concurrency, dict)
                self.assertEqual(concurrency.get("group"), EXPECTED_GROUP)
                self.assertEqual(concurrency.get("cancel-in-progress"), "false")

    def test_all_writer_workflows_refresh_main_before_generation(self):
        for name in WRITER_WORKFLOWS:
            with self.subTest(workflow=name):
                workflow, _ = self._load(name)
                jobs = workflow.get("jobs")
                self.assertIsInstance(jobs, dict)
                for job in jobs.values():
                    self.assertIsInstance(job, dict)
                    permissions = job.get("permissions")
                    if not isinstance(permissions, dict) or permissions.get("contents") != "write":
                        continue
                    steps = job.get("steps")
                    self.assertIsInstance(steps, list)
                    commands = "\n".join(
                        step.get("run", "")
                        for step in steps
                        if isinstance(step, dict)
                    )
                    self.assertIn("git fetch --no-tags origin main", commands)
                    self.assertIn("git checkout -B main origin/main", commands)

    def test_writer_workflows_do_not_rebase_finished_generated_commits(self):
        for name in WRITER_WORKFLOWS:
            with self.subTest(workflow=name):
                _, text = self._load(name)
                self.assertNotIn("git pull --rebase origin main", text)


if __name__ == "__main__":
    unittest.main()
