#!/usr/bin/env python3
"""GitHub-hosted runnerで公式英日モデルの実物と出典を確認する。"""
import hashlib
import json
import os
from pathlib import Path
import urllib.request
import urllib.error
import zipfile


def main():
    path = Path(os.environ['RUNNER_TEMP']) / 'translate-en_ja-1_1.argosmodel'
    # 両URLはArgos公式Indexに記載された同じen→ja Version 1.1の配布先。
    urls = (
        'https://argos-net.com/v1/translate-en_ja-1_1.argosmodel',
        'https://argosopentech.nyc3.digitaloceanspaces.com/argospm/translate-en_ja-1_1.argosmodel',
    )
    for url in urls:
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'ArgosTranslate/1.11.0'})
            with urllib.request.urlopen(request, timeout=90) as response:
                with path.open('wb') as output:
                    total = 0
                    while chunk := response.read(1024 * 1024):
                        total += len(chunk)
                        if total > 500_000_000:
                            raise RuntimeError('モデルの取得上限を超えました。')
                        output.write(chunk)
            print('MODEL_SOURCE=' + url)
            break
        except urllib.error.HTTPError as error:
            print(f'公式配布先の取得失敗: {url}: HTTP {error.code}')
    else:
        raise RuntimeError('公式配布先からモデルを取得できません。')
    print('MODEL_SHA256=' + hashlib.sha256(path.read_bytes()).hexdigest())
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            if info.filename.endswith(('metadata.json', 'README.md', 'LICENSE')) and info.file_size < 100_000:
                print(json.dumps({'path': info.filename,
                                  'text': archive.read(info).decode('utf-8')}, ensure_ascii=False))
        print(json.dumps({'files': archive.namelist()}, ensure_ascii=False))


if __name__ == '__main__':
    main()
