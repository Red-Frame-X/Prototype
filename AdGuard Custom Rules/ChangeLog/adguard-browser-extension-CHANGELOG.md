# AdGuardブラウザ拡張機能

このプロジェクトへの通知変更は、このファイルで行われます。

フォーマットはに基づいています[Changelog をキープ](https://keepachangelog.com/en/1.0.0/),
このプロジェクトは、[セマンティック・バージョン](https://semver.org/spec/v2.0.0.html).

## [5.5] - 2026-08-17

### 追加

- `$urltransform`修飾子サポート [tsurlfilter#111].
- `$removeparam`SPA ナビゲーション [tsurlfilter#188] のサポート
- MV2でフィルタルール変換エラーロギング。
- デフォルト登録スクリプトはローカルスクリプト規則[tsurlfilter#167]に常に追加されます。
- 専用のリストとエディタビューを備えた新しいルールエディタ。

### 変更点

- 移行された宣言的なネットワークルール変換から
  `@adguard/tsurlfilter/es/declarative-converter`専用に
  `@adguard/dnr-converter`パッケージ。
- 内部を一直線に並べる`RuleSet`/`ruleSet`識別子`Ruleset`/`ruleset`マッチする
リンクされたライブラリの名前を変更しました。`@adguard/dnr-converter`, `@adguard/tswebextension`).
- ログをフィルタリングすると、`declarativeRuleInfo.sourceRules`複数の
前の値を上書きするのではなく、同じイベントの DNR マッチ。
- サインイン`RuleActionType`PascalCase への enum ケーシング (`BLOCK` → `Block`等)への
マッチする`@adguard/dnr-converter`API です。
- MV3 のユーザルールのエラー報告では、動的ルール変換エラーが記録されます。
- [@adguard/agtree] を v4.2.0 に更新しました。
- [@adguard/dnr-converter] を v1.1.0 に更新しました。
- [@adguard/rules-editor] を v2.0.0 に更新しました。
- [@adguard/scriptlets] を v2.5.0 に更新しました。
- [@adguard/tsurlfilter] を v6.0.2 に更新しました。
- [@adguard/tswebextension] を v5.0.0 に更新しました。
- [@adguard/extended-css] を v2.2.0 に更新しました([@adguard/tswebextension])。

### 固定式

- MV3 [#3537]の高速ページリロードで適用されない要素の隠れる規則。
- ログをフィルタリングするとイベントが失われる`window.open()`タブリダイレクト [#2701].
- 閉じたタブのログイベントのフィルタリング`$popup`修飾ルールが表示されるようになりました
背景ページへのリンク [#1686].
- CSS ルールを含む「広告フィルタの使用状況を送信します」オプション`::before`または`::after`
[#1486] ページに表示されたコンテンツを引き起こします。
- WebRTC IPハンドリングポリシーが変更されました`disable_non_proxied_udp`お問い合わせ
  `default_public_interface_only`まだVoIPの破損を減らすため
IP漏洩を防ぐ
- DNR変換でワイルドカードTLDドメインを拡大`$domain`そして、`$to`
修飾子 [tsurlfilter#189].
- comma-containing 引数の Scriptlet 例外ルールは正しく機能します
  ([#3533]).
- 一般的なスクリプトレットルール(ドメイン制限なしのスクリプト)が表示されるようになりました
フィルタリングログ [#2895].
- OS 高コントラストモードでUI制御の可視性を改善
  (`forced-colors: active`):スイッチ、アクションボタン、エディタ、ドロップダウン、
オプション/ポップアップページ ([#3530]) のカードとモダラのようなカード。
- Firefox は Douyin 動画を再生するときに凍結します。, カスタムフィルタルール all.txt によってトリガー [#3525].
- AdGuardの拡張機能が有効になったときにFirefox 118でサイトの読み込みが遅い [#2524].
- フィルタリングログで欠落しているバーをスクロール [#3558].
- Allowlistエディタは、ベアコンパウンドパブリックサフィックス(例:)を受け入れます。`gov.br`,
  `co.uk`, `com.au`) シングルラベル TLD をまだ拒否しながら [#3587].
- 延長をインポートする際に追加リクエストの許可を求めることはありません
設定 [#2754].
- Monkeytype.com は読み込みに失敗します。 — AdGuard MV2 で "Pending" をスタックするリクエストは [#3565] を有効にしました。
- 正規表現による化粧品規則`$domain`複数のエスケープを含む修飾子
分離器(例)`[$domain=/example\d*\.(live\|com\|icu\|org)$/]##body`) なし
応用されている。
- ポップアップ統計「年」タブは、最後の3ヶ月しか表示され、古い消去
月間ロールオーバー後の月間履歴。

[5.5]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.4.3.0...v5.5.0.6
[#3537]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3537
[#1486]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/1486
[#1686]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/1686
[#2701]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2701
[#2754]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2754
[#2895]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2895
[#3533]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3533
[#3530]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3530
[#2524]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2524
[#3525]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3525
[#3558]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3558
[#3565]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3565
[#3587]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3587
[tsurlfilter#111]: https://github.com/AdguardTeam/tsurlfilter/issues/111
[tsurlfilter#167]: https://github.com/AdguardTeam/tsurlfilter/issues/167
[tsurlfilter#188]: https://github.com/AdguardTeam/tsurlfilter/issues/188
[tsurlfilter#189]: https://github.com/AdguardTeam/tsurlfilter/issues/189

## [5.4 パッチ 2] - 2026-05-14

### 固定式

- comma-containingセレクタのFalse-negative CSSセレクター検証
  (e.g., `IMG[alt="Reklama"], .l-box--99.l-box > .text-center`)。 ブラウザの
  `CSS.supports('selector(A, B)')`トップレベルのコンマで失敗します。 バリデータは現在
これらのセレクタを分割し、各パートを個別に検証します。

[5.4 patch 2]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.4.2.0...v5.4.3.0

## [5.4 パッチ 1] - 2026-05-08

### 固定式

- 共有URLからの設定をインポートしても[#3517]は動作しません。

[5.4 patch 1]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.4.1.3...v5.4.2.0
[#3517]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3517

## [5.4] - 2026-05-07

### 追加

- 問題報告でバージョンにベータサフィックスを追加しました [#3330].
- 特定プレンダーリクエストの処理
- 許可リストを反転するための確認モーダル。
- MV3のカスタムフィルタの独立した更新
延長更新の可用性を待つことなく[#2944].
- 「検索ページの結果へのアクセスを許可」権限が付与されていない場合は、オペラの警告通知 [#2485].
- インポート設定から`adguard:import_user_configuration`Report.adguard.comへのリンク。
- HTTP の使用`Last-Modified`カスタムフィルタ更新タイムスタンプのフォールバックとしてヘッダー
いつか`TimeUpdated`メタデータは欠落しています [#3407].
- `ROList`MV3のフィルタリスト [#3473].
- 一般ページの設定ボタンをシェアします。

### 変更点

- 発行報告URLがv4スキームに更新:コンマ区切りフィルタID、ステルス値
として`1`/`0`, `ext.manifest_version`変数、normalizedブラウザの名前、ISO 8601
タイムスタンプ`filters_last_update`、カスタムフィルタにはタイトルとURLが含まれます。
- Cookie 自己破壊ステルス パラム (Cookie self-destruct)`stealth.third_party_cookies_min`,
  `stealth.first_party_cookies_min`) は、問題のレポート URL で MV2 だけになりました (not)
MV3対応
- [@adguard/agtree] を v4.1.1 に更新しました。
- [@adguard/dnr-rulesets] を v4.2.1 に更新しました。
- [@adguard/filters-downloader] を v2.4.4 に更新しました。
- [@adguard/scriptlets] を v2.4.2 に更新しました。
- [@adguard/tsurlfilter] を v5.0.1 に更新しました。
- [@adguard/tswebextension] を v4.1.1 に更新しました。

### 固定式

- ポップアップを開くときにインジケータ矢印フリッカーを更新 [#3351].
- $badfilter は異なる $denyallow 値 [#3428] でルールを正しく無視します。
- ログウィンドウのサイズ/pos をズームで復元しない [#3255] をフィルタリングします。
- 検索結果[#3414]に正しく表示されないページをブロックします。
- Allowlist エディタは URL からドメインを抽出することでエントリを正規化します。そのため、プロトコル、パス、またはスラッシュの追跡は正しく機能します [#3430]。
- 要素の隠れる規則の無効なCSSセレクターの使用は、すべての注入されたスタイル[#3329]に影響を与えます。
- 「第三者からの名誉を隠す」ステルスオプションは、スラッシュ[#3393]を追跡して正しいレフリーラー値を設定します。
- `$removeparam`複数の規則がMV3 [#3444]の同じURLに一致したときに、すべての追跡パラメータを除去しないルール。
- 「広告マニュアルのブロック」は更新の前に開いたタブで動作しません[#3452]。
- ブラウザ[#3280]を起動すると、拡張はフィルタを更新しません。
- クロスドメインのiframeでブロックされたリクエストは、拡張子バッジ[#3446]でカウントされていない。
- カスタムフィルタサブスクリプションは、フィルタリスト[#3501]の代わりにHTMLページを返すURLを受け入れます。

[5.4]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.3.1.7...v5.4.1.3
[#2485]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2485
[#2944]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2944
[#3255]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3255
[#3280]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3280
[#3329]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3329
[#3330]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3330
[#3351]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3351
[#3393]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3393
[#3407]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3407
[#3414]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3414
[#3428]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3428
[#3430]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3430
[#3444]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3444
[#3446]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3446
[#3452]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3452
[#3473]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3473
[#3501]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3501

## [5.3 パッチ 1] - 2026-03-30

### 追加

- Opera MV3拡張サポート

### 固定式

- チャートの列を上回るときに統計ツールチップが間違った位置に表示されます [#3449].
- エクステンション起動時にフリーズ [#3400].

### 変更点

- [@adguard/agtree] を v4.0.1 に更新しました。
- [@adguard/scriptlets] を v2.2.16 に更新しました。
- [@adguard/tsurlfilter] を v4.0.2 に更新しました。
- [@adguard/tswebextension] を v4.0.2 に更新しました。

[5.3 patch 1]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.3.0.8...v5.3.1.7
[#3449]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3449
[#3400]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3400

## [5.3.0.8] - 2026-02-10

### 追加

- 改善された可読性のためのJSONをエクスポートする美化[#3069].
- [#3148] を有効にしたときに、サイズ制限なしでログレコードをフィルタリングし続ける機能。
- サポート`:has()`標準CSSとして擬似クラス 条件付き:
    - セレクタに他の拡張擬似クラスがない場合、または
    - もし`#?#`分離器は規則[#2587]で明示的に使用されます。
- HTML フィルタリングルール [tsurlfilter#96] でフル CSS セレクタの構文をサポート。

### 変更点

- 改善されたフィルター更新ログの可読性, 更新前後のバージョン情報を追加 [#2934].
- トラッキング保護(MV2)の機能名と説明を改善しました。
- [@adguard/tsurlfilter] を v4.0.0 に更新しました。
- [@adguard/tswebextension] を v4.0.0 に更新しました。
- [@adguard/agtree] を v4.0.0 に更新しました。
- [@adguard/scriptlets] を v2.2.15 に更新しました。
- [@adguard/dnr-rulesets] を v4.0 に更新しました。
- ルールテキスト検索を最適化することにより、ログのパフォーマンスをフィルタリングする改善を行いました。

### 固定式

- 動的ルールは重複通知を制限します。
- ネットワークルール`$important`保護を無効にしても修飾子が適用されます[#3227]。
- アクティブユーザー規則/アローリスト保存時に再活性化と欠落した出口プロンプトを保存 [#3151].
- Allowlist [#3193] にウェブサイトが追加されていないにもかかわらず、一部のリクエストは 'Inverted allowlist' モードでブロックされます。
- 設定のインポートにフィルターを有効にしないでください`enabled-filters`空 [#3136] です。
- 設定は、実際に[#3278]が適用されます。
- ログを保存すると、フィルタリングログ[#3148]内のすべてのレコードを保持しません。
- 保護が延長でpausedときMV3でまた保護を禁止します。
- 特定の例外規則が[#3262]を提示しても$documentブロックルールを適用します。
- ブロックされたiframeはFirefox [#3116] ではブロックされません。
- 拡張は予期しないエラーが発生しました`[::]:8000` [#3360].
- ユーザルールフルスクリーンモードでは動作しません [#3365]。
- ルールが変換されると、ログをフィルタリングする際に、元のルールテキストが正しく表示されます。

[5.3.0.8]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.3.0.8
[#2934]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2934
[#3069]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3069
[#3116]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3116
[#3136]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3136
[#3148]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3148
[#3151]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3151
[#3193]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3193
[#3227]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3227
[#3262]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3262
[#3278]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3278
[#3360]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3360
[#3365]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3365
[tsurlfilter#96]: https://github.com/AdguardTeam/tsurlfilter/issues/96

## [5.2.800] - 2025-12-25

### 固定式

- タブのコンテキスト[#2594]にデータURLのファビコンを保存することにより、メモリリークが発生します。

[5.2.800]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.800%2B1.build.20251216080045

## [5.2.600.3] - 2025-12-16

### 固定式

- Firefox 用のクリップボード権限を生成し、ユーザールールと許可エディタで必要なときに表示されるプロンプト [#3364]
- ブラウザ 360 [#3058] では拡張子が動作しません。

[5.2.600.3]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.600%2B3.build.20251209190042
[#3364]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3364
[#3058]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3058

## [5.2.500] - 2025-12-05

### 固定式

- 更新promoの旗は主張のunmissalをし、の後で再度示しません
拡張子の更新 [#3385].

### 変更点

- [@adguard/agtree] を v3.3.1 に更新しました。
- [@adguard/assistant] を v4.3.77 に更新しました。
- [@adguard/scriptlets] を v2.2.13 に更新しました。
- [@adguard/tsurlfilter] を v3.5.1 に更新しました。
- [@adguard/tswebextension] を v3.2.16 に更新しました。

[5.2.500]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.500%2B0.build.20251127140045
[#3385]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3385

## [5.2.400] - 2025-11-24

### 追加

- 拡張ポップアップ用の新しいロードアイコンとアニメーション。
- MV3 [#3016] でカスタムフィルタを更新する機能を追加します。

### 変更点

- アップデートが利用可能でブラウザの場合、MV3で自動更新を適用します
しばらくの間アイドルになった。

[5.2.400]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.400%2B0.build.20251119090043
[#3016]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3016

## [5.2.113.0]

### 固定式

- クリップボードの許可を削除します。 [#3362].

[5.2.113.0]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/5.2.113%2B0.build.20251022090039
[#3362]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3362

## [5.2.112.84] - 2025-10-25

### 変更点

- [@adguard/tswebextension] を v3.2.13 に更新しました。

[5.2.112.84]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.112%2B84.build.20251022090039

## [5.2.112.1] - 2025-10-14

### 固定式

- 拡張子はポップアップ[#3317]を介して更新できませんでした。

[5.2.112.1]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.112%2B1.build.20251009120050
[#3317]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3317

## [5.2.112.0] - 2025-10-13

### 変更点

- 新しい4桁のビルドバージョン作成スキーム:`major.minor.patch+buildTag`. `buildTag`
すべてのビルドで増やされます。

### 固定式

- MV3 の拡張更新のフェッチ応答サイズを最小化します。

[5.2.112.0]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.112%2B0.build.20251001190036

## [5.2.77] - 2025-09-22

### 追加

- MV3でより信頼性の高いスクリプトインジェクションを可能にするChromeのユーザースクリプトAPIのサポート。
- ユーザースクリプト API の使用により、カスタムフィルタのサポートが再びバックアップされます。
- 問題報告中に最後のフィルターの更新時間を[#3055]に送信します。
- 押すことによってエディタを終了する能力`Escape`キーボードボタン [#2333].
- ブロックされたリクエストのページのブロック`$document`MV3のルール
- 互換性`$header`修飾子と`$match-case`
そして、`$third-party`MV2の修飾子 [#2942].
- `zip`そして、`crx`拡張ビルド用のアーティファクト [#3163], [#2488].
- MV3 でフィルタを手動で更新する機能。

### 変更点

- Safebrowsing の MV2 拡張およびブロックされた web ページのための MV2 拡張のブロックのページを更新しました`$document`ルール。
- 視覚障がい者(#3035)、【#2315】、【#2332】のアクセシビリティの向上
- 「とにかく進む」をクリックすることによって引き起こされる一時的な例外の期間を減少させる
40分から10秒までのブロックページで [#3263].
- [@adguard/agtree] を v3.2.3 に更新しました。
- [@adguard/assistant] を v4.3.75 に更新しました。
- [@adguard/dnr-rulesets] を v3.2.0 に更新しました。
- [@adguard/filters-downloader] を v2.4.2 に更新しました。
- [@adguard/logger] を v2.0.0 に更新しました。
- [@adguard/scriptlets] を v2.2.10 に更新しました。
- [@adguard/tsurlfilter] を v3.4.6 に更新しました。
- [@adguard/tswebextension] を v3.2.11 に更新しました。

### 削除

- AdGuard DNS フィルタと AdGuard Annoyances フィルタを非推奨として保護します。

### 固定式

- ユーザルール[#3145]を保存したときに、カーソルは最後に移動します。
- Windows用のFirefoxでフィルタリングログを最大化できません[#2464]。
- Android [#3061] のユーザルール入力欄にテキストを貼り付けることができません。
- 無効な HTML ルールセレクターは、サイト読み込み [#2646], [#2826] を中断しています。
- ステルスモードの`Hide Referer from third parties`オプションは、いくつかのウェブサイトを破る可能性があります [#2839].
- フィルタリングログ: 適切なパネルをリサイズすると、そのコンテンツ [#2305] を選択します。
- ブロックされたリクエストの種類はポップアップ(Android用Firefox)[#3157]に表示されません。
- "Statistics" タブに切り替えると、"Actions" と "Statistics" ボタン (Edge for Android) [#3158] がシフトされます。
- ログをろ過して下さい: ローディングのとき要求の細部のパネルは自動的に閉鎖されます
別のウィンドウ/タブ [#2327] にあるウェブサイト。
- スクリプトルールは、フィルタリングログ[#3164]に表示されません。
- Edge の分割画面のフィルタリングは [#2832] では動作しません。
- 総ブロックされたポップアップ文字列は誤って翻訳 [#3204].
- `$replace`ルールは、いくつかのウェブサイトを破る可能性があります [#3122].
- ファイルサイズ制限を10MBまで増やす`$replace`Firefoxのルール [#3192].
- HTML フィルタリングルール [tsurlfilter#147] のセレクターで値なしで属性を指定できます。
- AdGuardのドイツ フィルターの記述のスペースを欠いて下さい`de`ロケール [#3216].
- MV2 [#3230] の行に複数のパッチを適用したときに OOM エラーが発生することがあります。
- Firefoxのブラウザ起動時の拡張初期化 [#3189].
- ブロックされたページでは、間違ったルールが表示されます。`$document`MV3のルール [#3260].
- オプションページの通知テキストをオーバーフローします。

[5.2.77]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.2.77
[#2305]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2305
[#2315]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2315
[#2327]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2327
[#2332]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2332
[#2333]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2333
[#2464]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2464
[#2488]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2488
[#2646]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2646
[#2826]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2826
[#2832]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2832
[#2839]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2839
[#2942]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2942
[#3035]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3035
[#3055]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3055
[#3061]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3061
[#3122]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3122
[#3145]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3145
[#3157]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3157
[#3158]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3158
[#3163]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3163
[#3164]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3164
[#3189]: https://github.com/AdguardTeam/AdguardBrowserExtension/pull/3189
[#3192]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3192
[#3204]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3204
[#3216]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3216
[#3260]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3260
[#3263]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3263
[tsurlfilter#147]: https://github.com/AdguardTeam/tsurlfilter/issues/147

## [5.1.102] - 2025-06-15

### 変更点

- [@adguard/filters-downloader] を v2.4.1 に更新しました。

## 固定式

- MV2 [#3230] の行に複数のパッチを適用したときに OOM エラーが発生することがあります。

[5.1.102]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.94...v5.1.102
[#3230]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3230

## [5.1.94] - 2025-05-29

### 変更点

- [@adguard/agtree] を v3.2.0 に更新しました。
- [@adguard/tsurlfilter] を v3.3.3 に更新しました。
- [@adguard/tswebextension] を v3.1.0-alpha.3 に更新しました。

[5.1.94]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.88...v5.1.94

## [5.1.88] - 2025-05-23

### 変更点

- [@adguard/agtree] を v3.1.3 に更新しました。
- [@adguard/dnr-rulesets] を v3.0.0-alpha.3 に更新しました。
- [@adguard/tsurlfilter] を v3.3.1 に更新しました。
- [@adguard/tswebextension] を v3.1.0-alpha.1 に更新しました。

[5.1.88]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.79...v5.1.88

## [5.1.79] - 2025-04-28

### 変更点

- [@adguard/tsurlfilter] を v3.2.3 に更新しました。
- [@adguard/tswebextension] を v3.0.2 に更新しました。

[5.1.79]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.70...v5.1.79

## [5.1.70] - 2025-03-19

### 固定式

- Android Edge のポップアップサイズの問題。

[5.1.70]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.68...v5.1.70

## [5.1.68] - 2025-03-07

### 変更点

- [@adguard/scriptlets] を v2.1.6 に更新しました。
- [@adguard/tsurlfilter] を v3.2.1 に更新しました。
- [@adguard/tswebextension] を v3.0.1 に更新しました。

[5.1.68]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.1.62...v5.1.68

## [5.1.62] - 2025-02-28

### 追加

- 値5000でMV3の安全でない動的ルール制限。
- dnr-rulesets バージョンを [#3054] タブで表示します。
- フィルタリングログ[#3028]のドメインでタブを検索する機能。
- Googleドライブ[#2908]からフィルタを追加する機能。

### 変更点

- サポートされている最小限のChromiumベースのMV2ブラウザバージョンが106以上になりました。
プレンダーリクエスト。
- MV3 の 30000 にすべての動的ルールを制限します。
- ネットワークルールに空の修飾子リストをスローするエラー。
- MV3拡張子専用のルールセットファイルでフィルタデータを保存
規則のみが変更される更新を許可します。
- [@adguard/agtree] を v3.0.1 に更新しました。
- [@adguard/scriptlets] を v2.1.5 に更新しました。
- [@adguard/tsurlfilter] を v3.2.0 に更新しました。
- [@adguard/tswebextension] を v3.0.0 に更新しました。

### 固定式

- 許可されたタブが許可された [#3020] [#3048] としてタブ内のすべての次のウェブサイトを検討したら。
- 特定のノードのdeserializerに欠けている子供データを処理します。
- 無効なフィルタリストからのルールは、別の規則[#3002]を無効にします。
- クロームの制限[#3004]のためにルールが適用されていないユーザーを通知します。
- URIエンコード`$removeparam`MV3 [#3014] では値が削除されません。
- に注入する化粧品の規則`about:blank`MV2のiframes。
- 短縮名翻訳`pt_BR`ロケール [#3075].
- フィルタリングログ[#2950]にステルスルールが表示されない
- `$removeparam`正しくエンコードされた URL [#3076] からパラメーターを削除します。
- エンジンアップデートの拡張アイコンを更新します。
- 終了ルールは、MV3の拡張アイコンの警告の更新を制限します。
- 他のタブ [#3050] からブロックされたリクエストのポップアップ更新のカウンターをブロックしました。
- `$popup,third-party`修飾子は [#3012] をブロックする文書を引き起こします。
- カスタムフィルタ[#3057]を追加すると、 absent メタデータの行を表示しないでください。
- ログのフィルタリングは、タブの変更、開口部、閉鎖を観察しません。
- スクリプトとスクリプトは、MV2 [#2855] でウェブサイトのリロードやナビゲーションに遅すぎると実行されます。
- MV3のアシスタントフレームに化粧品ルールを注入しないでください。

### 削除

- ストレージクラスは、彼らが移動していたので、`@adguard/tswebextension`パッケージ。

[5.1.62]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.0.188...v5.1.62
[#2855]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2855
[#2908]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2908
[#2950]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2950
[#3002]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3002
[#3004]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3004
[#3012]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3012
[#3014]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3014
[#3020]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3020
[#3028]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3028
[#3048]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3048
[#3050]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3050
[#3054]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3054
[#3057]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3057
[#3075]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3075
[#3076]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3076

## [5.0.188] - 2025-02-05

### 変更点

- スクリプトルールは、既定のフィルタからのみに限定されません。
- v2.4.0-alpha.11に[@adguard/tswebextension]を更新しました。

### 削除

- AdGuardクイックフィックスフィルタ。
- カスタムフィルタは一時的に使用できません。

[5.0.188]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.188

## [5.0.185] - 2025-01-22

### 追加

- AdGuard クイックフィックスフィルターが返されます。

### 変更点

- Scriptlet ルールは、既定のフィルターからのみ利用できます。
- [@adguard/tswebextension] を v2.4.0-alpha.10 に更新しました。

### 削除

- リモートでホストされているスクリプトの注入。

[5.0.185]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.185

## [5.0.183] - 2025-01-14

### 削除

- AdGuardクイックフィックスフィルタ。
- 拡張インストールのメタデータ更新をフィルタリングします。

[5.0.183]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.183

## [5.0.178] - 2024-12-24

### 変更点

- MV3 で JS 規則の注入を作った:
    - 使用方法`chrome.scripting`ビルド済みのフィルタからスクリプトルールの関数を注入するための API、
    - スクリプトのタグのインジェクションは、ユーザーによって手動で追加されるスクリプトルールのみを使用する —
*ユーザールール*と*カスタムフィルタ*からのルール。
- v2.4.0-alpha.8に[@adguard/tswebextension]を更新しました。

### 削除

- 新たな実行能力`AG_`MV3 の *User ルール* と *Custom フィルタ* からのスクリプトルール。

[5.0.178]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.178

## [4.4.48] - 2024-11-25

### 追加

- お問い合わせ`manifest_version`MV2に関する問題報告

### 変更点

- [@adguard/agtree] を v2.1.3 に更新しました。
- [@adguard/tsurlfilter] を v3.0.7 に更新しました。
- [@adguard/tswebextension] を v2.0.7 に更新しました。

### 固定式

- uBlock フィルタ パラメータ [#2962] の解析の最適化された性能。
- `$removeparam`MV2 [#3015] でエンコードされた URL パラメータと一致しない。
- 同じページの複数のスクリプトの注入によって引き起こされる記憶漏出
Firefox でイベントページが MV2 [#2594] で再起動した後。

[4.4.48]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.4.41...v4.4.48
[#2962]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2962
[#3015]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3015

## [5.0.170] - 2024-10-30

### 変更点

- v2.4.0-alpha.7に[@adguard/tswebextension]を更新しました。

### 固定式

- 同じページの複数のスクリプトの注入によって引き起こされる記憶漏出
MV3 [#2594] でサービスワーカーまたはイベントページを再起動した後。

[5.0.170]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.170
[#2594]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2594

## [5.0.162] - 2024-10-30

### 追加

- お問い合わせ`manifest_version`MV3に関する問題報告

[5.0.162]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.162

## [5.0.159] - 2024-10-23

### 変更点

- [@adguard/logger] を v1.1.1 に更新しました。
- [@adguard/tsurlfilter] を v3.1.0-alpha.7 に更新しました。
- [@adguard/tswebextension] を v2.4.0-alpha.6 に更新しました。

### 固定式

- 正しい輸入の`EXTENDED_CSS_VERSION`.
- タイプのリクエストを除き、ドキュメントブロック [#2992] を引き起こします。
- 単一の選択`$permissions`ログイベントのフィルタリングは、すべて選択します`$permissions`イベント

[5.0.159]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.159
[#2992]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2992

## [4.4.39] - 2024-10-21

### 変更点

- [@adguard/logger] を v1.1.1 に更新しました。
- [@adguard/tswebextension] を v2.0.4 に更新しました。

### 固定式

- ユーザルールのスキャンは、拡張ポップアップ [#2989] を破棄します。
- 単一の選択`$permissions`ログイベントのフィルタリングは、すべて選択します`$permissions`イベント

[4.4.39]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.4.30...v4.4.39
[#2989]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2989

## [5.0.138] - 2024-10-10

### 変更点

- [@adguard/logger] を v1.1.0 に更新しました。
- [@adguard/tsurlfilter] を v3.1.0-alpha.6 に更新しました。
- v2.4.0-alpha.3に[@adguard/tswebextension]を更新しました。

### 固定式

- MV3 拡張子が [#2985] をインストールすると、Edge ブラウザーで MV3 固有のフィルタを使用します。
- MS Edge [#2963] に AdGuard クイックフィックス フィルターを追加できません。
- 化粧品規則は時々適用されませんまたは間違ったドメイン[#2984]にも適用されません。
- JS ルールは、一部のウェブサイト [#2980] で Trusted Types によってブロックされます。
- MV3拡張子は、以下の規則を適用することはできません:blank iframes [#2975].
- スクリプトロギングは[#2977]は動作しません。
- コンテンツタイプのマッチング`$permissions`そして、`$removeparam`ルール [#2954].

[5.0.138]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.138
[#2985]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2985
[#2984]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2984
[#2980]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2980
[#2975]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2975
[#2977]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2977
[#2963]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2963
[#2954]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2954

## [5.0.128] - 2024-10-04

### 変更点

- [@adguard/scriptlets] を v1.12.1 に更新しました。
- [@adguard/tsurlfilter] を v3.1.0-alpha.5 に更新しました。
- [@adguard/tswebextension] を v2.3.0-alpha.1 に更新しました。

[5.0.128]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.128

## [4.4.30] - 2024-10-02

### 変更点

- [@adguard/agtree] を v2.1.2 に更新しました。
- [@adguard/logger]をv1.0.2に更新しました。
- [@adguard/scriptlets] を v1.12.1 に更新しました。
- [@adguard/tsurlfilter] を v3.0.5 に更新しました。
- [@adguard/tswebextension] を v2.0.3 に更新しました。

### 固定式

- 例外`$domain=~`フィルタルールは正しく機能しない [#2912].
- Scriptlets exclusion の一致は、引数 [#2947] のルールでは正しく機能しません。

[4.4.30]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.4.22...v4.4.30
[#2912]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2912
[#2947]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2947

## [5.0.112] - 2024-09-27

### 変更点

- 検索クエリを隠すための保護を追跡する無効なオプション [#2969].

[5.0.112]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.112
[#2969]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2969

## [5.0.97] - 2024-09-23

### 固定式

- カスタムグループが無効になっている場合でも、カスタムフィルタの一覧がReportWebAppに渡されます[#2951]。
- 動的ルール ID [#2953] の交差点で動作を停止します。

[5.0.97]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.97
<!--TODO: v5.0 ブランチをマスターにマージした後に URL を変更する価値 -->
<!-- [5.0.97]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v5.0.91...v5.0.97 -->
[#2951]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2951
[#2953]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2953

## [5.0.91] - 2024-09-19

拡張子はMV3と完全に互換性があります。

[5.0.91]: https://github.com/AdguardTeam/AdguardBrowserExtension/releases/tag/v5.0.91

## [4.4.22] - 2024-08-30

### 変更点

- [@adguard/tsurlfilter] を v3.0.1 に更新しました。
- [@adguard/tswebextension] を v2.0.1 に更新しました。
- [@adguard/scriptlets] を v1.11.16 に更新しました。

### 固定式

- 負のドメイン`$to`修飾子は期待どおりに動作しません [#2910].
- [#2913] をリダイレクトする代わりに、Spotify プレーヤーで規則ブロックリクエストをリダイレクトします。

[4.4.22]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.4.18...v4.4.22
[#2910]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2910
[#2913]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2913

## [4.4.18] - 2024-08-19

### 追加

- `HybridStorage`フォールバックでインデックス化されたDB経由でデータを格納する`chrome.storage.local`.
- Syntax のハイライト`$permissions`規則エディタの修飾子。
- [@adguard/agtree] ルールツリーと連携

### 変更点

- エクスポートされた設定ファイル名は、他のAdGuard製品[#2607]と一致させるために標準化された方法で作成します。
- フィルターリストは前処理されたフォーマットで保存され、エンジンがより効率的に始動させます、
エンジンはルールを変換または解析する必要はありません。
- [@adguard/tswebextension] を v2.0.0 に更新しました。
- [@adguard/tsurlfilter] を v3.0.0 に更新しました。
- [@adguard/scriptlets] を v1.11.6 に更新しました。

### 固定式

- ヤンデックスマップ(#2519)をナビゲートすると、ログのフィルタリングがリフレッシュされます。
- ログのフィルタリングは、`history.replaceState` [#2598].
- スタイルフィルタは適用されますが、スクリプトレットフィルタはFirefox [#2782] ではありません。
- [#2793] を報告するときにカスタムフィルタに関する情報を欠く。
- [#2818] を有効にすると、一部のフィルタは更新されません。
- 表示された通知を設定することはできません。
- 開いたときに背景ページのコンソールエラー`chrome://new-tab-page/`.
- `$permissions`フィルタリングログにルールが表示されません。
- タブ変更時に拡張機能のアクションアイコンが点滅します。
- フィルター自動更新はさっぱりしない`last updated date`フィールド [#2726].
- タブ変更時に拡張機能のアクションアイコンが点滅します。

[4.4.18]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.64...v4.4.18
[#2519]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2519
[#2598]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2598
[#2607]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2607
[#2726]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2726
[#2782]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2782
[#2793]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2793
[#2818]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2818

## [4.3.64] - 2024-07-10

### 固定式

- Firefox Nightly [#2817] でポップアップメニューが開きます。

[4.3.64]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.53...v4.3.64
[#2817]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2817

## [4.3.53]

### 変更点

- [@adguard/tswebextension] を v1.0.24 に更新しました。

### 固定式

- Cookie ドメインがリクエスト URL [#2683] と一致した場合、Cookie 設定中にエラーを投げないでください。
- スクリプトルールは、CSP [#1733] による Firefox では適用されません。

[4.3.53]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.46...v4.3.53
[#2683]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2683
[#1733]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/1733

## [4.3.46] - 2024-04-08

### 追加

- ログインメッセージの[@adguard/logger]

### 変更点

- 未加工フィルターは文字列として保存されます。
- [@adguard/filters-downloader] を v2.2.0 に更新しました。
- [@adguard/tsurlfilter] を v2.2.18 に更新しました。
- [@adguard/tswebextension] を v1.0.22 に更新しました。
- [@adguard/scriptlets] を v1.10.25 に更新しました。

### 固定式

- インストールプロセスは、filter.js が到達不可能な場合は停止します [#2761]。
- 最後の更新中にいくつかの致命的なエラーが発生した場合は、次のフルアップデートまでdiffの更新をフェッチしないでください[#2717]。
- ダウンロード後にフィルターチェックサムをチェック [#2681].
- アシスタント iframe スタイルは、ウェブサイト [#1848] に固有の化粧品規則の影響を受けます。
- 修飾子の適用`$popup`そして、`$all` [#2620], [#2728].
- 推奨フィルタを更新し、フィルタと局所検出のグループを有効にします [#2714].

[4.3.46]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.35...v4.3.46
[#2761]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2761
[#2717]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2717
[#2714]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2714
[#2681]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2681
[#1848]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/1848

## [4.3.35] - 2024-03-28

### 固定式

- ベータ [#2682] でリリースノートにつながる通知を更新します。
- 設定[#2735]をインポートすると、フィルタはプリインストールされたものに戻ります。

[4.3.35]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.31...v4.3.35
[#2682]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2682
[#2735]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2735

## [4.3.31] - 2024-03-11

### 変更点

- 一度にdiffの更新をチェックしてください。
- [@adguard/tswebextension] を v1.0.16 に更新しました。
- [@adguard/tsurlfilter] を v2.2.15 に更新しました。
- [@adguard/scriptlets] を v1.10.1 に更新しました。

### 固定式

- フィルタールールからパースされたタグでメモリリーク。
- 申し込み`$all`修飾子ルール [#2620].
- 設定は非常に最初の試み[#2712]で開くことができません。
- すべてのグループとフィルタは、インストール後に無効になっています [#2713].
- モーダルを追加するカスタムフィルタ [#2715].
- お問い合わせ`stealth.block_trackers`問題報告中 [#2721].
- `$popup`修飾子は、他の種類のリソースをブロック [#2723].
- `$popup`単純なブロックルール[#2728]を無効にしないでください。

[4.3.31]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.13...v4.3.31
[#2620]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2620
[#2712]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2712
[#2713]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2713
[#2715]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2715
[#2721]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2721
[#2723]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2723
[#2728]: https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2728

## [4.3.14] - 2024-06-02

### 固定式

- 化粧品のルールはオペラで動作しません[#2704](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2704)そして、[#2705](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2705).

## [4.3.13] - 2024-01-30

### 追加

- Edge と Opera dev のビルドを追加しました。
- 危険なルールの検出

### 固定式

- すべてのカスタムフィルタを表示していません[#2693](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2693).

## [4.3.10] - 2024-01-20

### 固定式

- 自動フィルタの更新は、モバイルブラウザで動作しません[#2423](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2423).

## 変更点

- [@adguard/filters-downloader] を v2.0.7 に更新しました。

## [4.3.4] - 2024-01-16

### 追加

- 迷惑なフィルターを有効にして、ユーザーの同意を得ること。

### 固定式

- サポートされている最小バージョンの互換性の修正[#2661](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2661).
- 一部のテキストがページで選択されている場合は、グループが開いていないフィルタ[#2662](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2662).

### 変更点

- 差分更新をダウンロードして適用[#2586](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2586).
- [@adguard/tswebextension] を v1.0.8 に更新しました。
- [@adguard/tsurlfilter] を v2.2.9 に更新しました。
- [@adguard/scriptlets] を v1.9.105 に更新しました。
- [@adguard/filters-downloader] を v2.0.4 に更新しました。

## [4.2.240] - 2023-12-15

### 追加

- インフォメーション`@adguard/tswebextension`, `@adguard/tsurlfilter`, `@adguard/extended-css`そして、`@adguard/scriptlets`オプションのページの「About」タブにバージョン[#2237](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2237).

### 変更点

- [@adguard/tswebextension] を v1.0.5 に更新しました。
- [@adguard/tsurlfilter] を v2.2.8 に更新しました。
- [@adguard/scriptlets] を v1.9.101 に更新しました。

### 固定式

- `$$`いくつかのウェブサイトでエンコーディングを破るルール[#2249](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2249).
- フルスクリーンユーザールールエディタによる TSUrlFilter ライブラリの読み込み
  [#2412](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2412).
- Stealth Mode 変更された Cookie ルールを「修正」としてフィルタリングログに表示します。
  [#2512](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2512).
- ハイライト`$inline-font`そして、`$inline-script`
  [#2609](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2609).
- スクリプトは、フィルタリングログが開いた場合にのみ、ブラウザコンソールでログを記録します
  [#2584](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2584).
- 通知スタイルを更新するフィルタ
  [#2309](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2309).

## [4.2.228] - 2023-11-27

### 固定式

- 化粧品規則の適用の記録。

## [4.2.226] - 2023-11-22

### 追加

- マケドニア語のサポート[#2574](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2574).

### 変更点

- オプションのコンテキストメニューから「管理設定...」を削除します。 ツイート[#2258](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2258).
- [@adguard/tswebextension] を v0.4.6 に更新しました。
- [@adguard/tsurlfilter] を v2.2.6 に更新しました。
- [@adguard/filters-downloader] を v1.1.23 に更新しました。
- [@adguard/scriptlets] を v1.9.96 に更新しました。

### 固定式

- Android用のFirefoxでログを開かないようにする[#2563](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2536).
- Firefox Mobileは正しく選択されていない`Report an issue`サイトマップ[2250](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2250).
- ブロックリクエストでログのクラッシュをフィルタリングし、申請から既に許可されている`$removeparam`, `$removeheader`または`$csp`ルール[#2534](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2534).
- 使用しないでください`zh-CN`ローカライズされたメタデータ`zh-TW`ブラウザ言語
  [#2504](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2504).
- ログをフィルタリングする際にのみログを収集[#2544](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2544).
- .php URL でカスタムフィルタリストを追加できません。[#1723](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/1723).

## [4.2.209] - 2023-11-01

### 固定式

- バックグラウンドページがウェイクアップした後、イベントリスナーを再同期します。

## [4.2.208] - 2023-10-23

### 追加

- お問い合わせ`system_version`問題報告中
  [#2535](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2535).

### 変更点

- [@adguard/filters-downloader] を v1.1.20 に更新しました。
- [@adguard/tswebextension] を v0.4.1 に更新しました。
- [@adguard/tsurlfilter] を v2.2.1 に更新しました。
- [@adguard/scriptlets] を v1.9.72 に更新しました。
- 拡張設定画面のタブボタンの削除[#2198](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2198).

### 固定式

- ルールパターンとオプションは、フィルタリングログの規則ウィザードでクリックできません[#2204](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2204).

## [4.2.189] - 2023-10-09

### 追加

- 設定リロードをトリガーしないステルスモードのトグルを修正しました。
- CSPとは`trusted-types`レスポンスヘッダ用のディレクティブ変更
  [#2068](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2068).

### 変更点

- [@adguard/tswebextension] を v0.3.21 に更新しました。
- [@adguard/tsurlfilter] を v2.1.12 に更新しました。

### 固定式

- 推奨フィルタを1グループで有効化
  [#2431](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2431).
- インポート時に重複をフィルタリングしないユーザルール
  [#2446](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2446).
- ルールウィザードのバグと高度な修飾ルール
  [#2456](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2456).
- フィルターダウンロードページの翻訳言語検出
  [#2430](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2430)
- タブの読み込みをブロックしないでください`$popup`直接URLナビゲーション上の修飾ルール
  [#2449](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2449).
- アクティブタブにログをフィルタリングする
  [#2482](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2482).
- ログリクエストの詳細をフィルタリングする際に適用されるステルスモードオプションの表示
  [#2455](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2455).
- ログのタブセレクタをフィルタリングするタブタイトルの更新
  [#2428](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2428).
- Stealth モードによって加えられるようにログでき事をろ過する Stealth モード Cookie の表示
  [#2487](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2487).
- ブロック解除のルールを破るCspルール
  [#2448](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2448).
- AdGuard v4.2.168は更新後にFirefoxで動作していません
  [#2501](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2501).

## [4.2.168] - 2023-09-07

### 変更点

- [@adguard/tsurlfilter] を v2.1.11 に更新しました。
- v0.3.16に[@adguard/tswebextension]を更新しました。
- [@adguard/scriptlets] を v1.9.72 に更新しました。

### 固定式

- エクステンションは頻繁にフィルタのダウンロードを開始しました。
- ログをフィルタリングしているときに追加されていないカスタムフィルタ名が開きます。
- 拡張初期化の chrome の Web ストア ページにコンテンツ スクリプトを注入しないでください。
- ブロックされたCSPレポートは、フィルタリングログの「ブロック」でフィルタリングされていません。
- リダイレクトはタブのブロックされたリクエスト数に含まれていません。
  [#2443](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2443).

## [4.2.162] - 2023-08-28

### 変更点

- [@adguard/tsurlfilter] を v2.1.10 に更新しました。
- [@adguard/tswebextension] を v0.3.11 に更新しました。
- [@adguard/scriptlets] を v1.9.70 に更新しました。

### 固定式

- ログをフィルタリング中に追加しても表示されていないカスタムフィルタ名。
- 拡張初期化の chrome の Web ストア ページにコンテンツ スクリプトを注入しないでください。

## [4.2.151] - 2023-08-11

### 追加

- [@adguard/tswebextension(アドガード)](https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/tswebextension/README.md)MV2の統合。

### 変更点

- Adguard API を別のパッケージに移動 —[@adguard/api(アドガード)](https://www.npmjs.com/package/@adguard/api).
- [@adguard/tsurlfilter] を v2.1.7 に更新しました。
- [@adguard/scriptlets] を v1.9.62 に更新しました。

[4.3.14]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.13...v4.3.14
[4.3.13]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.10...v4.3.13
[4.3.10]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.3.4...v4.3.10
[4.3.4]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.240...v4.3.4
[4.2.240]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.228...v4.2.240
[4.2.228]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.226...v4.2.228
[4.2.226]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.209...v4.2.226
[4.2.209]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/561737249b2c50c39b8e0ee6eefa5d19726c97b3...v4.2.209
[4.2.208]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.189...561737249b2c50c39b8e0ee6eefa5d19726c97b3
[4.2.189]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.168...v4.2.189
[4.2.168]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.162...v4.2.168
[4.2.162]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.2.151...v4.2.162
[4.2.151]: https://github.com/AdguardTeam/AdguardBrowserExtension/compare/v4.1.57...v4.2.151

[@adguard/agtree]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/agtree/CHANGELOG.md
[@adguard/assistant]: https://github.com/AdguardTeam/AdguardAssistant/blob/master/CHANGELOG.md
[@adguard/dnr-converter]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/dnr-converter/CHANGELOG.md
[@adguard/dnr-rulesets]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/dnr-rulesets/CHANGELOG.md
[@adguard/extended-css]: https://github.com/AdguardTeam/ExtendedCss/blob/master/CHANGELOG.md
[@adguard/filters-downloader]: https://github.com/AdguardTeam/FiltersDownloader/blob/master/CHANGELOG.md
[@adguard/logger]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/logger/CHANGELOG.md
[@adguard/rules-editor]: https://github.com/AdguardTeam/rules-editor/blob/master/CHANGELOG.md
[@adguard/scriptlets]: https://github.com/AdguardTeam/Scriptlets/blob/master/CHANGELOG.md
[@adguard/tswebextension]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/tswebextension/CHANGELOG.md
[@adguard/tsurlfilter]: https://github.com/AdguardTeam/tsurlfilter/blob/master/packages/tsurlfilter/CHANGELOG.md
