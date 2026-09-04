# Content Blocking FAQ 2026

コンテンツブロックについて自分が後から確認しやすいよう、FAQ形式で整理している個人用の学習メモです。

> [!NOTE]
> この文書は自分の学習・設定見直し用であり、一般向けの製品選定ガイド、推奨構成、サポート文書を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。重要な仕様は使用時点の公式ドキュメント、公開ソース、CHANGELOG、実環境で再確認します。

---

2026年9月1日時点で確認できるコンテンツブロックの仕様・運用上の注意点を、公式ドキュメント、公開ソースコード、公式リポジトリを優先して整理しています。

[Yuki2718/adblock2 Wiki「よくある質問」](https://github.com/Yuki2718/adblock2/wiki/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E8%B3%AA%E5%95%8F)で扱われている主要論点を参考にしていますが、古い製品状況や過去仕様は残さず、自分が現在確認できた情報だけで再構成しています。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | GPL-3.0 |
| **Version** | 20260904 |

第三者コンテンツの扱いおよび無保証は[LICENSES.md](../LICENSES.md)に記録しています。

---

## 1. ブラウザごとの主要な選択肢

### Firefox

フル版の **uBlock Origin（uBO）** を利用できます。uBO公式はFirefox版を「works best on Firefox」と案内しており、FirefoxではCNAME uncloaking、IPアドレスベースのフィルタリング、HTML filteringなど、Chromium系では利用できないか制限される機能があります。

ただし、追加フィルタ、DNSブロック、プロキシなどを重ねるほどトラブルシューティングは複雑になります。問題発生時はuBOのLoggerを使い、どのルール・レイヤーが原因かを切り分けます。

**参照**

- [gorhill/uBlock](https://github.com/gorhill/uBlock)
- [uBlock Origin works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox)

### Chromium / Chrome / ChromeOS

Chromium系では **uBlock Origin Lite（uBOL）** や **AdGuard Browser Extension MV3** など、Manifest V3（MV3）を前提とした選択肢が中心です。

フル版uBOとuBOLは別実装です。uBOLはMV3のDeclarative Net Request（DNR）を利用しており、フル版uBOと同一の機能セットではありません。サイト権限とフィルタリングモードによって、コスメティックフィルタやスクリプトレットの適用範囲も変わります。

フル版uBOのChromium版はGitHub Releases等で配布されていますが、Chrome Web Store版はuBO公式READMEが案内した **2026年8月31日の削除予定日を経過しています**。自分がChrome / ChromeOSで使う場合は、ストア配布のMV3対応拡張であるuBOLなどを前提にし、フル版uBOを利用する場合は配布元と導入方式を再確認します。

**参照**

- [gorhill/uBlock README](https://github.com/gorhill/uBlock/blob/master/README.md)
- [uBlockOrigin/uBOL-home](https://github.com/uBlockOrigin/uBOL-home)
- [uBO Lite Troubleshooting](https://github.com/uBlockOrigin/uBOL-home/wiki/Troubleshooting)

### Brave / Vivaldi

Brave ShieldsやVivaldiのTracker and Ad Blockerはブラウザ内蔵機能であり、通常のMV3拡張機能とは実装経路が異なります。

ただし、uBO、uBOL、AdGuardと完全に同じ構文、スクリプトレット、デバッグ機能を持つわけではありません。自分の用途では、必要なカスタムルール互換性、ログ、保守性を基準に比較します。

**参照**

- [Brave Shields](https://brave.com/shields/)
- [Vivaldi: Manifest V3 update](https://vivaldi.com/blog/manifest-v3-update-vivaldi-is-future-proofed-with-its-built-in-functionality/)
- [Vivaldi Desktop Releases](https://vivaldi.com/blog/desktop/releases/)

---

## 2. uBlock OriginとuBlock Origin Liteの違い

### Q. uBO LiteはuBlock OriginのMV3版ですか

同じ作者・関連プロジェクトですが、**フル版uBOをそのままMV3へ移植したものではありません**。

uBOLはMV3の制約に合わせて宣言的に動作する別実装です。ブラウザ側がDNRルールやコンテンツスクリプトを処理する設計で、通常のブロック処理のために常駐バックグラウンドプロセスを必要としません。

一方で、フル版uBOの動的フィルタリング、Loggerを中心とした詳細なデバッグ、一部の高度なフィルタリング機能などを完全には再現しません。

自分がuBOLを使うときは、サイト権限とフィルタリングモードを確認します。

**参照**

- [uBlockOrigin/uBOL-home](https://github.com/uBlockOrigin/uBOL-home)
- [uBO Lite Filtering modes](https://github.com/uBlockOrigin/uBOL-home/wiki/Filtering-mode)

---

## 3. AdGuard Browser Extension MV3

### Q. MV3版では何が変わりますか

ネットワークフィルタの多くをブラウザのDNR APIが処理するため、MV2版とは挙動が異なります。

主な制約は次のとおりです。

- DNRで利用できる静的・動的・正規表現ルール数に上限がある
- 同時に有効化できるフィルタ数に上限がある
- 一部のネットワーク修飾子は非対応または制限付き
- 通常版のFiltering logでは、DNR制約により実際に発火したルールを完全には特定できず、「発動したと想定されるルール」が表示される

### Q. MV3版のフィルタはどのように更新されますか

**URLで購読したCustom filters（カスタムフィルタ）は、現行の公式Knowledge Baseでは拡張機能本体とは独立して更新される仕様として案内されています。** Custom filtersはURLまたはローカルファイルから追加できます。

URLで管理している自作・第三者フィルタは、拡張機能本体のリリースを待たずに更新されます。なお、旧MV3解説ページには「自動および手動のフィルタ更新なし」という説明も残っており、これは組み込みフィルタ中心の旧仕様説明と現行Custom filters仕様が併存している状態です。自分のメモでは、Custom filtersと組み込みフィルタを分けて扱います。

一方、**AdGuardが組み込みで提供するフィルタは、URL購読のCustom filtersとは更新経路が異なります。** 現行の公式GitHubリポジトリでは、MV3向け組み込みフィルタについて最新の `@adguard/dnr-rulesets` を定期的に取り込み、更新済みrulesetを含む拡張機能ビルドを自動公開する更新サイクルが説明されています。Chrome Web Storeのskip reviewを利用できる更新は迅速に公開できますが、filtering script rulesの変更を含む場合にはskip reviewを利用できないという制約があります。

現時点で自分が区別している更新方式は次のとおりです。

- **URLで購読するCustom filters**: 現行の公式Knowledge Baseでは拡張機能本体とは独立して更新される
- **AdGuard組み込みフィルタ**: MV3用rulesetを取り込んだ拡張機能ビルドの更新サイクルで配信される。更新内容によってChrome Web Storeのskip reviewを利用できる範囲に制約がある

自分でユーザールールやカスタムフィルタを作成するときは、AdGuard構文として正しいだけでなく、MV3/DNRで実装可能かも確認します。

**参照**

- [AdGuard Browser Extension: Filters](https://adguard.com/kb/adguard-browser-extension/features/filters/)
- [AdGuard Browser Extension: Main menu](https://adguard.com/kb/adguard-browser-extension/features/main-menu/)
- [AdGuard Browser Extension Releases](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)
- [AdguardTeam/AdguardBrowserExtension](https://github.com/AdguardTeam/AdguardBrowserExtension)
- [AdGuard filtering rules syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)

---

## 4. 複数ブロッカーの併用

### Q. uBOと別のブラウザ用コンテンツブロッカーを同時に使うべきですか

自分の運用では原則として避けます。

uBO公式READMEは、uBOを他のコンテンツブロッカーと併用しないよう明示しています。複数のブラウザ用ブロッカーが同じ通信、リダイレクト、スクリプトレット、要素隠蔽を別々に処理すると、次の問題が起こり得ます。

- 例外ルールが期待どおり働かない
- アンチ広告ブロック対策が干渉する
- 誤ブロック時の原因特定が難しくなる
- 同じ処理を重複して実行する

自分のブラウザ環境では、原則として1つの主要コンテンツブロッカーへ集約します。

**参照**

- [gorhill/uBlock README](https://github.com/gorhill/uBlock/blob/master/README.md)

### Q. ブラウザブロッカーとDNSブロックは併用できますか

併用できます。ただし役割が異なります。

DNSブロックは名前解決レイヤーでドメイン単位の遮断を行います。URLパス、DOM要素、スクリプトレット、リソース種別などのページ文脈は扱えません。

ブラウザ用コンテンツブロッカーは、URL、リソース種別、サイト文脈、DOM、スクリプトレットなどを利用して細かな制御を行えます。

したがって、両者の併用は同じ機能の単純な二重化ではありません。ただし、DNS側で通信が先に遮断されるとブラウザ側のLoggerに通信が現れず、原因特定が難しくなる場合があります。

自分がトラブルシューティングするときは、ブラウザブロッカーとDNSブロックを一時的に切り離して検証します。

**参照**

- [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)

---

## 5. フィルタリストの選択

### Q. フィルタリストは多いほど強力ですか

いいえ。

追加リストが増えるほど必ず遅くなるとは限りませんが、対象範囲、例外処理、サイト破損、原因切り分けの複雑さは増えます。

uBOでは重複フィルタが除去され、純粋なホスト名フィルタなどは効率よく処理されます。一方で、複雑なパターン、正規表現、procedural cosmetic filterは書き方によって評価コストが変わります。

自分が追加リストを判断するときは、件数より次の点を確認します。

1. 必要な対象へ十分に絞られているか
2. 既定リストで対応済みではないか
3. 不要な正規表現や複雑なワイルドカードを使っていないか
4. procedural filterの対象を狭くできているか
5. 追加による誤ブロックを切り分けられるか

自分の環境では、まず標準フィルタを維持し、必要性を確認できた地域・用途別リストだけを追加する方針にしています。

**参照**

- [uBO Filter Performance](https://github.com/gorhill/uBlock/wiki/Filter-Performance)
- [uBO Dashboard: Filter lists](https://github.com/gorhill/uBlock/wiki/Dashboard%3A-Filter-lists)
- [uBO Procedural cosmetic filters](https://github.com/gorhill/uBlock/wiki/Procedural-cosmetic-filters)

### Q. ホスト名だけのルールは非効率ですか

用途が合えば効率的です。

uBOでは純粋なホスト名フィルタが効率よく処理されます。DNSブロックでもドメイン単位の遮断は基本的な方法です。

ただし、広告やトラッカーが正常コンテンツと同じドメインから配信される場合、ドメイン全体を遮断すると誤ブロックが起きます。その場合はURLパス、リソース種別、サイト条件、DOM条件など、より狭いルールを使います。

---

## 6. フィルタ構文の互換性

### Q. uBO用ルールをAdGuardへそのまま移植できますか

完全互換ではありません。

uBOとAdGuardはいずれもABP/EasyList系構文との共通部分を持ちますが、それぞれ独自拡張があります。

自分が別エンジンへ移植するときは、特に次の機能差を確認します。

- scriptlet名・引数
- redirect resource
- HTML filtering
- procedural cosmetic filtering
- action operator
- network modifier
- 例外ルールの適用範囲
- MV3/DNRへの変換可否

構文が受理されるかだけでなく、**同じ対象へ同じ副作用・例外処理で作用するか**まで確認します。

**参照**

- [uBO Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [AdGuard filtering rules syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)

---

## 7. CNAME・DNS・HTTPSフィルタリング

### Q. CNAME uncloakingはすべてのブラウザで同じですか

いいえ。

uBOのCNAME uncloakingは、DNS APIを利用できるFirefoxで提供されています。

一方、AdGuard for Androidはブラウザ拡張機能ではなく、ローカルVPN、DNS protection、HTTPS filteringなどを組み合わせて端末全体の通信を処理できます。

自分が製品を比較するときは、「CNAME対策があるか」だけでなく、**DNS・ネットワーク・HTTPS・ブラウザDOMのどのレイヤーで処理しているか**を区別します。

**参照**

- [uBlock Origin works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox)
- [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard for Android: Settings](https://adguard.com/kb/adguard-for-android/features/settings/)

---

## 8. アンチ広告ブロックへの対処

アンチ広告ブロック実装は頻繁に変わるため、固定された万能ルールより、現在のフィルタとログを基準に対処します。

自分が切り分けるときの順序：

1. ブラウザ用ブロッカーを複数併用していないことを確認する
2. 追加したサードパーティリストを一時的に減らす
3. Logger / Filtering logで発火ルールを確認する
4. 既存の主要フィルタで対応済みか確認する
5. 未対応なら対象フィルタのIssue受付先へ再現情報を報告する
6. 必要な場合だけサイト限定の最小ルールを作成する

スクリプトレット、HTML filtering、procedural cosmetic filteringなどは強力ですが、サイト内部実装への依存度が高いため、自分で作る場合も広範囲へ適用するルールは慎重に扱います。

---

## 9. 自分の運用メモ

### Firefox

- フル版uBOを中心にする
- まず既定フィルタを維持する
- 必要な地域・用途別リストだけ追加する
- 問題発生時はLoggerで原因ルールを確認する
- DNSブロック併用時は各レイヤーを切り離して検証できる構成にする

### Chromium / ChromeOS

- MV3前提でuBO Lite、AdGuard Browser Extension MV3、ブラウザ内蔵ブロッカー等から自分の用途に合うものを選ぶ
- uBO Liteではフィルタリングモードとサイト権限を確認する
- AdGuard MV3ではDNR変換可否、ルール上限、組み込みフィルタとCustom filtersの更新経路の違いを確認する
- URL購読のCustom filtersは組み込みフィルタと更新経路が異なるため、別物として管理する
- フル版uBOとuBO Liteを同一機能の製品として扱わない

### Android

- Firefox内だけを対象にする場合はFirefox + uBOを利用できる
- アプリを含む端末全体を対象にする場合はAdGuard for Android等のシステムレベル製品を比較する
- DNS protectionとHTTPS filteringを別機能として切り分ける

---

## 10. 参照する一次情報

- [gorhill/uBlock](https://github.com/gorhill/uBlock)
- [uBlockOrigin/uBOL-home](https://github.com/uBlockOrigin/uBOL-home)
- [uBO Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [uBO Filter Performance](https://github.com/gorhill/uBlock/wiki/Filter-Performance)
- [uBO Dashboard: Filter lists](https://github.com/gorhill/uBlock/wiki/Dashboard%3A-Filter-lists)
- [AdGuard filtering rules syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [AdGuard Browser Extension: Filters](https://adguard.com/kb/adguard-browser-extension/features/filters/)
- [AdGuard Browser Extension: Main menu](https://adguard.com/kb/adguard-browser-extension/features/main-menu/)
- [AdGuard Browser Extension Releases](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)
- [AdguardTeam/AdguardBrowserExtension](https://github.com/AdguardTeam/AdguardBrowserExtension)
- [AdGuard for Android DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)
- [Brave Shields](https://brave.com/shields/)
- [Vivaldi Manifest V3 update](https://vivaldi.com/blog/manifest-v3-update-vivaldi-is-future-proofed-with-its-built-in-functionality/)
