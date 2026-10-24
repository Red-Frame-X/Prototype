#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uB-filter-by-kdroidwin (AdGuard Optimized) の生成・Lintスクリプト。

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
FILTER_TITLE: str = FILTER_NAME
OUTPUT_FILE: str = os.path.join(BASE_DIR, "dist", f"{FILTER_NAME}.txt")
CAPABILITY_FILE: str = os.path.join(BASE_DIR, "config", "adguard-converter-capabilities.json")
CAPABILITY_TARGET: str = "adguard-browser-extension-mv3"
# Repositoryの慎重な運用方針に合わせ、大幅な減少の確認基準を設定する。
# 意図した大幅な削減でも、自動的に許可せずレビューを必要とする。
MAX_RULE_NET_LOSS: int = 120

CANDIDATE_URLS: List[str] = [
    "https://raw.githubusercontent.com/Kdroidwin/uB-filter-by-kdroidwin/refs/heads/main/uBlockorigin.txt",
    "https://cdn.jsdelivr.net/gh/Kdroidwin/uB-filter-by-kdroidwin@main/uBlockorigin.txt"
]


class AdGuardOptimizer:
    def __init__(self, capability_file: str = CAPABILITY_FILE) -> None:
        settings = self._load_converter_settings(capability_file)

        # AdGuard拡張CSSでJS解析が必須な疑似クラス (:is, :not, :where は標準CSSで処理可能なため除外)
        self.adg_supported_ext_css: List[str] = settings["adguard_extended_css"]
        self.ubo_unsupported_ext_css: List[str] = settings["unsupported_ubo_extended_css"]

        # uBO構文からAdGuardへ意味を安全に維持できると確認できていないスクリプトレット。
        # AdGuard MV3自体のscriptlet対応可否とは分離し、推測変換による挙動変更を防ぐ。
        self.compatible_scriptlets: List[str] = settings["compatible_scriptlets"]
        self.incompatible_scriptlets: List[str] = settings["incompatible_scriptlets"]

        # uBO独自演算子のAdGuard互換置換マップ
        self.modifier_replacements: Dict[str, str] = settings["modifier_replacements"]

        # 事前コンパイル済み正規表現 (処理速度向上・CPU負荷軽減)
        self.re_redos_check: Pattern = re.compile(
            r'(?:\.\*|\.\+){2,}|(?:\(?:[^)]*(?:\.\*|\.\+)[^)]*\)){2,}'
        )
        self.re_multi_commas: Pattern = re.compile(r',+')

        # スクリプトレット検知用正規表現の事前構築
        scriptlets_escaped = [re.escape(s) for s in self.incompatible_scriptlets]
        self.re_incompatible_js: Pattern = re.compile(
            rf'\+js\(\s*(?:{"|".join(scriptlets_escaped)})(?=\s*(?:,|\)))'
        )
        compatible_scriptlets_escaped = [re.escape(s) for s in self.compatible_scriptlets]
        self.re_compatible_js: Pattern = re.compile(
            rf'\+js\(\s*(?:{"|".join(compatible_scriptlets_escaped)})(?=\s*(?:,|\)))'
        )

    @staticmethod
    def _load_converter_settings(capability_file: str) -> Dict[str, object]:
        """査読済みの互換性プロファイルから変換設定を読み込む。

        データ形式の互換性判断はこのプロファイルを唯一の基準とする。
        不正または不足した設定は即時に失敗させ、古いハードコードへ
        暗黙にフォールバックしないようにする。
        """
        with open(capability_file, 'r', encoding='utf-8') as f:
            profile = json.load(f)

        try:
            target = profile["targets"][CAPABILITY_TARGET]
            settings = target["converter_settings"]
        except (KeyError, TypeError) as e:
            raise ValueError(
                f"対応機能プロファイルが不正です: {CAPABILITY_TARGET}の変換設定がありません"
            ) from e

        list_keys = (
            "adguard_extended_css",
            "unsupported_ubo_extended_css",
            "compatible_scriptlets",
            "incompatible_scriptlets",
        )
        for key in list_keys:
            value = settings.get(key)
            if not isinstance(value, list) or not value or not all(isinstance(item, str) for item in value):
                raise ValueError(f"対応機能プロファイルが不正です: {key}には空でない文字列リストが必要です")

        replacements = settings.get("modifier_replacements")
        if (
            not isinstance(replacements, dict)
            or not replacements
            or not all(isinstance(k, str) and isinstance(v, str) for k, v in replacements.items())
        ):
            raise ValueError(
                "対応機能プロファイルが不正です: modifier_replacementsには空でない文字列マッピングが必要です"
            )

        return {
            "adguard_extended_css": list(settings["adguard_extended_css"]),
            "unsupported_ubo_extended_css": list(settings["unsupported_ubo_extended_css"]),
            "compatible_scriptlets": list(settings["compatible_scriptlets"]),
            "incompatible_scriptlets": list(settings["incompatible_scriptlets"]),
            "modifier_replacements": dict(replacements),
        }

    def fetch_source(self) -> List[str]:
        req_headers = {'User-Agent': 'Mozilla/5.0 AdGuard-Optimizer/3.0'}
        for url in CANDIDATE_URLS:
            print(f"取得先: {url}")
            try:
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, timeout=15) as res:
                    lines = res.read().decode('utf-8-sig').splitlines()
                    if not self.get_rule_signature(lines):
                        raise ValueError("変換元に有効ルールがありません")
                    return lines
            except (HTTPError, URLError, TimeoutError, UnicodeDecodeError) as e:
                print(f"  -> 失敗: {e}")
            except ValueError as e:
                print(f"  -> 変換元が不正です: {e}")

        print("エラー: 元データの取得に失敗しました。")
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
                    normalized_pattern.append(r'\/')
                    idx += 1
                    continue

                # 正規表現中の候補となる `/` の直後が modifier 開始、行末、
                # または正規表現として自然な終端である場合だけ区切りとみなす。
                rest = check_line[idx + 1:]
                if rest and not rest.startswith('$') and re.match(r'[|)$?*+\]}]', rest[0]):
                    normalized_pattern.append('/')
                    idx += 1
                    continue

                normalized_pattern.append('/')
                return prefix, ''.join(normalized_pattern), rest
            normalized_pattern.append(char)
            idx += 1

        return None

    def _contains_unsupported_backreference(self, pattern_str: str) -> bool:
        """RE2非互換の未エスケープ後方参照が含まれるか判定する。"""
        idx = 0
        length = len(pattern_str)
        while idx < length:
            if pattern_str[idx] != '\\':
                idx += 1
                continue

            run_end = idx
            while run_end < length and pattern_str[run_end] == '\\':
                run_end += 1

            if (run_end - idx) % 2 == 1 and run_end < length:
                token_start = pattern_str[run_end]
                if token_start in '123456789gk':
                    return True

            idx = run_end
        return False

    def _contains_embedded_end_anchor(self, pattern_str: str) -> bool:
        """正規表現末尾より前に未エスケープの``$``アンカーがあるか判定する。

        AGLintの誤検知を限定的に抑制するためだけに使用する。
        リソース種別や例外ルールの意味は変更しない。
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

    @staticmethod
    def _rewrite_re2_safe_lookahead(pattern_str: str) -> str:
        """意味を厳密に維持できる既知の先読みだけRE2互換形へ変換する。

        `pay` 以降かつスラッシュ以前に数字が3個以上存在することを確認する
        positive lookahead は、同じ範囲を実際に消費する表現へ展開できる。
        一般のlookaroundを推測変換すると一致集合が変わり得るため扱わない。
        """
        digit_triplet_lookahead = r'(?=[^\/]*\d[^\/]*\d[^\/]*\d)[^\/]*\.com'
        digit_triplet_consuming = r'[^\/]*\d[^\/]*\d[^\/]*\d[^\/]*\.com'
        return pattern_str.replace(digit_triplet_lookahead, digit_triplet_consuming)

    def optimize_line(self, line: str) -> Optional[str]:
        original_line = line.strip()
        line = original_line

        if not line or line.startswith('!'):
            return None

        if '##^' in line or '#@#^' in line:
            return f"! [未対応のHTMLフィルター] {original_line}"

        if '##+js(' in line or '#@#+js(' in line:
            if self.re_incompatible_js.search(line):
                return f"! [互換性のないスクリプトレット] {original_line}"
            if not self.re_compatible_js.search(line):
                return f"! [未検証のスクリプトレット] {original_line}"
            return line

        regex_data = self._parse_regex_rule(line)
        if regex_data:
            prefix, regex_part, modifier_part = regex_data
            pattern_str = regex_part[1:-1]

            rewritten_pattern = self._rewrite_re2_safe_lookahead(pattern_str)
            if rewritten_pattern != pattern_str:
                pattern_str = rewritten_pattern
                regex_part = f"/{pattern_str}/"

            if (
                '(?=' in pattern_str
                or '(?!' in pattern_str
                or '(?<=' in pattern_str
                or '(?<!' in pattern_str
                or self._contains_unsupported_backreference(pattern_str)
            ):
                return f"! [MV3未対応の正規表現] {original_line}"

            if self.re_redos_check.search(pattern_str):
                return f"! [高負荷の正規表現] {original_line}"

            line = f"{prefix}{regex_part}{modifier_part}"

        if '##' in line or '#@#' in line:
            separator = '##' if '##' in line else '#@#'
            parts = line.split(separator, 1)
            if len(parts) == 2:
                domain_part, selector_part = parts
                rule_scope = domain_part

                if '/' in domain_part:
                    if ',' in domain_part:
                        return f"! [未対応の混在する要素非表示URL範囲] {original_line}"
                    rule_scope = f"[$url=||{domain_part}*]"

                if any(p in selector_part for p in self.ubo_unsupported_ext_css):
                    return f"! [未対応の拡張CSS] {original_line}"

                if any(p in selector_part for p in self.adg_supported_ext_css):
                    separator = '#?#' if separator == '##' else '#@?#'

                line = f"{rule_scope}{separator}{selector_part}"

        if '$' in line:
            regex_data = self._parse_regex_rule(line)
            if regex_data:
                prefix, regex_part, modifiers_str = regex_data
                rule = f"{prefix}{regex_part}"
                if modifiers_str.startswith('$'):
                    modifiers_str = modifiers_str[1:]
                elif not modifiers_str:
                    return line
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

            if re.search(r'(?:^|,)~?redirect-rule(?:=|,|$)', modifiers_str):
                return f"! [MV3未対応の修飾子: redirect-rule] {original_line}"

            if re.search(r'(?:^|,)~?cname(?:=|,|$)', modifiers_str):
                return f"! [MV3未対応の修飾子: cname] {original_line}"
            modifiers_str = modifiers_str.strip(',')
            modifiers_str = self.re_multi_commas.sub(',', modifiers_str)

            if not modifiers_str:
                return rule

            for ubo_mod, adg_mod in self.modifier_replacements.items():
                modifiers_str = re.sub(
                    rf'(?:^|,){re.escape(ubo_mod)}(?=,|=|$)',
                    lambda m: m.group(0).replace(ubo_mod, adg_mod),
                    modifiers_str
                )

            return f"{rule}${modifiers_str}"

        return line

    def get_rule_signature(self, lines: List[str]) -> List[str]:
        return [
            l.strip() for l in lines
            if l.strip() and not l.strip().startswith('!')
            and not re.fullmatch(r'\[Adblock(?: Plus)?(?: \d+(?:\.\d+)*)?\]', l.strip())
        ]

    def run(self) -> None:
        lines = self.fetch_source()
        stats = {"converted": 0, "bypassed": 0, "commented": 0}
        optimized_lines: List[str] = []

        for line in lines:
            optimized = self.optimize_line(line)
            if optimized is None:
                continue

            regex_data = self._parse_regex_rule(optimized)
            if (regex_data and not regex_data[2]
                    and self._contains_embedded_end_anchor(regex_data[1][1:-1])):
                optimized_lines.append('! aglint-disable-next-line invalid-modifiers')
            optimized_lines.append(optimized)

            if optimized != line and not optimized.startswith('! ['):
                stats["converted"] += 1
            elif optimized.startswith('! ['):
                stats["commented"] += 1
            else:
                stats["bypassed"] += 1

        new_signature = self.get_rule_signature(optimized_lines)
        if not new_signature:
            raise ValueError("有効ルールがない生成フィルターは書き込みません")
        expected_metadata = [
            f"! Title: {FILTER_TITLE}",
            "! Description: 詐欺・悪質アフィリエイトサイト向けブロックリスト。",
            "! Syntax: AdGuard",
            "! Expires: 12 hours",
            "! Homepage: https://github.com/Red-Frame-X/Prototype",
            "! License: GPL-3.0",
            "! Original Source: https://github.com/Kdroidwin/uB-filter-by-kdroidwin",
            "! Note: このフィルタは、AdGuard Browser Extension MV3 向けに最適化した非公式フォークです。",
            "! Compatibility: AdGuard for Androidはベストエフォート対応。CoreLibs固有機能は省略される場合があります。",
        ]

        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                existing_lines = f.read().splitlines()

            existing_signature = self.get_rule_signature(existing_lines)
            net_loss = len(existing_signature) - len(new_signature)
            if net_loss >= MAX_RULE_NET_LOSS:
                raise ValueError(
                    f"有効ルールの大幅な減少を拒否しました: {len(existing_signature)} -> "
                    f"{len(new_signature)}（純減 {net_loss}、基準 {MAX_RULE_NET_LOSS}）。"
                    "既存の出力を保持しました。公開する前に上流の変更を確認してください。"
                )

            metadata_matches = all(line in existing_lines[:12] for line in expected_metadata)
            if new_signature == self.get_rule_signature(existing_lines) and metadata_matches:
                print("変更なし: ルール本体と固定Metadataに差分がないため、ファイルの更新をスキップしました。")
                return

        jst = timezone(timedelta(hours=+9), 'JST')
        current_version = datetime.now(jst).strftime('%Y%m%d%H%M')

        header = [
            expected_metadata[0],
            expected_metadata[1],
            f"! Version: {current_version}",
            *expected_metadata[2:],
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
