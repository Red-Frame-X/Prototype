# ChromeOS & Android Optimization Guide

ChromeOS & Android 最適化ガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260825 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## Subscription
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
* **[tinyShield](https://github.com/List-KR/tinyShield/blob/main/README.ja.md)**：Ad-Shield対策用のUserScript ‐ Tampermonkeyで購読して、Manifest V3のフィルタ更新制限を回避する。
* **[uBlacklist](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)**：検索結果のフィルタリング、指定したサイトの検索結果を非表示にする。（詳細後述）

### YouTube関連
* **[Enhancer for YouTube™](https://chromewebstore.google.com/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle)**：再生速度や音量のマウス制御、画質固定、テーマ変更、コメント非表示などYouTubeの機能を強化する。
* **[SponsorBlock for YouTube-動画の広告シーンを自動スキップ](https://chromewebstore.google.com/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone)**：YouTube動画内のスポンサーセグメントやイントロなどを、ユーザーの報告に基づき自動でスキップする。

### ショッピング関連
* **[Amazonレビュー信頼度判定 & 無限スクロール（サクラ識別 / 品質チェック）](https://greasyfork.org/ja/scripts/561755)**：Amazonのレビュアー投稿履歴を分析し、信頼度をS〜Dランクで視覚化。信頼度フィルタリング機能や、レビュー一覧の無限スクロール化も提供。
* **[Condler](https://chromewebstore.google.com/detail/condler/ejjdbndmmongojeafjlilnchmkppbeap)**：Amazon検索結果の左側サイドバーに、並び替えやAmazon公式出品のみに絞り込むボタンを追加する。
* **[Keepa - Amazon Price Tracker](https://chromewebstore.google.com/detail/keepa-amazon-price-tracke/neebplgakaahbhdphmkckjjcegoiijjo)**：Amazon商品の価格履歴グラフをページ上に表示し、設定した価格になると通知を受け取れる。
* **[Knockoff — Amazon Brand Filter](https://chromewebstore.google.com/detail/knockoff-%E2%80%94-amazon-brand-f/pjgickchbiikhdfpmecaabkphmofpdce)**：Amazon検索結果に大量に現れるアルファベット羅列の無名・大量生産ブランドを識別し、ラベル付けや薄く表示、非表示（フィルタリング）にする。
* **[サクラチェッカーをAmazon内に直接表示 🔍️](https://greasyfork.org/ja/scripts/533121)**：Amazonの商品ページに、サクラチェッカーのスコアと判定結果を高速で自動表示する。

### 検索・ブラウジング補助
* **[Buster: Captcha Solver for Humans](https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl)**：音声認証とAIを活用してreCAPTCHAを自動で突破する。
* **[Cesturefy](https://chromewebstore.google.com/detail/cesturefy-navigate-operat/bifgfhokfobhebifcogneljkpaaloonp)**：マウス、ロッカー、ホイールジェスチャーでブラウザ操作を効率化する拡張機能。
* **[floccus bookmarks sync](https://chromewebstore.google.com/detail/floccus-bookmarks-sync/fnaicdffflnofjppbagibeoednhnbjhg)**：ブラウザのネイティブブックマークを、Google Drive、WebDAV、Nextcloudなどを利用して複数のブラウザや端末間で同期する。
* **[google-search-title-qualified](https://chromewebstore.google.com/detail/google-search-title-quali/bjcnnhojddnonjmhlpdjcdcfmofliagb)**：Google検索結果にサイト本来のタイトルを表示させる。
* **[Search Result Previews](https://chromewebstore.google.com/detail/search-result-previews/cedcejfiniojnlhlfhcppenochinijfo)**：検索結果のリンク横にウェブサイトのプレビュー画像（サムネイル）を表示させる。
* **[Tabs to Front v2](https://chromewebstore.google.com/detail/tabs-to-front-v2/iiojfifkpjkhcdjfgekmfobhfdohlecg)**：新しいタブを常にフォアグラウンド（最前面）で開く。
* **[VertiTab - 縦型タブ · AIブラウザエージェント](https://chromewebstore.google.com/detail/vertitab-vertical-tabs/chejfhdknideagdnddjpgamkchefjhoi)**：高度なタブ管理ツール、縦型タブ・ツリー型タブ・クラウド同期などを搭載。
* **[ブックマークサイドバー](https://chromewebstore.google.com/detail/%E3%83%96%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B5%E3%82%A4%E3%83%89%E3%83%90%E3%83%BC/jdbnofccmhefkmjbkkdkfiicjkgofkdh)**：ブラウザの端に切り替え可能なブックマークサイドバーを追加する。

### 特定サイト向け拡張
* **[ChatGPT Ctrl + Enter Sender](https://chromewebstore.google.com/detail/chatgpt-ctrl+enter-sender/gbncgdhklmnckojlibfhdadpfbcdbnch?hl=ja)**：AIチャットにおいて、Enterキーを改行、Ctrl + Enterキーを送信に割り当て、誤送信を防ぐ。
* **[Google Chatの改行・送信キー設定](https://chromewebstore.google.com/detail/google-chat%E3%81%AE%E6%94%B9%E8%A1%8C%E3%83%BB%E9%80%81%E4%BF%A1%E3%82%AD%E3%83%BC%E8%A8%AD%E5%AE%9A/kabocfciobpmopkcbiphmgdljpdlighk)**：Google Chatのキー設定をカスタマイズする。
* **[GitHub UI Translator](https://chromewebstore.google.com/detail/github-ui-translator/igdplojdbbpfbedgoaokfcagpkofmngk)**：GitHubのWeb画面上のメニュー、ボタン、説明文などのUIを日本語に翻訳して表示する。
* **[5CH STYLE FORMAT](https://chromewebstore.google.com/detail/5ch-style-format/aidnencnedgaflbgacmcbcokcpancdac?hl=ja)**：5chのスレッド記事の整形、URL直リンク化、画像・レスのPOP表示など。
* **[Twitterᴾˡᵘˢ](https://greasyfork.org/ja/scripts/387969-twitter%E1%B4%BE%CB%A1%E1%B5%98%CB%A2)**：オリジナル品質の画像を表示し、スパムツイートの削除機能をカスタマイズする。
* **[𝕏 Spam Highlighter](https://github.com/shapoco/x-spam-highlighter)**：PC向けWeb版𝕏のフォロワー一覧画面で、スパム疑いのアカウントを赤くハイライト表示する。
* **[Shadowban Scanner for Twitter / X](https://chromewebstore.google.com/detail/shadowban-scanner-for-twi/enlganfikppbjhabhkkilafmkhifadjd)**：𝕏のアカウントやツイートのシャドウバン、センシティブ判定を検出する。（[ろぼいんブログ](https://roboin.io/)）

### 業務効率化
* **[Advanced Font Settings](https://chromewebstore.google.com/detail/advanced-font-settings/caclkomlalccbpcdllchkeecicepbmbm?hl=ja)**：Webサイトのフォント設定を変更する
* **[Checker Plus for Gmail™](https://chromewebstore.google.com/detail/checker-plus-for-gmail/oeopbcgkkoapgobdbedcemjljbihmemj?hl=ja)**：Gmailを開かずに新着通知を受け、閲覧・削除・返信を可能にする。
* **[DeepL翻訳](https://chromewebstore.google.com/detail/deepl%EF%BC%9Aai%E7%BF%BB%E8%A8%B3%E3%81%A8%E6%96%87%E7%AB%A0%E4%BD%9C%E6%88%90%E3%83%84%E3%83%BC%E3%83%AB/cofdbpoegempjloogbagkncekinflcnj?hl=ja)**：高品質なAI翻訳と文章校正を提供する。
* **[Extensity](https://chromewebstore.google.com/detail/extensity/jjmflmamggggndanpgfnpelongoepncg?hl=ja)**：拡張機能のオン・オフをワンクリックで切り替えられる管理ツール。
* **[Google Keep Chrome 拡張機能](https://chromewebstore.google.com/detail/google-keep-chrome-%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD/lpcaedmchfhocbbapmcbpinfpgnhiddi?hl=ja)**：閲覧中のページやテキスト、画像をKeepに保存する。
* **[Google オフライン ドキュメント](https://chromewebstore.google.com/detail/google-%E3%82%AA%E3%83%95%E3%83%A9%E3%82%A4%E3%83%B3-%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/ghbmnnjooekpmoecnnnilnnbdlolhkhi)**：ドキュメント類をオフライン編集可能にする。
* **[PhotoShow](https://chromewebstore.google.com/detail/photoshow/mgpdnhlllbpncjpgokgfogidhoegebod)**：画像やURLにカーソルを合わせるだけで高画質拡大表示する。
* **[Sidely - ChatGPT Sidebar](https://chromewebstore.google.com/detail/sidely-chatgpt-sidebar/ibgipmeolfponfpmjhflfgkbcecpmcoo)**：ChatGPTをChromeのサイドパネルに表示し、閲覧中のWebページを開いたままChatGPTを利用できる。
* **[Shortcuts for Google™](https://chromewebstore.google.com/detail/shortcuts-for-google/baohinapilmkigilbbbcccncoljkdpnd)**：Googleサービスへのショートカットボタンを表示する。
* **[Similarweb - Website Traffic, AI Traffic & SEO Checker](https://chromewebstore.google.com/detail/similarweb-website-traffi/hoklmmgfnpapgjgcpechhaamimifchmp)**：閲覧中サイトのトラフィック指標、検索キーワード、AI流入などの競合分析データを表示する。
* **[System Memory Usage](https://chromewebstore.google.com/detail/system-memory-usage/fdefaodljgbdlmdhobjlechpgpblooeh)**：システムのメモリ使用量をツールバーに表示する。
* **[ドキュメント、スプレッドシート、スライドで Office ファイルを編集](https://chromewebstore.google.com/detail/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88%E3%80%81%E3%82%B9%E3%83%97%E3%83%AC%E3%83%83%E3%83%89%E3%81%A7-off/gbkeegbaiigmenfmjfclcdgdpimamgkj)**：Chromeブラウザ上でMicrosoft Officeファイルを直接開いて編集可能にする。
* **[ドライブ用アプリケーション ランチャー（Google）](https://chromewebstore.google.com/detail/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E7%94%A8%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3-%E3%83%A9%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC%EF%BC%88googl/lmjegmlicamnimmfhcmpkclmigmmcbeh)**：ブラウザから直接、PCにインストールされた対応アプリケーションでGoogle Driveのファイルを開く。
* **[設定（Settings）](https://chromewebstore.google.com/detail/settings/jkfjnjeniglhpiggnfpiombpaohknkie)**：Google設定、拡張機能、閲覧データの管理を一元化する。
* **[素晴らしい画面の並べ替えとスクリーンショット（Awesome Screenshot）](https://chromewebstore.google.com/detail/%E7%B4%A0%E6%99%B4%E3%82%89%E3%81%97%E3%81%84%E7%94%BB%E9%9D%A2%E3%81%AE%E4%B8%A6%E3%81%B9%E6%9B%BF%E3%81%88%E3%81%A8%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88/nlipoenfbbikpbjkfpfillcgkoblgpmj)**：画面の録画やスクリーンショットのキャプチャを容易にし、注釈追加も可能にする。

### 特殊用途
* **[Chromebook リカバリ ユーティリティ](https://chromewebstore.google.com/detail/chromebook-%E3%83%AA%E3%82%AB%E3%83%90%E3%83%AA-%E3%83%A6%E3%83%BC%E3%83%86%E3%82%A3%E3%83%AA%E3%83%86%E3%82%A3/pocpnlppkickgojjlmhdmidojbmbodfm?hl=ja)**：リカバリメディアを作成するGoogle公式ツール。

**参考サイト**
* [Kami-Browser-Add-on｜Kdroidwin](https://github.com/Kdroidwin/Kami-Browser-Add-on)

---

## ChromeOS Chrome テーマ
* **[Chrome Web Store テーマ](https://chromewebstore.google.com/category/themes)**
* **[Dark Horizon](https://chromewebstore.google.com/detail/dark-horizon/ncjjeokpcnllmmbbipeaagmdpdpiadin)**：Chrome標準テーマに近い外観を、より暗い配色にしたシンプルなダークテーマ。
* **[Royal Desert Sand](https://chromewebstore.google.com/detail/royal-desert-sand/nnieplejkjaodhemceganohmdkfekkem)**：デザートサンド（砂漠の砂）系の落ち着いた暖色とロイヤルブルーを組み合わせた、シンプルで上品なChromeテーマ。

---

## ChromeOS Chrome アプリ
* **[Chrome アプリのサポート終了（順次終了済み）](https://support.google.com/chrome/a/answer/15950395?hl=ja)**

---

## ChromeOS Android アプリ
* **[Google Play アプリ](https://play.google.com/store/apps)**

* **[ChMate](https://play.google.com/store/apps/details?id=jp.co.airfront.android.a2chMate)** (\*)
  * 説明：5ちゃんねるを高速・快適に閲覧できる多機能なAndroid専用ブラウザアプリ。（※ ChromeOSでの不具合は後述）
* **[personalDNSfilter](https://play.google.com/store/apps/details?id=dnsfilter.android)** (\*)
  * 説明：主にChMateでの広告ブロックを目的とし、副次的に他のAndroidアプリやChromeOS用Chromeブラウザでの広告・トラッキングをブロックする軽量アプリ。（※ 詳細後述）
* **[Google Home](https://play.google.com/store/apps/details?id=com.google.android.apps.chromecast.app)**
  * 説明：スマートデバイスを一元管理し、ルーティンによる自動化を実現するハブアプリ。
* **[Google フォト](https://play.google.com/store/apps/details?id=com.google.android.apps.photos)**
  * 説明：クラウド自動バックアップで端末容量を節約し、AI検索や編集が可能なギャラリーアプリ。

---

# ChatGPT プロンプト

OpenAIが提供する生成AI「ChatGPT」は、質問や指示である**プロンプト**と、会話内で与えられた文脈に基づいて回答を生成します。
プロンプトには特別な構文や固定書式は必須ではありませんが、目的、必要な背景情報、出力形式、変更してはいけない条件を明確にすると、意図に沿った回答を得やすくなります。

ただし、ChatGPTの回答は常に事実や正解であるとは限りません。事実と異なる内容をもっともらしく生成する現象は、一般に**ハルシネーション**と呼ばれます。
重要な数値、固有名詞、日付、引用、セキュリティ上の判断などは、回答だけを信用せず、公式ドキュメントや複数の信頼できる情報源で確認してください。

ChatGPTに検証を依頼するときは、非公開の内部思考過程をそのまま開示させようとするのではなく、次の情報を求めるほうが実用的です。

* 使用した情報源と、各情報源が裏付ける主張
* 判断根拠の簡潔な要約
* 前提条件と推測した部分
* 確認できなかった情報
* 結論を変える可能性がある反証や追加情報

**AdGuard for AndroidとAndroid版ChatGPTアプリを併用する際の注意**

通常はChatGPTアプリをAdGuardの保護対象から除外したり、QUICバイパスパッケージへ事前登録したりする必要はありません。
アプリ全体を除外すると、そのアプリの通信がAdGuardによるHTTPS・DNS・トラッカー保護の対象外になるため、常用する設定としてはプライバシー面のデメリットがあります。

ChatGPTアプリで接続エラー、ログイン失敗、回答の停止などが発生し、AdGuardを一時停止すると改善する場合に限り、次の順序で切り分けます。

1. ChatGPT、AdGuard、フィルタを最新版に更新して再試行する。
2. AdGuardの「統計」→「最近のアクティビティ」で、ChatGPTアプリの通信がブロックされていないか確認する。
3. DNSフィルタリングとHTTPSフィルタリングを一時的に個別に無効化し、原因となる機能を特定する。
4. QUICが原因と確認できた場合だけ、「一般設定」→「詳細設定」→「ローレベル設定」→「AdGuardによる保護」→「QUICバイパスパッケージ」に `com.openai.chatgpt` を追加して再試験する。
5. 改善しない場合は追加設定を元に戻す。最後の切り分け手段としてのみ、「アプリの管理」からChatGPTを一時的に保護対象外にする。

ローレベル設定は通信断、性能低下、セキュリティ・プライバシー低下を招く可能性があるため、症状がない状態で変更しないでください。

**プロンプトによる役割・目的の設定**

「あなたは〇〇の専門家です」のような役割指定は、回答の視点、用語の水準、重視する観点を明確にするために利用できます。
ただし、役割を指定してもChatGPTへ新しい資格、専門知識、最新情報が追加されるわけではありません。役割だけに依存せず、目的、対象読者、参照すべき資料、出力形式、禁止事項、確認方法も具体的に伝えることが重要です。

例：

> あなたはAndroidのネットワーク障害を調査する技術サポート担当者です。初心者向けに説明し、原因を断定せず、確認手順を影響の小さい順に提示してください。現在の仕様は公式ドキュメントで確認し、推測と確認済みの事実を分けてください。

## ChatGPTのGitHubプラグインとCodex

[GitHubプラグイン（OpenAI公式）](https://openai.com/business/plugins/github/) を追加すると、ChatGPTのChat・WorkおよびCodexから、許可したRepository、ファイル、commit、Issues、Pull Request、CIなどを参照・管理できます。プラグインはスキルとGitHubコネクタをまとめたもので、利用可能な操作は、ChatGPTのプランと画面、GitHub Appに付与したRepository・権限、ワークスペース管理者の設定、操作時の承認によって異なります（[OpenAI公式：Plugins](https://learn.chatgpt.com/docs/plugins)）。

**Chat・Work・Codexの役割**

| 画面 | 適した用途 | 主な制約 |
| :--- | :--- | :--- |
| **Chat** | リポジトリやファイルの検索・説明、Issues・Pull Request・CIの確認、Issues整理、コメント、ラベル、レビュー、許可されたファイル更新など | GitHubプラグインが提供する操作と権限の範囲内。リポジトリ全体をローカル作業環境として実行・検証する用途には向かない |
| **Work** | Chatで可能なGitHub操作に加え、複数の情報源やツールをまたぐ調査、長い査読、作業報告などの多段階タスク | 作業量に応じて時間・クレジットを多く使う場合がある（[OpenAI公式：ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work)） |
| **Codex** | リポジトリを作業環境で読み、複数ファイルを編集し、テスト・lint・生成処理を実行して、commit・push・Pull Request作成まで進める | 実行環境、sandbox、ネットワーク、GitHub権限、承認設定の制約を受ける |

したがって、**ChatGPT ChatでもGitHubリポジトリの管理・運用はある程度可能**です。従来の「ChatGPTのGitHub接続は読み取り専用、書き込みはすべてCodex」という説明は、現在のGitHubプラグイン全体には当てはまりません。ただし、ChatからのAPI操作でファイルを更新できることと、checkoutしたリポジトリでテストまで行えることは別です。コード変更の再現性と検証が重要な作業ではCodexを使います。

**追加・接続手順**

1. ChatGPTの「Plugins」からGitHubプラグインを追加します。プラグインは対応するChat・Work・Codexで利用できます（[OpenAI公式：Plugins](https://learn.chatgpt.com/docs/plugins)）。
2. GitHubで認証し、可能なら「All repositories」ではなく「Only select repositories」を選び、必要なリポジトリだけを許可します（[GitHub公式：GitHub Appのインストール](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party)）。
3. 新しい会話で `@GitHub` を指定し、リポジトリ、Issues、Pull RequestのURLと、調査・変更範囲、完了条件を伝えます。インストール後のプラグインは新しいChatまたはWorkで使用するのが確実です。
4. リポジトリが表示されない場合は、GitHubのInstalled GitHub Appsで対象リポジトリと権限を確認し、Organization所有の場合は管理者によるインストール・承認も確認します（[GitHub公式：インストール済みAppの確認・変更](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps)）。
5. 書き込み操作が使えない場合は、GitHub Appの権限、ChatGPTワークスペースのAction controls、操作時の承認、使用中の画面でそのツールが提供されているかを確認します。具体的な反映時間は公式資料で一律に保証されていないため、「接続後5分」などの固定値は目安として断定しません。

**リポジトリ管理に適した作業例**

* リポジトリ全体を査読し、重要度、根拠、修正案、影響範囲を整理する。
* IssuesとPull Requestを確認し、重複、再現手順不足、未解決レビュー、CI失敗を分類する。
* ChatからIssuesの作成・更新、コメント、ラベル、担当者、Pull Requestレビューなど、許可された管理操作を行う。
* 小規模なMarkdownや設定ファイルを更新する。テストが必要なコード変更はCodexへ回す。
* 最近のcommit、マージ済みPull Request、workflow結果から更新履歴や作業報告を作成する。
* CodexでAdGuardフィルタ、UserScript、正規表現、Markdownを修正し、関連するlint・テスト・生成処理を実行する。

**推奨ワークフロー**

1. `README.md`、`AGENTS.md`、対象Issues、関連ファイルを読み、作業範囲と完了条件を固定します。
2. ChatまたはWorkで現状調査、Issues整理、変更計画、リスク評価を行います。
3. コード実行を伴わない軽微な管理・文書更新はGitHubプラグインで行い、複数ファイルの実装や検証はCodexで専用ブランチに行います。
4. 自動テスト、lint、生成処理を実行し、生成物を含む差分を確認します。
5. Pull Requestに要約、理由、影響、テスト結果、未検証事項、残るリスクを記載します。
6. 人間が差分とCI結果を確認してからマージします。CodexのReviewは有用な追加チェックですが、テスト、branch protection、必須レビューの代替ではありません（[OpenAI公式：CodexによるGitHub Pull Requestレビュー](https://learn.chatgpt.com/docs/third-party/github)）。

CodexのPull Requestレビューは、コメントで `@codex review` と依頼でき、リポジトリ固有の確認事項は変更対象に最も近い `AGENTS.md` の `## Code Review Rules` に記載できます。機械的に判定できるformat・lintはCIへ残し、`AGENTS.md`には互換性、データ境界、副作用などリポジトリ固有の判断基準を簡潔に記載します（[OpenAI公式：AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)）。

Redditでは、ChatGPTを計画・整理、Codexを実装・検証に分け、`AGENTS.md`やチケット文書で作業範囲を固定する運用例があります（[Reddit：ChatGPTとCodexの併用](https://www.reddit.com/r/codex/comments/1vtmmjt/is_there_a_better_way_to_use_chatgpt_codex/)、[Reddit：AGENTS.mdを使った運用例](https://www.reddit.com/r/codex/comments/1tf4s07/my_best_workflow_so_far_for_building_projects/)）。一方、特定のChat画面やモデルではプライベートリポジトリの取得が安定しないという報告もあります（[Reddit：GitHub connectorの利用画面に関する報告](https://www.reddit.com/r/ChatGPTPro/comments/1ozf2jm/github_connector_only_works_in_deep_research/)）。これらは利用者個別の体験談であり、一般仕様や現在の障害を示す公式情報ではありません。

**❗️セキュリティ・運用上の注意**

* GitHub Appには必要最小限のリポジトリと権限だけを付与します。GitHub Appの権限は、APIで実行できる操作を決定します（[GitHub公式：GitHub Appの権限](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)）。
* APIキー、アクセストークン、Cookie、個人情報をリポジトリ、Issues、Pull Request、プロンプト、ログへ含めません。誤ってcommitした秘密情報は、削除commitだけでなく認証情報の失効・再発行も行います。
* AIが作成した変更には、誤修正、過剰変更、依存関係や生成物の見落としがあり得ます。削除、公開、merge、release、workflowの再実行など影響の大きい操作は、対象・差分・権限を確認してから実行します。
* Chatから書き込めても、テストを実行していなければ動作確認済みとは扱いません。実行した検証と未検証事項を分けて記録します。
* プラグインの機能、対応画面、権限は更新される可能性があります。導入時は [OpenAI公式：Plugins](https://learn.chatgpt.com/docs/plugins) とGitHubのInstalled GitHub Apps画面を再確認します。

## 汎用プロンプト集

用途に合わせて「〜」や「〇〇」などのプレースホルダーを書き換えて使用してください。複数の指示を組み合わせる場合は、矛盾する条件がないか確認してください。

### 情報検索・調査（Information Retrieval & OSINT）

* **【用語解説と事実確認】**：「〜」とは何ですか？ 初心者向けの概要と技術的な詳細を分けて説明してください。ChatGPTのウェブ検索を使用して公式ドキュメントなどの一次情報を優先し、主要な主張ごとに根拠となるリンクを付けてください。確認済みの事実、推測、確認できなかった点を区別してください。
* **【公式サイト・リンク収集】**：「〜」に関する主要な開発元・製造元の公式サイトと、詳しい技術仕様が掲載された信頼性の高いページをウェブ検索してください。各URLを実際に開いて到達できることを確認し、ページ名、運営主体、用途を箇条書きで整理してください。
* **【特定コミュニティ検索＆要約】**：「〇〇の✕✕」に関する言及を、GitHub IssuesやRedditなど指定したコミュニティから検索してください。関連URL、投稿日、投稿者が報告した環境、解決状況を日本語で要約し、公式見解とユーザー報告を混同しないでください。
* **【価格相場・市場調査】**：この商品・サービス（URLまたは名称：〜）の現在価格と過去の相場を検索してください。通貨、税、地域、契約期間、キャンペーン条件を揃えたうえで比較し、現在の価格が適正か評価してください。取得日時と情報源も示してください。
* **【詳細調査】**：「〜」について複数の情報源を横断する詳細調査を行ってください。必要に応じてDeep Researchを使用し、調査範囲、採用・除外した情報源、相反する見解、未確認事項を含む引用付きレポートにしてください。

### セキュリティ・安全性評価（Security & Safety Analysis）

※機密情報、認証情報、個人を特定できる情報、非公開のソースコードやログは入力しないでください。

* **【不審サイト・ドメイン評価】**：以下のサイト（ドメイン名：〜）について、URL構造、ドメイン登録情報、証明書、運営主体、既知の悪評やインシデントをOSINTの範囲で調査してください。不審なサイトへログイン、ファイル送信、ダウンロード、スクリプト実行は行わず、確認できた事実とリスクの推測を分けて評価してください。
* **【拡張機能のプライバシー・安全性調査】**：以下のブラウザ拡張機能（URL：〜）について、要求権限の必要性、開発元、プライバシーポリシー、外部通信、更新履歴、所有者変更、過去のマルウェア化やストア削除事例を調査してください。公式ストア、ソースコード、Issues、公開されたセキュリティ報告を優先し、利点と残存リスクを示してください。
* **【コード・ファイル静的解析】**：（解析対象を添付またはペースト）この内容を実行せずに静的解析し、難読化、認証情報、危険な権限、不審な外部通信、任意コード実行、脆弱性につながる処理がないか確認してください。証拠となるファイル名・行・コード断片を示し、確信度と誤検知の可能性も記載してください。

### テキスト処理・ドキュメント作成（Text Processing & Formatting）

* **【翻訳・文章校正】**：以下の文章を自然で正確な（日本語 / 英語）に翻訳してください。固有名詞、数値、URL、コードの意味は変えず、誤字脱字、文法、不自然な表現を修正してください。意味が曖昧な箇所は推測で確定せず、注記してください。：[改行]〜
* **【要約・比較検討】**：「〇〇」と「✕✕」の違いを、以下の資料または検証可能な事実に基づいて比較してください。比較条件を揃え、双方のメリット、デメリット、適する用途、判断できない点を表または箇条書きで整理してください。：[改行]〜
* **【分類とソート】**：以下の項目を重複を除いて適切なカテゴリーに分類し、それぞれ英数字順（0-9、A-Z）に並べてください。表記揺れを統一した場合は変更一覧も示してください。：[改行]〜
* **【検索・査読・Markdown化】**：以下のメモについてウェブ検索で最新情報を補完し、一次情報を優先して事実確認してください。誤り、古い情報、根拠不足、リンク切れを指摘・修正し、論理的で読みやすいMarkdown文書として出力してください。修正内容と情報源も示してください。：[改行]〜

### 開発・システム運用（Development & Engineering）

* **【正規表現の作成・除外・最適化】**：「〇〇」にマッチし、「✕✕」にはマッチしない正規表現を作成してください。対象エンジンを確認し、テストケースを正常系・除外系・境界値に分けて提示してください。以下の既存表現はマッチ条件を変えず、ChMateのNG Word機能で動作し、ReDoSにつながる過度なバックトラッキングを避けるよう最適化してください。最後にtypoと重複を確認してください。：[改行]〜
* **【問題解決・エラー解消】**：（エラー全文と発生条件を記載）原因候補を確度と根拠付きで整理し、データ消失や設定変更の影響が小さい順にトラブルシューティング手順を提示してください。各手順には期待される結果と、結果ごとの次の分岐を記載してください。
* **【代替案・ワークアラウンドの提示】**：「〜」を実現する別の手段を複数提案してください。公式機能、OSS、設計変更、一時的な回避策を区別し、利点、欠点、プライバシー、保守性、費用、元に戻せるかを比較してください。
* **【コード変更と検証】**：（リポジトリまたは対象ファイルを指定）関連コードと既存の変更を確認し、要求された範囲だけを修正してください。変更前後の差分、実行したテスト、未検証事項を示してください。明示的な許可がない限り、外部公開、送信、削除、デプロイは行わないでください。

### 計算・ユーティリティ（Calculation & Utilities）

* **【条件付き計算・為替変換】**：（例：現在の為替レートでのUSDからJPYへの換算、または「単価180円/L、燃費10km/L、走行距離3000km」）使用した数値、単位、取得日時、丸め方法を明示し、立式、途中計算、最終結果を示してください。外部レートを使う場合は情報源も付けてください。
* **【画像生成】**：「〜」の画像を生成してください。用途、画風、構図、含める要素、除外する要素、縦横比、文字の有無を指定します。既存画像を編集する場合は、変更箇所と維持する箇所を分けて記載してください。

### 出力制御（Output Control）

* **【フォーマット指定（末尾付与用）】**：回答本文をコピーしやすい1つのMarkdownコードブロック内にまとめてください。ただし、クリック可能にする必要がある参考リンクと、コードブロックを入れ子にできないコード例はブロックの外に出してください。
* **【不確実性の明示（末尾付与用）】**：確認済みの事実、推測、未確認事項を分け、確証がない内容を断定しないでください。
* **【簡潔化（末尾付与用）】**：冒頭に結論を示し、重複説明を削除してください。重要な制約、例外、デメリットは省略しないでください。

### パーソナライズ設定

ChatGPTの「設定」→「パーソナライズ」→「カスタム指示」に、複数のチャットで継続して適用したい好みを登録できます。
特定の作業だけに必要な指示は、そのチャットのプロンプトまたはプロジェクト指示へ記載してください。カスタム指示は回答傾向を調整しますが、事実の正確性や機能の追加を保証するものではありません。

* **パーソナライズ設定：1（情報収集と回答形式）**

```text
回答は、必要に応じてChatGPTのウェブ検索を使用し、公式ドキュメントや公的機関など信頼性の高い一次情報を優先してください。冒頭に簡潔な要約を提示してください。重要な主張には、その内容を直接裏付ける実在のリンクを付け、リンク先を確認できなかった場合はその旨を明記してください。事実、推測、未確認事項を区別し、利点と欠点の両方を示してください。検索エンジンの検索結果ページを情報源として提示する場合は、その旨を明記してください。URLはプレーンテキストではなく、クリック可能なMarkdown形式のリンクとして出力してください。
```

* **パーソナライズ設定：2（IT・セキュリティ・広告ブロック）**

```text
IT、セキュリティ、広告ブロックに関する質問では、公式ドキュメント、公開されたソースコード、Issues、変更履歴を優先して確認してください。uBlock Origin、AdGuard、主要フィルタリストなどの公開された設計方針とベストプラクティスを参考にし、誤ブロック、互換性、性能、保守性、プライバシーのトレードオフを示してください。特定の開発者やフィルタ作者については、本人が公開した資料だけを根拠とし、未公開の見解、査読、承認を推測しないでください。
```

**参考サイト**

* [ChatGPTのプロンプト作成ガイド（OpenAI公式）](https://learn.chatgpt.com/docs/prompting)
  * 目的、背景情報、出力形式、境界条件を伝え、回答後の追加指示で改善する方法を説明しています。
* [ChatGPTを使う（OpenAI公式）](https://learn.chatgpt.com/docs/use-chatgpt)
  * ファイル、ウェブ検索、プラグインなどの利用方法と、重要な回答を検証する際の注意点を説明しています。
* [ChatGPTのパーソナライズ（OpenAI公式）](https://learn.chatgpt.com/docs/personalize)
  * カスタム指示、メモリ、パーソナリティなどの設定を説明しています。
* [ChatGPTのプロジェクト（OpenAI公式）](https://learn.chatgpt.com/docs/projects)
  * 関連するチャット、ファイル、情報源、プロジェクト指示をまとめて扱う方法を説明しています。
* [ChatGPTの画像生成（OpenAI公式）](https://learn.chatgpt.com/docs/image-generation)
  * 自然言語による画像生成と、参照画像を使った編集方法を説明しています。
* [ChatGPT Androidアプリ（Google Play）](https://play.google.com/store/apps/details?id=com.openai.chatgpt)
* [AdGuard for Android ローレベル設定ガイド（AdGuard公式）](https://adguard.com/kb/ja/adguard-for-android/features/low-level-settings/)
  * QUICバイパスパッケージやアプリ除外の用途と、ローレベル設定を変更する際の注意事項を確認できます。

---

## Code Editor
**Visual Studio Code**
* **[Visual Studio Code: Workspace](https://vscode.dev/?vscode-lang=ja-jp)** / **[GitHub](https://github.com/microsoft/vscode)**
  * 説明：インストール不要でブラウザから直接利用できる軽量かつ高機能なコードエディタです。

**Visual Studio Code 拡張機能**
* **[Virtual Gists for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-virtualgists)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualGists)**
  * 説明：VS Code上でGitHub Gistを直接管理・編集できる拡張機能です。
* **[Virtual Git extension pack](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-virtualgit)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualGit)**
  * 説明：端末にGit環境を構築しなくても、ブラウザから直接GitHubやGistのファイルを編集・保存できるようになる便利なパックです。
* **[Virtual Repositories for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-virtualrepos)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualRepos)**
  * 説明：リモートリポジトリをクローン、コミット、プッシュすることなく開いて編集できる拡張機能です。

**Android アプリ**
* **[QuickEdit Pro](https://play.google.com/store/apps/details?id=com.rhmsoft.edit.pro)** / **[Help Center](https://rhmsoft.com/qedit/help.html)**

**QuickEdit Proの安全な推奨トークン権限（スコープ）の構成｜GitHub**

* GitHubサイト・右上アイコン > Settings > Developer Settings > Personal access tokens > Tokens（classic）。

* 「repo」「gist」にのみチェックを入れる。

**Issues報告**
* [Visual Studio Code Issues](https://github.com/microsoft/vscode/issues)
* [Virtual Gists Issues](https://github.com/carlocardella/vscode-VirtualGists/issues)
* [Virtual Git Issues](https://github.com/carlocardella/vscode-VirtualGit/issues)
* [Virtual Repositories Issues](https://github.com/carlocardella/vscode-VirtualRepos/issues)
* [Japanese IME failure on VS Code 1.107.1 (Crostini) #285154](https://github.com/microsoft/vscode/issues/285154) （計画されていないため閉鎖）

※ 現在はCrostini（Linux 開発環境）およびVSCodiumをデバイスから削除し、ブラウザとAndroidアプリベースの環境へ完全移行済みです。

---

## AdGuardユーザールールの作成（個人用途）

生成AIの提案は、実際のAdGuard製品で構文と動作を確認してから使用します。ChatGPTにはURLだけでなく、対象要素のHTML、目的、使用製品、期待する動作を渡してください。ログインが必要なページや動的ページはChatGPTが同じ状態を直接確認できない場合があります。
