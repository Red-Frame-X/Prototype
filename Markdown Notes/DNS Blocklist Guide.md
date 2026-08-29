# DNS Blocklist Guide

DNSブロックリストのガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260829 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット**：外部リゾルバや専用の解析エンジンなしに、ほぼ全てのOSやデバイスでネイティブに動作する圧倒的な互換性を持ちます。意図しないサブドメインを巻き込む過剰ブロック（誤爆）が起こりにくい点も優れています。
* **デメリット**：サブドメイン（例: `a.example.com`, `b.example.com`）をすべて個別に記載する必要があるため、ファイルサイズが数MB〜数十MBレベルに肥大化しやすく、OSのパース遅延やメモリ消費の増大を招きます。また、ワイルドカードや例外ルール（ホワイトリスト）の記述が一切できません。

### ドメインのみ（Domains only）
IPアドレスやフィルタ修飾子を付けず、ブロック対象のドメインを1行に1件ずつ記述するシンプルな形式です。

* **挙動・特徴**： `example.com` や `ads.example.com` のようにドメイン名だけを記述します。親ドメインの指定時にサブドメインも対象となるかは、使用するDNSブロッカーの実装に依存します。
* **メリット**：構文が単純でファイルサイズを抑えやすく、多くのDNSブロッカーで読み込めます。IPアドレスを含むHosts形式より再利用しやすく、リストの変換や管理も容易です。
* **デメリット**：例外ルールや正規表現などの高度な制御を記述できません。また、サブドメインの扱いが製品ごとに異なるため、利用環境の仕様確認が必要です。親ドメインを配下ごと遮断する実装では、正常なサービスまで巻き込む過剰ブロックにも注意が必要です。

### ABP形式のDNSブロックリスト
uBlock OriginやAdGuard等のブラウザ向け拡張機能で使われる構文を、DNSレイヤー向けに最適化（または流用）した形式です。

* **挙動・特徴**： `||example.com^` でドメイン全体をブロックし、`@@||example.com^` で例外処理（ホワイトリスト化）を行います。
* **メリット**：ブロックと例外ルールを複雑に組み合わせて制御できるため、フィルタのメンテナンス性が非常に高く、ブラウザ用とDNS用のリスト管理を共通化しやすいです。
* **デメリット**：対応する解析エンジンが必要です。DNSフィルタが解釈できるのは製品が対応する構文だけであり、URLパスやリソース種別を扱うブラウザ向けルールをそのまま流用しても同じ結果にはなりません。

AdGuard公式のDNS filtering syntaxでは、Adblock-style、`/etc/hosts`、domains-onlyの3方式を明示的に区別しています。ブラウザ用EasyList等を無変換でDNSへ投入すると、未対応modifierを含むルールは誤ブロック防止のため無視される場合があります。DNS用リストは「ブラウザ用フィルタの縮小版」ではなく、DNSで評価できる情報だけを使う別レイヤーのルールセットとして扱います。

---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

ここでは保守元、形式、利用環境との互換性が明確な候補を1つずつ示します。「最適」は端末性能、必要なサービス、誤ブロックの許容度で変わるため、ログを確認しながら選択してください。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **購読用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)

* **メリット**：AdGuard DNSフィルタリング向けに保守され、ブロックと例外をAdGuardのDNSフィルタ構文で配布しています。AdGuard製品との構文互換性を確認しやすい候補です。
* **デメリット**：personalDNSfilterや初期のPi-holeなど、高度なABP構文の解析を完全にサポートしていない他社製アプリにインポートすると、フォーマットエラーを起こすか、本来のブロック性能（特に例外ルール）が適用されず誤爆が増える場合があります。

### HaGeZi's Normal DNS Blocklist（personalDNSfilter向け）
複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Normalは作者が「balanced protection」と位置付ける中間的な選択肢です。

* **購読用URL**：[HaGeZi's Normal DNS Blocklist（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)

* **メリット**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べます。
* **デメリット**：Ultimateなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する「過剰ブロック」の可能性が高まります。そのため、ブロック率と安定性のバランスが取れた「Normal」バージョンの選定が推奨されます。

---

## 3. アプリ別の構成例

### AdGuard for Androidの場合
まずは **「AdGuard DNS filter」** 単体から開始します。
* **メリット**：アプリとフィルタの保守元が同じで、構文差による問題を切り分けやすくなります。
* **デメリット**：AdGuardの独自エコシステムに依存するため、将来的に他の軽量DNSアプリに乗り換える際、同じルールセットをそのまま持ち出すことが難しい場合があります。

### personalDNSfilterの場合
複雑なABP構文の処理制限を回避するため、シンプルで互換性の高いドメイン形式で配布されている **「HaGeZi's Normal DNS Blocklist」** を単体で指定します。
* **メリット**：単純な入力形式で、ABP固有構文の互換性を考慮する必要がありません。
* **デメリット**：例外を同じファイル内で表現できず、親ドメインとサブドメインの扱いはpersonalDNSfilter側の仕様に依存します。

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
* [uBlock Origin README — 他のコンテンツブロッカーとの併用について](https://github.com/gorhill/uBlock/blob/master/README.md)

**フィルタの公式リポジトリ**
* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)