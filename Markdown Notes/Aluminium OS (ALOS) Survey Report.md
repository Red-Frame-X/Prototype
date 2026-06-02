# Aluminium OS（ALOS）調査レポート
2026年5月31日時点で判明しているAluminium OS（ALOS）に関する情報。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260531 |

この備忘録は CC0 ライセンスの下で提供します（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

記述内容は生成AIが調査し作成したものであり、正確性を保証するものではありません。

## 1. 基本概要

Aluminium OSは、Googleが2026年頃のリリースに向けて開発中と噂される、Android（Android 17ベース）とChromeOSを統合した次世代PC向けOSです。AI（Gemini）を中核に据え、スマートフォンのエコシステムをそのままPCで展開する野心的なプロジェクトですが、デスクトップUXの成熟やハードウェア要件の高騰など、今後の課題も指摘されています。

* **AIネイティブ設計**：OSレベルでGeminiなどのAIが深く統合され、文脈の先読みやサポートを前提とした設計。
* **Android 17ベースの統合**：従来のChromeOS上の仮想環境ではなく、Androidがネイティブ動作。スマートフォン、タブレット、PC（Box等）でシームレスな体験を提供。
* **ローカルAI処理（NPU）**：クラウドに依存せず、端末内のNPUを活用することで、高速かつプライバシーを保護したリアルタイム処理（翻訳、要約等）を実現。

## 2. メリットとデメリット

| <div align="center">項目</div> | <div align="center">詳細</div> |
| :--- | :--- |
| **メリット** | **強大なエコシステム**：スマホと同じUI・アプリがネイティブ動作。<br>**プライバシーと速度**：NPUによるローカル処理でデータ漏洩リスクを低減。<br>**自由度と省電力**：Android由来のバッテリー効率と、APKサイドロードの可能性。 |
| **デメリット** | **デスクトップUXの未成熟**：モバイルUIの引き伸ばし感、マウス・キーボード操作時の「もっさり感」。<br>**ハードウェア要件の高騰**：システム全体のAI処理・ネイティブAndroid環境のため、大容量RAMとNPUが必須化。<br>**既存PCソフトとの互換性**：Windows / macOS向けの本格的な業務用ソフトウェアが動作しない懸念。 |
## 3. コミュニティの反応（Reddit等）

海外の主要Techコミュニティ（r/Android, r/chromeosなど）では、期待と懸念が二分しています。

* **ポジティブな意見**：「Samsung DeXの究極進化系」「これでアプリ開発者もデスクトップ（大画面）対応を余儀なくされ、エコシステム全体が底上げされる」
* **ネガティブな意見**：「UIデザインが散らかっている（タスクバーの不統一など）」「モバイルOSのPC市場参入は、過去の失敗（Windowsのモバイル参入の逆）を繰り返すのではないか」

## 4. ブラウジング環境とコンテンツブロックの最適化構成

**Chrome拡張機能 `AdGuard Browser Extension MV3` と Androidアプリ `personalDNSfilter` の併用**

OSのAndroidベース化に伴う環境変化において、システム全体の通信制御をAndroidアプリ `personalDNSfilter` に任せ、ブラウザ内の要素隠蔽やスクリプト制御をChrome拡張機能 `AdGuard Browser Extension MV3` で行う併用構成を採用することで、高いパフォーマンスとフィルタリング精度を両立できます。

この併用環境下において、フィルタリングルールを軽量かつ効果的に機能させるための技術的要件は以下の通りです。

* **役割の分離とDNSブロック**：トラフィック・ドメインレベルのブロック（広告やテレメトリの通信遮断）は、軽量なシステムレベルDNSフィルタである `personalDNSfilter` に一任します。これにより、ブラウザ拡張機能側の処理負荷を大幅に削減できます。
* **スクリプトレットの注入（AdGuard拡張機能）**：ブラウザ上の高度な制御においては、AdGuard専用の `#%#//scriptlet` を記述して適用します。
* **テキスト要素の非表示（AdGuard拡張機能）**：テキストベースの要素隠蔽機能では、AdGuard環境で適切に処理される `:contains(...)` を採用します。
* **CSSの最適化（AdGuard拡張機能）**：拡張機能によるブラウザのレンダリング負荷を最小限に抑えるため、要素隠蔽は可能な限りシンプルな標準CSS構文（`##`）で記述します。高度なCSS（`#$#`）や処理の重い拡張疑似クラス（`:has` など）の使用は、どうしても必要な場面のみに限定します。

## 5. プライバシーとカスタマイズ性

* **メリット**：APKのサイドロードにより、Morphe等のカスタマイズアプリの運用が容易になる。
* **懸念点**：OSレベルでのAI（Gemini）常時稼働によるテレメトリ（データ収集）リスク。データ送信を最小限に抑え、NPUによる「完全ローカル処理」がどこまで徹底されるかが最大の焦点となる。

## 6. 情報ソース

* 関連ニュースメディア
    * [DIME](https://dime.jp/)
    * [GIGAZINE](https://gigazine.net/)
* 海外Redditコミュニティ
    * [r/Android](https://www.reddit.com/r/Android/)
    * [r/chromeos](https://www.reddit.com/r/chromeos/)
    * [r/windows](https://www.reddit.com/r/windows/)
    * [r/Design](https://www.reddit.com/r/Design/)
