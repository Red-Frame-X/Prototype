#!/usr/bin/env python3
"""公式uBO Lite CHANGELOGを取得し、再現可能なメタデータを更新する。"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.request
from urllib.parse import urlsplit
from urllib.error import HTTPError, URLError
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
        headers = {"User-Agent": "Prototype-uBOL-changelog-updater/1.0"}
        token = os.environ.get("GITHUB_TOKEN")
        request = urllib.request.Request(source, headers=headers)
        parsed = urlsplit(request.full_url)
        if token and parsed.scheme == "https" and parsed.netloc == "api.github.com":
            # リダイレクト先には、同一ホストであっても認証情報を引き継がない。
            request.add_unredirected_header("Authorization", f"Bearer {token}")
        attempts = 4
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


def update(
    source: str,
    output: Path,
    now: datetime | None = None,
    source_output: Path | None = None,
) -> bool:
    changelog = read_source(source)
    digest = hashlib.sha256(changelog).hexdigest()
    # 保存済みファイルを書き換える前に、取得内容を検証する。
    timestamp = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    metadata = build_metadata(changelog, source, timestamp)
    source_changed = False
    if source_output is not None:
        source_output.parent.mkdir(parents=True, exist_ok=True)
        source_changed = (
            not source_output.exists() or source_output.read_bytes() != changelog
        )
        if source_changed:
            source_output.write_bytes(changelog)

    if output.exists():
        try:
            current = json.loads(output.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            current = {}
        if current.get("changelog_sha256") == digest:
            print("No upstream changelog changes detected.")
            return source_changed

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
    parser.add_argument(
        "--source-output",
        type=Path,
        default=base_dir / "upstream" / "ubol-CHANGELOG.source.md",
    )
    args = parser.parse_args()
    try:
        update(args.source, args.output, source_output=args.source_output)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
