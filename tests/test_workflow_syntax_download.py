"""actionlintの取得障害とhash不一致を、実HTTP・実Shellで検証する。"""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
from pathlib import Path
import subprocess
import tarfile
import tempfile
import threading
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WorkflowSyntaxDownloadTests(unittest.TestCase):
    def run_download(self, statuses, correct_hash=True, api_statuses=None):
        archive = io.BytesIO()
        with tarfile.open(fileobj=archive, mode='w:gz') as tar:
            content = b'#!/bin/sh\nprintf validated > lint-executed\n'
            info = tarfile.TarInfo('actionlint')
            info.size = len(content)
            info.mode = 0o755
            tar.addfile(info, io.BytesIO(content))
        payload = archive.getvalue()
        requests = []
        api_requests = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/asset-api':
                    if self.headers.get('Accept') != 'application/octet-stream':
                        self.send_error(406)
                        return
                    choices = api_statuses if api_statuses is not None else statuses
                    status = choices[min(len(api_requests), len(choices) - 1)]
                    api_requests.append(status)
                else:
                    status = statuses[min(len(requests) - len(api_requests), len(statuses) - 1)]
                requests.append(status)
                self.send_response(status)
                self.end_headers()
                if status == 200:
                    self.wfile.write(payload)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as directory:
                script = (ROOT / 'scripts/check_workflow_syntax.sh').read_text()
                # 配布物と接続先だけをテスト用に置き換え、同じ取得・検証・実行処理を使う。
                script = script.replace(
                    'https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/${ARCHIVE}',
                    f'http://127.0.0.1:{server.server_port}/actionlint.tar.gz')
                script = script.replace(
                    'https://api.github.com/repos/rhysd/actionlint/releases/assets/384924896',
                    f'http://127.0.0.1:{server.server_port}/asset-api')
                digest = hashlib.sha256(payload).hexdigest() if correct_hash else '0' * 64
                script = script.replace(
                    '8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8', digest)
                result = subprocess.run(['bash', '-c', script], cwd=directory,
                                        capture_output=True, text=True, timeout=30)
                executed = (Path(directory) / 'lint-executed').exists()
                return result, executed, requests
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_temporary_gateway_failure_is_retried_before_verified_execution(self):
        result, executed, requests = self.run_download([504, 200])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(executed)
        self.assertEqual(requests, [504, 200])

    def test_permanent_missing_asset_fails_without_execution(self):
        result, executed, requests = self.run_download([404])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(executed)
        self.assertEqual(requests, [404])

    def test_persistent_gateway_failure_stops_after_retry_limit(self):
        result, executed, requests = self.run_download([504])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(executed)
        self.assertEqual(requests, [504] * 8)

    def test_official_api_recovers_persistent_primary_gateway_failure(self):
        result, executed, requests = self.run_download([504], api_statuses=[200])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(executed)
        self.assertEqual(requests, [504] * 4 + [200])

    def test_fallback_hash_mismatch_never_executes_download(self):
        result, executed, requests = self.run_download([504], correct_hash=False, api_statuses=[200])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(executed)
        self.assertEqual(requests, [504] * 4 + [200])

    def test_forbidden_response_does_not_switch_endpoint(self):
        result, executed, requests = self.run_download([403], api_statuses=[200])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(executed)
        self.assertEqual(requests, [403])

    def test_hash_mismatch_never_executes_download(self):
        result, executed, requests = self.run_download([200], correct_hash=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(executed)
        self.assertEqual(requests, [200])
