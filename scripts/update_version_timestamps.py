#!/usr/bin/env python3
"""Update Version metadata in changed repository content using current JST time."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

JST = ZoneInfo("Asia/Tokyo")
HEADER_TEMPLATE = Path("Markdown Notes/Header Template.md")
STATE_FILE = Path(".github/version-timestamps-state.json")
TARGET_PREFIXES = (
    "AdGuard Custom Rules/",
    "Markdown Notes/",
    "NG Word Regex for ChMate/",
    "UserScript/",
)

PATTERNS = (
    (re.compile(r"(?m)^! Version:[ \t]*\d{8,14}$"), lambda stamp: f"! Version: {stamp}"),
    (re.compile(r"(?m)^\| \*\*Version\*\* \| \d{8,14} \|$"), lambda stamp: f"| **Version** | {stamp} |"),
    (re.compile(r"(?m)^(//[ \t]*@version[ \t]+)\S+[ \t]*$"), lambda stamp: rf"\g<1>{stamp}"),
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, encoding="utf-8")


def changed_files(base: str, head: str) -> list[Path]:
    output = git("diff", "--name-only", "-z", base, head)
    return [Path(line) for line in output.split("\0") if line]


def pending_files(since: str | None = None) -> list[Path]:
    """Find unsynchronized content edits on the current branch, regardless of actor."""
    synchronized = read_state()
    current = content_fingerprints()
    paths = [Path(name) for name, digest in current.items() if synchronized.get(name) != digest]
    if since:
        names = set(git("log", "--since=" + since, "--format=", "--name-only", "-z").split("\0"))
        paths = [path for path in paths if path.as_posix() in names]
    return paths


def read_state() -> dict[str, str]:
    # Keep the checkpoint in the same commit as the metadata. Missing state is
    # recovered conservatively by synchronizing every supported file once.
    if not STATE_FILE.exists():
        return {}
    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    if not isinstance(state, dict) or any(
        not isinstance(name, str) or not isinstance(digest, str)
        or not re.fullmatch(r"[0-9a-f]{64}", digest)
        for name, digest in state.items()
    ):
        raise ValueError("Invalid Version synchronization checkpoint")
    return state


def content_fingerprints() -> dict[str, str]:
    candidates = [Path(name) for name in git("ls-files", "-z").split("\0") if name]
    fingerprints = {}
    for path in sorted(candidates):
        if not is_target(path) or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        # A Version-only publication is already synchronized. Comments remain
        # part of the comparison, so a comment-only manual edit is recovered.
        normalized = version_text(path, text, "<VERSION>")
        if normalized is not None:
            fingerprints[path.as_posix()] = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return fingerprints


def is_target(path: Path) -> bool:
    if path == HEADER_TEMPLATE:
        return False
    posix = path.as_posix()
    return any(posix.startswith(prefix) for prefix in TARGET_PREFIXES)


def update_file(path: Path, stamp: str) -> bool:
    if not path.is_file():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    updated = version_text(path, text, stamp)
    if updated is None or updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def version_text(path: Path, text: str, stamp: str) -> str | None:
    # ファイル種別に対応する先頭メタデータだけを更新し、本文のコード例を保持する。
    lines = text.splitlines(keepends=True)
    if path.suffix == ".md":
        pattern, replacement = PATTERNS[1]
        header_end = 0
        for line in lines:
            if line.lstrip().startswith(("```", "~~~")):
                break
            header_end += len(line)
            if pattern.search(line.rstrip("\n")):
                break
    elif path.suffix == ".txt":
        pattern, replacement = PATTERNS[0]
        header_end = 0
        for line in lines:
            if line.strip() and not line.startswith("!"):
                break
            header_end += len(line)
    elif path.name.endswith(".user.js") and text.startswith("// ==UserScript==\n"):
        pattern, replacement = PATTERNS[2]
        marker = "// ==/UserScript=="
        header_end = text.find(marker)
        if header_end < 0:
            return None
    else:
        return None

    header, matches = pattern.subn(replacement(stamp), text[:header_end], count=1)
    updated = header + text[header_end:]

    return updated if matches else None


def main() -> int:
    parser = argparse.ArgumentParser()
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--base", help="Base commit SHA")
    selection.add_argument("--since", help="Recover pending edits since this git date")
    selection.add_argument("--pending", action="store_true", help="Recover all pending edits on current branch")
    parser.add_argument("--head", default="HEAD", help="Head commit/ref")
    args = parser.parse_args()

    stamp = datetime.now(JST).strftime("%Y%m%d%H%M")
    updated: list[str] = []
    paths = pending_files(args.since) if args.pending or args.since else changed_files(args.base, args.head)
    for path in paths:
        if is_target(path) and update_file(path, stamp):
            updated.append(path.as_posix())

    if args.pending or args.since:
        current = content_fingerprints()
        state = {name: digest for name, digest in read_state().items() if name in current}
        for path in paths:
            name = path.as_posix()
            if name in current:
                state[name] = current[name]
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if updated:
        print(f"Updated Version metadata to {stamp} JST:")
        for path in updated:
            print(f"- {path}")
    else:
        print("No changed files with supported Version metadata required an update.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
