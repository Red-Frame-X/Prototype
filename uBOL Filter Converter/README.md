# AdGuard Custom Rules to uBlock Origin Lite Converter

AdGuard用カスタムフィルタを、uBlock Origin Lite（uBOL）の
`Options > Custom filters`へ貼り付けるための形式に保守的に変換します。

## 重要な制限

uBOLは任意URLの外部カスタムフィルタリストを購読できません。生成された
`dist/AdGuard_Custom_Rules_uBOL.txt`を開き、内容をuBOLの`Custom filters`へ
貼り付けてください。

誤変換によるサイト破損を避けるため、意味を維持できない次のルールは出力せず、
JSONレポートへ理由と元の行番号を記録します。

- AdGuardアプリ専用の`$app`ルール
- HTMLフィルタリング（`$$`）
- AdGuard scriptlet（`#%#`）
- `:contains()`、`:upward()`、`:style()`などの手続き型・装飾型ルール
- `$replace`、`$redirect`、`$csp`など、uBOLへ安全に対応付けられない修飾子
- ChromeのRE2で表現できない後読み・後方参照付き正規表現

## 実行

Python 3.10以降、外部パッケージ不要です。

```bash
python "uBOL Filter Converter/converter.py"
```

ローカルファイルを変換する場合：

```bash
python "uBOL Filter Converter/converter.py" \
  --input "AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt"
```

出力先を変更する場合：

```bash
python "uBOL Filter Converter/converter.py" \
  --output /path/to/filters.txt \
  --report /path/to/report.json
```

## テスト

```bash
python -m unittest discover -s "uBOL Filter Converter/tests" -v
```

変換元の既存ファイルや、リポジトリ内の既存変換スクリプトは変更しません。
