# DNS Blocklist Guide

DNSブロックリストのガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260908 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット**：外部リゾルバや専用の解析エンジンなしに、ほぼ全てのOSやデバイスでネイティブに動作する圧倒的な互換性を持ちます。意図しないサブドメインを巻き込む過剰ブロック（誤爆）が起こりにくい点も優れています。
* **デメリット**：サブドメイン（例: `a.example.com`, `b.example.com`）をすべて個別に記載する必要があるため、ファイルサイズが数MB〜数十MBレベルに肥大化しやすく、OSのパース遅延やメモリ消費の増大を招きます。また、標準的なhostsファイル自体にはAdblock Plus形式の例外ルール等はありません。なお、読み込むアプリ側が独自構文を追加している場合は別です。

### ドメインのみ（Domains only）
IPアドレスやフィルタ修飾子を付けず、ブロック対象のドメインを1行に1件ずつ記述するシンプルな形式です。

* **挙動・特徴**： `example.com` や `ads.example.com` のようにドメイン名だけを記述します。親ドメインの指定時にサブドメインも対象となるかは、使用するDNSブロッカーの実装に依存します。
* **メリット**：構文が単純でファイルサイズを抑えやすく、多くのDNSブロッカーで読み込めます。IPアドレスを含むHosts形式より再利用しやすく、リストの変換や管理も容易です。
* **デメリット**：リスト自体には例外ルールや正規表現などの高度な制御を記述できません。また、サブドメインの扱いが製品ごとに異なるため、利用環境の仕様確認が必要です。親ドメインを配下ごと遮断する実装では、正常なサービスまで巻き込む過剰ブロックにも注意が必要です。

### ABP形式のDNSブロックリスト
uBlock OriginやAdGuard等のブラウザ向け拡張機能で使われる構文の一部を、DNSレイヤー向けに制限して利用する形式です。

* **挙動・特徴**：AdGuard DNS filtering syntaxでは、`||example.com^` でドメインをブロックし、`@@||example.com^` で例外処理を行うAdblock-styleルールをサポートしています。
* **メリット**：対応製品ではブロックと例外を同じルールセットで表現できます。
* **デメリット**：対応する解析エンジンが必要です。DNSフィルタが解釈できるのは製品が明示的に対応するDNS向け構文だけであり、URLパス、リソース種別、コスメティックフィルタ、スクリプトレット等のブラウザ向け構文をそのまま流用しても同じ結果にはなりません。

AdGuard公式のDNS filtering syntaxでは、Adblock-style、`/etc/hosts`、domains-onlyの3方式を明示的に区別しています。ブラウザ用EasyList等を無変換でDNSへ投入すると、未対応modifierを含むルールは無視される場合があります。DNS用リストは「ブラウザ用フィルタの縮小版」ではなく、DNSで評価できる情報だけを使う別レイヤーのルールセットとして扱います。

---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

ここでは保守元、形式、利用環境との互換性が明確な候補を1つずつ示します。「最適」は端末性能、必要なサービス、誤ブロックの許容度で変わるため、ログを確認しながら選択してください。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **購読用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)

* **メリット**：AdGuard DNSフィルタリング向けに保守され、ブロックと例外をAdGuardのDNSフィルタ構文で配布しています。AdGuard製品との構文互換性を確認しやすい候補です。
* **デメリット**：personalDNSfilterなど、AdGuardのAdblock-style DNS構文をそのまま解釈する設計ではない他社製アプリへ投入すると、意図した例外・修飾子が反映されない可能性があります。利用先が受理する形式へ合わせる必要があります。

### HaGeZi's Normal DNS Blocklist（personalDNSfilter向け）
複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Normalは作者が「balanced protection」と位置付ける中間的な選択肢です。

* **購読用URL**：[HaGeZi's Normal DNS Blocklist（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)

* **メリット**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べます。
* **デメリット**：Ultimateなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する「過剰ブロック」の可能性が高まります。そのため、ブロック率と安定性のバランスが取れた「Normal」バージョンから開始し、必要に応じて調整するのが安全です。

---

## 3. アプリ別の構成例

### AdGuard for Androidの場合
まずは **「AdGuard DNS filter」** 単体から開始します。
* **メリット**：アプリとフィルタの保守元が同じで、構文差による問題を切り分けやすくなります。
* **デメリット**：AdGuard向けの例外や構文を含むため、将来別のDNSクライアントへ移行する場合は、移行先が対応する形式を確認する必要があります。

### personalDNSfilterの場合
複雑なAdblock-style構文の互換性問題を避けるため、シンプルで互換性の高いドメイン形式で配布されている **「HaGeZi's Normal DNS Blocklist」** を単体で指定します。
* **メリット**：単純な入力形式で、AdGuard/ABP固有構文の互換性を考慮する必要がありません。
* **デメリット**：ダウンロードするリスト自体には例外ルールを含められないため、例外が必要な場合はpersonalDNSfilterの `additionalHosts.txt` 側で個別に管理します。公式の `additionalHosts.txt` 例では、`!` によるホワイトリスト、`*` ワイルドカード、`>` によるカスタムIPマッピングがサポートされています。これはAdblock Plusの `@@||example.com^` 等とは別のpersonalDNSfilter独自構文です。

---

## 4. ブラウザ用コンテンツブロッカーとの併用

ブラウザ用コンテンツブロッカーとDNSブロックは、同じものを二重に動かす構成ではありません。DNSは名前解決段階、uBlock OriginやAdGuard Browser Extension等はブラウザ内のリクエスト・DOM・スクリプトレット等を扱います。

### 併用の利点

* ブラウザ外のアプリ通信にもDNSレベルの遮断を適用できる
* 既知の広告・トラッキングドメインを早い段階で落とせる
* ブラウザ側はURLパス、リソース種別、要素隠蔽、スクリプトレット等の細かい処理に集中できる

### 併用の欠点

* DNSで先に遮断された通信はブラウザ側Loggerに現れず、原因追跡が難しくなる場合がある
* 同じサービスを両レイヤーで例外化しないと復旧できないことがある
* 強いDNSリストを追加しすぎると、アプリのログイン、通知、決済、CDN等まで巻き込む可能性がある

### トラブルシューティング

誤ブロックやアンチ広告ブロックを調査するときは、構成を一時的に単純化します。

1. ブラウザ用ブロッカーを1つに絞る
2. 追加フィルタを最小構成へ戻す
3. DNSブロックを一時的に外して再現性を確認する
4. ブラウザ側Logger / AdGuard Filtering logとDNS側ログを別々に確認する
5. 原因レイヤーが分かった後に最小の例外ルールを作成する

uBlock Origin公式は、uBOと別のブラウザ用コンテンツブロッカーの併用を明確に非推奨としています。一方、DNSブロックは別レイヤーなので併用自体は可能ですが、切り分け可能な構成にしておくことが重要です。

---

## ソース・参考文献

仕様の確認には、各プロジェクトの公開資料を優先します。

**形式と構文**
* [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)
* [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
* [personalDNSfilter additionalHosts.txt](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/assets/additionalHosts.txt)
* [personalDNSfilter DNSFilterManager.java](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/DNSFilterManager.java)
* [uBlock Origin README — 他のコンテンツブロッカーとの併用について](https://github.com/gorhill/uBlock/blob/master/README.md)

**フィルタの公式リポジトリ**
* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)