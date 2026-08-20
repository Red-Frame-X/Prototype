#!/usr/bin/env python3
"""Fetch the official uBO Lite changelog and update deterministic metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CHANGELOG_URL = (
    "https://raw.githubusercontent.com/uBlockOrigin/uBOL-home/refs/heads/main/"
    "CHANGELOG.md"
)
REMOTE_SUBSCRIPTION_SINCE = "2026.621.1813"
REMOTE_SUBSCRIPTION_COMMIT = (
    "https://github.com/gorhill/uBlock/commit/"
    "06deb19dfa85c13e48ad44d2e6dc4f64a96d6cbc"
)
VERSION_RE = re.compile(r"^### (\d{4}\.\d+\.\d+)\s*$", re.MULTILINE)


def read_source(source: str) -> bytes:
    if source.startswith(("https://", "http://")):
        request = urllib.request.Request(
            source,
            headers={"User-Agent": "Prototype-uBOL-changelog-updater/1.0"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    return Path(source).read_bytes()


def build_metadata(changelog: bytes, source: str, checked_at: str) -> dict[str, object]:
    text = changelog.decode("utf-8-sig")
    versions = VERSION_RE.findall(text)
    if not versions:
        raise ValueError("No uBO Lite version headings found in changelog")
    if REMOTE_SUBSCRIPTION_SINCE not in versions:
        raise ValueError(
            f"Expected feature version {REMOTE_SUBSCRIPTION_SINCE} is missing"
        )
    return {
        "source": source,
        "latest_version": versions[0],
        "changelog_sha256": hashlib.sha256(changelog).hexdigest(),
        "checked_at": checked_at,
        "tracked_features": {
            "remote_filter_list_subscriptions": {
                "supported_since": REMOTE_SUBSCRIPTION_SINCE,
                "implementation": REMOTE_SUBSCRIPTION_COMMIT,
                "safari_supported": False,
            }
        },
    }


def update(source: str, output: Path, now: datetime | None = None) -> bool:
    changelog = read_source(source)
    digest = hashlib.sha256(changelog).hexdigest()
    if output.exists():
        try:
            current = json.loads(output.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            current = {}
        if current.get("changelog_sha256") == digest:
            print("No upstream changelog changes detected.")
            return False

    timestamp = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    metadata = build_metadata(changelog, source, timestamp)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated {output} to uBO Lite {metadata['latest_version']}.")
    return True


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=CHANGELOG_URL)
    parser.add_argument(
        "--output",
        type=Path,
        default=base_dir / "upstream" / "ubol-changelog.json",
    )
    args = parser.parse_args()
    try:
        update(args.source, args.output)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
