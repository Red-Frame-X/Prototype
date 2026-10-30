"""Haiagaruの固定環境・準備手順・報告テンプレートの不一致を防ぐ。"""
import re
import unittest
from pathlib import Path

GUIDE = Path(__file__).resolve().parents[1] / 'Markdown Notes/ChromeOS & Android Optimization Guide.md'


class HaiagaruFixedEnvironmentTests(unittest.TestCase):
    def test_versions_and_original_apk_code_are_consistent(self):
        text = GUIDE.read_text(encoding='utf-8')
        section = text.split('**Haiagaru-Morpheの動作検証・不具合報告（固定環境）**', 1)[1]
        section = section.split('## Linux Mint', 1)[0]
        environment = re.search(r'^2chMate (\S+ dev)/', section, re.MULTILINE).group(1)
        preparation = re.search(r'未改変のChMate `([^`]+)` APK（versionCode `(\d+)`）', section)
        report = re.search(r'^動作環境：2chMate (\S+ dev)/', section, re.MULTILINE).group(1)
        self.assertEqual(environment, preparation.group(1))
        self.assertEqual(environment, report)
        supported = dict(re.findall(r'\* \*\*([^*]+ dev)\*\*：[^\n]*versionCodeは(\d+)。', text))
        self.assertIn(environment, supported)
        self.assertEqual(preparation.group(2), supported[environment])


if __name__ == '__main__':
    unittest.main()
