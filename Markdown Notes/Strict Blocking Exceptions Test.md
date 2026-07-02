# My docomoにおけるStrict blockingの挙動と各種例外化ルールの互換性検証レポート
 
AdGuard製品において、ユーザールール `||mydocomo.jp^$document` を適用した時の動作について

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-UserScript-Regex-Markdown](https://github.com/Red-Frame-X/AdGuard-UserScript-Regex-Markdown) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260702 |

この備忘録は CC0 ライセンスの下で提供します。（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

※ 記述内容は個人の検証に基づくものであり、正確性を保証するものではありません。

## 1. 動作環境

* **Desktop**：ChromeOS / Chrome / AdGuard Browser Extension MV3
* **Mobile**：Android / Chrome / AdGuard for Android

---

## 2. `||mydocomo.$document` ルールと例外化の検証

`||mydocomo.$document` は、対象となるメインドキュメントの読み込みを強力に遮断する Strict blocking ルールです。
このルールを例外化し、サイトアクセスを回復させる際の挙動には、各コンテンツブロッカーの構文解析（パーサー）の実装とアーキテクチャによる明確な違いが見られます。

### 2.1. AdGuardとuBlock Originにおける動作の違い

* **uBlock Originの挙動**
  
  uBlock Originの設計思想において、Strict blocking を解除する場合は、ブロックルールと完全に対応する同一スコープの `@@||mydocomo.docomo.ne.jp^$document` を用いるか、あるいは修飾子を持たない `@@||mydocomo.docomo.ne.jp^` を用いるのが公式なベストプラクティスです。非標準的な `$all` を用いた場合でも内部的に解釈されてアクセスが可能になるケースはありますが、厳格なルール記述としては推奨されません。

* **AdGuardの挙動**
  
  AdGuardの仕様において、`$all` 修飾子はすべてのコンテンツタイプ（ `$popup` を含む）を指定する役割を持ちますが、明示的な `$document` ブロックを完全に上書き・解除できないケースがあり、警告画面が発火したままアクセスが遮断されることが確認されました。AdGuard環境で確実に Strict blocking を解除するには、同一スコープである `$document` 修飾子を指定する必要があります。

---

### 2.2. 例外ルール適用時の挙動

#### `$all` による例外化（`@@||mydocomo.docomo.ne.jp^$all`）

* **挙動**：uBlock Originではアクセス可能となる場合があるが、AdGuardでは警告画面が回避できずアクセスが遮断される。

* **メリット**：記述が機能する環境においては、単一のルールで複数のリクエストやポップアップを網羅的に許可できる即効性があります。

* **デメリット**：エンジン間でパーサーの解釈違いが発生しやすく、意図した例外処理が行われない互換性のリスクを伴います。また、本来ブロックされるべきトラッキング通信まで許可してしまう「過剰な例外化」に繋がる恐れがあります。

* **ベストプラクティス**：クロスプラットフォームで提供されるフィルタリストの保守においては、互換性とセキュリティの観点から `$all` の使用を避け、ブロックルールと対応する修飾子を指定するのが標準的です。

#### `$document` による例外化（`@@||mydocomo.docomo.ne.jp^$document`）

* **挙動**：AdGuard・uBlock Originともに警告画面は回避されHTMLの読み込みは可能となるが、AdGuardではページ上で不規則なエラーダイアログが頻発する。

* **メリット**：エンジンを問わず、メインドキュメントに対する通信遮断（Strict blocking）を意図通りかつセキュアに解除できます。

* **デメリット**：この指定はあくまで「ネットワークレベルでのHTMLドキュメントの許可」に限定されるため、その他の保護機能が引き続き作動し、サイトの機能に干渉する可能性が残ります。

---

### 2.3. エラーの推測原因（`@@||mydocomo.docomo.ne.jp^$document` 適用時のAdGuard環境）

My docomoのような状態管理が厳密なSPAにおいて、AdGuardのCoreLibsエンジンや拡張機能が動的に適用する高度な要素隠蔽ルール（Extended CSS）やスクリプトレット注入（Scriptlets）は、`$document` 例外のみでは無効化されません。これらがフロントエンドのDOM操作と競合している可能性が高いと考えられます。

また、以下の要因によってサイト側の厳格なエラーハンドリングが予期せず発火しているケースも推測されます。

* システムレベルのHTTPSフィルタリングによる介入
* DNSモジュールによるバックグラウンドのテレメトリAPI通信の遮断

---

### 2.4. エラーの追加検証

* AdGuard製品を導入した環境では、`||mydocomo.$document` によりStrict blockingが発生してAdGuardの警告画面が表示され、`mydocomo.docomo.ne.jp` へのアクセスがブロックされます。→ ◯
* AdGuard製品を導入している環境では、`||mydocomo.$document` が原因で `mydocomo.docomo.ne.jp` へアクセスするたびにエラーダイアログが出現し続けます。→ △
  * My docomoの公式ウェブサイト（mydocomo.docomo.ne.jp）のような状態管理が厳密なSPAにおいては、AdGuard製品のローカルVPNの影響で、エラーダイアログが出現することがあります。→ ◯
  * `@@||mydocomo.docomo.ne.jp^$all` を例外ルールとして登録しても、AdGuard製品を導入した環境ではStrict blockingが発生してAdGuardの警告画面が表示され、`mydocomo.docomo.ne.jp` へのアクセスがブロックされます。→ ◯ 
  * `@@||mydocomo.docomo.ne.jp^$document` を例外ルールとして登録しても、AdGuard製品を導入した環境ではエラーダイアログが出現し続けます。→ ◯
