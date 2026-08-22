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

# AdGuard-only or non-declarative features which cannot be translated without
# changing behaviour.  False positives are worse than losing one cosmetic rule.
UNSUPPORTED_COSMETIC_TOKENS = (
    ":contains(", ":has-text(", ":upward(", ":nth-ancestor(", ":xpath(",
    ":matches-attr(", ":matches-css(", ":matches-css-after(",
    ":matches-css-before(", ":matches-property(", ":remove()", ":style(",
)
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


def _split_modifiers(line: str) -> tuple[str, list[str]] | None:
    """Split the last modifier section; regex filters are rejected separately."""
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
        if any(token in selector for token in UNSUPPORTED_COSMETIC_TOKENS):
            return Result(None, "excluded", "procedural-or-style-cosmetic")
        if separator == "#?#":
            separator = "##"
        elif separator == "#?@#":
            separator = "#@#"
        output = f"{domains}{separator}{selector}"
        return Result(output, "converted" if output != line else "preserved")

    # AdGuard application scoping has no browser-extension equivalent.
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

    # RE2 validity is decided by uBO Lite's own compiler.  Reject lookbehind and
    # backreferences here because Chrome declarativeNetRequest cannot express them.
    regex_body = line[2:] if line.startswith("@@") else line
    if regex_body.startswith("/"):
        if "(?<=" in regex_body or "(?<!" in regex_body or re.search(r"(?<!\\)\\[1-9]", regex_body):
            return Result(None, "excluded", "non-re2-regex")

    return Result(line, "preserved")


def convert(lines: Iterable[str]) -> tuple[list[str], list[dict[str, object]]]:
    """Convert rules while removing comments orphaned by excluded rules.

    Source files group each site with a ``! domain`` heading and place a
    descriptive comment immediately before each rule.  Keeping those comments
    after their rule is excluded makes the generated list misleading, so a
    block is emitted only for rules that survive conversion.
    """
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
            # Preserve standalone section notes; generated metadata is supplied
            # by ``main`` and is filtered there to avoid a duplicate header.
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
    """Return the canonical Version value from the AdGuard source metadata."""
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

    # Subscription metadata only.  Operational notes live in README.md so the
    # downloaded filter stays compact and stable between builds.
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
