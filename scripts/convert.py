#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uB-filter-by-kdroidwin to AdGuard Optimizer & Linter

uBlock Origin用フィルタをAdGuard (MV3 / Android) 向けに最適化・静的解析(Lint)するスクリプト。

License: GPL-3.0
Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin
"""

import os
import sys
import re
import urllib.request
from urllib.error import HTTPError, URLError
from datetime import datetime, timezone, timedelta
from typing import List, Optional, Tuple, Dict, Pattern

CANDIDATE_URLS: List[str] = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockOrigin.txt",
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/main/uBlockorigin.txt"
]

OUTPUT_FILE: str = "dist/uB-filter-by-kdroidwin_AdG_Optimized.txt"


class AdGuardOptimizer:
    def __init__(self) -> None:
        # AdGuard拡張CSSでJS解析が必須な疑似クラス (:is, :not, :where は標準CSSで処理可能なため除外)
        self.adg_supported_ext_css: List[str] = [
            ':has(', ':has-text(', ':contains(', ':matches-css(', ':matches-css-after(',
            ':matches-css-before(', ':matches-attr(', ':matches-property(', ':xpath(',
            ':nth-ancestor(', ':upward(', ':remove()'
        ]

        # AdGuard未対応・挙動不一致のuBO独自演算子
        self.ubo_unsupported_ext_css: List[str] = [
            ':matches-path(', ':min-text-length(', ':watch-attr(', ':matches-media(', ':others()'
        ]

        # MV3/Android環境で未対応・エラーリスクとなるスクリプトレット
        self.incompatible_scriptlets: List[str] = [
            'acis', 'spoof-css', 'trusted-replace-argument', 'trusted-set-cookie',
            'alert-buster', 'trusted-click-element', 'webassembly-interference',
            'm3u-prune', 'json-prune', 'json-prune-set'
        ]

        # uBO独自修飾子のAdGuard互換置換マップ
        self.modifier_replacements: Dict[str, str] = {
            'queryprune': 'removeparam',
            'redirect-rule=': 'redirect=',
            '3p': 'third-party',
            '1p': '~third-party',
        }

        # 事前コンパイル済み正規表現 (処理速度向上・CPU負荷軽減)
        self.re_redos_check: Pattern = re.compile(
            r'(?:\.\*|\.\+){2,}|(?:\(?:[^)]*(?:\.\*|\.\+)[^)]*\)){2,}'
        )
        self.re_unsupported_to: Pattern = re.compile(r'(?:^|,)\~?to=(?:[^,]+|$)')
        self.re_cname: Pattern = re.compile(r'(?:^|,)cname(?=,|$)')
        self.re_multi_commas: Pattern = re.compile(r',+')

    def fetch_source(self) -> List[str]:
        req_headers = {'User-Agent': 'Mozilla/5.0 AdGuard-Optimizer/3.0'}
        for url in CANDIDATE_URLS:
            print(f"Fetch: {url}")
            try:
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, timeout=15) as res:
                    return res.read().decode('utf-8').splitlines()
            except (HTTPError, URLError) as e:
                print(f"  -> Failed: {e}")
            except Exception as e:
                print(f"  -> Error: {e}")

        print("Error: 元データの取得に失敗しました。")
        sys.exit(1)

    def _count_consecutive_backslashes(self, text: str, end_idx: int) -> int:
        count = 0
        idx = end_idx - 1
        while idx >= 0 and text[idx] == '\\':
            count += 1
            idx -= 1
        return count

    def _parse_regex_rule(self, line: str) -> Optional[Tuple[str, str, str]]:
        prefix = '@@' if line.startswith('@@') else ''
        check_line = line[len(prefix):]
        
        if not check_line.startswith('/'):
            return None

        idx = 1
        length = len(check_line)
        while idx < length:
            if check_line[idx] == '/':
                # バックスラッシュが偶数個ならエスケープされていない終端と判定
                if self._count_consecutive_backslashes(check_line, idx) % 2 == 0:
                    return (prefix, check_line[:idx + 1], check_line[idx + 1:])
            idx += 1
            
        return None

    def _contains_unsupported_backreference(self, pattern_str: str) -> bool:
        idx = 0
        length = len(pattern_str)
        while idx < length - 1:
            if pattern_str[idx] == '\\' and pattern_str[idx + 1].isdigit() and pattern_str[idx + 1] != '0':
                # バックスラッシュが奇数個なら本物の後方参照 (\1 ~ \9)
                if self._count_consecutive_backslashes(pattern_str, idx + 1) % 2 == 1:
                    return True
            idx += 1
        return False

    def optimize_line(self, line: str) -> Optional[str]:
        original_line = line
        line = line.strip()

        if not line or line.startswith('!'):
            return None

        # [Step A-1] 非互換なHTMLフィルタのパージ
        if '##^' in line or '#@#^' in line:
            return f"! [Unsupported HTML Filter] {original_line}"

        # スクリプトレットの互換性チェック
        if '##+js(' in line or '#@#+js(' in line:
            for bad_js in self.incompatible_scriptlets:
                if re.search(rf'\+js\(\s*{re.escape(bad_js)}(?:\s*|\s*[,)])', line):
                    return f"! [Incompatible Scriptlet] {original_line}"
            return line

        # [Step A-2] MV3 (RE2) および Android 向け正規表現検証
        regex_data = self._parse_regex_rule(line)
        if regex_data:
            prefix, regex_part, modifier_part = regex_data
            pattern_str = regex_part[1:-1]

            # RE2未サポート構文 (後読み・後方参照) のパージ
            if '(?<=' in pattern_str or '(?<!' in pattern_str or self._contains_unsupported_backreference(pattern_str):
                return f"! [Unsupported MV3 Regex] {original_line}"

            # ReDoS対策 (過剰なバックトラックのパージ)
            if self.re_redos_check.search(pattern_str):
                return f"! [High-Load Regex] {original_line}"

            line = f"{prefix}{regex_part}{modifier_part}"

        # [Step B] コスメティックフィルタの拡張CSS (#?#) 変換
        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts

                if any(unsupported in selector_part for unsupported in self.ubo_unsupported_ext_css):
                    return f"! [Unsupported Extended CSS] {original_line}"

                if any(ext in selector_part for ext in self.adg_supported_ext_css):
                    new_separator = '#?#' if separator == '##' else '#?@#'
                    return f"{domain_part}{new_separator}{selector_part}"
            return line

        # [Step C] ネットワークルールの修飾子最適化
        if '$' in line:
            regex_data = self._parse_regex_rule(line)
            if regex_data:
                prefix, regex_part, modifier_part = regex_data
                if not modifier_part.startswith('$'):
                    return line
                rule = f"{prefix}{regex_part}"
                modifiers_str = modifier_part[1:]
            else:
                if line.endswith('$'):
                    if '$' not in line[:-1]:
                        return line

                parts = line.rsplit('$', 1)
                if len(parts) != 2:
                    return line
                rule, modifiers_str = parts

                if not modifiers_str:
                    return f"{rule}$"

            # to= 修飾子のパージ
            if self.re_unsupported_to.search(modifiers_str):
                return f"! [Unsupported Modifier: to=] {original_line}"

            # cname 修飾子の除去
            modifiers_str = self.re_cname.sub('', modifiers_str)
            modifiers_str = modifiers_str.strip(',')
            modifiers_str = self.re_multi_commas.sub(',', modifiers_str)

            if not modifiers_str:
                return rule

            # 修飾子の置換 (境界条件の適用)
            for ubo_mod, adg_mod in self.modifier_replacements.items():
                modifiers_str = re.sub(
                    rf'(?:^|,){re.escape(ubo_mod)}(?=,|=|$)',
                    lambda m: m.group(0).replace(ubo_mod, adg_mod),
                    modifiers_str
                )

            return f"{rule}${modifiers_str}"

        return line

    def get_rule_signature(self, lines: List[str]) -> List[str]:
        return [l.strip() for l in lines if l.strip() and not l.strip().startswith('!')]

    def run(self) -> None:
        lines = self.fetch_source()
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

        # [Step D] スマート差分検知
        new_signature = self.get_rule_signature(optimized_lines)

        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                existing_lines = f.read().splitlines()
            
            if new_signature == self.get_rule_signature(existing_lines):
                print("変更なし: ファイルの更新をスキップしました。")
                return

        jst = timezone(timedelta(hours=+9), 'JST')
        current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

        # Descriptionを指定の内容に完全固定
        header = [
            "! Title: uB-filter-by-kdroidwin (AdGuard Optimized)",
            "! Description: Scam and malicious affiliate sites blocklist.",
            f"! Version: {current_version}",
            "! Syntax: AdGuard",
            "! Expires: 12 hours",
            "! License: GPL-3.0",
            "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
            "! Disclaimer: Unofficial fork optimized for AdGuard MV3 & Android.",
            ""
        ]

        output_dir = os.path.dirname(OUTPUT_FILE)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(header + optimized_lines) + '\n')

        print(f"完了: {OUTPUT_FILE} (v{current_version})")
        print(f"統計: 変換 {stats['converted']} | パージ {stats['commented']} | パス {stats['bypassed']}")


if __name__ == '__main__':
    AdGuardOptimizer().run()
