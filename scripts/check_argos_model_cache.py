#!/usr/bin/env python3
"""取得やインストールをせず、固定モデルのcacheが保存・再利用可能か確認する。"""
import argparse
import json
import os
from pathlib import Path
import re
import zipfile

from argos_commit_translation import archive_digest


def check_cache(manifest_path, directory, required=False):
    manifest = json.loads(Path(manifest_path).read_text())
    digest = manifest.get('sha256')
    if (not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest)
            or manifest.get('license_verified') is not True):
        raise ValueError('固定モデルのhash・ライセンス確認情報が不正です。')
    archive = Path(directory) / (digest + '.argosmodel')
    if not archive.is_file():
        if required:
            raise ValueError('固定モデルのcacheが復元されていません。')
        print('モデルの取得は不要だったため、archiveの保存を省略します。')
        return False
    if archive.stat().st_size > 500_000_000:
        raise ValueError('モデルのcacheが取得上限を超えました。')
    if archive_digest(archive) != digest:
        raise ValueError('復元したモデルのSHA256が一致しません。')
    with zipfile.ZipFile(archive) as zipped:
        names = zipped.namelist()
        if any(Path(name).is_absolute() or '..' in Path(name).parts for name in names):
            raise ValueError('モデルに不正なPathがあります。')
        metadata_names = [name for name in names if name.endswith('/metadata.json')]
        if len(metadata_names) != 1:
            raise ValueError('モデルのMetadataが一意ではありません。')
        metadata = json.loads(zipped.read(metadata_names[0]))
        if any(metadata.get(key) != value for key, value in
               {'from_code': 'en', 'to_code': 'ja', 'package_version': '1.1'}.items()):
            raise ValueError('復元したモデルの言語・Versionが一致しません。')
    print(f'取得・インストールせずに固定モデルのcacheを検証しました。SHA256: {digest}')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require', action='store_true', help='cacheの未復元も失敗とする')
    args = parser.parse_args()
    ready = check_cache(Path(__file__).resolve().parents[1] / '.github/argos-model.json',
                        os.environ['ARGOS_MODEL_CACHE_DIR'], args.require)
    if output := os.environ.get('GITHUB_OUTPUT'):
        with open(output, 'a') as stream:
            stream.write(f'ready={str(ready).lower()}\n')


if __name__ == '__main__':
    main()
