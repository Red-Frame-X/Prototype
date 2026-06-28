import urllib.request
from urllib.error import HTTPError
import re
import os
import sys

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
                print("✔ データのダウンロードに成功しました！")
                return res.read().decode('utf-8').splitlines()
        except HTTPError as e:
            print(f"  × スキップ ({e.code}): 見つかりませんでした")
        except Exception as e:
            print(f"  × 通信エラー: {e}")

    print("\n[致命的エラー] 元データが取得できませんでした。URLを確認してください。")
    sys.exit(1)

def convert_ubo_to_adguard():
    lines = fetch_source_data()

    # 💡 赤枠内を「! Title: uB-filter-by-kdroidwin」だけに完全固定
    converted = [
        "! Title: uB-filter-by-kdroidwin",
        "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
        "! License: GPL-3.0",
        "! Converted automatically via GitHub Actions",
        "! ------------------------------------------------------------\n"
    ]

    print("uBlock Origin 構文から AdGuard 構文への変換処理を開始します...")
    for line in lines:
        line = line.strip()
        if not line or line.startswith('!'):
            continue
            
        if '+js(' in line:
            line = re.sub(r'\+js\((.*?)\)', r'#%#//scriptlet(\1)', line)
            
        converted.append(line)

    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted) + '\n')
    
    print(f"✔ 変換完了: {OUTPUT_FILE} を生成しました。")

if __name__ == '__main__':
    convert_ubo_to_adguard()
