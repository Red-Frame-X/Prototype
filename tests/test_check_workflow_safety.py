import tempfile
import unittest
from pathlib import Path

from scripts.check_workflow_safety import find_unsafe_workflows, is_unsafe_pull_request_writer


class WorkflowSafetyTests(unittest.TestCase):
    def test_rejects_pull_request_workflow_that_writes_and_pushes(self):
        workflow = """
on:
  pull_request:
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: git push origin HEAD:branch
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_pull_request_target_workflow_that_writes_and_pushes(self):
        workflow = """
on:
  pull_request_target:
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: git push origin HEAD:branch
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_write_all_permissions_with_git_push(self):
        workflow = """
on: [pull_request, workflow_dispatch]
permissions: write-all
jobs:
  fix:
    steps:
      - run: git push
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_job_level_write_all_permissions_with_git_push(self):
        workflow = """
on:
  pull_request:
jobs:
  fix:
    permissions: write-all
    steps:
      - run: git push
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_contents_write_with_inline_comment(self):
        workflow = """
on:
  pull_request:
permissions:
  contents: write # needed by an old fixer
jobs:
  fix:
    steps:
      - run: git push
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_allows_read_only_pull_request_workflow(self):
        workflow = """
on:
  pull_request:
permissions:
  contents: read
jobs:
  quality:
    steps:
      - run: git diff --check
"""
        self.assertFalse(is_unsafe_pull_request_writer(workflow))

    def test_allows_writer_that_does_not_run_on_pull_requests(self):
        workflow = """
on:
  push:
    branches: [main]
permissions:
  contents: write
jobs:
  sync:
    steps:
      - run: git push
"""
        self.assertFalse(is_unsafe_pull_request_writer(workflow))

    def test_supports_inline_pull_request_event_list(self):
        workflow = """
on: [pull_request, workflow_dispatch]
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: git push
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_supports_inline_pull_request_target_event_list(self):
        workflow = """
on: [workflow_dispatch, pull_request_target]
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: git push
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_comments_do_not_trigger_detection(self):
        workflow = """
on:
  pull_request:
permissions:
  contents: read
jobs:
  quality:
    steps:
      # contents: write
      # permissions: write-all
      # git push origin main
      - run: echo ok
"""
        self.assertFalse(is_unsafe_pull_request_writer(workflow))

    def test_find_unsafe_workflows_reports_only_matching_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "unsafe.yml").write_text(
                "on:\n  pull_request:\npermissions:\n  contents: write\n"
                "jobs:\n  fix:\n    steps:\n      - run: git push\n",
                encoding="utf-8",
            )
            (directory / "safe.yml").write_text(
                "on:\n  push:\npermissions:\n  contents: write\n"
                "jobs:\n  sync:\n    steps:\n      - run: git push\n",
                encoding="utf-8",
            )
            self.assertEqual(
                [directory / "unsafe.yml"], find_unsafe_workflows(directory)
            )


if __name__ == "__main__":
    unittest.main()
