#!/usr/bin/env python3
"""Convert an AdGuard user-filter file to conservative uBO Lite custom filters.

The output is intended for uBO Lite's ``Custom filters`` editor.  uBO Lite does
not support subscribing to an arbitrary remote filter-list URL, so this tool
does not attempt to create a remotely subscribable list.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

DEFAULT_SOURCE = (
    "https://raw.githubusercontent.com/Red-Frame-X/Prototype/refs/heads/main/"
    "AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt"
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
    output: list[str] = []
    excluded: list[dict[str, object]] = []
    for number, raw_line in enumerate(lines, 1):
        result = convert_line(raw_line)
        if result.output is None:
            excluded.append({"line": number, "reason": result.reason, "rule": raw_line.rstrip("\n")})
        else:
            output.append(result.output)
    return output, excluded


def read_source(source: str) -> str:
    if source.startswith(("https://", "http://")):
        request = urllib.request.Request(source, headers={"User-Agent": "Prototype-uBOL-converter/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8-sig")
    return Path(source).read_text(encoding="utf-8-sig")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_dist = Path(__file__).resolve().parent / "dist"
    parser.add_argument("--input", default=DEFAULT_SOURCE, help="input file or HTTP(S) URL")
    parser.add_argument("--output", default=str(default_dist / "AdGuard_Custom_Rules_uBOL.txt"))
    parser.add_argument("--report", default=str(default_dist / "AdGuard_Custom_Rules_uBOL.report.json"))
    args = parser.parse_args(argv)

    try:
        source_text = read_source(args.input)
        rules, excluded = convert(source_text.splitlines())
    except (OSError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    header = [
        "! Title: AdGuard Custom Rules - Red Frame X (uBO Lite Custom Filters)",
        "! Generated by: scripts/convert_adguard_to_ubol.py",
        f"! Generated: {generated}",
        f"! Source: {args.input}",
        "! Usage: Paste into uBO Lite > Options > Custom filters.",
        "! Note: uBO Lite cannot subscribe to arbitrary custom filter-list URLs.",
        "",
    ]
    output_path = Path(args.output)
    report_path = Path(args.report)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(header + rules) + "\n", encoding="utf-8")

    reason_counts = Counter(str(item["reason"]) for item in excluded)
    report = {
        "source": args.input,
        "generated": generated,
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
