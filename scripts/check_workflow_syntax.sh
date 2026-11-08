#!/usr/bin/env bash
set -euo pipefail

# CIで未検証の可変ダウンロードを実行しないよう、actionlintのバージョンと
# アーカイブSHA256を固定する。更新時は両方を同時に変更する。
readonly ACTIONLINT_VERSION='1.7.12'
readonly ACTIONLINT_SHA256='8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8'
readonly ARCHIVE="actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz"
readonly URL="https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/${ARCHIVE}"
# 同じVersion・ファイル名・SHA256の公式Release Asset。Version更新時はIDも照合する。
readonly ASSET_API_URL='https://api.github.com/repos/rhysd/actionlint/releases/assets/384924896'

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

# ダウンロード後にハッシュを検証してから展開・実行する。
# HTTP 504等の一時障害だけを上限付きで再試行する。取得失敗・hash不一致は失敗のまま扱う。
download() {
  curl --fail --silent --show-error --location \
    --retry 3 --retry-delay 2 --connect-timeout 10 --max-time 60 \
    --write-out '%{http_code}' "$@" --output "$tmp_dir/$ARCHIVE"
}
if status="$(download "$URL")"; then
  :
elif [[ "$status" =~ ^5[0-9]{2}$ ]]; then
  # 公式の別経路で同じ配布物を取得する。認証情報や第三者ミラーは使わない。
  # 403・404・通信許可の拒否はこの経路へ切り替えず、原因を隠さない。
  echo "配布URLがHTTP $statusを返したため、公式Release Asset APIで再取得します。" >&2
  download --header 'Accept: application/octet-stream' "$ASSET_API_URL" >/dev/null
else
  echo "actionlintの取得に失敗しました (HTTP $status)。" >&2
  exit 1
fi
printf '%s  %s\n' "$ACTIONLINT_SHA256" "$tmp_dir/$ARCHIVE" | sha256sum --check --status
tar --no-same-owner -xzf "$tmp_dir/$ARCHIVE" -C "$tmp_dir" actionlint

"$tmp_dir/actionlint" -color
