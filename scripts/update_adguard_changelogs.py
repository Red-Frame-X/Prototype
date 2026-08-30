#!/usr/bin/env python3
"""Mirror official AdGuard changelogs and flag converter-relevant changes."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.request
from urllib.error import HTTPError, URLError
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BROWSER_CHANGELOG_URL = "https://raw.githubusercontent.com/AdguardTeam/AdguardBrowserExtension/refs/heads/master/CHANGELOG.md"
BROWSER_RELEASES_URL = "https://api.github.com/repos/AdguardTeam/AdguardBrowserExtension/releases?per_page=100"
ANDROID_RELEASES_URL = "https://api.github.com/repos/AdguardTeam/AdguardForAndroid/releases?per_page=100"
VERSION_RE = re.compile(
    r"(?im)^#{2,4}\s+(?:AdGuard(?: for Android)?\s+)?\[?v?"
    r"(\d+(?:\.\d+)+)\]?(?=\s|$)"
)
TAG_VERSION_RE = re.compile(r"v?(\d+(?:\.\d+)+)")
IMPACT_RE = re.compile(r"(?i)\b(?:filtering engine|corelibs|scriptlets?|extended css|cosmetic|modifier|filtering rules?|declarative net request|dnr|manifest v3|mv3|html filtering|redirect|removeparam|csp|regex|regular expression)\b")


def fetch(url: str, attempts: int = 4) -> bytes:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Prototype-AdGuard-changelog-updater/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            if error.code in {400, 401, 404, 422} or attempt == attempts:
                raise
        except (URLError, TimeoutError):
            if attempt == attempts:
                raise
        time.sleep(min(2 ** (attempt - 1), 8))
    raise RuntimeError("unreachable")


def parse_releases(payload: bytes, product: str) -> list[dict[str, Any]]:
    releases = json.loads(payload.decode("utf-8"))
    if not isinstance(releases, list) or not releases:
        raise ValueError(f"{product} releases response is empty or invalid")
    return releases


def latest_stable_release(payload: bytes, product: str) -> dict[str, Any]:
    for release in parse_releases(payload, product):
        if release.get("draft") or release.get("prerelease"):
            continue
        label = str(release.get("tag_name") or release.get("name") or "")
        match = TAG_VERSION_RE.search(label)
        if not match:
            continue
        return {
            "version": match.group(1),
            "published_at": release.get("published_at"),
            "release_url": release.get("html_url"),
            "tag_name": release.get("tag_name"),
        }
    raise ValueError(f"No stable {product} GitHub Release found")


def android_releases_to_markdown(payload: bytes) -> bytes:
    releases = parse_releases(payload, "Android")
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


def metadata(
    name: str,
    source: str,
    content: bytes,
    checked_at: str,
    *,
    version: str | None = None,
    release: dict[str, Any] | None = None,
    digest_extra: bytes = b"",
) -> dict[str, Any]:
    text = content.decode("utf-8-sig")
    digest = hashlib.sha256(content + b"\0" + digest_extra).hexdigest()
    result: dict[str, Any] = {
        "product": name,
        "source": source,
        "latest_version": version or latest_version(text),
        "sha256": digest,
        "checked_at": checked_at,
        "converter_relevant_entries": relevant_lines(text),
        "automatic_code_changes": False,
        "review_policy": "Release-note prose is evidence, not an executable specification. Verify official filtering-engine documentation or source code, then update capability profiles and regression tests.",
    }
    if release:
        result.update({
            "release_url": release.get("release_url"),
            "published_at": release.get("published_at"),
        })
    return result


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


def update(
    output_dir: Path,
    browser_source: str,
    android_source: str,
    now: datetime | None = None,
    changelog_dir: Path | None = None,
    browser_releases_source: str = BROWSER_RELEASES_URL,
) -> bool:
    changelog_dir = changelog_dir or output_dir
    browser = fetch(browser_source)
    browser_releases = fetch(browser_releases_source)
    browser_release = latest_stable_release(browser_releases, "Browser Extension")
    android_payload = fetch(android_source)
    android = android_releases_to_markdown(android_payload)
    checked_at = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    products = [
        metadata(
            "AdGuard Browser Extension",
            browser_releases_source,
            browser,
            checked_at,
            version=browser_release["version"],
            release=browser_release,
            digest_extra=browser_releases,
        ),
        metadata("AdGuard for Android", android_source, android, checked_at),
    ]
    changed = write_if_changed(changelog_dir / "adguard-browser-extension-CHANGELOG.source.md", browser)
    changed |= write_if_changed(changelog_dir / "adguard-for-android-CHANGELOG.source.md", android)
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
    parser.add_argument("--browser-releases-source", default=BROWSER_RELEASES_URL)
    parser.add_argument("--android-source", default=ANDROID_RELEASES_URL)
    parser.add_argument("--output-dir", type=Path, default=Path("upstream/adguard"))
    parser.add_argument("--changelog-dir", type=Path, default=Path("AdGuard Custom Rules/ChangeLog"))
    args = parser.parse_args()
    try:
        changed = update(
            args.output_dir,
            args.browser_source,
            args.android_source,
            changelog_dir=args.changelog_dir,
            browser_releases_source=args.browser_releases_source,
        )
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print("AdGuard changelog mirror updated." if changed else "No upstream changes detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
