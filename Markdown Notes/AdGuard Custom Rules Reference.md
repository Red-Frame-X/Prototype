# AdGuard Custom Rules 個人リファレンスメモ

AdGuardの主要なフィルタ構文について、自分がルールを作成・修正するときに用途と注意点を確認するための個人用リファレンスメモです。

> [!NOTE]
> この文書は自分の学習・検証・設定バックアップ用であり、一般向けの完全な構文リファレンスや推奨ルール集を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。MV3のDNRへ変換されるブラウザ拡張機能とCoreLibsを使うAdGuard for Androidでは対応機能や制約が異なるため、実際に使うときは[AdGuard公式構文リファレンス](https://adguard.com/kb/general/ad-filtering/create-own-filters/)と使用中バージョンで再確認します。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

---

## 1. ネットワークルールの確認メモ

### 基本形

```adblock
||example.com^
@@||example.com^$script
```

`@@`は例外ルールです。例外は広くしすぎると、本来ブロックしたい通信まで許可するため、自分のルールでは対象URL、リソース種別、適用元をできるだけ限定します。

### `$document`

```adblock
||example.com^$document
@@||example.com^$document
```

メインドキュメントを対象にします。影響範囲が大きいため、自分が使う場合はBlocking pageやページ全体のフィルタリングへの影響を公式仕様で確認します。

### `$subdocument`

```adblock
||example.com/ad-frame.html^$subdocument
```

`iframe`等のサブドキュメントを対象にします。ログイン、決済、埋め込みコンテンツも`iframe`を使うことがあるため、対象を推測だけで決めません。

### `$domain=`

```adblock
||example.com/ads.js$domain=test.com|~sub.test.com
```

ルールを適用する発信元サイトを限定するときに使います。自分のルールでは、特定サイトだけの問題へ対応するときに優先して検討します。

### `$app=`

```adblock
||ads.example.com^$app=com.example.app
```

AdGuard for Androidなど対応製品で、特定アプリへ適用範囲を限定します。ブラウザ拡張機能とは対応範囲が異なるため、共有フィルタへ含める場合は変換・互換性を確認します。

### `$third-party`

```adblock
||tracker.example^$third-party
```

第三者通信へ限定します。ファーストパーティ／サードパーティ判定は単純な「運営会社が同じか」とは一致しないため、自分が使うときは実際のリクエスト関係を確認します。

### リソース種別

```adblock
||example.com/ad.js$script
||example.com/ad.jpg$image
||example.com/api/track$xmlhttprequest
||example.com/live$websocket
```

対象通信の種類を限定できます。自分のルールでは、Filtering logやDevToolsで種別を確認できた場合に使います。

### `$popup`

```adblock
||example.com^$popup
```

新しいタブ・ウィンドウとして開かれる動作を対象にします。正規のログインや決済が別窓を使う場合もあるため、広いドメイン指定は避けます。

### `$match-case`

```adblock
||example.com/AdBanner^$match-case
```

URLの大文字・小文字を区別します。URL変更で壊れやすくなるため、必要性がある場合だけ残します。

---

## 2. 通信の書き換え・変更系ルール

これらは単純なブロックより副作用が大きいため、自分の環境では「必要性と対応製品を説明できる場合だけ使う」扱いにしています。

### `$redirect`

```adblock
||example.com/analytics.js$redirect=noopjs
```

対象リクエストをAdGuard側のリソースへ置換します。利用できるリソースや対応製品を公式資料で確認します。

### `$removeparam`

```adblock
||example.com^$removeparam=utm_source
```

クエリパラメータを削除します。ルーティング、認証、決済等に必要なパラメータを巻き込まないよう、対象を限定します。

### `$cookie`

Cookieの制御は認証・設定保持・同意状態へ影響する可能性があります。自分が使う場合はCookie名と役割を確認し、単に「追跡らしい」という推測だけで広く削除しません。

### `$removeheader`

```adblock
||example.com^$removeheader=referer
```

HTTPヘッダーを削除します。CORS、認証、セキュリティ機能へ影響し得るため、自分の通常ルールでは優先度を低くしています。

### `$replace`

レスポンス本文の置換は強力ですが、ブラウザ拡張機能とCoreLibs系製品で対応範囲が異なります。自分が使う場合はHTTPSフィルタリング、対象コンテンツ種別、正規表現の一致範囲を確認します。

### `$csp` / `$permissions`

セキュリティポリシーやPermissions-Policyへ介入します。正規機能を壊したときの原因が分かりにくくなるため、明確な目的と検証条件がある場合だけ比較します。

---

## 3. 優先度・デバッグ用ルール

### `$important`

```adblock
||example.com/ads.js$important
```

優先順位へ大きく影響するため、自分のルールでは「通常の限定ルールで解決できない理由」を確認してから使います。

### `$badfilter`

```adblock
||example.com/ads.js$badfilter
```

既存のネットワークルールを無効化するために使えます。上流側のルールが更新・削除された後は不要になることがあるため、作成理由をコメントで残し、後で見直します。

### `$generichide` / `$specifichide`

コスメティックフィルタによる表示崩れを切り分けるときに確認します。サイト全体を解除する前に、汎用ルールかサイト固有ルールかを分けて調べる用途で使います。

---

## 4. コスメティックルールの確認メモ

### `##` — 標準的な要素非表示

```adblock
example.com##.ad-container
```

自分が最初に検討する形です。ID、意味のある属性、比較的安定したクラスを優先します。

### `:has()`

```adblock
example.com##.article-card:has(> .sponsored-label)
```

子孫要素を条件に親側を選択できます。ブラウザやAdGuardの実装状況を確認し、探索範囲が広くなりすぎないようにします。

### `:contains()`

```adblock
example.com#?#.sponsor:contains(PR)
```

テキストを条件にできますが、言語・表記変更に弱いため、自分のルールでは構造だけで特定できない場合に限定します。

### `:upward()`

```adblock
example.com#?#.ad-text:upward(.ad-container)
```

一致した要素から親方向へ対象を広げます。広い親コンテナを巻き込まないか確認します。

### `:xpath()`

CSSだけで表現しにくい条件を扱えますが、可読性・保守性が下がるため、自分のルールでは他の安定したセレクタで代替できない場合だけ検討します。

### `:matches-css*()` / `:matches-attr()`

計算済みスタイルや属性値を条件にできます。ページ内部実装への依存度が高くなるため、変更に弱いルールとして扱います。

### `:style()`

```adblock
example.com##body:style(overflow: auto !important;)
```

要素を消さず、特定のスタイルだけ調整するときに使います。スクロールロック解除など、目的を限定して使います。

### `:remove()`

DOMから要素を削除します。単純な非表示とはライフサイクルが異なるため、SPAや再描画への影響を確認します。自分の変換処理では、安全に意味を維持できない場合に除外することがあります。

---

## 5. Scriptlet・HTMLフィルタリングの確認メモ

### AdGuard Scriptlet

```adblock
example.com#%#//scriptlet('set-constant', 'exampleFlag', 'false')
```

自分がScriptletを使う場合は、[AdGuard Scriptlets](https://github.com/AdguardTeam/Scriptlets)で名前・引数・対応状況を確認します。uBlock Originの`##+js(...)`を文字列置換だけで移植しません。

Scriptletはサイト側JavaScriptへ介入するため、変数名やデータ構造の変更で壊れやすく、正常な処理へ干渉する可能性があります。CSSや限定的なネットワークルールで解決できない場合の候補として扱います。

### Scriptlet例外

既存のScriptletが原因と確認できた場合は、対応する例外構文を検討します。どのScriptletが原因か確認できない状態で広い例外を追加しません。

### HTMLフィルタリング `$$`

DOM構築前のHTMLへ介入できる製品・環境があります。強力ですが、対応製品が限られ、ページ構造そのものを壊す可能性があります。ブラウザ拡張機能 MV3とAdGuard for Androidを同一扱いしません。

### CSS注入 `#$#` / `#$?#`

スタイルを注入する用途です。単に要素を隠すだけなら、まず`##`または必要に応じて`#?#`を検討します。

---

## 6. 自分がルールを確認するときの順序

1. 対象URLと使用製品を固定する。
2. Filtering log / Networkで実際の通信や適用ルールを確認する。
3. DOM側の問題なら対象要素と周辺HTMLを確認する。
4. 標準CSSまたは限定的なネットワークルールで解決できるか確認する。
5. Extended CSS、Scriptlet、レスポンス改変などは必要性がある場合だけ検討する。
6. 変更後は対象だけでなく、ログイン、検索、再生、スクロール、決済等の正常系も確認する。
7. 一時的な例外・`$badfilter`は後で不要になっていないか見直す。

---

## 7. 参照する一次情報

- [AdGuard — How to create your own ad filters](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard Filters](https://github.com/AdguardTeam/AdguardFilters)
- [AdGuard Scriptlets](https://github.com/AdguardTeam/Scriptlets)
- [AdGuard Browser Extension](https://github.com/AdguardTeam/AdguardBrowserExtension)
- [AdGuard for Android](https://github.com/AdguardTeam/AdguardForAndroid)
- [uBlock Origin — Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [uBlock Origin uAssets](https://github.com/uBlockOrigin/uAssets)
- [EasyList](https://github.com/easylist/easylist)
- [Chrome — declarativeNetRequest API](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest)

このメモ内の要約より、使用時点の公式仕様と実際のログを優先します。
