# AdGuard Custom Rules

AdGuard向けの個人用フィルタです。通常のコンテンツブロック用フィルタとDNSフィルタは処理する層・構文・適用場所が異なるため、使用するAdGuard製品の対応する機能へ個別に追加してください。

## ファイル

- [`AdGuard Custom Rules - Red Frame X.txt`](AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：広告・不要要素の非表示、ネットワーク通信制御、互換性のための例外などを含むAdGuardフィルタ
- [`AdGuard DNS Custom Rules - Red Frame X.txt`](AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：DNSレベルのブロックに使用するAdGuard DNSフィルタ

## 購読URL

### コンテンツブロックフィルタ

AdGuardの「カスタムフィルタ」へ追加します。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt
```

AdGuard for Androidでは「広告ブロック」→「フィルタ」→「カスタムフィルタ」から追加できます。AdGuard ブラウザ拡張機能でもカスタムフィルタとして購読できます。MV3対応版ではUser Scripts APIなどブラウザ側の制約が関係するため、表示される案内に従って必要な権限を有効にしてください。

### DNSフィルタ

AdGuard for Androidなど、カスタムDNSフィルタを利用できる製品の「DNSフィルタ」へ追加します。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt
```

AdGuard for Androidでは「DNS通信を保護」の「DNSフィルタ」でカスタムDNSフィルタを追加できます。

> [!IMPORTANT]
> コンテンツブロックフィルタとDNSフィルタは相互に置き換えられません。DNSフィルタを通常のカスタムフィルタへ追加したり、コンテンツブロックフィルタをDNSフィルタとして追加したりしないでください。

## 利用上の注意

これらは個人環境向けです。`$app`のようなアプリ固有ルール、高度な整形ルール、scriptlet、許可ルールなどは、製品・プラットフォーム・フィルタリングエンジンによって対応状況や副作用が異なります。必要なルールだけを利用し、導入後は誤ブロックや表示崩れがないか確認してください。

uBlock Origin Liteで利用する場合は、互換性のないルールを保守的に除外・変換した生成版[`uBOL Filter - Red Frame X`](../uBOL%20Filter%20Converter/)を使用してください。元のAdGuardフィルタをそのままuBO Liteへ読み込むことは前提としていません。

## 編集時の品質確認

`AdGuard Custom Rules - Red Frame X.txt`はuBOL生成フィルタの変換元でもあります。ルールを追加・削除・変更する場合は、ヘッダーの`! Version:`を`YYYYMMDDHHMM`形式で更新してください。

リポジトリの品質チェックでは、原本フィルタの破損防止に加えて、重複した有効ルール、末尾空白、改行形式、意図しない大量削除などを検査します。ローカルでは次の順序で確認できます。

```bash
python scripts/check_adguard_filter_integrity.py
python scripts/check_adguard_user_rule_edit.py
npm run lint:adguard
python -m unittest discover -s tests -v
python -m unittest discover -s "uBOL Filter Converter/tests" -v
```

uBOL向け生成物はGitHub Actionsで同期されるため、通常は`uBOL Filter Converter/dist/`を直接編集しません。変換結果に問題がある場合は、原本ルール、コンバータ、能力定義またはテストを修正します。

## CHANGELOG追跡とコンバータ更新

[`update_adguard_changelogs.py`](../scripts/update_adguard_changelogs.py)は、AdGuard Browser Extensionの公式CHANGELOGとAdGuard for Androidの公式GitHub Releasesを毎日取得し、[`ChangeLog/`](ChangeLog/)へ英語原文のミラーを生成します。メタデータと互換性レビュー候補は`upstream/adguard/`へ生成します。

CHANGELOGは人向けの変更履歴であり、フィルタ構文の実行可能な仕様そのものではありません。このため、CHANGELOGの文章だけからコンバータコードを自己変更する処理は行いません。新しい構文や挙動は、AdGuard公式のフィルタリングルール仕様、公開ソース、上流Issuesなどで確認し、回帰テストを追加してから[`adguard-converter-capabilities.json`](../config/adguard-converter-capabilities.json)を更新します。

## 公式資料

- [AdGuardフィルタリングルール構文](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard for Android：設定](https://adguard.com/kb/ja/adguard-for-android/features/settings/)
- [AdGuard for Android：DNS通信を保護](https://adguard.com/kb/ja/adguard-for-android/features/protection/dns-protection/)
- [AdGuard ブラウザ拡張機能](https://adguard.com/kb/ja/adguard-browser-extension/)
- [AdGuard ブラウザ拡張機能 MV3対応版](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuard ブラウザ拡張機能 Release](https://adguard.com/ja/versions/browser-extension/release.html)
- [AdGuard Browser Extension CHANGELOG](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/CHANGELOG.md)
- [AdGuard for Android Releases](https://github.com/AdguardTeam/AdguardForAndroid/releases)
