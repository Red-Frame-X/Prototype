# Aluminium OS（ALOS）調査レポート 改訂版
2026年5月31日時点で判明しているAluminium OS（ALOS）に関する情報。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260603 |

この備忘録は CC0 ライセンスの下で提供します（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

※ 以下の記述は生成AIが調査し作成したものであり、正確性を保証するものではありません。

## 1. 基本概要

Aluminium OSは、Googleが次世代PC向けに開発中とされるOSです。公開されている一次情報とリーク情報を区別して整理します [Kdroidwin氏の査読と解説]。

**【公式発表に基づく確定事項】**
* **AndroidベースとAI中核設計**：2025年末のGoogleの求人情報にて、「Android-based」「AI at the core」の新OSとして示されています [Kdroidwin氏の査読と解説]。
* **ChromeOSとの共存**：当面の間はChromeOSと共存する方針です [Kdroidwin氏の査読と解説]。
* **Googlebookの発表**：2026年5月12日にGoogleから発表された「Googlebook」では、AndroidとChromeOSを結びつけたGemini中心のラップトップであることが説明されています [Kdroidwin氏の査読と解説]。

**【リーク・推測に基づく事項】**
* **Android 17ベースの統合**：従来の仮想環境ではなくAndroid 17がネイティブ動作し、スマートフォン等とシームレスな体験を提供すると噂されています [Kdroidwin氏の査読と解説]。
* **ローカルAI処理（NPU）とハードウェア要件**：クラウドに依存せずNPUを活用したローカル処理（翻訳、要約等）の実装や、それに伴う大容量RAMの必須化の可能性が高いと予測されていますが、確定事項ではありません [Kdroidwin氏の査読と解説]。

## 2. メリットとデメリット

| <div align="center">項目</div> | <div align="center">詳細</div> |
| :--- | :--- |
| **メリット** | **強大なエコシステム**：スマホと同じUI・アプリがネイティブ動作。<br>**プライバシーと速度（期待値）**：NPUによるローカル処理でデータ漏洩リスクを低減 [Kdroidwin氏の査読と解説]。<br>**自由度と省電力**：Android由来のバッテリー効率と、APKサイドロードの可能性。 |
| **デメリット** | **デスクトップUXの未成熟**：モバイルUIの引き伸ばし感、マウス・キーボード操作時の「もっさり感」。<br>**ハードウェア要件の高騰（推測）**：システム全体のAI処理・ネイティブAndroid環境のため、大容量RAMとNPUが必須化する可能性 [Kdroidwin氏の査読と解説]。<br>**既存PCソフトとの互換性**：Windows / macOS向けの本格的な業務用ソフトウェアが動作しない懸念。 |

## 3. コミュニティの反応（Reddit等）

海外の主要Techコミュニティ（r/Android, r/chromeosなど）では、期待と懸念が二分しています。

* **ポジティブな意見**：「[Samsung DeX](https://www.samsung.com/jp/apps/samsung-dex/)の究極進化系」「これでアプリ開発者もデスクトップ（大画面）対応を余儀なくされ、エコシステム全体が底上げされる」
* **ネガティブな意見**：「UIデザインが散らかっている（タスクバーの不統一など）」「モバイルOSのPC市場参入は、過去の失敗（Windowsのモバイル参入の逆）を繰り返すのではないか」

## 4. ブラウジング環境とコンテンツブロックの最適化構成

**Chrome拡張機能 `AdGuard Browser Extension MV3` と Androidアプリ `personalDNSfilter` の併用**

OSのAndroidベース化に伴う環境変化において、システム全体の通信制御をAndroidアプリ `personalDNSfilter` に任せ、ブラウザ内の要素隠蔽やスクリプト制御をChrome拡張機能 `AdGuard Browser Extension MV3` で行う併用構成を採用することで、高いパフォーマンスとフィルタリング精度を両立できます。

この併用環境下において、フィルタリングルールを効果的に機能させるための技術的要件は以下の通りです。

* **役割の分離とDNSブロック**：トラフィック・ドメインレベルのブロックは、軽量なシステムレベルDNSフィルタである `personalDNSfilter` に一任します。これにより、ブラウザ拡張機能側の処理負荷を大幅に削減できます。
* **スクリプトレットの注入（AdGuard拡張機能）**：ブラウザ上の高度な制御においては、`#%#//scriptlet(...)` を「scriptletルール」として記述して適用します [Kdroidwin氏の査読と解説]。
* **テキスト要素の非表示（AdGuard拡張機能）**：テキストベースの要素隠蔽では、拡張CSSの擬似クラスとしてサポートされている `:contains(...)` を採用します [Kdroidwin氏の査読と解説]。
* **CSSの最適化（AdGuard拡張機能）**：要素隠蔽は可能な限りシンプルな標準CSS構文（`##`）で記述します。AdGuard公式の仕様に基づき、高度な制御では `#$#`（CSSルール）や `#?# / #$?#`（拡張CSSルール）を使い分けます [Kdroidwin氏の査読と解説]。なお、`:has()` などの擬似クラスについては、最新のAdGuardではネイティブ実装が利用可能な環境ではそちらに寄せて処理負荷を下げる方針となっているため、一律に避けるのではなくブラウザの対応状況に応じて活用します [Kdroidwin氏の査読と解説]。

## 5. プライバシーとカスタマイズ性

* **メリット**：APKのサイドロードにより、Morphe等のカスタマイズアプリの運用が容易になる。
* **懸念点**：OSレベルでのAI（Gemini）常時稼働によるテレメトリ（データ収集）リスク。データ送信を最小限に抑え、NPUによる「完全ローカル処理」がどこまで徹底されるかが最大の焦点となる。

## 6. 情報ソース

* 関連ニュースメディア・公式情報
    * [DIME](https://dime.jp/)
    * [GIGAZINE](https://gigazine.net/)
    * [9to5Google: Google's Android PC, Aluminium OS](https://9to5google-com.translate.goog/2025/11/24/google-android-pc-aluminium-os/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp) [Kdroidwin氏の査読と解説]
    * [Android Authority: Will Aluminium OS avoid Android's early mistakes?](https://www-androidauthority-com.translate.goog/google-aluminium-os-avoid-android-early-mistakes-3663293/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp&_x_tr_hist=true) [Kdroidwin氏の査読と解説]
    * [AdGuard Blog: Browser Extension updates](https://adguard-com.translate.goog/en/blog/adguard-browser-extension-v5-3.html?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp) [Kdroidwin氏の査読と解説]
* 海外Redditコミュニティ
    * [r/Android](https://www.reddit.com/r/Android/)
    * [r/chromeos](https://www.reddit.com/r/chromeos/)
    * [r/windows](https://www.reddit.com/r/windows/)
    * [r/Design](https://www.reddit.com/r/Design/)
