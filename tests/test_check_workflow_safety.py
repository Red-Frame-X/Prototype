import tempfile
import unittest
from pathlib import Path

from scripts.check_workflow_safety import find_unsafe_workflows, is_unsafe_pull_request_writer


class WorkflowSafetyTests(unittest.TestCase):
    def test_rejects_pull_request_with_contents_write_even_without_push(self):
        workflow = """
on:
  pull_request:
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_scalar_pull_request_with_write_permission(self):
        workflow = """
on: pull_request
permissions:
  contents: write
jobs:
  fix:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_pull_request_with_non_contents_write_scope(self):
        workflow = """
on:
  pull_request:
permissions:
  issues: write
jobs:
  triage:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_write_all_permissions(self):
        workflow = """
on: [pull_request, workflow_dispatch]
permissions: write-all
jobs:
  fix:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_job_level_write_permission(self):
        workflow = """
on:
  pull_request:
jobs:
  fix:
    permissions:
      contents: write
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_pull_request_target_even_when_permissions_are_read_only(self):
        workflow = """
on:
  pull_request_target:
permissions:
  contents: read
jobs:
  inspect:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_scalar_pull_request_target(self):
        workflow = """
on: pull_request_target
permissions:
  contents: read
jobs:
  inspect:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_inline_pull_request_target_event_list(self):
        workflow = """
on: [workflow_dispatch, pull_request_target]
permissions:
  contents: read
jobs:
  inspect:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_flow_style_permissions(self):
        workflow = """
on: [pull_request, workflow_dispatch]
permissions: {contents: write}
jobs:
  fix:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_job_level_flow_style_permissions(self):
        workflow = """
on: pull_request
jobs:
  fix:
    permissions: {issues: write}
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_quoted_event_key(self):
        workflow = """
on:
  'pull_request':
permissions: {contents: write}
jobs:
  fix:
    steps:
      - run: echo ok
"""
        self.assertTrue(is_unsafe_pull_request_writer(workflow))

    def test_rejects_unusual_but_valid_indentation(self):
        workflow = """
on:
    pull_request:
permissions:
      contents: write
jobs:
    fix:
        steps:
          - run: echo ok
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

    def test_allows_scalar_read_only_pull_request_workflow(self):
        workflow = """
on: pull_request
permissions:
  contents: read
jobs:
  quality:
    steps:
      - run: echo ok
"""
        self.assertFalse(is_unsafe_pull_request_writer(workflow))

    def test_allows_read_all_pull_request_workflow(self):
        workflow = """
on: [pull_request, workflow_dispatch]
permissions: read-all
jobs:
  quality:
    steps:
      - run: echo ok
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
      # pull_request_target:
      - run: echo ok
"""
        self.assertFalse(is_unsafe_pull_request_writer(workflow))

    def test_invalid_yaml_fails_closed(self):
        with self.assertRaises(ValueError):
            is_unsafe_pull_request_writer("on: [pull_request\npermissions: write-all\n")

    def test_find_unsafe_workflows_reports_only_matching_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "unsafe.yml").write_text(
                "on:\n  pull_request:\npermissions:\n  contents: write\n"
                "jobs:\n  fix:\n    steps:\n      - run: echo ok\n",
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
