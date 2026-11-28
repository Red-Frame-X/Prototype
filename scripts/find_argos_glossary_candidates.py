#!/usr/bin/env python3
"""Commit・PR・Issue・Release Notes等のテキストから用語候補を抽出する。"""
from collections import Counter
import re
import sys

from argos_commit_translation import GLOSSARY, TERMS


CANDIDATE = re.compile(
    r'(?<![A-Za-z0-9_./-])(?:[A-Z][a-z][A-Za-z-]*(?: (?:[A-Z][a-z][A-Za-z-]*|for|of|by|in)){1,5}'
    r'|[A-Z][A-Z0-9]{1,}|[A-Za-z]+(?:[-_][A-Za-z0-9]+)+|[a-z]+[A-Z][A-Za-z0-9]*)(?![A-Za-z0-9_./-])'
)


def candidates(lines):
    """登録済みの用語を除外し、同じ表記を大文字小文字を区別せずに数える。"""
    registered = {term.casefold() for term in (*TERMS, *GLOSSARY)}
    counts = Counter()
    spellings = {}
    for line in lines:
        for match in CANDIDATE.finditer(line):
            term = match[0]
            key = term.casefold()
            if key not in registered and not all(word.casefold() in registered for word in term.split()):
                counts[key] += 1
                spellings.setdefault(key, term)
    return [(spellings[key], count) for key, count in sorted(counts.items(), key=lambda row: (-row[1], row[0]))]


def main():
    for term, count in candidates(sys.stdin):
        print(f'{count}\t{term}')


if __name__ == '__main__':
    main()
