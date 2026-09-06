#!/usr/bin/env python3
"""Convert an AdGuard user-filter file to a conservative uBO Lite filter list.

The output can be subscribed to by URL through uBO Lite's ``Filter lists``
pane (uBO Lite 2026.621.1813 or newer), or imported manually.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

FILTER_TITLE = "uBOL Filter - Red Frame X"
FILTER_BASENAME = "uBOL Filter - Red Frame X"

CANONICAL_SOURCE = (
    "https://raw.githubusercontent.com/Red-Frame-X/Prototype/refs/heads/main/"
    "AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt"
)
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = str(
    REPOSITORY_ROOT
    / "AdGuard Custom Rules"
    / "AdGuard Custom Rules - Red Frame X.txt"
)

# Features with no safe uBOL equivalent in this converter. When semantics cannot
# be preserved, exclusion is preferred to silently widening or changing scope.
UNSUPPORTED_MODIFIERS = {
    "app", "cname", "content", "csp", "hls", "jsonprune", "permissions",
    "redirect", "redirect-rule", "removeheader", "replace", "urltransform",
}
MODIFIER_ALIASES = {"xhr": "xmlhttprequest", "3p": "third-party", "1p": "first-party"}


@dataclass(frozen=True)
class Result:
    output: str | None
    status: str
    reason: str = ""


def _modifier_name(token: str) -> str:
    token = token.lstrip("~")
    return token.split("=", 1)[0].lower()


def _regex_closing_slash_index(line: str) -> int | None:
    """Return the closing delimiter for a network regex rule, if present."""
    start = 2 if line.startswith("@@") else 0
    if start >= len(line) or line[start] != "/":
        return None

    in_character_class = False
    for index in range(start + 1, len(line)):
        backslashes = 0
        previous = index - 1
        while previous >= start and line[previous] == "\\":
            backslashes += 1
            previous -= 1
        is_escaped = backslashes % 2 == 1

        char = line[index]
        if char == "[" and not is_escaped:
            in_character_class = True
            continue
        if char == "]" and not is_escaped and in_character_class:
            in_character_class = False
            continue
        if char == "/" and not is_escaped and not in_character_class:
            return index

    return None


def _contains_unsupported_backreference(pattern: str) -> bool:
    """Return whether a regex contains an unescaped RE2-incompatible backreference."""
    index = 0
    while index < len(pattern):
        if pattern[index] != "\\":
            index += 1
            continue

        run_end = index
        while run_end < len(pattern) and pattern[run_end] == "\\":
            run_end += 1

        if (run_end - index) % 2 == 1 and run_end < len(pattern):
            token_start = pattern[run_end]
            if token_start in "123456789gk":
                return True

        index = run_end
    return False


def _split_modifiers(line: str) -> tuple[str, list[str]] | None:
    """Split modifiers without treating ``$`` inside a regex as a separator."""
    closing_slash = _regex_closing_slash_index(line)
    if closing_slash is not None:
        suffix = line[closing_slash + 1:]
        if not suffix.startswith("$"):
            return None
        pattern = line[:closing_slash + 1]
        raw = suffix[1:]
    else:
        if "$" not in line:
            return None
        pattern, raw = line.rsplit("$", 1)
    return pattern, [part.strip() for part in raw.split(",") if part.strip()]


def convert_line(raw_line: str) -> Result:
    line = raw_line.strip()
    if not line:
        return Result("", "preserved")
    if line.startswith("!") or line.startswith("["):
        return Result(line, "preserved")

    if "$$" in line or "#@$#" in line:
        return Result(None, "excluded", "html-filtering")
    if "#%#" in line or "#@%#" in line or "##+js(" in line or "#@#+js(" in line:
        return Result(None, "excluded", "scriptlet")

    cosmetic_match = re.match(r"^(.*?)(#\?#|#\?@#|##|#@#)(.*)$", line)
    if cosmetic_match:
        domains, separator, selector = cosmetic_match.groups()
        # Direct semantic equivalents documented by uBO/uBOL syntax.
        selector = selector.replace(":contains(", ":has-text(")
        selector = selector.replace(":nth-ancestor(", ":upward(")
        selector = selector.replace(":matches-property(", ":matches-prop(")
        # uBO/uBOL supports :remove() as an action operator, so preserve it.
        if separator == "#?#":
            separator = "##"
        elif separator == "#?@#":
            separator = "#@#"
        output = f"{domains}{separator}{selector}"
        return Result(output, "converted" if output != line else "preserved")

    regex_start = 2 if line.startswith("@@") else 0
    closing_slash = _regex_closing_slash_index(line)
    if closing_slash is not None:
        regex_pattern = line[regex_start + 1:closing_slash]
        if (
            "(?=" in regex_pattern
            or "(?!" in regex_pattern
            or "(?<=" in regex_pattern
            or "(?<!" in regex_pattern
            or _contains_unsupported_backreference(regex_pattern)
        ):
            return Result(None, "excluded", "non-re2-regex")

    modifiers = _split_modifiers(line)
    if modifiers:
        pattern, tokens = modifiers
        names = {_modifier_name(token) for token in tokens}
        unsupported = sorted(names & UNSUPPORTED_MODIFIERS)
        if unsupported:
            return Result(None, "excluded", "modifier:" + ",".join(unsupported))

        converted_tokens: list[str] = []
        for token in tokens:
            negated = token.startswith("~")
            body = token[1:] if negated else token
            name, equals, value = body.partition("=")
            mapped = MODIFIER_ALIASES.get(name.lower(), name)
            converted_tokens.append(("~" if negated else "") + mapped + equals + value)
        output = pattern + "$" + ",".join(converted_tokens)
        return Result(output, "converted" if output != line else "preserved")

    return Result(line, "preserved")


def convert(lines: Iterable[str]) -> tuple[list[str], list[dict[str, object]]]:
    """Convert rules while removing comments orphaned by excluded rules."""
    output: list[str] = []
    excluded: list[dict[str, object]] = []
    block: list[tuple[int, str]] = []

    def flush_block() -> None:
        if not block:
            return

        domain_heading: str | None = None
        pending_comments: list[str] = []
        emitted: list[str] = []
        has_rule = False

        for index, (number, raw_line) in enumerate(block):
            line = raw_line.strip()
            if line.startswith("!") or line.startswith("["):
                if index == 0 and re.fullmatch(
                    r"!\s+[A-Za-z0-9.*_-]+(?:,[A-Za-z0-9.*_-]+)*",
                    line,
                ):
                    domain_heading = line
                else:
                    pending_comments.append(line)
                continue

            has_rule = True
            result = convert_line(raw_line)
            if result.output is None:
                excluded.append({"line": number, "reason": result.reason, "rule": raw_line.rstrip("\n")})
                pending_comments.clear()
                continue

            emitted.extend(pending_comments)
            pending_comments.clear()
            emitted.append(result.output)

        if emitted:
            if domain_heading:
                emitted.insert(0, domain_heading)
            output.extend(emitted)
        elif not has_rule:
            output.extend(comment for _, comment in block)

        block.clear()

    for number, raw_line in enumerate(lines, 1):
        if raw_line.strip():
            block.append((number, raw_line))
        else:
            flush_block()
            if output and output[-1] != "":
                output.append("")
    flush_block()

    while output and output[-1] == "":
        output.pop()
    return output, excluded


def read_source(source: str) -> str:
    if source.startswith(("https://", "http://")):
        request = urllib.request.Request(source, headers={"User-Agent": "Prototype-uBOL-converter/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8-sig")
    return Path(source).read_text(encoding="utf-8-sig")


def extract_source_version(source_text: str) -> str:
    match = re.search(r"^! Version:\s*(\S.*)$", source_text, flags=re.MULTILINE)
    if not match:
        raise ValueError("source filter is missing ! Version metadata")
    return match.group(1).strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_dist = Path(__file__).resolve().parent / "dist"
    parser.add_argument("--input", default=DEFAULT_SOURCE, help="input file or HTTP(S) URL")
    parser.add_argument("--output", default=str(default_dist / f"{FILTER_BASENAME}.txt"))
    parser.add_argument("--report", default=str(default_dist / f"{FILTER_BASENAME}.report.json"))
    args = parser.parse_args(argv)

    try:
        source_text = read_source(args.input)
        source_version = extract_source_version(source_text)
        rules, excluded = convert(source_text.splitlines())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    header = [
        f"! Title: {FILTER_TITLE}",
        "! Description: Customize uBOL filters for personal use.",
        f"! Version: {source_version}",
        "! Syntax: uBOL",
        "! Expires: 1 day",
        "! Homepage: https://github.com/Red-Frame-X/Prototype",
        "! License: CC0-1.0",
        "! Note: Combination of Japan’s community-driven rules and my own rules.",
        "",
    ]
    source_metadata = re.compile(
        r"^! (?:Title|Description|Version|Syntax|Expires|Homepage|License|Note):"
    )
    rules = [line for line in rules if not source_metadata.match(line)]
    while rules and rules[0] == "":
        rules.pop(0)
    output_path = Path(args.output)
    report_path = Path(args.report)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(header + rules) + "\n", encoding="utf-8")

    reason_counts = Counter(str(item["reason"]) for item in excluded)
    input_path = Path(args.input)
    try:
        is_repository_source = input_path.resolve() == Path(DEFAULT_SOURCE).resolve()
    except OSError:
        is_repository_source = False
    report = {
        "source": CANONICAL_SOURCE if is_repository_source else args.input,
        "input_lines": len(source_text.splitlines()),
        "output_lines_excluding_generated_header": len(rules),
        "excluded_count": len(excluded),
        "excluded_by_reason": dict(sorted(reason_counts.items())),
        "excluded": excluded,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_path} ({len(rules)} lines); excluded {len(excluded)} rules")
    print(f"wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
