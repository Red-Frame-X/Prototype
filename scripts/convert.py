import urllib.request
from urllib.error import HTTPError, URLError
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
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for url in CANDIDATE_URLS:
        print(f"接続試行中: {url}")
        try:
            # タイムアウトを設定してハングアップを防止
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=15) as res:
                print("✔ 元データのダウンロードに成功しました")
                # BOM付きUTF-8にも対応できるよう utf-8-sig を使用
                return res.read().decode('utf-8-sig').splitlines()
        except HTTPError as e:
            print(f"   × スキップ (HTTPエラー: {e.code} {e.reason})")
        except URLError as e:
            print(f"   × スキップ (通信エラー: {e.reason})")
        except Exception as e:
            print(f"   × スキップ (予期せぬエラー: {e})")

    print("\n[致命的エラー] すべての候補URLから元データを取得できませんでした。")
    sys.exit(1)

def build_adguard_filter():
    lines = fetch_source_data()

    # 日本時間(JST)での現在時刻を「YYYYMMDDHHmm」形式で取得
    jst = timezone(timedelta(hours=+9), 'JST')
    current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

    # AdGuard公式基準の並び順に沿ってメタデータを配置
    converted = [
        "! Title: uB-filter-by-kdroidwin (AdGuard Optimized)",
        "! Description: This is an unofficial version of uB-filter-by-kdroidwin, optimised for AdGuard.",
        f"! Version: {current_version}",
        "! Expires: 4 days",
        "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
        "! License: GPL-
