# AdGuard Custom Rules 設計・検証メモ

AdGuard ブラウザ拡張機能 MV3対応版とAdGuard for Androidで、自分がカスタムルールを作成・検証するときに確認する考え方をまとめた個人用の学習メモです。

> [!NOTE]
> この文書は自分の学習・検証・設定バックアップ用であり、一般向けのチュートリアル、ベストプラクティス集、推奨構成を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。構文や製品差は変更される可能性があるため、実際にルールを変更するときはAdGuard公式リファレンス、公開ソース、Filtering log、実環境で再確認します。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

---

## 1. 自分が最初に確認する製品差

同じAdGuard構文でも、ブラウザ拡張機能 MV3対応版とAdGuard for Androidでは実行基盤が異なります。自分がルールを移すときは、構文が受理されるかだけでなく、同じ意味で動くかを確認します。

| 機能・特性 | AdGuard ブラウザ拡張機能 MV3対応版 | AdGuard for Android |
| :--- | :--- | :--- |
| **主な動作範囲** | ブラウザ内。ネットワーク制御はDNRの制約を受ける | ローカルVPN等を使い、対応アプリの通信を処理 |
| **ルール上限** | DNRの静的・動的ルール上限を考慮する | DNRの固定上限はないが、ルール量や処理内容による負荷は考慮する |
| **`$app`** | ブラウザ拡張機能では対象外 | 対応 |
| **レスポンス改変** | MV3/DNRでは制約が大きい | HTTPSフィルタリング等の条件を満たす場合に利用できる機能がある |
| **主な確認点** | DNR変換可否、サイト権限、User Scripts API、更新方式 | HTTPSフィルタリング、対象アプリ、ローカルVPN、互換性 |

製品ごとの最終的な対応状況は、[AdGuard公式フィルタリングルール構文](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)と使用中バージョンで確認します。

---

## 2. 自分の学習・検証手順

### Step 1：単純なルールから確認する

要素非表示では、まず標準CSSセレクタで表現できる`example.com##.ad-box`のような単純なルールを検討します。通信を止める必要がある場合は、Filtering logやDevToolsのNetwork情報で対象リクエストを確認してからネットワークルールを作ります。

自動生成されたクラス、位置依存の`:nth-child()`、長いDOMパスは、サイト変更で壊れやすいため、自分のルールでは可能な限り避けます。

### Step 2：通信ブロックと要素非表示を分ける

ネットワークルールとコスメティックルールは役割が異なります。広告枠が見えるという理由だけで通信先を推測してブロックせず、HTMLだけでは通信を特定できない場合はNetwork情報を追加で確認します。

### Step 3：既存フィルタとの重複を確認する

AdGuard Base Filter、AdGuard Japanese filter、その他自分が有効にしているフィルタですでに処理されていないかを確認します。自分のユーザールールは、特定サイト・特定アプリの差分や、自分の環境で必要になった例外を中心に残します。

### Step 4：別エンジンのルールは意味を確認してから移す

uBlock OriginとAdGuardには共通する構文が多い一方、scriptlet、redirect resource、procedural cosmetic filtering、修飾子などに差があります。uBO用の`##+js(...)`を文字列置換だけでAdGuardの`#%#//scriptlet(...)`へ変換せず、両者の公開ドキュメントやソースで名前・引数・副作用を比較します。

### Step 5：ログで原因を切り分ける

誤ブロックを疑う場合は、追加したルールを一つずつ無効化し、Filtering log、DevTools、必要に応じてDNSログを確認します。DNS、ネットワーク、コスメティック、scriptletなど複数レイヤーを同時に変更しないようにします。

### Step 6：変更後に正常系も確認する

対象要素が消えたことだけではなく、ログイン、検索、再生、決済、スクロール、リンク遷移など、そのページで必要な機能が壊れていないかも確認します。

---

## 3. 自分がルール設計で優先すること

### 適用範囲を狭くする

サイト限定ルール、リソース種別、`$domain=`、AdGuard for Androidで必要な場合の`$app=`などを使い、無関係なサイト・アプリへ影響しない形を優先します。

### 強力な例外・修飾子を最初から広く使わない

`$document`や広い例外ルールは対象ページのフィルタリングへ大きな影響を与えます。`$important`などの強い修飾子も、既存ルールとの優先順位を変える必要性を確認してから使います。

### 標準CSSで済む場合は標準CSSを使う

Extended CSSやテキスト一致は便利ですが、DOMや表示文言への依存が強くなる場合があります。`:has()`などは対応環境では有効な選択肢ですが、単純なID・属性・クラスで十分な場合はそちらを優先します。

### テキスト一致は変更に弱いことを意識する

AdGuardの`:contains()`などで表示文言へ依存すると、言語・表記変更でルールが壊れる可能性があります。テキスト一致が必要な場合は、対象サイトと目的を限定して残します。

### Scriptletは最後の候補にする

CSSや限定的なネットワークルールでは解決できない場合に、AdGuard公式Scriptletsライブラリで存在と引数を確認したうえで使います。サイト側JavaScriptの変更で壊れやすく、正常処理へ干渉する可能性があるため、広い適用は避けます。

### 生成AIの提案をそのまま採用しない

ChatGPTなどが生成したルールは、構文上もっともらしくても対象製品で未対応だったり、見えていないDOM・通信を推測している場合があります。自分の環境では、公式構文とログで検証できたものだけを残します。

---

## 4. AdGuard for Android ローレベル設定の扱い

ローレベル設定は通常のフィルタ作成とは別の領域です。VPN、DNS、HTTPSフィルタリング、プロキシ、ログなどの挙動へ影響するため、自分の通常運用では既定値を基準にします。

設定を変更するのは、再現する不具合があり、公式ドキュメントやサポート情報から比較対象を特定できる場合に限定します。変更前の値を記録し、一項目ずつ比較して、効果がなければ元へ戻します。

### 自分が確認する項目

- **VPN・バックグラウンド動作**：OSの省電力やVPN状態が保護の継続へ影響していないか。
- **DNS関連**：プライベートDNS、DoH、DNSフィルタリングを混同せず、どのレイヤーが原因か切り分ける。
- **HTTP/3 / QUIC・ECH関連**：接続性やフィルタリングへ関係する症状がある場合だけ、公式説明を確認して比較する。
- **IPv6関連**：IPv6そのものを一律に無効化せず、再現する通信問題との因果を確認する。
- **ログレベル**：詳細ログは必要な検証時だけ一時的に使い、個人情報・URL・通信内容が含まれ得る点に注意する。

ローレベル設定の名称・既定値はバージョンで変わる可能性があります。古いメモの設定名をそのまま現在版へ適用しません。

---

## 5. 誤ブロック時の自分用チェック

1. 直前に追加・変更した自分のルールを無効化する。
2. 問題が消えるか確認する。
3. Filtering logで対象通信と適用ルールを確認する。
4. コスメティックルールの場合は、対象DOMとセレクタの一致範囲を確認する。
5. DNSフィルタも使用している場合は、DNS側を一時的に切り離す。
6. 原因が購読フィルタ側と確認できた場合は、自分用の例外が本当に必要か、上流ですでに修正されていないかを確認する。
7. 一時回避ルールを残した場合は、後日不要になっていないか見直す。

`$badfilter`や広い例外は便利ですが、上流修正後も残ると不要な状態変更になるため、作成理由をコメントで残します。

---

## 6. 自分用の構文確認メモ

| 目的 | まず確認する方法 |
| :--- | :--- |
| 特定要素を隠す | `example.com##selector` |
| テキスト条件が必要 | `:contains()`などAdGuard対応構文を公式資料で確認 |
| 特定通信を止める | Filtering log / NetworkでURLと種別を確認して限定的なネットワークルール |
| 特定サイトだけに限定 | `$domain=`またはドメイン付きコスメティックルール |
| Androidの特定アプリに限定 | `$app=`の対応と対象パッケージを確認 |
| 購読フィルタの誤ブロックを避ける | 原因ルールを特定して最小の例外を検討 |
| JavaScript挙動へ介入 | AdGuard Scriptlets公式ライブラリを確認し、必要な場合だけ使用 |

---

## 7. 参照する資料

- [AdGuard — How to create your own ad filters](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard for Android — Settings](https://adguard.com/kb/adguard-for-android/features/settings/)
- [AdGuard for Android — Low-level settings](https://adguard.com/kb/ja/adguard-for-android/features/low-level-settings/)
- [AdGuard Scriptlets](https://github.com/AdguardTeam/Scriptlets)
- [AdGuard Filters](https://github.com/AdguardTeam/AdguardFilters)
- [uBlock Origin — Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [uBlock Origin — Element picker](https://github.com/gorhill/uBlock/wiki/Element-picker)
- [Chrome — declarativeNetRequest API](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest)
- [EasyList](https://easylist.to/)

これらのリンクも将来変更される可能性があるため、自分が重要な変更を行うときはリンク先の現行内容を確認します。
