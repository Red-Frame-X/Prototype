import urllib.request
from urllib.error import HTTPError
import json
import re
import os
import sys
from datetime import datetime, timezone, timedelta

OUTPUT_FILE = "dist/uB-filter-by-kdroidwin.txt"

# 探索対象の上流リポジトリ情報
REPO_OWNER = "Kdroidwin"
REPO_NAME = "uB-filter-by-kdroidwin"

# API探索が万が一ブロックされた場合に備えた「総当たりフォールバック候補」
FALLBACK_URLS = [
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/uBlockOrigin.txt",
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/master/ublockorigin.txt",
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/uBlockOrigin.txt",
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main/ublockorigin.txt",
]

def fetch_source_data():
    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    # 【フェーズ1】GitHub REST APIによる実在ファイルの動的自動探索
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents"
    print(f"[フェーズ1] GitHub APIにて上流リポジトリの構成を自動探索中...\n接続先: {api_url}")
    
    try:
        req = urllib.request.Request(api_url, headers=req_headers)
        with urllib.request.urlopen(req) as res:
            contents = json.loads(res.read().decode('utf-8'))
            
            # ライセンス等を除外した本物のフィルタ(.txt)を探し出す
            ignore_list = ["license.txt", "readme.txt"]
            for item in contents:
                name_lower = item.get("name", "").lower()
                if item.get("type") == "file" and name_lower.endswith(".txt") and name_lower not in ignore_list:
                    target_url = item.get("download_url")
                    print(f"✔ 実在するターゲットファイルを発見しました: {item['name']}")
                    print(f"  ダウンロードを実行します: {target_url}")
                    
                    dl_req = urllib.request.Request(target_url, headers=req_headers)
                    with urllib.request.urlopen(dl_req) as dl_res:
                        return dl_res.read().decode('utf-8').splitlines()
                        
            print("  × ルートディレクトリにフィルタ(.txt)が見つかりません。フォールバックへ移行します。")

    except HTTPError as e:
        if e.code == 404:
            print(f"\n=======================================================")
            print(f"[根本原因が確定しました]")
            print(f"GitHub上にリポジトリ 'https://github.com/{REPO_OWNER}/{REPO_NAME}' が存在しません。")
            print(f"（※提供者によるリポジトリ名の変更、または削除・非公開化が原因です）")
            print(f"=======================================================")
            sys.exit(1)
        print(f"  × API通信スキップ ({e.code})。フォールバックへ移行します。")
    except Exception as e:
        print(f"  × API探索エラー: {e}。フォールバックへ移行します。")

    # 【フェーズ2】静的候補による総当たり試行（マスターブランチ等）
    print("\n[フェーズ2] 静的URL候補の総当たりを試行します...")
    for url in FALLBACK_URLS:
        print(f"接続試行中: {url}")
        try:
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req) as res:
                print("✔ 静的フォールバックURLでの取得に成功しました！")
                return res.read().decode('utf-8').splitlines()
        except HTTPError:
            pass

    print("\n[致命的エラー] 上流リポジトリから有効なテキストデータを一切取得できませんでした。")
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

    jst = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(jst)
    
    current_version = now.strftime('%Y%m%d%H%M')
    time_updated = now.strftime('%Y-%m-%dT%H:%M:%S+09:00')

    converted = [
        "! Title: uB-filter-by-kdroidwin",
        "! Description: This is an unofficial version of uB-filter-by-kdroidwin, optimised for AdGuard.",
        f"! Version: {current_version}",
        f"! TimeUpdated: {time_updated}",
        "! Expires: 1 day",
        "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
        "! License: GPL-3.0",
        "!",
        "! --- Upstream & Build Attribution ---",
        f"! Upstream repository: https://github.com/{REPO_OWNER}/{REPO_NAME}",
        "! Converted automatically via GitHub Actions",
        ""
    ]

    print("\n構文変換処理を開始します...")
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

if
