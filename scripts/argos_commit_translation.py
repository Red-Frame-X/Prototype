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
    'Prototype', 'Red-Frame-X', 'Python', 'JavaScript', 'TypeScript', 'Node.js',
    'Linux', 'Windows', 'macOS', 'Docker', 'React', 'OpenAI',
)
HASH_REFERENCE = re.compile(r'(?<![A-Za-z0-9_])[0-9a-fA-F]{7,40}(?![A-Za-z0-9_])')
PROTECTED = re.compile(
    HASH_REFERENCE.pattern + r'|https?://[^\s<>]+|'
    r'(?<!\w)(?:[\w.-]+/[\w.-]+)?#\d+\b|'
    + '|'.join(re.escape(term) + r'(?![A-Za-z0-9_./-])' for term in TERMS)
    + r'|\b(?:[A-Za-z0-9_.-]+(?:/|\.)[A-Za-z0-9_./-]+|v?\d+(?:\.\d+)+(?:[-+][\w.-]+)?|[A-Z][A-Z0-9_]+|'
      r'\w*[a-z][A-Z]\w*|\w+_\w+|[\w.-]+(?:/|\.)[\w./-]+)\b'
)
# 未登録の固有名詞も保守的に保持する。一般説明の先頭に多い語は翻訳する。
PROSE_WORDS = (
    'Update|Fix|Add|Remove|Delete|Rename|Refactor|Improve|Correct|Create|Change|'
    'Ensure|Preserve|Keep|Prevent|Allow|Use|Support|Handle|Check|Validate|Document|'
    'Configure|Enable|Disable|Bump|Pin|Migrate|Replace|Restore|Revert|Merge|Build|'
    'Sync|See|Do|This|The|A|An|In|For|To|With|Without|When|If|It|Please|Note'
)
# Commitで一般的な動詞は活用形も一般説明として扱う。
verb_forms = set(PROSE_WORDS.split('|'))
for verb in ('Update Fix Add Remove Delete Rename Refactor Improve Correct Create Change '
             'Ensure Preserve Prevent Allow Use Support Handle Check Validate Test Document '
             'Configure Enable Disable Bump Migrate Replace Restore Revert Merge Sync').split():
    verb_forms.update((verb + ('d' if verb.endswith('e') else 'ed'),
                       verb + ('es' if verb.endswith('x') else 's'),
                       (verb[:-1] if verb.endswith('e') else verb) + 'ing'))
verb_forms.update(('Kept', 'Keeping', 'Built', 'Building', 'Pinned', 'Pinning',
                   'Did', 'Done', 'Doing', 'Saw', 'Seen', 'Seeing'))
PROSE_WORDS = '|'.join(sorted(verb_forms, key=lambda word: (-len(word), word)))
PROTECTED = re.compile(PROTECTED.pattern + r'|\b(?!(?:' + PROSE_WORDS
                       + r')\b)[A-Z][a-z]+\b')


def load_engine():
    """既定Branchの固定情報だけから取得し、hashとMetadataを確認する。"""
    manifest = json.loads((ROOT / '.github/argos-model.json').read_text())
    digest = manifest.get('sha256')
    if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
        raise TranslationError('英日モデルのSHA256が未確認です。取得・実物確認後に固定してください。')
    if manifest.get('license_verified') is not True:
        raise TranslationError('英日モデル個別のライセンス確認が未完了です。')
    try:
        import argostranslate.package as package
        import argostranslate.translate as translate
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'model.argosmodel'
            # 認証情報も翻訳対象本文も送信しない。配布先は固定する。
            with urllib.request.urlopen(
                    urllib.request.Request(
                        'https://argos-net.com/v1/translate-en_ja-1_1.argosmodel',
                        headers={'User-Agent': 'ArgosTranslate/1.11.0'}), timeout=90) as response:
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
        configure_offline_engine(engine, installed[0])
        return engine.translate
    except TranslationError:
        raise
    except Exception as error:
        # 入力本文・外部応答はログへ出さない。
        raise TranslationError('Argosモデルの取得・検証・初期化に失敗しました。') from error


class RuleSentencizer:
    """学習済みモデルや外部通信を使わない英語の文分割。"""
    def __init__(self):
        import spacy
        self.nlp = spacy.blank('en')
        self.nlp.add_pipe('sentencizer')

    def split_sentences(self, text):
        return [sentence.text for sentence in self.nlp(text).sents]


def configure_offline_engine(engine, installed):
    """旧Stanzaモデルの代わりにspaCyのルールだけで文を区切る。"""
    from argostranslate.translate import PackageTranslation
    backend = engine.underlying
    if not isinstance(backend, PackageTranslation) or backend.pkg.package_path != installed.package_path:
        raise TranslationError('固定モデルの翻訳経路が変わったため停止しました。')
    # Argos 1.11.0のISentenceBoundaryDetectionModelに合わせる。
    # 古いStanzaの重みの書き換えや、別モデルの暗黙の取得を行わない。
    backend.sentencizer = RuleSentencizer()


# 翻訳器に本文の文脈を渡し、保護表記は衝突しない識別子で置き換える。
MARKER = re.compile(r'ZXQ[0-9]+QXZ')
TOKENS = re.compile(PROTECTED.pattern + r'|[ぁ-んァ-ヶ一-龠々ー][ぁ-んァ-ヶ一-龠々ー。、！？「」『』…]*')


def markdown_segments(text):
    """CommonMarkが判定したコードブロックとCode spanを原文で保持する。"""
    from markdown_it import MarkdownIt
    lines = re.findall(r'[^\r\n]*(?:\r\n|\r|\n|$)', text)
    if lines and not lines[-1]:
        lines.pop()
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    ranges = []
    for token in MarkdownIt('commonmark').parse(text):
        if token.type not in {'fence', 'code_block'}:
            continue
        start, end = token.map
        if token.type == 'fence':
            # CommonMarkは未完結フェンスをEOFで閉じるが、自動翻訳では停止する。
            closing = r'^[ \t>]*' + re.escape(token.markup[0]) + r'{' + str(len(token.markup)) + r',}[ \t]*(?:\r?\n|\r)?$'
            if end - start < 2 or not re.fullmatch(closing, lines[end - 1]):
                raise TranslationError('コードブロックが完結していません。')
        ranges.append((offsets[start], offsets[end]))

    def inline_segments(value):
        position = plain_start = 0
        backticks = re.compile(r'`+')
        while position < len(value):
            if value[position] != '`':
                position += 1
                continue
            delimiter = backticks.match(value, position)[0]
            closing = re.compile(r'(?<!`)' + re.escape(delimiter) + r'(?!`)')
            match = closing.search(value, position + len(delimiter))
            if match is None:
                raise TranslationError('Code spanが完結していません。')
            if plain_start < position:
                yield False, value[plain_start:position]
            yield True, value[position:match.end()]
            position = plain_start = match.end()
        if plain_start < len(value):
            yield False, value[plain_start:]

    position = 0
    for start, end in sorted(ranges):
        yield from inline_segments(text[position:start])
        # 改行は保護識別子の外へ残し、後続の本文と同じ行にしない。
        raw = text[start:end]
        suffix = re.search(r'(\r\n|\r|\n)$', raw)
        if suffix:
            yield True, raw[:suffix.start()]
            yield False, suffix[0]
        else:
            yield True, raw
        position = end
    yield from inline_segments(text[position:])


def translate_text(text, engine):
    if '\x00' in text or MARKER.search(text):
        raise TranslationError('入力にNULまたは予約した保護識別子があります。')
    tokens = {}
    def protect(match):
        marker = f'ZXQ{len(tokens):04d}QXZ'
        tokens[marker] = match[0]
        return marker
    masked = ''.join(protect((value,)) if code else TOKENS.sub(protect, value)
                     for code, value in markdown_segments(text))
    result = []
    for line in masked.splitlines(keepends=True):
        # Markdownの行構造と公式原文の引用はそのまま残す。
        match = re.fullmatch(r'(\s*(?:(?:[a-z]+(?:\([^()\n]+\))?!?:[ \t]*)|(?:#{1,6}|[-*+]|[0-9]+[.)]|>) +(?:\[[ xX]\][ \t]+)?)?)(.*?)(\s*)', line)
        if match is None:
            raise TranslationError('本文の行構造を解釈できません。')
        leading, source, trailing = match.groups()
        if leading.lstrip().startswith('>') or not re.search(r'[A-Za-z]', MARKER.sub('', source)):
            result.append(line)
            continue
        try:
            target = engine(source)
        except Exception as error:
            raise TranslationError('Argosによる翻訳に失敗しました。') from error
        if (not isinstance(target, str) or not target.strip() or '\x00' in target
                or '\n' in target or '\r' in target or not JAPANESE.search(target)):
            raise TranslationError('翻訳結果が空・不正・未翻訳のため停止しました。')
        if sorted(MARKER.findall(source)) != sorted(MARKER.findall(target)):
            raise TranslationError('翻訳結果で保護表記が欠落・重複・変更されました。')
        # 英日モデルがCommitの命令形Fixだけを英語で残す場合の固定表現。
        # 残りの句の訳と保護識別子は保持し、動作を日本語で明示する。
        if source.startswith('Fix ') and target.startswith('Fix '):
            target = target[4:].rstrip('。') + 'を修正'
        if re.search(r'[A-Za-z]', MARKER.sub('', target)):
            raise TranslationError('一般説明に未翻訳の英語が残っています。')
        result.append(leading + target + trailing)
    translated = ''.join(result)
    return MARKER.sub(lambda match: tokens[match[0]], translated)


def translate_payload(original, engine):
    return {'title': translate_text(original['title'], engine),
            'body': translate_text(original['body'], engine),
            'commits': [{'sha': item['sha'], 'message': translate_text(item['message'], engine)}
                        for item in original['commits']]}
