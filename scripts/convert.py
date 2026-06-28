import urllib.request
import re
import os

# 取得元：Kdroidwin氏のuBlock Origin用フィルタURL
SOURCE_URL = "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt"

# 出力先：distフォルダと、スペース・カッコを含む新しいファイル名
OUTPUT_FILE = "dist/uB-filter-by-kdroidwin (AdGuard Optimized).txt"

def convert_ubo_to_adguard():
    print("ユーザーエージェントを設定して元データをダウンロード中...")
    req = urllib.request.Request(SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as res:
            lines = res.read().decode('utf-8').splitlines()
    except Exception as e:
        print(f"元データのダウンロードに失敗しました: {e}")
        return

    # フィルタのヘッダー情報（メタデータ）の構築
    converted = []
    converted.append("! Title: uB-filter-by-kdroidwin (AdGuard Optimized)")
    converted.append("! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin")
    converted.append("! License: GPL-3.0 (Inherited from original source)")
    converted.append("! Converted automatically via GitHub Actions")
    converted.append("! ------------------------------------------------------------\n")

    print("uBlock Origin 構文から AdGuard 構文への変換処理を開始します...")
    for line in lines:
        line = line.strip()
        
        # 空行や、元ファイルのヘッダーコメント行はスキップ（重複防止）
        if not line or line.startswith('!'):
            continue
            
        # --- 基本的な構文変換ロジック ---
        # スクリプトレットの変換 (uBO: +js(...) -> AdGuard: #%#//scriptlet(...))
        if '+js(' in line:
            line = re.sub(r'\+js\((.*?)\)', r'#%#//scriptlet(\1)', line)

        # 必要に応じて、ここに他の構文変換ルールを追跡・追加できます

        converted.append(line)

    # 💡 dist フォルダが存在しない場合は自動で作成する安全弁
    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        print(f"フォルダを作成しました: {output_dir}")

    # ファイルへの書き込み
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(converted) + '\n')
    
    print(f"変換が正常に完了しました。出力先: {OUTPUT_FILE}")

if __name__ == '__main__':
    convert_ubo_to_adguard()
