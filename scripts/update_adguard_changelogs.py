#!/usr/bin/env python3
"""Mirror official AdGuard changelogs and flag converter-relevant changes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BROWSER_CHANGELOG_URL = "https://raw.githubusercontent.com/AdguardTeam/AdguardBrowserExtension/refs/heads/master/CHANGELOG.md"
ANDROID_RELEASES_URL = "https://api.github.com/repos/AdguardTeam/AdguardForAndroid/releases?per_page=100"
VERSION_RE = re.compile(
    r"(?im)^#{2,4}\s+(?:AdGuard(?: for Android)?\s+)?\[?v?"
    r"(\d+(?:\.\d+)+)\]?(?=\s|$)"
)
IMPACT_RE = re.compile(r"(?i)\b(?:filtering engine|corelibs|scriptlets?|extended css|cosmetic|modifier|filtering rules?|declarative net request|dnr|manifest v3|mv3|html filtering|redirect|removeparam|csp|regex|regular expression)\b")


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "Prototype-AdGuard-changelog-updater/1.0", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def android_releases_to_markdown(payload: bytes) -> bytes:
    releases = json.loads(payload.decode("utf-8"))
    if not isinstance(releases, list) or not releases:
        raise ValueError("Android releases response is empty or invalid")
    lines = ["# AdGuard for Android changelog mirror", "", f"> Source: {ANDROID_RELEASES_URL}", "> Generated from official GitHub Releases; newest release first.", ""]
    for release in releases:
        name = release.get("name") or release.get("tag_name")
        if not name:
            continue
        lines.extend([f"## {name}", "", f"- Published: {release.get('published_at') or 'unknown'}", f"- Release: {release.get('html_url') or ''}", "", (release.get("body") or "_No release notes provided._").strip(), ""])
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def relevant_lines(text: str) -> list[str]:
    items: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if IMPACT_RE.search(line) and line not in items:
            items.append(line)
    return items[:200]


def latest_version(text: str) -> str:
    match = VERSION_RE.search(text)
    if not match:
        raise ValueError("No version heading found")
    return match.group(1)


def metadata(name: str, source: str, content: bytes, checked_at: str) -> dict[str, Any]:
    text = content.decode("utf-8-sig")
    return {"product": name, "source": source, "latest_version": latest_version(text), "sha256": hashlib.sha256(content).hexdigest(), "checked_at": checked_at, "converter_relevant_entries": relevant_lines(text), "automatic_code_changes": False, "review_policy": "Release-note prose is evidence, not an executable specification. Verify official filtering-engine documentation or source code, then update capability profiles and regression tests."}


def write_if_changed(path: Path, content: bytes) -> bool:
    if path.exists() and path.read_bytes() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return True


def build_review(items: list[dict[str, Any]]) -> bytes:
    lines = ["# AdGuard converter compatibility review", "", "This file is generated. Changelog matches are review candidates, not proof that a rule syntax is supported.", ""]
    for item in items:
        lines.extend([f"## {item['product']} {item['latest_version']}", ""])
        entries = item["converter_relevant_entries"]
        lines.extend((f"- {entry}" for entry in entries) if entries else ["- No converter-relevant keywords detected."])
        lines.append("")
    lines.extend(["## Required verification before converter changes", "", "1. Confirm behavior in official AdGuard filtering documentation, CoreLibs/Scriptlets source, or a linked upstream issue.", "2. Add positive, negative, and false-positive regression tests.", "3. Update `config/adguard-converter-capabilities.json` in a reviewed pull request.", "4. Rebuild generated filters and run AGLint plus unit tests.", ""])
    return "\n".join(lines).encode("utf-8")


def update(output_dir: Path, browser_source: str, android_source: str, now: datetime | None = None) -> bool:
    browser = fetch(browser_source)
    android = android_releases_to_markdown(fetch(android_source))
    checked_at = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    products = [metadata("AdGuard Browser Extension", browser_source, browser, checked_at), metadata("AdGuard for Android", android_source, android, checked_at)]
    changed = write_if_changed(output_dir / "adguard-browser-extension-CHANGELOG.md", browser)
    changed |= write_if_changed(output_dir / "adguard-for-android-CHANGELOG.md", android)
    metadata_path = output_dir / "metadata.json"
    old: dict[str, Any] = {}
    if metadata_path.exists():
        try:
            old = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    old_by_product = {p.get("product"): p for p in old.get("products", [])}
    for product in products:
        previous = old_by_product.get(product["product"], {})
        if previous.get("sha256") == product["sha256"]:
            product["checked_at"] = previous.get("checked_at", checked_at)
    data = (json.dumps({"products": products}, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    changed |= write_if_changed(metadata_path, data)
    changed |= write_if_changed(output_dir / "converter-review.md", build_review(products))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser-source", default=BROWSER_CHANGELOG_URL)
    parser.add_argument("--android-source", default=ANDROID_RELEASES_URL)
    parser.add_argument("--output-dir", type=Path, default=Path("upstream/adguard"))
    args = parser.parse_args()
    try:
        changed = update(args.output_dir, args.browser_source, args.android_source)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print("AdGuard changelog mirror updated." if changed else "No upstream changes detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
