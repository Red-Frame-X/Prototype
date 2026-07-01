# Aluminium OS（ALOS）/ Googlebook 調査レポート 改訂版
2026年6月12日時点で判明しているAluminium OS（製品名：Googlebook）に関する情報

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-UserScript-Regex-Markdown](https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260701 |

この備忘録は CC0 ライセンスの下で提供します。（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

※ 記述内容は [Kdroidwin氏の査読と解説](https://gist.github.com/Red-Frame-X/bdb94de10653edf1d11bd341d2eb2118?permalink_comment_id=6179721#gistcomment-6179721) および最新の公開情報を反映していますが、一部推測やリーク情報を含むため、完全な正確性を保証するものではありません。

## 1. 基本概要

Aluminium OSは、Googleが次世代PC向けに開発していたOSの開発コードネームです。2026年5月12日に「Googlebook」として正式発表されました。公開されている一次情報（確定事項）と、リーク・推測情報を明確に区別して整理します。

**【公式発表に基づく確定事項】**
* **Googlebookの発表と名称**：2026年5月12日のGoogle I/Oにて、Aluminium OSを搭載したAIネイティブなノートPC「Googlebook」が発表されました（2026年秋発売予定）。
* **AndroidとChromeOSの融合**：AndroidのアプリエコシステムとChromeOSの軽快なWeb体験を結びつけたハイブリッドな設計となっています。
* **Gemini Intelligenceの中核化**：システム全体にGeminiが統合されています。カーソルを動かすだけで文脈に応じた提案を行う「マジックポインタ（Magic Pointer）」や、音声・テキスト指示で専用ダッシュボードを作る「カスタムウィジェットの作成（Create My Widget）」が実装されています。

**【リーク・推測に基づく事項】**
* **Android 17ベースの統合**：従来の仮想環境ではなく、ネイティブ動作の基盤として「Android 17」が採用されると噂されていますが、現時点の公式発表ではOSの正確なナンバリングベースは明言されていません。
* **ローカルAI処理（NPU）とハードウェア要件の高騰**：OEM各社（Acer、ASUS、Dell、HP、Lenovoなど）に対する厳格なハードウェア要件が確立されていることは事実ですが、「NPUによる完全なローカル処理」や「大容量RAMの絶対的な必須化」についての技術的な全容は、現段階では推測の域を出ない部分も含まれています。

## 2. メリットとデメリット

| <div align="center">項目</div> | <div align="center">詳細</div> |
| :--- | :--- |
| **メリット** | **強大なエコシステム**：Androidスマホと同じUI・アプリがシームレスに連携・ネイティブ動作し、スマホとPC間でタスクが途切れません。<br>**AIによる生産性向上**：OSレベルで統合されたGeminiが、ユーザーの意図を先読みし作業を大幅に効率化します。<br>**自由度と省電力**：Android由来のバッテリー効率と、アプリの幅広い選択肢が期待されます。 |
| **デメリット** | **デスクトップUXの未成熟な部分**：モバイルUIの引き伸ばし感や、従来のデスクトップOS（Windows/macOS）に最適化された本格的な業務用ソフトウェアが動作しない懸念が残ります。<br>**ハードウェア要件の高騰（推測）**：プレミアムなAI体験を提供するため、システム全体のAI処理環境として大容量RAMとNPU等を要求され、端末価格が高額になる可能性があります。 |

## 3. コミュニティの反応（Reddit等）

海外の主要Techコミュニティ（r/Android, r/chromeosなど）では、期待と懸念が二分しています。

* **ポジティブな意見**：「Androidアーキテクチャのネイティブサポートにより、エミュレーションなしで動くのは素晴らしい」「これでアプリ開発者もデスクトップ（大画面）対応を余儀なくされ、エコシステム全体が底上げされる」
* **ネガティブな意見**：「UIデザインが散らかっているのではないか」「モバイルOSのPC市場参入は、過去の失敗を繰り返すのではないか」「全てのChromebookがアップデートできるわけではない点への不満」

## 4. ブラウジング環境とコンテンツブロックの最適化構成

**Chrome拡張機能 `AdGuard Browser Extension MV3` と Androidアプリ `personalDNSfilter` の併用**

OSのAndroidベース化に伴い、システム全体のトラフィック・ドメインレベルの通信制御を軽量なAndroidアプリ `personalDNSfilter` に任せ、ブラウザ内の要素隠蔽や高度なスクリプト制御をChrome拡張機能 `AdGuard Browser Extension MV3`（以下 `MV3`）で行う併用構成が効果的です。これにより、ブラウザ側の負荷を大幅に削減できます。

この環境下において、AdGuardの公式仕様に基づいた正確な技術的要件（記法）は以下の通りです。

* **スクリプトレットの注入（MV3）**：ブラウザ上の高度な制御においては、`#%#//scriptlet(...)` を「scriptletルール」として適用します。
* **CSSによる要素隠蔽（MV3）**：要素隠蔽は可能な限りシンプルな標準CSS構文 `##` で記述します。高度な制御が必要な場合は、`#$#` を「CSSルール」として記述します。
* **拡張CSSルール（MV3）**：標準CSSで対応できない複雑な要素には、`#?#` または `#$?#(...)` を「拡張CSSルール」として使用します。
* **擬似クラスの最適化（MV3）**：
  * テキストベースの要素隠蔽には、拡張CSSの擬似クラスとしてサポートされている `:contains(...)` を活用します。
  * 状態を表す `:has(...)` については、最新のAdGuardでは**ブラウザのネイティブ実装が利用可能な環境（モダンブラウザ等）ではそちらに処理を寄せて負荷を下げる方針**となっています。そのため、一律に避けるのではなく、環境に応じて適切に活用することが推奨されます。

## 5. プライバシーとカスタマイズ性

* **メリット**：Androidベースであるため、Morphe等のカスタマイズアプリの運用やAPKサイドロードの恩恵を受けやすい環境になると期待されます。
* **懸念点**：OSレベルでのAI（Gemini）常時稼働とインターネット連携（検索、Gmail、カレンダー等）によるデータ収集（テレメトリ）リスクがあります。データ送信を最小限に抑え、NPUによる「完全ローカル処理」がどこまで徹底・選択可能であるかが、プライバシー保護の最大の焦点となります。

## 6. 情報ソース

* 国内Techメディア
    * [GIGAZINE: Gemini向けノートPC「Googlebook」の登場によってChromebookはどうなるのか？](https://gigazine.net/news/20260514-googlebooks-premium-focus/)
    * [ケータイ Watch: グーグル、新たなノートパソコン「Googlebook」発表](https://k-tai.watch.impress.co.jp/docs/news/2106890.html)
* Wikipedia
    * [Aluminium OS](https://en.wikipedia.org/wiki/Aluminium_OS)
* Reddit
    * [r/chromeos](https://www.reddit.com/r/chromeos/)
    * [r/AluminiumOS](https://www.reddit.com/r/AluminiumOS/)
    * [r/Android](https://www.reddit.com/r/Android/)
* 9to5google
    * [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
* Android Authority    
    * [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
* AdGuard
   * [AdGuard Browser Extension v5.3: A stronger core, a smoother experience](https://adguard.com/en/blog/adguard-browser-extension-v5-3.html)
