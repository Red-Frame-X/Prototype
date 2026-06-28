import urllib.request
from urllib.error import HTTPError
import re
import os
import sys
from datetime import datetime, timezone, timedelta

# 取得元：Kdroidwin氏のuBlock Origin用フィルタURL
CANDIDATE_URLS = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt",
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
]

OUTPUT_FILE = "dist/uB-filter-by-kdroidwin.txt"

def fetch_source_data():
    req_headers = {'User-Agent': 'Mozilla/5.0'}
    for url in CANDIDATE_URLS:
        print(f"接続試行中: {url}")
        try:
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req) as res:
                print("✔ 元データのダウンロードに成功しました")
                return res.read().decode('utf-8').splitlines()
        except HTTPError as e:
            print(f"   × スキップ ({e.code})")
        except Exception as e:
            print(f"   × 通信エラー: {e}")

    print("\n[致命的エラー] 元データが取得できませんでした。")
    sys.exit(1)

def format_scriptlet_args(args_raw_str):
    raw_args = [arg.strip() for arg in args_raw_str.split(',')]
    formatted_args = []
    
    for arg in raw_args:
        if not arg:
            continue
        clean_arg = re.sub(r'^[\'"]|[\'"]$', '', arg)
        escaped_arg = clean_arg.replace("'", "\\'")
        formatted_args.append(f"'{escaped_arg}'")
        
    return ", ".join(formatted_args)

def convert_ubo_to_adguard():
    lines = fetch_source_data()

    # 日本時間(JST)での現在時刻を「YYYYMMDDHHmm」形式で取得
    jst = timezone(timedelta(hours=+9), 'JST')
    current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

    # 💡 HomepageのURLをご指定のもの（リポジトリのルート）に変更しました
    converted = [
        "! Title: uB-filter-by-kdroidwin",
        "! Description: This is an unofficial version of uB-filter-by-kdroidwin, optimised for AdGuard.",
        f"! Version: {current_version}",
        "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
        "! License: GPL-3.0",
        "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
        "! Converted automatically via GitHub Actions\n"
    ]

    print("構文変換処理を開始します...")
    for line in lines:
        line = line.strip()
        if not line or line.startswith('!'):
            continue
            
        if '#@#+js(' in line:
            prefix, args_part = line.split('#@#+js(', 1)
            args_raw = args_part.rstrip(')')
            line = f"{prefix}#@%#//scriptlet({format_scriptlet_args(args_raw)})"
            
        elif '##+js(' in line:
            prefix, args_part = line.split('##+js(', 1)
            args_raw = args_part.rstrip(')')
            line = f"{prefix}#%#//scriptlet({format_scriptlet_args(args_raw)})"

        converted.append(line)

    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted) + '\n')
    
    print(f"✔ 変換完了: {OUTPUT_FILE} (Version: {current_version})")

if __name__ == '__main__':
    convert_ubo_to_adguard()
