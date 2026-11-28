#!/usr/bin/env python3
"""固定モデルの実翻訳をRunner上で確認する。GitHubの更新APIは使わない。"""
import json
import os
from pathlib import Path
from unittest.mock import patch
from argos_commit_translation import load_engine, translate_text, translate_payload
from automate_japanese_commits import validate_translation


def main():
    engine = load_engine()
    if os.environ.get('ARGOS_MODEL_CACHE_DIR'):
        with patch('urllib.request.urlopen', side_effect=AssertionError('cache利用中の再取得')):
            assert callable(load_engine())
        print('固定hashを再検証し、モデルのarchiveを再取得せず再利用しました。')
    samples = [
        'Update documentation',
        'Update hash calculation',
        'Fix a bug',
        'Update check:offline',
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
        "Fix ${{ github.event_name == 'pull_request' }}",
        "起動条件は${{ contains(github.ref, 'release') }}を使用",
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
        'Update documentation\n\nCo-authored-by: Alice Example <alice@example.com>\n'
        'Signed-off-by: 日本語の名前 <author@example.com>\n',
    ]
    for source in samples:
        # モデル導入後はネットワークを禁止して実翻訳する。
        with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
            target = translate_text(source, engine)
        print(json.dumps({'source': source, 'target': target}, ensure_ascii=False))
        assert target.strip()
        if '${{' in source:
            from argos_commit_translation import ACTION_EXPRESSION
            assert ACTION_EXPRESSION.findall(target) == ACTION_EXPRESSION.findall(source)
            if source.startswith('Fix '):
                assert '修正' in target
            else:
                assert target == source
        if '\nCo-authored-by:' in source:
            assert target.split('\n\n', 1)[1] == source.split('\n\n', 1)[1]
            assert '更新' in target.splitlines()[0]
        expected = {
            'Update documentation': ('ドキュメント', '更新'),
            'Fix a bug': ('バグ', '修正'),
            'Do not remove existing tests.': ('既存', 'テスト', '削除しない'),
            'Fix GitHub Actions configuration': ('GitHub Actions', '設定', '修正'),
        }
        for word in expected.get(source, ()):
            assert word in target, (source, target, word)
        if source == 'Update hash calculation':
            assert 'hash' in target and '更新' in target, target
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

    # 辞書を使った定型表現と、実モデルが組み立てる英文を別々に検証する。
    glossary_titles = {
        'Fix workflow failure': ('Workflow', '実行エラー', '修正'),
        'Update translation glossary': ('翻訳用語辞書', '更新'),
        'Fix pull request merge conflict': ('Pull Request', 'マージ競合', '修正'),
        'Add regression tests': ('回帰テスト', '追加'),
        'Update GitHub Actions dependencies': ('GitHub Actions', '依存関係', '更新'),
        'Fix Argos model cache restoration': ('Argosモデル', 'Cache復元処理', '修正'),
        'Preserve filter rule syntax': ('フィルタリングルール', '構文', '維持'),
        'Fix false positive in DNS filtering': ('DNSフィルタリング', '誤ブロック', '修正'),
        'Prevent duplicate workflow runs': ('Workflow', '重複実行', '防止'),
        'Fix UserScript metadata handling': ('UserScript', 'Metadata処理', '修正'),
        'Improve Markdown Notes validation': ('Markdown Notes', '検証', '改善'),
        'Fix placeholder restoration': ('Placeholder', '復元処理', '修正'),
        'Update AdGuard Custom Rules': ('AdGuard Custom Rules', '更新'),
        'Fix upstream filter conversion': ('上流フィルタ', '変換処理', '修正'),
        'Prevent infinite translation loops': ('翻訳処理', '無限ループ', '防止'),
        'Check documentation for regression tests': ('回帰テスト', 'ドキュメント'),
        'Use the new DNS resolver': ('DNSリゾルバー', '新しい', '使用'),
    }
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        for source, expected in glossary_titles.items():
            target = translate_text(source, engine)
            assert all(word in target for word in expected), (source, target, expected)

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

    original261 = json.loads(snapshot.with_name('pr261-japanese-translation.json').read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        unchanged261 = translate_payload(original261, forbidden_translation)
        assert translate_payload(original261, engine) == original261
    assert unchanged261 == original261
    validate_translation(original261, unchanged261)
    print('PR #261: 日本語に隣接するファイル名・技術表記・コマンドを原文のまま保持しました。')

    original291 = json.loads(snapshot.with_name('pr291-japanese-translation.json').read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        unchanged291 = translate_payload(original291, forbidden_translation)
        assert translate_payload(original291, engine) == original291
    assert unchanged291 == original291
    validate_translation(original291, unchanged291)
    print('PR #291: 依存名・npm audit・設定値を含む日本語本文を原文のまま保持しました。')

    original292 = json.loads(snapshot.with_name('pr292-japanese-translation.json').read_text())
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        unchanged292 = translate_payload(original292, forbidden_translation)
        assert translate_payload(original292, engine) == original292
    assert unchanged292 == original292
    validate_translation(original292, unchanged292)
    print('PR #292: 追加の依存名・Branch protection・Xを原文のまま保持しました。')

    for number in (311, 312, 319):
        source = json.loads(snapshot.with_name(f'pr{number}-japanese-translation.json').read_text())
        with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
            assert translate_payload(source, forbidden_translation) == source
            assert translate_payload(source, engine) == source
        validate_translation(source, source)
        print(f'PR #{number}: 日本語本文中のコマンド名・技術表記を原文のまま保持しました。')

    original = {'title': 'Update README.md',
                'body': '既存の説明\nSee https://example.com/a #12 `my_func` v1.2.3',
                'commits': [{'sha': 'a' * 40, 'message': 'Fix GitHub Actions configuration'}]}
    with patch('socket.socket.connect', side_effect=AssertionError('翻訳中の外部通信')):
        translated = validate_translation(original, translate_payload(original, engine))
    assert translated['messages']['a' * 40] == translated['commits'][0]['message']
    print(json.dumps({'pipeline': translated}, ensure_ascii=False))
    from test_argos_automation_lifecycle import run_end_to_end
    with patch('socket.socket.connect', side_effect=AssertionError('一連の検証中の外部通信')):
        run_end_to_end(engine)


if __name__ == '__main__':
    main()
