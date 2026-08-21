#!/usr/bin/env python3
"""Translate a Markdown changelog from English to Japanese with Argos Translate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Callable

CACHE_FORMAT = 1
ENGINE = "argos-translate-1.11.0-en-ja"
PROTECTED_RE = re.compile(
    r"(" + chr(96) + r"+[^" + chr(96) + r"]*" + chr(96) + r"+|"
    r"https?://[^\s)>]+)"
)
TRANSLATABLE_RE = re.compile(r"[A-Za-z]{2,}")
FENCE_RE = re.compile(r"^\s*(" + chr(96) * 3 + r"|~~~)")


def load_cache(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if payload.get("format") != CACHE_FORMAT or payload.get("engine") != ENGINE:
        return {}
    translations = payload.get("translations", {})
    return translations if isinstance(translations, dict) else {}


def save_cache(path: Path, translations: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "format": CACHE_FORMAT,
        "engine": ENGINE,
        "translations": dict(sorted(translations.items())),
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def cache_key(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def translate_piece(
    text: str,
    translator: Callable[[str], str],
    cache: dict[str, str],
) -> str:
    if not TRANSLATABLE_RE.search(text):
        return text
    key = cache_key(text)
    if key not in cache:
        translated = translator(text).strip()
        cache[key] = translated if translated else text
    return cache[key]


def translate_line(
    line: str,
    translator: Callable[[str], str],
    cache: dict[str, str],
) -> str:
    if not TRANSLATABLE_RE.search(line):
        return line
    if re.match(r"^\s*\[[^\]]+\]:\s+\S+", line):
        return line

    prefix_match = re.match(
        r"^(\s*(?:#{1,6}\s+|(?:[-*+]|\d+\.)\s+|>+\s*))",
        line,
    )
    prefix = prefix_match.group(1) if prefix_match else ""
    body = line[len(prefix):]
    output: list[str] = [prefix]
    cursor = 0
    for match in PROTECTED_RE.finditer(body):
        output.append(translate_piece(body[cursor:match.start()], translator, cache))
        output.append(match.group(0))
        cursor = match.end()
    output.append(translate_piece(body[cursor:], translator, cache))
    return "".join(output)


def translate_markdown(
    text: str,
    translator: Callable[[str], str],
    cache: dict[str, str],
) -> str:
    output: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append(line)
        elif in_fence:
            output.append(line)
        else:
            output.append(translate_line(line, translator, cache))
    return "\n".join(output).rstrip() + "\n"


def argos_translator() -> Callable[[str], str]:
    import argostranslate.package
    import argostranslate.translate

    installed = argostranslate.translate.get_installed_languages()
    english = next((language for language in installed if language.code == "en"), None)
    japanese = next((language for language in installed if language.code == "ja"), None)
    translation = english.get_translation(japanese) if english and japanese else None

    if translation is None:
        argostranslate.package.update_package_index()
        package = next(
            (
                item
                for item in argostranslate.package.get_available_packages()
                if item.from_code == "en" and item.to_code == "ja"
            ),
            None,
        )
        if package is None:
            raise RuntimeError("Argos English-to-Japanese model is unavailable")
        argostranslate.package.install_from_path(package.download())
        installed = argostranslate.translate.get_installed_languages()
        english = next(language for language in installed if language.code == "en")
        japanese = next(language for language in installed if language.code == "ja")
        translation = english.get_translation(japanese)

    return translation.translate


def update(
    source: Path,
    output: Path,
    cache_path: Path,
    translator: Callable[[str], str] | None = None,
) -> bool:
    source_text = source.read_text(encoding="utf-8-sig")
    cache = load_cache(cache_path)
    translated = translate_markdown(
        source_text,
        translator or argos_translator(),
        cache,
    )
    changed = not output.exists() or output.read_text(encoding="utf-8") != translated
    output.parent.mkdir(parents=True, exist_ok=True)
    if changed:
        output.write_text(translated, encoding="utf-8")
    save_cache(cache_path, cache)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    args = parser.parse_args()
    try:
        changed = update(args.source, args.output, args.cache)
    except (OSError, RuntimeError, UnicodeError) as error:
        parser.error(str(error))
    print(f"Japanese changelog {'updated' if changed else 'unchanged'}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
