"""辞書、構文保護、固定モデルのCache復旧を検証する。"""
import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import argos_commit_translation as argos
from find_argos_glossary_candidates import candidates


class GlossaryTests(unittest.TestCase):
    def test_schema_and_existing_terms(self):
        self.assertEqual(len(argos.load_glossary(argos.GLOSSARY_PATH)), 11)
        examples = (
            'B\tunknown\n', 'C\tPatch\n', 'B\tbad\tEnglish only\n',
            'A\tGitHub Actions\n', 'A\tDoH\nB\tdoh\t説明\n',
            '[Example]\nA\tNew Name\n', 'A\t bad\n',
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'terms.tsv'
            for example in examples:
                with self.subTest(example=example):
                    path.write_text('[Example]\n' + example, encoding='utf-8')
                    with self.assertRaises(argos.TranslationError):
                        argos.load_glossary(path)

    def test_known_noun_phrases_prefer_longest_and_accept_plural_and_case(self):
        for source, expected in (
            ('Fix PULL REQUEST MERGE CONFLICT', 'Pull Requestのマージ競合を修正'),
            ('Add regression tests', '回帰テストを追加'),
            ('Improve REGRESSION TEST', '回帰テストを改善'),
            ('Update GitHub Actions dependencies', 'GitHub Actionsの依存関係を更新'),
            ('Fix false positive in DNS filtering', 'DNSフィルタリングの誤ブロックを修正'),
        ):
            with self.subTest(source=source):
                engine = Mock(side_effect=AssertionError)
                result = argos.translate_text(source, engine)
                self.assertEqual(result, expected)
                self.assertEqual(argos.translate_text(result, engine), result)
                engine.assert_not_called()

    def test_glossary_only_lines_are_translated_without_argos(self):
        source = 'regression tests\n## Dependency resolution\n既存のregression testsを確認\n'
        engine = Mock(side_effect=AssertionError)
        self.assertEqual(argos.translate_text(source, engine),
                         '回帰テスト\n## 依存関係の解決\n既存のregression testsを確認\n')
        engine.assert_not_called()

    def test_full_product_name_precedes_generic_hyphenated_identifiers(self):
        product = 'uB-filter-by-kdroidwin (AdGuard Optimized)'
        engine = Mock(return_value='ZXQ0000QXZを更新')
        self.assertEqual(argos.translate_text('Update ' + product, engine), product + 'を更新')
        engine.assert_called_once_with('Update ZXQ0000QXZ')

    def test_case_boundaries_and_context(self):
        engine = Mock(return_value='ZXQ0000QXZを確認')
        argos.translate_text('Check doh and dependenciesExtra', engine)
        engine.assert_called_once_with('Check doh and ZXQ0000QXZ')
        self.assertEqual(argos.translate_text('DoHと回帰テストを確認', Mock(side_effect=AssertionError)),
                         'DoHと回帰テストを確認')
        engine = Mock(return_value='内容を確認')
        argos.translate_text('Check interdependency and config', engine)
        engine.assert_called_once_with('Check interdependency and config')

    def test_filter_literals_tables_and_markdown_links(self):
        protected = (
            '@@||example.com^$domain=test.example,script\r\n'
            'example.com##+js(remove-node-text, script, Example)\r\n'
            'example.com#@?#div:has(.banner)\r\n'
            '// @name:ja Japanese metadata\r\n'
            '$ git rebase --continue\r\n'
            '> Quoted upstream text\r\n\r\n'
            'Header | Value\r\n--- | ---\r\nKey | Selector\r\n'
        )
        engine = Mock(side_effect=AssertionError)
        self.assertEqual(argos.translate_text(protected, engine), protected)
        engine.assert_not_called()
        source = 'Update [configuration](<docs/a(b).md> "Link title") <em lang="en">docs</em>'
        def reply(line):
            link, opening, closing = argos.MARKER.findall(line)
            return f'{link}の{opening}文書{closing}を更新'
        self.assertEqual(argos.translate_text(source, reply),
                         '[configuration](<docs/a(b).md> "Link title")の<em lang="en">文書</em>を更新')

    def test_addresses_paths_and_flags_are_restored_exactly(self):
        literals = (
            'user+filter@example.com', 'mailto:user@example.com', '192.0.2.1',
            '2001:db8::1', '/usr/local/bin/check', r'C:\Tools\verify.exe',
            '/^[a-z]+$/iu', 'git rebase', '--force-with-lease', '$removeparam',
        )
        for literal in literals:
            with self.subTest(literal=literal):
                engine = Mock(return_value='ZXQ0000QXZを確認')
                self.assertEqual(argos.translate_text(f'Check {literal}', engine), f'{literal}を確認')
                engine.assert_called_once_with('Check ZXQ0000QXZ')

    def test_json_document_is_retained(self):
        source = '{\n  "value": "Do not translate",\n  "enabled": false\n}'
        engine = Mock(side_effect=AssertionError)
        self.assertEqual(argos.translate_text(source, engine), source)
        engine.assert_not_called()

    def test_structural_reordering_and_new_markdown_are_rejected(self):
        with self.assertRaisesRegex(argos.TranslationError, '順序'):
            argos.translate_text('Update `test` and `fixture`', lambda _: 'ZXQ0001QXZとZXQ0000QXZを更新')
        with self.assertRaisesRegex(argos.TranslationError, 'Markdown'):
            argos.translate_text('Update docs', lambda _: '# ドキュメントを更新')

    def test_candidate_extraction_uses_existing_registrations(self):
        self.assertEqual(candidates(['AdGuard GitHub Actions SOME_API', 'SOME_API OTHER_TOOL']),
                         [('SOME_API', 2), ('OTHER_TOOL', 1)])


class CacheRecoveryTests(unittest.TestCase):
    def test_repair_requires_verified_download(self):
        verified = b'expected archive bytes'
        digest = hashlib.sha256(verified).hexdigest()
        with tempfile.TemporaryDirectory() as root, patch.dict(os.environ, {'ARGOS_MODEL_CACHE_DIR': root}):
            archive = Path(root) / (digest + '.argosmodel')
            archive.write_bytes(b'corrupt')
            with patch.object(argos, 'download_model', side_effect=lambda path: path.write_bytes(b'wrong')):
                with self.assertRaisesRegex(argos.TranslationError, 'SHA256'):
                    argos.model_archive(root, digest, recover_cache=True)
                self.assertEqual(archive.read_bytes(), b'corrupt')
            with patch.object(argos, 'download_model', side_effect=lambda path: path.write_bytes(verified)) as download:
                self.assertEqual(argos.model_archive(root, digest, recover_cache=True), archive)
                self.assertEqual(argos.model_archive(root, digest, recover_cache=True).read_bytes(), verified)
                download.assert_called_once()

    def test_network_timeout_has_bounded_retries(self):
        with tempfile.TemporaryDirectory() as root:
            archive = Path(root) / 'model.argosmodel'
            with patch.object(argos.urllib.request, 'urlopen', side_effect=TimeoutError) as open_url, \
                    patch.object(argos.time, 'sleep') as sleep:
                with self.assertRaisesRegex(argos.TranslationError, '再試行上限'):
                    argos.download_model(archive)
            self.assertEqual(open_url.call_count, 4)
            self.assertEqual(sleep.call_count, 3)
            self.assertFalse(archive.exists())


if __name__ == '__main__':
    unittest.main()
