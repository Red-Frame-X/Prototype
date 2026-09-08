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
* **[ドキュメント、スプレッドシート、スライドで Office ファイルを編集](https://chromewebstore.google.com/detail/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88%E3%80%81%E3%82%B9%E3%83%97%E3%83%AC%E3%83%83%E3%83%89%E3%82%B7%E3%83%BC%E3%83%88%E3%80%81%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%89%E3%81%A7-off/gbkeegbaiigmenfmjfclcdgdpimamgkj)**：Chromeブラウザ上でMicrosoft Officeファイルを直接開いて編集可能にする。
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
* **[Virtual Repositories for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-VirtualRepos)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualRepos)**
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

### AdGuardユーザールール作成手順

1. 対象ページをデスクトップ版Google Chromeで開き、デベロッパーツール（Ctrl + Shift + I）の要素選択アイコンを有効にします（[Chrome DevTools公式](https://developer.chrome.com/docs/devtools/inspect-mode?hl=ja)）。
2. 非表示にしたい要素を選択し、DOMツリーで右クリックして「Copy」>「Copy outerHTML」を選びます。必要なら親要素や、同種要素との違いが分かる周辺HTMLも取得します。
3. ChatGPTに、対象URL、コピーしたHTML、使用製品（AdGuard ブラウザ拡張機能 MV3対応版 / AdGuard for Android）、目的をまとめて入力します。スクリーンショットも補助資料になりますが、ルール作成にはHTMLのほうが適しています。
4. 次のプロンプトを貼り付け、プレースホルダーを置き換えます。

````text
# 目的
以下の対象だけを非表示またはブロックする、AdGuard用のユーザールールを提案してください。

# 使用環境
- 製品: AdGuard ブラウザ拡張機能 MV3対応版 / AdGuard for Android（該当するものを残す）
- 対象URL: （URL）
- 期待する動作: （消したい要素、残すべき要素、発生している問題）
- 対象要素と周辺のHTML:
```html
（Copy outerHTMLで取得したHTML）
```

# 調査と根拠
- 必要に応じてChatGPTのウェブ検索を使い、AdGuard公式ナレッジベース、AdGuardTeamの公開ソースコード、Issues、変更履歴を優先してください。
- URLへアクセスできない、ログイン後の状態を再現できない、または情報が不足している場合は、その制約を明記してください。見えていないDOMや通信を推測で断定しないでください。
- 使用した構文について、対応製品と根拠となる公式リンクを示してください。

# 設計方針
1. まず対象ドメインに限定した単純な要素非表示ルール `example.com##selector` を検討してください。
2. ID、意味が安定した属性、固有のクラスを優先し、自動生成されたクラス、位置依存の `:nth-child()`、過度に長いセレクターは避けてください。
3. `:has()` は一律に避けないでください。AdGuardでは `##` 付きのルールが、対応環境ではネイティブ実装を使い、必要に応じてExtendedCssへフォールバックします。ExtendedCssを強制する必要がある場合だけ `#?#` を検討してください。
4. テキスト一致が不可欠な場合はAdGuardの `:contains()` を使用し、言語変更や文言変更による保守性低下を説明してください。`:has-text()` は互換エイリアスですが、AdGuard向け出力では原則 `:contains()` に統一してください。
5. `#$#` と `#$?#` はCSS宣言を注入するルールです。単に要素を隠すだけなら `##` または `#?#` を優先してください。
6. ネットワークルールは、対象リクエストがHTMLだけから確実に特定できない場合は作らないでください。必要ならDevToolsのNetwork情報を追加で求めてください。提案する場合はリソース種別と `$domain=` などで適用範囲を最小化し、機能破壊とプライバシー上の影響を説明してください。
7. Scriptletは通常のCSS・ExtendedCss・限定的なネットワークルールで解決できない場合だけ検討してください。uBlock Origin形式の `##+js(...)` をAdGuard形式として出力せず、AdGuard Scriptlets公式ライブラリに存在する名前・引数・対応製品を確認して `#%#//scriptlet('name', 'arg')` を使用してください。
8. HTMLフィルタリング、JavaScriptルール、強力な修飾子は、製品互換性と副作用を確認できた場合だけ別案として提示してください。
9. 広すぎるルール、対象サイト全体の機能を壊す可能性があるルール、根拠を確認できないルールは出力しないでください。

# 出力形式
- 冒頭に推奨ルールを1つの `adblock` コードブロックで提示してください。
- 個人用ユーザールールでは、購読フィルタ用メタデータを必要がない限り付けないでください。
- 続けて「選定理由」「互換性」「誤ブロックの可能性」「確認手順」「必要なら代替案」を簡潔に説明してください。
- 候補が複数ある場合は、推奨順とトレードオフを示してください。
- 十分な情報がなければ無理にルールを生成せず、追加で必要なHTML、Network情報、再現手順を具体的に質問してください。
- 最後に、AdGuard構文として有効か、uBlock Origin専用構文が混入していないかを再確認してください。
````

5. 出力されたルールをユーザールールへ登録し、ページを再読み込みして確認します。対象が消えるだけでなく、ログイン、検索、再生、スクロール、リンク操作などが壊れていないかも確認します。
6. 意図どおりでない場合は、実際の結果、コンソールエラー、追加のHTML、Network情報を同じチャットへ渡して修正を依頼します。ルールを一つずつ有効化・無効化すると原因を切り分けやすくなります。

▶ 生成AIの出力は検証が必要です。一般の利用者にも影響する広告・トラッカー・迷惑要素は、再現手順とスクリーンショットを添えて [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues) または [AdGuard reporting tool](https://reports.adguard.com/) へ報告する方法が適しています。報告前にリポジトリのIssuesテンプレートとポリシーを確認してください。

### 作成したAdGuardユーザールールの整理

整理対象のルールを次のプロンプトの後へ貼り付けます。

```text
# タスク
以下のAdGuardユーザールールを、マッチ条件と動作を変えずに整理してください。

# 必須条件
- ルール本文、ドメイン指定、修飾子、例外、正規表現、エスケープ、コメントアウト状態を変更しないでください。
- 完全に同一の有効ルールだけを重複として削除してください。似ているだけのルール、例外ルール、コメントアウトされたルールは削除しないでください。
- ドメインを推測して書き換えたり、疑わしいルールを削除・無効化したりしないでください。
- ドメイン見出しごとにまとめ、各ドメイン内では元の相対順序を可能な限り維持してください。
- 変更後に、削除した完全重複ルールと、移動以外の変更がないことを確認してください。

# 出力形式
- 全ルールを1つの `adblock` コードブロックに入れてください。
- ドメインが変わる箇所だけ1行空けてください。
- 同一ドメイン内ではカテゴリーが変わっても空行を入れないでください。
- 見出しは `! example.com`、カテゴリーは `! カテゴリー名` としてください。
- 罫線コメントは追加しないでください。

# 整理対象
（ここにルールを貼り付ける）
```

### uBlock Origin用Scriptletルールの変換

uBlock OriginとAdGuardでは、同名に見えるScriptletでも引数、動作、対応バージョンが異なる場合があります。構文を機械的に置換せず、公式ライブラリで意味上の互換性を確認します。

```text
# タスク
以下のuBlock Origin用Scriptletルールを、AdGuard ブラウザ拡張機能 MV3対応版で同じ目的と副作用になるAdGuard Scriptletルールへ変換可能か調査してください。

# 調査対象
- uBlock Origin Resources Library:
  https://github.com/gorhill/uBlock/wiki/Resources-Library
- AdGuard Scriptlets:
  https://github.com/AdguardTeam/Scriptlets
- AdGuard Scriptlets wiki:
  https://github.com/AdguardTeam/Scriptlets/blob/master/wiki/about-scriptlets.md

# 必須条件
- 両方の公開ドキュメントまたはソースコードで、Scriptlet名、引数、既定値、対象、制限を比較してください。
- 名前が似ているだけでは互換と判断しないでください。
- AdGuard側に同等機能があり、対象環境で対応し、動作と主要な副作用を再現できる場合だけ変換してください。
- 変換する場合はAdGuard構文 `example.com#%#//scriptlet('name', 'arg')` を使用してください。
- 完全な同等性を確認できない場合は、ルールを生成せず「変換不可能」または「同等性未確認」と回答し、相違点を示してください。
- uBlock Originの `##+js(...)` をAdGuard向けの回答としてそのまま出力しないでください。

# 出力形式
1. 判定: 変換可能 / 変換不可能 / 同等性未確認
2. 根拠と互換性上の注意
3. 変換可能な場合のみ、1つの `adblock` コードブロック
4. 実環境での確認手順

# 変換対象
（ここにuBlock Origin用ルールを貼り付ける）
```

### 不具合を起こすAdGuardユーザールールの特定・修正

````text
# タスク
以下のAdGuardユーザールールのうち、指定した不具合を起こす可能性があるルールを特定し、安全に修正してください。

# 状況
- 不具合が起きるURL: （URL）
- 不具合の発生箇所: （箇所）
- 不具合の内容: （内容）
- 正常時に期待する動作: （期待する動作）
- 再現手順: （手順）
- 対象ページのHTML:
```html
（HTML）
```

# 必須条件
- まず候補ルールを一つずつ無効化して切り分ける手順を示してください。
- HTMLだけで判断できないネットワークルールやScriptletについては、必要なNetwork情報、コンソールエラー、ログを具体的に求めてください。
- 原因ルール、根拠、確信度、誤判定の可能性を示してください。
- 修正は適用範囲を狭める方法を優先し、元の目的、誤ブロック、互換性、性能を比較してください。
- 根拠なく正常なルールを変更・削除しないでください。
- 安全な修正を確認できない場合は「修正不可」とし、削除を自動決定せず、無効化候補として分けてください。

# 出力形式
1. 原因候補と切り分け手順
2. 修正内容とトレードオフ
3. 修正後の全ルールを1つの `adblock` コードブロック
4. 未確認事項と動作確認項目
````

**Google スプレッドシートを用いた単純な重複確認**

1. 1セルに1ルールを貼り付けます。
2. 「データ」>「データ クリーンアップ」>「重複を削除」を使用します。
3. 並べ替えはルールの評価順や可読性を変えるため、動作確認済みのルール群では慎重に行います。コメントとルールの対応関係が崩れないようにしてください。

---

## UserScriptの作成（個人用途）

AdGuardルールで実現できない処理だけをUserScriptで補います。UserScriptはページ上でJavaScriptを実行するため、単純な要素非表示にはAdGuardルールを優先したほうが、権限、保守、性能、セキュリティの面で扱いやすくなります。

````text
# 目的
以下の要件を満たす、TampermonkeyまたはViolentmonkey用UserScriptを作成してください。

# 入力
- 対象URL: （URL）
- 対象ブラウザ: （Chromeなど）
- UserScriptマネージャー: Tampermonkey / Violentmonkey
- 実現したい動作: （要件）
- 対象要素と周辺のHTML:
```html
（HTML）
```

# 実装条件
- 必要に応じて公式仕様、MDN、UserScriptマネージャーの公式ドキュメントをウェブ検索し、参照したリンクを示してください。
- `@match` は必要最小限のoriginとpathに限定し、無関係なサイトで実行しないでください。
- 必要な権限だけを `@grant` に指定してください。特権APIが不要な場合だけ `@grant none` を使用してください。
- 外部コードの動的取得、`eval`、`new Function`、インラインイベントハンドラー、不要な外部通信は使用しないでください。
- ページの既存機能、CSP、アクセシビリティ、プライバシーを損なわないようにしてください。
- SPAや遅延生成DOMに対応する必要がある場合は、まず既存イベントを検討し、MutationObserverを使う場合は監視範囲を狭め、処理を冪等にし、不要になったら切断してください。無制限のポーリングは避けてください。
- セレクターは安定したIDや属性を優先し、自動生成クラスや過度に長いDOMパスへの依存を避けてください。
- `@version` は更新時に必ず増やしてください。`@updateURL` と `@downloadURL` は実在する配布URLが指定された場合だけ追加し、プレースホルダーURLは出力しないでください。
- 不明点が実装を左右する場合は、推測でコードを書かず、先に確認質問をしてください。

# 出力形式
1. 実装方針と主なトレードオフ
2. 完全なUserScriptを1つの `javascript` コードブロック
3. インストール、確認、元に戻す手順
4. 未確認事項
````

### AdGuardユーザールールをUserScriptに置き換える場合

単純な構文変換ではなく、ルールの目的をJavaScriptで再実装します。ネットワークブロック、HTMLフィルタリング、ScriptletなどはUserScriptでは同じタイミングや権限で再現できないことがあります。

```text
# タスク
以下のAdGuardユーザールールの目的を分析し、TampermonkeyまたはViolentmonkey用UserScriptで安全に再現可能か判定してください。

# 必須条件
- 要素非表示、ネットワークブロック、例外、Scriptletなど、各ルールの種類と目的を説明してください。
- UserScriptは通常、ページ読み込み前のネットワークリクエストをAdGuardと同じ方法では遮断できない点を考慮してください。
- 同じ動作、タイミング、適用範囲を再現できない場合は、コードを出力せず「同等変換不可」と回答してください。
- 再現可能な場合は、対象URLを限定し、必要最小限の権限で、SPAと動的DOMを考慮した完全なUserScriptを作成してください。
- 元ルールよりプライバシー、性能、ちらつき、保守性が悪化する点を明記してください。

# 出力形式
1. 判定: 変換可能 / 一部のみ可能 / 同等変換不可
2. ルールごとの分析
3. 変換可能な場合のみ、完全なUserScriptを1つの `javascript` コードブロック
4. 動作確認とロールバック手順

# 変換対象
（ここにAdGuardユーザールールを貼り付ける）
```

---

## 主要な生成AI
* **[ChatGPT](https://chat.openai.com/)**：汎用性が高い + 多様なモード。
* **[Gemini](https://gemini.google.com/)**：汎用性 + マルチモーダル + 膨大な情報を高速で読み込み回答を出力（Gemini Pro）。
* **[GitHub Copilot](https://github.com/features/copilot)**：コーディング用。
* **[Grok](https://grok.com/)**：汎用性 + 制限が緩い - 𝕏の投稿の信憑性をチェックするのに使えそう？
  * xAI Support Teamへの問い合わせ先 `support@x.ai` / [Contact: Get in Touch with xAI](https://x.ai/contact)
  * [xAIアカウントのMFA（多要素認証）を紛失してログイン不能 → xAIアカウント削除のために問い合わせ](https://docs.x.ai/console/faq/accounts#ive-forgotten-my-multi-factor-authentication-mfa-method-can-you-remove-it) てから5ヶ月後に [返信](https://imgur.com/a/rLKewye) がありました。
  * 問い合わせ用メールは下書きをGemini Proで推敲するも伝わらず、ChatGPT Plusに推敲させたものを再送しました。
  * MFA（多要素認証）を紛失しログイン不能になったxAIアカウントは、有料プランに加入していない場合、[1年以上（over a year）の非アクティブ状態が継続すると自動的に削除（または停止）される](https://x.ai/legal/terms-of-service#termination-suspension-discontinuation) 対象となります。
  * 削除後、アカウントのデータは法的義務などの例外を除き、通常30日以内にシステムから消去されます。
* **[SDXL](https://stablediffusionweb.com/)**：狙い撃ち・人物や複雑な構図の生成で優秀。
* **[z.ai GLM-4.5](https://chat.z.ai/)**：無料でそこそこの性能・ローカルで動かせる。

**資料**
* [メインで使われている生成AIと統合開発環境（IDE）](https://mond.how/ja/topics/iozm87r4wyxx8ao/amp4bswp4hi8d0m)
* [5年後の主要な生成AIサービス（予測シェア）2026/05/24時点](https://mond.how/ja/topics/lahgbycmk0p72zr/1adfp0b6xmc4hps)

---

## Web サービス統合リスト

### AdGuard 関連サービス・サポート群
AdGuardドメイン（adguard.com系）で提供されている監査・ステータス・公式サポートを統合しています。
* [AdGuard 診断ページ](https://adguard.com/ja/test.html)
* [Webサイトをチェック (AdGuard)](https://reports.adguard.com/ja/welcome.html)
* [AdGuard Status](https://status.adguard.com/)
* [AdGuard > サポートセンター](https://adguard.com/ja/support.html)

### Google 関連サービス・管理群
Googleドメイン（google.com系）の検索・プライバシー管理、ステータス、各種ヘルプ・トラッカーを統合しています。
* [Google あなたに関する検索結果](https://myactivity.google.com/results-about-you)
* [Google ニュース提供元の優先度](https://www.google.com/preferences/source?hl=ja)
* [Google Workspace ステータス ダッシュボード](https://www.google.com/appsstatus/dashboard/#hl=ja&v=status)
* [Google Issue Tracker](https://issuetracker.google.com/home)
* [Google ヘルプ](https://support.google.com/?hl=ja)
* [Google Pixel ヘルプ](https://support.google.com/pixelphone/?hl=ja#topic=)
* [Chromebook ヘルプ](https://support.google.com/chromebook/?hl=ja#topic=)

### AI分析・診断ツール
ユーザーローカル（userlocal.jp系）で提供されているAI関連の分析・診断ツールです。
* [AI性チェッカー](https://ai-tool.userlocal.jp/x_llm_match)
* [𝕏ポスト性格診断](https://ai-tool.userlocal.jp/x_shindan)

### 画像共有・データ削除管理
Imgur（imgur.com）のアップロード・削除申請、およびオンラインデータの削除リクエストツールです。
* [imgur Upload](https://imgur.com/upload)
* [Imgur Removal Request](https://imgur.com/removalrequest)
* [Redact](https://redact.dev/)

### ネットワーク環境・コンテンツブロック検証
接続環境の性能評価や、広告ブロッカー・セキュリティ保護機能の有効性を確認する専門ツールです。
* [確認君+（Plus）](https://env.b4iine.net/)
* [インターネット回線スピードテスト | USEN GATE 02](https://speedtest.gate02.ne.jp/)
* [Octane 2.0 plus](https://octane.webmarks.info/ja/)
* [AdBlock Tester](https://adblock-tester.com/)
* [Test Ad Block - Toolz](https://adblock.turtlecute.org/)
* [Norton Safe Web](https://safeweb.norton.com/)

### サービス稼働状況・障害検知
外部インフラやSNS、掲示板などのリアルタイムな死活・障害状況・トレンドを確認します。
* [Downdetector](https://downdetector.jp/)
* [サイトはダウンしている？](https://www.websiteplanet.com/ja/webtools/down-or-not/)
* [Yahoo!リアルタイム検索](https://search.yahoo.co.jp/realtime/)
* [GitHub Status](https://www.githubstatus.com/)
* [5chサーバ稼働状況](https://www.kyodemo.net/sdemo/k/5_?hs=1)
* [偽 SPARROW AIM-7P Ver.1.00](https://5ch.ape.jp/SPARROW/)

### ファイル共有・メディア編集ユーティリティ
ブラウザ上で大容量ファイルの転送や、画像・動画・圧縮ファイルの加工・変換を行います。
* [GigaFile便](https://gigafile.nu/)
* [Gofile](https://gofile.io/home)
* [123apps](https://123apps.com/ja/)
* [iLoveIMG](https://www.iloveimg.com/ja)
* [Fotoramio](https://fotoram.io/jp)
* [ezyZip](https://www.ezyzip.com/ja.html)
* [AddYoutube.com](https://addyoutube.com/)
* [YouTubeMP3もどき](https://receive.shamimomo.net/YouTubeMP3modoki/)

### テキスト作成・マークダウンエディタ
プレーンテキストやMarkdownの記述、共有に特化したオンラインエディタです。
* [Dillinger](https://dillinger.io/)
* [Writebox](https://write-box.appspot.com/)
* [Writening](https://writening.net/)

### 統計・サポート・情報メディア・その他
アクセス統計、各種ジェネレーター、通信キャリアの手続き、および技術情報サイトです。
* [Statcounter](https://gs.statcounter.com/)
* [Xranks](https://xranks.com/ja/)
* [docomo オンライン手続きサポート](https://tetsuduki-support.docomo.ne.jp/)
* [VRSNS風ロゴジェネレーター](https://logo-bzr.pages.dev/)
* [mond](https://mond.how/)
* [Eylenburg's Tech Website](https://eylenburg.github.io/)
* [innovaTopia](https://innovatopia.jp/)
* [Sundry Street](https://sundryst.com/)

---

## セキュリティ・プライバシー・匿名性の違い

* **セキュリティ（システムの堅牢性と防護）**

    鍵のかかった強固な檻の中に手紙が入っている状態。外部からの物理的な強奪や破壊からは守られているが、檻が透明であれば手紙の内容は見えてしまう。外部の脅威から情報を「防護」することはできても、中身を隠せる（機密性）とは限らない。

* **プライバシー（情報の機密性と自己コントロール権）**

    手紙が中身の透けない封筒に入っている状態。誰に読ませるかを自分でコントロールできるが、守るための檻（セキュリティ）がなければ封筒は容易に盗まれ、破られてしまう。プライバシーを守るためには、基盤となる強固なセキュリティが不可欠である。

* **匿名性（行動と身元の切り離し・特定の不可能性）**

    手紙の中身は公開されているが、差出人も宛先も白紙である状態。情報自体を隠すのではなく「誰の行動か」を隠すが、筆跡や消印（IPアドレスやメタデータ）から身元が推測されるリスクは常に伴う。

* **【結論】セキュリティとプライバシーは相互依存する別物である**

   高水準のセキュリティ（強固な檻）が提供されていても、サービス提供者自身が手紙の中身を覗き見ている場合、プライバシーは守られていない。逆に、プライバシー（封筒）があっても、セキュリティが脆弱であれば情報は外部の攻撃者によって簡単に暴かれてしまう。

---

## 特殊詐欺対策
**！[警察庁・SOS47特殊詐欺対策ページ](https://www.npa.go.jp/bureau/safetylife/sos47/)**

**成りすまし・その他の特殊詐欺**

警察官、医師、弁護士、自治体職員などを名乗る電話やLINEでの個人情報の聞き取り・金銭の要求は、特殊詐欺の可能性が極めて高いです。日本では、公的機関や企業が重要な連絡・手続きを電話やLINEのみで行うことは通常ありません。還付金詐欺、サポート詐欺、当選詐欺、企業の音声案内を装う手口が典型例です。安易に金銭を支払ったり個人情報を教えたりせず、スパムフィルタ導入などの対策を取り、まずは詐欺を疑ってください。

**SNSの投資・ロマンス型詐欺**

SNSでは短期間で高収入を得られる副業や闇バイトの勧誘が多いです。今後、生成AIによる著名人の偽画像・音声・動画を使った投資詐欺やロマンス詐欺が増加すると予想されます。LINEなどへの誘導や不審な勧誘に安易に応じず、情報源を十分に確認するなど、一層の注意が必要です。

**！[日本電話番号検索](https://www.jpnumber.com/)**

**注意が必要な特殊な電話番号**
1. `+` で始まる or `+81-` → 国際電話で折り返し電話をすると高額な通話料や利用料が発生する場合があります。
2. 末尾が `-0110` → 警察署の番号を装った詐欺電話の可能性があります。
3. `0120-` or `0800-` → 電話を受けた側（フリーダイヤルの契約者）が通話料を全額負担します。
4. `050-` → IP電話の番号を悪用した迷惑電話である可能性があります。
5. `0570-` → ナビダイヤルの通話料は、発信者（電話をかけた側）が全額負担します。
6. `0180-` → 情報料として通話料とは別に料金が発生します。

**フィッシング詐欺**

フィッシング詐欺では、常に疑う意識が不可欠です。SMSやメールで利用規約確認やパスワード更新の通知が来ても、本文中のURLはクリックせず、ログインは公式アプリ経由、または正規サイトをブックマーク登録し、パスワードマネージャーを使いアクセスしましょう。不審な点があれば、正規サイトのサポートに問い合わせ、2段階認証やパスキーを設定してください。

**悪質なECサイト**

支払い方法が銀行振込のみのサイトや、商品未開封でも返品時にキャンセル料が発生するECサイトは、詐欺寄りの悪質サイトの特徴とのことです。

**SEOポイズニング**

ログインやECサイト利用時にGoogleなどの検索エンジンの検索結果を経由する癖をつけていると、SEOポイズニングの餌食になる可能性があります。SEOポイズニングとは、SEO技術を悪用し、不正サイトを検索結果上位に表示させて、ユーザーをマルウェア感染や詐欺サイトに誘導するサイバー攻撃です。

ブラウジング中にコンテンツブロッカーを使うことで、特殊詐欺に遭う確率を大幅に下げることができるので、多層防御の1つに加えてもよいかと思います。個人的に特殊詐欺に遭う確率を最小限に抑えることを最優先事項にしているので、広告を非表示にするサブスクリプションの利用も考慮しています。

**参考サイト**
* [詐欺サイト対策 Wiki*（Kdroidwin氏寄稿）](https://wikiwiki.jp/antiscamsite/)
* [おたくま経済新聞｜【特集】STOP！ネット詐欺！](https://otakuma.net/category/internet/internet-scam)
* [SEOポイズニングとは？仕組みや対策をわかりやすく解説](https://www.lanscope.jp/blogs/cyber_attack_cpdi_blog/20240530_20684/)

---

## AdGuard 公式フィルタ

**AdGuard filters**
* [組み込みフィルタリスト・標準フィルタリスト](https://adguard.com/kb/ja/general/ad-filtering/adguard-filters/) と呼ばれることが多いです。

[Yuki2718氏のよくある質問](https://github.com/Yuki2718/adblock2/wiki/よくある質問) より引用
> Q 4-8：uBlock Origin以外のブロッカー（PC）でおすすめのフィルタ構成を教えてください。

> A 4-8：AdGuardでは組込みのフィルタを使っていただくのが無難と思います。AdGuardはuBlock Origin文法の大部分をサポートしていることになっていますが、実際は仕様の違いにより効かなかったり、動作が異なったりすることもあり、そうした細かい仕様は公式ドキュメントに必ずしも載っていません。当然ですが、AdGuardのフィルタはAdGuard上で完璧に動作します4-9。AdGuard日本語フィルタはかつて不評でしたが、今では昔と別物といってよいほど精度が高くなっています。

**コンテンツブロックフィルタ**
* **[AdGuard 公式フィルタ](https://github.com/AdguardTeam/AdguardFilters)**：AdGuardの接頭語 or `#recommended` のタグが付く各種フィルタ + 日本語フィルタ。
* **[Online Malicious URL Blocklist](https://gitlab.com/malware-filter/urlhaus-filter)**：uBlock Origin ＆ AdGuardの標準セキュリティフィルタ。
* **[uBlock Origin – Badware risks](https://github.com/uBlockOrigin/uAssets)**：Yuki2718氏がフィルタの監修に関わっています。

※ ChromeのDNR静的ルールは、拡張機能ごとに30,000件以上が保証されます。保証枠を超えて利用できる件数は、他の拡張機能の使用状況などで変動するため、固定の上限として扱わず `getAvailableStaticRuleCount()` で確認する必要があります。

**カスタムフィルタ・ユーザールール**
* **カスタムフィルタ**
  * **[AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)**：Yuki2718氏自身がフィルタの監修をしています。
  * **[AdGuard module - not for independent use](https://github.com/Yuki2718/adblock2)**：上記フィルタのmodule。
  * **[自作のカスタムフィルタ](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex)**：各フィルタ作者様のルールを参考にしたり、自作のルールと組み合わせたりして作成しています。

**参考サイト**
* [Yuki2718/adblock2 > AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)
  
  AdGuard Japanese filterを補完するフィルタ。迂回広告や悪質ポップアップ、一部のAnti-Adblockへの汎用的な追加対策。

**DNSフィルタ**
* AdGuard for Android：DNS通信を保護 > DNSフィルタ > [AdGuard DNS filter](https://github.com/AdguardTeam/AdGuardSDNSFilter)

**例外ルール**
サイトの機能やAndroidアプリの動作を阻害するルールを例外（`@@`）にすることが多いです。

**AdGuardユーザールール作成ガイド**
* [なんJ AdGuard部 Wiki* > フィルタ構文](https://wikiwiki.jp/nanj-adguard/%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E6%A7%8B%E6%96%87)
* [AdGuard-自分の広告フィルタを作成する方法](https://adguard-com.translate.goog/kb/ja/general/ad-filtering/create-own-filters/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp)
* [AdGuard - DNS filtering rules syntax](https://adguard--dns-io.translate.goog/kb/ja/general/dns-filtering-syntax/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp)

**Issues報告**

AdGuardでの広告ブロック漏れ、Anti-Adblock Scriptによるコンテンツブロッカー検出、コンテンツブロックフィルタの誤ブロックといったフィルタ関連の不具合は、以下のいずれかの方法でGitHub Issuesで報告してください。

▶ AdGuard for AndroidにおけるFilter Issuesは、HTTPSフィルタリングの使用が前提となって対処されます。

詳細な検証にはブラウザのデベロッパーツールが使えます。
* [概要｜Chrome DevTools｜Chrome for Developers](https://developer.chrome.com/docs/devtools/overview?hl=ja)
* [ブラウザーの開発者ツールとは｜MDN](https://developer.mozilla.org/ja/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)
* [ウェブ開発の学習 | MDN](https://developer.mozilla.org/ja/docs/Learn_web_development)

**報告用Webサイト**
* [AdGuard Filters Issues reporting tool](https://reports.adguard.com/ja/new_issue.html)
またはAdGuard製品に搭載されている報告ツールを使います（[報告方法ガイド](https://adguard.com/kb/ja/guides/report-website/)）。

報告されたIssuesは [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues) に反映されます。
Issues報告はGitHubアカウントがなくても可能ですが、GitHubアカウントがあるとIssuesやコメントの編集ができるようになります。報告の形式には自由記述形式とテンプレート形式があり、いずれも問題の切り分けと再現方法の説明に、ある程度の慣れが必要です。

報告時に重要となるのは「**問題が発生するサイトのURL**」「**問題の再現手順**」「**問題発生時のスクリーンショット**」「**ロガーのスクリーンショット**」です。必要に応じてスクリーンショットにマーキングしたり、ログや設定ファイルを添付します。
GitHubでのやり取りは基本的に英語ですが、ツールを使い分けるとスムーズです（Google翻訳で全体を把握し、DeepL翻訳を活用するなど）。▶ [Issues例](https://github.com/AdguardTeam/AdguardFilters/issues/217897)

Issuesのコメント欄を下書きし、Geminiに推敲とMarkdown形式への変換を依頼することもできます。▶ [Issues例](https://github.com/Kdroidwin/uB-filter-by-kdroidwin/issues/11)

**Issues報告・補足**
* [AdGuardフィルタポリシー](https://adguard.com/kb/ja/general/ad-filtering/filter-policy/) に従って処理されます。
* [AdGuard Sitereport website](https://github.com/AdguardTeam/ReportsWebApp)

---

## AdGuard ブラウザ拡張機能 MV3対応版
* **[Chrome Web Store](https://chromewebstore.google.com/detail/adguard-%E5%BA%83%E5%91%8A%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/bgnkhhnnamicmpeenaelnjfhikgbkllg)**
* **[HP](https://adguard.com/ja/adguard-browser-extension/overview.html)** / **[GitHub](https://github.com/AdguardTeam/AdguardBrowserExtension)**

AdGuard ブラウザ拡張機能 MV3対応版でスクリプトレットを含む高度なルールを使用する場合は、拡張機能の内部設定から**ユーザースクリプトを許可する**トグルを有効にする必要があります。組み込み・カスタムフィルタは、拡張機能本体の更新に加え、対応バージョンではポップアップまたはフィルタ画面から手動更新を確認できます。

v5.2.400以降、拡張機能と組み込み・カスタムフィルタは、「ツールバーのアイコン > 右上ポップアップの↻」または「フィルタ > ↻アップデートを確認する」から最新状態を確認できます。

v5.2.400で強化された機能は、設定画面内でカスタムフィルタを手動で更新できるようにするものです。

（※ Chromeの拡張機能管理画面での「更新ボタン↻」では、カスタムフィルタの再読み込みがトリガーされないケースが報告されています。 [Issues #2944](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2944)  / [Issues #3016](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3016)）

[AdGuard ブラウザ拡張機能 MV3対応版 v5.4.1.3](https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.4.1.3)

ポップアップパネルの更新ボタン↻、またはフィルタセクションの更新ボタン↻から、カスタムフィルタを手動で更新できるようになりました。`! Version:` は版の識別と更新状況の確認に有用ですが、URLの再取得そのものを成立させる唯一の条件ではありません。

* **[AdGuard ブラウザ拡張機能 MV3対応版の解説](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)**

**カスタムフィルタで購読する場合**

`AdGuard module - not for independent use` は、`AdGuard Japanese filter Plus` のサブリストとして自動的にincludeされます。

**ユーザールールにルールを全コピー & 全ペーストする場合**

両方のフィルタのルールを全コピー & ペーストする必要があります。

**! カスタムフィルタ・ユーザールール**
* AdGuard Japanese filter Plus
  ```
  https://yuki2718.github.io/adblock2/japanese/jpf-plus.txt
  ```
* AdGuard module - not for independent use
  ```
  https://yuki2718.github.io/adblock2/japanese/jpfp-ag.txt
  ```

**❗️留意点**

 [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues) への報告が煩雑になるため、カスタムフィルタは基本的に上記2種以外は追加しないほうが良いです。

**Filter Issues**
* [AdGuard Japanese filter Plus Issues](https://github.com/Yuki2718/adblock2/issues)

**開発者ツールと連動した手動ブロック機能**

開発者ツールと連動した手動ブロック機能が搭載されています（[画像](https://imgur.com/DcEH4K4)）。作成したルールはユーザールールに格納されます。

**Chromeのアドレスバーから新しいタブでユーザールールを開く**

* アドレスバーに以下をコピー & ペーストして移動します。
  ```
  chrome-extension://bgnkhhnnamicmpeenaelnjfhikgbkllg/pages/fullscreen-user-rules.html?theme=system
  ```

**参考サイト**
* [はちまブログ > uBlock Origin](https://hachima25.hatenablog.com/archive/category/uBlock%20Origin)
  
  マイフィルタが分かりやすく紹介されています。
* [r/uBlockOrigin > solutions > youtube](https://www.reddit.com/r/uBlockOrigin/wiki/solutions/youtube/)
* [r/uBlockOrigin > solutions > twitter](https://www.reddit.com/r/uBlockOrigin/wiki/solutions/twitter/)
* [YouTube Fix & Customizations（Reddit）](https://www.reddit.com/r/youtube/comments/1b40hra/youtube_fix_customizations_4_videos_per_row/)
* [White area on Youtube（Reddit）](https://www.reddit.com/r/uBlockOrigin/comments/1l4r84i/white_area_on_youtube/)
  
  YouTubeのホーム画面から、Shortsやおすすめなどの特別セクションを単なる非表示ではなくDOMから完全に削除（:remove()）するuBlock Origin用のフィルタです。動画サムネイル整列時の不自然な空白を防ぐ目的で使用されます。
    ```
    www.youtube.com##ytd-browse[page-subtype="home"] ytd-rich-section-renderer:remove()
    ```
  [Enhancer for YouTube™](https://chromewebstore.google.com/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle) を使う場合、いくつかのUI調整ユーザールールは不要になります。

**Web版YouTubeについての留意点**

YouTube Anti-Adblock回避ルールは、uBlock Origin開発チームの解析を参考にAdGuardが開発・調整しています。YouTube Premium未加入者がカスタムフィルタや拡張機能を使いすぎると、検知されやすくなります。無料利用する際は、公式ルールのみの使用が推奨されます。要件を満たさない報告はuBlock Origin開発チーム・AdGuard開発チームの負担となります。Yuki2718氏はuBlock Origin開発チームに所属しながらWeb版YouTubの解析を行っています（[Issues #27415](https://github.com/uBlockOrigin/uAssets/issues/27415)。 / [Issues #28707](https://github.com/uBlockOrigin/uAssets/issues/28707)）。

**𝕏/Twitter ルール作り資料｜uBlock Origin**

* [uAssets（𝕏投稿）](https://x.com/Red_Frame_X/status/2010925824636252329)
* [uAssets / filters / filters-2023.txt](https://github.com/uBlockOrigin/uAssets/blob/e4933fdffaaaa318f58fb8a7a34d784220100ff2/filters/filters-2023.txt#L4284-L4288)
* [json-prune-xhr-response.js](https://github.com/gorhill/uBlock/wiki/Resources-Library#json-prune-xhr-responsejs-)

---

## Chrome 拡張機能 uBlacklist
* **[Chrome Web Store](https://chromewebstore.google.com/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe)**
* **[HP](https://iorate.github.io/ublacklist/ja/docs)** / **[GitHub](https://github.com/iorate/ublacklist)**

uBlacklistは、Googleなどの検索結果から指定したWebサイトを非表示にする拡張機能です。正規表現ルール、クラウド同期、公開ブラックリストの購読などが可能です。

**! ブラックリストを追加する**
* uBlacklist-filter-by-kdroidwin 1
  ```
  https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt
  ```
* uBlacklist exclusionフィルター（除外用）
  ```
  https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist-Exclusion.txt
  ```

* 検索結果の非表示ルール例
  ```text
  *://*.example.com/*
  /example\.(net|org)/
  title/Example Domain/
  ```
* 例外ルール（再表示ルール）例
  ```text
  @*://*.example.com/*
  ```

**Filter Issues**
* [uB-filter-by-kdroidwin Issues](https://github.com/Kdroidwin/uB-filter-by-kdroidwin/issues)

**参考サイト**
* [Kdroidwin / uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)
* [コミュニティルールセット｜uBlacklist](https://ublacklist.github.io/ja/rulesets)

---

## Android アプリ personalDNSfilter（ChromeOS）
* **[Google Play](https://play.google.com/store/apps/details?id=dnsfilter.android)**
* **[HP](https://www.zenz-solutions.de/personaldnsfilter-wp/)** / **[GitHub](https://github.com/IngoZenz/personaldnsfilter)** / **[FAQ](https://www.zenz-solutions.de/faq/)**

**personalDNSfilter（ローカルVPNモード）の常駐・DNS設定**

Android向けの[公式FAQ](https://www.zenz-solutions.de/faq/)に沿った設定メモです。ChromeOS上のAndroid環境では、設定項目の有無やDNSが処理される範囲を実機で確認します。

* **常駐対策**：personalDNSfilterをバッテリー最適化の対象から除外し、バックグラウンド動作を許可します。ローカルVPNモードでは、AndroidのVPN設定で「常時接続VPN」を有効にします。設定名・導線はOSや端末によって異なり、停止を完全に防ぐ保証はありません。
* **「VPNなしの接続をブロック」は無効のままにします**。personalDNSfilterはDNS問い合わせだけを処理するため、この設定を有効にすると通常のインターネット通信が遮断されると公式FAQに明記されています。
* **DNSフィルタリングの迂回対策**：Androidの「プライベートDNS」と、Android版Chromeの「セキュアDNSを使用」を無効にします。これはDNS問い合わせをpersonalDNSfilterに処理させるための設定であり、VPNの停止を防ぐ設定ではありません。
* **DNS通信の暗号化**：OS・ブラウザ側の暗号化DNSを無効にする場合は、personalDNSfilter側でDoHまたはDoTの上流DNSを設定します。[公式製品説明](https://www.zenz-solutions.de/personaldnsfilter-wp/)に両方式の対応が記載されています。
* **ChromeOS側の設定**：「サイトのルックアップに安全な接続を使用する」の無効化は、上記のAndroid向けFAQからChromeOS全体へ一律に適用しません。ChromeOS側のDNSもpersonalDNSfilterで処理する構成では、設定変更前後の問い合わせがアプリのログに記録されるか確認します。Android環境内で動作しているだけでは、ChromeOS全体への適用を確認したことにはなりません。

通知のサイレント化は、通知音などを抑えるための任意設定です。VPNの安定化対策には含めません（[Android公式：通知の管理](https://support.google.com/android/answer/9079661?hl=ja)）。VPNプロファイルの削除・再設定も、公式FAQで一般的な安定化対策として確認できないため、常用手順には含めません。

ログのドメインを長押しすると、ブラック/ホワイトリストへの登録が可能です。

※ 実態はDNSブロッカーのため、ABP形式の構文（`||example.com^`）には対応していません。

**! 購読済みのDNSブロックリスト・hostsファイル**
* HaGeZi's Normal DNS Blocklist
  ```
  https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt
  ```

**参考サイト**
* [HaGeZi's DNS Blocklists](https://github.com/hagezi/dns-blocklists)：世界で最も高評価な有志による統合型DNSブロックリスト。
  * [gitlab.com/hagezi/mirror](https://gitlab.com/hagezi/mirror)：1日1回、GitHubと同期して更新。
  * [codeberg.org/hagezi/mirror2](https://codeberg.org/hagezi/mirror2)：1日1回、GitHubと同期して更新。
  * [hagezi-mirror.dnsbunker.org](https://hagezi-mirror.dnsbunker.org)：4〜8時間ごとに更新。

---

## Android アプリ 有償版 AdGuard for Android（Android）
* **[HP](https://adguard.com/ja/adguard-android/overview.html)** / **[GitHub](https://github.com/AdguardTeam/AdguardForAndroid)**

**AdGuard for Android（ローカルVPNモード）の常駐・DNS設定**

**常駐・再起動対策**
* AdGuardのバックグラウンド動作を許可し、バッテリー最適化の対象から除外します。Pixelでの設定例：設定 > アプリ > AdGuard > アプリのバッテリー使用量 > バックグラウンドでの使用を許可 > 制限なし。設定名・導線はAndroidのバージョンや端末によって異なります。
* バックグラウンドで停止する場合は、AndroidのVPN設定でAdGuardの「常時接続VPN」を有効にします。[AdGuard公式のメーカー別対処手順](https://adguard.com/kb/adguard-for-android/solving-problems/background-work/)でもPixelなどに案内されています。有効化後も、端末再起動後にアプリの保護状態を確認します。
* **「VPNなしの接続をブロック」は別機能です**。有効にするとVPNから除外したアプリも通信できなくなるため、安定化目的では有効にしません（[Android公式：VPN](https://developer.android.com/develop/connectivity/vpn#blocked-connections)）。

**AdGuardのDNS保護を利用する場合**
* DNS処理をAdGuardに集約する場合は、Androidの「プライベートDNS」を無効にします。AdGuard公式は、Android 10以降のプライベートDNSによるDNS処理の迂回を説明しています。これはDNSフィルタリングの整合性を保つための設定です（[公式互換性情報](https://adguard.com/kb/adguard-for-android/solving-problems/compatibility-issues/#private-dns)）。
* ブラウザの「セキュアDNSを使用」の無効化は、DNS設定をAdGuardに集約する方法の一つです。ただし必須ではありません。AdGuardのローレベル設定「Filter secure DNS」には、ブラウザ指定のDNSを利用したままDoHを処理する方式と、AdGuardのDNSプロキシへ転送する方式があります。利用するブラウザ・設定でDNS問い合わせが処理されるか確認します（[公式仕様](https://adguard.com/kb/adguard-for-android/features/low-level-settings/#filter-secure-dns)）。
* OS・ブラウザ側の暗号化DNSを無効にする場合は、AdGuardのDNS保護でDoH・DoTなどの暗号化DNSサーバーを設定します。代替の暗号化を設定せずに無効化すると、DNS問い合わせが暗号化されない可能性があります（[公式：DNS保護](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)）。

**任意設定・不具合時の切り分け**
* 通知のサイレント化は通知音などを抑えるための任意設定で、VPN維持のための設定ではありません（[Android公式：通知の管理](https://support.google.com/android/answer/9079661?hl=ja)）。
* 「接続の自動調整」は一律に無効化しません。Googleは省電力のための有効化を案内しています。接続切り替え時に不具合がある場合だけ、該当項目を一つずつ変更して再現性を比較し、改善しなければ元に戻します。これは切り分け案であり、AdGuard公式の必須設定ではありません（[Google公式：ネットワーク設定](https://support.google.com/pixelphone/answer/2819583?hl=ja)）。
* VPNプロファイルの削除・再設定は、一般的な安定化対策として公式の裏付けを確認できないため、常用手順には含めません。停止が続く場合は、メーカー別の常駐設定を確認し、発生時刻と[デバッグログ](https://adguard.com/kb/adguard-for-android/solving-problems/log/)を記録して原因を調べます。

⚙ > 一般設定 > 詳細設定 > ローレベル設定 > その他の設定 - 「メイン画面にデベロッパーツールを表示する」をONにすると、ホーム画面右上にレンチアイコンが表示され設定アクセスが容易になります（[画像](https://imgur.com/UKGTVnZ)）。

**HTTPSフィルタリング**

Android版Chromeなどで高精度なブロックを行うには必須です。暗号化通信を一時解析し、要素をブロックします。Personal CA証明書のインストールが必要です。

**CoreLibs**

ネットワークフィルタリングの心臓部（[GitHub](https://github.com/AdguardTeam/CoreLibs)）はプロプライエタリですが、フィルタリングルールやScriptletsはオープンソースです。

**HTTPSフィルタリング対象外Webサイト**

予期せぬ不具合回避のため除外されているドメインがあります（例: [Issues #6016](https://github.com/AdguardTeam/AdguardForAndroid/issues/6016)）。

**❗️留意点**

 HTTPSフィルタリングの有効化は、AdGuard社への根本的な信頼が前提となります（[参考回答](https://mond.how/ja/topics/2e44jvg4wahf54j/oupbjuuxjlg4tjl)）。OFFにするとドメイン単位のブロックのみとなります。金融・決済系アプリは「アプリの除外設定」「仕事用プロファイル」「プライベートスペース」への隔離運用がおすすめです。

**ローカルVPNによる監視を行わず、強力な内蔵ブロッカー単体で遮断できるブラウザ**
* [Brave](https://play.google.com/store/apps/details?id=com.brave.browser) ▶ [AdGuard Mobile Ads filter](https://filters.adtidy.org/extension/ublock/filters/11_optimized.txt) を追加
* [Cromite](https://github.com/uazo/cromite)
* [Elixir Browser](https://github.com/SF-FLAM/ElixirBrowser)
* [Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox)

* 参考：[HTTPSフィルタリングについて（Wiki）](https://wikiwiki.jp/nanj-adguard/HTTPS%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6) / [中間者攻撃とは](https://www.nri-secure.co.jp/glossary/mtm-attack)

**! カスタムフィルタ・ユーザールール**
* AdGuard Japanese filter Plus
  ```
  https://yuki2718.github.io/adblock2/japanese/jpf-plus.txt
  ```
* AdGuard module - not for independent use
  ```
  https://yuki2718.github.io/adblock2/japanese/jpfp-ag.txt
  ```
**❗️留意点**

 [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues) への報告が煩雑になるため、カスタムフィルタは基本的に上記2種以外は追加しないほうが良いです。

**Filter Issues**
* [AdGuard Japanese filter Plus Issues](https://github.com/Yuki2718/adblock2/issues)

**DNS通信を保護 > DNSフィルタ**

[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) によるブロックはシステム全体に及びます（[DNS書き換えの基本](https://writening.net/page?keELEF)）。
プライバシー関連のルールによる不具合（[Issues #217896](https://github.com/AdguardTeam/AdguardFilters/issues/217896), [#220178](https://github.com/AdguardTeam/AdguardFilters/issues/220178)）を緩和する方法。

① **[AdGuard DNS filter without privacy filters (Ads only)](https://github.com/kitadai31/AdGuardSDNSFilter_withoutPrivacyFilters)**

② **[AdGuard_DNS_Filter_for_myself](https://github.com/monsivamon/AdGuard_DNS_Filter_for_myself)**

③ **DNSユーザーフィルタ** で自作例外ルール（`@@`）を作成。

**DNSサーバー & ChromeOS追加設定**

AdGuard内でDNSを設定します（Google Public DNS推奨）。
ChromeOS追加設定: 設定 > ネットワーク > Wi-Fi > ルーター > ネームサーバー > [Google ネームサーバー](https://developers.google.com/speed/public-dns/docs/using?hl=ja#chromeos) に変更。

**トラブルシューティング**
* **Wi-Fi接続不良**：IPv6フィルタリングをOFFにする。
* **フィルタ自動更新不可**：ホーム画面の↻を手動タップ。

**拡張機能（有償）**
* [tinyShield](https://github.com/FilteringDev/tinyShield/blob/main/README.ja.md)（Ad-Shield対策、原則不要）
* [最上部/最下部 移動ボタン追加](https://github.com/PermanentWave/SetTopAndBottomButtons)

**Product Issues**
* [AdGuard for Android Issues](https://github.com/AdguardTeam/AdguardForAndroid/issues)

**参考サイト / 質問テンプレ**
* [なんJ AdGuard部 Wiki*](https://wikiwiki.jp/nanj-adguard/) / [5ch【広告除去】AdGuard](https://ff5ch.syoboi.jp/?q=%E3%80%90%E5%BA%83%E5%91%8A%E9%99%A4%E5%8E%BB%E3%80%91AdGuard)

  ```text
  AdGuard for Androidの質問テンプレ
  【問題が出るWebサイト / Androidアプリ】
  【問題の内容】
  【ライセンス】
  【HTTPSフィルタリング】
  【DNSブロック】
  【使用コンテンツブロックフィルタ】
  【使用DNSフィルタ】
  【その他初期状態から変更した設定】
  【フィルタの更新日】
  【Androidのバージョン】
  【AdGuardのバージョン】
  【機種情報】
   ```

---

## HTTPSフィルタリング・DNSフィルタリング
* **HTTPSフィルタリング：** 通信の中身を端末内で復号・検査・改変し、再暗号化する方式。高機能だがオーバーヘッドが発生する。
* **DNSフィルタリング：** ドメイン名レベルでブロックする方式。高速だがページ内要素単位の細かな制御はできない。

---

## 【解決済み】Android System WebView 問題
**概要**

* AdGuard for Android v4.7.1以上のプライベートブラウザが原因で、WebViewの更新後に自動再起動に失敗する現象がありました。

**対処法（※ローカルVPNの安定化）**

**Android 17の「デバイスの管理」を有効化（Pixel 10aで確認）**

Android 17では、**設設定 > セキュリティとプライバシー > その他のセキュリティとプライバシー > デバイス管理 > アドガード** を開き、AdGuardのトグルをONにします。これにより、システムの最適化によってAdGuardがバックグラウンドで停止されにくくなり、アプリを閉じている間も保護を維持しやすくなります。

* この項目が表示される端末・OSビルドでのみ設定できます。メーカーやAndroidのバージョンによって、項目名や経路が異なる場合があります。
* バックグラウンド停止を完全に防ぐ保証はありません。Android 17では端末のRAM容量に応じたアプリのメモリ上限も導入されており、上限を超えたプロセスは終了される場合があります（[Android Developers](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits)）。
* あわせて、Androidの**常時接続VPN**と**VPN以外の接続をブロック**を必要に応じて設定し、AdGuardのバッテリー使用量を**制限なし**にすると安定性の向上が期待できます（[AdGuard公式タスクキル対策ガイド](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)）。ただし、「VPN以外の接続をブロック」を有効にすると、AdGuard停止時やVPN接続失敗時に通信できなくなる点に注意してください。

① v4.6.5以下（例: [v3.6.11](https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11)）へダウングレード。

② v4.7.1〜v4.9でウォッチドッグ機能を有効化。

③ **MacroDroidを利用したVPN自動再接続タスクの作成**（最も効果的）▶ [MacroDroid](https://play.google.com/store/search?q=MacroDroid&c=apps) をインストール ▶ マクロの作成（[画像参考](https://imgur.com/a/5Xi8h9r)）

  * **AdGuard側**: 設定 ⚙ > 一般設定 > 詳細設定 > 自動化 > トグルONにし「パスワード」をメモ
  * **MacroDroid側 トリガー**：「VPN状態の変化時」> 無効
  * **MacroDroid側 アクション**：「インテントを送信」
    * ターゲット：Broadcast
    * アクション：start
    * パッケージ：com.adguard.android
    * クラス：com.adguard.android.receiver.AutomationReceiver
    * エクストラ1：パラメーター名 `password` ｜ 値 `（メモしたパスワード）`
    * エクストラ2：パラメーター名 `quiet` ｜ 値 `true`

④ **MacroDroidを利用したフィルタ更新タスクの作成**（③を複製してアクションのみ変更）

  * **AdGuard側**: ③と同じく、設定 ⚙ > 一般設定 > 詳細設定 > 自動化をONにし、「パスワード」を使用
  * **MacroDroid側 トリガー**：「VPN状態の変化時」> 無効
  * **MacroDroid側 アクション**：「インテントを送信」
    * ターゲット：Broadcast
    * アクション：`update`
    * パッケージ：com.adguard.android
    * クラス：com.adguard.android.receiver.AutomationReceiver
    * エクストラ1：パラメーター名 `password` ｜ 値 `（メモしたパスワード）`
    * エクストラ2：パラメーター名 `quiet` ｜ 値 `true`

  AdGuard公式の自動化インターフェースでは、`update` は「利用可能なフィルタとアプリの更新を確認する」アクションとして定義されています。追加データは不要ですが、各Intentには `password`、パッケージ名、クラス名が必要で、`quiet: true` を付けるとトーストを抑制できます。したがって、③の `start` を `update` に差し替える構成は公式仕様に沿っています。ただし、`update` はフィルタだけでなくAdGuardアプリ本体の更新確認も含む点に注意してください。（[AdGuard公式：Android版の自動化](https://adguard.com/kb/adguard-for-android/solving-problems/tasker/)）

  ③と④を同じ「VPN状態の変化時 > 無効」トリガーにすると、AdGuardのVPN接続が無効になった際に、③の `start` でAdGuardの保護を再開し、その後④の `update` で利用可能なフィルタとAdGuardアプリ本体の更新を確認できます。AdGuard公式ドキュメントでは、`start` は「保護を開始する」、`update` は「利用可能なフィルタとアプリの更新を確認する」アクションとしてそれぞれ定義されています。（[AdGuard公式：Android版の自動化](https://adguard.com/kb/adguard-for-android/solving-problems/tasker/)）

  この構成の目的は、VPNが無効になったときに「保護の再起動」と「更新確認」を続けて実行し、AdGuardを通常の保護状態へ戻しやすくすることです。ただし、公式ドキュメントには `update` が保護を再起動するとは記載されていないため、④を「2回目の再起動」とみなすことはできません。確実に2回の再起動を行いたい場合は、④の `update` の後に別途 `start` を実行するアクションを追加する必要があります。端末やAndroidの電源管理によって復帰挙動は異なるため、必要に応じて各アクションの間に短い待機時間を入れて動作確認してください。

**Issuesの時系列**
* [Issues #5598](https://github.com/AdguardTeam/AdguardForAndroid/issues/5598)（Base filterの不正確な説明）
* [Issues #5593](https://github.com/AdguardTeam/AdguardForAndroid/issues/5593)（Android 15によるタスクキル）
* [Issues #5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)（WebView更新時の無効化）
▶ [AdGuard for Android v4.10 Nightly 4で修正](https://adguard.com/ja/versions/android/nightly.html#version-41019) されました。

**結論**

* WebViewの影響は v4.10 以降で修正されました。OSによるタスクキル問題は常時接続VPNの有効化やMacroDroidの導入で対処します。（[タスクキル対策ガイド](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)）

---

## AndroidのプライベートDNSを利用したDNSブロック

スマートフォンの「プライベートDNS」設定に特定のホスト名を入力するだけで、端末全体に表示される広告を非表示にすることができます。

**設定手順**

  1. **設定** を開く。
  2. **ネットワークとインターネット** を選択する。
  3. **プライベート DNS** をタップする。
  4. **「プライベートDNSプロバイダのホスト名」** を選択する。

**設定するホスト名**
  * 入力欄に以下のホスト名を入力して保存します。現在はより安定している**新バージョン**の入力が推奨されています。
  
    * **新バージョン（推奨）**：`dns.adguard-dns.com`
    * **旧バージョン** ：`dns.adguard.com`

**コンテンツブロックの対象**
  * **ブラウザ**（ChromeでのWebブラウジングなど）
  * **各種アプリ**（アプリ内のバナー広告など）

---

## Android アプリ ReVanced・Morphe・URV（Android）
公式Androidアプリに改良パッチを適用し、UXを向上させるオープンソースプロジェクトです。
※ビルドツール（Manager）の利用は**自己責任**です（[VirusTotal](https://www.virustotal.com/gui/home/upload) でのスキャン推奨）。APKファイルは [APKMirror](https://www.apkmirror.com/) から調達します。

**略称・ツール**
* **[ReVanced 公式](https://revanced.app/)** / [GitHub](https://github.com/revanced)
* **RVX**: inotia00氏版（[※開発終了 Issues #3334](https://github.com/inotia00/ReVanced_Extended/issues/3334)）
* **[Morphe 公式](https://morphe.software/)** / [GitHub](https://github.com/MorpheApp)（RVX開発陣も合流した新プロジェクト）
  * [Morphe Community Patches](https://morphe-patches.software/)（コミュニティが作成したパッチバンドル）
* **[URV 公式](https://jmancentral.com/)** / [GitHub](https://github.com/Jman-Github)（使いやすい上位互換Manager）

**使い方・質問用テンプレ**

* [Morphe インストール方法（Kdroidwinの日記）](https://kdroidwin.hatenablog.com/entry/2026/02/27/213227)
* [5ch Revanced総合スレ](https://ff5ch.syoboi.jp/?q=Revanced%E7%B7%8F%E5%90%88)

  ```text
   【質問テンプレ】
    [使用したパッチ]：
    [パッチのバージョン]：
    [使用したマネージャー]：
    [マネージャーのバージョン]：
    [使用したMicroG]：
    [MicroGのバージョン]：
    [YouTube apkのバージョン]：
    [Android OSのバージョン]：
    [端末情報]：
    質問内容:
    ```

**補足・Auto Builder**
* [anddea Patch（RVXフォーク）](https://github.com/anddea/revanced-patches/releases)
* [Bundle Search](https://revanced-external-bundles.brosssh.com/)
* [Morphe Patches Auto Builder](https://github.com/monsivamon/morpheapp-apk)
* [RVX（anddea版）Auto Builder](https://github.com/monsivamon/revanced_extended_anddea-apk)

**❗️留意点**

利用規約違反によるアカウント凍結リスクは常に伴います。（[Reddit体験談1](https://www.reddit.com/r/revancedapp/comments/132ojbg/my_account_has_been_suspended_today_and_i_am_no/), [Reddit体験談2](https://www.reddit.com/r/revancedapp/comments/17a6iqj/can_google_suspend_my_account_if_i_use_revanced/)）

Premium加入者は「動画ストリームを偽装（Spoof video streams）」をOFFにすることが推奨されます。
* [YouTube 利用規約](https://www.youtube.com/t/terms) / [ヘルプページ](https://support.google.com/youtube/answer/14129599?hl=ja&ref_topic=15848873&sjid=5246634321435162902-NC) / [GIGAZINE記事](https://gigazine.net/news/20240416-youtube-ad-blocker-crackdown-third-party-apps/)

**𝕏/Twitter ReVancedの使い方**

Modアプリ検知の強化によりログインが困難になっています。（[Issues #714](https://github.com/crimera/piko/issues/714)）
* [導入方法解説](https://pfbcoconut.com/2024/04/21/twitter-x-revanced/) / [ログイン方法更新](https://kdroidwin.hatenablog.com/entry/2025/11/04/210359)
* パッチ・ビルド済みapk：[crimera (Piko)](https://github.com/crimera/piko) / [monsivamon](https://github.com/monsivamon/twitter-apk) / [lluni](https://github.com/lluni/twitter-apk) / [Origin Twitter Neo](https://github.com/YuzuMikan404/Origin-Twitter-Neo)

**併用すると便利かもしれないAndroidアプリ**
* **[File Manager Plus](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager)**
* **[Obtainium](https://github.com/ImranR98/Obtainium)**
* **[YTDLnis](https://github.com/deniscerri/ytdlnis)**
* **[Seal Plus](https://github.com/MaheshTechnicals/Sealplus)**
* **[Yahoo!リアルタイム検索](https://play.google.com/store/apps/details?id=jp.co.yahoo.android.ybuzzdetection&hl=ja)**
* **[GitHub](https://play.google.com/store/apps/details?id=com.github.android)**
* **[Aurora Store](https://auroraoss.com/aurora-store)**
* **[F-Droid](https://f-droid.org/ja/)**
* **[Accrescent](https://accrescent.app/)**
* **[Device Info](https://play.google.com/store/apps/details?id=com.ytheekshana.deviceinfo&hl=ja)**

**参考サイト**
* [r/revancedapp](https://www.reddit.com/r/revancedapp/) / [r/revancedextended](https://www.reddit.com/r/revancedextended/) / [r/MorpheApp](https://www.reddit.com/r/MorpheApp/)
* [5ch Android Twitterクライアント](https://ff5ch.syoboi.jp/?q=Android+Twitter%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88) / [5ch 神アプリスレ](https://ff5ch.syoboi.jp/?q=Android%E3%81%AE%E7%A5%9E%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E6%8C%99%E3%81%92%E3%82%8B%E3%82%B9%E3%83%AC) / [5ch Androidアプリ 質問スレ](https://ff5ch.syoboi.jp/?q=Android%E3%82%A2%E3%83%97%E3%83%AA%E8%B3%AA%E5%95%8F%E3%82%B9%E3%83%AC)
* [Kami-Android-app｜Kdroidwin](https://github.com/Kdroidwin/Kami-Android-app)

---

## Android アプリ ChMate（ChromeOS・Android）
* **[Google Play](https://play.google.com/store/apps/details?id=jp.co.airfront.android.a2chMate)** / **[HP](https://chmate.airfront.co.jp/)**

**ChMate テーマ変更**
* [2chMateのテーマ専用アップローダー](https://ux.getuploader.com/2chmate_theme/)

**アニメーション動作の変更**
* Homeやスレッドの右下︙ > 表示設定 >「リストをアニメーションする」をOFF。

**レクタングル広告について**
* ChMate側の広告と5ch側の広告（レクタングル広告）があり、後者の完全除去にはUPLIFTの購入が必要です（[仕様変更のお知らせ](https://www.airfront.co.jp/pr20250116.html)）。

**代替ブラウザ**
* [したらばStorm](https://play.google.com/store/apps/details?id=jp.everystorm.shitarabastorm) / [Channeler](https://play.google.com/store/apps/details?id=pro.hirooka.channeler)

**IOMate**
* [IOMate](https://github.com/kitadai31/IOMate)
  * 5ch.io対応前の古いChMateで5ch.ioに読み書きするためのローカルプロキシアプリです。

ChromeOS上での完全な動作保証はありません。（[動作環境](https://chmate.airfront.co.jp/docs/supported-os/#%e5%8b%95%e4%bd%9c%e7%92%b0%e5%a2%83%e3%81%ab%e3%81%a4%e3%81%84%e3%81%a6)）
* [Android アプリ ChMate 不具合修正済みメモ](https://writening.net/page?DW58re)

**参考サイト**
* [5chブラウザ「ChMate」質問スレ](https://ff5ch.syoboi.jp/?q=5ch%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%80%8CChMate%E3%80%8D%E8%B3%AA%E5%95%8F%E3%82%B9%E3%83%AC) / [5chどんぐり非公式まとめwiki](https://donguri.wikiru.jp/)

---

## Aluminium OS / Googlebook / Linux
2026年5月のGoogleによる公式発表（The Android Showなど）やリーク情報により、ChromeOSの今後のロードマップが明確になりました。Linux®ディストリビューションの移行についても少し触れておきます。

* Aluminium OS（通称：ALOS）: Androidのカーネルやフレームワークをベースに、デスクトップ環境（ChromeOSのUI/UX）と高度なAI（Gemini）をネイティブ統合した新世代OS。

* Googlebook: Aluminium OSを搭載し、2026年秋以降の展開が予定されている新しいプレミアムデバイス。

既存のChromeOSは2034年頃まで段階的にサポート（セキュリティ保守等）が継続される見込みですが、Androidアプリのネイティブ動作やシステムレベルのAI統合においては、Aluminium OSへの移行が今後のメインストリームとなります。

**ChromeOSの今後の動向**
* [Googlebook 正式発表後もChromebookは継続。Googleが改めて明言した10年サポートと移行方針](https://helentech.jp/news-chromebook-continues-after-googlebook-86132/)
* [Aluminium OSの完全リリースは2028年以降の可能性](https://helentech.jp/news-81647/)
* [ChromeOSは2034年に段階的廃止へ](https://internet.watch.impress.co.jp/docs/yajiuma/2083598.html)
* [Aluminium OSの展開。2026年後半リリース予定](https://helentech.jp/news-chromebook-82961/)
* [AluminiumOS - Android For PC](https://aluminium--os-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp)

**Linux 関連**
* [ChromebookにLinuxをクリーンインストールする方法](https://zenn.dev/roistaff/articles/30ce3883b3b9d9)
* [Linux Mint 22をパソコンにインストールする方法](https://tanoike.com/install-linux-mint-on-pc)
* [Timeshift（バックアップツール）](https://github.com/linuxmint/timeshift) / [使い方](https://sub-log.jp/2022/12/14/linux-mint-%E3%81%A7-timeshift-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%90%E3%83%83%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E3%81%99%E3%82%8B/)
* [Linux Mint搭載 既製品ノートPC](https://raylink-inc.com/product/rl-bnc00010/)
* [AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/)

**ECサイト購入優先順位**
* Amazon.co.jp（セール時） > メーカー直売サイト > 楽天市場 = ヨドバシ.com

---

## Credits
* [5ch【広告除去】personalDNSfilter](https://ff5ch.syoboi.jp/?q=%E3%80%90%E5%BA%83%E5%91%8A%E9%99%A4%E5%8E%BB%E3%80%91personalDNSfilter)
* [r/Adguard](https://www.reddit.com/r/Adguard/) / [r/uBlockOrigin](https://www.reddit.com/r/uBlockOrigin/)
* [AdGuard ナレッジベース](https://adguard.com/kb/ja/) / [AdGuard（𝕏）](https://x.com/AdGuard) / [AdGuardJP（𝕏）](https://x.com/AdGuardJP) / [AdGuard ブログ](https://adguard-com.translate.goog/en/blog/index.html?_x_tr_sl=auto&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp)

**コンテンツブロックに関するアナウンス**
* [Yuki2718氏の𝕏アカウント](https://x.com/Yuki27183) / [Yuki2718’s gists](https://gist.github.com/Yuki2718)
* [雪フィルタ簡易報告掲示板](https://jbbs.shitaraba.net/internet/25463/)
* [コンテンツブロックについてよくある質問と回答](https://github.com/Yuki2718/adblock2/wiki/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E8%B3%AA%E5%95%8F)

**Web技術・参考資料**
* [とほほのwww入門](https://www.tohoho-web.com/www.htm)
* [初めてのWebサイト](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web)
* [サルにもわかる正規表現入門](https://userweb.mnet.ne.jp/nakama/)
* 正規表現：[資料1](https://regex101.com/r/pxx7fR/1) / [資料2](https://uxmilk.jp/50674)
* [uBlock Originでネットを優しい世界に](https://qiita.com/shtainze/items/1136dfc8e245f5c250fe)
* [:has-text()の使い方に関する相談](https://writening.net/page?VjrZNv)
* [Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f)

**ブログ・情報サイト**
* [Chrome DevTools](https://developer.chrome.com/docs/devtools?hl=ja)
* [9to5Google](https://9to5google.com/)
* [Android Police](https://www.androidpolice.com/)
* [Android Authority](https://www.androidauthority.com/)
* [TestingCatalog | AI News & Rumours](https://www.testingcatalog.com/)
* [Kdroidwinの日記](https://kdroidwin.hatenablog.com/archive)
* [HelenTech](https://helentech.jp/) / [🌴 officeの杜 🥥](https://officeforest.org/wp/)
* [Chromium派生ブラウザ総合 まとめWiki](https://w.atwiki.jp/chromiumbased/pages/1.html)
* [スマホブラウザ@ウィキ](https://w.atwiki.jp/sumaho_browser/pages/1.html)
* 5ch 各種スレッド検索結果：[Chromebook](https://ff5ch.syoboi.jp/?q=Chromebook) / [Google Pixel](https://ff5ch.syoboi.jp/?q=Google+Pixel)
