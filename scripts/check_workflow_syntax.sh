#!/usr/bin/env bash
set -euo pipefail

# Keep the version and archive digest pinned so CI does not execute an
# unverified, moving download. Update both values together when upgrading.
readonly ACTIONLINT_VERSION='1.7.12'
readonly ACTIONLINT_SHA256='8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8'
readonly ARCHIVE="actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz"
readonly URL="https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/${ARCHIVE}"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

curl --fail --silent --show-error --location "$URL" --output "$tmp_dir/$ARCHIVE"
printf '%s  %s\n' "$ACTIONLINT_SHA256" "$tmp_dir/$ARCHIVE" | sha256sum --check --status
tar --no-same-owner -xzf "$tmp_dir/$ARCHIVE" -C "$tmp_dir" actionlint

"$tmp_dir/actionlint" -color
