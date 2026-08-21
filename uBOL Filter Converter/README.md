# AdGuard Custom Rules to uBlock Origin Lite Converter

AdGuard用カスタムフィルタを、uBlock Origin Lite（uBOL）で購読・利用できる
外部フィルタリストへ保守的に変換します。

## 購読方法（推奨）

uBOL `2026.621.1813`以降では、リモートサーバー上の外部フィルタリストを
URLで購読できます。uBOLのオプションを開き、`Filter lists`の
`Add filter list…`へ次のRaw URLを入力してください。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/refs/heads/main/uBOL%20Filter%20Converter/dist/AdGuard_Custom_Rules_uBOL.txt
```

追加後は`Imported lists`に表示されます。リスト内のコスメティックフィルタを
有効にするには、ブラウザの拡張機能設定でuBOLのユーザースクリプト実行を
許可する必要があります。許可しない場合でも、対応するネットワークフィルタは
適用されます。

### 対応条件と制限

- 外部リスト購読にはuBOL `2026.621.1813`以降が必要です。
- Safari版は必要なOffscreen APIがないため、外部リスト購読に対応していません。
- インポートしたリストは動的DNRルールへ変換されるため、ブラウザの動的ルール上限の影響を受けます。
- 汎用コスメティックフィルタ、厳格ブロック、`popup`など、一部機能には対応上の制限があります。
- 信頼できるURLだけを追加してください。外部リストは更新時にも取得・再コンパイルされます。

手動で使用する場合は、生成された`dist/AdGuard_Custom_Rules_uBOL.txt`の内容を
uBOLの`Custom filters`からインポートできます。ただし、通常は自動更新される
URL購読を推奨します。

## 変換方針

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

変換元または変換コードをmainで更新すると、GitHub Actionsがテスト後にフィルタと
JSONレポートを再生成します。Pull Requestでは同じ変換を実行し、コミット済みの
生成物と一致しない場合に品質チェックを失敗させます。レポートから実行時刻を除外し、
同じ入力から常に同じ内容を生成できるようにしています。

## uBOL CHANGELOGの自動確認

GitHub Actionsが[uBOL公式CHANGELOG](https://github.com/uBlockOrigin/uBOL-home/blob/main/CHANGELOG.md)を
毎日03:37（JST）に取得します。上流CHANGELOGのSHA-256が変化した場合のみ、
最新バージョン、確認日時、追跡している互換性情報を
[`upstream/ubol-changelog.json`](upstream/ubol-changelog.json)へ自動反映し、英語原文を
[`upstream/ubol-CHANGELOG.source.md`](upstream/ubol-CHANGELOG.source.md)へミラーします。

取得失敗や予期しないCHANGELOG形式は正常終了として扱わず、誤ったメタデータで
上書きしません。また、CHANGELOGの文章から変換ルールを推測して自動変更することは
ありません。新しい構文や制限は内容を確認し、テストを追加してから変換処理へ反映します。

変換元の既存ファイルや、リポジトリ内の既存変換スクリプトは変更しません。

## 参考資料

- [外部フィルタリスト購読機能の実装コミット](https://github.com/gorhill/uBlock/commit/06deb19dfa85c13e48ad44d2e6dc4f64a96d6cbc)

## 英語CHANGELOG

- [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home/blob/main/CHANGELOG.md)
