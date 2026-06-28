import urllib.request
import re
import datetime

# 上流（Kdroidwin氏）のuBlock Origin用フィルタのRaw URL
UPSTREAM_URL = "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
OUTPUT_PATH = "dist/adguard_filter.txt"

def convert_filter():
    # 1. 上流データの取得
    req = urllib.request.Request(UPSTREAM_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')

    lines = content.splitlines()
    converted_lines = []

    for line in lines:
        # メタデータのタイトルや説明文をAdGuard向けに調整
        if line.startswith("! Title:"):
            converted_lines.append("! Title: uB-filter-by-kdroidwin (AdGuard Optimized)")
            continue
        if line.startswith("! Last modified:"):
            now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            converted_lines.append(f"! Last modified: {now}")
            continue

        # uBO特有のスクリプトレット(+js)をAdGuard構文(#%#//scriptlet)に変換する例
        if "+js(" in line:
            line = re.sub(r'##\+js\(([^,]+)(?:,\s*(.+))?\)', r'#%#//scriptlet(\1, \2)', line)

        converted_lines.append(line)

    # 2. 変換後ファイルの保存
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted_lines) + '\n')

if __name__ == "__main__":
    convert_filter()
