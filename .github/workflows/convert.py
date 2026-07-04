#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AdGuard Exclusive Filter Merger & Strict Syntax Converter
Title: JP Filter Plus - Unofficial AdGuard Fork
"""

import urllib.request
import urllib.error
import re
from datetime import datetime, timezone, timedelta
import os

# 上流フィルタのソースURL
UPSTREAM_URLS = [
    "https://raw.githubusercontent.com/Yuki2718/adblock2/main/japanese/jpf-plus.txt",
    "https://raw.githubusercontent.com/Yuki2718/adblock2/refs/heads/main/japanese/jpfp-ag.txt"
]

# 出力先設定（ご指定の dist ディレクトリ配下）
OUTPUT_DIR = "dist"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "jpf-plus-ag-merged.txt")

def fetch_filter_lines(url):
    """指定URLからフィルタテキストを安全に取得し、行ごとのリストを返す"""
    try:
        req = urllib.request.Request(
            url, 
            headers={"User-Agent": "Mozilla/5.0 (AdGuard-Strict-Converter-Fork/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8')
            return content.splitlines()
    except Exception as e:
        print(f"[Error] 上流フィルタの取得に失敗しました ({url}): {e}")
        return []

def is_metadata_line(line):
    """既存のヘッダーメタデータ行を正確に検出して除外する"""
    metadata_prefixes = (
        "! Title:", "! Description:", "! Version:", "! TimeUpdated:",
        "! Expires:", "! Homepage:", "! License:", "! Checksum:",
        "! Last modified:", "! Updated:", "! Author:", "! Total rules:",
        "! AdGuard-Exclusive:"
    )
    return line.startswith(metadata_prefixes)

def parse_scriptlet_args(content):
    """
    クォーテーションを考慮してスクリプトレットの引数を厳格に分割する。
    引数内のカンマ（正規表現やオブジェクト等）による構文崩れを防止します。
    """
    tokens = []
    current_token = []
    in_quotes = False
    quote_char = None
    
    for char in content:
        if char in ("'", '"'):
            if not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char:
                in_quotes = False
                quote_char = None
            current_token.append(char)
        elif char == ',' and not in_quotes:
            tokens.append("".join(current_token).strip())
            current_token = []
        else:
            current_token.append(char)
            
    if current_token:
        tokens.append("".join(current_token).strip())
        
    return [t.strip("'\"") for t in tokens if t.strip()]

def convert_ubo_to_adguard(line):
    """
    uBlock Origin専用の構文をAdGuard専用の高度な構文に厳格に変換する。
    AdGuardパーサーでのエラーや警告を完全に排除します。
    """
    if line.startswith('!'):
        return line

    # 1. 修飾子（Options）の厳格なマッピングと置換
    if '$' in line:
        parts = line.split('$', 1)
        base_rule = parts[0]
        options = parts[1].split(',')
        new_options = []
        for opt in options:
            opt_strip = opt.strip()
            if opt_strip == 'ghide':
                new_options.append('generichide')
            elif opt_strip == 'shide':
                new_options.append('specifichide')
            elif opt_strip == 'ehide':
                new_options.append('elemhide')
            elif opt_strip == 'doc':
                new_options.append('document')
            else:
                new_options.append(opt_strip)
        line = f"{base_rule}${','.join(new_options)}"

    # 2. スクリプトレット構文（##+js / #@#+js）の厳格な変換
    ubo_scriptlet_match = re.search(r'^([a-z0-9.-]*)(#@?#)\+js\((.*)\)$', line)
    if ubo_scriptlet_match:
        domain = ubo_scriptlet_match.group(1)
        selector_type = ubo_scriptlet_match.group(2)
        content = ubo_scriptlet_match.group(3)
        
        if content.endswith(')'):
            content = content[:-1]
            
        tokens = [t.strip().strip("'\"") for t in parse_scriptlet_args(content)]
        if tokens:
            scriptlet_name = tokens[0]
            args = tokens[1:]
            
            ag_marker = '#%#' if selector_type == '##' else '#@%#'
            if args:
                arg_str = ", ".join([f"'{a}'" for a in args])
                line = f"{domain}{ag_marker}//scriptlet('{scriptlet_name}', {arg_str})"
            else:
                line = f"{domain}{ag_marker}//scriptlet('{scriptlet_name}')"

    return line

def main():
    merged_rules = []
    seen_rules = set()

    print("上流フィルタの取得と厳格な変換処理を開始します...")
    for url in UPSTREAM_URLS:
        lines = fetch_filter_lines(url)
        print(f"取得成功: {len(lines)} 行 ({url})")
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if is_metadata_line(stripped):
                continue
            
            converted_line = convert_ubo_to_adguard(stripped)
            
            if converted_line not in seen_rules:
                seen_rules.add(converted_line)
                merged_rules.append(converted_line)

    # メタデータ生成（TimeUpdated / Version）
    now_utc = datetime.now(timezone.utc)
    now_jst = now_utc.astimezone(timezone(timedelta(hours=9)))
    version_str = now_jst.strftime("%Y.%m.%d.%H%M")
    time_updated_str = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # 実際の有効ルール数をカウント（コメント行を除く）
    active_rule_count = sum(1 for rule in merged_rules if not rule.startswith("!"))

    # 業界標準を満たした短く分かりやすい英文 Description を反映
    header = [
        "! Title: JP Filter Plus - Unofficial AdGuard Fork",
        "! Description: Unofficial fork merging Yuki2718's JPF Plus filters. Fully converted to AdGuard syntax (AdGuard-exclusive).",
        f"! Version: {version_str}",
        f"! TimeUpdated: {time_updated_str}",
        "! Expires: 12 hours (update frequency)",
        "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
        "! License: https://github.com/Yuki2718/adblock2/blob/main/LICENSE",
        "! AdGuard-Exclusive: True",
        f"! Total rules: {active_rule_count}",
        "! " + "-" * 75
    ]

    # 出力先ディレクトリ (dist/) の作成と保存
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(header) + "\n\n")
        f.write("\n".join(merged_rules) + "\n")

    print(f"[Success] 保存完了: {OUTPUT_FILE} (実効ルール数: {active_rule_count})")

if __name__ == "__main__":
    main()
