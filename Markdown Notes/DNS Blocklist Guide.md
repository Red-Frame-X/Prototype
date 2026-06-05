# DNS Blocklist Guide

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260605 |

この備忘録は CC0 ライセンスの下で提供します（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

※ 記述内容は個人の検証に基づくものであり、正確性を保証するものではありません。

## 要約

本ドキュメントは、Google検索で得られたGitHubドキュメントやRedditの議論（検索結果）を元に、DNSブロックリストの3つの主要な形式（Hosts、Wildcard、ABP形式）の挙動と特徴、およびAdGuard for AndroidとpersonalDNSfilterに最適なDNSブロックリストをそれぞれ1つに厳選して統合したものです。

* **フォーマットの比較**：Hosts形式は互換性が高い反面ファイルが肥大化しやすく、Wildcard形式は軽量ですが過剰ブロックのリスクがあります。ABP形式は柔軟な指定が可能ですが、システム側の解析負荷が高くなります。
* **推奨リストの結論**：アプリの仕様と処理能力を考慮し、AdGuard for Androidには公式の「AdGuard DNS filter」を、ABP形式の解析に制限があるpersonalDNSfilterにはドメイン形式で安定稼働しつつ高いブロック精度を誇る「HaGeZi's Pro DNS Blocklist」をそれぞれ単体で設定することが最適解となります。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット:** 外部リゾルバなしに、ほぼ全てのOSやデバイスでネイティブに動作する圧倒的な互換性を持ちます。意図しないドメインを巻き込む過剰ブロックが起こりにくい点も優れています。
* **デメリット**：サブドメインをすべて個別に記載する必要があるため、ファイルサイズが数MBレベルに肥大化しやすく、OSのパース遅延やパフォーマンス低下を招く原因となります。ワイルドカードやホワイトリストの記述はできません。

### ワイルドカードドメイン（Wildcard Domains）
特定のドメインとその配下にあるすべてのサブドメインを包括的に対象とする形式です。

* **挙動・特徴**： `*.example.com` のように記述し、関連するサブドメインをすべてブロック対象とします。
* **メリット:** 数千のサブドメインを1行で表現できるためリストサイズを大幅に削減でき、トラッキング企業がランダム生成する使い捨てサブドメインにも強力に対抗できます。
* **デメリット**：AdGuard HomeやPi-holeなどの対応するリゾルバ環境が必須です。また、ルートドメインを指定すると、同じドメインを利用している正常なCDNや別サービスまで一括遮断してしまう過剰ブロックのリスクが高まります。

### ABP形式のDNSブロックリスト
Adblock PlusやuBlock Originなどのブラウザ向け構文を、DNSレイヤー向けに応用した形式です。

* **挙動・特徴**： `||example.com^` でドメイン全体をブロックし、`@@||example.com^` で例外処理（ホワイトリスト化）を行います。
* **メリット**：ブロックと例外ルールを複雑に組み合わせて制御できるため、フィルタのメンテナンス性が非常に高く、ブラウザ用とDNS用のリスト管理を共通化しやすいです。
* **デメリット:** 構文が複雑なため、システム側での解析（パース）に高い処理オーバーヘッドが発生します。また、ブラウザ用のURLパス指定構文をそのままDNSに流用すると、意図せぬ広範囲のブロッキングを引き起こす危険性があります。

---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

各アプリの仕様に基づき、ブロック率と正常なサイトの維持（誤爆回避）を両立するための最適なリストを1つずつ選定しました。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスするDNSブロッキング特化のリストです。

* **メリット**：DNSレイヤー向けのABP構文を最適化して使用しており、AdGuard for Androidの最新機能（高度な正規表現や例外ルールなど）をフル活用できるため、単体で軽量かつ最も高い精度を発揮します。
* **デメリット**：personalDNSfilterなど、高度なABP構文の解析を完全にサポートしていない他社製アプリにインポートすると、パースエラーを起こすか、本来のブロック性能を発揮できない場合があります。

### HaGeZi's Pro DNS Blocklist（personalDNSfilter向け）
現在のコミュニティにおけるデファクトスタンダードとされる統合リストです。モバイル環境でもより高いブロック効果を得るため、このProバージョンが推奨されます。

* **メリット**：強力なホワイトリストシステムにより高いブロック率を保ちながら誤爆が極めて少なく、開発者の対応も迅速です。Hostsや単一ドメイン形式など、シンプルなフォーマットでの配布が充実しているため、高度な構文を処理できないアプリでも安定して読み込めます。
* **デメリット**：Ultimateなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する可能性があります。そのため、ブロック率と安定性のバランスが取れたProバージョンの選定が重要となります。

---

## 3. アプリ別の最適な構成案（最終結論）

* **AdGuard for Androidの場合**：アプリのネイティブな解析能力を最大限に引き出せる **「AdGuard DNS filter」** を単体で使用します。
* **personalDNSfilterの場合**：複雑なABP構文の処理制限を回避するため、シンプルで互換性の高いドメイン形式で配布されており、効果と安定性のバランスに優れた **「HaGeZi's Pro DNS Blocklist」** を単体で指定します。

---

## ソース・参考文献

以下のリンクは、本レポートの作成にあたりGoogle検索の検索結果から取得した情報源です（すべてのURLについてリンク切れがないことを確認済みです）。

**Hosts vs Wildcard / ABP構文に関する議論（Google検索結果より）**
* [Reddit（r/pihole）-  What are the similarities and differences between a hosts file and pi-hole](https://www.reddit.com/r/pihole/comments/nw9b9w/what_are_the_similarities_and_differences_between/)
* [GitHub - DRSDavidSoft/additional-hosts](https://github.com/DRSDavidSoft/additional-hosts)
* [Reddit（r/pihole）-  Blocklist Syntax (Hosts vs ABP list)](https://www.reddit.com/r/pihole/comments/11spawr/blocklist_syntax/)
* [Reddit（r/pihole）-  Support AdGuard's DNS filtering rules syntax?](https://www.reddit.com/r/pihole/comments/n2gfeu/support_adguards_dns_filtering_rules_syntax/)

**厳選DNSブロックリストの公式リポジトリ（Google検索結果より）**
* [AdGuard SDNSFilter](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS  Blocklists](https://github.com/hagezi/dns-blocklists)
