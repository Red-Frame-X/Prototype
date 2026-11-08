"""翻訳対象と保護表記、失敗時の停止を検証する。"""
import hashlib
import io
import json
from pathlib import Path
import sys
import unittest
import types
import zipfile
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import argos_commit_translation as argos


class ArgosTranslationTests(unittest.TestCase):
    def test_english_is_translated(self):
        engine = Mock(return_value='説明を更新')
        self.assertEqual(argos.translate_text('Update description\n', engine), '説明を更新\n')
        engine.assert_called_once_with('Update description')

    def test_japanese_is_unchanged(self):
        engine = Mock()
        text = '既存の日本語文章。READMEの説明を更新\n'
        self.assertEqual(argos.translate_text(text, engine), text)
        engine.assert_not_called()

    def test_mixed_preserves_japanese_and_protected_terms(self):
        engine = Mock(return_value='説明を更新')
        text = '既存の説明\nUpdate README.md https://example.com/a #12 `my_func` v1.2.3\n'
        result = argos.translate_text(text, engine)
        self.assertTrue(result.startswith('既存の説明\n説明を更新'))
        for value in ('README.md', 'https://example.com/a', '#12', '`my_func`', 'v1.2.3'):
            self.assertIn(value, result)

    def test_unseparated_mixed_prose_stops_without_changing_japanese(self):
        engine = Mock()
        with self.assertRaises(argos.TranslationError):
            argos.translate_text('既存の説明 and update details', engine)
        engine.assert_not_called()

    def test_names_code_and_identifiers_never_reach_engine(self):
        text = 'AdGuard Custom Rules GitHub Actions myFunction my_func CONFIG_KEY\n```python\nx = 1\n```'
        engine = Mock()
        self.assertEqual(argos.translate_text(text, engine), text)
        engine.assert_not_called()

    def test_empty_english_truncated_and_failed_translation_stop(self):
        for value in ('', 'unchanged English', '日本語\n欠落', None):
            with self.subTest(value=value), self.assertRaises(argos.TranslationError):
                argos.translate_text('Update description', lambda text: value)
        with self.assertRaises(argos.TranslationError):
            argos.translate_text('Update description', Mock(side_effect=RuntimeError()))

    def test_unverified_model_never_downloads(self):
        with patch.object(argos.urllib.request, 'urlopen') as download:
            with self.assertRaises(argos.TranslationError):
                argos.load_engine()
            download.assert_not_called()

    def model_fixture(self, metadata=None):
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as archive:
            archive.writestr('translate-en_ja-1_1/metadata.json', json.dumps(metadata or {
                'from_code': 'en', 'to_code': 'ja', 'package_version': '1.1'}))
        return data.getvalue()

    def load_with_fixture(self, data, digest=None, download_error=None):
        root = types.ModuleType('argostranslate')
        root.package = Mock()
        root.translate = Mock()
        root.package.get_installed_packages.return_value = [types.SimpleNamespace(
            from_code='en', to_code='ja', package_version='1.1')]
        manifest = {'sha256': digest or hashlib.sha256(data).hexdigest(), 'license_verified': True}
        with patch.object(Path, 'read_text', return_value=json.dumps(manifest)), \
                patch.dict(sys.modules, {'argostranslate': root,
                                        'argostranslate.package': root.package,
                                        'argostranslate.translate': root.translate}), \
                patch.object(argos.urllib.request, 'urlopen', side_effect=download_error,
                             return_value=io.BytesIO(data)) as download:
            try:
                result = argos.load_engine()
                root.package.install_from_path.assert_called_once()
                return result
            finally:
                download.assert_called_once()

    def test_model_download_failure_stops(self):
        with self.assertRaisesRegex(argos.TranslationError, '取得・検証・初期化'):
            self.load_with_fixture(b'', download_error=OSError())

    def test_model_hash_mismatch_stops(self):
        with self.assertRaisesRegex(argos.TranslationError, 'SHA256'):
            self.load_with_fixture(self.model_fixture(), digest='a' * 64)

    def test_wrong_language_or_version_stops(self):
        for changes in ({'to_code': 'fr'}, {'package_version': '2.0'}):
            metadata = {'from_code': 'en', 'to_code': 'ja', 'package_version': '1.1', **changes}
            with self.subTest(changes=changes), self.assertRaisesRegex(argos.TranslationError, '言語・Version'):
                self.load_with_fixture(self.model_fixture(metadata))

    def test_verified_model_fixture_initializes_engine(self):
        self.assertTrue(callable(self.load_with_fixture(self.model_fixture())))


if __name__ == '__main__':
    unittest.main()
