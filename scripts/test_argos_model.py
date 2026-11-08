#!/usr/bin/env python3
"""固定モデルの実翻訳をRunner上で確認する。GitHubの更新APIは使わない。"""
import json
from unittest.mock import patch
from argos_commit_translation import load_engine, translate_text, translate_payload
from automate_japanese_commits import validate_translation


def main():
    engine = load_engine()
    samples = [
        'Update documentation',
        'Fix a bug',
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
        if 'Update README.md' in source:
            assert '更新' in target
            assert 'ニュース' not in target

        for term in ('README.md', 'https://example.com/a', '#12', '`my_func`', 'v1.2.3', 'GitHub Actions', 'c77ede4b', 'a1' * 20, '`~~~`'):
            if term in source:
                assert term in target, term
        if source in ('fix: 説明を修正', 'feat(core): READMEの説明を更新') or source.startswith(('```', '- 検証例')):
            assert target == source
        if source.startswith('既存の日本語文章'):
            assert target == source
        if source.startswith('既存の説明\n'):
            assert target.startswith('既存の説明\n')

    original = {'title': 'Update README.md',
                'body': '既存の説明\nSee https://example.com/a #12 `my_func` v1.2.3',
                'commits': [{'sha': 'a' * 40, 'message': 'Fix GitHub Actions configuration'}]}
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        translated = validate_translation(original, translate_payload(original, engine))
    assert translated['messages']['a' * 40] == translated['commits'][0]['message']
    print(json.dumps({'pipeline': translated}, ensure_ascii=False))


if __name__ == '__main__':
    main()
