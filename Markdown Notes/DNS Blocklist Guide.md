# DNS Blocklist Guide

DNSブロックリストのガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202609201658 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---


## 0. DNS Blocklist（DNSBL）の基礎

### 「DNSBL」という言葉の意味
「DNSBL」は歴史的には、スパム送信元などのIPアドレスやドメインをDNS経由で照会できる形で配布する **DNS-based Block List / DNS blacklist** を指してきました。RFC 5782では、DNSをブラックリスト／ホワイトリスト配布の事実上の標準手段として利用する仕組みが説明されています。一方、広告・トラッカー遮断の文脈では、一般に「DNS blocklist」は、DNS問い合わせ対象のドメインを照合し、広告・トラッカー・マルウェア等への接続をDNSレイヤーで制御するためのリストという意味で使われます。

このガイドでは後者、すなわち **広告・トラッカー・マルウェア等のドメインへの名前解決をDNSレイヤーで制御するためのブロックリスト** を中心に扱います。メールスパム対策で用いられるDNSBLとは技術的背景を共有しますが、用途・照会方法・運用方法は同一ではありません。

### DNSブロックの基本動作
通常は次のように名前解決が行われます。

`アプリ / ブラウザ → DNS問い合わせ → DNSリゾルバ → IPアドレス取得 → 接続`

DNSフィルタリングを挟む場合は、問い合わせ先ドメインをルールと照合してから応答します。

`アプリ / ブラウザ → DNS問い合わせ → DNSフィルタリング → 許可または遮断 → DNS応答`

通常時のイメージ：

`example.com → DNS問い合わせ → IPアドレス取得 → 接続`

ブロック時のイメージ：

`ads.example.com → DNS問い合わせ → DNSフィルタで遮断 → 接続不可`

遮断時の応答は製品によって異なります。たとえば、`0.0.0.0` や `::` を返す、NXDOMAINやREFUSED等の応答コードを返す、空の応答や独自のブラックホール応答へ置き換える、といった方式があります。したがって、「DNSブロック＝必ずNXDOMAINを返す」といった一般化はできません。

### DNSブロックでできること / できないこと

| 項目 | DNSブロック |
| :--- | :--- |
| 広告配信専用ドメインの遮断 | 可能 |
| トラッキング専用ドメインの遮断 | 可能 |
| 既知のマルウェア・フィッシングドメインの遮断 | リストに含まれていれば可能 |
| ブラウザ以外のAndroidアプリ等にも適用 | DNS経路を経由する構成なら可能 |
| URLパス単位の判定 | 不可 |
| 同一ホスト上の広告と正常コンテンツの区別 | 原則不可 |
| HTML要素の非表示 | 不可 |
| CSSによる要素隠蔽 | 不可 |
| scriptlet / JavaScriptによるページ挙動変更 | 不可 |

DNSは基本的にホスト名単位で判断するため、`example.com/ads/` と `example.com/content/` を安全に区別することはできません。同じホスト名から本編と広告が配信されるサービスでは、DNSだけで広告だけを選択的に遮断するのは困難です。このため、DNSブロックはブラウザ用コンテンツブロッカーの完全な代替ではありません。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット**：hosts形式は広く利用されています。ただし、OSのhostsファイルを編集できる権限が必要で、Androidなどでは通常のアプリからシステムファイルを書き換えられません。DNSブロッカーに読み込ませる場合は、そのアプリの対応形式と動作に従います。意図しないサブドメインを巻き込む過剰ブロック（誤爆）が起こりにくい点も優れています。
* **デメリット**：サブドメイン（例: `a.example.com`, `b.example.com`）をすべて個別に記載する必要があるため、ファイルサイズが数MB〜数十MBレベルに肥大化しやすく、OSのパース遅延やメモリ消費の増大を招きます。また、標準的なhostsファイル自体にはAdblock Plus形式の例外ルール等はありません。なお、読み込むアプリ側が独自構文を追加している場合は別です。

### ドメインのみ（Domains only）
IPアドレスやフィルタ修飾子を付けず、ブロック対象のドメインを1行に1件ずつ記述するシンプルな形式です。

* **挙動・特徴**： `example.com` や `ads.example.com` のようにドメイン名だけを記述します。AdGuard DNS filtering syntaxのdomains-onlyでは、`example.com` はそのドメインだけをブロックし、`www.example.com` は別扱いです。一方、personalDNSfilterの `additionalHosts.txt` では、明示的なホスト指定はそのホストとサブドメインに適用され、より具体的なルールがあればそちらが優先されます。このように親ドメインの扱いは製品・入力形式ごとに異なります。
* **メリット**：構文が単純でファイルサイズを抑えやすく、多くのDNSブロッカーで読み込めます。IPアドレスを含むHosts形式より再利用しやすく、リストの変換や管理も容易です。
* **デメリット**：リスト自体には例外ルールや正規表現などの高度な制御を記述できません。また、サブドメインの扱いが製品ごとに異なるため、利用環境の仕様確認が必要です。親ドメインを配下ごと遮断する実装では、正常なサービスまで巻き込む過剰ブロックにも注意が必要です。

### ABP形式のDNSブロックリスト
uBlock OriginやAdGuard等のブラウザ向け拡張機能で使われる構文の一部を、DNSレイヤー向けに制限して利用する形式です。

* **挙動・特徴**：AdGuard DNS filtering syntaxでは、`||example.com^` は `example.com` とそのサブドメインをブロックし、`@@||example.com^` は対応する範囲を例外化します。
* **メリット**：対応製品ではブロックと例外を同じルールセットで表現できます。
* **デメリット**：対応する解析エンジンが必要です。DNSフィルタが解釈できるのは製品が明示的に対応するDNS向け構文だけであり、URLパス、リソース種別、コスメティックフィルタ、スクリプトレット等のブラウザ向け構文をそのまま流用しても同じ結果にはなりません。

AdGuard公式のDNS filtering syntaxでは、Adblock-style、`/etc/hosts`、domains-onlyの3方式を明示的に区別しています。ブラウザ用EasyList等を無変換でDNSへ投入すると、未対応modifierを含むルールは無視される場合があります。DNS用リストは「ブラウザ用フィルタの縮小版」ではなく、DNSで評価できる情報だけを使う別レイヤーのルールセットとして扱います。

### 形式を選ぶときの実務的な基準

| 観点 | 確認内容 |
| :--- | :--- |
| 対応形式 | 使用するDNSブロッカーがその構文を解釈できるか |
| 保守状況 | 現在も更新されているか |
| 誤ブロック対応 | Issue、allowlist、例外申請などの窓口があるか |
| 強度 | Light / Balanced / Aggressive等の性格 |
| サイズ | 端末・クライアントに対して過大でないか |
| 例外機構 | allowlistやユーザールールで復旧できるか |
| 更新頻度 | 古い死活ドメインを放置していないか |
| ライセンス | 再配布・加工条件に問題がないか |

リスト数やエントリ数が多いほど品質が高いわけではありません。ソースの重複除去、dead domain cleanup、誤ブロック対応、allowlist管理、更新頻度、目的との一致を合わせて評価する必要があります。

### 複数リストを併用するときの注意
複数リストの併用にはカバー範囲を補完できる利点がありますが、重複ドメインが増え、読み込み時間・メモリ使用量・更新負荷・誤ブロック原因の特定難易度が上がる可能性があります。特に、複数ソースを統合・最適化したリスト同士をさらに重ねても、増える保護範囲が小さい一方で切り分けが難しくなる場合があります。

HaGeZiの主要なMultiリストは Light / Normal / Pro / Pro++ / Ultimate が段階的に積み上がる構成で、作者は最初の5種類について「いずれか1つを選ぶ」前提を明記しています。サイズ最適化版も通常版へ重ねるのではなく代替として扱います。

---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

ここでは保守元、形式、利用環境との互換性が明確な候補を1つずつ示します。「最適」は端末性能、必要なサービス、誤ブロックの許容度で変わるため、ログを確認しながら選択してください。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **購読用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)

* **メリット**：AdGuard DNSフィルタリング向けに保守され、ブロックと例外をAdGuardのDNSフィルタ構文で配布しています。AdGuard製品との構文互換性を確認しやすい候補です。
* **デメリット**：personalDNSfilterなど、AdGuardのAdblock-style DNS構文をそのまま解釈する設計ではない他社製アプリへ投入すると、意図した例外・修飾子が反映されない可能性があります。利用先が受理する形式へ合わせる必要があります。

### HaGeZi's Normal DNS Blocklist（personalDNSfilter向け）
HaGeZiのMultiリストは、調査時点で Light / Normal / Pro / Pro++ / Ultimate の5段階が提供されています。公式READMEではおおむね、Lightは最小限、Normalは緩やか〜バランス、Proはバランス、Pro++はバランス〜攻撃的、Ultimateは攻撃的という位置付けで、強度が上がるほど機能破損のリスクも高くなると説明されています。作者のCheat Sheetでは「Pro + TIF」が強いバランス型の推奨例として示されていますが、Normalはより保守的に始めたいユーザー向けの開始候補として位置付けられます。
複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Normalは作者が「balanced protection」と位置付ける中間的な選択肢です。

* **購読用URL**：[HaGeZi's Normal DNS Blocklist（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)

* **メリット**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べます。
* **デメリット**：Ultimateなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する「過剰ブロック」の可能性が高まります。そのため、ブロック率と安定性のバランスが取れた「Normal」バージョンから開始し、必要に応じて調整するのが安全です。

---

## 3. アプリ別の構成例

### AdGuard for Androidの場合
まずは **「AdGuard DNS filter」** 単体から開始します。これは唯一の正解ではなく、AdGuard製品との構文互換性と、誤ブロック時に原因を切り分けやすいことを重視した開始構成です。
* **メリット**：アプリとフィルタの保守元が同じで、構文差による問題を切り分けやすくなります。
* **デメリット**：AdGuard向けの例外や構文を含むため、将来別のDNSクライアントへ移行する場合は、移行先が対応する形式を確認する必要があります。

### personalDNSfilterの場合
複雑なAdblock-style構文の互換性問題を避けるため、シンプルで互換性の高いドメイン形式で配布されている **「HaGeZi's Normal DNS Blocklist」** を単体で指定します。これは「最強」構成ではなく、誤ブロックを抑えながら運用を始めやすくするための保守的な開始例です。
* **メリット**：単純な入力形式で、AdGuard/ABP固有構文の互換性を考慮する必要がありません。
* **デメリット**：ダウンロードするリスト自体には例外ルールを含められないため、例外が必要な場合はpersonalDNSfilterの `additionalHosts.txt` 側で個別に管理します。公式の `additionalHosts.txt` 例では、`!` によるホワイトリスト、`*` ワイルドカード、`>` によるカスタムIPマッピングがサポートされています。これはAdblock Plusの `@@||example.com^` 等とは別のpersonalDNSfilter独自構文です。
* **競合時の優先順位**：公式サンプルでは、カスタムIPマッピング → ワイルドカードなしの明示的なblacklist / whitelist → ワイルドカードblacklist / whitelist → ダウンロード済みblocklist の順で優先されます。

---

## 4. AdGuard for AndroidのDNS保護と暗号化DNS

AdGuard for AndroidのDNS protectionでは、**DNS server / DNS filters / user rules** を別々の要素として扱います。

* **DNS server**：DNS問い合わせをどこで解決するかを決める
* **DNS filter**：問い合わせ先ドメインをブロック・許可するためのルールセット
* **User rules**：ユーザーが独自に追加するDNSブロック／例外ルール

したがって、「DNSサーバー」と「DNSブロックリスト」は同じものではありません。フィルタリングDNSサーバー自体がblocklistを持つ場合もありますが、AdGuard for Android側でDNS filterを追加してローカルに判定する構成も可能です。

### DoH / DoT / DoQとの違い
DNS over HTTPS（DoH）、DNS over TLS（DoT）、DNS over QUIC（DoQ）は、DNS問い合わせ・応答の**転送経路を暗号化する技術**です。DNS blocklistは、**どのドメインを許可・遮断するかを決める仕組み**です。

そのため、

* DoH / DoT / DoQを使うだけで広告がブロックされるわけではない
* DNS blocklistを使うだけでDNS通信が暗号化されるわけではない
* VPNはさらに別の仕組みで、DNS暗号化やDNSブロックと同一ではない

という点に注意が必要です。

### Recent activityによる確認
AdGuard for Androidでは、Recent activity（旧Filtering log）から処理したリクエストを確認でき、block / allow状態や、どのアプリから発生した通信かを切り分ける手掛かりにできます。誤ブロック調査では、DNS側の遮断をRecent activityで確認し、必要ならユーザールールで最小限の例外を追加します。

---

## 5. ブラウザ用コンテンツブロッカーとの併用

ブラウザ用コンテンツブロッカーとDNSブロックは、同じものを二重に動かす構成ではありません。DNSは名前解決段階、uBlock OriginやAdGuard Browser Extension等はブラウザ内のリクエスト・DOM・スクリプトレット等を扱います。

### レイヤーごとの役割

| 項目 | DNSブロック | ブラウザ用コンテンツブロッカー |
| :--- | :--- | :--- |
| 主な判定単位 | ドメイン / ホスト名 | URL・リクエスト種別・DOM等 |
| ブラウザ外アプリへの適用 | 構成次第で可能 | 原則不可 |
| URLパス単位の制御 | 不可 | 可能 |
| 要素隠蔽 | 不可 | 可能 |
| scriptlet | 不可 | 対応製品では可能 |
| ログの確認先 | DNS側ログ | ブラウザ拡張側Logger等 |

### 併用の利点

* ブラウザ外のアプリ通信にもDNSレベルの遮断を適用できる
* 既知の広告・トラッキングドメインを早い段階で落とせる
* ブラウザ側はURLパス、リソース種別、要素隠蔽、スクリプトレット等の細かい処理に集中できる

### 併用の欠点

* ブラウザ側LoggerだけではDNS側の遮断ルールを特定できない。リクエストが記録されていてもDNS側ログとの照合が必要になる
* 同じサービスを両レイヤーで例外化しないと復旧できないことがある
* 強いDNSリストを追加しすぎると、アプリのログイン、通知、決済、CDN等まで巻き込む可能性がある

### トラブルシューティング

誤ブロックやアンチ広告ブロックを調査するときは、構成を一時的に単純化します。DNSキャッシュ、アプリ側キャッシュ、ブラウザ側キャッシュ、上流リゾルバのキャッシュやTTLにより、ルール変更後もしばらく挙動が残る場合がある点にも注意します。キャッシュの保持場所やクリア方法は環境ごとに異なるため、OSやアプリの仕様に従ってください。

1. ブラウザ用ブロッカーを1つに絞る
2. 追加フィルタを最小構成へ戻す
3. DNSブロックを一時的に外して再現性を確認する
4. ブラウザ側Logger / AdGuard Filtering logとDNS側ログを別々に確認する
5. 原因レイヤーが分かった後に最小の例外ルールを作成する
6. 一時的なallowlistで復旧するか確認する
7. 該当リストを特定し、必要なら作者のfalse positive報告窓口へ報告する

uBlock Origin公式は、uBOと別のブラウザ用コンテンツブロッカーの併用を明確に非推奨としています。一方、DNSブロックは別レイヤーなので併用自体は可能ですが、切り分け可能な構成にしておくことが重要です。

---

## 6. プライバシーとセキュリティ上の位置付け

DNS blocklistでトラッキングドメインへの接続自体を防ぐことはできますが、それだけでDNS問い合わせ内容をDNS resolverから隠したり、ISP等から通信先を完全に隠したりすることはできません。暗号化DNSはDNS問い合わせの転送経路を保護し、VPNはより広い範囲の通信経路をトンネル化します。役割は重なって見えても同一ではありません。

また、malware / phishingドメインを含むリストは接続前の防御層として役立ちますが、DNS blocklistだけでマルウェア対策が完結するわけではありません。リストに未収載の新規ドメイン、同一ドメイン上の悪性パス、侵害済み正規サイト等には限界があります。

### CNAME等の特殊ケース
CNAMEは別名から実体ホストへ名前解決する仕組みです。CNAMEを利用してfirst-party風に見せるトラッキングも存在しますが、CNAME応答をどこまで追跡・再評価するかはDNSクライアントやフィルタリング製品の実装によって異なります。したがって、「DNSブロッカーならすべてCNAME-based trackingを同じ方法で遮断できる」とは考えないでください。

---

## ソース・参考文献

仕様の確認には、各プロジェクトの公開資料を優先します。

**DNSBL / DNS / 暗号化DNS**
* [RFC 5782 — DNS Blacklists and Whitelists](https://www.rfc-editor.org/rfc/rfc5782.html)
* [RFC 6471 — Overview of Best Email DNS-Based List Operational Practices](https://www.rfc-editor.org/rfc/rfc6471.html)
* [RFC 8484 — DNS Queries over HTTPS (DoH)](https://www.rfc-editor.org/rfc/rfc8484.html)
* [RFC 7858 — DNS over TLS (DoT)](https://www.rfc-editor.org/rfc/rfc7858.html)
* [RFC 9250 — DNS over Dedicated QUIC Connections (DoQ)](https://www.rfc-editor.org/rfc/rfc9250.html)

**形式と構文**
* [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)
* [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
* [AdGuard for Android: Statistics / Recent activity](https://adguard.com/kb/adguard-for-android/features/statistics/)
* [personalDNSfilter additionalHosts.txt](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/assets/additionalHosts.txt)
* [personalDNSfilter DNSFilterManager.java](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/DNSFilterManager.java)
* [uBlock Origin README — 他のコンテンツブロッカーとの併用について](https://github.com/gorhill/uBlock/blob/master/README.md)

**フィルタの公式リポジトリ**
* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
* [HaGeZi Blocklists Cheat Sheet](https://github.com/hagezi/dns-blocklists/blob/main/CHEATSHEET.md)
