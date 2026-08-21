# AdGuard Custom Rules

AdGuard向けの個人用フィルタです。Webページ用ルールとDNS用ルールは用途が異なるため、使用するAdGuard製品の該当機能へ個別に追加してください。

## ファイル

- [`AdGuard Custom Rules - Red Frame X.txt`](AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：広告・不要要素の非表示、通信制御、互換性例外を含むAdGuardフィルタ
- [`AdGuard DNS Custom Rules - Red Frame X.txt`](AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：AdGuard DNS／DNSフィルタリング向けルール

## 使い方

1. 使用するファイルを開き、`Raw`を選択してURLをコピーします。
2. AdGuardの「カスタムフィルタ」またはDNSの「ユーザールール」へ追加します。
3. 誤ブロックや表示崩れがないか確認し、問題があれば該当ルールを無効化します。

これらは個人環境向けです。アプリ専用の`$app`、高度なコスメティックルール、許可ルールは環境により動作や副作用が異なります。必要なルールだけを選んで利用してください。

uBlock Origin Liteで利用する場合は、互換性のないルールを除外した[`uBOL Filter Converter`](../uBOL%20Filter%20Converter/)の生成版を使用してください。

## CHANGELOG追跡とコンバータ更新

[`update_adguard_changelogs.py`](../scripts/update_adguard_changelogs.py)は、AdGuard Browser Extensionの公式CHANGELOGとAdGuard for Androidの公式GitHub Releasesを毎日取得し、`upstream/adguard/`へミラー、メタデータ、互換性レビュー候補を生成します。

CHANGELOGは人向けの要約であり、フィルタ構文の実行可能な仕様ではありません。このため、文章からコンバータコードを自己変更する処理は行いません。新しい構文や挙動は、公式フィルタリング仕様・CoreLibs／Scriptletsの公開ソースまたは上流Issueで確認し、回帰テストを追加してから[`adguard-converter-capabilities.json`](../config/adguard-converter-capabilities.json)を更新します。これにより、誤変換や広すぎるブロックを防ぎます。
