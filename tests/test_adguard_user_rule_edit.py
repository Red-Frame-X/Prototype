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

    def exercise(self, base_approval=None, head_approval=None, after=None, workflow_event=None, missing_base=False, cli_approval=None, staged=False, unstaged_after=None, unstaged_approval=None):
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
            if staged:
                git("add", ".")
                if unstaged_after is not None:
                    target.write_text(unstaged_after, encoding="utf-8")
                if unstaged_approval is not None:
                    config.write_text(json.dumps(unstaged_approval), encoding="utf-8")
                return subprocess.run(
                    ["python", str(script), "--staged"],
                    cwd=root, text=True, capture_output=True,
                )
            if workflow_event:
                workflow = yaml.load((SCRIPT.parents[1] / ".github/workflows/quality.yml").read_text(), Loader=yaml.BaseLoader)
                step = next(s for s in workflow["jobs"]["quality"]["steps"] if s["name"] == "AdGuardユーザールールの編集前検査")
                return subprocess.run(
                    ["bash", "-e", "-o", "pipefail", "-c", step["run"]], cwd=root, text=True, capture_output=True,
                    env={**os.environ, "GITHUB_EVENT_NAME": workflow_event,
                         "ADGUARD_BASE_REF": "origin/main" if workflow_event == "pull_request" else ("0" * 40 if missing_base else base)},
                )
            return subprocess.run(
                ["python", str(script), "--base-ref", "missing" if missing_base else base,
                 *(["--allow-rule-removal", cli_approval] if cli_approval is not None else [])],
                cwd=root, text=True, capture_output=True,
            )

    def test_accepts_exact_commentout_on_pr_and_push(self):
        after = self.baseline.replace(self.removed + "\n", "! " + self.removed + "\n")
        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                result = self.exercise(after=after, workflow_event=event)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_commentout_with_changed_rule(self):
        after = self.baseline.replace(self.removed + "\n", "! example.com##.different\n")
        result = self.exercise(after=after)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_commentout_does_not_hide_other_removals(self):
        after = "! " + self.removed + "\nexample.net##.banner\n"
        result = self.exercise(after=after)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_existing_comment_cannot_authorize_removal(self):
        self.baseline += "! " + self.removed + "\n"
        result = self.exercise(after=self.baseline.replace(self.removed + "\n", "", 1))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_rejects_unapproved_removal(self):
        result = self.exercise()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_staged_rejects_unapproved_yahoo_pair_removal(self):
        selector = "div#newsFeed:has(> h2:contains(/^あなたにおすすめ$/)):has(> ul.newsFeed_list)"
        self.baseline = (f"news.yahoo.co.jp#?#{selector}\n"
                         f"news.yahoo.co.jp#@?#{selector}\nexample.net##.banner\n")
        result = self.exercise(after="example.net##.banner\n", staged=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("(2件）", result.stderr)

    def test_staged_accepts_exact_approval_and_consumption(self):
        result = self.exercise(base_approval=self.approval(), staged=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unstaged_restore_cannot_hide_staged_removal(self):
        result = self.exercise(staged=True, unstaged_after=self.baseline)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_unstaged_consumption_cannot_hide_staged_approval_reuse(self):
        result = self.exercise(base_approval=self.approval(), head_approval=self.approval(),
                               staged=True, unstaged_approval={"version": 1, "approvals": []})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("承認の再利用", result.stderr)

    def test_staged_cannot_self_approve(self):
        result = self.exercise(head_approval=self.approval(), staged=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("明示的な承認がない", result.stderr)

    def test_staged_rejects_crlf(self):
        result = self.exercise(after=self.baseline.replace("\n", "\r\n"), staged=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CR文字を検出", result.stderr)

    def test_diamond_container_addition_preserves_existing_rules(self):
        self.baseline = (
            "diamond.jp###cx-recommend-member-articles\n"
            "diamond.jp###cx-recommend\n"
        )
        replacements = (
            "diamond.jp###recommend-member-articles\n"
            "diamond.jp##.sub-column:has(> #cx-recommend)\n"
        )
        for event in ("pull_request", "push"):
            with self.subTest(event=event, change="replacement"):
                result = self.exercise(after=replacements, workflow_event=event)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("明示的な承認がない", result.stderr)
            with self.subTest(event=event, change="addition"):
                result = self.exercise(after=self.baseline + replacements, workflow_event=event)
                self.assertEqual(result.returncode, 0, result.stderr)

        # 実際の配布ファイルでも、親コンテナーと内部枠の両方を保持する。
        target = SCRIPT.parents[1] / "AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt"
        rules = set(target.read_text(encoding="utf-8").splitlines())
        self.assertTrue(set((self.baseline + replacements).splitlines()) <= rules)

    def test_accepts_exact_approval_from_base(self):
        result = self.exercise(base_approval=self.approval())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_overlapping_cli_and_recorded_approval_is_not_counted_twice(self):
        result = self.exercise(base_approval=self.approval(), cli_approval=self.removed)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_overlapping_approval_does_not_hide_extra_cli_approval(self):
        result = self.exercise(base_approval=self.approval(), cli_approval="example.org##.promo")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("削除の承認が実際の差分と一致しません", result.stderr)

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
