"""途中停止・応答喪失・モデルcacheの復旧と安全停止を検証する。"""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import shlex
import subprocess
import tempfile
import unittest
import urllib.error
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import automate_japanese_commits as automation
import argos_commit_translation as argos


class ModelRecoveryTests(unittest.TestCase):
    @patch.object(argos.time, 'sleep')
    def test_transient_download_recovers_and_reuses_verified_cache(self, sleep):
        data = b'verified archive'
        digest = hashlib.sha256(data).hexdigest()
        with tempfile.TemporaryDirectory() as directory, patch.dict(
                os.environ, {'ARGOS_MODEL_CACHE_DIR': directory}), patch.object(
                argos.urllib.request, 'urlopen', side_effect=[TimeoutError(), io.BytesIO(data)]) as request:
            archive = argos.model_archive(directory, digest)
            self.assertEqual(archive.read_bytes(), data)
            self.assertEqual(argos.model_archive(directory, digest), archive)
            self.assertEqual(request.call_count, 2)
            sleep.assert_called_once()

    @patch.object(argos.time, 'sleep')
    def test_download_timeout_retry_limit(self, sleep):
        with tempfile.TemporaryDirectory() as directory, patch.object(
                argos.urllib.request, 'urlopen', side_effect=TimeoutError()) as request:
            with self.assertRaises(argos.TranslationError):
                argos.download_model(Path(directory) / 'model')
            self.assertEqual(request.call_count, 4)
            self.assertEqual(sleep.call_count, 3)

    @patch.object(argos.time, 'sleep')
    def test_http_classification_and_retry_after(self, sleep):
        for code in (403, 429, 503):
            headers = {'Retry-After': '2'}
            error = urllib.error.HTTPError('https://argos-net.com/', code, 'error', headers, None)
            with self.subTest(code=code), tempfile.TemporaryDirectory() as directory, patch.object(
                    argos.urllib.request, 'urlopen', side_effect=[error, io.BytesIO(b'archive')]) as request:
                if code == 403:
                    with self.assertRaises(argos.TranslationError):
                        argos.download_model(Path(directory) / 'model')
                    request.assert_called_once()
                else:
                    argos.download_model(Path(directory) / 'model')
                    self.assertEqual(request.call_count, 2)
                    sleep.assert_called_with(2)

    def test_corrupt_cache_is_not_installed_or_silently_replaced(self):
        digest = 'a' * 64
        with tempfile.TemporaryDirectory() as directory, patch.dict(
                os.environ, {'ARGOS_MODEL_CACHE_DIR': directory}), patch.object(
                argos.urllib.request, 'urlopen') as request:
            archive = Path(directory) / (digest + '.argosmodel')
            archive.write_bytes(b'corrupt')
            with self.assertRaisesRegex(argos.TranslationError, 'cache'):
                argos.model_archive(directory, digest)
            request.assert_not_called()
            self.assertEqual(archive.read_bytes(), b'corrupt')


class IntentTests(unittest.TestCase):
    def test_intent_is_saved_before_write_and_duplicate_is_not_sent(self):
        state = {}
        recorded = []
        def save(gh, number, value, text):
            recorded.append(copy.deepcopy(value))
        send = Mock(side_effect=lambda: self.assertEqual(
            recorded[-1]['intents']['quality:sha']['status'], 'reserved'))
        with patch.object(automation, 'save_state', side_effect=save):
            self.assertTrue(automation.perform_once(Mock(), 1, state, 'quality:sha', send))
            self.assertFalse(automation.perform_once(Mock(), 1, state, 'quality:sha', send))
        send.assert_called_once()
        self.assertEqual(recorded[-1]['intents']['quality:sha']['status'], 'sent')

    def test_failed_intent_record_never_writes(self):
        send = Mock()
        with patch.object(automation, 'save_state', side_effect=automation.AutomationError('保存失敗')):
            with self.assertRaises(automation.AutomationError):
                automation.perform_once(Mock(), 1, {}, 'quality:sha', send)
        send.assert_not_called()

    def test_uncertain_write_is_reconciled_instead_of_replayed(self):
        state = {}
        with patch.object(automation, 'save_state'), patch.object(automation.time, 'time', return_value=100):
            with self.assertRaises(TimeoutError):
                automation.perform_once(Mock(), 1, state, 'review:sha', Mock(side_effect=TimeoutError()))
        send = Mock()
        with patch.object(automation.time, 'time', return_value=401):
            with self.assertRaisesRegex(automation.AutomationError, '再送しません'):
                automation.perform_once(Mock(), 1, state, 'review:sha', send)
        send.assert_not_called()

    def test_pending_codex_state_or_exact_bot_receipt_prevents_duplicate_request(self):
        marker = '<!-- commit-ja-review-request:sha -->'
        bot = {'user': {'login': automation.BOT_LOGIN, 'type': 'Bot'}, 'body': marker}
        self.assertTrue(automation.review_observed([bot], 'sha'))
        self.assertFalse(automation.review_observed([bot], 'other'))
        human = {**bot, 'user': {'login': 'owner', 'type': 'User'}}
        self.assertFalse(automation.review_observed([human], 'sha'))
        review = {'code_review': {'commit_sha': 'sha', 'status': 'running'}}
        codex = {'user': {'login': automation.CODEX_LOGIN, 'type': 'Bot'},
                 'body': '<!-- codex-review-state:v1 ' + json.dumps(review) + ' -->'}
        self.assertTrue(automation.review_observed([codex], 'sha'))


class ClosedResumeTests(unittest.TestCase):
    def test_diagnostic_artifact_exists_even_when_python_syntax_is_broken(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        workflow = yaml.load((root / '.github/workflows/japanese-commits.yml').read_text(),
                             Loader=yaml.BaseLoader)
        script = next(step['run'] for step in workflow['jobs']['diagnose']['steps']
                      if 'py_compile' in step.get('run', ''))
        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / 'invalid.py'
            invalid.write_text('def broken(:\n')
            script = script.replace('scripts/automate_japanese_commits.py scripts/argos_commit_translation.py',
                                    shlex.quote(str(invalid)))
            result = subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', script],
                                    env={**os.environ, 'RUNNER_TEMP': directory}, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('SyntaxError', (Path(directory) / 'commit-ja-diagnostics.txt').read_text())

    def test_real_git_lifecycle_uses_separate_post_merge_ci_and_is_idempotent(self):
        from test_argos_automation_lifecycle import run_end_to_end
        translations = {'Update documentation': 'ドキュメントを更新',
                        'Do not remove existing tests.': '既存のテストを削除しないでください。'}
        run_end_to_end(lambda source: translations[source])

    def test_merge_success_with_lost_response_resumes_dispatch_once(self):
        sha, head, parent = 'c' * 40, 'a' * 40, 'b' * 40
        message = '説明を更新 (#1)\n\n理由を追記。'
        state = {'phase': 'MERGE_READY', 'sha': head, 'managed': True,
                 'merge_message_digest': hashlib.sha256(message.encode()).hexdigest()}
        pr = {'number': 1, 'merged': True, 'merge_commit_sha': sha,
              'head': {'sha': head}, 'base': {'ref': 'main'}}
        gh = Mock()
        def api(path, method='GET', data=None):
            if path == '/git/commits/' + sha:
                return {'message': message, 'parents': [{'sha': parent}]}
            if '/runs?' in path:
                return {'workflow_runs': []}
            if path == '/git/ref/heads/main':
                return {'object': {'sha': sha}}
            if path.endswith('/dispatches'):
                return None
            raise AssertionError(path)
        gh.api.side_effect = api
        with patch.object(automation, 'read_state', return_value=state), patch.object(automation, 'save_state'):
            automation.verify_merged_pr(gh, pr)
            automation.verify_merged_pr(gh, pr)
        dispatches = [call for call in gh.api.call_args_list if call.args[1:2] == ('POST',)]
        self.assertEqual(len(dispatches), 1)
        self.assertEqual(state['phase'], 'MERGED')
        self.assertEqual(state['merge_parent'], parent)

    def test_mismatched_merge_message_is_never_accepted(self):
        state = {'phase': 'MERGE_READY', 'sha': 'a' * 40, 'merge_message_digest': 'wrong'}
        pr = {'number': 1, 'merged': True, 'merge_commit_sha': 'c' * 40, 'head': {'sha': 'a' * 40}}
        gh = Mock()
        gh.api.return_value = {'message': '別の内容', 'parents': [{'sha': 'b' * 40}]}
        with patch.object(automation, 'read_state', return_value=state), patch.object(
                automation, 'save_state') as save:
            with self.assertRaises(automation.AutomationError):
                automation.verify_merged_pr(gh, pr)
            save.assert_not_called()


if __name__ == '__main__':
    unittest.main()
