# uBOL Filter - Red Frame X

`uBOL Filter - Red Frame X`は、自分が管理しているAdGuard用カスタムフィルタをuBlock Origin Lite（uBOL）向けに保守的に変換するための個人用生成物です。このディレクトリには、変換処理、テスト、生成フィルタ、上流CHANGELOG追跡データを保存しています。

> [!IMPORTANT]
> このディレクトリは一般向けの配布や導入ガイドを目的としていません。主な目的は、変換ロジックの学習・検証と、自分の環境を再構成するためのバックアップです。文章の下書きはChatGPTで推敲・整理しているため、説明に誤り、古い情報、環境依存の内容が含まれる可能性があります。uBOLの仕様や制限は公式CHANGELOG、公開ソース、実際の挙動で再確認します。

## 自分の環境での利用メモ

uBOLの外部フィルタリスト購読機能を利用できる環境では、次のRaw URLを自分のカスタムフィルターとして登録しています。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/refs/heads/main/uBOL%20Filter%20Converter/dist/uBOL%20Filter%20-%20Red%20Frame%20X.txt
```

外部リスト購読やインポートしたリストの適用条件はuBOLのバージョンやブラウザ機能に依存します。Safari版、Offscreen API、動的DNRルール上限、サイト権限、ユーザースクリプト許可などの条件は、保存時点のメモだけで判断せず、使用中バージョンの公式情報と実際のUIを確認します。

必要に応じて、生成された`dist/uBOL Filter - Red Frame X.txt`を手動インポートすることもありますが、自分の通常運用では更新追従のためURL購読を使います。

## 変換方針

誤変換によるサイト破損を避けるため、意味を維持できないルールは出力せず、JSONレポートへ理由と元の行番号を記録します。

対応可能なコスメティックルールは、`:contains()`を`:has-text()`、`:nth-ancestor()`を`:upward()`、`:matches-property()`を`:matches-prop()`へ変換します。`:remove()`、`:style()`、`:matches-attr()`、`:matches-css*()`、`:xpath()`などuBO/uBOLが対応する演算子は維持して出力します。

次のルールは意味または信頼境界を維持できないため除外します。

- AdGuardアプリ専用の`$app`ルール
- HTMLフィルタリング（`$$`）。同じ目的のCSSフォールバックがある場合はそちらを出力
- `[$app=...]`、`[$url=...]`などの非基本ルール修飾子。現在の変換器では適用範囲を安全に対応付けられない
- スクリプトレットルールとその例外（`#%#`、`#@%#`、`##+js`、`#@#+js`）。現在の変換器では種類を問わず除外
- `$replace`、`$redirect`、`$csp`など、uBOLへ安全に対応付けられない修飾子
- ChromeのRE2で表現できない先読み・後読み・後方参照付き正規表現

## 実行メモ

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

変換元または変換コードをmainで更新すると、GitHub Actionsがテスト後にフィルタとJSONレポートを再生成します。Pull Requestでは同じ変換を実行して変換処理と出力の整合性を確認し、生成物の同期自体はmainへマージ後に`build-ubol.yml`が行います。レポートから実行時刻を除外し、同じ入力から同じ内容を生成できるようにしています。

## uBOL CHANGELOGの自動確認

GitHub Actionsが[uBOL公式CHANGELOG](https://github.com/uBlockOrigin/uBOL-home/blob/main/CHANGELOG.md)を毎日03:37（JST）に取得します。上流CHANGELOGのSHA-256が変化した場合のみ、最新バージョン、確認日時、追跡している互換性情報を[`upstream/ubol-changelog.json`](upstream/ubol-changelog.json)へ反映し、英語原文を[`upstream/ubol-CHANGELOG.source.md`](upstream/ubol-CHANGELOG.source.md)へミラーします。

取得処理では、`GITHUB_TOKEN`が設定されている場合も、認証情報を付与するのは`https://api.github.com`への直接のリクエストだけです。Raw URLや外部サイトには付与せず、同一ホストを含むリダイレクト先にも転送しません。認証が必要な取得先を指定する場合は、リダイレクトを経由しないGitHub API URLを使用します。

取得失敗や予期しないCHANGELOG形式は正常終了として扱わず、誤ったメタデータで上書きしません。また、CHANGELOGの文章から変換ルールを推測して自動変更することはありません。新しい構文や制限は内容を確認し、テストを追加してから変換処理へ反映します。

## 参考資料

- [uBlock Origin Lite 日本語ロケール](https://github.com/gorhill/uBlock/blob/master/platform/mv3/extension/_locales/ja/messages.json)
- [外部フィルタリスト購読機能の実装コミット](https://github.com/gorhill/uBlock/commit/06deb19dfa85c13e48ad44d2e6dc4f64a96d6cbc)
- [uBlock Origin Lite CHANGELOG](https://github.com/uBlockOrigin/uBOL-home/blob/main/CHANGELOG.md)
