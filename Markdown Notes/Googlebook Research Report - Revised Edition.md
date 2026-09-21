# Googlebook Research Report - Revised Edition

Googleが2026年5月に発表した「Googlebook」と、発表前に報道された開発コードネーム「Aluminium」を整理します。将来の端末選定や仕様比較で再確認できるよう、公式発表・報道・未確認事項を分けて残している調査記録です。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202609220801 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

> [!IMPORTANT]
> 2026年9月21日にGoogleがGooglebookの予約開始、Googlebook OSの主要仕様、初期5モデル、価格・発売地域を正式発表しました。一方、日本発売、APKサイドロード、Play Integrity、Linux環境の詳細構成など未確認事項も残っています。公式発表、報道、推測を引き続き区別してください。

## 要約

### ひと目で分かる現状

| 項目 | 現時点の整理 |
| :--- | :--- |
| **製品** | Googleが正式発表した新しいノートPCカテゴリ「Googlebook」 |
| **OS基盤** | Android technology stackを基盤に、ChromeOSのdesktop foundationsを組み合わせる |
| **Chrome** | desktop-class Chrome browser with extensions |
| **Androidアプリ** | Google PlayおよびAndroidアプリ・ゲームに対応 |
| **Linux** | pKVMで隔離されたフルLinuxターミナル環境を搭載 |
| **AI** | Gemini Intelligenceを中核に、Magic Pointer、Rambler、Create My Widgetなどを提供 |
| **初期メーカー** | Acer / ASUS / Dell / HP / Lenovo |
| **初期仕様** | Intel Core Ultra Series 3またはSnapdragon X Elite、16GB以上RAM、45 TOPS超NPU |
| **価格** | 899米ドルから |
| **発売** | 米国：2026年10月4日、6か国：10月5日 |
| **日本発売** | 2026年9月22日時点で未発表 |
| **旧コードネーム** | 「Aluminium」は報道上の開発コードネーム。正式製品名ではない |

### 要点

Googlebookは、Googleが2026年5月12日に正式発表し、2026年9月21日に予約開始と主要仕様を公開した新しいノートPCカテゴリです。GoogleはGooglebook OSについて、**Android technology stackを基盤とし、ChromeOSのdesktop foundationsを組み合わせた構成**と説明しています。Gemini Intelligenceを中核に据え、Androidスマートフォンとの連携を重視しています。初期ハードウェアパートナーは **Acer、ASUS、Dell、HP、Lenovo** で、米国では2026年10月4日、カナダ・英国・アイルランド・フランス・ドイツ・オーストラリアでは10月5日に発売予定です。価格は899米ドルからです。一方、日本発売、APKサイドロード、Play Integrity、Linux環境の詳細構成、既存Chromebookの移行対象などは未確認です。

「Aluminium」は求人情報などを根拠に報道されたAndroidベースPCプロジェクトのコードネームです。Googleの正式な製品発表では「Googlebook」を使用しており、「Aluminium OS」または「ALOS」を正式な製品名としていません。したがって、バックアップ目的でAluminiumに関する過去の報道・予測を残す場合も、Google公式の確定情報とは区別します。

## Kdroidwin氏による査読

2026年6月2日、Kdroidwin氏から旧「Aluminium OS（ALOS）調査レポート」に対する査読を受けました。査読では、大枠として「AndroidベースのPC向け新OS」という方向性は公開情報と整合する一方、**事実・リーク・予測が混在している**点が主な問題として指摘されています。

特に、旧レポートで断定していた「Android 17ベース」「NPUによるローカルAI処理」「大容量RAM必須化」は、査読時に確認された公式公開情報では確定事項ではないため、確定情報として扱わないことが推奨されました。また、AdGuardのフィルタ記法については、scriptlet・CSS・拡張CSSの区別を明確にし、`:has()`を一律に「重いから避ける」とする説明は最新の実装を踏まえて見直すべきとの指摘がありました。

本改訂版では、この査読結果を踏まえ、Google公式発表で確認できる内容と、報道・未確認事項を分離しています。Aluminiumに関する過去の予測はGooglebookの確定仕様とはみなさず、背景資料として扱います。

- [Kdroidwin氏による査読｜Aluminium OS（ALOS）調査レポート](https://gist.github.com/Red-Frame-X/bdb94de10653edf1d11bd341d2eb2118)

## 確認できる情報

Google公式発表で確認できる主な内容を、分野ごとに整理します。

| 分野 | 確認済みの内容 |
| :--- | :--- |
| **製品・OS** | GooglebookはGemini Intelligence向けに設計された新しいノートPCカテゴリ。Googlebook OSは **Android technology stack** を基盤とし、**ChromeOSのdesktop foundations** を組み合わせる。 |
| **Chrome** | **desktop-class Chrome browser with extensions** を提供。 |
| **Androidアプリ** | Google Playに対応し、Androidアプリやゲームを利用できる。QualcommはSnapdragon X Elite搭載Googlebookについて、**native Android applications and games** への対応を明記。 |
| **Linux** | フルLinuxターミナル環境を搭載し、Claude CodeやAntigravity CLIなどを実行可能。Linux環境は **Level 5 security-certified pKVM hypervisor** でOS本体から隔離される。 |
| **セキュリティ** | ChromeOSと同じセキュリティアーキテクチャを基礎とし、Google Titan hardware root of trust、Defense in Depth、オンデバイスマルウェア検出を採用。 |
| **更新** | 定期的なFeature Dropと最大10年間のアップデートに対応。 |
| **AI機能** | Magic Pointer、Rambler、Create My Widget、Gemini Live、Proactive Suggestions、Gemini Spark、Task Automationなど。 |
| **スマートフォン連携** | Continue On、Cast My Apps、Quick Accessを提供。公式サイトではこれらの連携機能について **Android 17以上** の対応端末を要件として示す。 |
| **ハードウェア** | Acer、ASUS、Dell、HP、Lenovoの5社から初期モデルを展開。Intel Core Ultra Series 3またはSnapdragon X Elite、45 TOPS超NPU、16GB以上RAMを搭載。 |
| **価格・発売** | 899米ドルから。米国では2026年10月4日、カナダ・英国・アイルランド・フランス・ドイツ・オーストラリアでは10月5日に発売予定。 |
| **特典** | すべてのGooglebookに12か月分のGoogle AI Proと5TBクラウドストレージが付属。 |

> [!NOTE]
> GoogleはOS内部の全レイヤー構成や、Android Framework・ChromeOS由来コンポーネントの境界を完全公開していません。公式発表の範囲を超えて「Aluminium OS搭載」や特定のAndroidバージョン、未公開の内部構造を確定事項として扱わないようにします。

### ChromeOSとの関係

GoogleはGooglebook OSを「ChromeOSそのもの」とは説明していません。2026年9月21日の公式発表では、Android technology stackを基盤にしながらChromeOSのdesktop foundationsを組み合わせるとしています。

そのため、現時点では次のように整理します。

- **Googlebook OS**：Android技術スタックを主要基盤とし、ChromeOS由来のデスクトップ基盤を組み合わせる新しいPC向けプラットフォーム。
- **ChromeOS**：引き続きChromebookで提供される別のOS。Googlebook発表時点でChromeOS終了の公式発表は確認されていない。

「Googlebook OSがChromeOSを即時置換する」「すべてのChromebookがGooglebookへ移行する」といった説明は、公式確認がないため行いません。

### Androidアプリ

Google Play対応とAndroidアプリ利用は公式確認済みです。Android Developersは、既存のAndroidアプリがGooglebookで動作すると案内しています。QualcommもSnapdragon X Elite搭載Googlebookについてnative Android applications and gamesへの対応を明記しています。

ChromebookのARCVMと異なり、GooglebookはAndroid technology stackをOS基盤にしています。ただし、GoogleはAndroidアプリ実行層の内部構造を完全公開していないため、「すべてのAndroidアプリが仮想化なしで直接実行される」といった実装レベルの断定は避けます。

現時点で未確認の事項：

| 項目 | 状態 |
| :--- | :--- |
| APKサイドロードの正式手順 | 未確認 |
| Developer Modeの要否 | 未確認 |
| ADBの標準利用方法 | 未確認 |
| Play IntegrityのGooglebook上での挙動 | 未確認 |
| すべてのAndroidアプリとの完全互換性 | 未確認 |

### Linux環境

2026年9月21日の正式発表で、Linux環境の存在と仮想化方式の主要部分が確認されました。

| 項目 | 確認済みの内容 |
| :--- | :--- |
| ターミナル | フルLinuxターミナル環境を搭載 |
| 開発ツール | Claude Code、Antigravity CLI、Git、一般的なLinux開発ツールを利用可能 |
| 隔離方式 | **pKVM** によりGooglebook OS本体から隔離 |
| pKVMの説明 | Googleは **Level 5 security-certified pKVM hypervisor** と説明 |

一方、次の詳細は未確認です。

| 未確認項目 | 状態 |
| :--- | :--- |
| Debianなど具体的なディストリビューション | 未確認 |
| `apt` の正式サポート範囲 | 未確認 |
| USB passthrough | 未確認 |
| Linux GUIアプリの完全な対応範囲 | 未確認 |
| GPUアクセラレーション方式 | 未確認 |
| VirtIO、Waylandなどの詳細構成 | 未確認 |

従来のChromeOS Crostiniはcrosvm、Termina VM、LXCコンテナなどを利用しますが、Googlebookは公開情報上pKVMを中心とする隔離Linux環境です。したがって、少なくとも仮想化基盤は従来Crostiniと同一とは扱いません。

### Chrome・Web・拡張機能

GoogleはGooglebookのChromeを **desktop-class Chrome browser with extensions** と明記しています。このため、Androidスマートフォン版Chromeと同じ構成ではありません。

| 区分 | 項目 | 状態 |
| :--- | :--- | :--- |
| 確認済み | デスクトップクラスのChrome | 確認済み |
| 確認済み | Chrome拡張機能対応 | 確認済み |
| 未確認 | Chrome Web Store上の全拡張機能との完全互換性 | 未確認 |
| 未確認 | Manifest V3 / Declarative Net RequestのGooglebook固有制約 | 未確認 |
| 未確認 | Native Messagingの対応範囲 | 未確認 |
| 未確認 | Enterprise Policyの全対応範囲 | 未確認 |
| 未確認 | Lacrosとの関係 | 未確認 |

### Androidスマートフォン連携

Googlebookでは従来ChromebookのPhone Hubとは別に、Android端末とのより深い連携機能が用意されています。

- **Continue On**：スマートフォンで開始した作業をGooglebookへ引き継ぐ。
- **Cast My Apps**：スマートフォン側のアプリをGooglebook上から利用する。Googlebookへそのアプリをインストールする仕組みとは区別する。
- **Quick Access**：スマートフォン内のファイルや写真へGooglebookからアクセスする。
- **Fast Pair等の周辺機器連携**：Googlebookの製品ページで案内されている。

Googlebook公式サイトでは対応端末についてAndroid 17以上を要件として示しています。Pixel限定とはされていませんが、端末ごとの互換性一覧は今後の確認が必要です。

### Gemini Intelligence

2026年9月21日時点でGoogleが案内している主なAI機能は次のとおりです。

| 機能 | 概要 | 処理場所・要件 |
| :--- | :--- | :--- |
| Magic Pointer | 画面上のテキスト・画像・文脈を理解してGemini操作を呼び出す | オンデバイスとクラウドの具体的分担は未公開 |
| Rambler | 自由な音声入力を整理し、文章・箇条書き等へ整形する | 詳細未公開 |
| Create My Widget | 自然言語からカスタムウィジェットを作成する | Gemini利用。詳細な処理分担は未公開 |
| Proactive Suggestions | 画面内容をもとに次の操作候補を提示する | 詳細未公開 |
| Gemini Live | 対話型Gemini機能 | Geminiサービスを利用 |
| Gemini Spark | 複雑な依頼をバックグラウンド処理する | 端末を閉じた状態でも処理できるため、少なくとも端末NPUのみで完結する機能ではない |
| Antigravity | AIエージェントを利用した開発環境 | Googlebookに搭載 |
| Task Automation | Geminiによるタスク自動化 | 詳細は機能ごとに確認が必要 |

初期GooglebookはIntel Core Ultra Series 3またはSnapdragon X Eliteと45 TOPS超のNPUを搭載し、GoogleはオンデバイスAI処理能力を強調しています。ただし、各Gemini機能がNPU・CPU・クラウドのどこでどの処理を行うかは完全公開されていません。

### セキュリティ

確認済みの主要項目：

- ChromeOSと同じセキュリティアーキテクチャを基礎とする。
- Google Titan hardware root of trust。
- Defense in Depth。
- オンデバイスマルウェア検出。
- Androidアプリのサンドボックス。
- pKVMによるLinux環境の隔離。
- 最大10年間のOS・セキュリティ更新。

Verified Bootについては安全な起動とハードウェアルートオブトラストの採用は確認できますが、ChromeOSのVerified Bootと内部実装まで完全同一であることを示すGooglebook向け技術資料は未確認です。

### 発売地域・日本

2026年9月21日に発表された初期発売地域は次のとおりです。

- 米国：2026年10月4日。
- カナダ、英国、アイルランド、フランス、ドイツ、オーストラリア：2026年10月5日。

**日本は初期発売地域に含まれていません。**

Google Japanは2026年5月にGooglebookを日本語で紹介していますが、2026年9月22日時点で日本発売日、日本価格、日本語キーボード仕様、日本向け型番、技適取得モデルは正式発表されていません。海外仕様をそのまま日本仕様として扱わないようにします。

## 未確認・未発表の事項

2026年9月21日の正式発表により、Linux環境、pKVM、CPU、最低RAM、価格、発売地域など従来未確認だった複数項目は確認済みとなりました。現在も未確認・未発表の主な事項は次のとおりです。

| 分野 | 未確認・未発表の内容 |
| :--- | :--- |
| **OS基盤** | Googlebook OSが使用するAndroidの具体的なバージョン番号、Androidアプリ実行層の詳細な内部構造 |
| **Androidアプリ** | APKサイドロードの正式手順、Developer Modeの要否、Play IntegrityのGooglebook上での挙動 |
| **Linux** | ディストリビューション、`apt`、USB passthrough、GPUアクセラレーションなどの詳細 |
| **Chrome** | Chrome Web Store上の全拡張機能との互換性、Manifest V3 / Declarative Net RequestのGooglebook固有仕様、Lacrosとの関係、Enterprise Policyの完全な対応範囲 |
| **移行** | 既存Chromebookへの移行またはバックポートの対象、ChromeOS製品全体の終了時期 |
| **Gemini** | 機能ごとの端末内処理、クラウド処理、データ保持条件 |
| **日本市場** | 日本発売日、日本価格、日本語キーボード、日本向け型番、技適取得モデル |

## 期待できる点とリスク

| 観点 | 期待できる点 | リスク・未解決点 |
| :--- | :--- | :--- |
| アプリ | Google PlayとネイティブAndroidアプリ対応が公式確認された | 大画面、キーボード、マウスへの最適化や個別アプリの互換性は確認が必要 |
| Chrome | desktop-class Chromeと拡張機能対応が公式確認された | Manifest V3/DNR、Native Messaging、Enterprise PolicyなどのGooglebook固有差異は未確認 |
| Linux | pKVMで隔離されたフルLinuxターミナル環境が公式確認された | ディストリビューション、apt、USB、GPU、GUIアプリの詳細は未確認 |
| AI | OS全体で文脈に応じた支援を利用でき、45 TOPS超NPU搭載モデルが用意される | 処理場所、送信データ、保持期間を機能ごとに確認する必要がある |
| 端末連携 | Continue On、Cast My Apps、Quick Accessが公式確認された | 対応端末、権限、企業管理の詳細は未発表部分がある |
| 移行 | AndroidとChromeOSで培われた技術を組み合わせた構成が公式確認された | 既存Chromebook・周辺機器・業務フローの移行対象は未確認 |

## 広告ブロックとプライバシー

発売前の段階で特定アプリの組み合わせを「最適構成」と断定することはできません。次の順序で判断します。

1. ブラウザがChrome拡張機能をどの範囲でサポートするか確認する。
2. AndroidのVPN API、プライベートDNS、HTTPS証明書、アプリ単位VPNの実装を確認する。
3. AdGuard for Android、personalDNSfilterなどがGooglebookを正式対応環境に含めるか確認する。
4. ブラウザ内フィルタとDNS・VPNフィルタを重ねる場合は、誤ブロック、二重処理、電池消費、ログの分散を実機で比較する。

AdGuardのフィルタ構文については、製品予測から切り離し、[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)を参照してください。

## 今後確認する項目

- 日本発売日、日本価格、日本語キーボード、日本向け型番、技適。
- APKサイドロード、ADB、Developer Mode、Play Integrity。
- Linux環境のディストリビューション、apt、USB、GPU、GUIアプリ。
- Chrome Web Store、Manifest V3、DNR、Native Messaging、Enterprise Policy、Lacros。
- Androidアプリ、Linuxツール、周辺機器の個別互換性。
- VPN、DNS、証明書、拡張機能に関する制約。
- Gemini機能ごとのオンデバイス処理、クラウド処理、プライバシー説明、管理者向け設定。
- ChromeOS / ChromiumOSの今後の開発方針と既存Chromebookへの影響。

## 情報源

### 公式

- [Googlebook: The laptop your Android phone has been waiting for](https://blog.google/products-and-platforms/devices/googlebook/pre-order-googlebook/)
- [Googlebook is raising the bar for premium laptops](https://blog.google/products-and-platforms/devices/googlebook/first-look-googlebook/)
- [Googlebook’s built-in intelligence reinvents the way you use your laptop](https://blog.google/products-and-platforms/devices/googlebook/googlebook-built-in-intelligence/)
- [Googlebook公式サイト](https://googlebook.google/)
- [Googlebook FAQ](https://googlebook.google/frequently-asked-questions/)
- [Android Developers: Googlebook](https://developer.android.com/googlebook)
- [Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)
- [The Android Show: I/O Edition 2026（Google Japan）](https://blog.google/intl/ja-jp/products/android-chrome-play/android-show-io-edition-2026/)
- [Google AI announcements from May 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/)
- [Qualcomm: Snapdragon X Series Powers Googlebook](https://www.qualcomm.com/news/releases/2026/09/snapdragon-x-series-powers-googlebook--the-first-laptops-designe)
- [Chromium: Add Googlebook to English dictionaries](https://chromium.googlesource.com/chromium/deps/hunspell_dictionaries/+/refs/heads/main)
- [Chromium: Googlebook dictionary update roll](https://chromium.googlesource.com/chromium/src/+/3260aa4a5a9886e6a18ffd0b061665b9a4f155b6)
- [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)

### 報道・背景資料

以下は公式製品仕様ではなく、発表前後のコードネームや移行予測を追うための背景資料として保存します。

- [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
- [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
