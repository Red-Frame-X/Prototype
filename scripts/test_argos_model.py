#!/usr/bin/env python3
"""固定モデルの実翻訳をRunner上で確認する。GitHubの更新APIは使わない。"""
import json
from pathlib import Path
from unittest.mock import patch
from argos_commit_translation import load_engine, translate_text, translate_payload
from automate_japanese_commits import validate_translation


def main():
    engine = load_engine()
    samples = [
        'Update documentation',
        'Fix a bug',
        'Merge main',
        'Merge SHA abcdef1',
        'Squash merge main',
        'Update subtitle rendering',
        'Do not remove existing tests.',
        'Update README.md\n\nSee https://example.com/a #12 `my_func` v1.2.3',
        '既存の日本語文章。READMEの説明を更新\n',
        '既存の説明\nUpdate README.md',
        '既存の説明: Update README.md',
        'Fix GitHub Actions configuration',
        'Updated README.md',
        'Added documentation',
        'Fixed a bug',
        'Update README.md c77ede4b ' + 'a1' * 20,
        'fix: 説明を修正',
        'feat(core): READMEの説明を更新',
        'Code fence example: `~~~`',
        '```python\nvalue = "~~~"\n```',
        '- 検証例\n\n    ~~~sh\n    echo hello\n    ~~~\n',
        '    ~~~sh\n    echo hello\n',
        '- [x] Update README.md',
        '- [x] 説明を更新',
    ]
    for source in samples:
        # モデル導入後はネットワークを禁止して実翻訳する。
        with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
            target = translate_text(source, engine)
        print(json.dumps({'source': source, 'target': target}, ensure_ascii=False))
        assert target.strip()
        expected = {
            'Update documentation': ('ドキュメント', '更新'),
            'Fix a bug': ('バグ', '修正'),
            'Do not remove existing tests.': ('既存', 'テスト', '削除しない'),
            'Fix GitHub Actions configuration': ('GitHub Actions', '設定', '修正'),
        }
        for word in expected.get(source, ()):
            assert word in target, (source, target, word)
        if source.startswith('- [x]'):
            assert target.startswith('- [x] ')
        if 'Update README.md' in source:
            assert '更新' in target
            assert 'ニュース' not in target

        for term in ('README.md', 'https://example.com/a', '#12', '`my_func`', 'v1.2.3', 'GitHub Actions', 'c77ede4b', 'a1' * 20, '`~~~`'):
            if term in source:
                assert term in target, term
        if source in ('fix: 説明を修正', 'feat(core): READMEの説明を更新') or source.startswith(('```', '- 検証例', '    ~~~', '- [x] 説明')):
            assert target == source
        if source.startswith('既存の日本語文章'):
            assert target == source
        if source.startswith('既存の説明\n'):
            assert target.startswith('既存の説明\n')

    # 実際に停止した日本語PRのスナップショット。本文はGitHubへ送信・更新しない。
    snapshot = Path(__file__).resolve().parents[1] / 'tests/fixtures/pr248-japanese-translation.json'
    original_japanese = json.loads(snapshot.read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        def forbidden_translation(source):
            raise AssertionError('日本語化済みの本文を翻訳器へ渡しています。')
        unchanged = translate_payload(original_japanese, forbidden_translation)
    assert unchanged == original_japanese
    validate_translation(original_japanese, unchanged)
    print('PR #248: title・body・Commit messageを翻訳器の呼出しなしで原文のまま保持しました。')

    snapshot251 = snapshot.with_name('pr251-japanese-translation.json')
    original251 = json.loads(snapshot251.read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        unchanged251 = translate_payload(original251, forbidden_translation)
    assert unchanged251 == original251
    validate_translation(original251, unchanged251)
    print('PR #251: title・body・Commit messageの技術表記とIssue参照を原文のまま保持しました。')

    original259 = json.loads(snapshot.with_name('pr259-japanese-translation.json').read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        unchanged259 = translate_payload(original259, forbidden_translation)
    assert unchanged259 == original259
    validate_translation(original259, unchanged259)
    print('PR #259: Workflowの技術表記を含む日本語本文を翻訳器の呼出しなしで保持しました。')

    original = {'title': 'Update README.md',
                'body': '既存の説明\nSee https://example.com/a #12 `my_func` v1.2.3',
                'commits': [{'sha': 'a' * 40, 'message': 'Fix GitHub Actions configuration'}]}
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        translated = validate_translation(original, translate_payload(original, engine))
    assert translated['messages']['a' * 40] == translated['commits'][0]['message']
    print(json.dumps({'pipeline': translated}, ensure_ascii=False))


if __name__ == '__main__':
    main()
