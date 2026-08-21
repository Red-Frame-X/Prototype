import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "translate_changelog.py"
SPEC = importlib.util.spec_from_file_location("translate_changelog", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)


class MarkdownTranslationTests(unittest.TestCase):
    def test_preserves_urls_inline_code_and_fenced_code(self):
        source = """# Changelog

- Added `$removeparam` support. See https://example.com/docs.

```text
||example.com^$removeparam
```
"""
        translated = module.translate_markdown(
            source,
            lambda text: text.replace("Changelog", "変更履歴")
            .replace("Added", "追加")
            .replace("support", "対応")
            .replace("See", "参照"),
            {},
        )
        self.assertIn("# 変更履歴", translated)
        self.assertIn("`$removeparam`", translated)
        self.assertIn("https://example.com/docs", translated)
        self.assertIn("||example.com^$removeparam", translated)

    def test_reference_definition_is_not_translated(self):
        line = "[issue]: https://github.com/example/repo/issues/1"
        self.assertEqual(module.translate_line(line, lambda text: "broken", {}), line)

    def test_markdown_prefix_is_preserved_when_engine_drops_it(self):
        self.assertEqual(
            module.translate_line("## Changed", lambda text: "変更", {}),
            "## 変更",
        )

    def test_translation_cache_avoids_duplicate_calls(self):
        calls = []

        def translator(text):
            calls.append(text)
            return "翻訳"

        cache = {}
        first = module.translate_line("Same text", translator, cache)
        second = module.translate_line("Same text", translator, cache)
        self.assertEqual(first, second)
        self.assertEqual(len(calls), 1)

    def test_update_writes_japanese_output_and_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source.md"
            output = base / "ja.md"
            cache = base / "cache.json"
            source.write_text("# Changelog\n", encoding="utf-8")
            self.assertTrue(
                module.update(
                    source,
                    output,
                    cache,
                    lambda text: text.replace("Changelog", "変更履歴"),
                )
            )
            self.assertEqual(output.read_text(encoding="utf-8"), "# 変更履歴\n")
            payload = json.loads(cache.read_text(encoding="utf-8"))
            self.assertEqual(payload["engine"], module.ENGINE)


if __name__ == "__main__":
    unittest.main()
