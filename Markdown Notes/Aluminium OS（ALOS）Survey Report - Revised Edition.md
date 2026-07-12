# Aluminium OS（ALOS）Survey Report - Revised Edition

Aluminium OS（ALOS）/ Googlebook 調査レポート 改訂版

2026年5月のGoogle I/OおよびAndroid Showにて正式発表された「Googlebook（開発コードネーム：Aluminium OS）」に関する最新情報のまとめです。
AndroidのエコシステムとChromeOSの利便性をネイティブに統合し、AI（Gemini）をOSの基盤レベルで組み込んだ次世代ノートPC規格であり、2026年秋のリリースが予定されています。
本レポートでは、確定した公式仕様、プライバシーを保護しつつ高度な広告ブロックを両立する技術的最適化の手法、およびコミュニティの動向を客観的な視点から整理しています。

---

### メタデータ (2026年7月2日時点)

| 項目 | 詳細 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260712 |

**【ライセンスおよび免責事項】**

この備忘録は [コモンズ証 - CC0 1.0 全世界 - Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) の下で提供します。

※ ただし、引用等で示された第三者の文章、ソフトウェア・アプリ・拡張機能の名称および公式の製品説明文、リンク先のコンテンツは本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。

※ 本記述内容はセキュリティおよびフィルタリングのベストプラクティス、ならびに2026年7月時点の公開情報を反映していますが、発売前の製品仕様については一部変更される可能性があります。

---

## 1. 基本概要

Aluminium OSは、Googleが次世代PC向けに開発していたOSの開発コードネーム（Project Aluminium / ALOS）です。2026年5月のGoogle I/OおよびAndroid Showにて新カテゴリ「Googlebook」の基盤システムとして正式発表されました。

### 公式発表に基づく確定事項
* **Googlebookの展開**：AndroidとChromeOSを融合。2026年秋よりOEM各社（Acer、ASUS、Dell、HP、Lenovoなど）から第一弾モデル発売。
* **Gemini Intelligence**：OSレベルでのAI統合。「マジックポインタ」による文脈提案や、音声・テキスト指示による「カスタムウィジェットの作成」を実装。
* **スマホとのシームレス統合**：同一GoogleアカウントのAndroid端末内データ（写真・ファイル）を、PC側のウィンドウから直接参照・挿入可能。
* **ネイティブなAndroid環境**：仮想化に頼らず、Androidアプリがネイティブ速度で動作。
* **セキュアなLinux対応**：AVF（Android Virtualization Framework）を採用し、安全にLinux環境（Debian等）を仮想動作。
* **既存Chromebookの移行**：RAM 8GB / ストレージ 128GB / Intel第12世代またはRyzen以上のプロセッサを搭載する「Chromebook Plus」相当の要件が必須（段階的サポート移行）。

### リーク・未確定事項
* **ベースOS**：「Android 17」が基盤になると推測されるが、ナンバリングの公式明言はなし。
* **展開スケジュール**：一般・法人向けの本格展開は2028年までずれ込む可能性（裁判資料・リークより）。
* **ChromeOSの終焉**：既存端末のメンテナンスモードは10年保証に基づき継続。完全なフェーズアウトは2034年頃と推測。

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
* **標準CSSによる要素隠蔽**：ブラウザ負荷の少ない標準構文 `##` を優先。Shadow DOMの突破などが必要な場合は `#$#` を使用。
* **拡張CSSルール**：標準CSSで対応できない複雑な要素には `#?#` または `#$?#(...)` を使用。
* **擬似クラスの最適化**：
  * テキスト隠蔽には `:contains(...)` を活用。
  * 状態を表す `:has(...)` は、モダンブラウザのネイティブ実装へ処理を寄せて負荷を下げる方針が推奨される。

---

## 4. AdGuardの対応状況とローカルVPNの活用

Aluminium OS環境下におけるAdGuardの動作見通しは以下の通りです。

* **AdGuard専用版の開発状況**：
  * 2026年7月現在、「AdGuard for Aluminium OS」という専用アプリの開発計画は公式発表されていません。
* **AdGuard for Android（APK版）のシステム全体保護**：
  * Aluminium OSはAndroidアプリをネイティブ実行するため、従来の「AdGuard for Android（APK版）」がローカルVPNを用いて機能する可能性が高いです。
  * 既存のChromeOSでもAndroid向けVPNアプリがシステム全体のトラフィック（Chromeブラウザの通信含む）をルーティングできる仕様があり、本OSでもこのアーキテクチャが踏襲されると見込まれます。

---

## 5. テレメトリとAI処理の境界

完全なAndroidベースとなるため、高度なカスタマイズやAPKサイドロードの恩恵を受けやすい一方、プライバシー管理が重要になります。
最大の焦点は、**システムレベルで稼働するAI（Gemini）のデータ処理の所在**です。NPUを活用した「完全ローカル処理」がアピールされていますが、ウェブ検索やGmail連携等のクラウド処理が混在するため、データ送信のオプトアウト制御が今後のセキュリティ監査における重要課題となります。

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
