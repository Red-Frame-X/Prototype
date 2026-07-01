import urllib.request
from urllib.error import HTTPError
import os
import sys
import re
from datetime import datetime, timezone, timedelta

# 取得元：Kdroidwin氏のuBlock Origin用フィルタURL
CANDIDATE_URLS = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt",
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
]

OUTPUT_FILE = "dist/uB-filter-by-kdroidwin_AdG_Optimized.txt"

class AdGuardOptimizer:
    def __init__(self):
        # 1. 拡張CSS（Extended CSS）を必要とするuBOのプロシージャル・コスメティック修飾子
        self.ext_css_keywords = [
            ':has(', ':has-text(', ':contains(', ':matches-path(', ':matches-attr(', 
            ':matches-property(', ':xpath(', ':min-text-length(', ':watch-attr(', 
            ':matches-css(', ':matches-media(', ':upward(', ':remove()'
        ]
        
        # 2. AdGuardではサポート外、またはエラーの元となるuBO特有のスクリプトレット
        self.incompatible_scriptlets = [
            'acis', 'spoof-css', 'trusted-replace-argument', 'trusted-set-cookie',
            'alert-buster', 'trusted-click-element', 'webassembly-interference',
            'm3u-prune', 'json-prune', 'json-prune-set'
        ]
        
        # 3. 修飾子の置換マップ (uBO独自の修飾子をAdGuard互換の修飾子へ)
        self.modifier_replacements = {
            'queryprune': 'removeparam',
            'redirect-rule=': 'redirect=',
            # 注: 'to=' は 'domain=' とスコープが逆転するためここでは置換せず、後段で安全にパージする
        }

    def fetch_source(self):
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

    def optimize_line(self, line):
        original_line = line
        line = line.strip()

        # 空行や元のヘッダー（!から始まる行）は除外
        if not line or line.startswith('!'):
            return None  

        # --- [Step A] 致命的な非互換ルールのパージ (Lint機能) ---
        # uBOのHTMLフィルタ（##^）はAdGuardでは解釈できずパースエラーになるため無効化
        if '##^' in line:
            return f"! [Unsupported HTML Filter] {original_line}"

        # スクリプトレットの互換性チェック
        if '##+js(' in line or '#@#+js(' in line:
            for bad_js in self.incompatible_scriptlets:
                if f"+js({bad_js}" in line or f"+js({bad_js}," in line:
                    return f"! [Incompatible Scriptlet] {original_line}"
            # 互換性があるものはそのまま返す
            return line

        # --- [Step B] コスメティックフィルタの拡張CSS（#?#）最適化 ---
        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts
                # uBOのプロシージャル演算子が含まれているか解析
                if any(ext in selector_part for ext in self.ext_css_keywords):
                    # AdGuardの拡張CSSセパレータ（#?# または #?@#）に明示的に置換
                    new_separator = '#?#' if separator == '##' else '#?@#'
                    return f"{domain_part}{new_separator}{selector_part}"
            return line

        # --- [Step C] ネットワークルールの修飾子最適化 ---
        if '$' in line and not line.startswith('/') and not line.startswith('@@/'):
            parts = line.rsplit('$', 1)
            if len(parts) == 2:
                rule, modifiers = parts
                mod_list = modifiers.split(',')
                
                # cname修飾子の除去
                if 'cname' in mod_list:
                    mod_list = [m for m in mod_list if m != 'cname']

                # to=修飾子の検知 (リクエスト先とリクエスト元の意味論的相違による誤爆を防止)
                if any(m.startswith('to=') for m in mod_list):
                    return f"! [Unsupported Modifier: to=] {original_line}"

                if not mod_list:
                    return rule 
                
                # 修飾子の置換処理（例: queryprune -> removeparam）
                modifiers_str = ','.join(mod_list)
                for ubo_mod, adg_mod in self.modifier_replacements.items():
                    modifiers_str = re.sub(rf'\b{ubo_mod}', adg_mod, modifiers_str)

                return f"{rule}${modifiers_str}"

        return line

    def run(self):
        lines = self.fetch_source()
        
        jst = timezone(timedelta(hours=+9), 'JST')
        current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

        converted = [
            "! Title: uB-filter-by-kdroidwin (AdGuard Optimized)",
            "! Description:  A filter that blocks scam sites, fake sites and malicious affiliate sites.",
            f"! Version: {current_version}",
            "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
            "! License: GPL-3.0",
            "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
            "! The rules were automatically converted by a custom Python script (convert.py) and then strictly linted by AGLint.\n"
        ]

        print("フィルタの高度な最適化とLint（静的解析）処理を開始します...")
        stats = {"converted": 0, "bypassed": 0, "commented": 0}

        for line in lines:
            optimized = self.optimize_line(line)
            if optimized is None:
                continue
            
            converted.append(optimized)
            
            if optimized != line and not optimized.startswith('! ['):
                stats["converted"] += 1
            elif optimized.startswith('! ['):
                stats["commented"] += 1
            else:
                stats["bypassed"] += 1

        output_dir = os.path.dirname(OUTPUT_FILE)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(converted) + '\n')
        
        print(f"✔ 変換完了: {OUTPUT_FILE} (Version: {current_version})")
        print(f"  [統計] 最適化適用: {stats['converted']}件 | 無効化(パージ): {stats['commented']}件 | パス(そのまま): {stats['bypassed']}件")


if __name__ == '__main__':
    opt = AdGuardOptimizer()
    opt.run()
