# ChromeOS & Android Optimization Guide

ChromeOS & Android 最適化ガイド

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260910 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

> [!NOTE]
> この文書は個人の学習記録・設定バックアップ・実機検証メモを含みます。公式ドキュメントや一次情報で確認できない内容は、一般仕様ではなく個人の体験・観測・推測として扱います。製品やサービスへの評価は利用環境や時期によって変わるため、主観的な優劣ではなく、可能な限り機能・制約・確認できた事実を記述します。

## Subscription
サブスクリプションの料金、年額割引、払い戻し条件はサービスごとに異なり、変更されることがあります。契約前に各サービスの公式料金ページと解約・返金条件を確認します。

**利用中のサブスクリプション一覧**

サブスクリプションの購読基準は、「ITインフラになり得ているか」と「保守の負担比率が、対処 > 利用になった」という個人の判断基準です。

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
  * 2 TBの年額プラン契約中にPixel購入特典を適用した利用者が、契約期間の扱いに問題が生じたと報告している事例です。
  * これはユーザー報告であり、自分の環境と同一原因であることを示すものではありません。

**個人の問い合わせ記録**

Google Oneの問題が長期化した際、Google Oneヘルプやdocomoへ複数回問い合わせても解決まで時間を要した経験があります。これは個別事例であり、通常のサポート品質や全利用者の対応結果を示すものではありません。

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

### 検索・ブラウジング補助
* **[Buster: Captcha Solver for Humans](https://chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl)**：reCAPTCHAの音声チャレンジの解答を補助する。
* **[Cesturefy](https://chromewebstore.google.com/detail/cesturefy-navigate-operat/bifgfhokfobhebifcogneljkpaaloonp)**：マウス、ロッカー、ホイールジェスチャーでブラウザ操作を補助する。
* **[floccus bookmarks sync](https://chromewebstore.google.com/detail/floccus-bookmarks-sync/fnaicdffflnofjppbagibeoednhnbjhg)**：ブラウザのネイティブブックマークをGoogle Drive、WebDAV、Nextcloudなどを利用して複数のブラウザや端末間で同期する。
* **[google-search-title-qualified](https://chromewebstore.google.com/detail/google-search-title-quali/bjcnnhojddnonjmhlpdjcdcfmofliagb)**：Google検索結果のタイトル表示を補助する。
* **[Search Result Previews](https://chromewebstore.google.com/detail/search-result-previews/cedcejfiniojnlhlfhcppenochinijfo)**：検索結果のリンク横にWebサイトのプレビュー画像を表示する。
* **[Tabs to Front v2](https://chromewebstore.google.com/detail/tabs-to-front-v2/iiojfifkpjkhcdjfgekmfobhfdohlecg)**：新しいタブをフォアグラウンドで開く。
* **[VertiTab - 縦型タブ · AIブラウザエージェント](https://chromewebstore.google.com/detail/vertitab-vertical-tabs/chejfhdknideagdnddjpgamkchefjhoi)**：縦型タブ、ツリー型タブ、クラウド同期などのタブ管理機能を提供する。
* **[ブックマークサイドバー](https://chromewebstore.google.com/detail/%E3%83%96%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B5%E3%82%A4%E3%83%89%E3%83%90%E3%83%BC/jdbnofccmhefkmjbkkdkfiicjkgofkdh)**：ブラウザの端にブックマークサイドバーを追加する。

### 特定サイト向け拡張
* **[ChatGPT Ctrl + Enter Sender](https://chromewebstore.google.com/detail/chatgpt-ctrl+enter-sender/gbncgdhklmnckojlibfhdadpfbcdbnch?hl=ja)**：AIチャットでEnterを改行、Ctrl + Enterを送信に割り当てる。
* **[Google Chatの改行・送信キー設定](https://chromewebstore.google.com/detail/google-chat%E3%81%AE%E6%94%B9%E8%A1%8C%E3%83%BB%E9%80%81%E4%BF%A1%E3%82%AD%E3%83%BC%E8%A8%AD%E5%AE%9A/kabocfciobpmopkcbiphmgdljpdlighk)**：Google Chatのキー設定をカスタマイズする。
* **[GitHub UI Translator](https://chromewebstore.google.com/detail/github-ui-translator/igdplojdbbpfbedgoaokfcagpkofmngk)**：GitHub Web UIのメニューや説明文などを日本語表示する。
* **[5CH STYLE FORMAT](https://chromewebstore.google.com/detail/5ch-style-format/aidnencnedgaflbgacmcbcokcpancdac?hl=ja)**：5chのスレッド表示整形、URL直リンク化、画像・レスのポップアップ表示などを提供する。
* **[Twitterᴾˡᵘˢ](https://greasyfork.org/ja/scripts/387969-twitter%E1%B4%BE%CB%A1%E1%B5%98%CB%A2)**：画像表示やスパム投稿関連の表示設定を拡張するUserScript。
* **[𝕏 Spam Highlighter](https://github.com/shapoco/x-spam-highlighter)**：Web版𝕏のフォロワー一覧でスパム疑いアカウントを視覚的に強調する。
* **[Shadowban Scanner for Twitter / X](https://chromewebstore.google.com/detail/shadowban-scanner-for-twi/enlganfikppbjhabhkkilafmkhifadjd)**：ツール独自の判定に基づき、𝕏アカウントや投稿の状態を確認する。（[ろぼいんブログ](https://roboin.io/)）

### 業務効率化
* **[Advanced Font Settings](https://chromewebstore.google.com/detail/advanced-font-settings/caclkomlalccbpcdllchkeecicepbmbm?hl=ja)**：Webサイトのフォント設定を変更する。
* **[Checker Plus for Gmail™](https://chromewebstore.google.com/detail/checker-plus-for-gmail/oeopbcgkkoapgobdbedcemjljbihmemj?hl=ja)**：Gmailの新着通知、閲覧、返信などを拡張機能から行う。
* **[DeepL翻訳](https://chromewebstore.google.com/detail/deepl%EF%BC%9Aai%E7%BF%BB%E8%A8%B3%E3%81%A8%E6%96%87%E7%AB%A0%E4%BD%9C%E6%88%90%E3%83%84%E3%83%BC%E3%83%AB/cofdbpoegempjloogbagkncekinflcnj?hl=ja)**：翻訳と文章校正機能を提供する。
* **[Extensity](https://chromewebstore.google.com/detail/extensity/jjmflmamggggndanpgfnpelongoepncg?hl=ja)**：拡張機能の有効・無効を切り替える管理ツール。
* **[Google Keep Chrome 拡張機能](https://chromewebstore.google.com/detail/google-keep-chrome-%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD/lpcaedmchfhocbbapmcbpinfpgnhiddi?hl=ja)**：閲覧中のページやテキスト、画像をGoogle Keepへ保存する。
* **[Google オフライン ドキュメント](https://chromewebstore.google.com/detail/google-%E3%82%AA%E3%83%95%E3%83%A9%E3%82%A4%E3%83%B3-%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88/ghbmnnjooekpmoecnnnilnnbdlolhkhi)**：Googleドキュメント等のオフライン利用を補助する。
* **[PhotoShow](https://chromewebstore.google.com/detail/photoshow/mgpdnhlllbpncjpgokgfogidhoegebod)**：画像やURLにカーソルを合わせて拡大表示する。
* **[Sidely - ChatGPT Sidebar](https://chromewebstore.google.com/detail/sidely-chatgpt-sidebar/ibgipmeolfponfpmjhflfgkbcecpmcoo)**：ChatGPTをChromeのサイドパネルに表示する。
* **[Shortcuts for Google™](https://chromewebstore.google.com/detail/shortcuts-for-google/baohinapilmkigilbbbcccncoljkdpnd)**：Googleサービスへのショートカットをまとめる。
* **[Similarweb - Website Traffic, AI Traffic & SEO Checker](https://chromewebstore.google.com/detail/similarweb-website-traffi/hoklmmgfnpapgjgcpechhaamimifchmp)**：閲覧中サイトのトラフィック指標等を表示する。
* **[System Memory Usage](https://chromewebstore.google.com/detail/system-memory-usage/fdefaodljgbdlmdhobjlechpgpblooeh)**：システムのメモリ使用量をツールバーに表示する。
* **[ドキュメント、スプレッドシート、スライドで Office ファイルを編集](https://chromewebstore.google.com/detail/%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88%E3%80%81%E3%82%B9%E3%83%97%E3%83%AC%E3%83%83%E3%83%89%E3%82%B7%E3%83%BC%E3%83%88%E3%80%81%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%89%E3%81%A7-off/gbkeegbaiigmenfmjfclcdgdpimamgkj)**：Microsoft OfficeファイルをChrome上で開いて編集する機能を提供する。
* **[ドライブ用アプリケーション ランチャー（Google）](https://chromewebstore.google.com/detail/%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96%E7%94%A8%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3-%E3%83%A9%E3%83%B3%E3%83%81%E3%83%A3%E3%83%BC%EF%BC%88googl/lmjegmlicamnimmfhcmpkclmigmmcbeh)**：Google Drive上のファイルを対応アプリケーションで開くための連携機能を提供する。
* **[設定（Settings）](https://chromewebstore.google.com/detail/settings/jkfjnjeniglhpiggnfpiombpaohknkie)**：Google関連設定やChrome設定へのアクセスをまとめる。
* **[素晴らしい画面の並べ替えとスクリーンショット（Awesome Screenshot）](https://chromewebstore.google.com/detail/%E7%B4%A0%E6%99%B4%E3%82%89%E3%81%97%E3%81%84%E7%94%BB%E9%9D%A2%E3%81%AE%E4%B8%A6%E3%81%B9%E6%9B%BF%E3%81%88%E3%81%A8%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88/nlipoenfbbikpbjkfpfillcgkoblgpmj)**：画面録画、スクリーンショット、注釈追加機能を提供する。

### 特殊用途
* **[Chromebook リカバリ ユーティリティ](https://chromewebstore.google.com/detail/chromebook-%E3%83%AA%E3%82%AB%E3%83%90%E3%83%AA-%E3%83%A6%E3%83%BC%E3%83%86%E3%82%A3%E3%83%AA%E3%83%86%E3%82%A3/pocpnlppkickgojjlmhdmidojbmbodfm?hl=ja)**：Chromebookのリカバリメディアを作成するGoogle公式ツール。

**参考サイト**
* [Kami-Browser-Add-on｜Kdroidwin](https://github.com/Kdroidwin/Kami-Browser-Add-on)

---

## ChromeOS Chrome テーマ
* **[Chrome Web Store テーマ](https://chromewebstore.google.com/category/themes)**
* **[Dark Horizon](https://chromewebstore.google.com/detail/dark-horizon/ncjjeokpcnllmmbbipeaagmdpdpiadin)**：Chrome標準テーマに近い外観のダークテーマ。
* **[Royal Desert Sand](https://chromewebstore.google.com/detail/royal-desert-sand/nnieplejkjaodhemceganohmdkfekkem)**：暖色系の砂色と青系を組み合わせたChromeテーマ。

---

## ChromeOS Chrome アプリ
* **[Chrome アプリのサポート終了](https://support.google.com/chrome/a/answer/15950395?hl=ja)**

---

## ChromeOS Android アプリ
* **[Google Play アプリ](https://play.google.com/store/apps)**

* **[ChMate](https://play.google.com/store/apps/details?id=jp.co.airfront.android.a2chMate)** (*)
  * 説明：5ちゃんねる向けAndroidブラウザアプリ。（ChromeOSでの利用状況は後述）
* **[personalDNSfilter](https://play.google.com/store/apps/details?id=dnsfilter.android)** (*)
  * 説明：DNSレイヤーで広告・トラッキングドメインをブロックするAndroidアプリ。（詳細後述）
* **[Google Home](https://play.google.com/store/apps/details?id=com.google.android.apps.chromecast.app)**
  * 説明：対応するスマートホーム機器を管理する。
* **[Google フォト](https://play.google.com/store/apps/details?id=com.google.android.apps.photos)**
  * 説明：写真・動画のバックアップ、検索、編集等を提供する。

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

[GitHubプラグイン（OpenAI公式）](https://openai.com/business/plugins/github/) を追加すると、ChatGPTのChat・WorkおよびCodexから、許可したRepository、ファイル、commit、Issues、Pull Request、CIなどを参照・管理できます。利用可能な操作は、ChatGPTのプランと画面、GitHub Appに付与したRepository・権限、ワークスペース管理者の設定、操作時の承認によって異なります。

**Chat・Work・Codexの役割**

| 画面 | 適した用途 | 主な制約 |
| :--- | :--- | :--- |
| **Chat** | リポジトリやファイルの検索・説明、Issues・Pull Request・CIの確認、許可された管理操作 | GitHubプラグインが提供する操作と権限の範囲内 |
| **Work** | 複数の情報源やツールをまたぐ調査、長い査読、多段階タスク | 利用可能なツール・プラン・権限に依存 |
| **Codex** | リポジトリを作業環境で読み、複数ファイル編集、テスト・lint、PR作成など | 実行環境、sandbox、ネットワーク、GitHub権限、承認設定の制約を受ける |

ChatからのAPI操作でファイルを更新できることと、checkoutしたリポジトリでテストまで行えることは別です。コード変更の再現性と検証が重要な作業では、実際にテスト可能な環境を利用します。

**追加・接続手順**

1. ChatGPTの「Plugins」からGitHubプラグインを追加します。
2. GitHubで認証し、必要なリポジトリだけを許可します。
3. GitHubを利用できるChatまたはWorkで対象リポジトリ、Issues、Pull RequestのURLと作業範囲を指定します。
4. リポジトリが表示されない場合はGitHub Appの対象リポジトリと権限を確認します。
5. 書き込み操作が使えない場合はGitHub Appの権限、ワークスペースのAction controls、利用中の画面で提供される操作を確認します。

**リポジトリ管理に適した作業例**

* リポジトリ全体を査読し、重要度、根拠、修正案、影響範囲を整理する。
* IssuesとPull Requestを確認し、重複、再現手順不足、未解決レビュー、CI失敗を分類する。
* Issuesの作成・更新、コメント、ラベル、レビューなど、許可された管理操作を行う。
* 小規模なMarkdownや設定ファイルを更新する。
* 最近のcommit、マージ済みPull Request、workflow結果から更新履歴や作業報告を作成する。
* テストが必要なコード変更は、実行可能な作業環境でlint・テスト・生成処理まで確認する。

**推奨ワークフロー**

1. `README.md`、`AGENTS.md`、対象Issues、関連ファイルを読み、作業範囲と完了条件を固定します。
2. 現状調査、Issues整理、変更計画、リスク評価を行います。
3. 軽微な管理・文書更新はGitHub API操作で行い、複数ファイルの実装や検証はテスト可能な作業環境で行います。
4. 自動テスト、lint、生成処理を実行し、生成物を含む差分を確認します。
5. Pull Requestに要約、理由、影響、テスト結果、未検証事項、残るリスクを記載します。
6. 差分とCI結果を確認してからマージします。

**❗️セキュリティ・運用上の注意**

* GitHub Appには必要最小限のリポジトリと権限だけを付与します。
* APIキー、アクセストークン、Cookie、個人情報をリポジトリ、Issues、Pull Request、プロンプト、ログへ含めません。
* AIが作成した変更には誤修正、過剰変更、依存関係や生成物の見落としがあり得ます。
* Chatから書き込めても、テストを実行していなければ動作確認済みとは扱いません。

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
* [ChatGPTを使う（OpenAI公式）](https://learn.chatgpt.com/docs/use-chatgpt)
* [ChatGPTのパーソナライズ（OpenAI公式）](https://learn.chatgpt.com/docs/personalize)
* [ChatGPTのプロジェクト（OpenAI公式）](https://learn.chatgpt.com/docs/projects)
* [ChatGPTの画像生成（OpenAI公式）](https://learn.chatgpt.com/docs/image-generation)
* [ChatGPT Androidアプリ（Google Play）](https://play.google.com/store/apps/details?id=com.openai.chatgpt)
* [AdGuard for Android ローレベル設定ガイド（AdGuard公式）](https://adguard.com/kb/ja/adguard-for-android/features/low-level-settings/)

---

## Code Editor
**Visual Studio Code**
* **[Visual Studio Code: Workspace](https://vscode.dev/?vscode-lang=ja-jp)** / **[GitHub](https://github.com/microsoft/vscode)**
  * 説明：ブラウザから利用できるVisual Studio CodeのWeb版。

**Visual Studio Code 拡張機能**
* **[Virtual Gists for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-virtualgists)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualGists)**
  * 説明：VS Code上でGitHub Gistを管理・編集するための拡張機能。
* **[Virtual Git extension pack](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-virtualgit)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualGit)**
  * 説明：Virtual Git関連機能をまとめた拡張機能パック。
* **[Virtual Repositories for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CarloCardella.vscode-VirtualRepos)** / **[GitHub](https://github.com/carlocardella/vscode-VirtualRepos)**
  * 説明：リモートリポジトリをブラウザ版VS Code等から参照・編集するための拡張機能。

**Android アプリ**
* **[QuickEdit Pro](https://play.google.com/store/apps/details?id=com.rhmsoft.edit.pro)** / **[Help Center](https://rhmsoft.com/qedit/help.html)**

**QuickEdit ProからGitHubへ接続する場合の個人メモ**

PAT（classic）を使用する場合は、用途に必要な権限だけを付与します。`repo` や `gist` は広い権限を含むため、必要性を確認し、可能ならfine-grained tokenやGitHub Appなどより限定しやすい方式を検討します。

**Issues報告**
* [Visual Studio Code Issues](https://github.com/microsoft/vscode/issues)
* [Virtual Gists Issues](https://github.com/carlocardella/vscode-VirtualGists/issues)
* [Virtual Git Issues](https://github.com/carlocardella/vscode-VirtualGit/issues)
* [Virtual Repositories Issues](https://github.com/carlocardella/vscode-VirtualRepos/issues)
* [Japanese IME failure on VS Code 1.107.1 (Crostini) #285154](https://github.com/microsoft/vscode/issues/285154)

※ 現在はCrostini（Linux 開発環境）およびVSCodiumをデバイスから削除し、ブラウザとAndroidアプリベースの環境へ移行した、という個人の運用記録です。

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

▶ 生成AIの出力は検証が必要です。一般の利用者にも影響する広告・トラッカー・迷惑要素は、再現手順とスクリーンショットを添えて [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues) または [AdGuard reporting tool](https://reports.adguard.com/) へ報告する方法があります。報告前にリポジトリのIssuesテンプレートとポリシーを確認してください。

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

AdGuardルールで実現できない処理だけをUserScriptで補います。UserScriptはページ上でJavaScriptを実行するため、単純な要素非表示にはAdGuardルールを優先したほうが、権限、保守、性能、セキュリティの面で扱いやすくなる場合があります。

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

以下は個人の利用・比較メモです。性能評価や使い勝手は時期、モデル、料金プラン、用途によって変わります。

* **[ChatGPT](https://chatgpt.com/)**：汎用的な対話・調査・文章作成・コーディング等に利用。
* **[Gemini](https://gemini.google.com/)**：Googleの生成AIサービス。
* **[GitHub Copilot](https://github.com/features/copilot)**：主にソフトウェア開発支援に利用。
* **[Grok](https://grok.com/)**：xAIの生成AIサービス。
  * xAIアカウントのMFA紛失時にサポートへ問い合わせ、返信まで約5か月を要したという個人の対応記録があります。
  * 問い合わせ文を複数の生成AIで推敲したことがありますが、これは個人の体験であり、各サービスの一般的な回答品質を比較する根拠にはしません。
* **[SDXL](https://stability.ai/)**：画像生成モデル系統の一つ。
* **[z.ai](https://chat.z.ai/)**：GLM系モデルを提供するサービス。

**資料**
* [メインで使われている生成AIと統合開発環境（IDE）](https://mond.how/ja/topics/iozm87r4wyxx8ao/amp4bswp4hi8d0m)
* [5年後の主要な生成AIサービス（予測シェア）2026/05/24時点](https://mond.how/ja/topics/lahgbycmk0p72zr/1adfp0b6xmc4hps)

---

## Web サービス統合リスト

### AdGuard 関連サービス・サポート群
AdGuardドメイン（adguard.com系）で提供されている監査・ステータス・公式サポートをまとめています。
* [AdGuard 診断ページ](https://adguard.com/ja/test.html)
* [Webサイトをチェック (AdGuard)](https://reports.adguard.com/ja/welcome.html)
* [AdGuard Status](https://status.adguard.com/)
* [AdGuard > サポートセンター](https://adguard.com/ja/support.html)

### Google 関連サービス・管理群
Googleドメイン（google.com系）の検索・プライバシー管理、ステータス、各種ヘルプ・トラッカーをまとめています。
* [Google あなたに関する検索結果](https://myactivity.google.com/results-about-you)
* [Google ニュース提供元の優先度](https://www.google.com/preferences/source?hl=ja)
* [Google Workspace ステータス ダッシュボード](https://www.google.com/appsstatus/dashboard/#hl=ja&v=status)
* [Google Issue Tracker](https://issuetracker.google.com/home)
* [Google ヘルプ](https://support.google.com/?hl=ja)
* [Google Pixel ヘルプ](https://support.google.com/pixelphone/?hl=ja#topic=)
* [Chromebook ヘルプ](https://support.google.com/chromebook/?hl=ja#topic=)

### AI分析・診断ツール
* [AI性チェッカー](https://ai-tool.userlocal.jp/x_llm_match)
* [𝕏ポスト性格診断](https://ai-tool.userlocal.jp/x_shindan)

### 画像共有・データ削除管理
* [imgur Upload](https://imgur.com/upload)
* [Imgur Removal Request](https://imgur.com/removalrequest)
* [Redact](https://redact.dev/)

### ネットワーク環境・コンテンツブロック検証
これらのテストサイトは測定方法や判定基準が異なるため、単独のスコアを広告ブロッカー全体の性能や安全性の証明として扱いません。
* [確認君+（Plus）](https://env.b4iine.net/)
* [インターネット回線スピードテスト | USEN GATE 02](https://speedtest.gate02.ne.jp/)
* [Octane 2.0 plus](https://octane.webmarks.info/ja/)
* [AdBlock Tester](https://adblock-tester.com/)
* [Test Ad Block - Toolz](https://adblock.turtlecute.org/)
* [Norton Safe Web](https://safeweb.norton.com/)

### サービス稼働状況・障害検知
外部の障害報告サイトやSNS検索は補助情報として使い、可能な場合は公式ステータスページと照合します。
* [Downdetector](https://downdetector.jp/)
* [サイトはダウンしている？](https://www.websiteplanet.com/ja/webtools/down-or-not/)
* [Yahoo!リアルタイム検索](https://search.yahoo.co.jp/realtime/)
* [GitHub Status](https://www.githubstatus.com/)
* [5chサーバ稼働状況](https://www.kyodemo.net/sdemo/k/5_?hs=1)
* [偽 SPARROW AIM-7P Ver.1.00](https://5ch.ape.jp/SPARROW/)

### ファイル共有・メディア編集ユーティリティ
* [GigaFile便](https://gigafile.nu/)
* [Gofile](https://gofile.io/home)
* [123apps](https://123apps.com/ja/)
* [iLoveIMG](https://www.iloveimg.com/ja)
* [Fotoramio](https://fotoram.io/jp)
* [ezyZip](https://www.ezyzip.com/ja.html)
* [AddYoutube.com](https://addyoutube.com/)
* [YouTubeMP3もどき](https://receive.shamimomo.net/YouTubeMP3modoki/)

### テキスト作成・マークダウンエディタ
* [Dillinger](https://dillinger.io/)
* [Writebox](https://write-box.appspot.com/)
* [Writening](https://writening.net/)

### 統計・サポート・情報メディア・その他
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

以下は概念を大まかに区別するための比喩です。実際の情報セキュリティでは各概念は重なり合い、CIA（機密性・完全性・可用性）など、より具体的な要件で評価します。

* **セキュリティ（システムの防護）**

    鍵のかかった檻に手紙が入っている状態に例えられます。外部からの破壊や不正アクセスを防いでも、檻が透明なら内容の機密性までは保証されない、という違いを表します。

* **プライバシー（個人情報や行動情報の扱い）**

    手紙を中身の透けない封筒に入れる状態に例えられます。誰にどの情報を開示するかを制御する観点ですが、情報を保護するセキュリティ対策も必要です。

* **匿名性（行動と身元の結び付きにくさ）**

    差出人を明示しない手紙に例えられます。ただしIPアドレスやメタデータなど、複数情報の組み合わせによって再識別される可能性があります。

* **結論**

  セキュリティ、プライバシー、匿名性は関連しますが同一概念ではありません。高いセキュリティがあってもサービス側のデータ収集方針によってプライバシー水準は変わり、匿名化されていても再識別リスクが残る場合があります。

---

## 特殊詐欺対策
**[警察庁・SOS47特殊詐欺対策ページ](https://www.npa.go.jp/bureau/safetylife/sos47/)**

**成りすまし・その他の特殊詐欺**

警察官、自治体職員、金融機関、企業などを名乗る連絡で、個人情報・認証情報・金銭の提供を求められた場合は、相手が示した電話番号やリンクをそのまま信用せず、公式サイト等から正規の窓口を確認します。電話やLINEを使う正規の連絡も存在するため、連絡手段だけで詐欺と断定せず、内容と送信元を検証します。

**SNSの投資・ロマンス型詐欺**

SNS上の投資、副業、ロマンスをきっかけに金銭を要求する詐欺が報告されています。著名人の画像・音声・動画を生成AIで偽造する手口もあり得るため、外部メッセージアプリへの誘導、送金要求、本人確認情報の要求がある場合は特に注意します。

**[日本電話番号検索](https://www.jpnumber.com/)**

**注意が必要な電話番号・表示の例**
1. `+` で始まる国際番号 → 心当たりのない国際電話は折り返す前に発信元を確認します。`+81` は日本の国番号でもあるため、それ自体は不審性を示しません。
2. 末尾が `-0110` → 実在する警察署でも使われる番号体系があるため、番号表示だけで真偽を判断せず、警察の公式サイト等に掲載された番号へ掛け直して確認します。
3. `0120-` / `0800-` → 一般に着信側が料金を負担するフリーダイヤルですが、番号種別だけで安全性は判断できません。
4. `050-` → IP電話番号です。正規サービスにも利用されるため、番号種別のみで迷惑電話とは判断しません。
5. `0570-` → ナビダイヤル等で使われ、発信者側に通話料がかかる場合があります。
6. `0180-` → サービス内容と料金体系を確認してから利用します。

**フィッシング詐欺**

SMSやメールのリンクから認証情報を入力する前に、公式アプリやブックマークした正規サイトから同じ通知が確認できるか検証します。パスワードマネージャー、2段階認証、パスキーは被害軽減に役立つ場合がありますが、単独で全てのフィッシングを防げるわけではありません。

**悪質なECサイト**

銀行振込しか選べない、返品条件が不自然、運営者情報が不十分、相場から極端に安いなどは確認材料になりますが、いずれか一つだけで詐欺サイトと断定はしません。特定商取引法に基づく表示、連絡先、決済手段、ドメイン、外部の注意喚起などを複数確認します。

**SEOポイズニング**

SEOポイズニングは検索順位や広告表示等を悪用して不正サイトへ誘導する手法です。ログインや決済を伴うサービスは、検索結果の順位だけを信用せず、公式アプリや保存済みの正規URLからアクセスする方が誤誘導を減らせます。

コンテンツブロッカーは一部の悪質広告・既知の危険ドメインへのアクセス抑制に役立つ場合がありますが、特殊詐欺全般を防止する仕組みではありません。ブラウザやOSの保護機能、フィッシング対策、送信元確認などと組み合わせる多層防御の一要素として扱います。

**参考サイト**
* [詐欺サイト対策 Wiki*（Kdroidwin氏寄稿）](https://wikiwiki.jp/antiscamsite/)
* [おたくま経済新聞｜【特集】STOP！ネット詐欺！](https://otakuma.net/category/internet/internet-scam)
* [SEOポイズニングとは？仕組みや対策をわかりやすく解説](https://www.lanscope.jp/blogs/cyber_attack_cpdi_blog/20240530_20684/)

---

## AdGuard 公式フィルタ

**AdGuard filters**
* [組み込みフィルタリスト・標準フィルタリスト](https://adguard.com/kb/ja/general/ad-filtering/adguard-filters/)

[Yuki2718氏のよくある質問](https://github.com/Yuki2718/adblock2/wiki/よくある質問) も運用上の参考資料として参照しています。これはAdGuard公式文書ではないため、AdGuard構文や製品仕様はAdGuard公式ナレッジベースと実環境でも確認します。

**コンテンツブロックフィルタ**
* **[AdGuard 公式フィルタ](https://github.com/AdguardTeam/AdguardFilters)**：AdGuard公式が管理する各種フィルタ。
* **[Online Malicious URL Blocklist](https://gitlab.com/malware-filter/urlhaus-filter)**：悪性URL対策用リストの一つ。利用中の製品での収録状況はその時点のフィルタ一覧を確認します。
* **[uBlock Origin – Badware risks](https://github.com/uBlockOrigin/uAssets)**：uBlock OriginのuAssets内で管理されるセキュリティ関連フィルタ。

※ ChromeのDNR静的ルールは拡張機能ごとに保証枠があります。利用可能数はChromeのバージョンと他拡張機能の利用状況等によって変わるため、固定値だけで判断せず `getAvailableStaticRuleCount()` 等のAPI仕様を確認します。

**カスタムフィルタ・ユーザールール**
* **カスタムフィルタ**
  * **[AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)**
  * **[AdGuard module - not for independent use](https://github.com/Yuki2718/adblock2)**：上記フィルタに関連するAdGuard向けmodule。
  * **[自作のカスタムフィルタ](https://github.com/Red-Frame-X/Prototype)**：個人用に作成・保管しているルール。

**参考サイト**
* [Yuki2718/adblock2 > AdGuard Japanese filter Plus](https://github.com/Yuki2718/adblock2)

**DNSフィルタ**
* AdGuard for Android：DNS通信を保護 > DNSフィルタ > [AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter)

**例外ルール**
サイトやアプリの機能を阻害するブロックルールを解除する場合、適用範囲を確認したうえで例外ルール（`@@`）を使用します。

**AdGuardユーザールール作成ガイド**
* [なんJ AdGuard部 Wiki* > フィルタ構文](https://wikiwiki.jp/nanj-adguard/%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E6%A7%8B%E6%96%87)
* [AdGuard - 自分の広告フィルタを作成する方法](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
* [AdGuard - DNS filtering rules syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/)

**Issues報告**

AdGuardでの広告ブロック漏れ、Anti-Adblock、コンテンツブロックフィルタの誤ブロックなどは、AdGuardの報告ツールまたは該当するGitHub Issuesを利用します。報告先のテンプレートやポリシーは変更される可能性があるため、その時点の案内を確認します。

詳細な検証にはブラウザのデベロッパーツールが使えます。
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/overview?hl=ja)
* [MDN: ブラウザーの開発者ツール](https://developer.mozilla.org/ja/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)

**報告用Webサイト**
* [AdGuard Filters Issues reporting tool](https://reports.adguard.com/ja/new_issue.html)
* [報告方法ガイド](https://adguard.com/kb/ja/guides/report-website/)
* [AdGuard Filters Issues](https://github.com/AdguardTeam/AdguardFilters/issues)

報告時は、問題のURL、再現手順、スクリーンショット、使用製品とバージョン、使用フィルタ、必要に応じてフィルタリングログ等を整理します。公開ログやスクリーンショットには個人情報・認証情報が含まれていないか確認します。

---

## AdGuard ブラウザ拡張機能 MV3対応版
* **[Chrome Web Store](https://chromewebstore.google.com/detail/adguard-%E5%BA%83%E5%91%8A%E3%83%96%E3%83%AD%E3%83%83%E3%82%AB%E3%83%BC/bgnkhhnnamicmpeenaelnjfhikgbkllg)**
* **[HP](https://adguard.com/ja/adguard-browser-extension/overview.html)** / **[GitHub](https://github.com/AdguardTeam/AdguardBrowserExtension)**

AdGuard Browser Extension MV3では、ネットワークルールの多くがChromeのDeclarative Net Request（DNR）へ変換されます。カスタムフィルタや高度なルールでは、AdGuard構文として有効であることに加え、MV3環境で実装可能か確認します。

対応バージョンではポップアップまたはフィルタ画面の更新操作からカスタムフィルタの手動更新を確認できます。更新方式は組み込みフィルタとURL購読のCustom filtersで異なるため、[Content Blocking FAQ 2026.md](Content%20Blocking%20FAQ%202026.md) も参照します。

（Chromeの拡張機能管理画面の「更新」とカスタムフィルタの再取得は同じ操作ではありません。関連報告：[Issues #2944](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2944) / [Issues #3016](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3016)）

**カスタムフィルタで購読する場合の個人設定例**

`AdGuard module - not for independent use` の取り込み方法は配布元の現在の構成を確認します。サブリストとしてincludeされる場合、同じルールを別途重複購読しないようにします。

* AdGuard Japanese filter Plus
  ```
  https://yuki2718.github.io/adblock2/japanese/jpf-plus.txt
  ```
* AdGuard module - not for independent use
  ```
  https://yuki2718.github.io/adblock2/japanese/jpfp-ag.txt
  ```

**個人の運用方針**

カスタムフィルタを増やすほど、どのフィルタが原因かの切り分けは複雑になります。AdGuard Filtersへ問題を報告する際は、追加フィルタを一時的に無効化して公式推奨構成に近づけ、再現性を確認します。

**Filter Issues**
* [AdGuard Japanese filter Plus Issues](https://github.com/Yuki2718/adblock2/issues)

**開発者ツールと連動した手動ブロック機能**

利用可能なバージョンでは、開発者ツールと連動してルール作成を補助する機能があります（[画像](https://imgur.com/DcEH4K4)）。

**Chromeのアドレスバーからユーザールール画面を開く個人メモ**

拡張機能内部URLはバージョン変更で変わる可能性があります。現在の拡張機能ID・画面構成を確認したうえで利用します。

```text
chrome-extension://bgnkhhnnamicmpeenaelnjfhikgbkllg/pages/fullscreen-user-rules.html?theme=system
```

**参考サイト**
* [r/uBlockOrigin > solutions > youtube](https://www.reddit.com/r/uBlockOrigin/wiki/solutions/youtube/)
* [r/uBlockOrigin > solutions > twitter](https://www.reddit.com/r/uBlockOrigin/wiki/solutions/twitter/)
* [YouTube Fix & Customizations（Reddit）](https://www.reddit.com/r/youtube/comments/1b40hra/youtube_fix_customizations_4_videos_per_row/)
* [White area on Youtube（Reddit）](https://www.reddit.com/r/uBlockOrigin/comments/1l4r84i/white_area_on_youtube/)

uBlock Origin向けルールはAdGuardと構文・実装が異なる場合があります。参考にする場合は、そのまま転用せず対象製品での互換性を確認します。

**Web版YouTubeについての留意点**

YouTubeの広告配信・Anti-Adblock対策は頻繁に変化します。uBlock OriginやAdGuardの公式・公開リポジトリで現時点の対策を確認し、古いカスタムルールを重ねすぎないようにします。特定のフィルタ作者・開発者の役割や見解については、本人またはプロジェクトが公開した情報で確認できる範囲だけを記述します。

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

* **常駐対策**：personalDNSfilterをバッテリー最適化の対象から除外し、バックグラウンド動作を許可します。ローカルVPNモードでは、AndroidのVPN設定で「常時接続VPN」を利用できます。設定名・導線はOSや端末によって異なり、停止を完全に防ぐ保証はありません。
* **「VPNなしの接続をブロック」**：personalDNSfilterの公式FAQでは、DNSのみをVPN経由にする構成との組み合わせで通常通信が遮断される可能性が説明されています。使用前に現在のFAQを確認します。
* **DNSフィルタリングの迂回対策**：Androidの「プライベートDNS」やブラウザ独自の暗号化DNSを利用すると、personalDNSfilterの処理を迂回する場合があります。必要に応じて設定変更前後のログで確認します。
* **DNS通信の暗号化**：OS・ブラウザ側の暗号化DNSを無効にする場合は、personalDNSfilter側でDoHまたはDoTの上流DNSを設定できます。[公式製品説明](https://www.zenz-solutions.de/personaldnsfilter-wp/)で対応方式を確認します。
* **ChromeOS側の設定**：Android環境内で動作しているだけではChromeOS全体のDNSがpersonalDNSfilterを経由していると断定できません。ChromeOS側のDNSも対象にしたい場合は、アプリのログ等で実際の問い合わせ経路を確認します。

通知のサイレント化は通知音などを抑えるための任意設定で、VPNの安定化対策には含めません。

補足：端末やOSの表示によっては、「サイレント」に相当する選択肢や通知一覧の見出しが「マナー」と表示される場合があります。手元のPixel 10aでは、AdGuardの通知設定に「マナー（着信音もバイブレーションもOFFになります）」と表示されることを確認しています。これは個人の実機観測です。

ログのドメインを長押ししてブラック/ホワイトリストへ登録できる操作は、アプリのバージョンによってUIが変わる可能性があるため実機で確認します。

※ personalDNSfilterはDNS/hosts系のフィルタリングを主目的とし、ブラウザ拡張機能用のABPネットワーク構文すべてを解釈する製品ではありません。

**! 購読済みのDNSブロックリスト・hostsファイル**
* HaGeZi's Normal DNS Blocklist
  ```
  https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/wildcard/multi-onlydomains.txt
  ```

**参考サイト**
* [HaGeZi's DNS Blocklists](https://github.com/hagezi/dns-blocklists)
  * [gitlab.com/hagezi/mirror](https://gitlab.com/hagezi/mirror)
  * [codeberg.org/hagezi/mirror2](https://codeberg.org/hagezi/mirror2)
  * [hagezi-mirror.dnsbunker.org](https://hagezi-mirror.dnsbunker.org)

ミラーの更新頻度は運営側で変更される可能性があるため、各配布元の現在の説明を確認します。

---

## Android アプリ 有償版 AdGuard for Android（Android）
* **[HP](https://adguard.com/ja/adguard-android/overview.html)** / **[GitHub](https://github.com/AdguardTeam/AdguardForAndroid)**

**AdGuard for Android（ローカルVPNモード）の常駐・DNS設定**

**常駐・再起動対策**
* AdGuardのバックグラウンド動作を許可し、バッテリー最適化の対象から除外します。Pixelでの設定例：設定 > アプリ > AdGuard > アプリのバッテリー使用量 > バックグラウンドでの使用を許可 > 制限なし。設定名・導線はAndroidのバージョンや端末によって異なります。
* バックグラウンドで停止する場合は、AndroidのVPN設定でAdGuardの「常時接続VPN」を利用できます。[AdGuard公式のメーカー別対処手順](https://adguard.com/kb/adguard-for-android/solving-problems/background-work/)を確認します。
* **「VPNなしの接続をブロック」は別機能です**。有効化時の通信範囲・除外アプリへの影響をAndroid公式仕様で確認してから使用します。

**AdGuardのDNS保護を利用する場合**
* DNS処理をAdGuardに集約する場合、Androidの「プライベートDNS」が競合・迂回要因になることがあります（[公式互換性情報](https://adguard.com/kb/adguard-for-android/solving-problems/compatibility-issues/#private-dns)）。
* ブラウザの「セキュアDNSを使用」の無効化はDNS設定をAdGuardに集約する方法の一つですが、構成によっては必須ではありません。[Filter secure DNS](https://adguard.com/kb/adguard-for-android/features/low-level-settings/#filter-secure-dns) の現在の仕様を確認します。
* OS・ブラウザ側の暗号化DNSを無効にする場合は、AdGuardのDNS保護でDoH・DoTなどの暗号化DNSサーバーを設定できます（[公式：DNS保護](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)）。

**任意設定・不具合時の切り分け**
* 通知のサイレント化は通知音などを抑えるための任意設定で、VPN維持のための設定ではありません。
* 「接続の自動調整」は一律に無効化せず、接続切り替え時に再現する不具合がある場合だけ変更前後を比較します。
* VPNプロファイルの削除・再設定は常用手順にせず、停止が続く場合はメーカー別の常駐設定と[デバッグログ](https://adguard.com/kb/adguard-for-android/solving-problems/log/)で原因を調べます。

⚙ > 一般設定 > 詳細設定 > ローレベル設定 > その他の設定 - 「メイン画面にデベロッパーツールを表示する」をONにすると、対応バージョンではホーム画面から開発者向け項目へアクセスしやすくなります（[画像](https://imgur.com/UKGTVnZ)）。

**HTTPSフィルタリング**

HTTPS通信のURLパス、レスポンス内容、要素等に基づく高度なフィルタリングにはHTTPSフィルタリングが必要になる場合があります。AdGuardは端末内でTLS通信を検査するため、ユーザーCA証明書等の仕組みを利用します。対象アプリやAndroidバージョンによっては証明書を信頼しない通信もあります。

**CoreLibs**

AdGuard for AndroidのネットワークフィルタリングにはCoreLibsが使われます（[GitHub](https://github.com/AdguardTeam/CoreLibs)）。公開範囲はリポジトリやライセンス表示を確認します。フィルタリングルールやScriptletsには公開リポジトリがあります。

**HTTPSフィルタリング対象外Webサイト**

互換性や安全性上の理由でHTTPSフィルタリング対象外となるドメインが存在する場合があります（例：[Issues #6016](https://github.com/AdguardTeam/AdguardForAndroid/issues/6016)）。

**❗️留意点**

HTTPSフィルタリングではAdGuardが端末内でTLS通信を中継・検査するため、その実装と証明書管理を信頼する必要があります。OFFにするとHTTPS本文やURLパスに依存するフィルタリングは制限されますが、DNSや接続先ホストに基づくブロックなど別レイヤーの保護は利用できます（[公式：HTTPSフィルタリング](https://adguard.com/kb/general/https-filtering/what-is-https-filtering/)）。金融・決済系アプリ等は証明書ピンニングやセキュリティ要件により対象外となる場合があるため、アプリ単位の設定を確認します。

**ローカルVPNを使わず、ブラウザ内の機能・拡張機能で遮断する選択肢**
* [Brave](https://play.google.com/store/apps/details?id=com.brave.browser)
* [Cromite](https://github.com/uazo/cromite)
* [Elixir Browser](https://github.com/SF-FLAM/ElixirBrowser)
* [Firefox](https://play.google.com/store/apps/details?id=org.mozilla.firefox)：uBlock Origin等の対応拡張機能を利用可能（[uBO公式](https://github.com/gorhill/uBlock)）。

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

**個人の運用方針**
追加するカスタムフィルタを少数に絞ると、誤ブロック発生時の原因切り分けが容易になります。これは個人の保守方針であり、すべての利用者に必要な制限ではありません。

**Filter Issues**
* [AdGuard Japanese filter Plus Issues](https://github.com/Yuki2718/adblock2/issues)

**DNS通信を保護 > DNSフィルタ**

[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) はDNSレイヤーでドメイン単位のブロックを行います。プライバシー関連ドメインの遮断でアプリ機能に影響が出る場合は、原因となるドメインをログで確認し、必要最小限の例外を検討します。

個人の比較・検証対象：

① **[AdGuard DNS filter without privacy filters (Ads only)](https://github.com/kitadai31/AdGuardSDNSFilter_withoutPrivacyFilters)**

② **[AdGuard_DNS_Filter_for_myself](https://github.com/monsivamon/AdGuard_DNS_Filter_for_myself)**

③ **DNSユーザーフィルタ** で必要な例外ルール（`@@`）を作成。

**DNSサーバー & ChromeOS追加設定**

AdGuard内のDNSサーバーは目的に応じて選択します。Google Public DNSは選択肢の一つであり、プライバシー、フィルタリング機能、遅延、障害耐性などの要件によってCloudflare、Quad9、AdGuard DNS等も比較します。
ChromeOS側のネームサーバーを変更する場合は、その設定がAndroid VPN内のDNS処理とどう組み合わさるか実機で確認します（[Google Public DNS設定例](https://developers.google.com/speed/public-dns/docs/using?hl=ja#chromeos)）。

**トラブルシューティング**
* **Wi-Fi接続不良**：まず電波状態やAdGuard停止時の再現性を確認します。IPv6フィルタリングの変更は原因切り分けが必要な場合に限定し、改善しなければ元へ戻します。
* **フィルタ自動更新不可**：手動更新を行い、更新日時・バージョン・ログを確認します。繰り返す場合は自動更新設定やアプリ側のバックグラウンド制限も確認します。

**拡張機能・補助ツールの個人メモ**
* [tinyShield](https://github.com/FilteringDev/tinyShield/blob/main/README.ja.md)
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
* **HTTPSフィルタリング：** HTTPS通信を端末内で復号・検査し、必要に応じてフィルタリングして再暗号化する方式。より細かな制御が可能ですが、証明書・互換性・処理負荷を考慮します。
* **DNSフィルタリング：** 名前解決段階でドメイン単位にブロックする方式。ページ内要素単位や同一ドメイン内のURL単位の制御はできません。

---

## 【解決済み】Android System WebView 問題
**概要**

AdGuard for Androidの特定バージョンでWebView更新後に保護の再開へ影響する不具合が報告されていました。詳細な原因・対象バージョンは下記Issuesとリリースノートを基準に確認します。

**Android 17の「デバイスの管理」に関する実機記録（Pixel 10a）**

手元のPixel 10aでは、Android 17で `設定 > セキュリティとプライバシー > その他のセキュリティとプライバシー > デバイス管理 > AdGuard` に相当する項目を確認しました。この設定がAdGuardのバックグラウンド維持へどの程度寄与するかは、AndroidまたはAdGuardの公開資料だけでは一般化できないため、実機観測として記録します。

* この項目が表示される端末・OSビルドでのみ設定できます。
* バックグラウンド停止を完全に防ぐ保証はありません。
* 常時接続VPNやバッテリー最適化除外は、AdGuard公式のバックグラウンド動作ガイドも確認します（[AdGuard公式](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)）。

**過去に検討した対処・個人運用記録**

① 旧版へのダウングレードは、脆弱性修正や互換性改善を失う可能性があるため、現在は原則として第一選択にしません。特定バージョンでの回帰を切り分ける必要がある場合だけ、リリースノートとリスクを確認して検討します。

② ウォッチドッグ等の低レベル設定は対象バージョンの公式説明を確認し、必要な場合だけ変更します。

③ **MacroDroidを利用した保護再開タスクの個人設定例**

* **AdGuard側**: 設定 ⚙ > 一般設定 > 詳細設定 > 自動化をONにし「パスワード」を設定
* **MacroDroid側**: 「インテントを送信」
  * ターゲット：Broadcast
  * アクション：`start`
  * パッケージ：`com.adguard.android`
  * クラス：`com.adguard.android.receiver.AutomationReceiver`
  * エクストラ：`password` = 設定したパスワード
  * 必要に応じて `quiet` = `true`

④ **MacroDroidを利用した更新確認タスクの個人設定例**

* アクションを `update` とする以外は、AdGuard公式自動化インターフェースに沿って必要項目を設定します。
* `update` は利用可能なフィルタとアプリ更新を確認するアクションであり、保護再起動と同じ意味ではありません（[AdGuard公式：Android版の自動化](https://adguard.com/kb/adguard-for-android/solving-problems/tasker/)）。
* 現在の個人運用ではVPN状態変化を更新トリガーにせず、1日1回などの時刻トリガーで更新確認する方式を使います。
* 保護復帰を補助する場合は、`start` → `update` → 必要に応じて再度 `start` のように役割を分けて検証します。各アクションの間隔は端末で実測します。

**Issuesの時系列**
* [Issues #5598](https://github.com/AdguardTeam/AdguardForAndroid/issues/5598)
* [Issues #5593](https://github.com/AdguardTeam/AdguardForAndroid/issues/5593)
* [Issues #5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)
* [AdGuard for Android v4.10 Nightly](https://adguard.com/ja/versions/android/nightly.html)

**結論**

過去のWebView関連不具合は修正版が公開されています。一方、OSによるバックグラウンド制限は別問題なので、常時接続VPN、バッテリー設定、ログ、必要に応じた自動化を個別に切り分けます。

---

## AndroidのプライベートDNSを利用したDNSブロック

Androidの「プライベートDNS」にフィルタリングDNSサービスのホスト名を設定すると、DNSレイヤーでブロック対象ドメインの名前解決を抑止できます。結果として一部のアプリやWebサイトの広告・トラッカー通信を抑制できますが、YouTubeのようにコンテンツと広告が同一ドメインから配信される場合や、ページ内要素だけを消す用途には対応できません。

**設定手順の例**

1. **設定** を開く。
2. **ネットワークとインターネット** を選択する。
3. **プライベート DNS** を開く。
4. **「プライベートDNSプロバイダのホスト名」** を選択する。

**AdGuard DNSのホスト名例**

* `dns.adguard-dns.com`

旧ホスト名や他の提供方式は変更される可能性があるため、利用時点のAdGuard DNS公式ドキュメントで確認します。

**主な対象**
* ブラウザのDNS問い合わせ
* AndroidアプリのDNS問い合わせ

ただし、アプリ独自のDoH、VPN、直接IP接続などで迂回される場合があります。

---

## Android アプリ ReVanced・Morphe・URV（Android）
Androidアプリへパッチを適用して挙動を変更するプロジェクト群の個人メモです。各プロジェクトの正規配布元、利用規約、パッチ対象バージョンを確認し、ビルド済みAPKを第三者から取得する場合は配布元の信頼性に注意します。VirusTotalの検査結果だけで安全性を保証できるわけではありません。

**略称・ツール**
* **[ReVanced 公式](https://revanced.app/)** / [GitHub](https://github.com/revanced)
* **RVX**: inotia00氏によるReVanced Extended系プロジェクト。現在の開発状況は公式リポジトリで確認します。
* **[Morphe](https://morphe.software/)** / [GitHub](https://github.com/MorpheApp)
  * [Morphe Community Patches](https://morphe-patches.software/)
* **[URV](https://jmancentral.com/)** / [GitHub](https://github.com/Jman-Github)

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

改変クライアントやパッチの利用がサービス利用規約、サポート対象、アカウント状態へ与える影響はサービス側の現在の規約を確認します。Reddit等のアカウント停止報告は参考にはなりますが、利用だけで必ず停止されることを示すものではありません。

Premium加入者向けのパッチ設定についても、パッチ側のリリースノート・Issuesで現在の推奨設定を確認します。

**𝕏/Twitter ReVancedの使い方**

改変クライアントでログイン問題が報告される場合があります（例：[Issues #714](https://github.com/crimera/piko/issues/714)）。原因や現在の対応状況は対象プロジェクトのIssuesを確認します。
* [導入方法解説](https://pfbcoconut.com/2024/04/21/twitter-x-revanced/) / [ログイン方法更新](https://kdroidwin.hatenablog.com/entry/2025/11/04/210359)
* 関連プロジェクト：[crimera (Piko)](https://github.com/crimera/piko) / [monsivamon](https://github.com/monsivamon/twitter-apk) / [lluni](https://github.com/lluni/twitter-apk) / [Origin Twitter Neo](https://github.com/YuzuMikan404/Origin-Twitter-Neo)

**併用候補として記録しているAndroidアプリ**
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
* Homeやスレッドの右下︙ > 表示設定 >「リストをアニメーションする」をOFF、という個人設定例です。UIはバージョンで変わる可能性があります。

**レクタングル広告について**
* ChMate側と5ch側で異なる広告枠が存在する場合があります。広告非表示の条件やUPLIFTの現在の仕様は、[ChMate/運営側の案内](https://www.airfront.co.jp/pr20250116.html)を確認します。

**代替ブラウザ**
* [したらばStorm](https://play.google.com/store/apps/details?id=jp.everystorm.shitarabastorm) / [Channeler](https://play.google.com/store/apps/details?id=pro.hirooka.channeler)

**IOMate**
* [IOMate](https://github.com/kitadai31/IOMate)
  * 5ch.io対応前の旧ChMateで5ch.ioへの読み書きを補助するローカルプロキシとして記録しています。現在必要かどうかはChMateの現行版とIOMate側の説明を確認します。

ChromeOS上での動作は端末・ChromeOS・Androidランタイム等に依存します。（[動作環境](https://chmate.airfront.co.jp/docs/supported-os/#%e5%8b%95%e4%bd%9c%e7%92%b0%e5%a2%83%e3%81%ab%e3%81%a4%e3%81%84%e3%81%a6)）
* [Android アプリ ChMate 不具合修正済みメモ](https://writening.net/page?DW58re)

**参考サイト**
* [5chブラウザ「ChMate」質問スレ](https://ff5ch.syoboi.jp/?q=5ch%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%80%8CChMate%E3%80%8D%E8%B3%AA%E5%95%8F%E3%82%B9%E3%83%AC) / [5chどんぐり非公式まとめwiki](https://donguri.wikiru.jp/)

---

## Aluminium OS / Googlebook / Linux

この節は、Googleの公式発表と、報道・リーク・予測を分けて記録します。未発表の製品仕様や移行時期は確定情報として扱いません。より詳しい整理は [`Googlebook & Aluminium Survey Report - Revised Edition.md`](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md) を参照します。

* **Googlebook**：Googleが2026年5月に正式発表したPCカテゴリー。発売時期、構成、仕様の詳細はその時点の公式発表を確認します。
* **Aluminium OS / AndroidベースPC構想**：開発情報や報道で用いられてきた呼称・コードネームを含みます。ChromeOSからの移行方式や既存端末への適用範囲は、Googleが公表した内容と未確認情報を区別します。

「ChromeOSが2034年に終了する」「Aluminium OSが特定年に完全移行する」といった記述は、報道や予測だけを根拠に確定事項として扱いません。ChromeOS端末のサポート期間は各モデルの自動更新ポリシー（AUE）とGoogleの公式発表を確認します。

**ChromeOSの今後の動向を追うための資料**
* [Googlebook 正式発表後もChromebookは継続。Googleが改めて明言した10年サポートと移行方針](https://helentech.jp/news-chromebook-continues-after-googlebook-86132/)
* [Aluminium OSの完全リリースは2028年以降の可能性](https://helentech.jp/news-81647/)
* [ChromeOSは2034年に段階的廃止へ](https://internet.watch.impress.co.jp/docs/yajiuma/2083598.html)
* [Aluminium OSの展開。2026年後半リリース予定](https://helentech.jp/news-chromebook-82961/)

上記の第三者記事は動向把握用です。将来時期や未発表仕様は、Google公式発表があるまで予測・報道として扱います。

**Linux 関連**
* [ChromebookにLinuxをクリーンインストールする方法](https://zenn.dev/roistaff/articles/30ce3883b3b9d9)
* [Linux Mint 22をパソコンにインストールする方法](https://tanoike.com/install-linux-mint-on-pc)
* [Timeshift（バックアップツール）](https://github.com/linuxmint/timeshift) / [使い方](https://sub-log.jp/2022/12/14/linux-mint-%E3%81%A7-timeshift-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%90%E3%83%83%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E3%81%99%E3%82%8B/)
* [Linux Mint搭載 既製品ノートPC](https://raylink-inc.com/product/rl-bnc00010/)
* [AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/)

**ECサイト購入時の個人優先順位**
* Amazon.co.jp（セール時） > メーカー直売サイト > 楽天市場 = ヨドバシ.com

これは価格、ポイント、保証、返品条件等を考慮した個人の購入傾向であり、一般的な優劣を示すものではありません。

---

## Credits
* [5ch【広告除去】personalDNSfilter](https://ff5ch.syoboi.jp/?q=%E3%80%90%E5%BA%83%E5%91%8A%E9%99%A4%E5%8E%BB%E3%80%91personalDNSfilter)
* [r/Adguard](https://www.reddit.com/r/Adguard/) / [r/uBlockOrigin](https://www.reddit.com/r/uBlockOrigin/)
* [AdGuard ナレッジベース](https://adguard.com/kb/ja/) / [AdGuard（𝕏）](https://x.com/AdGuard) / [AdGuardJP（𝕏）](https://x.com/AdGuardJP) / [AdGuard ブログ](https://adguard.com/en/blog/)

**コンテンツブロックに関するアナウンス・参考**
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

---

## 参照

* [Chrome User Scripts API](https://developer.chrome.com/docs/extensions/reference/api/userScripts?hl=ja)
* [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)
* [AdGuard Browser Extension](https://github.com/AdguardTeam/AdguardBrowserExtension)
* [AdGuard for Android](https://github.com/AdguardTeam/AdguardForAndroid)
* [personalDNSfilter](https://github.com/IngoZenz/personaldnsfilter)

> [!NOTE]
> この文書に掲載しているアプリ、拡張機能、サービスは推奨や安全性保証を意味しません。最新の仕様、権限、プライバシーポリシー、対応OSを各配布元で確認してください。
