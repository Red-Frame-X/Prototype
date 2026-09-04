#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uB-filter-by-kdroidwin (AdGuard Optimized) generator and linter.

uBlock Origin用フィルタをAdGuard for Chrome MV3向けに、安全性と互換性を優先して
変換・静的解析(Lint)するスクリプト。生成物はAdGuard for Androidでも読み込めますが、
CoreLibs固有機能の保持やAndroid向けの完全な最適化は保証しません。

License: GPL-3.0
Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Pattern, Tuple
from urllib.error import HTTPError, URLError

# スクリプト自身の場所を基準にプロジェクトルートと出力先パスを確定
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILTER_NAME: str = "uB-filter-by-kdroidwin (AdGuard Optimized)"
OUTPUT_FILE: str = os.path.join(BASE_DIR, "dist", f"{FILTER_NAME}.txt")
CAPABILITY_FILE: str = os.path.join(BASE_DIR, "config", "adguard-converter-capabilities.json")
CAPABILITY_TARGET: str = "adguard-browser-extension-mv3"

CANDIDATE_URLS: List[str] = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/refs/heads/main/uBlockorigin.txt",
    "https://cdn.jsdelivr.net/gh/Kdroidwin/uB-filter-by-kdroidwin@main/uBlockorigin.txt"
]


class AdGuardOptimizer:
    def __init__(self, capability_file: str = CAPABILITY_FILE) -> None:
        settings = self._load_converter_settings(capability_file)

        # AdGuard拡張CSSでJS解析が必須な疑似クラス (:is, :not, :where は標準CSSで処理可能なため除外)
        self.adg_supported_ext_css: List[str] = settings["adguard_extended_css"]

        # AdGuard未対応・挙動不一致のuBO独自演算子
        self.ubo_unsupported_ext_css: List[str] = settings["unsupported_ubo_extended_css"]

        # Chrome MV3向け出力で未対応・エラーリスクとなるスクリプトレット
        self.incompatible_scriptlets: List[str] = settings["incompatible_scriptlets"]

        # uBO独自修飾子のAdGuard互換置換マップ
        self.modifier_replacements: Dict[str, str] = settings["modifier_replacements"]

        # 事前コンパイル済み正規表現 (処理速度向上・CPU負荷軽減)
        self.re_redos_check: Pattern = re.compile(
            r'(?:\.\*|\.\+){2,}|(?:\(?:[^)]*(?:\.\*|\.\+)[^)]*\)){2,}'
        )
        self.re_cname: Pattern = re.compile(r'(?:^|,)cname(?=,|$)')
        self.re_multi_commas: Pattern = re.compile(r',+')

        # スクリプトレット検知用正規表現の事前構築
        scriptlets_escaped = [re.escape(s) for s in self.incompatible_scriptlets]
        self.re_incompatible_js: Pattern = re.compile(
            rf'\+js\(\s*(?:{"|".join(scriptlets_escaped)})(?=\s*(?:,|\)))'
        )

    @staticmethod
    def _load_converter_settings(capability_file: str) -> Dict[str, object]:
        """Load reviewed converter behavior from the repository capability profile.

        The capability profile is the single source of truth for data-like
        compatibility decisions. Invalid or incomplete settings fail fast so a
        CI run cannot silently fall back to stale hard-coded behavior.
        """
        with open(capability_file, 'r', encoding='utf-8') as f:
            profile = json.load(f)

        try:
            target = profile["targets"][CAPABILITY_TARGET]
            settings = target["converter_settings"]
        except (KeyError, TypeError) as e:
            raise ValueError(
                f"Invalid capability profile: missing {CAPABILITY_TARGET} converter settings"
            ) from e

        list_keys = (
            "adguard_extended_css",
            "unsupported_ubo_extended_css",
            "incompatible_scriptlets",
        )
        for key in list_keys:
            value = settings.get(key)
            if not isinstance(value, list) or not value or not all(isinstance(item, str) for item in value):
                raise ValueError(f"Invalid capability profile: {key} must be a non-empty string list")

        replacements = settings.get("modifier_replacements")
        if (
            not isinstance(replacements, dict)
            or not replacements
            or not all(isinstance(k, str) and isinstance(v, str) for k, v in replacements.items())
        ):
            raise ValueError(
                "Invalid capability profile: modifier_replacements must be a non-empty string map"
            )

        return {
            "adguard_extended_css": list(settings["adguard_extended_css"]),
            "unsupported_ubo_extended_css": list(settings["unsupported_ubo_extended_css"]),
            "incompatible_scriptlets": list(settings["incompatible_scriptlets"]),
            "modifier_replacements": dict(replacements),
        }

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
        in_character_class = False
        normalized_pattern: List[str] = ['/']

        while idx < length:
            char = check_line[idx]
            is_escaped = self._count_consecutive_backslashes(check_line, idx) % 2 == 1

            if char == '[' and not is_escaped:
                in_character_class = True
            elif char == ']' and not is_escaped:
                in_character_class = False
            elif char == '/' and not is_escaped:
                if in_character_class:
                    # AdGuardの /.../ 区切りで文字クラス内の / が終端と誤認されないよう正規化
                    normalized_pattern.append(r'\/')
                    idx += 1
                    continue

                normalized_pattern.append('/')
                return prefix, ''.join(normalized_pattern), check_line[idx + 1:]
            normalized_pattern.append(char)
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

    def _contains_embedded_end_anchor(self, pattern_str: str) -> bool:
        """Return whether an unescaped $ anchor appears before the pattern end.

        AGLint interprets an embedded ``$`` followed by regex tokens (for example
        ``(?:/|$)``) as the start of AdGuard modifiers when the rule has no real
        modifier section.  The affected source rules are document URL rules, so
        adding an explicit ``$document`` modifier removes the ambiguity without
        changing which top-level navigations they block.
        """
        in_character_class = False
        for idx, char in enumerate(pattern_str):
            is_escaped = self._count_consecutive_backslashes(pattern_str, idx) % 2 == 1
            if char == '[' and not is_escaped:
                in_character_class = True
            elif char == ']' and not is_escaped:
                in_character_class = False
            elif char == '$' and not is_escaped and not in_character_class:
                if idx != len(pattern_str) - 1:
                    return True
        return False

    def optimize_line(self, line: str) -> Optional[str]:
        original_line = line.strip()
        line = original_line

        if not line or line.startswith('!'):
            return None

        # [Step A-1] 非互換なHTMLフィルタのパージ
        if '##^' in line or '#@#^' in line:
            return f"! [Unsupported HTML Filter] {original_line}"

        # スクリプトレットの互換性チェック
        if '##+js(' in line or '#@#+js(' in line:
            if self.re_incompatible_js.search(line):
                return f"! [Incompatible Scriptlet] {original_line}"
            return line

        # [Step A-2] Chrome MV3 (RE2) との互換性を優先した正規表現検証
        regex_data = self._parse_regex_rule(line)
        if regex_data:
            prefix, regex_part, modifier_part = regex_data
            pattern_str = regex_part[1:-1]

            # RE2未サポート構文 (先読み・後読み・後方参照) のパージ
            if (
                '(?=' in pattern_str
                or '(?!' in pattern_str
                or '(?<=' in pattern_str
                or '(?<!' in pattern_str
                or self._contains_unsupported_backreference(pattern_str)
            ):
                return f"! [Unsupported MV3 Regex] {original_line}"

            # ReDoS対策 (過剰なバックトラックのパージ)
            if self.re_redos_check.search(pattern_str):
                return f"! [High-Load Regex] {original_line}"

            # Bare regex rules containing an embedded end anchor are ambiguous
            # to AGLint (it treats the anchor as the modifier separator).
            if not modifier_part and self._contains_embedded_end_anchor(pattern_str):
                modifier_part = '$document'

            line = f"{prefix}{regex_part}{modifier_part}"

        # [Step B] コスメティックフィルタの拡張CSS (#?#) 変換
        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts
                rule_scope = domain_part

                # パス付きドメイン指定を、Chrome MV3対応の非基本 $url 修飾子へ変換する。
                # ドメインだけに丸めると適用範囲が広がるため、必ず元のパスを維持する。
                if '/' in domain_part:
                    if ',' in domain_part:
                        return f"! [Unsupported Mixed Cosmetic URL Scope] {original_line}"

                    domain, path = domain_part.split('/', 1)
                    if not domain or not path:
                        return f"! [Invalid Cosmetic URL Scope] {original_line}"

                    rule_scope = f"[$url=||{domain}/{path}*]"

                if any(unsupported in selector_part for unsupported in self.ubo_unsupported_ext_css):
                    return f"! [Unsupported Extended CSS] {original_line}"

                if any(ext in selector_part for ext in self.adg_supported_ext_css):
                    new_separator = '#?#' if separator == '##' else '#?@#'
                    return f"{rule_scope}{new_separator}{selector_part}"
                return f"{rule_scope}{separator}{selector_part}"
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

            # redirect-rule は別の基本ルールでブロックされた場合だけリダイレクトする。
            # Chrome MV3で未対応だからといって redirect へ変換すると適用範囲が広がるため、
            # 意味を安全に維持できないルールは無効化する。
            if re.search(r'(?:^|,)~?redirect-rule(?:=|,|$)', modifiers_str):
                return f"! [Unsupported MV3 Modifier: redirect-rule] {original_line}"

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
                print("変更なし: ルール本体に差分がないため、ファイルの更新をスキップしました。")
                return

        jst = timezone(timedelta(hours=+9), 'JST')
        current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

        header = [
            f"! Title: {FILTER_NAME}",
            "! Description: Scam and malicious affiliate sites blocklist.",
            f"! Version: {current_version}",
            "! Syntax: AdGuard",
            "! Expires: 12 hours",
            "! Homepage: https://github.com/Red-Frame-X/Prototype",
            "! License: GPL-3.0",
            "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
            "! Disclaimer: Unofficial fork optimized primarily for AdGuard for Chrome MV3.",
            "! Compatibility: AdGuard for Android is supported on a best-effort basis; CoreLibs-specific features may be omitted.",
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