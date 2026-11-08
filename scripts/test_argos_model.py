#!/usr/bin/env python3
"""固定モデルの実翻訳をRunner上で確認する。GitHubの更新APIは使わない。"""
import json
from argos_commit_translation import load_engine, translate_text


def main():
    engine = load_engine()
    samples = [
        'Update documentation',
        'Fix a bug',
        'Do not remove existing tests.',
        'Update README.md\n\nSee https://example.com/a #12 `my_func` v1.2.3',
        '既存の日本語文章。READMEの説明を更新\n',
        '既存の説明\nUpdate README.md',
        'Fix GitHub Actions configuration',
    ]
    for source in samples:
        target = translate_text(source, engine)
        print(json.dumps({'source': source, 'target': target}, ensure_ascii=False))
        assert target.strip()
        for term in ('README.md', 'https://example.com/a', '#12', '`my_func`', 'v1.2.3', 'GitHub Actions'):
            if term in source:
                assert term in target, term
        if source.startswith('既存の日本語文章'):
            assert target == source
        if source.startswith('既存の説明'):
            assert target.startswith('既存の説明\n')


if __name__ == '__main__':
    main()
