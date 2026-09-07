# AdGuard Custom Rules

AdGuard向けに自分の環境で使用・検証している個人用フィルタと、その保守メモです。通常のコンテンツブロック用フィルタとDNSフィルタは処理する層・構文・適用場所が異なるため、このREADMEでは自分の設定を再現するときに混同しないための記録として整理しています。

> [!IMPORTANT]
> このディレクトリは個人の設定バックアップと検証記録です。一般向けの配布や導入手順を目的としていません。記述の下書きはChatGPTで推敲・整理しているため、内容に誤り、古い情報、環境依存の挙動が含まれる可能性があります。重要な仕様はAdGuard公式資料、公開ソース、実環境で再確認します。

## ファイル

- [`AdGuard Custom Rules - Red Frame X.txt`](AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：広告・不要要素の非表示、ネットワーク通信制御、互換性のための例外などを含む個人用AdGuardフィルタ
- [`AdGuard DNS Custom Rules - Red Frame X.txt`](AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：DNSレベルのブロックに使用している個人用AdGuard DNSフィルタ

## 自分の環境での登録先メモ

### コンテンツブロックフィルタ

自分の環境では、AdGuardのカスタムフィルタとして次のRaw URLを登録しています。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt
```

AdGuard for Androidでの登録先：

**ボトムバーの ⚙ → 「フィルタリング」→「フィルタ」→「カスタムフィルタ」→「＋ カスタムフィルタを追加する」**

AdGuard ブラウザ拡張機能ではカスタムフィルタとして扱います。MV3対応版ではUser Scripts APIなどブラウザ側の制約が関係するため、必要な権限や挙動は使用中バージョンの公式資料と実際のUIで確認します。

### DNSフィルタ

自分の環境では、カスタムDNSフィルタとして次のRaw URLを使用しています。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt
```

AdGuard for Androidでの登録先：

**ボトムバーの 🛡️ → 「DNS通信を保護」→「DNSフィルタ」→「＋ DNSフィルターを追加する」**

> [!IMPORTANT]
> コンテンツブロックフィルタとDNSフィルタは相互に置き換えられません。自分の環境を再構成するときも、それぞれ対応する機能へ登録します。

## 検証時の注意

`$app`のようなアプリ固有ルール、高度な整形ルール、scriptlet、許可ルールなどは、製品・プラットフォーム・フィルタリングエンジンによって対応状況や副作用が異なります。変更時は自分の環境で誤ブロック、表示崩れ、機能不全がないかを確認します。

uBlock Origin Lite向けには、互換性のないルールを保守的に除外・変換した生成版[`uBOL Filter - Red Frame X`](../uBOL%20Filter%20Converter/)を別途生成しています。元のAdGuardフィルタをそのままuBO Liteへ読み込む構成にはしていません。

## 編集時の品質確認

`AdGuard Custom Rules - Red Frame X.txt`はuBOL生成フィルタの変換元でもあります。ルールを追加・削除・変更する場合は、ヘッダーの`! Version:`を`YYYYMMDDHHMM`形式で更新します。

リポジトリの品質チェックでは、原本フィルタの破損防止に加えて、重複した有効ルール、末尾空白、改行形式、意図しない大量削除などを検査します。ローカルで確認する場合は次を実行します。

```bash
python scripts/check_adguard_filter_integrity.py
python scripts/check_adguard_user_rule_edit.py
npm run lint:adguard
python -m unittest discover -s tests -v
python -m unittest discover -s "uBOL Filter Converter/tests" -v
```

uBOL向け生成物はGitHub Actionsで同期するため、通常は`uBOL Filter Converter/dist/`を直接編集しません。変換結果に問題がある場合は、原本ルール、コンバータ、能力定義またはテストを修正します。

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
