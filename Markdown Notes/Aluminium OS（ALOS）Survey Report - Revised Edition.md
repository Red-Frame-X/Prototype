# Aluminium OS（ALOS）/ Googlebook 調査レポート 改訂版

**【要約】**
2026年5月のGoogle I/OおよびAndroid Showにて正式発表された「Googlebook（開発コードネーム：Aluminium OS）」に関する最新情報のまとめです。AndroidのエコシステムとChromeOSの利便性をネイティブに統合し、AI（Gemini）をOSの基盤レベルで組み込んだ次世代ノートPC規格であり、2026年秋のリリースが予定されています。本レポートでは、確定した公式仕様、プライバシーを保護しつつ高度な広告ブロックを両立する技術的最適化の手法、およびコミュニティの動向を客観的な視点から整理しています。

---

2026年7月1日時点で判明しているAluminium OS（製品名：Googlebook）に関する情報

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

※ 本記述内容はセキュリティおよびフィルタリングのベストプラクティス、ならびに2026年7月時点の公開情報を反映していますが、発売前の製品仕様については一部変更される可能性があります。

## 1. 基本概要

Aluminium OSは、Googleが次世代PC向けに開発していたOSの開発コードネーム（Project Aluminium / ALOS）です。2026年5月のGoogle I/OおよびAndroid Showにて「Googlebook」として正式発表されました。

**【公式発表に基づく確定事項】**
* **Googlebookの発表と名称**：
  * AndroidとChromeOSを融合したAIネイティブなノートPC規格「Googlebook」として展開され、2026年秋よりOEM各社（Acer、ASUS、Dell、HP、Lenovoなど）から第一弾モデルが発売予定です。
* **Gemini Intelligenceの中核化**：
  * システム全体にAIが統合されています。画面上でカーソルを小さく振るだけで文脈に応じたAI提案を呼び出せる「マジックポインタ（Magic Pointer）」や、音声・テキスト指示でGmailやカレンダーの情報をまとめた専用ダッシュボードを生成する「カスタムウィジェットの作成（Create My Widget）」が実装されています。
* **スマートフォンとのシームレスな統合**：
  * 同じGoogleアカウントで紐付けたAndroid端末内のデータ（写真やファイル）を、PC側の「ファイル」ウィンドウから直接参照・挿入できる機能が標準搭載されています。
* **AVF（Android Virtualization Framework）によるLinux対応**：
  * Androidアーキテクチャ内部で安全にLinux環境（Debianなど）を仮想動作させる仕組みが採用されており、開発者向けの高度な作業もサポートされます。
* **既存Chromebookの継続サポート**：
  * ChromeOSは直ちに廃止されるわけではなく、既存のChromebookに対してもアップデートを通じてGooglebookと同等の機能が順次バックポートされる計画が公式に明言されました。

**【リーク・未確定事項】**
* **Androidベースのバージョン**：
  * 「Android 17」が基盤になるとの有力な推測がありますが、Googleからの公式なナンバリング明言は控えられています。

## 2. メリットとデメリット

Aluminium OS（Googlebook）導入における主な利点と懸念点は以下の通りです。

### メリット
* **強大なエコシステムとの連携**：
  * Androidアプリがエミュレーション不要でネイティブ動作します。また、スマートフォンとの直接的なファイル連携により、デバイス間の境界がシームレスになります。
* **AIによる生産性向上**：
  * OSレベルで統合されたGeminiがユーザーの意図を先読みします。日程調整や視覚的シミュレーションといった複雑なタスクを劇的に短縮可能です。
* **安全な開発環境**：
  * AVF（Android Virtualization Framework）によるセキュアなコンテナ技術を採用。ホストシステムを汚染することなく、安全にLinux環境を構築・運用できます。

### デメリット
* **デスクトップUXの最適化途上**：
  * 全てのAndroidアプリが大画面やマルチウィンドウ、キーボード・マウス操作に完全対応しているわけではありません。一部のアプリでは、モバイルUIが引き伸ばされたような表示になる可能性があります。
* **ハードウェア要件と価格**：
  * NPUを用いたローカルAI処理を前提とした設計です。そのため、従来の安価なChromebookと比較して、端末のベース価格が高額化する傾向にあります。

## 3. コミュニティの反応（Reddit等）

海外の主要Techコミュニティ（r/Android, r/chromeosなど）では、公式発表を経て議論が成熟しつつあります。

* **ポジティブな意見**：
  * 「AVFによるLinux対応が確定したことで、開発機としての実用性が担保された」「Androidアプリが仮想環境ではなくネイティブ動作するため、パフォーマンスのオーバーヘッドが解消されるのは革新的」
* **懸念・注視されている意見**：
  * 「WindowsやmacOS向けの本格的なレガシー業務ソフトへの代替アプローチがウェブアプリ依存になる点」「既存Chromebookへの機能バックポートがどこまで（どの世代のハードウェアまで）適用されるかの詳細待ち」

## 4. ブラウジング環境とコンテンツブロックの最適化構成

**Chrome拡張機能 `AdGuard Browser Extension MV3` と Androidアプリ `personalDNSfilter` の併用**

OSのネイティブAndroidベース化に伴い、システム全体のトラフィック・ドメインレベルの通信制御を軽量なAndroidアプリ `personalDNSfilter` に任せ、ブラウザ内の要素隠蔽や高度なスクリプト制御をChrome拡張機能 `AdGuard Browser Extension MV3`（以下 `MV3`）で行うハイブリッド構成が最も効率的です。これにより、ブラウザのレンダリング負荷を大幅に削減しつつ、強固なプライバシー保護を実現します。

この環境下において、AdGuardの公式仕様に基づいたフィルタ開発・技術的要件（記法）は以下の通りです。

* **スクリプトレットの注入（MV3）**：
  * ブラウザ上の高度な制御においては、`#%#//scriptlet(...)` を「scriptletルール」として適用します。
* **CSSによる要素隠蔽（MV3）**：
  * 要素隠蔽は可能な限りブラウザへの負荷が少ない標準CSS構文 `##` で記述します。Shadow DOMの突破など高度な制御が必要な場合は、`#$#` を「CSSルール」として記述します。
* **拡張CSSルール（MV3）**：
  * 標準CSSで対応できない複雑な要素には、`#?#` または `#$?#(...)` を「拡張CSSルール」として使用します。
* **擬似クラスの最適化（MV3）**：
  * テキストベースの要素隠蔽には、拡張CSSの擬似クラスとしてサポートされている `:contains(...)` を活用します。
  * 状態を表す `:has(...)` については、最新のAdGuardでは**ブラウザのネイティブ実装が利用可能な環境（モダンブラウザ等）ではそちらに処理を寄せて負荷を下げる方針**となっています。そのため、一律に避けるのではなく、環境に応じて適切に活用することが推奨されます。

## 5. プライバシーとカスタマイズ性

* **カスタマイズの恩恵**：
  * 完全なAndroidベースとなるため、従来のChromeOS以上に高度なカスタマイズやAPKサイドロードの恩恵を受けやすい環境が整っています。
* **テレメトリとAI処理の境界**：
  * 最大の焦点は、システムレベルで稼働するAI（Gemini）のデータ処理の所在です。NPUを活用した「完全ローカル処理」によるプライバシー保護機能がアピールされているものの、ウェブ検索やGmail連携等のクラウド処理が混在するため、データ送信をどこまでユーザー側でオプトアウト・制御できるかが、今後のセキュリティ監査における重要課題となります。

## 6. 関連情報ソース一覧 (2026年7月時点)

本リストは、「Googlebook」および関連するOS「Aluminium OS」に関する最新の報道、技術解説、セキュリティ動向をまとめたものです。

### 公式・技術報道
Googleによる公式発表および主要メディアによる速報です。
* **[ITmedia]** [Googleが「Googlebook」をチラ見せ AndroidとChromeOSを“融合”した全く新しいノートPC 詳細は2026年後半に紹介](https://www.itmedia.co.jp/pcuser/articles/2605/13/news059.html)
* **[ケータイ Watch]** [グーグル、新たなノートパソコン「Googlebook」発表 Gemini搭載でAndroidとChromeOSが融合](https://k-tai.watch.impress.co.jp/docs/news/2106890.html)
* **[GIGAZINE]** [Gemini向けノートPC「Googlebook」の登場によってChromebookはどうなるのか？](https://gigazine.net/news/20260514-googlebooks-premium-focus/)

### 技術解説・分析
OSの統合や将来的な戦略に関する専門的な分析記事です。
* **[株式会社オブライト]** [Googlebook 完全解説 — Google I/O 2026 で発表された Chromebook 後継の Android+ChromeOS 統合ノートPC規格](https://www.oflight.co.jp/ja/columns/google-googlebook-chromebook-successor-io-2026)
* **[Android Authority]** [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
* **[9to5google]** [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)

### フィルタリング・セキュリティ関連
コンテンツブロックおよびプライバシー保護に関する最新の技術情報です。
* **[AdGuard Blog]** [AdGuard Browser Extension v5.3: A stronger core, a smoother experience](https://adguard.com/en/blog/adguard-browser-extension-v5-3.html)

### 検索ポータル・コミュニティ
最新動向を追跡するためのコミュニティおよび検索リソースです。
* **[Google 検索]** ["Googlebook" Android ChromeOS 関連最新動向](https://www.google.com/search?q=%22Googlebook%22+Android+ChromeOS)
* **[Reddit]** [r/chromeos](https://www.reddit.com/r/chromeos/)
* **[Reddit]** [r/AluminiumOS](https://www.reddit.com/r/AluminiumOS/)
