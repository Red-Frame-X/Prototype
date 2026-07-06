import urllib.request
from urllib.error import HTTPError, URLError
import os
import sys
import re
from datetime import datetime, timezone, timedelta
from typing import List, Optional, Tuple

# 取得元：Kdroidwin氏のuBlock Origin用フィルタURL
CANDIDATE_URLS: List[str] = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt",
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
]

OUTPUT_FILE: str = "dist/uB-filter-by-kdroidwin_AdG_Optimized.txt"


class AdGuardOptimizer:
    def __init__(self) -> None:
        # 1. AdGuard Extended CSSでサポートされており、JSエンジンの介入が必須となる疑似クラス
        # 参照: https://github.com/AdguardTeam/ExtendedCss
        # ※注意: :is(), :not(), :where() はモダンブラウザの標準CSSで高速処理できるため除外
        self.adg_supported_ext_css: List[str] = [
            ':has(', ':has-text(', ':contains(', ':matches-css(', ':matches-css-after(',
            ':matches-css-before(', ':matches-attr(', ':matches-property(', ':xpath(',
            ':nth-ancestor(', ':upward(', ':remove()'
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
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AdGuard-Optimizer/2.3-MV3-Android'
        }
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

    def _parse_regex_rule(self, line: str) -> Optional[Tuple[str, str, str]]:
        """
        正規表現ルールを正確にパースするヘルパーメソッド
        戻り値: (例外フラグ '@@' or '', 正規表現本文 '/.../', 修飾子文字列 '$...')
        """
        prefix = '@@' if line.startswith('@@') else ''
        check_line = line[len(prefix):]
        
        if not check_line.startswith('/'):
            return None

        # エスケープされていない終端の / を探す
        idx = 1
        while idx < len(check_line):
            if check_line[idx] == '/' and check_line[idx - 1] != '\\':
                regex_part = check_line[:idx + 1]
                modifier_part = check_line[idx + 1:]
                return (prefix, regex_part, modifier_part)
            idx += 1
            
        return None

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
        regex_data = self._parse_regex_rule(line)
        if regex_data:
            prefix, regex_part, modifier_part = regex_data
            pattern_str = regex_part[1:-1]  # 前後のスラッシュを除去

            # 1. MV3非互換チェック: Chrome MV3のRE2エンジンは「後読み（Lookbehind: (?<= や (?<! ）」を未サポート
            # これが含まれるとMV3環境下でルール全体がパースエラーとなり破棄されるためパージする
            if '(?<=' in pattern_str or '(?<!' in pattern_str:
                return f"! [Unsupported MV3 Regex: Lookbehind not allowed in RE2] {original_line}"

            # 2. Android負荷チェック: モバイル端末でのバッテリー/メモリ消耗（ReDoS）を引き起こしやすい
            # 過剰なバックトラック（例: (.*)* や .+.+ のような二重量指定子）を検出して無効化
            if re.search(r'(?:\.\*|\.\+){2,}|(?:\(?:[^)]*(?:\.\*|\.\+)[^)]*\)){2,}', pattern_str):
                return f"! [High-Load Regex: Potential ReDoS / Battery Drain on Android] {original_line}"

            # 正規表現の検証を通過した場合、以降のネットワークルール修飾子処理へ受け渡す
            line = f"{prefix}{regex_part}{modifier_part}"

        # --- [Step B] コスメティックフィルタの拡張CSS（#?#）最適化 ---
        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts

                # AdGuard未対応のuBO独自修飾子が含まれる場合はパージ（CSSパーサーエラー・表示崩れ防止）
                if any(unsupported in selector_part for unsupported in self.ubo_unsupported_ext_css):
                    return f"! [Unsupported Extended CSS Modifier] {original_line}"

                # AdGuardの拡張CSS（JS解析）が必須な疑似クラスが含まれている場合のみ、セパレータを #?# へ自動変換
                if any(ext in selector_part for ext in self.adg_supported_ext_css):
                    new_separator = '#?#' if separator == '##' else '#?@#'
                    return f"{domain_part}{new_separator}{selector_part}"
            return line

        # --- [Step C] ネットワークルールの修飾子最適化 ---
        # 正規表現ルール、または通常のネットワークルールの修飾子処理
        if '$' in line:
            # 正規表現ルール内の $（アンカー等）を誤認しないよう安全に分割
            regex_data = self._parse_regex_rule(line)
            if regex_data:
                prefix, regex_part, modifier_part = regex_data
                if not modifier_part.startswith('$'):
                    return line  # 修飾子なしの正規表現ルール
                rule = f"{prefix}{regex_part}"
                modifiers_str = modifier_part[1:]  # 先頭の $ を除去
            else:
                # 行末アンカーとしての $ （例: ||example.com/test$ ）を保護する
                if line.endswith('$'):
                    # 行末の $ を除いた部分に、さらに修飾子区切りの $ があるか確認
                    line_without_end_anchor = line[:-1]
                    if '$' not in line_without_end_anchor:
                        return line  # 純粋な行末アンカーのみのルール

                parts = line.rsplit('$', 1)
                if len(parts) != 2:
                    return line
                rule, modifiers_str = parts

                # 分割結果、右側が空文字列（＝行末アンカーのみだった場合）は復元して終了
                if not modifiers_str:
                    return f"{rule}$"

            # 1. to= 修飾子の検知（リクエスト先とリクエスト元の意味論的相違による過剰ブロック・誤爆防止）
            if re.search(r'(?:^|,)\~?to=', modifiers_str):
                return f"! [Unsupported Modifier: to=] {original_line}"

            # 2. cname 修飾子の安全な除去 (AdGuard Web版および一部Android環境でのパースエラー回避)
            modifiers_str = re.sub(r'(?:^|,)cname(?=,|$)', '', modifiers_str)
            modifiers_str = modifiers_str.strip(',')
            modifiers_str = re.sub(r',+', ',', modifiers_str)  # 連続カンマの整理

            if not modifiers_str:
                return rule

            # 3. 修飾子の置換処理（例: queryprune -> removeparam）
            for ubo_mod, adg_mod in self.modifier_replacements.items():
                modifiers_str = re.sub(
                    rf'(?:^|,){re.escape(ubo_mod)}',
                    lambda m: m.group(0).replace(ubo_mod, adg_mod),
                    modifiers_str
                )

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
            ""  # 空行でヘッダーとルール本文を分離
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
