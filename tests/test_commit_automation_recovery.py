"""通信の復旧上限と、書き込みを再送しない安全境界を検証する。"""
import io
import json
from pathlib import Path
import sys
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import automate_japanese_commits as automation


class APIRecoveryTests(unittest.TestCase):
    def response(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"ok":true}'
        return response

    def error(self, code, headers=None):
        return urllib.error.HTTPError('https://api.github.com/test', code, 'error',
                                      headers or {}, io.BytesIO(b'private response'))

    @patch.object(automation.time, 'sleep')
    def test_transient_get_recovers(self, sleep):
        for error in (TimeoutError(), urllib.error.URLError('timeout'),
                      self.error(429, {'Retry-After': '2'}), self.error(500),
                      self.error(502), self.error(503), self.error(504)):
            with self.subTest(error=error), patch.object(
                    automation.urllib.request, 'urlopen', side_effect=[error, self.response()]) as request:
                self.assertEqual(automation.request_json('https://api.github.com/test', 'secret'),
                                 {'ok': True})
                self.assertEqual(request.call_count, 2)

    @patch.object(automation.time, 'sleep')
    def test_retry_limit(self, sleep):
        with patch.object(automation.urllib.request, 'urlopen', side_effect=self.error(503)) as request:
            with self.assertRaises(automation.APIError) as caught:
                automation.request_json('https://api.github.com/test', 'secret')
        self.assertEqual(caught.exception.category, 'A')
        self.assertEqual(request.call_count, 4)
        self.assertEqual(sleep.call_count, 3)
        self.assertNotIn('private', str(caught.exception))

    @patch.object(automation.time, 'sleep')
    def test_permission_conflict_validation_never_retry(self, sleep):
        for code, category in ((403, 'D'), (409, 'B'), (422, 'D')):
            with self.subTest(code=code), patch.object(
                    automation.urllib.request, 'urlopen', side_effect=self.error(code)) as request:
                with self.assertRaises(automation.APIError) as caught:
                    automation.request_json('https://api.github.com/test', 'secret')
                self.assertEqual(caught.exception.category, category)
                request.assert_called_once()
        sleep.assert_not_called()

    @patch.object(automation.time, 'sleep')
    def test_mutation_is_not_blindly_replayed(self, sleep):
        for method in ('POST', 'PATCH', 'PUT'):
            with self.subTest(method=method), patch.object(
                    automation.urllib.request, 'urlopen', side_effect=self.error(503)) as request:
                with self.assertRaises(automation.APIError):
                    automation.request_json('https://api.github.com/test', 'secret', method, {})
                request.assert_called_once()
        sleep.assert_not_called()

    @patch.object(automation.time, 'sleep')
    def test_long_retry_after_is_not_shortened(self, sleep):
        with patch.object(automation.urllib.request, 'urlopen',
                          side_effect=self.error(429, {'Retry-After': '120'})) as request:
            with self.assertRaises(automation.APIError):
                automation.request_json('https://api.github.com/test', 'secret')
            request.assert_called_once()
        sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
