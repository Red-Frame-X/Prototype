"""モデル未取得時の保存省略と、別Runから復元したarchiveの厳格な検証。"""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_argos_model_cache import check_cache


class ArchiveValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.manifest = self.root / 'manifest.json'
        self.cache = self.root / 'cache'
        self.cache.mkdir()

    def archive(self, metadata=None, extra_name=None):
        temporary = self.root / 'fixture.zip'
        with zipfile.ZipFile(temporary, 'w') as archive:
            archive.writestr('translate-en_ja-1_1/metadata.json', json.dumps(metadata or {
                'from_code': 'en', 'to_code': 'ja', 'package_version': '1.1'}))
            if extra_name:
                archive.writestr(extra_name, 'invalid')
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        target = self.cache / (digest + '.argosmodel')
        temporary.replace(target)
        self.manifest.write_text(json.dumps({'sha256': digest, 'license_verified': True}))
        return target

    def test_valid_restored_archive_is_ready_without_downloading(self):
        self.archive()
        self.assertTrue(check_cache(self.manifest, self.cache, required=True))

    def test_absent_archive_is_skipped_only_when_optional(self):
        self.manifest.write_text(json.dumps({'sha256': 'a' * 64, 'license_verified': True}))
        self.assertFalse(check_cache(self.manifest, self.cache))
        with self.assertRaisesRegex(ValueError, '復元されていません'):
            check_cache(self.manifest, self.cache, required=True)
        self.assertEqual(list(self.cache.iterdir()), [])

    def test_corrupt_archive_is_never_saved_or_accepted(self):
        target = self.archive()
        target.write_bytes(b'corrupt')
        with self.assertRaisesRegex(ValueError, 'SHA256'):
            check_cache(self.manifest, self.cache)

    def test_wrong_language_version_and_path_fail_even_with_valid_hash(self):
        for metadata, name in (({'from_code': 'en', 'to_code': 'fr', 'package_version': '1.1'}, None),
                               ({'from_code': 'en', 'to_code': 'ja', 'package_version': '2.0'}, None),
                               (None, '../escape.txt')):
            with self.subTest(metadata=metadata, name=name):
                self.archive(metadata, name)
                with self.assertRaises(ValueError):
                    check_cache(self.manifest, self.cache, required=True)

    def test_unverified_manifest_is_rejected_before_cache_lookup(self):
        for manifest in ({'sha256': '../invalid', 'license_verified': True},
                         {'sha256': 'a' * 64, 'license_verified': False}):
            with self.subTest(manifest=manifest):
                self.manifest.write_text(json.dumps(manifest))
                with self.assertRaises(ValueError):
                    check_cache(self.manifest, self.cache)


if __name__ == '__main__':
    unittest.main()
