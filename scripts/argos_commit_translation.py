"""Argosの固定英日モデルを使い、保護表記を翻訳器へ渡さずに日本語化する。"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import tempfile
import urllib.request
import zipfile


class TranslationError(RuntimeError):
    pass


ROOT = Path(__file__).resolve().parents[1]
JAPANESE = re.compile(r'[ぁ-んァ-ヶ一-龠]')
# 固定名称は長いものから照合する。引用・コード・URLは原文のまま残す。
TERMS = (
    'AdGuard Browser Extension MV3', 'AdGuard DNS Custom Rules', 'AdGuard Custom Rules',
    'uB-filter-by-kdroidwin (AdGuard Optimized)', 'NG Word Regex for ChMate',
    'Markdown Notes', 'GitHub Actions', 'Pull Request', 'uBlock Origin',
    'Argos Translate', 'Codex Review', 'UserScript', 'Workflow', 'Commit', 'Branch',
    'Repository', 'README', 'GitHub', 'AdGuard', 'Version', 'AGLint', 'Markdownlint',
    'CI', 'Lint', 'Test', 'Script', 'API', 'PR', 'Issue',
)
PROTECTED = re.compile(
    r'```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]+`|https?://[^\s<>]+|'
    r'(?<!\w)(?:[\w.-]+/[\w.-]+)?#\d+\b|'
    + '|'.join(re.escape(term) + r'(?![A-Za-z0-9_./-])' for term in TERMS)
    + r'|\b(?:[A-Za-z0-9_.-]+(?:/|\.)[A-Za-z0-9_./-]+|v?\d+(?:\.\d+)+(?:[-+][\w.-]+)?|[A-Z][A-Z0-9_]+|'
      r'\w*[a-z][A-Z]\w*|\w+_\w+|[\w.-]+(?:/|\.)[\w./-]+)\b'
)


def load_engine():
    """既定Branchの固定情報だけから取得し、hashとMetadataを確認する。"""
    manifest = json.loads((ROOT / '.github/argos-model.json').read_text())
    digest = manifest.get('sha256')
    if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
        raise TranslationError('英日モデルのSHA256が未確認です。取得・実物確認後に固定してください。')
    if not manifest.get('license_verified'):
        raise TranslationError('英日モデル個別のライセンス確認が未完了です。')
    try:
        import argostranslate.package as package
        import argostranslate.translate as translate
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'model.argosmodel'
            # 認証情報も翻訳対象本文も送信しない。配布先は固定する。
            with urllib.request.urlopen(
                    'https://argos-net.com/v1/translate-en_ja-1_1.argosmodel', timeout=90) as response:
                with archive.open('wb') as output:
                    total = 0
                    while chunk := response.read(1024 * 1024):
                        total += len(chunk)
                        if total > 500_000_000:
                            raise TranslationError('モデルが取得上限を超えました。')
                        output.write(chunk)
            if hashlib.sha256(archive.read_bytes()).hexdigest() != digest:
                raise TranslationError('モデルのSHA256が一致しません。')
            with zipfile.ZipFile(archive) as zipped:
                names = zipped.namelist()
                if any(Path(name).is_absolute() or '..' in Path(name).parts for name in names):
                    raise TranslationError('モデルに不正なPathがあります。')
                metadata_names = [name for name in names if name.endswith('/metadata.json')]
                if len(metadata_names) != 1:
                    raise TranslationError('モデルのMetadataが一意ではありません。')
                metadata = json.loads(zipped.read(metadata_names[0]))
                if any(metadata.get(key) != value for key, value in
                       {'from_code': 'en', 'to_code': 'ja', 'package_version': '1.1'}.items()):
                    raise TranslationError('モデルの言語・Versionが一致しません。')
            package.install_from_path(archive)
        installed = package.get_installed_packages()
        if len(installed) != 1 or (installed[0].from_code, installed[0].to_code,
                                  installed[0].package_version) != ('en', 'ja', '1.1'):
            raise TranslationError('固定モデル以外がインストールされています。')
        engine = translate.get_translation_from_codes('en', 'ja')
        return engine.translate
    except TranslationError:
        raise
    except Exception as error:
        # 入力本文・外部応答はログへ出さない。
        raise TranslationError('Argosモデルの取得・検証・初期化に失敗しました。') from error


def translate_text(text, engine):
    if '\x00' in text:
        raise TranslationError('入力にNULがあります。')
    result = []
    position = 0
    # 行と保護表記を境界にする。日本語を含む区間はそのまま残し、
    # 未翻訳の英語が混在する場合は停止する。
    def prose(part):
        pieces = re.split(r'(\r?\n)', part)
        for piece in pieces:
            if JAPANESE.search(piece) and re.search(r'[A-Za-z]', piece):
                raise TranslationError('同一区間の日英混在を安全に分離できません。手動で日本語化してください。')
            if not re.search(r'[A-Za-z]', piece):
                result.append(piece)
                continue
            match = re.fullmatch(r'(\s*)(.*?)(\s*)', piece)
            leading, source, trailing = match.groups()
            try:
                target = engine(source)
            except Exception as error:
                raise TranslationError('Argosによる翻訳に失敗しました。') from error
            if (not isinstance(target, str) or not target.strip() or '\x00' in target
                    or '\n' in target or not JAPANESE.search(target)):
                raise TranslationError('翻訳結果が空・不正・未翻訳のため停止しました。')
            result.append(leading + target + trailing)
    for match in PROTECTED.finditer(text):
        prose(text[position:match.start()])
        result.append(match[0])
        position = match.end()
    prose(text[position:])
    return ''.join(result)


def translate_payload(original, engine):
    return {'title': translate_text(original['title'], engine),
            'body': translate_text(original['body'], engine),
            'commits': [{'sha': item['sha'], 'message': translate_text(item['message'], engine)}
                        for item in original['commits']]}
