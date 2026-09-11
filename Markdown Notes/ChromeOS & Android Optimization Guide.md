# ChromeOS & Android Optimization Guide

ChromeOS & Android 最適化ガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260910 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## Subscription

この項目は、自身が実際に利用していたサブスクリプションで発生した不具合と、その際に行った対処の記録を中心にまとめています。

Googleの多くのサービスでは、年額サブスクリプションを「月額 × 約10か月分」の料金で提供しており、割安になります。
ただし、年額サブスクリプションは一度支払うと、契約期間の途中で解約しても日割り計算による払い戻しは行われません。

**利用中のサブスクリプション一覧**

サブスクリプションの購読基準は、「ITインフラになり得ているか」と「保守の負担比率が、対処 > 利用になった」という点に尽きます。

* Amazon Prime（年額）
* ChMate スタンダードプラン（月額）
* ChatGPT Plus（月額）
* Google AI Plus 400 GB（年額）
* [mond｜Kdroidwinさんのメンバーシップ](https://mond.how/ja/kdroidwin)（Premium / 月額）
* 𝕏プレミアム ベーシック（年額）
* YouTube Premium（年額）

トラブルを完全に避けるのであれば、サブスクリプションを一切契約しないのが最も安全です。
必要があって契約する場合は、トラブルの原因となりやすい携帯キャリア提供の月額オプションは避け、公式サイトが直接提供するプランを必要最小限選ぶのが無難です。

* **参考**： [【お詫び/復旧】一部お客さまでドコモからご契約いただいたYouTube Premiumがご利用いただけない事象について](https://www.docomo.ne.jp/info/notice/page/251222_03_m.html)

**Google One メンバーシップ・不具合**

下記の購入特典と有料プランにおいて、システム上で重複適用できてしまう不具合がありました。

1. Chromebook Plusの購入特典（Google AI Pro 2 TB 1年間無料）
2. docomo 爆アゲ セレクション Google One ベーシック（100 GB）（月額）
3. Google AI Pro 2 TB（年額）

確認を怠ってこれらを重複適用してしまうと、Google OneのWebサイトでストレージ容量を正確に取得できず、コンテンツの確認ができなくなるエラーが発生します。
* [エラー画像 1](https://imgur.com/CNjeA2d)
* [エラー画像 2（500エラー）](https://imgur.com/cIa8AJt)
* [エラー画像 3（Androidアプリ ロック状態）](https://imgur.com/a/u9f38dX#3dKWbMC)

> **※ 以下2つの記述は未検証の仮説です**
> 1. Google One メンバーシップ プランの管理権限が、Googleからdocomoの月額プランへ一時的に移管されます。
> 2. dポイントが付与される代わりに、Google公式のAIプラン（Google AI Plus 200 GB〜）が選択できなくなります。（[参考URL](https://one.google.com/about/plans?hl=ja-JP&g1_landing_page=0)）

不具合の内容をコピー＆ペーストできるようメモにまとめ、お問い合わせ方法からチャットを選択します。
* **[Google One ヘルプ > お問い合わせ](https://support.google.com/googleone/gethelp)**

なお、ahamo回線契約者は基本的にdocomoのサポートを受けることができません。
* **[docomo｜ご意見・ご要望](https://www.docomo.ne.jp/support/inquiry/feedback/?hl=ja-JP)** > 「ご意見・ご要望はこちら 開く+」をクリックする。

過去に同様の不具合がなかったかRedditで検索したところ、既存の有料プランにGoogle Pixelの購入特典を重複適用した結果、Google One メンバーシップに問題が発生したという報告も見つかりました。

* **[Google free trial Premium AI Scam](https://www.reddit.com/r/GoogleOne/comments/1dqzsrv/google_free_trial_premium_ai_scam/)**
  * 2TBの年額プランを契約中のユーザーが、Pixel 8 Pro購入特典の4ヶ月無料トライアルを有効化した事例です。
  * 元のプランが上位プランに強制変換された結果、支払い済みの契約期間が大幅短縮され、元のプランの権利が失われたと報告されています。

問題が長期化し、週に1回程度のペースでGoogle One ヘルプに進捗確認を求めても、定型文の返答しか得られないことがあります。GoogleとdocomoにGoogle Oneの不具合を問い合わせても、たらい回しにされるばかりで、問題が解決する見込みがありませんでした。

これらの不具合の多くは、複数の契約がGoogle One メンバーシップ上で重複し、システムが矛盾した状態に陥ることが原因と考えられます。Google One メンバーシップの重複を整理した後、時間の経過をおいても、それで全ての不具合が直るかどうかは分かりません。

**❗️いずれにしろ、Google One メンバーシップに適用する購入特典や有料プランは1つに限定するべきです。**

**Google One メンバーシップ・不具合解決の最終手段**

[Google アカウント](https://myaccount.google.com/) > データとプライバシー > サービスを削除 > パスワード・PIN入力による本人確認 > 「Google サービスの削除」から「Google One」の情報削除を選択することで、Google One メンバーシップの初期化が可能です。
ただし、Google Oneに関連付けられた情報はすべて削除されるため、Google One メンバーシップに付与されていた購入特典や有料プランも失われます。

* **参考サイト**： [r/GoogleOne｜Reddit](https://www.reddit.com/r/GoogleOne/)

---

## ChromeOS Chrome 拡張機能
* **[Manifest V2 のサポート タイムライン（サポート終了済み）](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)**

 ChromeOSおよびChromeブラウザにおいて、Manifest V2拡張機能のサポートは順次終了・無効化されています。

* **[Chrome Web Store 拡張機能](https://chromewebstore.google.com/category/extensions)**

Chrome Web Store外から入手した拡張機能を自分でインストールする場合は、拡張機能ページの右上にあるトグルスイッチを切り替えて**デベロッパーモード**を有効にする必要があります。

**Violentmonkeyの導入**

ブラウザに機能を追加するUserScriptを管理・実行できる無料のブラウザ拡張機能です。
* **[Violentmonkey](https://chromewebstore.google.com/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)**
* **[Greasy Fork‐便利で安全なUserScript](https://greasyfork.org/ja)**

Chrome 138以降でViolentmonkeyを使用する場合は、`chrome://extensions` > Violentmonkey > **詳細** > **ユーザースクリプトを許可する** を有効にします。Chrome 138未満では、代わりに拡張機能ページの**デベロッパーモード**を有効にする必要があります。

**❗️留意点**

 以下のブラウザ拡張機能やUserScriptは、全てをインストールして使用しているわけではありません。ブラウザ拡張機能やUserScriptを入れすぎると競合を起こしてトラブルの原因になるため、数は少なければ少ないほど良いです。

* ブラウザ拡張機能の競合を疑いながらも問題の切り分けができず、AdGuard Filtersに相談したIssuesの例。：[#228169](https://github.com/AdguardTeam/AdguardFilters/issues/228169)
* Gmail 「システムで問題が発生しました（#2014）」。：[Reddit報告例](https://www.reddit.com/r/techsupport/comments/1b4rocl/oops_the_system_encountered_a_problem_2014/?tl=ja)

▶ 断定はできませんが、[PhotoShow](https://chromewebstore.google.com/detail/photoshow/mgpdnhlllbpncjpgokgfogidhoegebod) が原因だった可能性が高く、同様のブラウザ拡張機能でも同じ不具合が起きるかもしれません。

### コンテンツブロック・プライバシー関連
* **[AdGuard Extra](https://github.com/AdguardTeam/AdGuardExtra)**：Anti-Adblocker対策用UserScript ‐ 対象サイトはFacebook、Twitchなど。
* **[AdGuard ブラウザ拡張機能 MV3対応版](https://chromewebstore.google.com/detail/adguard-%E5%BA%83%E5%91%8A%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=ja)**：Chrome 拡張機能。（詳細後述）
* **[tinyShield](https://github.com/List-KR/tinyShield/blob/main/README.ja.md)**：Ad-Shield対策用UserScript ‐ Tampermonkeyで購読して、Manifest V3のフィルタ更新制限を回避する。
* **[uBlacklist](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)**：検索結果のフィルタリング、指定したサイトの検索結果を非表示にする。（詳細後述）

### YouTube関連
* **[Enhancer for YouTube™](https://chromewebstore.google.com/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle)**：再生速度や音量のマウス制御、画質固定、テーマ変更、コメント非表示などYouTubeの機能を強化する。
* **[SponsorBlock for YouTube-動画の広告シーンを自動スキップ](https://chromewebstore.google.com/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone)**：YouTube動画内のスポンサーセグメントやイントロなどを、ユーザーの報告に基づき自動でスキップする。

### ショッピング関連
* **[Amazonレビュー信頼度判定 & 無限スクロール（サクラ識別 / 品質チェック）](https://greasyfork.org/ja/scripts/561755)**：Amazonのレビュアー投稿履歴を分析し、信頼度をS〜Dランクで視覚化。信頼度フィルタリング機能や、レビュー一覧の無限スクロール化も提供。
* **[Condler](https://chromewebstore.google.com/detail/condler/ejjdbndmmongojeafjlilnchmkppbeap)**：Amazon検索結果の左側サイドバーに、並び替えやAmazon公式出品のみに絞り込むボタンを追加する。
* **[Keepa - Amazon Price Tracker](https://chromewebstore.google.com/detail/keepa-amazon-price-tracke/neebplgakaahbhdphmkckjjcegoiijjo)**：Amazon商品の価格履歴グラフをページ上に表示し、設定した価格になると通知を受け取れる。
* **[Knockoff — Amazon Brand Filter](https://chromewebstore.google.com/detail/knockoff-%E2%80%94-amazon-brand-f/pjgickchbiikhdfpmecaabkphmofpdce)**：Amazon検索結果に大量に現れるアルファベット羅列の無名・大量生産ブランドを識別し、ラベル付けや薄く表示することで商品の視認性を向上させる。
* **[Enhancer for Amazon™](https://chromewebstore.google.com/detail/enhancer-for-amazon/fenpmbpefjpljmgmdcnghfjhcaeebemj)**：商品詳細ページでKeepaの価格履歴グラフを目立たせ、価格推移を確認しやすくする。

### ブックマーク関連
* **[Floccus Bookmarks Sync](https://chromewebstore.google.com/detail/floccus-bookmarks-sync/fnaicdnakpoinaagfhnjfhecicmdaadc)**：WebDAV、Nextcloud、Google Driveなどを利用してブラウザのブックマークを同期する。

### セキュリティ関連
* **[Bitwarden Password Manager](https://chromewebstore.google.com/detail/bitwarden-password-manager/nngceckbapebfimnlniiiahkandclblb)**：パスワードマネージャー。
* **[Malwarebytes Browser Guard](https://chromewebstore.google.com/detail/malwarebytes-browser-guard/ihcjicgdanjaechkgeegckofmomjlfmg)**：悪質なWebサイト、フィッシング、トラッキング等をブロックする。
* **[uBO Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)**：Chromium系ブラウザ向けのManifest V3対応コンテンツブロッカー。

### ブラウザ操作・UI関連
* **[Copy Link Text](https://chromewebstore.google.com/detail/copy-link-text/lckkkbmbafkfhilbmgojlibmjimcicbb)**：リンクテキストを右クリックメニューからコピーする。
* **[Enable Copy](https://chromewebstore.google.com/detail/enable-copy/cjlaemndpmlilamgkeikjpbjpenfmhbo)**：コピー禁止ページで選択・コピーを可能にする。
* **[Tab Suspender](https://chromewebstore.google.com/detail/tab-suspender/fiabciakcmgepblmdkmemdbbkilneeeij)**：一定時間使っていないタブを休止してメモリ消費を抑える。

### Android アプリ

#### 有償版 AdGuard for Android

AdGuard for AndroidはローカルVPN方式を利用します。HTTPSフィルタリングを有効化すると、対象アプリの暗号化通信を検査するためにユーザーCA証明書を利用します。証明書ピンニング等により一部アプリではHTTPSフィルタリングが利用できない場合があります。

#### personalDNSfilter

personalDNSfilterはローカルVPNとしてDNS問い合わせを処理し、ブロックリストに基づいてドメインを遮断します。ブラウザ内のAdGuard拡張機能と異なり、URLパスやDOM要素のフィルタリングは行いません。

#### 通知のサイレント化

Androidの通知設定では、端末・アプリ・通知カテゴリによって「サイレント」ではなく「マナー」など異なる名称が表示される場合があります。表示される選択肢に従ってください。

---

## Android 自動化

### MacroDroidからAdGuardのフィルタ更新を実行する

AdGuard for Androidでは、`com.adguard.android.receiver.AutomationReceiver` に `update` アクションを送ることで、外部オートメーションからフィルタ更新を実行できます。

安定運用を優先する場合は、VPN状態の変化をトリガーにせず、1日1回などの時刻トリガーで実行します。VPN再接続直後はサービス状態が安定していない場合があるため、必要に応じてAdGuardの再起動を挟んでから更新を実行します。

---

## ChromeOSアップデート

ChromeOSの手動更新・更新エラー時の切り分けについては、[`ChromeOS Manual Update and Troubleshooting.md`](ChromeOS%20Manual%20Update%20and%20Troubleshooting.md)に分離しています。

---

## 参考

- [Google ChromeOS Help](https://support.google.com/chromebook/)
- [Android Help](https://support.google.com/android/)
- [AdGuard Knowledge Base](https://adguard.com/kb/)
