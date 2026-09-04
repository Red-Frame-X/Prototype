# DNS Blocklist 調査メモ

DNSブロックリストの形式、候補、ブラウザ用コンテンツブロッカーとの役割分担について、自分の環境で選定・切り分けするときに参照する個人用メモです。

> [!NOTE]
> この文書は自分の学習・設定見直し用であり、一般向けの製品選定ガイドや推奨構成を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。実際にリストを変更するときは、使用時点の公式資料、リスト作者の公開情報、実環境のログで再確認します。

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

---

## 1. DNSブロックリストの主要フォーマット比較

### Hostsファイル形式

各OSが外部DNSへ問い合わせる前に参照する、ローカルの名前解決ファイルに基づいたレガシーな形式です。

* **挙動・特徴**：`0.0.0.0 example.com`のようにIPとドメインを記述し、完全一致でのみ機能します。
* **メリット**：外部リゾルバや専用の解析エンジンなしに、多くのOSやデバイスで扱えます。意図しないサブドメインを巻き込む過剰ブロックが起こりにくい点もあります。
* **デメリット**：サブドメインを個別に記載する必要があるため、ファイルサイズが大きくなりやすく、OSのパース遅延やメモリ消費が増える場合があります。また、ワイルドカードや例外ルールを記述できません。

### ドメインのみ（Domains only）

IPアドレスやフィルタ修飾子を付けず、ブロック対象のドメインを1行に1件ずつ記述するシンプルな形式です。

* **挙動・特徴**：`example.com`や`ads.example.com`のようにドメイン名だけを記述します。親ドメインの指定時にサブドメインも対象となるかは、使用するDNSブロッカーの実装に依存します。
* **メリット**：構文が単純でファイルサイズを抑えやすく、多くのDNSブロッカーで読み込めます。IPアドレスを含むHosts形式より変換や管理がしやすい場合があります。
* **デメリット**：例外ルールや正規表現などの高度な制御を記述できません。また、サブドメインの扱いが製品ごとに異なるため、自分の利用環境で仕様を確認する必要があります。

### ABP形式のDNSブロックリスト

uBlock OriginやAdGuard等のブラウザ向け拡張機能で使われる構文を、DNSレイヤー向けに最適化または流用した形式です。

* **挙動・特徴**：`||example.com^`でドメイン全体をブロックし、`@@||example.com^`で例外処理を行います。
* **メリット**：ブロックと例外ルールを組み合わせて制御でき、対応エンジンでは保守しやすくなります。
* **デメリット**：対応する解析エンジンが必要です。DNSフィルタが解釈できるのは製品が対応する構文だけであり、URLパスやリソース種別を扱うブラウザ向けルールをそのまま流用しても同じ結果にはなりません。

AdGuard公式のDNS filtering syntaxでは、Adblock-style、`/etc/hosts`、domains-onlyの3方式を明示的に区別しています。ブラウザ用EasyList等を無変換でDNSへ投入すると、未対応modifierを含むルールは無視される場合があります。自分のメモでは、DNS用リストを「ブラウザ用フィルタの縮小版」ではなく、DNSで評価できる情報だけを使う別レイヤーのルールセットとして扱います。

---

## 2. 自分の環境で比較している候補

ここでは、自分がAdGuard for AndroidとpersonalDNSfilterで比較する際の候補を記録しています。一般的な「最適解」を示すものではなく、端末性能、必要なサービス、誤ブロックの許容度によって選択は変わります。

### AdGuard DNS filter（AdGuard for Androidでの比較候補）

AdGuard公式がメンテナンスする、DNSブロッキング特化のリストです（SDNSFilter）。

* **確認用URL**：[AdGuard DNS filter（Optimized）](https://filters.adtidy.org/android/filters/15_optimized.txt)
* **利点として見ている点**：AdGuard DNSフィルタリング向けに保守され、ブロックと例外をAdGuardのDNSフィルタ構文で配布しているため、AdGuard製品との構文互換性を確認しやすい。
* **注意点**：personalDNSfilterや初期のPi-holeなど、高度なABP構文の解析を完全にサポートしない他製品へそのまま読み込むと、構文や例外の扱いが異なる可能性があります。

### HaGeZi's Normal DNS Blocklist（personalDNSfilterでの比較候補）

複数ソースを統合し、用途別の強度と複数の配布形式を提供するコミュニティ管理リストです。Normalは作者が「balanced protection」と位置付ける中間的な選択肢です。

* **確認用URL**：[HaGeZi's Normal DNS Blocklist（Domains only）](https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt)
* **利点として見ている点**：許可リストと偽陽性対応の仕組みが公開され、domains-onlyを含む複数形式からクライアントに合うものを選べる。
* **注意点**：Ultimateなど強度の高い版ほど、スマートフォンのバックグラウンド通信やアプリの正常動作を巻き込む可能性が高くなります。自分の環境では、比較基準としてNormalを使い、必要性を確認できた場合だけ強度変更を検討します。

---

## 3. 自分の構成メモ

### AdGuard for Android

自分が構成を切り分けるときは、まず**AdGuard DNS filter**単体の状態を基準にします。

* **利点**：アプリとフィルタの保守元が同じため、構文差による問題を切り分けやすい。
* **欠点**：AdGuard固有の構文や運用へ依存する部分があり、別の軽量DNSアプリへ移行すると同じルールセットをそのまま使えない場合がある。

### personalDNSfilter

自分のpersonalDNSfilter環境では、複雑なABP構文の互換性問題を避けるため、シンプルなdomains-only形式の**HaGeZi's Normal DNS Blocklist**を比較基準にしています。

* **利点**：単純な入力形式で、ABP固有構文の互換性を考慮する必要が少ない。
* **欠点**：例外を同じファイル内で表現できず、親ドメインとサブドメインの扱いはpersonalDNSfilter側の仕様に依存する。

---

## 4. ブラウザ用コンテンツブロッカーとの併用メモ

ブラウザ用コンテンツブロッカーとDNSブロックは、同じものを二重に動かす構成ではありません。DNSは名前解決段階、uBlock OriginやAdGuard Browser Extension等はブラウザ内のリクエスト・DOM・スクリプトレット等を扱います。

### 自分が利点として見ている点

* ブラウザ外のアプリ通信にもDNSレベルの遮断を適用できる
* 既知の広告・トラッキングドメインを早い段階で落とせる
* ブラウザ側はURLパス、リソース種別、要素隠蔽、スクリプトレット等の細かい処理に集中できる

### 自分が注意している点

* DNSで先に遮断された通信はブラウザ側Loggerに現れず、原因追跡が難しくなる場合がある
* 同じサービスを両レイヤーで例外化しないと復旧できないことがある
* 強いDNSリストを追加しすぎると、アプリのログイン、通知、決済、CDN等まで巻き込む可能性がある

### 自分が誤ブロックを切り分ける順序

1. ブラウザ用ブロッカーを1つに絞る
2. 追加フィルタを最小構成へ戻す
3. DNSブロックを一時的に外して再現性を確認する
4. ブラウザ側Logger / AdGuard Filtering logとDNS側ログを別々に確認する
5. 原因レイヤーが分かった後に最小の例外ルールを作成する

uBlock Origin公式は、uBOと別のブラウザ用コンテンツブロッカーの併用を明確に非推奨としています。一方、DNSブロックは別レイヤーなので併用自体は可能です。自分の環境では、問題発生時に各レイヤーを切り離せる状態を維持します。

---

## 参照している資料

仕様の確認には、各プロジェクトの公開資料を優先します。

**形式と構文**

* [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)
* [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
* [uBlock Origin README — 他のコンテンツブロッカーとの併用について](https://github.com/gorhill/uBlock/blob/master/README.md)

**フィルタの公式リポジトリ**

* [AdGuard SDNSFilter (AdGuard DNS filter)](https://github.com/AdguardTeam/AdGuardSDNSFilter)
* [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)
