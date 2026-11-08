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
    def test_squash_merge_command_keeps_merge_as_english_prose(self):
        from automate_japanese_commits import validate_translation
        source = 'Squash merge main'
        engine = Mock(side_effect=lambda value: value.replace(' merge ', 'で統合 '))
        target = argos.translate_text(source, engine)
        self.assertEqual(target, 'Squashで統合 main')
        self.assertIn(' merge ', engine.call_args[0][0])
        validate_translation({'title': source, 'body': '', 'commits': []},
                             {'title': target, 'body': '', 'commits': []})

    def test_term_suffix_does_not_mask_ordinary_english_word(self):
        engine = Mock(return_value='字幕の描画を更新')
        self.assertEqual(argos.translate_text('Update subtitle rendering', engine), '字幕の描画を更新')
        engine.assert_called_once_with('Update subtitle rendering')

    def test_japanese_commit_message_term_is_preserved(self):
        source = '日本語の本文と全Commit messageを原文のまま扱います。'
        engine = Mock()
        self.assertEqual(argos.translate_text(source, engine), source)
        engine.assert_not_called()

    def test_english_merge_and_push_commands_are_translated(self):
        from automate_japanese_commits import validate_translation
        for verb in ('Merge', 'merge', 'push'):
            with self.subTest(verb=verb):
                source = verb + ' main'
                engine = Mock(side_effect=lambda value: value.replace(verb + ' ', '') + 'へ統合')
                target = argos.translate_text(source, engine)
                self.assertEqual(target, 'mainへ統合')
                engine.assert_called_once()
                original = {'title': source, 'body': '', 'commits': []}
                validate_translation(original, {'title': target, 'body': '', 'commits': []})

    def test_pr259_payload_is_unchanged_without_calling_translation_engine(self):
        from automate_japanese_commits import validate_translation
        original = json.loads((Path(__file__).parent / 'fixtures/pr259-japanese-translation.json').read_text())
        engine = Mock(side_effect=AssertionError('日本語本文の技術表記を翻訳器へ渡しています。'))
        translated = argos.translate_payload(original, engine)
        self.assertEqual(translated, original)
        validate_translation(original, translated)
        engine.assert_not_called()

    def test_english_prose_around_workflow_terms_still_requires_translation(self):
        source = 'Fix concurrency group configuration'
        engine = Mock(side_effect=lambda text: text.replace('Fix ', '').replace(' configuration', 'の設定を修正'))
        self.assertEqual(argos.translate_text(source, engine), 'concurrency groupの設定を修正')
        engine.assert_called_once()

    def test_pr251_payload_is_unchanged_without_calling_translation_engine(self):
        from automate_japanese_commits import validate_translation
        original = json.loads((Path(__file__).parent / 'fixtures/pr251-japanese-translation.json').read_text())
        engine = Mock(side_effect=AssertionError('日本語本文の技術表記を翻訳器へ渡しています。'))
        translated = argos.translate_payload(original, engine)
        self.assertEqual(translated, original)
        validate_translation(original, translated)
        engine.assert_not_called()

    def test_issue_references_next_to_japanese_are_preserved(self):
        for source in ('PR #248で復元します。', '前回#251の承認',
                       'Red-Frame-X/Prototype#251を確認します。',
                       'Yahoo!ニュースのExtendedCss非表示を確認します。'):
            with self.subTest(source=source):
                engine = Mock(side_effect=AssertionError('保護表記の翻訳'))
                self.assertEqual(argos.translate_text(source, engine), source)
                engine.assert_not_called()

    def test_english_prose_around_new_terms_still_requires_translation(self):
        source = 'Fix Yahoo! ExtendedCss configuration'
        engine = Mock(side_effect=lambda text: text.replace('Fix ', '').replace(' configuration', 'の設定を修正'))
        self.assertEqual(argos.translate_text(source, engine), 'Yahoo! ExtendedCssの設定を修正')
        engine.assert_called_once()

    def test_pr248_payload_is_unchanged_without_calling_translation_engine(self):
        from automate_japanese_commits import validate_translation
        original = json.loads((Path(__file__).parent / 'fixtures/pr248-japanese-translation.json').read_text())
        engine = Mock(side_effect=AssertionError('日本語化済みの本文を翻訳器へ渡しています。'))
        translated = argos.translate_payload(original, engine)
        self.assertEqual(translated, original)
        self.assertEqual(validate_translation(original, translated)['messages'][original['commits'][0]['sha']],
                         original['commits'][0]['message'])
        engine.assert_not_called()

    def test_japanese_prose_with_branch_hook_and_acronyms_needs_no_translation(self):
        for source in ('mainには既に回帰Testがあります。',
                       'pre-commit検査で拒否します。',
                       'VersionをJSTで更新します。',
                       '既存のHTTP設定とUTF8の表記を保持します。'):
            engine = Mock()
            with self.subTest(source=source):
                self.assertEqual(argos.translate_text(source, engine), source)
                engine.assert_not_called()

    def test_main_substring_does_not_hide_ordinary_english(self):
        for source in ('Update domain description', 'Fix mainly failing tests'):
            engine = Mock(return_value='一般説明を更新')
            self.assertEqual(argos.translate_text(source, engine), '一般説明を更新')
            engine.assert_called_once_with(source)

    def test_naked_short_and_full_commit_hashes_are_protected(self):
        hashes = ('c77ede4b', '1a2b3c4', 'a1' * 20)
        source = 'Update ' + ' and '.join(hashes)
        engine = Mock(side_effect=lambda value: value.replace('Update ', '').replace(' and ', 'と') + 'を更新')
        target = argos.translate_text(source, engine)
        for sha in hashes:
            self.assertEqual(target.count(sha), 1)
            self.assertNotIn(sha, engine.call_args[0][0])

    def test_inflected_commit_verbs_are_translated(self):
        for verb in ('Updated', 'Added', 'Fixed', 'Updating', 'Fixes', 'Removed', 'Built'):
            engine = Mock(side_effect=lambda value: value.replace(verb + ' ', '') + 'を更新')
            with self.subTest(verb=verb):
                self.assertEqual(argos.translate_text(verb + ' README.md', engine), 'README.mdを更新')
                self.assertTrue(engine.call_args[0][0].startswith(verb + ' '))

    def test_japanese_conventional_commit_does_not_call_engine(self):
        for text in ('fix: 説明を修正', 'feat(core): READMEの説明を更新', 'fix!: 説明を修正\n'):
            engine = Mock()
            with self.subTest(text=text):
                self.assertEqual(argos.translate_text(text, engine), text)
                engine.assert_not_called()

    def test_code_span_and_other_fence_contents_are_opaque(self):
        for text in ('`~~~`', '```python\nvalue = "~~~"\n```',
                     '~~~python\nvalue = "```"\n~~~', '``literal ` character``',
                     '````python\n```\n````'):
            engine = Mock()
            with self.subTest(text=text):
                self.assertEqual(argos.translate_text(text, engine), text)
                engine.assert_not_called()

    def test_indented_list_fences_and_code_lines_never_reach_engine(self):
        for text in ('- 検証例\n\n    ~~~sh\n    echo hello\n    ~~~\n',
                     '- 検証例\n\n    ```sh\n    echo hello\n    ```\n',
                     '        ~~~sh\n        echo hello\n        ~~~\n',
                     '\t~~~sh\n\techo hello\n\t~~~\n',
                     '    echo hello\n    echo world\n',
                     '- ~~~sh\n  echo hello\n  ~~~\n',
                     '1. ~~~sh\n   echo hello\n   ~~~\n',
                     '> ~~~sh\n> echo hello\n> ~~~\n',
                     '> - ~~~sh\n>   echo hello\n>   ~~~\n'):
            engine = Mock()
            with self.subTest(text=text):
                self.assertEqual(argos.translate_text(text, engine), text)
                engine.assert_not_called()

    def test_literal_fence_in_indented_code_does_not_need_closing_fence(self):
        text = '    ~~~sh\n    echo hello\n'
        engine = Mock()
        self.assertEqual(argos.translate_text(text, engine), text)
        engine.assert_not_called()

    def test_task_list_markers_are_not_translated(self):
        for box in ('[x]', '[X]', '[ ]'):
            for prefix in ('- ', '1. '):
                text = prefix + box + ' 説明を更新'
                engine = Mock()
                with self.subTest(text=text):
                    self.assertEqual(argos.translate_text(text, engine), text)
                    engine.assert_not_called()
                engine = lambda value: value.replace('Update ', '') + 'を更新'
                self.assertEqual(argos.translate_text(prefix + box + ' Update README.md', engine),
                                 prefix + box + ' README.mdを更新')

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
        engine = Mock(side_effect=lambda value: value.replace('Update ', '').replace('See ', '') + 'を更新')
        text = '既存の説明\nUpdate README.md https://example.com/a #12 `my_func` v1.2.3\n'
        result = argos.translate_text(text, engine)
        self.assertTrue(result.startswith('既存の説明\nREADME.md'))
        for value in ('README.md', 'https://example.com/a', '#12', '`my_func`', 'v1.2.3'):
            self.assertIn(value, result)

    def test_mixed_prose_keeps_japanese_with_sentence_context(self):
        engine = Mock(side_effect=lambda value: value.replace('and update details', 'と詳細を更新'))
        source = '既存の説明 and update details'
        self.assertEqual(argos.translate_text(source, engine), '既存の説明 と詳細を更新')
        self.assertIn('and update details', engine.call_args[0][0])
        self.assertNotIn('既存の説明', engine.call_args[0][0])

    def test_lost_duplicate_or_corrupt_placeholder_stops(self):
        for target in ('説明を更新', 'ZXQ0000QXZ ZXQ0000QXZの更新', 'ZXQ9999QXZの更新'):
            with self.subTest(target=target), self.assertRaises(argos.TranslationError):
                argos.translate_text('Update README.md', lambda value: target)

    def test_fix_action_is_japanese_and_general_english_cannot_remain(self):
        self.assertEqual(argos.translate_text('Fix README.md', lambda value: 'Fix ZXQ0000QXZの説明'),
                         'README.mdの説明を修正')
        with self.assertRaises(argos.TranslationError):
            argos.translate_text('Update README.md', lambda value: 'Update ZXQ0000QXZを更新')

    def test_names_code_and_identifiers_never_reach_engine(self):
        text = 'AdGuard Custom Rules GitHub Actions Prototype Python Acme myFunction my_func CONFIG_KEY\n```python\nx = 1\n```'
        engine = Mock()
        self.assertEqual(argos.translate_text(text, engine), text)
        engine.assert_not_called()

    def test_empty_english_truncated_and_failed_translation_stop(self):
        for value in ('', 'unchanged English', '日本語\n欠落', '日本語\r', None):
            with self.subTest(value=value), self.assertRaises(argos.TranslationError):
                argos.translate_text('Update description', lambda text: value)
        with self.assertRaises(argos.TranslationError):
            argos.translate_text('Update description', Mock(side_effect=RuntimeError()))

    def test_unverified_model_never_downloads(self):
        with patch.object(argos.urllib.request, 'urlopen') as download, \
                patch.object(Path, 'read_text', return_value=json.dumps({'sha256': None})):
            with self.assertRaises(argos.TranslationError):
                argos.load_engine()
            download.assert_not_called()

    def test_conventional_prefix_and_markdown_structure_are_preserved(self):
        engine = lambda value: value.replace('Update ', '') + 'の更新'
        self.assertEqual(argos.translate_text('feat(core): Update README.md\n', engine),
                         'feat(core): README.mdの更新\n')
        self.assertEqual(argos.translate_text('- Update README.md\n', engine),
                         '- README.mdの更新\n')
        self.assertEqual(argos.translate_text('> Official English quotation\n', Mock()),
                         '> Official English quotation\n')

    def test_unverified_license_never_downloads(self):
        with patch.object(argos.urllib.request, 'urlopen') as download, \
                patch.object(Path, 'read_text', return_value=json.dumps({
                    'sha256': 'a' * 64, 'license_verified': False})):
            with self.assertRaisesRegex(argos.TranslationError, 'ライセンス'):
                argos.load_engine()
            download.assert_not_called()

    def test_unterminated_code_or_reserved_marker_stops(self):
        for text in ('```python\nx = 1', '~~~code', 'Update `identifier', 'Update ZXQ0000QXZ'):
            with self.subTest(text=text), self.assertRaises(argos.TranslationError):
                argos.translate_text(text, Mock())

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
        with patch.object(argos, 'configure_offline_engine'), \
                patch.object(Path, 'read_text', return_value=json.dumps(manifest)), \
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
