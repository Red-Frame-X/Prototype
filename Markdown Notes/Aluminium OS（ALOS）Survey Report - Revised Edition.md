# Aluminium OS（ALOS）Survey Report - Revised Edition

Aluminium OS（ALOS）/ Googlebook 調査レポート 改訂版

2026年5月にGoogleが発表した「Googlebook」と、発表以前に報道された開発コードネーム「Aluminium」に関する情報のまとめです。
Googleは、AndroidとChromeOSの長所を取り入れ、Geminiを中核に据えた新しいノートPCカテゴリとしてGooglebookを紹介し、2026年秋の発売を予告しています。発売前のため、公式発表と報道・推測を分けて記載します。
本レポートでは、確定した公式仕様、プライバシーを保護しつつ高度な広告ブロックを両立する技術的最適化の手法、およびコミュニティの動向を客観的な視点から整理しています。

---

### メタデータ (2026年7月2日時点)

| 項目 | 詳細 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260804 |

**【ライセンスおよび免責事項】**

この備忘録は [コモンズ証 - CC0 1.0 全世界 - Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) の下で提供します。

※ ただし、引用等で示された第三者の文章、ソフトウェア・アプリ・拡張機能の名称および公式の製品説明文、リンク先のコンテンツは本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。

※ 本記述内容はセキュリティおよびフィルタリングのベストプラクティス、ならびに2026年7月時点の公開情報を反映していますが、発売前の製品仕様については一部変更される可能性があります。

---

## 1. 基本概要

「Aluminium」は、GoogleのAndroidベースPCプロジェクトについて求人情報などから報道された開発コードネームです。Googleの2026年5月の公式発表は製品カテゴリ名を「Googlebook」としており、公式記事では「Aluminium OS」や「ALOS」を製品名として確定していません。

### 公式発表に基づく確定事項
* **Googlebookの展開**：AndroidとChromeOSの長所を取り入れた新カテゴリ。Googleは主要パートナーによるプレミアムハードウェアと、2026年秋の発売を予告しています。公式記事では個別メーカー、発売日、価格は確定していません。
* **Gemini Intelligence**：OSレベルでのAI統合。「マジックポインタ」による文脈提案や、音声・テキスト指示による「カスタムウィジェットの作成」を実装。
* **Android端末との連携**：スマートフォンのアプリやファイルへアクセスできる連携を予告しています。具体的な要件や対応範囲は未公表です。

### リーク・未確定事項
* **ベースOS**：「Android 17」が基盤になると推測されるが、ナンバリングの公式明言はなし。
* **AndroidアプリとLinux環境**：実行方式、互換性、AVF採用の有無などの詳細は、現時点の公式紹介記事では確定していません。
* **既存Chromebookの移行**：対象機種、最低RAM・ストレージ・CPU要件、移行時期は公式発表されていません。
* **ChromeOSの将来**：既存端末は各モデルの自動更新期限に従いますが、Googlebook発表だけからChromeOSの終了時期を断定することはできません。

---

## 2. メリットとデメリット

| メリット (Pros) | デメリット (Cons) |
| :--- | :--- |
| **強大なエコシステム**<br>Androidアプリがエミュレーション不要でネイティブ動作。オーバーヘッドが解消される。 | **移行ハードルの高さ**<br>高度なAI処理のため高スペック（最低8GB RAM等）が必須。安価な旧型機は非対応。 |
| **AIによる生産性向上**<br>システム全体に統合されたGeminiが意図を先読みし、複雑なタスクを短縮。 | **デスクトップUXの最適化途上**<br>全アプリが大画面やマウス操作に完全対応しておらず、モバイルUIが引き伸ばされる可能性。 |
| **安全で柔軟な開発環境**<br>AVFによるセキュアなLinux環境の構築。スマホとPC間のシームレスな体験。 | **レガシー業務ソフトへの対応**<br>Windows/macOS向け本格ソフトへの代替アプローチは、引き続きウェブ/クラウド依存。 |

---

## 3. プライバシーと広告ブロックの最適化構成

OSのネイティブAndroidベース化に伴い、通信制御とブラウザ上のコンテンツブロックを分離する「ハイブリッド構成」が最もリソース効率に優れます。

**【推奨ハイブリッド構成】**
1. **システム全体**：Androidアプリ `personalDNSfilter`
2. **ブラウザ内**：Chrome拡張機能 `AdGuard Browser Extension MV3`

### フィルタ開発と技術的要件
AdGuardの公式仕様に基づいたフィルタの記述ベストプラクティスは以下の通りです。

* **スクリプトレット注入 (MV3)**：高度な制御には `#%#//scriptlet(...)` を適用。
* **標準CSSによる要素隠蔽**：標準構文 `##` を優先。`#$#`はCSSスタイルを注入する構文であり、Shadow DOMを一律に越える構文ではありません。
* **拡張CSSルール**：標準CSSで対応できない複雑な要素には `#?#` を使用します。スタイルを指定する拡張CSSルールは `example.com#$?#selector { property: value; }` の形で記述します。
* **擬似クラスの最適化**：
  * テキスト隠蔽には `:contains(...)` を活用。
  * 状態を表す `:has(...)` は、モダンブラウザのネイティブ実装へ処理を寄せて負荷を下げる方針が推奨される。

---

## 4. AdGuardの対応状況とローカルVPNの活用

Aluminium OS環境下におけるAdGuardの動作見通しは以下の通りです。

* **AdGuard専用版の開発状況**：
  * 2026年8月4日現在、「AdGuard for Aluminium OS」という専用アプリの開発計画は公式発表されていません。
* **AdGuard for Android（APK版）のシステム全体保護**：
  * Googlebook上で「AdGuard for Android（APK版）」のローカルVPNがシステム全体へ適用できるかは、OSのVPN実装とアプリ互換性が公表されるまで未確定です。

---

## 5. テレメトリとAI処理の境界

OSの詳細設計は未公表ですが、Androidアプリや端末連携を扱う以上、プライバシー管理は重要になります。
最大の焦点は、**Geminiの各機能が端末内とクラウドのどちらで処理されるか**です。公式発表は機能概要に留まるため、「完全ローカル処理」と断定せず、発売時のプライバシー説明、管理設定、データ保持方針を確認する必要があります。

---

## 6. コミュニティの反応（Reddit等）

海外の主要Techコミュニティ（r/Android, r/chromeos等）での主な議論：

* **ポジティブな意見**
  * 「AVFによるLinux対応確定で、開発機としての実用性が担保された」
  * 「Androidアプリが仮想環境ではなくネイティブ動作するのは革新的」
* **懸念・注視事項**
  * 「既存Chromebookへのバックポートがどの世代まで適用されるかの詳細待ち」

---

## 7. 関連情報ソース一覧 (2026年7月時点)

### 公式・技術報道
* **Google公式ブログ**：
  * [Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)
* **ITmedia**：
  * [Googleが「Googlebook」をチラ見せ AndroidとChromeOSを“融合”した全く新しいノートPC 詳細は2026年後半に紹介](https://www.itmedia.co.jp/pcuser/articles/2605/13/news059.html)
* **ケータイ Watch**：
  * [グーグル、新たなノートパソコン「Googlebook」発表 Gemini搭載でAndroidとChromeOSが融合](https://k-tai.watch.impress.co.jp/docs/news/2106890.html)
* **GIGAZINE**：
  * [Gemini向けノートPC「Googlebook」の登場によってChromebookはどうなるのか？](https://gigazine.net/news/20260514-googlebooks-premium-focus/)

### 技術解説・分析
* **株式会社オブライト**：
  * [Googlebook 完全解説 — Google I/O 2026 で発表された Chromebook 後継の Android+ChromeOS 統合ノートPC規格](https://www.oflight.co.jp/ja/columns/google-googlebook-chromebook-successor-io-2026)
* **Android Authority**：
  * [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
* **9to5google**：
  * [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
* **GbookHub**：
  * [GbookHub｜HelenTech氏が運営するGooglebook（Aluminium OS）専門特化型メディア](https://gbookhub.io/)
* **GitHub Gists**：
  * [Kdroidwin氏による査読](https://gist.github.com/Red-Frame-X/bdb94de10653edf1d11bd341d2eb2118)

### フィルタリング・セキュリティ関連
* **AdGuard Blog**：
  * [AdGuard Browser Extension v5.3: A stronger core, a smoother experience](https://adguard.com/en/blog/adguard-browser-extension-v5-3.html)

### 検索ポータル・コミュニティ
* **Google 検索**：
  * ["Googlebook" Android ChromeOS 関連最新動向](https://www.google.com/search?q=%22Googlebook%22+Android+ChromeOS)
* **Reddit**：
  * [r/chromeos](https://www.reddit.com/r/chromeos/)
* **Reddit**：
  * [r/AluminiumOS](https://www.reddit.com/r/AluminiumOS/)
