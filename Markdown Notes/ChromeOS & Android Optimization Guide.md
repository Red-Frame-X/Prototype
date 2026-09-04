# ChromeOS & Android 個人環境メモ

ChromeOSとAndroidで自分が使っている設定、アプリ、拡張機能、コンテンツブロック、トラブルシューティング、関連サービスについて、後から環境を再構成できるように残している個人用メモです。

> [!IMPORTANT]
> この文書は個人の学習記録、検証ログ、設定バックアップです。一般向けの最適化ガイド、推奨構成、サポート文書を目的としていません。
>
> 文章は自分で作成した下書きをChatGPTで推敲・整理している部分があるため、専門性・正確性・完全性を保証できません。誤り、古い情報、環境依存の挙動、未検証の仮説が含まれる可能性があります。重要な仕様、料金、UI、セキュリティ上の判断は、使用時点の公式ドキュメント、公開ソース、CHANGELOG、Issues、実機の挙動で再確認します。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

---

## 1. サブスクリプションの管理メモ

自分が有料サービスを継続するか判断するときは、利用頻度、代替手段、年間総額、解約条件、保守やトラブル対応に使う時間を確認します。料金や年額割引はサービスごとに異なるため、「月額×一定月数」といった一般化はせず、更新時点の公式料金ページを確認します。

### 現在の利用状況を記録しているサービス

- Amazon Prime
- ChMate スタンダードプラン
- ChatGPT Plus
- Google AI / Google One関連プラン
- mond メンバーシップ
- 𝕏 Premium
- YouTube Premium

契約経路がGoogle、Apple、携帯キャリア等に分かれると、請求・解約・特典の管理主体も分かれる場合があります。自分の環境では、契約変更前に「現在の請求元」「既存特典」「次回更新日」を確認します。

### Google One関連で残しているトラブル記録

過去に購入特典と有料プランを重複して適用した際、Google Oneの表示やプラン管理が正常でない状態を経験しました。この記録は自分の事例であり、一般仕様としては扱いません。

- [Google One ヘルプ](https://support.google.com/googleone/)
- [Google One お問い合わせ](https://support.google.com/googleone/gethelp)
- [Google One プラン](https://one.google.com/about/plans?hl=ja-JP)

Reddit等のユーザー報告は原因候補の参考にはしますが、公式仕様や自分の事例の原因確定には使いません。

---

## 2. ChromeOS / Chrome 拡張機能メモ

Chrome拡張機能は必要最小限にし、問題が出た場合に一つずつ無効化して原因を切り分けられる状態を保ちます。拡張機能の権限、所有者変更、更新履歴、ストア公開状態は将来変わる可能性があるため、再インストール時に確認します。

- [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=ja)
- [Chrome Web Store](https://chromewebstore.google.com/category/extensions)

### UserScriptマネージャー

自分のUserScriptは主にViolentmonkeyまたはTampermonkeyで管理します。ChromeのUser Scripts APIや拡張機能の権限要件はバージョンで変わるため、保存している手順だけで判断せず、使用時のUIと公式資料を確認します。

- [Violentmonkey](https://violentmonkey.github.io/)
- [Tampermonkey Documentation](https://www.tampermonkey.net/documentation.php)
- 自分のスクリプト一覧：[`../UserScript/`](../UserScript/)

### 自分が用途別に確認している拡張機能・ツール

以下は候補・使用履歴のメモであり、すべてを同時に有効化する構成ではありません。

**コンテンツブロック・検索**

- [AdGuard Browser Extension](https://github.com/AdguardTeam/AdguardBrowserExtension)
- [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home)
- [uBlacklist](https://github.com/iorate/ublacklist)

**YouTube**

- Enhancer for YouTube
- SponsorBlock

**GitHub・文章・翻訳**

- GitHub関連UI補助
- DeepL
- Googleオフラインドキュメント

**タブ・ブックマーク・表示補助**

- タブ管理系拡張
- ブックマークサイドバー
- 画像プレビュー系拡張

拡張機能を追加した直後にGmail、Googleサービス、AdGuard等で異常が出た場合は、拡張機能の競合も原因候補に含めます。以前の環境では画像プレビュー系拡張との関連を疑った事例がありましたが、一般化できる原因としては扱っていません。

---

## 3. ChromeOS上のAndroidアプリメモ

自分のChromeOS環境で利用または検証したAndroidアプリを記録しています。ChromeOS上での互換性はAndroidスマートフォンと同じとは限らないため、Play Storeでの対応表示と実機挙動を優先します。

- [ChMate](https://play.google.com/store/apps/details?id=jp.co.airfront.android.a2chMate)
- [personalDNSfilter](https://github.com/IngoZenz/personaldnsfilter)
- Google Home
- Google Photos

### ChMate

ChMateのNG設定で使う自分用の正規表現は[`../NG Word Regex for ChMate/`](../NG%20Word%20Regex%20for%20ChMate/)に分離しています。

ChromeOSでの表示・入力・ウィンドウ動作は端末やChromeOSバージョンの影響を受けるため、スマートフォンで正常でもChromeOSで同じとはみなしません。

- [ChMate公式](https://chmate.airfront.co.jp/)
- [対応OS](https://chmate.airfront.co.jp/docs/supported-os/)

---

## 4. ChatGPTを使うときの自分用メモ

ChatGPTは下書きの整理、文章校正、調査項目の洗い出し、コード・設定の査読などに使っています。回答は正解保証ではないため、重要な固有名詞、日付、数値、構文、セキュリティ判断は一次情報で再確認します。

### 自分が調査依頼に含める条件

- 公式ドキュメント、公開ソース、CHANGELOG、Issuesなど一次情報を優先する
- 事実、推測、未確認事項を分ける
- 重要な主張に直接対応する根拠を示す
- 利点だけでなく欠点・互換性・保守性・プライバシーも確認する
- 見えていないDOM、ログ、非公開情報を推測で断定しない

### 自分がGitHub作業で確認すること

ChatGPTやCodexへリポジトリ変更を依頼する場合は、対象ファイル、変更範囲、完了条件、実行すべきテストを明示します。AIが作成した差分は、テストを実行していなければ動作確認済みとは扱いません。

GitHub Appやプラグインには必要なリポジトリと権限だけを許可し、APIキー、トークン、Cookie、個人情報をリポジトリやプロンプトへ保存しません。

- [OpenAI Help / Documentation](https://help.openai.com/)
- [GitHub Apps permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)

### 自分用プロンプトの基本形

```text
# 目的
（調べたいこと、修正したいこと）

# 対象
（URL、ファイル、製品、バージョン、環境）

# 条件
- 一次情報を優先する
- 事実・推測・未確認事項を分ける
- 変更は指定範囲に限定する
- 互換性・副作用・ロールバック方法を確認する

# 出力
- 結論
- 根拠
- 変更内容または確認手順
- 未確認事項
```

このテンプレート自体も万能ではなく、作業ごとに必要な条件だけ残します。

---

## 5. コード編集環境のメモ

ChromeOSではブラウザやAndroidアプリ中心の編集環境も利用しています。Gitを直接実行できる環境と、Web API経由でGitHubファイルを編集する環境は同じではないため、テストや生成処理が必要な変更では実行環境の有無を確認します。

- [Visual Studio Code for the Web](https://vscode.dev/)
- [Visual Studio Code](https://github.com/microsoft/vscode)
- QuickEdit系Androidエディタ
- GitHub公式Web UI / GitHubアプリ

Personal Access Tokenを使う場合は必要最小限の権限にし、不要になったトークンは失効します。トークン文字列そのものはメモやリポジトリへ保存しません。

---

## 6. AdGuardユーザールールの自分用作成フロー

詳細な構文メモは以下へ分離しています。

- [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md)
- [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)
- [`../AdGuard Custom Rules/`](../AdGuard%20Custom%20Rules/)

### 自分が新しいルールを作るとき

1. 対象URL、使用製品、期待する動作を固定する。
2. 要素非表示なら対象要素と周辺DOMを確認する。
3. 通信ブロックならFiltering logまたはDevTools Networkで対象通信を確認する。
4. まず適用範囲の狭い標準的なルールを試す。
5. Extended CSS、Scriptlet、レスポンス改変は必要性を確認できた場合だけ使う。
6. 対象が消えたことに加え、ログイン、検索、再生、スクロール、決済等が壊れていないか確認する。
7. ルール追加理由と、必要なら参照Issueをコメントで残す。

### 自分がAIへルール作成を依頼するとき

対象URLだけではなく、可能な場合はHTML、Network情報、使用製品を渡します。AIがログイン後ページや動的DOMを実際に確認できない場合は、その制約を明示させ、見えていない要素を推測で決めさせません。

### 既存ルールを整理するとき

- 完全に同一の有効ルールだけを機械的重複として削除する
- 似ているだけのルールは動作確認なしに統合しない
- コメントと対象ルールの対応を維持する
- ドメイン、修飾子、例外、正規表現の意味を変えない
- 変更後はAGLintとリポジトリのテストを実行する

---

## 7. AdGuard Browser Extension MV3の運用メモ

自分のChrome / ChromeOS環境では、MV3のDNR制約、サイト権限、User Scripts API、Custom filtersの更新経路を分けて確認します。

- [AdGuard Browser Extension](https://adguard.com/kb/ja/adguard-browser-extension/)
- [MV3 version](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuard Browser Extension GitHub](https://github.com/AdguardTeam/AdguardBrowserExtension)

### 自分のカスタムフィルタ

[`../AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt`](../AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt)を原本として管理しています。

uBO Lite向けの生成物は[`../uBOL Filter Converter/`](../uBOL%20Filter%20Converter/)で別に変換し、AdGuard原本をそのまま別エンジンへ流用しません。

問題が出た場合は、まず自分のカスタムルール／カスタムフィルタを外して再現するかを確認し、組み込みフィルタやブラウザ機能との原因を分離します。

---

## 8. AdGuard for Androidの運用メモ

自分のAndroid環境では、ローカルVPN、HTTPSフィルタリング、DNS保護を別機能として切り分けます。金融・認証・証明書ピンニング等の影響があるアプリでは、HTTPSフィルタリングの可否を個別に確認します。

- [AdGuard for Android](https://adguard.com/kb/ja/adguard-for-android/)
- [GitHub Releases](https://github.com/AdguardTeam/AdguardForAndroid/releases)
- [Background work](https://adguard.com/kb/ja/adguard-for-android/solving-problems/background-work/)
- [Automation](https://adguard.com/kb/adguard-for-android/solving-problems/tasker/)

### 自分が安定性を確認するとき

- Androidのバッテリー制限でAdGuardが停止していないか
- 常時接続VPNの設定
- 他のVPN、Private DNS、ブラウザのSecure DNSとの競合
- HTTPSフィルタリングの対象アプリ
- DNSフィルタの誤ブロック
- AdGuard本体とフィルタのバージョン

### MacroDroidからの自動化メモ

AdGuardのAutomationReceiverを利用する場合は、AdGuard公式の自動化仕様に記載された`start`、`update`等のアクションを確認してから設定します。`update`は保護の再起動と同義ではなく、利用可能な更新を確認するアクションとして扱います。

自動化パスワードはリポジトリへ保存しません。

---

## 9. DNSブロックの個人運用メモ

DNSブロックの詳細は[`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md)へ分離しています。

自分の環境では、ブラウザ用コンテンツブロッカーとDNSフィルタを同じものとして扱いません。DNSで先に遮断されるとブラウザ側ログに通信が現れない場合があるため、誤ブロック時には各レイヤーを個別に停止して原因を切り分けます。

### personalDNSfilter

- [personalDNSfilter GitHub](https://github.com/IngoZenz/personaldnsfilter)
- [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)

自分がdomains-onlyリストを使う場合は、クライアント側のサブドメイン処理、例外方法、更新状態を確認します。

### Android Private DNS

AndroidのPrivate DNSはDNS-over-TLS用の設定です。特定のフィルタリングDNSを使う場合は、そのサービスのプライバシーポリシー、障害時の影響、ブロック内容を確認します。

AdGuard DNSのホスト名や仕様は変更され得るため、保存した文字列ではなく[AdGuard DNS公式](https://adguard-dns.io/)を参照します。

---

## 10. uBlacklistの個人設定メモ

uBlacklistは検索結果から指定サイトを非表示にする用途で使います。

- [uBlacklist](https://github.com/iorate/ublacklist)
- [Documentation](https://iorate.github.io/ublacklist/ja/docs)

自分が外部ルールセットを購読する場合は、配布元、更新履歴、ルール内容を確認し、検索結果が過剰に消える場合は購読リストを一つずつ無効化します。

---

## 11. ReVanced / Morphe等の検証メモ

公式Androidアプリへパッチを適用するプロジェクトを検証する場合があります。この項目は利用を勧めるためではなく、自分が出所とリスクを確認するための記録です。

- [ReVanced](https://revanced.app/)
- [ReVanced GitHub](https://github.com/revanced)
- Morphe関連の公開リポジトリ

自分が確認する項目：

- パッチ・Managerの公式配布元
- ソースコードとRelease
- 対象APKのバージョン
- 署名・ハッシュ
- アカウントや利用規約への影響
- 更新停止やフォーク移行の有無

第三者が配布するビルド済みAPKは、公開ソースと同一であることを自動的には保証できないため、出所を分けて扱います。

---

## 12. セキュリティ・プライバシーの自分用整理

### セキュリティ

端末、アカウント、通信、データを不正アクセスや改変から守るための仕組みとして整理しています。

### プライバシー

どの情報を誰へ渡すか、どの範囲で処理・保存されるかを自分で把握・制御する観点として整理しています。

### 匿名性

行動と実名・アカウント・端末等の識別子を結び付けにくくする性質として整理しています。セキュリティやプライバシーと同義ではありません。

自分の設定変更では、「ブロック数が多いほど安全」とは考えず、誤ブロック、ログ収集、証明書介入、権限、アップデート経路まで含めて判断します。

---

## 13. 詐欺・フィッシング対策の個人メモ

自分が不審な連絡を受けたときに確認する項目です。

- 電話・SMS・メールのリンクから直接ログインしない
- 公式アプリ、保存済みブックマーク、公式サイトから確認する
- 電話中や画面共有中にセキュリティ機能を解除しない
- パスワード、PIN、ワンタイムコード、リカバリコードを第三者へ渡さない
- 支払い、送金、暗号資産購入を急かされた場合は別経路で真偽を確認する
- 公的機関・企業を名乗る場合も、相手が提示した連絡先ではなく公式窓口を自分で調べる

- [警察庁 SOS47](https://www.npa.go.jp/bureau/safetylife/sos47/)
- [フィッシング対策協議会](https://www.antiphishing.jp/)

電話番号の先頭や末尾だけで詐欺と断定しません。番号表示は偽装される場合があり、正規の050、0120、0800、0570等も存在するため、連絡内容と公式窓口で確認します。

---

## 14. Googlebook / Aluminium関連メモ

GooglebookとAluminiumに関する調査は[`Googlebook & Aluminium Survey Report - Revised Edition.md`](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md)へ分離しています。

発売前・移行期の情報は変化が大きいため、この総合メモでは個別の発売時期、終了時期、Linux実装などを確定事項として重複記載しません。

---

## 15. 自分がトラブルを切り分ける基本順序

ChromeOS、Android、AdGuard、拡張機能などで問題が起きた場合、データ消失や設定変更の影響が小さい順に確認します。

1. 発生時刻、バージョン、直前の変更を記録する。
2. ページ再読み込み、アプリ再起動、端末再起動を試す。
3. 直前に追加した拡張機能、UserScript、フィルタ、DNS設定を一つずつ戻す。
4. 別ネットワークや公式のステータス情報で外部障害を確認する。
5. ログやDevToolsで原因レイヤーを絞る。
6. 設定初期化、Powerwash、OS復元など影響の大きい操作は最後に検討する。
7. 復旧後、原因が確認できたものと推測に留まるものを分けて記録する。

ChromeOS更新についての詳細は[`ChromeOS Manual Update and Troubleshooting.md`](ChromeOS%20Manual%20Update%20and%20Troubleshooting.md)に分離しています。

---

## 16. 自分が参照している一次情報

### Chrome / ChromeOS

- [Chrome for Developers](https://developer.chrome.com/)
- [ChromeOS / Chromebook Help](https://support.google.com/chromebook/)
- [Chromium](https://chromium.googlesource.com/)

### Android

- [Android Developers](https://developer.android.com/)
- [Android Help](https://support.google.com/android/)

### AdGuard

- [AdGuard Knowledge Base](https://adguard.com/kb/)
- [AdGuard GitHub](https://github.com/AdguardTeam)
- [AdGuard Filters](https://github.com/AdguardTeam/AdguardFilters)

### uBlock Origin / uBO Lite

- [uBlock Origin](https://github.com/gorhill/uBlock)
- [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home)
- [uAssets](https://github.com/uBlockOrigin/uAssets)

### GitHub

- [GitHub Docs](https://docs.github.com/)
- [GitHub Status](https://www.githubstatus.com/)

### Web技術

- [MDN Web Docs](https://developer.mozilla.org/)

コミュニティ、Reddit、ブログ、掲示板は再現例や問題発見の補助として使いますが、公式仕様と同じ確度では扱いません。

---

## 17. このメモの更新方針

- 自分が現在使っていない設定も、再検証の価値がある場合だけ履歴として残す。
- 一般論として断定せず、「自分の環境で確認」「公式で確認」「未確認」を分ける。
- 同じ内容が専用ドキュメントにある場合は、この総合メモから詳細手順を削り、リンクへ集約する。
- UI名、料金、バージョン依存情報は更新時に公式資料を再確認する。
- ChatGPTで推敲した文章も、そのまま正しいとはみなさない。
- 不要になった古い手順、リンク切れ、重複、テーマ等の削除済みコンテンツは復活させない。
