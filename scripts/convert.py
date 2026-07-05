import urllib.request
from urllib.error import HTTPError, URLError
import os
import sys
import re
from datetime import datetime, timezone, timedelta
from typing import List, Optional

# 取得元：Kdroidwin氏のuBlock Origin用フィルタURL
CANDIDATE_URLS: List[str] = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt",
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
]

OUTPUT_FILE: str = "dist/uB-filter-by-kdroidwin_AdG_Optimized.txt"

class AdGuardOptimizer:
    def __init__(self) -> None:
        # 1. AdGuard Extended CSSでサポートされている疑似クラス
        # 参照: https://github.com/AdguardTeam/ExtendedCss
        self.adg_supported_ext_css: List[str] = [
            ':has(', ':has-text(', ':contains(', ':matches-css(', ':matches-css-after(',
            ':matches-css-before(', ':matches-attr(', ':matches-property(', ':xpath(', 
            ':nth-ancestor(', ':upward(', ':remove()', ':is(', ':not(', ':where('
        ]
        
        # 2. AdGuardでは未対応・挙動不一致となるuBO独自のプロシージャル演算子（パージ対象）
        self.ubo_unsupported_ext_css: List[str] = [
            ':matches-path(', ':min-text-length(', ':watch-attr(', ':matches-media('
        ]
        
        # 3. AdGuard（特にMV3/Android環境）で未対応、またはセキュリティ・エラーリスクとなるスクリプトレット
        self.incompatible_scriptlets: List[str] = [
            'acis', 'spoof-css', 'trusted-replace-argument', 'trusted-set-cookie',
            'alert-buster', 'trusted-click-element', 'webassembly-interference',
            'm3u-prune', 'json-prune', 'json-prune-set'
        ]
        
        # 4. 修飾子の置換マップ (uBO独自の修飾子をAdGuard互換の修飾子へ)
        self.modifier_replacements = {
            'queryprune': 'removeparam',
            'redirect-rule=': 'redirect=',
        }

    def fetch_source(self) -> List[str]:
        req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AdGuard-Optimizer/2.2-MV3-Android'}
        for url in CANDIDATE_URLS:
            print(f"接続試行中: {url}")
            try:
                # タイムアウトを15秒に設定し、ハングアップを防止
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, timeout=15) as res:
                    print("✔ 元データのダウンロードに成功しました")
                    return res.read().decode('utf-8').splitlines()
            except HTTPError as e:
                print(f"   × スキップ (HTTP Error: {e.code})")
            except URLError as e:
                print(f"   × 通信エラー (URL Error): {e.reason}")
            except Exception as e:
                print(f"   × 予期せぬエラー: {e}")

        print("\n[致命的エラー] 元データが取得できませんでした。")
        sys.exit(1)

    def optimize_line(self, line: str) -> Optional[str]:
        original_line = line
        line = line.strip()

        # 空行や元のヘッダー（!から始まる行）は除外
        if not line or line.startswith('!'):
            return None  

        # --- [Step A-1] 致命的な非互換ルールのパージ (HTMLフィルタ等) ---
        # uBOのHTMLフィルタ（##^や#@#^）はAdGuardでは解釈できずパースエラーになるため無効化
        if '##^' in line or '#@#^' in line:
            return f"! [Unsupported HTML Filter] {original_line}"

        # スクリプトレットの互換性チェック
        if '##+js(' in line or '#@#+js(' in line:
            for bad_js in self.incompatible_scriptlets:
                if f"+js({bad_js}" in line or f"+js({bad_js}," in line:
                    return f"! [Incompatible Scriptlet] {original_line}"
            return line

        # --- [Step A-2] MV3 (RE2エンジン) および Android 向けの正規表現（Regex）厳格検証 ---
        # 正規表現ルール（/で始まり、末尾または$の直前が/で終わるパターン）を安全に検出
        is_regex_rule = False
        pattern_str = ""
        if line.startswith('/') or line.startswith('@@/'):
            check_line = line[2:] if line.startswith('@@/') else line
            if check_line.startswith('/'):
                # スラッシュで囲まれているかを判定 (エスケープされた \/ は正しく除外)
                parts = check_line.split('$')
                rule_part = parts[0]
                if len(rule_part) >= 2 and rule_part.startswith('/') and rule_part.endswith('/') and not rule_part.endswith('\\/'):
                    is_regex_rule = True
                    pattern_str = rule_part[1:-1] # 前後のスラッシュを除去
        
        if is_regex_rule:
            # 1. MV3非互換チェック: Chrome MV3のRE2エンジンは「後読み（Lookbehind: (?<= や (?<! ）」を未サポート
            # これが含まれるとMV3環境下でルール全体がパースエラーとなり破棄されるためパージする
            if '(?<=' in pattern_str or '(?<!' in pattern_str:
                return f"! [Unsupported MV3 Regex: Lookbehind not allowed in RE2] {original_line}"
            
            # 2. Android負荷チェック: モバイル端末でのバッテリー/メモリ消耗（ReDoS）を引き起こしやすいい
            # 過剰なバックトラック（例: (.*)* や .+.+ のような二重量指定子）を検出して無効化
            if re.search(r'(?:\.\*|\.\+){2,}|(?:\(?:[^)]*(?:\.\*|\.\+)[^)]*\)){2,}', pattern_str):
                return f"! [High-Load Regex: Potential ReDoS / Battery Drain on Android] {original_line}"

        # --- [Step B] コスメティックフィルタの拡張CSS（#?#）最適化 ---
        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts
                
                # AdGuard未対応のuBO独自修飾子が含まれる場合はパージ（CSSパーサーエラー・表示崩れ防止）
                if any(unsupported in selector_part for unsupported in self.ubo_unsupported_ext_css):
                    return f"! [Unsupported Extended CSS Modifier] {original_line}"
                
                # AdGuard対応の拡張CSS疑似クラスが含まれている場合、セパレータを #?# へ自動変換
                if any(ext in selector_part for ext in self.adg_supported_ext_css):
                    new_separator = '#?#' if separator == '##' else '#?@#'
                    return f"{domain_part}{new_separator}{selector_part}"
            return line

        # --- [Step C] ネットワークルールの修飾子最適化 ---
        if '$' in line and not line.startswith('/') and not line.startswith('@@/'):
            parts = line.rsplit('$', 1)
            if len(parts) == 2:
                rule, modifiers_str = parts
                
                # 【重要】カンマ分割(split)を使わず、正規表現でセキュアにチェック・置換を行う
                # domain=a.com,b.com や removeparam=a,b 等の値に含まれるカンマ破壊を防止

                # 1. to= 修飾子の検知（リクエスト先とリクエスト元の意味論的相違による過剰ブロック・誤爆防止）
                if re.search(r'(?:^|,)\~?to=', modifiers_str):
                    return f"! [Unsupported Modifier: to=] {original_line}"

                # 2. cname 修飾子の安全な除去 (AdGuard Web版および一部Android環境でのパースエラー回避)
                modifiers_str = re.sub(r'(?:^|,)cname(?=,|$)', '', modifiers_str)
                modifiers_str = modifiers_str.strip(',')
                modifiers_str = re.sub(r',+', ',', modifiers_str) # 連続カンマの整理

                if not modifiers_str:
                    return rule 
                
                # 3. 修飾子の置換処理（例: queryprune -> removeparam）
                for ubo_mod, adg_mod in self.modifier_replacements.items():
                    modifiers_str = re.sub(rf'(?:^|,){re.escape(ubo_mod)}', lambda m: m.group(0).replace(ubo_mod, adg_mod), modifiers_str)

                return f"{rule}${modifiers_str}"

        return line

    def get_rule_signature(self, lines: List[str]) -> List[str]:
        """コメント行と空行を除いた純粋なルール本文だけのリストを生成（差分比較用）"""
        return [l.strip() for l in lines if l.strip() and not l.strip().startswith('!')]

    def run(self) -> None:
        lines = self.fetch_source()
        
        print("フィルタの高度な最適化とLint（静的解析・MV3/Android互換チェック）処理を開始します...")
        stats = {"converted": 0, "bypassed": 0, "commented": 0}
        optimized_lines: List[str] = []

        for line in lines:
            optimized = self.optimize_line(line)
            if optimized is None:
                continue
            
            optimized_lines.append(optimized)
            
            if optimized != line and not optimized.startswith('! ['):
                stats["converted"] += 1
            elif optimized.startswith('! ['):
                stats["commented"] += 1
            else:
                stats["bypassed"] += 1

        # --- [Step D] スマート差分検知 (無駄なコミットの抑止) ---
        new_signature = self.get_rule_signature(optimized_lines)
        
        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                existing_lines = f.read().splitlines()
            old_signature = self.get_rule_signature(existing_lines)
            
            if new_signature == old_signature:
                print("\n[お知らせ] 元ルール本文に実質的な変更はありません。ファイルの更新をスキップします。")
                print("※ 無駄なバージョンアップやGitコミットを抑止しました。")
                return

        # 変更があった場合のみ、新しいタイムスタンプでファイルを生成
        jst = timezone(timedelta(hours=+9), 'JST')
        current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

        header = [
            "! Title: uB-filter-by-kdroidwin (AdGuard Optimized)",
            "! Description: A filter that blocks scam sites, fake sites and malicious affiliate sites. Optimized for AdGuard MV3 & Android.",
            f"! Version: {current_version}",
            "! Syntax: AdGuard (MV3 & Android Compatible)",
            "! Expires: 12 hours",
            "! Homepage: https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown",
            "! License: GPL-3.0",
            "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
            "! Disclaimer: This is an unofficial personal fork. The rules were automatically converted by a custom Python script (convert.py) and strictly linted by AGLint for MV3 & Android compatibility.",
            "" # 空行でヘッダーとルール本文を分離
        ]

        converted_full = header + optimized_lines

        output_dir = os.path.dirname(OUTPUT_FILE)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(converted_full) + '\n')
        
        print(f"\n✔ 変換および更新完了: {OUTPUT_FILE} (Version: {current_version})")
        print(f"  [統計] 最適化適用: {stats['converted']}件 | 無効化(パージ): {stats['commented']}件 | パス(そのまま): {stats['bypassed']}件")


if __name__ == '__main__':
    opt = AdGuardOptimizer()
    opt.run()
