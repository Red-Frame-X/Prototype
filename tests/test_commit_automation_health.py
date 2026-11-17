"""自然起動の実測と、書き込み上限付きの保守引き継ぎを検証する。"""
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import report_commit_automation_health as health


class CadenceTests(unittest.TestCase):
    def run_sample(self, number, minute, **changes):
        run = dict(id=number, event='schedule', path=health.WORKFLOW,
                   head_branch='main', run_attempt=1, head_sha='a' * 40,
                   created_at=f'2026-11-17T09:{minute:02d}:00Z', status='completed',
                   conclusion='success')
        run.update(changes)
        return run

    def test_three_natural_runs_measure_intervals(self):
        now = health.timestamp('2026-11-17T09:11:00Z')
        runs = [self.run_sample(i, i * 5) for i in range(3)]
        report = health.cadence_report(runs + runs, 'main', now)
        self.assertEqual(report['state'], 'OBSERVED')
        self.assertEqual(report['sample_count'], 3)
        self.assertEqual(report['interval_seconds'], [300, 300])

    def test_manual_rerun_other_workflow_and_branch_are_not_evidence(self):
        runs = [self.run_sample(1, 0), self.run_sample(2, 5, event='workflow_dispatch'),
                self.run_sample(3, 5, run_attempt=2),
                self.run_sample(4, 5, path='.github/workflows/quality.yml'),
                self.run_sample(5, 5, head_branch='feature')]
        report = health.cadence_report(runs, 'main', health.timestamp('2026-11-17T09:06:00Z'))
        self.assertEqual(report['sample_count'], 1)
        self.assertEqual(report['state'], 'INSUFFICIENT_SAMPLES')

    def test_delayed_or_stale_runs_are_not_healthy(self):
        for minutes, now in [([0, 5, 20], '09:21'), ([0, 5, 10], '09:30')]:
            report = health.cadence_report(
                [self.run_sample(i, minute) for i, minute in enumerate(minutes)],
                'main', health.timestamp(f'2026-11-17T{now}:00Z'))
            self.assertEqual(report['state'], 'DELAYED')

    def test_missing_and_old_history_is_insufficient(self):
        report = health.cadence_report([self.run_sample(1, 0)], 'main',
                                      health.timestamp('2026-11-19T09:00:00Z'))
        self.assertEqual(report['sample_count'], 0)
        self.assertEqual(report['state'], 'INSUFFICIENT_SAMPLES')

    def test_api_failure_is_not_missing_history(self):
        gh = Mock()
        gh.api.side_effect = health.AutomationError('API failed')
        with self.assertRaises(health.AutomationError):
            health.collect_cadence(gh, 0)


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.gh = Mock(repository='Red-Frame-X/Prototype')
        self.gh.api.side_effect = lambda path, *args: (
            {'private': False} if path == '' else {'number': 1, 'html_url': 'https://example.test/1'})
        self.gh.pages.return_value = []
        self.root = Path(__file__).resolve().parents[1]

    def call(self):
        return health.maintenance_issue(self.gh, self.root, '123', 'a' * 40, 'failure')

    def test_creates_one_issue_with_reproduction_without_executing_code(self):
        with patch.object(health.subprocess, 'check_output') as execute:
            self.assertEqual(self.call()['state'], 'CREATED')
        execute.assert_not_called()
        writes = [call for call in self.gh.api.call_args_list if len(call.args) > 1]
        self.assertEqual(len(writes), 1)
        self.assertEqual(writes[0].args[1], 'POST')
        self.assertIn('python -m unittest', writes[0].args[2]['body'])

    def test_closed_bot_issue_is_not_recreated(self):
        self.gh.pages.return_value = [{
            'body': f'<!-- {health.MARKER} {health.maintenance_fingerprint(self.root)} -->',
            'user': {'login': 'github-actions[bot]', 'type': 'Bot'},
            'number': 7, 'html_url': 'https://example.test/7', 'state': 'closed'}]
        self.assertEqual(self.call()['state'], 'EXISTING')
        self.gh.api.assert_called_once_with('')

    def test_forged_marker_does_not_suppress_issue(self):
        self.gh.pages.return_value = [{
            'body': f'<!-- {health.MARKER} {health.maintenance_fingerprint(self.root)} -->',
            'user': {'login': 'other', 'type': 'User'}}]
        self.assertEqual(self.call()['state'], 'CREATED')

    def test_private_repository_stops_without_listing_or_writing(self):
        self.gh.api.side_effect = None
        self.gh.api.return_value = {'private': True}
        with self.assertRaises(health.AutomationError):
            self.call()
        self.gh.pages.assert_not_called()
        self.gh.api.assert_called_once_with('')

    def test_listing_failure_does_not_create_and_post_failure_is_not_retried(self):
        self.gh.pages.side_effect = health.AutomationError('read failed')
        with self.assertRaises(health.AutomationError):
            self.call()
        self.gh.api.assert_called_once_with('')
        self.gh.reset_mock()
        self.gh.pages.side_effect = None
        self.gh.api.side_effect = [{'private': False}, health.AutomationError('lost response')]
        with self.assertRaises(health.AutomationError):
            self.call()
        self.assertEqual(self.gh.api.call_count, 2)

    def test_invalid_run_id_is_rejected_before_api(self):
        with self.assertRaises(health.AutomationError):
            health.maintenance_issue(self.gh, self.root, 'bad', 'a' * 40, 'failure')
        self.gh.api.assert_not_called()


if __name__ == '__main__':
    unittest.main()
