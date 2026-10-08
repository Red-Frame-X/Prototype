# Googlebook Research Report - Revised Edition

Googleが2026年5月に発表した「Googlebook」と、発表前に報道された開発コードネーム「Aluminium」を整理します。将来の端末選定や仕様比較で再確認できるよう、公式発表・報道・未確認事項を分けて残している調査記録です。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202609300530 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

> [!IMPORTANT]
> 2026年9月21日にGoogleがGooglebookの予約開始、Googlebook OSの主要仕様、初期5モデル、価格・発売地域を正式発表しました。さらに9月23日、Chrome Enterprise and Education Helpで既存ChromebookのGooglebook OS移行方針を公開しました。一方、日本発売、Googlebook上のAPKサイドロードの具体的な操作手順、Play Integrity、Linux環境の詳細構成、Chromebookの具体的な移行対象モデルなど未確認事項も残っています。公式発表、報道、推測を引き続き区別してください。

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
| **日本発売** | 2026年10月8日の調査でも日本発売・日本価格・日本向けSKUを確認できず |
| **既存Chromebook** | ChromeOSの自動更新期限まではサポート継続。2034年を超えて10年サポートが続く対象機種はGooglebook OSへの移行支援対象となり、多くの新しい商用Chromebookに直接移行パスを用意する方針。具体的な対象モデル・移行方法は未発表 |
| **旧コードネーム** | 「Aluminium」は報道上の開発コードネーム。正式製品名ではない |

### 要点

Googlebookは、Googleが2026年5月12日に正式発表し、2026年9月21日に予約開始と主要仕様を公開した新しいノートPCカテゴリです。GoogleはGooglebook OSについて、**Android technology stackを基盤とし、ChromeOSのdesktop foundationsを組み合わせた構成**と説明しています。Gemini Intelligenceを中核に据え、Androidスマートフォンとの連携を重視しています。初期ハードウェアパートナーは **Acer、ASUS、Dell、HP、Lenovo** で、米国では2026年10月4日、カナダ・英国・アイルランド・フランス・ドイツ・オーストラリアでは10月5日を初期発売日として発表しました。2026年10月8日時点でGoogle公式ショップに購入案内が掲載されていますが、個別モデル・地域の在庫と出荷状況はメーカー販売ページで確認する必要があります。[Google公式ショップ](https://googlebook.google/shop/) 価格は899米ドルからです。Googleは2026年9月23日、現行Chromebookを各機種の自動更新期限までサポートし、現在購入される対象機種のうち10年のサポート期間が2034年を超えるものについてGooglebook OSへの移行を支援すると説明しました。また、多くの新しい商用ChromebookがGooglebook OSへアップグレード可能になるとしています。ただし、具体的な対象モデルと移行方法は未発表です。一方、日本発売、Googlebook上のAPKサイドロードの具体的な操作手順、Play Integrity、Linux環境の詳細構成なども未確認です。

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
| **価格・発売** | 899米ドルから。米国では2026年10月4日、カナダ・英国・アイルランド・フランス・ドイツ・オーストラリアでは10月5日を初期発売日として発表。2026年10月8日時点で公式ショップに購入案内を掲載。個別モデル・地域の在庫・出荷状況は別途確認。 |
| **特典** | すべてのGooglebookに12か月分のGoogle AI Proと5TBクラウドストレージが付属。 |

> [!NOTE]
> GoogleはOS内部の全レイヤー構成や、Android Framework・ChromeOS由来コンポーネントの境界を完全公開していません。公式発表の範囲を超えて「Aluminium OS搭載」や特定のAndroidバージョン、未公開の内部構造を確定事項として扱わないようにします。

### ChromeOSとの関係

GoogleはGooglebook OSを「ChromeOSそのもの」とは説明していません。2026年9月21日の公式発表では、Android technology stackを基盤にしながらChromeOSのdesktop foundationsを組み合わせるとしています。

そのため、現時点では次のように整理します。

- **Googlebook OS**：Android技術スタックを主要基盤とし、ChromeOS由来のデスクトップ基盤を組み合わせる新しいPC向けプラットフォーム。
- **ChromeOS**：引き続きChromebookで提供される別のOS。Googlebook発表時点でChromeOS終了の公式発表は確認されていない。

「Googlebook OSがChromeOSを即時置換する」「すべてのChromebookがGooglebookへ移行する」といった説明は、公式確認がないため行いません。

#### 既存ChromebookからGooglebook OSへの移行

Googleは2026年9月23日、Chrome Enterprise and Education Helpで既存Chromebookの移行方針を明確化しました。

| 項目 | Google公式の説明 |
| :--- | :--- |
| **現行Chromebookのサポート** | 各機種は自動更新ポリシーに定められたサポート期間中、ChromeOSの更新を継続して受ける。ChromeOSデバイスには2034年半ばまで定期アップデートとセキュリティパッチを提供する。 |
| **2034年を超える対象機種** | 現在購入される対象機種のうち、10年のサポート期間が2034年を超えるものについて、GoogleはGooglebook OSへの移行を支援すると説明。多くの機種に直接移行パスを用意する方針。 |
| **商用Chromebook** | 多くの新しい商用ChromebookモデルがGooglebook OSへアップグレード可能になる予定。 |
| **対象モデル一覧** | 未発表。Googleは対象機種と移行パスの詳細を後日公開するとしている。 |
| **既存の管理ライセンス** | ChromeOS Enterprise Upgrade / ChromeOS Education Upgradeは、既存Chromebookのライフサイクル中は引き続き有効。Googlebook OSへ移行した対象Chromebookは新しいライセンス体系で管理される。 |
| **Googlebookの組織管理** | 2026年発売モデルは個人向けで、ドメイン登録・集中管理には未対応。包括的な管理機能は2027年後半から段階的に提供予定。 |

ここでいう「2034年を超える」は、**自動更新期限が2034年より後なら無条件に移行対象になる、という確定したモデル一覧ではありません。** Googleの表現は「qualifying devices（対象となるデバイス）」であり、個別の移行可否は今後公開される対象機種情報で確認する必要があります。自動更新ポリシーには2035年・2036年まで更新対象となるChromebookがすでに掲載されていますが、AUEだけを根拠に個別モデルをGooglebook OS移行対応と断定しません。

また、GoogleはChromeOSの自動更新ポリシー自体を廃止しておらず、現在所有しているChromebookはプラットフォームがどちらで動作するかにかかわらず、各機種の10年間の自動更新コミットメントに基づくサポートを維持するとGooglebook FAQでも説明しています。

### Androidアプリ

Google Play対応とAndroidアプリ利用は公式確認済みです。Android Developersは、既存のAndroidアプリがGooglebookで動作すると案内しています。QualcommもSnapdragon X Elite搭載Googlebookについてnative Android applications and gamesへの対応を明記しています。

ChromebookのARCVMと異なり、GooglebookはAndroid technology stackをOS基盤にしています。ただし、GoogleはAndroidアプリ実行層の内部構造を完全公開していないため、「すべてのAndroidアプリが仮想化なしで直接実行される」といった実装レベルの断定は避けます。

2026年10月8日時点の確認状況：

| 項目 | 状態 |
| :--- | :--- |
| Googlebook上のAPKサイドロードの具体的な操作手順 | ADBによるインストール・実行・デバッグは公式確認済み。ファイルマネージャーからの導入など一般利用者向け手順は未確認 |
| GooglebookでAndroidの「Allow apps from unverified developers」Advanced flowを利用できるか | 未確認 |
| Developer options / Developer ModeのGooglebook固有UI・要否 | ADBではDeveloper optionsを使用することが公式確認済み。設定画面全体とChromeOSのDeveloper Modeに相当する機能は未確認 |
| ADBのGooglebook上での標準利用方法 | Wi-Fiは全モデル対応。USBはHP・XPSの左端子で対応、他3モデルは公式資料上coming soon |
| Play IntegrityのGooglebook上での挙動 | 未確認 |
| すべてのAndroidアプリとの完全互換性 | 未確認 |

#### CPUアーキテクチャとAndroidアプリのABI

2026年10月8日の調査では、Android一般の仕様、Googlebook固有の公式資料、Googleへの取材に基づく報道を分けて評価します。GooglebookはAndroid技術スタックを基盤とし、AndroidアプリがデスクトップクラスのChromeと並んで動作する環境ですが、内部の全レイヤー構成や特定のAndroidバージョンは未公開です。[Android Developers: Googlebook向け開発](https://developer.android.com/develop/adaptive-apps/guides/googlebook/overview)

Snapdragon X EliteはArm64系、Intel Core UltraはIntel 64 / x86-64系です。AndroidのネイティブABIである`arm64-v8a`と`x86_64`は別のABIであり、ARM64コードをIntel CPUがそのまま同じ命令として実行できるわけではありません。[Qualcomm公式Arm64開発資料](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-Dev-Kit-for-Windows-Product-Brief.pdf)、[Intel Core Ultra 5 325公式仕様](https://www.intel.com/content/www/us/en/products/sku/245720/intel-core-ultra-5-processor-325-12m-cache-up-to-4-50-ghz/specifications.html)、[Android NDK: ABI](https://developer.android.com/ndk/guides/abis)

| アプリの構成 | 互換性の確認ポイント |
| :--- | :--- |
| ライブラリ・SDKを含めJava/Kotlinのみ | ARM専用ネイティブライブラリへの依存はない。ただしAPI、画面、入力、配信条件は別途確認する |
| `arm64-v8a`と`x86_64`の両方を含む | 各CPUに合ったネイティブコードを利用できる構成。全機能の動作保証とは別 |
| `arm64-v8a`のみを含む | Intel側ではARM64変換対応が重要。Snapdragon側でもOS・API・配信条件等の確認が必要 |
| ARM32のみを含む | ARM64対応とは別問題。Snapdragon搭載だけを理由に動作すると判断しない |
| 本体はJava/KotlinだがSDKがネイティブコードを含む | ネイティブコードを含むアプリとして調査する |

Android DevelopersのJava/Kotlinのみという条件には、すべての依存ライブラリ・SDKも含まれます。Google Playの64ビット要件はすべての64ビットABIの搭載義務ではないため、ARM64対応アプリがx86-64版も含むとは限りません。[Android Developers: 64ビット対応](https://developer.android.com/google/play/requirements/64-bit)

**Android一般の一次情報**として、AOSPは異なるISA / ABIのネイティブコンポーネントを対応する変換実装で実行するNative Bridgeを説明しています。ただし、このインターフェースの存在だけではGooglebookが採用する変換実装を特定できません。[AOSP: Native Bridge](https://android.googlesource.com/platform/art/+/main/libnativebridge/README.md)

**Googlebook固有の二次情報**として、Android Authorityは2026年10月7日、Googleからの回答に基づき、Intel Googlebookが`arm64-v8a`を`x86_64`命令へ動的変換する64ビットのバイナリ変換レイヤーを利用すると報じています。Google公式サイトの技術文書とは区別し、Houdini、Berberis、Intel Bridge等との関係、実装名、対応命令、JIT等の制限は未確認とします。[Android Authority: Googleの追加説明](https://www.androidauthority.com/googlebooks-top-android-apps-intel-3719888/)

同記事はGoogleの説明として、利用頻度上位10,000以上のアプリの96.6%がIntel機で利用可能・正常動作すると伝えています。対象一覧・試験条件・版が公開されていないため、全Playアプリの対応率、残り3.4%のIntel固有非互換、Snapdragonの100%対応を示す数値とは扱いません。Googleの回答は残る配信除外の主因を大画面非対応やジャイロスコープ要求等としており、CPU以外の条件も含みます。

ChromeOS向けのAndroid Developers資料は、x86 ChromebookのARMコード変換による性能低下と電池消費増加を説明しています。これはGooglebookの新しい変換実装を測定した結果ではなく、Googlebookの低下率・安定性へ直接流用しません。[Android Developers: ChromeOS端末のアプリ対応](https://developer.android.com/develop/devices/chromeos/learn/device-support)

Google PlayはABIに加え、必要なハードウェア機能、API、画面条件、国・地域、開発者の配信設定等でフィルタリングします。Intel機で表示されない理由を直ちにARM依存と判断せず、インストール可能であることを全機能の保証ともみなしません。[Google Playのフィルター](https://developer.android.com/google/play/filters)

DRM・動画では認証と画質、ゲームではGPU・入力・センサー・アンチチート、エミュレータではJITとABI、VPN・セキュリティアプリでは権限・常時稼働・証明書・ネイティブSDKを個別に確認します。これらは確認項目であり、カテゴリ全体にIntel固有の不具合が確認されたという意味ではありません。カスタム入力方式とランチャーはGooglebookで非対応と公式説明されており、CPU選択では解消しないOS側の制約です。[入力方式・ランチャー互換性](https://developer.android.com/develop/adaptive-apps/guides/googlebook/keyboard-apps-and-launcher-compatibility)

#### ADBとDeveloper optionsの確認済み手順

Android Developersの2026年10月3日更新資料は、GooglebookへのADB接続とアプリのインストール・実行・デバッグを案内しています。全モデルでDeveloper optionsとWireless debuggingを有効化し、Wi-Fi経由で接続できます。外部ワークステーションだけでなく、Googlebook内のLinuxターミナルからのペアリングも案内されています。[ADB debugging on Googlebook](https://developer.android.com/develop/adaptive-apps/guides/googlebook/adb-debugging)

| モデル | 公式に案内されているADB接続 |
| :--- | :--- |
| HP Googlebook 14 / XPS Googlebook | Wi-Fi、USB（左端子のみ） |
| Acer Googlebook 14 / ASUS Googlebook 14 / Lenovo Googlebook 15 | Wi-Fi。USBは同資料上coming soon |

USB対応モデルではDeveloper optionsのUSB debuggingを有効化して対応端子へ接続します。これは開発用ADBの確認済み手順であり、一般利用者向けAPK導入、Advanced flow、developer verificationとの関係まで確定するものではありません。

#### APKサイドロードとAndroid developer verification

2026年9月24日時点で、**GooglebookでもAPKサイドロードが可能になる可能性を示す二次情報はありますが、Google公式のGooglebook向け資料では具体的なサイドロード手順を確認できていません。** ここではGoogle公式のAndroid developer verification資料と、GoogleがArs Technicaへ説明したGooglebook固有情報を分けて整理します。

| 区分 | 確認できた内容 |
| :--- | :--- |
| **Googlebook固有情報（二次情報）** | Ars Technicaは、Googleへの確認に基づく説明として、GooglebookでもAndroidスマートフォンと同様のdeveloper verification要件を適用し、ダウンロードしたAPKについて開発者の本人確認・アプリ登録を求める仕組みになると報じている。Googlebook固有の実装については、Google公式資料または実機で確認できるまで二次情報として扱う。 |
| **Android公式仕様** | Googleは、verified developerが登録したアプリについて、Google Play外からの直接配布・サイドロードを引き続き認めると明記している。 |
| **未認証アプリ** | certified Android deviceでは、未認証開発者のアプリも、ユーザーがDeveloper optionsから一度限りのAdvanced flowを完了すればインストール可能。Google公式Android Helpでは24時間のsecurity delay後、7日間または無期限で許可できるとしている。 |
| **ADB** | Android Developer Console Helpは、開発者・power userがADBを使ってmodified / unverified appsを自分の端末へインストールできると明記している。 |
| **適用範囲** | developer verificationはcertified Android devices向け。2026年9月30日にブラジル、インドネシア、シンガポール、タイの対象ストアから段階導入し、2027年に全世界・全インストール元へ拡大予定。 |

このため、**「開発者認証要件を満たしたAPKならGooglebookでもサイドロードできる可能性がある」という見方には一定の根拠がありますが、Googlebook固有の公式仕様として確定したとは扱いません。** Ars Technicaの記事は、Googlebookで「ダウンロードしたAPK」をインストールする場合にdeveloper verificationが適用されるとGoogleが確認した、と報じています。またGoogle公式Android資料では、developer verificationはサイドロード自体を廃止する制度ではなく、verified developerが登録したAPKはGoogle Play外でも配布・インストール可能とされています。

ただし、次の点は分けて考える必要があります。

- **確認済み**：Androidのdeveloper verification制度は、認証済み開発者が登録したアプリのサイドロードを許容する。
- **Googlebookについて二次情報で確認**：Ars Technicaは、Googleへの確認に基づく説明として、Googlebookでも同様のdeveloper verification要件を適用すると報じている。Google公式資料または実機で確認できるまでは、Googlebook固有の実装を確定事項として扱わない。
- **合理的な推測**：GooglebookがこのAndroid標準制度をそのまま採用するなら、認証・登録済みAPKは通常のサイドロード対象になり、未認証APKもAdvanced flowまたはADB経由で導入できる可能性がある。
- **未確認**：Googlebookの設定画面にAndroidスマートフォンと同じ「Allow apps from unverified developers」が存在するか、24時間待機を含むAdvanced flowがそのまま提供されるか、APKをファイルマネージャーから直接開けるか、ADBによる導入にdeveloper verificationの例外・制限がどのように適用されるか、Googlebook独自の追加制限があるか。ADBの有効化・接続方法自体は上記のADB公式資料で確認済み。

したがって現段階では、**「Googlebookはサイドロード不可」と断定する根拠は確認できません。一方で、ADBによる開発用インストールは上記のGooglebook向けADB資料で確認できるものの、認証済みAPKを一般利用者がファイルマネージャー等から導入する具体的手順は未確認です。** ただし、Androidスマートフォン向けAdvanced flowの手順をGooglebookの確定手順として流用してはいけません。Googlebook公式ヘルプと実機で、Advanced flowや一般利用者向けAPK導入、ADBとdeveloper verificationの関係を引き続き確認する必要があります。

> [!NOTE]
> Ars TechnicaのGooglebook固有のdeveloper verification説明は二次情報です。Google公式Android資料で確認できる一般仕様とは区別し、Googlebookでの具体的な実装・操作手順は公式資料または実機で確認できるまで未確認として扱います。

参考：

- [Android Developers Blog: Android developer verification: Building a safer ecosystem together](https://android-developers.googleblog.com/2026/06/android-developer-verification.html)
- [Android Help: Learn about Android developer verification](https://support.google.com/android/answer/17065026?hl=en)
- [Android Help: Allow app installs from unverified developers](https://support.google.com/android/answer/17588095?hl=en-GB)
- [Android Developer Console Help: Understanding Android developer verification](https://support.google.com/android-developer-console/answer/16561738?hl=en)
- [Android Developers: Register on Android Developer Console](https://developer.android.com/developer-verification/guides/android-developer-console)
- [Ars Technica: Googlebooks launch October 4 starting at $899—here are the five models you can preorder today](https://arstechnica.com/gadgets/2026/09/googlebook-laptops-launch-october-4-starting-at-899-preorders-for-five-models-live-today/)

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

GoogleはGooglebookのChromeを **desktop-class Chrome browser with extensions** と明記しています。通常のAndroidスマートフォン版Chromeとは提供機能に違いがありますが、実装基盤やWindows/macOS/Linux版との全機能の一致まで示すものではありません。

| 区分 | 項目 | 状態 |
| :--- | :--- | :--- |
| 確認済み | デスクトップクラスのChrome | 確認済み |
| 確認済み | Chrome拡張機能対応 | 確認済み |
| 未確認 | Chrome Web Store上の全拡張機能との完全互換性 | 未確認 |
| 未確認 | Manifest V3 / Declarative Net RequestのGooglebook固有制約 | 未確認 |
| 未確認 | Native Messagingの対応範囲 | 未確認 |
| 未確認 | Enterprise Policyの全対応範囲 | 未確認 |
| 未確認 | Lacrosとの関係 | 未確認 |

#### Chromeプロファイル・Googleアカウント・OSユーザー

| 概念 | 意味・確認状況 |
| :--- | :--- |
| Chromeプロファイル | ブラウザ情報を分ける単位。現状複数非対応というGoogle担当者の公開回答がある |
| Googleアカウント | アプリ・Webサービスへの認証情報。一つのOSユーザー内で複数利用できる |
| GooglebookのOSユーザー | 設定・ファイル等の利用空間。ログイン画面から切り替える複数ユーザー機能は公式確認済み |

Google公式ヘルプはユーザーとアカウントを区別し、同じユーザーで複数アカウントを利用できると説明しています。**複数アカウントへのログインは、Chromeの複数プロファイル対応を意味しません。** [ユーザーとアカウントの公式説明](https://support.google.com/chrome/answer/18206266?hl=en)

GoogleのAndroidコミュニティマネージャーを名乗るMishaal Rahman氏は、Googlebook OSのChromeが現状複数プロファイルに対応しないと公開回答しています。これは社員の公開回答という一次的証言で、正式な製品仕様書・ヘルプ記事とは区別します。Android AuthorityもASUS機でプロファイル切り替えがないことを確認しています。[担当者の公開回答](https://www.reddit.com/r/Googlebook/comments/1wxjzba/comment/pdug1vo/)、[実機確認の報道](https://www.androidauthority.com/googlebooks-chrome-multiple-profiles-3719566/)

Android版Chrome一般のヘルプには一つのプロファイルのみという説明がありますが、これだけでGooglebook固有仕様や内部実装を断定しません。デスクトップクラスのChrome・拡張機能対応も、Windows/macOS/Linux版との全機能一致を保証しません。[Chromeプロファイルの公式ヘルプ](https://support.google.com/chrome/answer/2364824?co=GENIE.Platform%3DAndroid&hl=en)

個人・仕事の分離についてGoogleは、別々のOSユーザーを作る方法と、同じユーザーに別アカウントを追加する方法を案内しています。バッジ付き仕事アプリを含むAndroidの独立した仕事用プロファイルは現状非対応です。[仕事・学校アカウントの公式案内](https://support.google.com/chrome/answer/18178630?hl=en)

ブラウザ情報を分離したい場合は、別々のOSユーザーと同期アカウントの利用を優先します。同一ユーザーへのアカウント追加だけを、ブックマーク・履歴・Cookie・パスワード・拡張機能・同期設定の分離とみなさないでください。同じ同期アカウントを使うと同期対象データが再び共有される点も考慮します。全項目の分離保証を列挙したGooglebook公式資料は未確認です。Beta / Canary併用の回避策は報道にありますが、公式の標準的な分離方法としては扱いません。

Chromebookも公式ヘルプでは端末ユーザーの追加・切り替えを案内しています。ChromeOSのOSユーザー切り替えを、Windows等の同一OSユーザー内のChromeプロファイル切り替えと同一視しないようにします。[Chromeの複数プロファイルとChromebookの案内](https://support.google.com/chrome/answer/2364824?hl=en)

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

Google Japanは2026年5月にGooglebookを日本語で紹介していますが、2026年9月23日時点で日本発売日、日本価格、日本語キーボード仕様、日本向け型番、技適取得モデルは正式発表されていません。海外仕様をそのまま日本仕様として扱わないようにします。

## 初期モデル・I/O・購入判断（2026年10月8日調査）

### 製品シリーズと構成

Google公式ショップ・比較表に掲載されているのは以下の5シリーズです。**Snapdragon X Elite搭載はXPS GooglebookとHP Googlebook 14の2シリーズ**で、今回追加のシリーズは確認できませんでした。「2機種」は製品シリーズ単位の数で、RAM・SSD・地域別のSKUが2つだけという意味ではありません。[Google公式比較表](https://googlebook.google/shop/compare/)

| メーカー・製品名 / 系列 | CPU・区分 | RAM / SSD | ディスプレイ | 電池・公称時間 | 重量 | 米国開始価格 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Acer Googlebook 14 / GP714-91N | Ultra 5 325 / Ultra 7 355・Intel | 基本16GB / 512GB、最大32GB / 512GB | 14型2880×1800 OLEDタッチ | 71Wh、Web最大16時間 / 動画14時間 | 1.14kg | $899 |
| ASUS Googlebook 14 / CX9406CAA | Ultra 5 325 / Ultra 7 355・Intel | 16 / 32GB、256 / 512GB等を仕様掲載 | 14型2880×1800 OLEDタッチ | 70Wh、Google比較表は最大16時間 | 約0.99kgから | $1,299 |
| Dell XPS Googlebook / DX13267 | X Elite X1E-80-100・Snapdragon | 米国掲載16GB / 512GB、32GB / 512GB、32GB / 1TB | 13.4型2560×1600 LCDタッチ、最大120Hz | 52Wh、Google比較表は最大18時間 | 約1.0kg | $999.99（Dell） |
| HP Googlebook 14 / 14c-cf系列 | X Elite X1E-80-100・Snapdragon | 個別本文で16GB / 512GB、16GB / 1TBを確認 | 14型2880×1800 OLEDタッチ、最大120Hz | 70Wh、Google比較表は最大19時間 | 約1.24kg | $1,299（Google掲載） |
| Lenovo Googlebook 15 | Ultra 5 325・Intel | 16 / 32GB、256 / 512GB | 15.3型2880×1800 OLEDタッチ、最大120Hz | 70Wh、メーカー12.5時間 / Google比較表13時間 | 1.29kgから | $1,099.99（メーカー） |

メーカー本文：[Acer公式仕様](https://news.acer.com/acer-debuts-first-googlebook-the-embodiment-of-premium-intelligence-powered-hardware)、[ASUS公式仕様](https://www.asus.com/laptops/for-home/googlebook/asus-googlebook-14/techspec/)、[Dell米国構成一覧](https://www.dell.com/en-us/shop/laptop-computers/spd/xps13dx13267)、[HP 512GBモデル](https://www.hp.com/us-en/shop/pdp/hp-googlebook-14c-cf0815nr)、[HP 1TBモデル](https://www.hp.com/us-en/shop/pdp/hp-googlebook-14c-cf0910nr)、[Lenovo公式仕様](https://news.lenovo.com/pressroom/press-releases/first-googlebook-premium-ai-experiences-sleek-lightweight-design/)

グローバル仕様の全構成が米国で選択可能とは限りません。ASUSの最大64GBという記載も実売SKUの確認とは分けます。HPの32GB構成は公式検索情報に存在しますが、個別本文で確認した構成と区別して再確認します。HPページ取得本文の価格には$0.00等の不整合があり、実売価格として採用していません。Googleの開始価格とメーカー販売価格は区別します。公称電池時間は試験条件付きで、実使用の順位付けには使いません。

日本発売・日本円公式価格・日本向けSKUは、5シリーズとも今回確認できませんでした。これは未発売を証明するものではありません。海外価格の円換算を日本公式価格として扱わず、地域別の販売・在庫・出荷情報を確認します。

### 内蔵端子とSnapdragonモデルの制約

以下はメーカーの端子一覧に基づきます。「記載なし」は、明示的な非搭載説明と区別します。

| モデル | USB-C | USB-A | Thunderbolt / USB4 | HDMI | 3.5mm音声 | SD / microSD | RJ45有線LAN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Acer | 3基 | 記載なし | TB4×1、他2基はUSB 3.2 Gen 2 | 記載なし | あり | 記載なし | 記載なし |
| ASUS | 2基 | 2基（USB 3.2 Gen 2） | TB4×2、USB4準拠 | 2.1 TMDS×1 | あり | 記載なし | 記載なし |
| XPS | 2基 | 記載なし | USB 3.2 Gen 2 / 10Gbps、TB・USB4対応の記載なし | 記載なし | 記載なし | カードリーダーなしと明記 | 記載なし |
| HP | 2基 | 記載なし | USB 10Gbps、TB・USB4対応の記載なし | 記載なし | ヘッドホン / マイクコンボあり | 記載なし | 記載なし |
| Lenovo | 2基 | 1基（USB 10Gbps） | TB4×2 | 2.0×1 | あり | 記載なし | 記載なし |

上記メーカー仕様に加え、[LenovoのPorts & Slots](https://www.lenovo.com/us/en/p/laptops/googlebook/googlebook-series/lenovo-googlebook-15/83w60009us)も確認しました。主要無線接続はWi-Fi 7、BluetoothはAcer・ASUS・Lenovoが6.0、Dell・HPが5.4と掲載されています。OS上の全機能対応とは区別します。

初期Snapdragon機はUSB-A・HDMIを搭載端子として掲載せず、USB-C中心です。ただし、**HPには音声端子があるため、両モデルを一括して「USB Type-Cのみ」と表現しません。** XPSはDisplayPort Alt ModeとPower Delivery、HPはDisplayPort 1.4とUSB PD 3.0を掲載しています。DellブログはXPSのDisplayPort 1.4を説明しています。[Dell公式I/O解説](https://www.dell.com/en-us/blog/everything-you-need-to-know-about-dell-s-xps-googlebook)

USB-Cという形状やSnapdragon X EliteというSoC名だけでUSB4 / Thunderbolt対応と判断しません。外部画面の最大台数・解像度、ドックの全機能対応は未確認です。USB-CハブでUSB-A・HDMI・カードリーダー・有線LANを追加できる構成はありますが、内蔵端子とは別で、OSのドライバー、USBモード、映像方式、給電の確認が必要です。

### Intelモデルを購入候補から除外すべきか

| 根拠の強さ | 評価 |
| :--- | :--- |
| 一次情報から明確に確認できる | ARM64とx86-64のABIは別。ネイティブライブラリと配信条件の確認が必要。ASUS・LenovoにはUSB-A・HDMI・TB4がある |
| 合理的に推測できるが断定できない | ARM64専用ネイティブコードへの依存が強い用途では、命令セット変換を避けられるSnapdragonを優先する合理性がある |
| 根拠不足で判断できない | Intel全機を除外すべき、Snapdragonは全アプリ対応、Intelは常に低速・不安定、特定アプリカテゴリ全体がIntel非対応という判断 |

**Androidアプリ互換性だけを理由にIntel搭載Googlebookを一律に除外することは推奨しません。** 必須アプリのABI・配信・主要機能を確認して選択します。ARM64専用コードへの依存が強く変換実行の不確実性を減らしたい場合はSnapdragonを優先できますが、全互換性は保証されません。USB-A・HDMIの直接接続とTB4を重視する場合はASUS・Lenovo等のIntel機に利点があります。AcerもIntel機ですがUSB-A・HDMIを掲載しておらず、I/OはCPUで一括評価しません。

Webアプリ中心ならAndroid ABIだけでIntelを除外する理由は乏しく、Chrome拡張機能もCPU名だけで優劣を断定できません。Native Messaging等は個別確認が必要です。Linux開発では使用するバイナリ・SDKのアーキテクチャが重要ですが、ゲストの構成・変換対応は未確認です。CPU / GPU性能はコア数・クロック・NPU TOPSだけで順位付けせず、同じOS・アプリ・条件での測定を待ちます。公称値ではSnapdragon機の電池時間が長いものの、実使用の優劣は未確認です。

| 購入前に確認する対象 | 主な確認項目 | Snapdragon / Intelの確認結果 |
| :--- | :--- | :--- |
| 必須Androidアプリ | Play配信、ABI、ログイン、主要機能、DRM等 | 個別に未確認。開発元の対応資料と実機で確認 |
| Linuxツール | arm64 / x86_64バイナリ、SDK、GPU・USB等 | 個別に未確認。配布元資料と実機で確認 |
| USB-Cドック・周辺機器 | 映像、給電、USB、LAN、Thunderbolt依存等 | 個別に未確認。メーカー対応表と実機で確認 |

## 未確認・未発表の事項

2026年9月21日の正式発表により、Linux環境、pKVM、CPU、最低RAM、価格、発売地域など従来未確認だった複数項目は確認済みとなりました。現在も未確認・未発表の主な事項は次のとおりです。

| 分野 | 未確認・未発表の内容 |
| :--- | :--- |
| **OS基盤** | Googlebook OSが使用するAndroidの具体的なバージョン番号、Androidアプリ実行層の詳細な内部構造 |
| **Androidアプリ** | ADBによる導入・接続方法とDeveloper optionsの使用は確認済み。一般利用者向けAPK導入、Advanced flow、developer verificationとADBの関係、Developer Mode、Play Integrity、Intelの変換実装名・制限・性能測定、CPU別の個別互換性は未確認 |
| **Linux** | ディストリビューション、`apt`、USB passthrough、GPUアクセラレーションなどの詳細 |
| **Chrome** | Chrome Web Store上の全拡張機能との互換性、Manifest V3 / Declarative Net RequestのGooglebook固有仕様、Lacrosとの関係、Enterprise Policyの完全な対応範囲 |
| **移行** | Googlebook OSへ移行できる具体的なChromebookモデル一覧、移行手順・時期、移行後の新ライセンス体系の詳細、ChromeOS製品全体の終了時期 |
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
| 移行 | 2034年を超えて10年サポートが続く対象機種への移行支援と、多くの新しい商用Chromebookのアップグレード方針が公式確認された | 個別の対象モデル、移行手順・時期、移行後ライセンスの詳細は未発表 |

## 広告ブロックとプライバシー

発売後もGooglebook固有の対応範囲と実機確認が揃うまでは、特定アプリの組み合わせを「最適構成」と断定することはできません。次の順序で判断します。

1. ブラウザがChrome拡張機能をどの範囲でサポートするか確認する。
2. AndroidのVPN API、プライベートDNS、HTTPS証明書、アプリ単位VPNの実装を確認する。
3. AdGuard for Android、personalDNSfilterなどがGooglebookを正式対応環境に含めるか確認する。
4. ブラウザ内フィルタとDNS・VPNフィルタを重ねる場合は、誤ブロック、二重処理、電池消費、ログの分散を実機で比較する。

AdGuardのフィルタ構文については、製品予測から切り離し、[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)を参照してください。

## 今後確認する項目

- 日本発売日、日本価格、日本語キーボード、日本向け型番、技適。
- 一般利用者向けAPK導入、Advanced flow、developer verificationとADBの関係、Developer Mode、Play Integrity。ADB接続方法とDeveloper optionsの使用は確認済み。
- Linux環境のディストリビューション、apt、USB、GPU、GUIアプリ。
- Chrome Web Store、Manifest V3、DNR、Native Messaging、Enterprise Policy、Lacros。Chrome複数プロファイルの正式ヘルプ・将来対応とOSユーザー間のデータ分離仕様。
- AndroidアプリのCPU別配信・主要機能、Intelの変換実装と性能、Linuxツールのアーキテクチャ、周辺機器・ドック・外部画面の個別互換性。
- VPN、DNS、証明書、拡張機能に関する制約。
- Gemini機能ごとのオンデバイス処理、クラウド処理、プライバシー説明、管理者向け設定。
- Googlebook OSへ移行できるChromebookの具体的な対象モデル、移行手順・時期、移行後のライセンス体系。
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
- [What the Googlebook announcement means for your ChromeOS devices](https://support.google.com/chrome/a/answer/16634428)
- [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)

### 担当者の公開回答

- [Mishaal Rahman氏のGooglebook Chromeプロファイルに関する回答](https://www.reddit.com/r/Googlebook/comments/1wxjzba/comment/pdug1vo/) — 社員の公開回答という一次的証言。正式な仕様書・ヘルプとは区別。

### 報道・背景資料

以下は公式製品仕様ではなく、発表前後のコードネームや移行予測を追うための背景資料として保存します。発売後の取材記事は上記各節で二次情報と明記し、公式仕様と区別しています。

- [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
- [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)

- [Android Authority: Intel Googlebookの変換・アプリ対応に関するGoogle回答](https://www.androidauthority.com/googlebooks-top-android-apps-intel-3719888/)
- [Android Authority: Googlebook Chromeの複数プロファイル実機確認](https://www.androidauthority.com/googlebooks-chrome-multiple-profiles-3719566/)
