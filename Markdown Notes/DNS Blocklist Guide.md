# DNS Blocklist Guide
DNSブロックリストのガイド

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-UserScript-Regex-Markdown](https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown) |
| **License** | CC0-1.0 |
| **Version** | 20260703 |

この備忘録は CC0 ライセンスの下で提供します。（This work is licensed under CC0 1.0 Universal）
* [コモンズ証 - CC0 1.0 全世界 - Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/deed.ja)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

※ 記述内容はコミュニティの知見や専門家の技術的見地（各種コンテンツブロッカー開発者の知見等）の査読を取り入れた検証に基づくものですが、すべての環境での完全な動作を保証するものではありません。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット**：外部リゾルバや専用の解析エンジンなしに、ほぼ全てのOSやデバイスでネイティブに動作する圧倒的な互換性を持ちます。意図しないサブドメインを巻き込む過剰ブロック（誤爆）が起こりにくい点も優れています。
* **デメリット**：サブドメイン（例: `a.example.com`, `b.example.com`）をすべて個別に記載する必要があるため、ファイルサイズが数MB〜数十MBレベルに肥大化しやすく、OSのパース遅延やメモリ消費の増大を招きます。また、ワイルドカードや例外ルール（ホワイトリスト）の記述が一切できません。

### ワイルドカードドメイン（Wildcard Domains）
特定のドメインとその配下にあるすべてのサブドメインを包括的に対象とする形式です。

* **挙動・特徴**： `*.example.com` （または正規表現）のように記述し、関連するサブドメインをすべてブロック対象とします。
* **メリット**：数千のサブドメインを1行のルールで表現できるため、リストのファイルサイズを劇的に削減できます。トラッキング企業がランダムに自動生成する使い捨てサブドメインにも強力に対抗可能です。
* **デメリット**：AdGuard Home、Pi-hole、dnsmasqなど、ワイルドカードや正規表現に対応するリゾルバ環境が必須です。また、ルートドメインを指定すると、同じドメインを利用している正常なCDNや別サービスまで一括遮断してしまう過剰ブロックのリスクが高まります。

### ABP形式のDNSブロックリスト
uBlock OriginやAdGuard等のブラウザ向け拡張機能で使われる構文を、DNSレイヤー向けに最適化（または流用）した形式です。

* **挙動・特徴**： `||example.com^` でドメイン全体をブロックし、`@@||example.com^` で例外処理（ホワイトリスト化）を行います。
* **メリット**：ブロックと例外ルールを複雑に組み合わせて制御できるため、フィルタのメンテナンス性が非常に高く、ブラウザ用とDNS用のリスト管理を共通化しやすいです。
* **デメリット**：システム側での解析（パース）に専用のエンジンが必要となり、高い処理オーバーヘッドが発生します。また、ブラウザ用のURLパス指定（例: `/ads.js`）はDNSレイヤーでは機能しないため、ブラウザ用のリストをそのままDNSに流用すると、意図せぬ広範囲のブロッキングやパースエラーを引き起こす危険性があります。

---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

各アプリの仕様・パース能力に基づき、ブロック率と正常なサイトの維持（誤爆回避）を両立するための最適なリストを1つずつ選定しました。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **メリット**：DNSレイヤー向けに不要な構文を削ぎ落とした独自のABP構文を使用しており、AdGuard for Androidの最新パースエンジンをフル活用できます。高度な例外ルールや修飾子を解釈できるため、単体で軽量かつ最も高い精度を発揮します。
* **デメリット**：personalDNSfilterや初期のPi-holeなど、高度なABP構文の解析を完全にサポートしていない他社製アプリにインポートすると、フォーマットエラーを起こすか、本来のブロック性能（特に例外ルール）が適用されず誤爆が増える場合があります。

### HaGeZi's Pro DNS Blocklist（personalDNSfilter向け）
現在のコミュニティにおけるデファクトスタンダードとされる統合リストです。モバイル環境の安定性を保ちつつ高い効果を得るため、Proバージョンが推奨されます。

* **メリット**：強力なホワイトリストシステムが組み込まれており、高いブロック率を保ちながら誤爆が極めて少ないのが特徴です。Hostsや単一ドメイン形式など、シンプルなフォーマットでの配布が充実しているため、高度な構文を処理できない軽量アプリでも極めて安定して読み込めます。
* **デメリット**：Ultimateなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する「過剰ブロック」の可能性が高まります。そのため、ブロック率と安定性のバランスが取れた「Pro」バージョンの選定が必須となります。

---

## 3. アプリ別の最適な構成案（最終結論）

### AdGuard for Androidの場合
アプリのネイティブな解析能力を最大限に引き出せる **「AdGuard DNS filter」** を単体で使用します。
* **メリット**：アプリの開発元が提供する専用フィルタであるため、ソフトウェアとの親和性が最も高く、無駄なリソース消費なしに高度なブロッキングが可能です。
* **デメリット**：AdGuardの独自エコシステムに依存するため、将来的に他の軽量DNSアプリに乗り換える際、同じルールセットをそのまま持ち出すことが難しい場合があります。

### personalDNSfilterの場合
複雑なABP構文の処理制限を回避するため、シンプルで互換性の高いドメイン形式で配布されている **「HaGeZi's Pro DNS Blocklist」** を単体で指定します。
* **メリット**：アプリ側のパース負荷（CPUおよびメモリ消費）を最小限に抑えられるため、バッテリー消費が厳しく問われるAndroidの常駐アプリとして極めて安定して稼働します。
* **デメリット**：ドメイン完全一致ベースのリストとなるため、高度な正規表現を用いたブロックが行えず、一部の巧妙なトラッキングドメインをブロックしきれないケースが稀に発生します。

---

## ソース・参考文献

以下のリンクは、本ドキュメントの作成および技術検証にあたり、Google検索の検索結果（検索エンジンから抽出した情報）として取得・参照したソースです。

**Hosts vs Wildcard / ABP構文に関する議論（Google検索結果より）**
* [Reddit（r/pihole）：What are the similarities and differences between a hosts file and pi-hole](https://www.reddit.com/r/pihole/comments/nw9b9w/what_are_the_similarities_and_differences_between/)
* [GitHub - DRSDavidSoft/additional-hosts](https://github.com/DRSDavidSoft/additional-hosts)
* [Reddit（r/pihole）：Blocklist Syntax (Hosts vs ABP list)](https://www.reddit.com/r/pihole/comments/11spawr/blocklist_syntax/)
* [Reddit（r/pihole）：Support AdGuard's DNS filtering rules syntax?](https://www.reddit.com/r/pihole/comments/n2gfeu/support_adguards_dns_filtering_rules_syntax/)

**厳選DNSブロックリストの公式リポジトリ（Google検索結果より）**
* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
