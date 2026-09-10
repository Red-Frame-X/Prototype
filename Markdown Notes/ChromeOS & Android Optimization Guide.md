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
サブスクリプションの料金、年額割引、払い戻し条件はサービスごとに異なり、変更されることがあります。契約前に各サービスの公式料金ページと解約・返金条件を確認します。

**利用中のサブスクリプション一覧**

サブスクリプションの購読基準は、「ITインフラになり得ているか」と「保守の負担比率が、対処 > 利用になった」という点に尽きます。

* Amazon Prime（年額）
* ChMate スタンダードプラン（月額）
* ChatGPT Plus（月額）
* Google AI Plus 400 GB（年額）
* [mond｜Kdroidwinさんのメンバーシップ](https://mond.how/ja/kdroidwin)（Premium / 月額）
* 𝕏プレミアム ベーシック（年額）
* YouTube Premium（年額）

契約経路が増えるほど、請求元、解約窓口、特典の重複などを切り分ける手間が増えることがあります。公式サイト、アプリストア、携帯キャリア等のどの経路で契約するかは、価格だけでなく管理しやすさやサポート窓口も含めて判断します。

* **参考**： [【お詫び/復旧】一部お客さまでドコモからご契約いただいたYouTube Premiumがご利用いただけない事象について](https://www.docomo.ne.jp/info/notice/page/251222_03_m.html)

**Google One メンバーシップ・不具合の記録**

以下は自分の利用環境で発生した事象の記録です。Google One全体の一般仕様として確認できたものではありません。

1. Chromebook Plusの購入特典（Google AI Pro 2 TB 1年間無料）
2. docomo 爆アゲ セレクション Google One ベーシック（100 GB）（月額）
3. Google AI Pro 2 TB（年額）

これらを同一アカウントで扱っていた期間に、Google OneのWebサイトでストレージ容量を正常に取得できない、500エラーが出る、Androidアプリ側で利用状態を確認しにくくなる、といった現象を観測しました。

* [エラー画像 1](https://imgur.com/CNjeA2d)
* [エラー画像 2（500エラー）](https://imgur.com/cIa8AJt)
* [エラー画像 3（Androidアプリ ロック状態）](https://imgur.com/a/u9f38dX#3dKWbMC)

> [!NOTE]
> 契約の重複や請求経路が原因だったかどうかは、Googleまたはdocomoの公開資料では確認できていません。原因は未確認です。類似事例があっても、同一原因と断定しません。

不具合が発生した場合は、契約中プラン、購入特典、請求元、発生日時、画面表示を整理したうえで、まずGoogle Oneヘルプや実際の請求元のサポート窓口へ確認します。

* **[Google One ヘルプ > お問い合わせ](https://support.google.com/googleone/gethelp)**
* **[docomo｜お問い合わせ](https://www.docomo.ne.jp/support/inquiry/)**

Redditなどのユーザー報告は、同様の現象が存在するかを探す補助情報としてのみ扱い、一般仕様や原因の根拠には使用しません。

* **参考例**：[Google free trial Premium AI Scam](https://www.reddit.com/r/GoogleOne/comments/1dqzsrv/google_free_trial_premium_ai_scam/)

**Google Oneの削除操作について**

Googleアカウントの「サービスを削除」画面にGoogle Oneが表示される場合でも、削除による影響範囲はその時点の画面とGoogle公式説明を確認してから操作します。購入特典、有料プラン、保存データ等への影響をこのメモだけから断定しません。

---

## ChromeOS Chrome 拡張機能
* **[Manifest V2 のサポート タイムライン](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)**

Chrome / ChromeOSではManifest V2拡張機能の段階的な無効化・移行が進められてきました。利用可否はChromeのバージョン、管理ポリシー、配布形態によって異なるため、実機の拡張機能ページとChrome公式タイムラインを確認します。

* **[Chrome Web Store 拡張機能](https://chromewebstore.google.com/category/extensions)**

Chrome Web Store外から未パッケージの拡張機能を読み込む場合は、`chrome://extensions` で**デベロッパーモード**を有効にし、「パッケージ化されていない拡張機能を読み込む」を使用します。

**Violentmonkeyの導入**

ブラウザに機能を追加するUserScriptを管理・実行できるブラウザ拡張機能です。
* **[Violentmonkey](https://chromewebstore.google.com/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag)**
* **[Greasy Fork](https://greasyfork.org/ja)**

Chrome 138以降で、拡張機能が`chrome.userScripts` APIを利用する場合は、`chrome://extensions` > 対象拡張機能 > **詳細** > **ユーザースクリプトを許可する** を有効にします。Chrome 138未満では、User Scripts APIの利用に**デベロッパーモード**が必要です。これはChrome公式のUser Scripts API仕様です。

**❗️留意点**

以下のブラウザ拡張機能やUserScriptは、全てをインストールして使用しているわけではありません。拡張機能を増やすほど必ず競合するわけではありませんが、サイト不具合や権限競合の切り分けは複雑になります。問題発生時は、拡張機能を一つずつ無効化して再現性を確認します。

* ブラウザ拡張機能の競合を疑いながらも問題の切り分けができず、AdGuard Filtersに相談したIssuesの例。：[#228169](https://github.com/AdguardTeam/AdguardFilters/issues/228169)
* Gmail 「システムで問題が発生しました（#2014）」のユーザー報告例：[Reddit](https://www.reddit.com/r/techsupport/comments/1b4rocl/oops_the_system_encountered_a_problem_2014/?tl=ja)

PhotoShow等、特定の拡張機能が原因だった可能性を検証する場合も、無効化時の再現性などを確認し、推測と観測事実を分けて記録します。

### コンテンツブロック・プライバシー関連
* **[AdGuard Extra](https://github.com/AdguardTeam/AdGuardExtra)**：Anti-Adblock対策を補助するUserScript。
* **[AdGuard ブラウザ拡張機能 MV3対応版](https://chromewebstore.google.com/detail/adguard-%E5%BA%83%E5%91%8A%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=ja)**：Chrome向けManifest V3対応版。（詳細後述）
* **[tinyShield](https://github.com/List-KR/tinyShield/blob/main/README.ja.md)**：対象サイトの広告ブロック回避対策を補助するUserScript。対応範囲や導入方法はプロジェクトのREADMEを確認します。
* **[uBlacklist](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)**：検索結果から指定サイトを非表示にする。

### YouTube関連
* **[Enhancer for YouTube™](https://chromewebstore.google.com/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle)**：YouTubeの操作性を拡張する。
* **[SponsorBlock for YouTube](https://chromewebstore.google.com/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone)**：コミュニティ提供データを使い、動画内のスポンサー等のセグメントをスキップする。

### ショッピング関連
* **[Amazonレビュー信頼度判定 & 無限スクロール（サクラ識別 / 品質チェック）](https://greasyfork.org/ja/scripts/561755)**：Amazonレビュー表示を補助するUserScript。
* **[Condler](https://chromewebstore.google.com/detail/condler/ejjdbndmmongojeafjlilnchmkppbeap)**：Amazon検索結果の絞り込み操作を補助する。
* **[Keepa - Amazon Price Tracker](https://chromewebstore.google.com/detail/keepa-amazon-price-tracke/neebplgakaahbhdphmkckjjcegoiijjo)**：Amazon商品の価格履歴表示・価格通知を提供する。
* **[Knockoff — Amazon Brand Filter](https://chromewebstore.google.com/detail/knockoff-%E2%80%94-amazon-brand-f/pjgickchbiikhdfpmecaabkphmofpdce)**：Amazon検索結果のブランド表示を補助する。
* **[サクラチェッカーをAmazon内に直接表示](https://greasyfork.org/ja/scripts/533121)**：Amazon商品ページから外部評価情報を参照しやすくするUserScript。

---

## 参照

* [Chrome User Scripts API](https://developer.chrome.com/docs/extensions/reference/api/userScripts?hl=ja)
* [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)
* [AdGuard Browser Extension](https://github.com/AdguardTeam/AdguardBrowserExtension)

> [!NOTE]
> この文書は個人の設定・検証記録です。ここに掲載しているアプリ、拡張機能、サービスは推奨や安全性保証を意味しません。最新の仕様、権限、プライバシーポリシー、対応OSを各配布元で確認してください。
