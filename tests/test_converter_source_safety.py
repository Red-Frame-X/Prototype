"""Invalid upstream content must never replace a usable generated filter."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts.convert import AdGuardOptimizer, CANDIDATE_URLS, MAX_RULE_NET_LOSS


def response(body):
    result = MagicMock()
    result.__enter__.return_value.read.return_value = body
    return result


class ConverterSourceSafetyTests(unittest.TestCase):
    def setUp(self):
        self.optimizer = AdGuardOptimizer()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / "filter.txt"
        self.original = ("! Previous output\n" + "".join(
            f"||host{i}.example^\n" for i in range(200)
        )).encode()
        self.output.write_bytes(self.original)
        patcher = patch("scripts.convert.OUTPUT_FILE", str(self.output))
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_invalid_primary_uses_fallback(self):
        for invalid in (b"", b" \n\t", b"! Title: empty\n", b"[Adblock Plus 2.0]\n! comment\n", b"\xef\xbb\xbf! comment\n"):
            with self.subTest(body=invalid), patch(
                "scripts.convert.urllib.request.urlopen",
                side_effect=[response(invalid), response(b"||valid.example^\n")],
            ) as fetch:
                self.assertEqual(self.optimizer.fetch_source(), ["||valid.example^"])
                self.assertEqual([c.args[0].full_url for c in fetch.call_args_list], CANDIDATE_URLS)

    def test_all_invalid_sources_fail_without_changing_output(self):
        with patch("scripts.convert.urllib.request.urlopen", return_value=response(b"! empty\n")) as fetch:
            with self.assertRaises(SystemExit) as error:
                self.optimizer.run()
        self.assertEqual(error.exception.code, 1)
        self.assertEqual(fetch.call_count, len(CANDIDATE_URLS))
        self.assertEqual(self.output.read_bytes(), self.original)

    def test_empty_converted_output_is_rejected_before_writing(self):
        for lines in ([], ["! comment"], ["[Adblock Plus 2.0]"], ["example.com##^script"]):
            with self.subTest(lines=lines), patch.object(self.optimizer, "fetch_source", return_value=lines):
                with self.assertRaisesRegex(ValueError, "no active rules"):
                    self.optimizer.run()
                self.assertEqual(self.output.read_bytes(), self.original)

    def test_substantial_loss_boundary_preserves_existing_bytes(self):
        for loss in (MAX_RULE_NET_LOSS, MAX_RULE_NET_LOSS + 1, 199):
            lines = [f"||host{i}.example^" for i in range(200 - loss)]
            with self.subTest(loss=loss), patch.object(self.optimizer, "fetch_source", return_value=lines):
                with self.assertRaisesRegex(ValueError, "substantial active-rule loss"):
                    self.optimizer.run()
                self.assertEqual(self.output.read_bytes(), self.original)

    def test_below_loss_threshold_is_allowed(self):
        lines = [f"||host{i}.example^" for i in range(200 - MAX_RULE_NET_LOSS + 1)]
        with patch.object(self.optimizer, "fetch_source", return_value=lines):
            self.optimizer.run()
        self.assertEqual(self.optimizer.get_rule_signature(self.output.read_text().splitlines()), lines)

    def test_valid_fallback_can_generate_and_repeat_without_changes(self):
        with patch("scripts.convert.urllib.request.urlopen", side_effect=[response(b""), response(self.original)]):
            self.optimizer.run()
        generated = self.output.read_bytes()
        with patch("scripts.convert.urllib.request.urlopen", return_value=response(self.original)):
            self.optimizer.run()
        self.assertEqual(self.output.read_bytes(), generated)
        self.assertEqual(len(self.optimizer.get_rule_signature(generated.decode().splitlines())), 200)

    def test_invalid_first_generation_does_not_create_output(self):
        missing = Path(self.temp.name) / "new.txt"
        with patch("scripts.convert.OUTPUT_FILE", str(missing)), patch.object(self.optimizer, "fetch_source", return_value=[]):
            with self.assertRaises(ValueError):
                self.optimizer.run()
        self.assertFalse(missing.exists())

    def test_non_basic_url_scoped_rule_is_active(self):
        rule = "[$url=||example.com/path*]##.ad"
        self.assertEqual(self.optimizer.get_rule_signature([rule]), [rule])
