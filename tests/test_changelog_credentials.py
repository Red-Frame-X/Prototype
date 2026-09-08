"""Credential boundaries for both standalone changelog downloaders."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch
from urllib.request import HTTPRedirectHandler

from scripts import update_adguard_changelogs as adguard

spec = importlib.util.spec_from_file_location(
    'credential_test_ubol',
    Path(__file__).resolve().parents[1] / 'uBOL Filter Converter/update_ubol_metadata.py',
)
ubol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ubol)


class CredentialBoundaryTests(unittest.TestCase):
    def request_for(self, module, fetch, url):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'ok'
        with patch.dict(module.os.environ, {'GITHUB_TOKEN': 'test-only-token'}), patch.object(
            module.urllib.request, 'urlopen', return_value=response
        ) as opened:
            self.assertEqual(fetch(url), b'ok')
        return opened.call_args.args[0]

    def test_only_exact_https_api_origin_receives_token(self):
        for module, fetch in ((adguard, adguard.fetch), (ubol, ubol.read_source)):
            for url in (
                'https://example.test/source',
                'https://raw.githubusercontent.com/owner/repo/main/source',
                'http://api.github.com/repos/owner/repo',
                'https://api.github.com.example.test/source',
                'https://api.github.com@evil.test/source',
                'https://api.github.com:8443/source',
            ):
                with self.subTest(module=module.__name__, url=url):
                    self.assertIsNone(self.request_for(module, fetch, url).get_header('Authorization'))
            request = self.request_for(module, fetch, 'https://api.github.com/repos/owner/repo')
            self.assertEqual(request.get_header('Authorization'), 'Bearer test-only-token')

    def test_redirects_never_inherit_credentials(self):
        for module, fetch in ((adguard, adguard.fetch), (ubol, ubol.read_source)):
            request = self.request_for(module, fetch, 'https://api.github.com/repos/owner/repo')
            for destination in ('https://example.test/source', 'http://api.github.com/source',
                                'https://api.github.com/another'):
                for code in (301, 302, 303, 307, 308):
                    with self.subTest(module=module.__name__, destination=destination, code=code):
                        redirected = HTTPRedirectHandler().redirect_request(
                            request, None, code, 'redirect', {}, destination,
                        )
                        self.assertIsNone(redirected.get_header('Authorization'))
                        self.assertIsNotNone(redirected.get_header('User-agent'))
