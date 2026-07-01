import urllib.request
from urllib.error import HTTPError
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

def convert_ubo_to_adguard():
    lines = fetch_source_data()

    # 日本時間(JST)での現在時刻を「YYYYMMDDHHmm」形式で取得
    jst = timezone(timedelta(hours=+9), 'JST')
    current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

    # ヘッダーの生成
    converted = [
        "! Title: uB-filter-by-kdroidwin (AdGuard Optimized)",
        "! Description: This is an unofficial version of uB-filter-by-kdroidwin, optimised for AdGuard.",
        f"! Version: {current_version}",
        "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
        "! License: GPL-3.0",
        "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
        "! Converted automatically via GitHub Actions\n"
    ]

    print("フィルタの最適化処理を開始します...")
    for line in lines:
        line = line.strip()
        
        # 空行や元のヘッダー（!から始まる行）はスキップ
        if not line or line.startswith('!'):
            continue
            
        # AdGuard CoreLibsはuBOの `##+js()` および `#@#+js()` 構文をネイティブサポートしているため、
        # 破壊リスクのあるレガシー構文への置換処理を撤廃し、そのまま追加します。
        converted.append(line)

    # 出力先ディレクトリの作成
    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # 書き込み
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted) + '\n')
    
    print(f"✔ 変換完了: {OUTPUT_FILE} (Version: {current_version})")

if __name__ == '__main__':
    convert_ubo_to_adguard()
