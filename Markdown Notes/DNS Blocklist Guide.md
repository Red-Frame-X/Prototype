# DNS Blocklist Guide

DNSブロックリストのガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202610210008 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---


## 0. DNS Blocklist（DNSBL）の基礎

### はじめに：DNSとブロックリストを知る

**DNS（Domain Name System）** は、インターネット上の名前を調べる仕組みです。たとえば **ドメイン** は `example.com` のような名前で、接続先の名前（ホスト名）として使われます。アプリが接続するときは、通常、この名前から **IPアドレス（通信先を示す数値の住所）** を調べます。この処理を **名前解決** と呼び、問い合わせを受けて調べるDNSサーバーを **DNSリゾルバ** と呼びます。[DNSの基本仕様](https://www.rfc-editor.org/rfc/rfc1034.html)

**DNSブロック** は、この名前解決の段階で、接続させたくない名前への応答を制御する方法です。**DNSブロックリスト（blocklist／遮断リスト）** は、その判定に使うドメインやルールの一覧です。**フィルタ** は、通信を許可・遮断するためのルール、またはルール集を指します。**allowlist（許可リスト）** は、遮断対象から外すための例外です。例外の優先順位は製品と構文に従います。

広告や、利用状況を収集する **トラッカー**、悪意のあるソフトウェアである **マルウェア** に関係するドメインがリストにあれば、そこへ接続する前の名前解決段階で遮断できます。ただし、リストにない相手や、このDNSフィルタを経由しない通信には効きません。

DNSブロックはドメイン単位です。ページ内の広告枠を消したり、同じホスト名の特定のURLだけを止めたりする処理は、後述するブラウザ用コンテンツブロッカーが担当します。DNSブロックだけで、すべての広告・追跡・マルウェアを防げるわけではありません。

**読む順番**：0章で仕組み → 1章で形式と強さ → 2章でリスト選び → 3章で導入 → 4章でDNS設定 → 5章でブラウザとの併用と不具合対処 → 6章で安全性の限界、の順に進んでください。はじめはAdGuard for AndroidかpersonalDNSfilterのどちらかを選び、基本リスト1つで動作を確認します。

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

#### 縦に追ってみる

```text
通常：
アプリ・ブラウザ
  ↓ 接続先の名前を調べる
DNS問い合わせ → DNSリゾルバ
  ↓
IPアドレス取得
  ↓
サーバーへ接続

DNSブロック時（概念図）：
アプリ・ブラウザ
  ↓
DNS問い合わせ
  ↓
DNSフィルタがブロックリスト・例外と照合
  ├─ 対象でない → 通常の名前解決 → 接続
  └─ 対象である → 遮断用の応答など → 接続を防ぐ
```

これは代表的な流れを示す図です。端末内で判定するか、DNSサーバー側で判定するか、問い合わせと応答のどちらを調べるかは実装で異なります。キャッシュ（以前の回答の一時保存）や既存の接続があると、操作のたびに新しいDNS問い合わせが発生するとは限りません。NXDOMAINは「名前が存在しない」、REFUSEDは「問い合わせを拒否」というDNS応答コードです。[AdGuardの構文と応答制御](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)

### DNSブロックでできること / できないこと

表中のHTMLはページの構造を記述する言語、CSSは見た目を指定する仕組みです。JavaScriptはページの動作を制御する言語で、scriptlet（スクリプトレット）はブロッカーがページへ適用する小さなスクリプトを指します。これらによるページ内の調整は、DNSで名前を判定する処理とは別です。

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

**hosts（ホスツ）** は、ホスト名とIPアドレスの対応を端末内で指定するファイルです。**サブドメイン** は、`example.com` に対する `ads.example.com` のように、左側へ名前を付けたものです。リストのファイル形式と、アプリがその内容をどう解釈するかは分けて考えます。

### Hostsファイル形式
各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**： `0.0.0.0 example.com` のようにIPとドメインを記述します。標準的なOSのhostsファイルではホスト名の完全一致で適用されます。DNSブロッカーが取り込む場合は、その実装のサブドメイン判定に従います。
* **メリット**：hosts形式は広く利用されています。ただし、OSのhostsファイルを編集できる権限が必要で、Androidなどでは通常のアプリからシステムファイルを書き換えられません。DNSブロッカーに読み込ませる場合は、そのアプリの対応形式と動作に従います。標準的なOSのhostsのように完全一致で適用される場合は、意図しないサブドメインを巻き込む過剰ブロック（誤爆）が起こりにくい点も優れています。
* **デメリット**：標準的なOSのhostsファイルではサブドメイン（例: `a.example.com`, `b.example.com`）をすべて個別に記載する必要があるため、ファイルサイズが数MB〜数十MBレベルに肥大化しやすく、OSのパース遅延やメモリ消費の増大を招きます。また、標準的なhostsファイル自体にはAdblock Plus形式の例外ルール等はありません。なお、読み込むアプリ側が独自構文を追加している場合は別です。

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

### 3形式の早見表

以下は[AdGuard公式構文](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)と[personalDNSfilterの判定処理](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/BlockedHosts.java)に基づく比較です。ABPはAdblock Plus由来の構文を指し、DNS製品がブラウザ向け機能すべてに対応するという意味ではありません。

| 観点 | Hosts形式 | Domains only | Adblock-style / ABP系DNS構文 |
| :--- | :--- | :--- | :--- |
| 例 | `0.0.0.0 example.com` | `example.com` | `\|\|example.com^` |
| 仕組み | IPと名前の対応を書く。ブロッカーへの取り込み時は独自の解釈もある | 名前を1行に1件書く | 名前の一致範囲や例外を記号で指定 |
| 長所 | OSのhostsでも利用でき、対応製品が多い | 単純で管理しやすい | 対応製品では配下の一括指定・例外が書ける |
| 短所 | 標準hostsでは配下を個別記載。IP指定の扱いも製品差がある | 適用範囲が製品に依存。形式自体に例外はない | 記号や対応修飾子の確認が必要 |
| サブドメイン | OS標準hosts・AdGuardのhosts構文では別扱い。personalDNSfilterの取り込みでは親も照合 | AdGuardでは別扱い。personalDNSfilterでは親も照合 | AdGuardの `\|\|example.com^` は配下も対象 |
| 例外 | 標準形式にはない。アプリ側で管理 | 形式自体にはない。アプリ側で管理 | AdGuardでは `@@\|\|example.com^` など |
| 対応例 | OSのhosts、AdGuard DNS構文対応製品、personalDNSfilter | AdGuard DNS構文対応製品、personalDNSfilter | AdGuard for Android / Home / DNS。ただし修飾子には製品差あり |
| 初心者の扱いやすさ | IP行を自分で書くより、対応アプリで購読すると扱いやすい | personalDNSfilterで購読する開始例に向く | AdGuardでDNS用リストを購読し、必要時だけ例外を作ると扱いやすい |

**`example.com`、`0.0.0.0 example.com`、`||example.com^` を一括置換しても同じ意味にはなりません。** AdGuard公式ではhosts行の任意IPへの書き換え例はAdGuard Home向けで、Private AdGuard DNSでは遮断になると明記されています。Androidを含む全製品が任意IPへの書き換えまで同じように扱う、と推測しないでください。

personalDNSfilterでは、購読リストにも親ドメイン照合が適用されます。`BlockedHosts.contains()` は問い合わせ名から左端のラベルを順に外して照合します。したがって、購読した `example.com` は通常 `a.example.com` にも効きます。独自例外の詳細は3章を参照してください。

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

### 「強さ」と「品質」を分けて考える

**ブロック件数が多いリストほど優秀とは限りません。** 同じ利用目的に対して、不要な通信を止めつつ、必要な通信を壊さないことが大切です。

| 観点 | 初心者向けの読み方 |
| :--- | :--- |
| ブロック率 | 観測した問い合わせのうち遮断された割合。端末の使い方やアプリの再試行にも左右され、安全性の点数ではない |
| False Positive（偽陽性・誤ブロック） | 必要な通信を誤って遮断すること。ログインや画像表示の不具合につながる |
| False Negative（偽陰性・見逃し） | 防ぎたい通信が通ること。未登録ドメインなどが原因になる |
| リストサイズ・重複 | 行数は保護の広さと同じではない。同じドメインの重複やサブドメイン表現でも件数は変わる |
| 更新頻度・保守 | 最終更新だけでなく、誤ブロック報告への対応や不要ドメインの整理も確認する |
| Allowlist | 必要な通信を戻す仕組み。リスト作者の除外方針と、自分の端末の例外を区別する |
| アプリ互換性 | 普段のログイン、通知、決済などが動くか。利用者の環境でも結果が変わる |
| 端末負荷・クライアントの処理能力 | 更新・索引作成・検索の実装、メモリ、ストレージによって扱える規模が異なる |

「最大」「Ultimate」は、すべての環境で快適になるという保証ではありません。広告と正常な機能が通信先を共有していると、ログイン、プッシュ通知、決済、CDN（画像や動画などを各地のサーバーから配信する仕組み）、アプリ内コンテンツ、API（アプリとサービスがデータをやり取りする窓口）まで止まる場合があります。[HaGeZiの強度・機能破損リスク](https://github.com/hagezi/dns-blocklists/blob/main/CHEATSHEET.md#cheat_multi)

最初は控えめな構成で、普段使う機能が動くか確認します。強度を上げる場合も1つずつ変更し、変更前後のログと使い勝手を比較してください。

### 複数リストを併用するときの注意
複数リストの併用にはカバー範囲を補完できる利点がありますが、重複ドメインが増え、読み込み時間・メモリ使用量・更新負荷・誤ブロック原因の特定難易度が上がる可能性があります。特に、複数ソースを統合・最適化したリスト同士をさらに重ねても、増える保護範囲が小さい一方で切り分けが難しくなる場合があります。

HaGeZiの主要なMultiリストは Multi LIGHT / Multi NORMAL / Multi PRO / Multi PRO++ / Multi ULTIMATE が段階的に積み上がる構成で、作者は最初の5種類について「いずれか1つを選ぶ」前提を明記しています。サイズ最適化版も通常版へ重ねるのではなく代替として扱います。

#### 重ねる前に確認すること

同じドメインを3つのリストで遮断しても、そのドメインへの遮断が3倍強くなるわけではありません。統合リストには複数ソースの整理や重複除去を保守元へ任せられる利点がありますが、見逃しや誤ブロックがなくなる保証はありません。

1. 基本リストを1つ決め、現在の設定と例外を保存する。
2. 追加リストが補う目的を確認する。Multi同士の重ね掛けと、TIFのような別用途の追加を区別する。
3. 1つだけ追加し、更新完了・負荷・必要なアプリの動作を確認する。
4. 不具合時は直前の追加を一時的に戻し、どのリストで何が遮断されたか調べる。
5. 例外が他のリストにも効くか確認する。ルール優先順位により、許可を追加するだけで復旧するとは限らない。

重複除去の有無やメモリへの影響はクライアント次第です。統合後に重複が消えても、ダウンロード・更新時の処理が不要になるわけではありません。[HaGeZiの併用方針](https://github.com/hagezi/dns-blocklists/blob/main/CHEATSHEET.md#quickguide)


---

## 2. AdGuard for Android / personalDNSfilter 向け厳選リスト

ここでは保守元、形式、利用環境との互換性が明確な基本候補と、脅威対策を補う追加候補を示します。「最適」は端末性能、必要なサービス、誤ブロックの許容度で変わるため、ログを確認しながら選択してください。

### AdGuard DNS filter（AdGuard for Android向け）
AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **購読用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)

* **メリット**：AdGuard DNSフィルタリング向けに保守され、ブロックと例外をAdGuardのDNSフィルタ構文で配布しています。AdGuard製品との構文互換性を確認しやすい候補です。
* **デメリット**：personalDNSfilterなど、AdGuardのAdblock-style DNS構文をそのまま解釈する設計ではない他社製アプリへ投入すると、意図した例外・修飾子が反映されない可能性があります。利用先が受理する形式へ合わせる必要があります。

#### AdGuardアプリ・DNSサービス・ブラウザ用フィルタの関係

AdGuard for Androidはフィルタを読み込んで処理するアプリ、AdGuard DNS filterはそのDNS保護で利用できるルール集、AdGuard DNSはDNSサービスです。3つは別のものです。[公式DNS保護説明](https://github.com/AdguardTeam/KnowledgeBase/blob/master/docs/adguard-for-android/features/protection/dns-protection.md)

SDNSFilterの[公式README](https://github.com/AdguardTeam/AdGuardSDNSFilter)は、Base / Tracking Protection / Mobile Ads / EasyList / EasyPrivacyなどをDNS向けに簡略化したフィルタと説明しています。ブラウザ用フィルタ全体をそのままDNSで使う構成ではありません。基本の広告ブロック構文への対応が必要で、ドメインだけ抽出すると例外などの意味を失う可能性があります。

AdGuard DNS filtering syntaxはAdblock-style、Hosts、Domains onlyを区別します。AndroidでもDNS用の入力欄で使います。ただし、共通文書に載る `$client` などの一部修飾子はHome / DNS専用です。ブラウザ用の要素非表示ルールはDNS欄へ追加しません。

### HaGeZi's Multi NORMAL（personalDNSfilter向け）
HaGeZiのMultiリストは、調査時点で Multi LIGHT / Multi NORMAL / Multi PRO / Multi PRO++ / Multi ULTIMATE の5段階が提供されています。公式READMEではおおむね、Lightは最小限、Multi NORMALは緩やか〜バランス、Proはバランス、Pro++はバランス〜攻撃的、Ultimateは攻撃的という位置付けで、強度が上がるほど機能破損のリスクも高くなると説明されています。作者のCheat Sheetでは「Pro + TIF」が強いバランス型の推奨例として示されていますが、Multi NORMALはより保守的に始めたいユーザー向けの開始候補として位置付けられます。
複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Multi NORMALは作者のCheat Sheetで「Relaxed to Balanced / Low」と位置付けられる、控えめ〜バランス型の選択肢です。

* **購読用URL**：[HaGeZi's Multi NORMAL（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)

* **メリット**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べます。
* **デメリット**：Multi ULTIMATEなどの最も強力なバージョンを使用すると、スマートフォンのバックグラウンド通信やアプリの正常な挙動を阻害する「過剰ブロック」の可能性が高まります。そのため、ブロック率と安定性のバランスが取れた「Multi NORMAL」から開始し、必要に応じて調整するのが安全です。

#### HaGeZiの主要リストを選ぶ目安

| リスト | 作者の強度 / 機能破損リスク | 選ぶときの目安 |
| :--- | :--- | :--- |
| Light | Relaxed / Minimal | 軽量・保守的。Normalでも支障がある場合や低メモリ環境の候補 |
| Normal | Relaxed to Balanced / Low | バランスを取りつつ控えめに開始。常時管理者がいない環境にも作者が案内 |
| Pro | Balanced / Low to moderate | 作者の推奨デフォルト。例外を調整できる管理者がいる環境向け |
| Pro++ | Balanced to Aggressive / Moderate | 強力。問題発生時に調整できる経験者向け |
| Ultimate | Aggressive / High | 非常に強力。正常機能への影響も許容して調整する熟練者向け |

これは作者の[Cheat Sheet](https://github.com/hagezi/dns-blocklists/blob/main/CHEATSHEET.md#cheat_multi)の分類であり、第三者による精度ランキングではありません。本ガイドではNormalの開始例を維持します。作者がPro + TIFを推奨していることと、初心者がNormalから段階的に導入することは、目的が異なります。Light以外のMini版は各強度のサイズ最適化版で、通常版との併用は不要です。

### HaGeZi's Threat Intelligence Feeds - medium version (best for browser/mobile ad blockers)

脅威対策を補うTIFのmedium版です。[HaGeZi公式README](https://github.com/hagezi/dns-blocklists#tifmedium)では、フル版を扱いにくいブラウザ・モバイル向けブロッカー用に、主要なフィードへ絞った版として案内されています。

* **AdGuard for Android用（Adblock形式）**：
  ```
  https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/tif.medium.txt
  ```
* **personalDNSfilter用（Domains only形式）**：
  ```
  https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/tif.medium-onlydomains.txt
  ```

同じmedium版の配布形式が異なるため、使用するアプリに合うURLを選びます。

見出しの「best for browser/mobile ad blockers」は公式の版名に由来し、すべてのモバイル端末で最適という保証ではありません。公式READMEにはiOS版AdGuardでは大きすぎること、AdGuard Homeでは最低1 GB RAMが必要との注意があります。この数値をAndroid版やpersonalDNSfilterの必要メモリへ流用しないでください。mediumでも負荷が大きい場合は、公式が案内するTIF Miniなどの小さい代替版を検討します。基本構成へ必須として同時導入するのではなく、動作確認後の追加候補として扱います。


---

## 3. アプリ別の構成例

### AdGuard for Androidの場合
まずは **「AdGuard DNS filter」** 単体から開始するか、より広いカバー範囲を求める場合は **「HaGeZi's Multi NORMAL」** を選択肢にします。HaGeZi公式はAdblock形式をAdGuard対応として案内しており、Multi NORMALを「Relaxed/Balanced」、機能破損リスクを「Low」と位置付けています。両方を同時に追加すると対象ドメインが重複する可能性があるため、まずはいずれか1つから開始し、Recent activityで誤ブロックを確認しながら運用する構成が切り分けやすくなります。
* **AdGuard DNS filter のメリット**：アプリとフィルタの保守元が同じで、構文差による問題を切り分けやすくなります。
* **AdGuard DNS filter のデメリット**：AdGuard向けの例外や構文を含むため、将来別のDNSクライアントへ移行する場合は、移行先が対応する形式を確認する必要があります。
* **HaGeZi's Multi NORMAL のメリット**：広告・トラッカー・テレメトリ・フィッシング・マルウェア等を対象とするMultiリストで、AdGuardで利用できるAdblock形式が公式に提供されています。
* **HaGeZi's Multi NORMAL のデメリット**：AdGuard DNS filterと併用するとカバー範囲の重複が生じる可能性があり、誤ブロック発生時の原因特定も複雑になります。

### personalDNSfilterの場合
複雑なAdblock-style構文の互換性問題を避けるため、シンプルで互換性の高いドメイン形式で配布されている **「HaGeZi's Multi NORMAL」** を単体で指定します。これは「最強」構成ではなく、誤ブロックを抑えながら運用を始めやすくするための保守的な開始例です。
* **メリット**：単純な入力形式で、AdGuard/ABP固有構文の互換性を考慮する必要がありません。
* **デメリット**：ダウンロードするリスト自体には例外ルールを含められないため、例外が必要な場合はpersonalDNSfilterの `additionalHosts.txt` 側で個別に管理します。公式の `additionalHosts.txt` 例では、`!` によるホワイトリスト、`*` ワイルドカード、`>` によるカスタムIPマッピングがサポートされています。これはAdblock Plusの `@@||example.com^` 等とは別のpersonalDNSfilter独自構文です。
* **競合時の優先順位**：公式サンプルでは、カスタムIPマッピング → ワイルドカードなしの明示的なblacklist / whitelist → ワイルドカードblacklist / whitelist → ダウンロード済みblocklist の順で優先されます。

#### personalDNSfilterの例外を小さく作る

`additionalHosts.txt` は、購読リストを上書きするための少量の自分用設定です。公式サンプルは **巨大なリストをここへ追加しないこと** を明記しています。大量のドメインは購読URLとして設定します。[公式サンプル](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/assets/additionalHosts.txt)

```text
# 以下は説明用。必要な行だけを自分の環境に合わせて使う
ads.example.com
!login.example.com
*tracker.example.net
!trusted.example.net
>router 192.168.2.1
```

* `ads.example.com`：その名前と配下を遮断する。
* `!login.example.com`：その名前と配下を許可する。`!example.com` より範囲を絞れる。
* `*tracker.example.net`：`*` は文字列に一致するワイルドカード。単なるサブドメイン指定より広く一致し得るため、最初は明示的なホスト名を優先する。
* `!trusted.example.net`：ワイルドカードなしの許可例。親ドメインのルールより具体的なルールがあれば、そちらが優先される。
* `>router 192.168.2.1`：名前を指定IPへ割り当てるカスタムIPマッピング。広告対策の例外ではなく、例示IPが自宅ルーターのIPとは限らない。マッピングでも `*` が使えるが、用途がなければ設定しない。

**AdGuardでは行頭 `!` はコメントです。personalDNSfilterでは許可です。** `@@||example.com^` をpersonalDNSfilterへ貼り付けたり、`!example.com` をAdGuardの許可ルールとして使ったりしないでください。

前述の優先順位は公式サンプルの説明です。さらに[ソースの `contains()`](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/BlockedHosts.java)では、問い合わせ名から親へ進み、各名前で明示ルール → ワイルドカード → 購読リストを順に調べ、判定が見つかると返します。そのため「親への許可が、購読リスト中のより具体的な子ドメインを必ず許可する」とは限りません。ログで止まった正確な名前を特定し、まずその名前で例外を試してください。

#### 大きなリストを読み込むとき

[DNSFilterManager.java](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/DNSFilterManager.java)では、購読データから索引を作成して重複を除き、永続化後は全構造をメモリへ載せない形で読み直します。照合結果のキャッシュもあります。これは大規模リストへの工夫であり、端末負荷がなくなる保証ではありません。初回・更新時のダウンロード、索引作成、ストレージ、メモリの負荷は残ります。端末ごとの上限件数・処理時間は一次情報では一律に確認できません。

購読リストの取り込みと `additionalHosts.txt` のワイルドカード機能も同一ではありません。確認した取り込み処理では先頭の `*.` は親ドメインへ変換しますが、その他のワイルドカード行はスキップします。任意のABPルールを変換できるという意味ではありません。

### TIF mediumで脅威対策を補う場合

上記の基本構成に脅威対策を追加する場合は、セクション2の **「HaGeZi's Threat Intelligence Feeds - medium version」** を追加候補にします。

* **AdGuard for Android**：「DNS通信を保護 > DNSフィルタ」にAdblock形式の `adblock/tif.medium.txt` を追加します。
* **personalDNSfilter**：購読するDNSブロックリストにDomains only形式の `wildcard/tif.medium-onlydomains.txt` を追加します。

追加後はログと普段使うアプリの動作を確認し、問題があればTIF mediumを一時的に無効にして原因を切り分けます。

### 初めて導入するときの手順

以下は設定の順序です。画面名や保存・更新の操作はアプリのバージョンと言語で異なるため、表示に合わせてください。OSのhostsファイルを書き換える必要はありません。

#### AdGuard for Androidへの導入

1. 現在のDNSサーバー、DNSフィルタ、ユーザールールを記録し、変更前に普段使うサイトやアプリが動くことを確認する。
2. 「保護（Protection）→ DNS保護（DNS protection）」を開き、有効にする。DNSサーバーとDNSフィルタは別項目として確認する。
3. DNSフィルタでAdGuard DNS filterが既に有効なら、同じURLを重複追加しない。なければ2章の購読URLをDNSフィルタとして追加する。
4. HaGeZi Normalを代わりに使う場合はAdGuard向けAdblock形式を選ぶ。下記URLは既存のDomains only版とは別形式である。

   ```text
   https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/multi.txt
   ```

5. 更新が完了し、エラーがないことを確認する。Recent activityでDNS保護が処理した通信を確認する。
6. ログイン、画像・動画、通知、決済画面など日常の機能を確認する。TIF mediumなどの追加は、この確認後に1つずつ行う。

AdGuard DNSユーザールールの説明用例：

```text
! 以下は説明用。遮断と許可の例を同時に追加する必要はない
||ads.example.com^
@@||login.example.com^
```

上は `ads.example.com` と配下の遮断、下は `login.example.com` と配下の例外です。ホスト名1つだけの許可を表現するなら `@@|login.example.com|` のように両端を固定できます。まずログからルールを作り、適用範囲を確認してください。通常の例外より `$important` 付きの遮断が優先されるなど、例外が効かないケースもあります。[公式構文](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)

#### personalDNSfilterへの導入

1. 現在の購読URL、DNS設定、`additionalHosts.txt` の内容を保存する。
2. 購読フィルタの設定欄へ、2章のHaGeZi Multi NORMAL（Domains only）のURLを指定する。初回の動作確認では、他の購読リストを一時的に外すか無効にして構成を把握する。
3. リストを更新し、ダウンロードと索引作成が完了するまで確認する。巨大なリストを `additionalHosts.txt` へ貼り付けない。
4. 保護を有効にし、問い合わせのログと普段使うアプリの動作を確認する。リストを取得できただけでは、そのアプリのDNS通信が保護を経由している確認にはならない。
5. 不具合が出たら5章で切り分け、必要な名前だけを `!login.example.com` のように追加する。保存後はアプリの再読み込み・再起動の案内に従い、例外が反映されたかログで確認する。

personalDNSfilterの手順は公開ソースから確認できる設定要素を基にしています。実機の画面操作は未検証です。AndroidのVPN枠を使う構成では、他のVPN方式のアプリと同時に使えるかも事前に確認してください。


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

ブラウザ用コンテンツブロッカーとDNSブロックは、同じものを二重に動かす構成ではありません。DNSは名前解決段階、uBlock OriginやAdGuard Browser Extension等はブラウザ内のリクエスト・DOM（ページ内の要素の構造）・スクリプトレット等を扱います。

### ブラウザ用ブロッカーを選ぶとき

**DOM** は、ページの見出し・画像・広告枠などをブラウザが扱うための構造です。**要素非表示（コスメティックフィルタ）** は不要な枠を隠す処理、**スクリプトレット** はページの挙動を調整するためにブロッカーが適用する小さなスクリプトです。DNSブロックにはページのDOMやURLパスは見えません。

| 製品 | ブラウザ内で担当する範囲・注意 |
| :--- | :--- |
| uBlock Origin（uBO） | URLやリクエストのフィルタ、要素非表示、スクリプトレットなど。ブラウザ対応状況は公式READMEを確認 |
| uBlock Origin Lite（uBOL） | MV3の宣言的APIでブラウザがルールを処理。CSS / JSによる処理もあるが、権限・動作モードや機能はuBOと同一ではない |
| AdGuard Browser Extension | URLリクエスト制御、要素非表示、スクリプトレットなど。ブラウザやMV2 / MV3で使える機能と制限が異なる |

根拠：[uBO README](https://github.com/gorhill/uBlock/blob/master/README.md)、[uBOL README](https://github.com/uBlockOrigin/uBOL-home/blob/main/README.md)、[AdGuard拡張README](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/README.md)。uBOLを含め、すべての製品で同じカスタムルール・Logger・DOM操作が使えると考えないでください。

例として、DNSで `ads.example.com` を止めてもページに空の広告枠が残る場合があります。ブラウザ側では、その枠を要素非表示で隠せます。また `example.com/ads/` だけを対象にするURLルールも、対応するブラウザ用ブロッカーの役割です。

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

このuBO公式の注意を「DNSとの併用を公式に推奨している」という意味に読み替えないでください。ここで示すDNSとの構成はレイヤーの違いに基づく運用例で、HaGeZi公式FAQにもDNSとブラウザの併用説明があります。AdGuard for AndroidはDNS保護以外のWebフィルタリングも持つため、アプリ全体を「DNSだけの製品」として扱わず、どの保護機能を有効にしているかを確認します。

#### 症状から確認する場所を探す

次の表は原因の候補です。症状だけで誤ブロックと断定しないでください。

| 症状 | 調査する候補 |
| :--- | :--- |
| Webサイトが開かない | DNS遮断、上流DNS、ブラウザの通信ルール、サイト側の障害 |
| アプリにログインできない | 認証先やAPIの遮断、カスタムルール、認証サービスの障害 |
| 画像だけ表示されない | 画像CDNのDNS遮断、ブラウザの画像リクエスト遮断・要素非表示 |
| 動画が再生できない | 動画配信先やAPIの遮断、ブラウザ側スクリプトレット・通信ルール |
| プッシュ通知が届かない | 通知先のDNS遮断、アプリの通知権限、OSの省電力・バックグラウンド制限 |
| 決済できない | 決済先・認証先・APIの遮断、サービス障害。調査時に支払いを繰り返して二重決済しない |
| 広告を消したらページの一部も消えた | ブラウザの要素非表示・自作ルール。DNSで必要データを止めた結果、表示が崩れる場合もある |

#### 一度に1か所だけ変えて切り分ける

前述の手順を具体的に実施する場合は、各変更の前後で同じ操作を試します。改善しなければ設定を元に戻してから次へ進みます。複数のレイヤーが同時に原因になる場合もあるため、結果は記録してください。

1. **記録する**：症状、時刻、対象アプリ・URL、最近追加したリスト、現在の例外を控える。ログを開いて問題を1回再現する。
2. **DNSブロックを調べる**：ブラウザ側は変えず、ローカルのDNSフィルタだけ短時間停止して比較する。上流のフィルタリングDNSにも遮断があれば、ローカル停止だけでは解除されない。DNSサーバーの変更はフィルタ停止と別のテストにする。
3. **ブラウザ用ブロッカーを調べる**：DNS設定を戻し、問題のサイトだけで拡張の保護を短時間停止して比較する。改善したら、通信ルール、要素非表示、スクリプトレットのどれが関係するか、その製品のログや報告機能で調べる。
4. **カスタムフィルタを調べる**：自分で追加したフィルタ・ユーザールールを1つずつ一時停止する。DNS用とブラウザ用を別々に調べ、購読リストならどのリスト由来かも確認する。
5. **Allowlist / 例外設定を調べる**：製品に合う構文か、正しい設定欄か、対象名は正しいか、強いルールや上流DNSが残っていないか確認する。ブラウザで許可してもDNSで許可したことにはならない。
6. **その他のネットワーク設定を調べる**：VPN、プロキシ、OSのプライベートDNS、ブラウザ独自の暗号化DNS、Wi-Fiや回線、サイト障害を順に確認する。DNSログにない通信は別経路やキャッシュも疑う。キャッシュの影響を考慮して再接続・アプリ再起動などを試す。
7. **原因にだけ例外を作る**：問題発生時刻のログと照合し、たとえば `login.example.com` だけを許可する。無関係な `example.com` 全体、CDN全体、通知サービス全体をまとめて許可しない。子ドメインへの適用範囲も確認する。
8. **復旧を確認して保護を戻す**：一時停止した機能を戻し、必要な操作と他の普段使う機能を確認する。試験用例外は不要なら削除し、継続する例外は理由と日付を残す。リスト作者へ報告するときは再現手順と該当ルールを用意し、ログの個人情報は伏せる。

すべての保護を恒久的に無効にして完了としないでください。必要な通信先が確認できない場合は、推測で広い許可を足さず、いったん直前の動作していた構成へ戻して調査します。


---

## 6. プライバシーとセキュリティ上の位置付け

DNS blocklistでトラッキングドメインへの接続自体を防ぐことはできますが、それだけでDNS問い合わせ内容をDNS resolverから隠したり、ISP等から通信先を完全に隠したりすることはできません。暗号化DNSはDNS問い合わせの転送経路を保護し、VPNはより広い範囲の通信経路をトンネル化します。役割は重なって見えても同一ではありません。

また、malware / phishingドメインを含むリストは接続前の防御層として役立ちますが、DNS blocklistだけでマルウェア対策が完結するわけではありません。リストに未収載の新規ドメイン、同一ドメイン上の悪性パス、侵害済み正規サイト等には限界があります。

**DNSブロックはアンチウイルスの代替ではありません。** すべてのマルウェアやトラッキングを防げず、同じドメインで配信される広告・追跡と正常なコンテンツを安全に分離できない場合があります。IPアドレスへ直接接続する通信や、別のDNS経路を使うアプリにも、想定どおり適用できるとは限りません。OS・アプリの更新や端末の保護と組み合わせて使ってください。[HaGeZi公式の限界・無保証の説明](https://github.com/hagezi/dns-blocklists#disclaimer)

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


**今回の補足説明に対応する一次情報**
* [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)：0章のDNS・名前解決・キャッシュの基本。
* [AdGuard for Android DNS protectionの公式原稿](https://github.com/AdguardTeam/KnowledgeBase/blob/master/docs/adguard-for-android/features/protection/dns-protection.md)：2〜4章のDNS server / filters / user rules、設定への入口。
* [AdGuard for Android Statisticsの公式原稿](https://github.com/AdguardTeam/KnowledgeBase/blob/master/docs/adguard-for-android/features/statistics.md)：Recent activityでの状態確認とルール作成。
* [personalDNSfilter BlockedHosts.java](https://github.com/IngoZenz/personaldnsfilter/blob/master/app/src/main/java/dnsfilter/BlockedHosts.java)：1・3章の親ドメイン照合、具体的な名前からの判定順序。索引作成・重複除去は既掲のDNSFilterManager.javaも参照。
* [HaGeZi FAQ](https://github.com/hagezi/dns-blocklists/blob/main/FAQ.md)：形式、リスト併用、選択方針の詳細。強度表は既掲のCheat Sheetに対応。
* [uBlock Origin Lite README](https://github.com/uBlockOrigin/uBOL-home/blob/main/README.md)：5章の宣言的処理・CSS / JSによるフィルタリング。
* [AdGuard Browser Extension README](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/README.md)：5章のリクエスト制御・要素非表示・スクリプトレットとブラウザ別の制限。

確認日：2026年10月20日。公開ドキュメントと取得時点の公式ソースに基づきます。個別端末の性能・画面操作・各サイトでの結果は保証しません。Issueの一般ユーザー投稿を公式仕様の根拠には使用していません。
