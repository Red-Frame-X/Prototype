from __future__ import annotations

from pathlib import Path
import hashlib
import json
import os
import subprocess
import tempfile
import unittest

import yaml

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_adguard_user_rule_edit.py"


class AdGuardEditPreflightTests(unittest.TestCase):
    def run_script(self, content: str | bytes):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "AdGuard Custom Rules"
            target.mkdir()
            (root / "scripts").mkdir()
            script = root / "scripts" / SCRIPT.name
            script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
            filter_path = target / "AdGuard Custom Rules - Red Frame X.txt"
            if isinstance(content, bytes):
                filter_path.write_bytes(content)
            else:
                filter_path.write_text(content, encoding="utf-8", newline="\n")
            return subprocess.run(
                ["python", str(script)],
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def test_accepts_unique_rules(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad
example.org##.promo
"""
        result = self.run_script(text)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_crlf_line_endings(self):
        content = (
            "! Title: AdGuard Custom Rules - Red Frame X\r\n"
            "! Description: Test\r\n"
            "example.com##.ad\r\n"
        ).encode("utf-8")
        result = self.run_script(content)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CR文字を検出しました", result.stderr)

    def test_rejects_cr_line_endings(self):
        content = (
            "! Title: AdGuard Custom Rules - Red Frame X\r"
            "! Description: Test\r"
            "example.com##.ad\r"
        ).encode("utf-8")
        result = self.run_script(content)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CR文字を検出しました", result.stderr)

    def test_rejects_duplicate_active_rule(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad
example.com##.ad
"""
        result = self.run_script(text)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("有効ルールの重複", result.stderr)

    def test_rejects_duplicate_non_basic_modifier_rule(self):
        result = self.run_script("[$app=com.example.app]##.ad\n" * 2)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("有効ルールの重複", result.stderr)

    def test_rejects_trailing_whitespace(self):
        text = """! Title: AdGuard Custom Rules - Red Frame X
! Description: Test
! Version: 202608272045
! Syntax: AdGuard
! Expires: 1 day
! Homepage: https://example.com
! License: CC0-1.0
! Note: Test

example.com##.ad   
"""
        result = self.run_script(text)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("末尾に空白", result.stderr)


class AdGuardRemovalApprovalTests(unittest.TestCase):
    baseline = "example.com##.ad\nexample.org##.promo\nexample.net##.banner\n"
    removed = "example.com##.ad"

    def approval(self, rules=None, baseline=None):
        text = self.baseline if baseline is None else baseline
        return {
            "version": 1,
            "approvals": [{
                "rules_sha256": hashlib.sha256("\n".join(sorted(text.splitlines())).encode()).hexdigest(),
                "rules": [self.removed] if rules is None else rules,
                "reason": "ユーザーが指定した広告ルールを削除するため",
                "reference": "https://example.com/approval/1",
            }],
        }

    def exercise(self, base_approval=None, head_approval=None, after=None, workflow_event=None, missing_base=False):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "scripts").mkdir()
            (root / "config").mkdir()
            script = root / "scripts" / SCRIPT.name
            script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
            target = root / "AdGuard Custom Rules" / "AdGuard Custom Rules - Red Frame X.txt"
            target.parent.mkdir()
            target.write_text(self.baseline, encoding="utf-8")
            config = root / "config" / "adguard-rule-removal-approvals.json"
            if base_approval is not None:
                config.write_text(json.dumps(base_approval), encoding="utf-8")

            def git(*args):
                return subprocess.check_output(["git", *args], cwd=root, text=True, stderr=subprocess.PIPE).strip()

            git("init", "-q")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.com")
            git("add", ".")
            git("commit", "-qm", "検証用の比較元を作成")
            base = git("rev-parse", "HEAD")
            git("update-ref", "refs/remotes/origin/main", base)
            target.write_text(self.baseline.replace(self.removed + "\n", "") if after is None else after, encoding="utf-8")
            if base_approval is not None:
                config.write_text(json.dumps({"version": 1, "approvals": []}), encoding="utf-8")
            if head_approval is not None:
                config.write_text(json.dumps(head_approval), encoding="utf-8")
            if workflow_event:
                workflow = yaml.load((SCRIPT.parents[1] / ".github/workflows/quality.yml").read_text(), Loader=yaml.BaseLoader)
                step = next(s for s in workflow["jobs"]["quality"]["steps"] if s["name"] == "AdGuardユーザールールの編集前検査")
                return subprocess.run(
                    ["bash", "-e", "-o", "pipefail", "-c", step["run"]], cwd=root, text=True, capture_output=True,
                    env={**os.environ, "GITHUB_EVENT_NAME": workflow_event,
                         "ADGUARD_BASE_REF": "origin/main" if workflow_event == "pull_request" else ("0" * 40 if missing_base else base)},
                )
            return subprocess.run(
                ["python", str(script), "--base-ref", "missing" if missing_base else base],
                cwd=root, text=True, capture_output=True,
            )

    def test_rejects_unapproved_removal(self):
        result = self.exercise()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_accepts_exact_approval_from_base(self):
        result = self.exercise(base_approval=self.approval())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_cannot_self_approve_in_removal_pr(self):
        result = self.exercise(head_approval=self.approval())
        self.assertNotEqual(result.returncode, 0)

    def test_accepts_approval_registration_without_removal(self):
        result = self.exercise(head_approval=self.approval(), after=self.baseline)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_stale_approval(self):
        result = self.exercise(base_approval=self.approval(baseline=self.baseline + "other.example##.ad\n"))
        self.assertNotEqual(result.returncode, 0)

    def test_requires_consuming_used_approval(self):
        result = self.exercise(base_approval=self.approval(), head_approval=self.approval())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("承認の再利用", result.stderr)

    def test_rejects_malformed_approval_registration(self):
        result = self.exercise(head_approval={"version": True, "approvals": []}, after=self.baseline)
        self.assertNotEqual(result.returncode, 0)

    def test_rejects_ambiguous_approvals(self):
        approval = self.approval()
        approval["approvals"] *= 2
        result = self.exercise(base_approval=approval)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("複数の承認", result.stderr)

    def test_approval_does_not_bypass_bulk_removal_guard(self):
        self.baseline = "".join(f"example.com##.ad{i}\n" for i in range(40))
        rules = self.baseline.splitlines()[:11]
        result = self.exercise(base_approval=self.approval(rules=rules), after="\n".join(self.baseline.splitlines()[11:]) + "\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("大量減少", result.stderr)

    def test_rejects_additional_removal(self):
        result = self.exercise(base_approval=self.approval(), after="example.net##.banner\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("example.org##.promo", result.stderr)

    def test_rejects_partial_use_of_approval(self):
        result = self.exercise(base_approval=self.approval(rules=[self.removed, "example.org##.promo"]))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("削除の承認が実際の差分と一致しません", result.stderr)

    def test_metadata_update_does_not_invalidate_approval(self):
        result = self.exercise(base_approval=self.approval(), after="! Version: 202611070500\nexample.org##.promo\nexample.net##.banner\n")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_malformed_approval(self):
        result = self.exercise(base_approval={"version": 1, "approvals": [{}]})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("削除承認が不正", result.stderr)

    def test_missing_base_fails_closed(self):
        result = self.exercise(missing_base=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("比較元", result.stderr)

    def test_workflow_pr_accepts_approved_removal(self):
        result = self.exercise(base_approval=self.approval(), workflow_event="pull_request")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_workflow_push_accepts_approved_removal(self):
        result = self.exercise(base_approval=self.approval(), workflow_event="push")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_workflow_push_rejects_unapproved_removal(self):
        result = self.exercise(workflow_event="push")
        self.assertNotEqual(result.returncode, 0)

    def test_workflow_push_rejects_unknown_before(self):
        result = self.exercise(workflow_event="push", missing_base=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
