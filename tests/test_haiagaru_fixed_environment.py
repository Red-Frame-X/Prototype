"""Haiagaruの固定環境・準備手順・報告テンプレートの不一致を防ぐ。"""
import re
import unittest
from pathlib import Path

GUIDE = Path(__file__).resolve().parents[1] / 'Markdown Notes/ChromeOS & Android Optimization Guide.md'


class HaiagaruFixedEnvironmentTests(unittest.TestCase):
    def required_match(self, pattern, text, label):
        match = re.search(pattern, text, re.MULTILINE)
        self.assertIsNotNone(match, f'{label}を読み取れません。ガイドの記載と検査の対応書式を確認してください。')
        return match

    def assert_consistent(self, text):
        # 太字の段落とMarkdown見出しの両方を扱い、本文中の言及は見出しとみなさない。
        title = 'Haiagaru-Morpheの動作検証・不具合報告（固定環境）'
        heading = self.required_match(
            r'^(?:\*\*' + re.escape(title) + r'\*\*|#{1,6}[ \t]+(?:'
            + re.escape(title) + r'|\*\*' + re.escape(title) + r'\*\*))[ \t]*$',
            text, '固定環境の見出し',
        )
        section = text[heading.end():]
        section = section.split('## Linux Mint', 1)[0]
        # Code spanや太字の有無で、Versionの意味は変わらない。
        section = section.replace('`', '').replace('**', '')
        environment = self.required_match(
            r'^2chMate (\d+(?:\.\d+)+ dev)/', section, '固定環境のChMate Version',
        ).group(1)
        preparation = self.required_match(
            r'未改変の(?:ChMate\s*)?(\d+(?:\.\d+)* dev)\s*APK\s*（versionCode\s+(\d+)）',
            section, '準備する元APKのVersionとversionCode',
        )
        report = self.required_match(
            r'^動作環境：2chMate (\d+(?:\.\d+)+ dev)/', section, '報告テンプレートのChMate Version',
        ).group(1)
        # 「242 dev」の省略表記だけを補完する。完全なVersion同士の違いは隠さない。
        prepared_version = preparation.group(1)
        if '.' not in prepared_version:
            prepared_version = environment.rsplit('.', 1)[0] + '.' + prepared_version
        self.assertEqual(environment, prepared_version, '固定環境と準備する元APKのVersionが異なります。')
        self.assertEqual(environment, report, '固定環境と報告テンプレートのVersionが異なります。')

        # 個別の箇条書きと、1行にまとめた対応一覧の両方を検査する。
        supported = self.required_match(
            re.escape(environment)
            + r'(?:：元APKのminSdkは\d+（[^）\n]+）、versionCodeは|（(?:versionCode\s+)?)(\d+)',
            text.replace('`', '').replace('**', ''), '対応一覧の元APKのversionCode',
        ).group(1)
        self.assertEqual(preparation.group(2), supported, '準備する元APKと対応一覧のversionCodeが異なります。')

    def test_versions_and_original_apk_code_are_consistent(self):
        self.assert_consistent(GUIDE.read_text(encoding='utf-8'))

    def fixture(self, compact):
        supported = (
            '* **対応ChMate**：0.8.10.226 dev（494・Android 6.0以降）、0.8.10.242 dev（512・Android 6.0以降）。'
            if compact else
            '* **0.8.10.242 dev**：元APKのminSdkは23（Android 6.0以降）、versionCodeは512。'
        )
        preparation = (
            '未改変の242 dev APK（versionCode 512）'
            if compact else
            '未改変のChMate `0.8.10.242 dev` APK（versionCode `512`）'
        )
        return '\n'.join((
            supported,
            '**Haiagaru-Morpheの動作検証・不具合報告（固定環境）**',
            '2chMate 0.8.10.242 dev/Google/Pixel 10a/17/DT/Haiagaru x.xx.x',
            preparation,
            '動作環境：2chMate 0.8.10.242 dev/Google/Pixel 10a/17/DT/Haiagaru x.xx.x',
            '## Linux Mint',
        ))

    def test_both_document_layouts_are_supported(self):
        for compact in (False, True):
            with self.subTest(compact=compact):
                self.assert_consistent(self.fixture(compact))

    def test_heading_formats_preserve_validation(self):
        title = 'Haiagaru-Morpheの動作検証・不具合報告（固定環境）'
        for compact in (False, True):
            for heading in ('**' + title + '**', '### ' + title, '### **' + title + '**'):
                text = self.fixture(compact).replace('**' + title + '**', heading)
                with self.subTest(compact=compact, heading=heading):
                    self.assert_consistent(text)
                    # 表示形式を変えても実際のVersion不一致は拒否する。
                    with self.assertRaisesRegex(AssertionError, 'テンプレートのVersionが異なります'):
                        self.assert_consistent(text.replace(
                            '動作環境：2chMate 0.8.10.242', '動作環境：2chMate 0.8.10.226',
                        ))
                    with self.assertRaisesRegex(AssertionError, 'versionCodeが異なります'):
                        self.assert_consistent(text.replace('512', '999', 1))
                    with self.assertRaisesRegex(AssertionError, '読み取れません'):
                        self.assert_consistent(text.replace(heading, '本文中の言及：' + title))

    def test_inconsistent_versions_and_codes_fail(self):
        for compact in (False, True):
            text = self.fixture(compact)
            preparation = '未改変の242 dev' if compact else '未改変のChMate `0.8.10.242 dev'
            for old, new, message in (
                (preparation, preparation.replace('242', '226'), '元APKのVersionが異なります'),
                (preparation, preparation.replace('242', '243'), '元APKのVersionが異なります'),
                ('動作環境：2chMate 0.8.10.242', '動作環境：2chMate 0.8.10.226', 'テンプレートのVersionが異なります'),
                ('512', '999', 'versionCodeが異なります'),
            ):
                with self.subTest(compact=compact, replacement=(old, new)):
                    with self.assertRaisesRegex(AssertionError, message):
                        self.assert_consistent(text.replace(old, new, 1))

    def test_missing_fields_fail_with_a_useful_message(self):
        for field in ('**Haiagaru-Morpheの動作検証・不具合報告（固定環境）**',
                      '2chMate 0.8.10.242 dev/', '未改変の242 dev APK（versionCode 512）',
                      '動作環境：', '0.8.10.242 dev（512・Android 6.0以降）'):
            with self.subTest(field=field):
                with self.assertRaisesRegex(AssertionError, 'ありません|読み取れません'):
                    self.assert_consistent(self.fixture(True).replace(field, '', 1))


if __name__ == '__main__':
    unittest.main()
