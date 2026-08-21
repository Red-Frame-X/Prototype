# アンドロイドのchangelogミラーのためのAdGuard

> ソース:https://api.github.com/repos/AdguardTeam/AdguardForAndroid/releases?per_page=100
> GitHub リリースの公式リリースから、リリースを最初に作成します。

## 4.13.1

- 公表: 2026-08-03T16:50:17Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.1

最近、Android v4.13用のAdGuardをリリースし、バグのカップルに対処するための迅速なホットフィックスでフォローしています。

統合モードが適切に機能するため、AdGuardとAdGuard VPNの両方を最新バージョンにアップデートする必要があります。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.13

- 公表: 2026-07-28T14:04:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13

Android v4.13で予想されるAdGuardをお待ちください! 私たちは、このリリースのための野心的な目標を設定しました, そして、配信するために最善を尽くしました: 多くの仕事は、大きな機能の面だけでなく、より良いパフォーマンスのためのバグや油着ギアの固定の場面のルーチンの背後にある両方の大きな機能で行われました. 詳しくは以下をご覧ください。

このリリースで、Android用のAdGuardに差異フィルタの更新を導入しました! これを実現するために、フィルタリストマネージャライブラリをアプリに統合しました。 これで、トラフィックとサーバーを過負荷することなく、自動的にフィルタがロードされます。

また、DnsLibs にポスト量暗号化サポートを追加しました。 AdGuardは、他のフルアドブロック製品と同様に、将来の脅威からDNSリクエストを保護します。

もう1つの重要な変更は、Revoked証明書を検証するためにMozillaによるCRLiteの採用です。 より古いOCSP(オンライン証明書ステータスプロトコル)の代わりに、またはCRL(証明書の取消リスト)に対する各証明書を、Webサイトの読み込みをスピードアップするだけでなく、閲覧中にプライバシーと安全を向上させることができます。

AdGuard VPN との統合モードでのセキュリティを改善するために、接続プロトコルを変更し、認証情報の使用を導入しました。 Android v4.13 用の AdGuard のリリースでは、広告ブロッカーと VPN はシームレスに連携し、安全に連携し、同期させるためのユーザーの部分で必要な追加のアクションはありません。 サードパーティのアプリは、追加のボーナスとして、あなたの活動をスパイすることができません。

以前のバージョンでは、HTTPS 証明書をインストールするためのアプリ内指示が追加されました。このプロセスは、デバイスの作成とモデルに関して異なる可能性があるためです。 Android 4.13 用の AdGuard では、ColorOS (Oppo) のサポートを追加しました。

そして最後に、しかし、少なくとも、我々は私たちのフィルタリングエンジンと時間をかけて蓄積した固定バグに多くの仕事をしてきました。 スクリプトとCoreLibsは、より良いアプリのパフォーマンスのために更新されました。

下記の変更履歴を参考にして、すべての修正と改善を見ることができます。

## 変更履歴


### 改善点
* フィルタリングログ [5637] で詳細に適用される規則をコピーする可能性を追加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5637)
* Googleバックアップのサポートを追加 [5879](https://github.com/AdguardTeam/AdguardForAndroid/issues/5879)
* デフォルトでフィルタリングから2ndLineアプリケーションを除外 [5116](https://github.com/AdguardTeam/AdguardForAndroid/issues/5116)
* DNS リストの DNS フィルターの更新に関する情報を表示 [5519](https://github.com/AdguardTeam/AdguardForAndroid/issues/5519)
* フィルタリングログ [5636] の詳細は、package name のリクエストをコピーする可能性を追加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5636)
* 更新チェック画面で*Check for update*ボタンの動作を改善しました [5923](https://github.com/AdguardTeam/AdguardForAndroid/issues/5923)
* 最近の活動タブ[5193]を経由して空のユーザールールを追加する可能性を排除しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5193)
* *Updates*画面に更新されたコンテンツのカラー差別化を追加 [5886](https://github.com/AdguardTeam/AdguardForAndroid/issues/5886)
* *プライベートブラウザ*のトークバックボイスアシスタントの要素の改善*
* *追跡保護*の入力/ダイアログを再構成しました
* クラッシュレポートとアプリの使用データ名とダイアログを更新
* 最近の活動で適用される規則によって要求を見つけるオプションを追加しました
* ※IP*アドレス画面をマークする
* *Webサイト保護*スイッチを*プライベートブラウザ*に切り替えた後、Webページの自動更新を追加
* ローカルプロキシの認証を追加
* クリアする可能性を追加`.hprof`必要なくない場合
* TV用のアプリ更新エラー画面を追加しました
* 背景と画像画像画像(PiP)モードでYouTubeプレーヤーで動画再生を改善

### フィックス
* ブロックルール`$network`リクエスト詳細に規則*ボタンを許可する追加で追加されます[5390](https://github.com/AdguardTeam/AdguardForAndroid/issues/5390)
* *Disable all?* ポップアップは、ルールリストが空の場合でも、*ユーザールール*画面に表示されます[5175](https://github.com/AdguardTeam/AdguardForAndroid/issues/5175)
* CA 証明書のインストール手順は、ColorOS [5827] には関係ありません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5827)
* DNS フィルターの表示`null`最後の更新の代わりに [5902](https://github.com/AdguardTeam/AdguardForAndroid/issues/5902)
* *Usage access* システム許可[5927]を付与した後に自動的に防火壁が活動化します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5927)
* v4.12(5893)から始まる高電池消費量https://github.com/AdguardTeam/AdguardForAndroid/issues/5893)
* ドメインをブロックし、DNSフィルタでブロック解除し、フィルタリングログのみ[5880](https://github.com/AdguardTeam/AdguardForAndroid/issues/5880)
* 誤ったサブドメインが統計で表示されます [5868](https://github.com/AdguardTeam/AdguardForAndroid/issues/5868)
* 多くのアプリは、AdGuardがアクティブなときに動作を停止します [5617](https://github.com/AdguardTeam/AdguardForAndroid/issues/5617)
* 最近の活動ログはv4.12.1に更新した後に大きく遅れる [5882](https://github.com/AdguardTeam/AdguardForAndroid/issues/5882)
* 英語以外の言語モードで拡張機能を編集する際の問題 [5914](https://github.com/AdguardTeam/AdguardForAndroid/issues/5914)
* 最近の活動ログは、AdGuard v4.14 夜 4 で即座に消去されなかった [5908](https://github.com/AdguardTeam/AdguardForAndroid/issues/5908)
* *Statistics* [5840] で重複するサブドメイン (https://github.com/AdguardTeam/AdguardForAndroid/issues/5840)
* カスタムDNSサーバーは、単にエクスポートされた設定をインポートした後に消え [5892](https://github.com/AdguardTeam/AdguardForAndroid/issues/5892)
* 水平モード [5612] で共有ボタンをクリックすると、動画のタイトルが最小化されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5612)
* タイルを使用してAdGuardをオンにして通知パネルを閉じる[5915](https://github.com/AdguardTeam/AdguardForAndroid/issues/5915)
* 許可なしのフィルター更新 [5309](https://github.com/AdguardTeam/AdguardForAndroid/issues/5309)
* *Ad blocking* および *DNS filtering* のユーザレグテックスは、AdGuard v4.14 夜 5 [5916] 以降に動作します。https://github.com/AdguardTeam/AdguardForAndroid/issues/5916)
* ベータ版(RCなど)を更新しようとすると、アップデートは最新のリリース版[5920]に進みます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5920)
* 設定は、バージョンが一貫した場合でも、リンクを介してインポートできません[5912](https://github.com/AdguardTeam/AdguardForAndroid/issues/5912)
* *適用規則*セクションで自分自身を複製するルール
* AdGuard Personal CA をアプリの *Move* ボタンでシステムストアに移動できなかった
* カスタムコンテンツフィルタリストは時間後に消えます
* 保護は*HTTPSのろ過*および*FakeDNS*によって可能にされるあらゆる秒を再開します
* userscript を編集した後にエラースナックが表示されます
* 設定名をタップすると、拡張子設定のスイッチは応答しません
* 電話を再起動した後、ブロックされたURLは、ログにブロックされた理由を示すことはありません
* ※ホットスポットがアクティブである間、保護が正常に動作しない場合があります* 通知はAndroid 10以降で表示されます
* *Recent アクティビティ* から追加の修飾子でブロックルールを追加できません。
* *Saveとselect*をタップすることで、カスタムDNSサーバーを選択可能
* 実際の DNS プロトコルは、設定のインポート後に *DNS サーバの詳細* 画面に表示されているものと一致しません。
* 拡張エディタを開くと、ナビゲーションバーの下の空スペース
* AdGuardは再起動後に起動しません
* リンクを介して設定をインポートする際に、証明書のインストールのオンボーディングの誤った表示
* 統合モード対話は、アプリの最初の起動時に一貫して開いていません
* リクエスト詳細から返された後、ヘッダが崩壊しなかった場合は、*Recent アクティビティ*画面にクエリを検索しない
* DNS プロバイダーの *Open* ボタンは、ブラウザが開いているが、Xiaomi TV Box の Web サイトが表示されない
* ※ライセンスチェックタイムアウト後の*TVライセンス*画面にライセンス情報*スナックが表示されない
* TVの*License*スクリーンの*Refreshの状態*ボタンを押した後にデフォルトに焦点を合わせて下さい
* *証明書がインストールされていない*ダイアログは、設定共有による証明書のインストール後に表示されます。
* フィルター更新後にカスタムフィルタバージョンが更新されていない
* *Ruleエディタ*のキーボードによってカバーされるテキストのクリッピング、ヘッダーの重複、および内容
* AdGuardプレーヤーのYouTubeボタンが動画を再起動します
* *Quick action*画面ファイアウォール通知は、*Show blocked only*フィルタが選択されたときにブロックされたアプリと許可されたアプリの両方で表示されます。
* スクロール *ユーザールール* 別のビューを重ねる
* スクロールフォーカスは、テレビで*アプリ管理*の急激なスクロール中にビューポートから動き出します
* YouTube MusicからAdGuardプレーヤーへの共有は機能しません
* AdGuardの通知は、デバイスの画面をスリープモードから引き出します。
* *プライベートブラウザ*は、他のアプリはWebページから開くことはありません。
* フィルタルールエディタは、構文検証なしで有効なルールとして、任意の非空の文字列を受け入れます
* ※プライベートブラウザ*を閉じた後、動的テーマはアドガードアプリには適用されません。

* Kazakh または Kyrgyz をシステム言語として使用して、AdGuard はロシアとしてそれを誤って表示します
* hieroglyphs を使用する言語の通知では、ブロックされたリクエストの数が誤って表示されます。

### DnsLibs (DNSのろ過エンジン)
* DnsLibsをv2.8.45に更新 [5961](https://github.com/AdguardTeam/AdguardForAndroid/issues/5961)

#### 改善点
* DnsLibs へのポスト量子暗号化サポートを追加 [245]()https://github.com/AdguardTeam/DnsLibs/issues/245)
* 削除するオプションを追加`h3`から`alpn`HTTPS RRのパラメーター [257](https://github.com/AdguardTeam/DnsLibs/issues/257)
 * テストの信頼性を改善しました。 DoT アップストリームの可用性 [263] (https://github.com/AdguardTeam/DnsLibs/issues/263)
* フィルターをリロードすることなくDNSアップストリームリストの更新を改善 [248](https://github.com/AdguardTeam/DnsLibs/issues/248)

#### フィックス
* DNSのブロック解除ルールは動作しません
* 時折、システム:// 上流応答は、Android上で受け入れられなかった [265](https://github.com/AdguardTeam/DnsLibs/issues/265)
* hitomi.laのような一部のウェブサイトでAdGuardの証明書を見逃す [2055](https://github.com/AdguardTeam/CoreLibs/issues/2055)

### CoreLibs (フィルターエンジン)

* CoreLibsをv1.21.38に更新

#### 改善点
* URL のデコードをサポート`$urltransform` [1915](https://github.com/AdguardTeam/CoreLibs/issues/1915)
* ベータ/ナイトリービルドでデフォルトで HTTP/3 フィルタリングを有効にしました [2014](https://github.com/AdguardTeam/CoreLibs/issues/2014)
* 例.org/path 化粧品規則 [2012] のサポートを追加しました。https://github.com/AdguardTeam/CoreLibs/issues/2012)
* 新しいサポートを追加`$reason`修飾子 [1986](https://github.com/AdguardTeam/CoreLibs/issues/1986)
* *Do Not Track* 動作改善 (1982)https://github.com/AdguardTeam/CoreLibs/issues/1982)
* 保護を有効にした後、 local.adguard.org DNS の漏洩を防止 [1854](https://github.com/AdguardTeam/CoreLibs/issues/1854)
* 安定ビルドでデフォルトで HTTP/3 フィルタリングを有効にしました [2015](https://github.com/AdguardTeam/CoreLibs/issues/2015)

#### フィックス
* 誤った証明書シリアル番号マーシャリングが偽陽性CRLiteマッチにつながり [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* 高度なオプション*チェックウェブサイトの証明書の透明性*が有効になっている場合は、AdGuard証明書はありません[2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* CoreLibs v1.19の接続リセット
* localhost は v1.19 [2019] の手動プロキシモードでは到達できません。https://github.com/AdguardTeam/CoreLibs/issues/2019)
* AdGuard VPN との統合が有効になっている場合は、*Request の詳細* に間違った宛先アドレスが表示される [2021](https://github.com/AdguardTeam/CoreLibs/issues/2021)
* BOM(2009年)によるユーザスクリプトのインポート失敗https://github.com/AdguardTeam/CoreLibs/issues/2009)
* プロキシ設定でFakeDNSが使用されているときに壊れた注射[2017](https://github.com/AdguardTeam/CoreLibs/issues/2017)
* スペースでスクリプトタグを閉じる壊れた処理[2042](https://github.com/AdguardTeam/CoreLibs/issues/2042)
* エラー`$generichide`ドメインスコープルールの動作 [2041](https://github.com/AdguardTeam/CoreLibs/issues/2041)
* QUIC/HTTP/3 フィルタリングの高レイテンシは、プロトコルが HTTP/2 [2062] にフォールバックする原因https://github.com/AdguardTeam/CoreLibs/issues/2062)

### スクリプト(フィルタリングルールのJavaScript強化)
* スクリプトをv2.2.16に更新

#### 改善点
* 新しいスクリプトレットを追加 —`prevent-innerHTML` [488](https://github.com/AdguardTeam/Scriptlets/issues/488)
* 改善しました`fingerprintjs2`— サポートウィンドウ [541](https://github.com/AdguardTeam/Scriptlets/issues/541)
* 期間を増加させるパラメータを追加`trusted-click-element`scriptletの実行期間 [400](https://github.com/AdguardTeam/Scriptlets/issues/400)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12.3

- 公表: 2026-02-20T18:11:04Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.3

アプリの安定性を高め、マイナーなバグを修正する技術アップデートです。

## 変更履歴

### フィックス
* 保護機能が有効になった場合、インターネットアクセスなし [#5897](https://github.com/AdguardTeam/AdguardForAndroid/issues/5897)

### CoreLibs (フィルターエンジン)

* 更新されたCoreLibsにv1.19.48 [#6011](https://github.com/AdguardTeam/AdguardForAndroid/issues/6011)

### スクリプト(フィルタリングルールのJavaScript強化)

* スクリプトをv2.2.10に更新

### 改善点
* 'href-sanitizer ' — uBO 引数をサポート [#493](https://github.com/AdguardTeam/Scriptlets/issues/493)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12.2

- 公表: 2025-12T17:57:02Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.2

アプリの安定性を高め、マイナーなバグを修正する技術アップデートです。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12.1

- 公表: 2025-10-14T09:37:46Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.1

Android 用の AdGuard の最新の更新後、2 つのバグが見つかった: アプリは自動的に起動せず、一部のユーザーに対して自動更新を停止します。 私たちは、これらの問題に対処するために迅速な修正をロールアウトし、あなたの広告ブロックを正常に取得しています。

## 変更履歴

### フィックス
* システム起動時にアプリが起動を停止
 [#5862](https://github.com/AdguardTeam/AdguardForAndroid/issues/5862)
* フィルターの自動更新は機能しません
 [#5866](https://github.com/AdguardTeam/AdguardForAndroid/issues/5866)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12

- 公開日: 2025-10-01T18:40:48Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12

このリリースでは、タブレット上のAndroid用のAdGuardを使用して、より便利になりました。ランドスケープモードに投票した全員のおかげで。 また、新しい *Share 設定* 機能を追加し、CoreLibs の改善を行いました。 バージョン4.12へのアップデートを忘れずに、以下の新機能についてもっと読む!
## 景観モード
私たちはいつも言うように、あなたのフィードバックは私たちにとって本当に重要であり、今回は私たちが最も要求された機能の1つを追加しました。 タブレットでAdGuardを使うと、より便利になりました。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/tablet_en.png"幅="700">
</p>

研磨が必要な画面もありますが、積極的に取り組んでいます!

## 共有設定

共有設定機能も追加しました。 これで、新しいデバイスですべてを再構成したり、見逃された広告を報告するときに設定を記述する時間を費やす必要はありません。リンクを共有したり、QRコードをスキャンしたりできます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/share_en.png"幅="300">
</p>

設定を共有するには、[設定] → [メニュー (有料) → [設定を共有する] → [設定を共有する] に移動します。 誰かがリンクを送信したら、ブラウザで開くだけでインポートをタップします。

## コアライブラリ

新しいCoreLibsリリースには、バグ修正とさまざまな改善が含まれています。 例えば、ユーザスクリプトは、SPA(単一ページアプリケーション)のウェブサイト上でより確実に機能できるようになりました。https://en.wikipedia.org/wiki/Single-page_application)。 詳細は変更履歴をご確認ください。

## 変更履歴

### 改善点
* アプリが正しく動作するように、com.bKash.customerapp 用の「AdGuard によるルートトラフィック」オプションを無効にしました [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### フィックス
* CA 証明書のインストール手順は、名誉 [#5779] には関係ありません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* アプリ固有の HTTPS 除外 [#5290] を追加できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* 更新セクション[#5821]にカスタムDNSフィルタが表示されない(https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* スナックバーにクロスをタッピングして、新しいアプリバージョンをダウンロードしてもダウンロードを停止しない[#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* AdGuard のフィルタリング [#5819] による銀行アプリで一部の画像が欠落しています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)

### CoreLibs (フィルターエンジン)

* 更新されたCoreLibsにv1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### 改善点
* 改善された`$app`修飾語:ワイルドカードと正規表現のサポートを追加
[#1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* ALPSエクステンションのサポートを追加 [#1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### フィックス
* ログ[#5739]に表示されている間違った追跡保護オプション(https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* パフォーマンス警告(new.lewd.ninja)による一部のウェブサイトで無効なフィルタリング [#1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* プロキシサーバーの「FakeDNS」オプションは、バイパスされたアプリの接続を中断 [#5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* 一部の拡張子はv2.17 [#1993](更新後に動作しません)https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHRタイムアウトとXHRタイムアウト`immersivetranslate`ユーザスクリプト [#2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* コンテンツタイプの修飾子は機能しません`$urltransform`修飾子 [#1978] (https://github.com/AdguardTeam/CoreLibs/issues/1978)
* DNS フィルターは適用しません [#5851] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### DnsLibs (DNSのろ過エンジン)

* DnsLibsをv2.6.20に更新 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### スクリプト(フィルタリングルールのJavaScript強化)

* スクリプトをv2.2.9に更新しました

#### 改善点
* 新しいスクリプトレットを追加 — 'trusted-replace-argument' [#405]()https://github.com/AdguardTeam/Scriptlets/issues/405)

#### フィックス
* 'prevent-element-src-loading' — TrustedScriptURL は Firefox [#514] で定義されていません。https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — 引用符は正しくエスケープされます [#517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* 未サポートの正規表現によるSafari 15のコンパイルエラー [#519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.11

- 発行: 2025-08-26T15:38:16Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.11

このリリースには、いくつかのアンダーフードの改善、バグ修正のかなりの数、およびCoreLibsの更新が含まれます。 その結果、アプリ全体の安定性が大幅に向上しました。

## 変更履歴

### フィックス
* Createボタンは、トライアルアクティベーション画面のチェックボックスをオーバーラップ [#5039](https://github.com/AdguardTeam/AdguardForAndroid/issues/5039)
* YouTubeアプリから動画を共有するときにAdGuardプレーヤーが開いていない[#5780](https://github.com/AdguardTeam/AdguardForAndroid/issues/5780)
* AdGuard は、統合モード [#5567] でサードパーティの VPN として AdGuard VPN を識別します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5567)
* UIDが除外するアプリは、AdGuard [#5731] を介してルーティングされています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5731)
* 日本語、韓国語、中国語の無効なフィルタ更新日フォーマット [#5703](https://github.com/AdguardTeam/AdguardForAndroid/issues/5703)
* プライベートブラウザ通知の文字列を欠く [#5741](https://github.com/AdguardTeam/AdguardForAndroid/issues/5741)
* 専用ブラウザのオンボーディングが2回表示されます[#5752](https://github.com/AdguardTeam/AdguardForAndroid/issues/5752)
* ブラウザの設定をタップした後、プライベートブラウザがクラッシュ [#5781](https://github.com/AdguardTeam/AdguardForAndroid/issues/5781)
* 「Nothing found」の警告は、いくつかの画面で欠落しています [#5038](https://github.com/AdguardTeam/AdguardForAndroid/issues/5038)
* 「プロキシで動作するアプリ」画面は、インテグレーションモード[#5732]()で灰色で表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5732)
* 許可が既に付与されているにもかかわらず、アプリはバックグラウンドで実行する許可を求める [#5560](https://github.com/AdguardTeam/AdguardForAndroid/issues/5560)
* DNS サーバー、拡張機能、およびフィルタのタイトルと説明は、AdGuard [#5709] で異なる言語が選択されている場合、システム言語に翻訳されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5709)
* 同じ時間に2つの類似のグラフを表示することができます [#4915](https://github.com/AdguardTeam/AdguardForAndroid/issues/4915)
* アプリのアイコンは、Amazon Fire TV Stick 4K Max [#5476] にデザインされた領域を埋めません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5476)
* `com.carshering`AdGuard [#5464] を経由してルーティングしたときに壊れています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5464)
* 「ルールを削除」をタップした後、規則はファイアウォールから削除されません [#5613](https://github.com/AdguardTeam/AdguardForAndroid/issues/5613)

### CoreLibs (フィルターエンジン)

* CoreLibs が v1.18.28 に更新されました(#5792)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5792)

#### 改善点

* ABPのCSSインジェクション・シンタックス(#1927)のサポートを追加しました。https://github.com/AdguardTeam/CoreLibs/issues/1927)
* 空の属性でコンテンツを削除する権限を追加 [#1934](https://github.com/AdguardTeam/CoreLibs/issues/1934)
* ブラウザキャッシュを適切に使用することにより、コンテンツスクリプトのパフォーマンスを改善しました [#1929](https://github.com/AdguardTeam/CoreLibs/issues/1929)
* コンテンツスクリプトの読み込みのパフォーマンスを改善しました [#1930](https://github.com/AdguardTeam/CoreLibs/issues/1930)
* 複雑なロジックを削除`$domain`修飾子 [#1875] (https://github.com/AdguardTeam/CoreLibs/issues/1875)
* 「zstd」のエンコーディングサポートを追加(#1976)https://github.com/AdguardTeam/CoreLibs/issues/1976)

#### フィックス

* `$removeparam`ペアリング時に動作しません`$domain`修飾子 [#1999] (https://github.com/AdguardTeam/CoreLibs/issues/1999)
* 一部の React ベースのサイトは “Minified React error” [#1953] で正しく読み込まれません。https://github.com/AdguardTeam/CoreLibs/issues/1953)
* `urltransform`組み合わせて`$~3p`アドレスバー[#1931]に直接開くとリクエストURLを変更しません()(https://github.com/AdguardTeam/CoreLibs/issues/1931)
* `paramountplus.com`壊れた [#1937] (https://github.com/AdguardTeam/CoreLibs/issues/1937)
* `dailydot.com`[#1925]を継続的にリロードします(https://github.com/AdguardTeam/CoreLibs/issues/1925)
* コンテンツスクリプトは注入されません`www.huya.com` [#1897](https://github.com/AdguardTeam/CoreLibs/issues/1897)
* コンテンツスクリプトのエラー`$jsinject`例外は適用されます [#1960] (https://github.com/AdguardTeam/CoreLibs/issues/1960)

### スクリプト(フィルタリングルールのJavaScript強化)
* スクリプトはv2.2.8に更新しました

#### 改善点

* scriptlet docs [#392] により多くの例を追加します。https://github.com/AdguardTeam/Scriptlets/issues/392)
* 新しいスクリプトレットを追加 — 'trusted-replace-argument' [#405]()https://github.com/AdguardTeam/Scriptlets/issues/405)
* 'prevent-fetch' を改良 — ランダムなレスポンスコンテンツをセットする機能を追加します。 [#416](https://github.com/AdguardTeam/Scriptlets/issues/416)
* 'set-cookie' を改良 — 空のオブジェクト値 [#497](https://github.com/AdguardTeam/Scriptlets/issues/497)
* AGTreeをv3に更新 [#247](https://github.com/AdguardTeam/AGLint/issues/247)

#### フィックス
* 'inject-css-in-shadow-dom' — scriptlet は use が上書きされていれば動作しません [#477](https://github.com/AdguardTeam/Scriptlets/issues/477)
* 'json-prune' を修正 — オブジェクトで指定されたキーをチェックしながら 'null' 値を扱う[#504](https://github.com/AdguardTeam/Scriptlets/issues/504)
* 'prevent-element-src-loading' を修正 — TrustedScriptURL は Firefox [#514] で定義されていません(https://github.com/AdguardTeam/Scriptlets/issues/514)
* Fix 'spoof-css' — DOMRect は正しく設定されます [#498](https://github.com/AdguardTeam/Scriptlets/issues/498)
* 'trusted-replace-node-text' — エスケープされた引用符の出力 literal quotes [#440](https://github.com/AdguardTeam/Scriptlets/issues/440)
* 'trusted-replace-node-text' を修正 — いくつかの引用符は正しくエスケープされます [#517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* 'trusted-set-cookie-reload' を修正 — 常に値を変更するための無限のリロードを防ぐ [#489](https://github.com/AdguardTeam/Scriptlets/issues/489)
* Fix 'trusted-suppress-native-method' — スタックが一致していないときに'isMatchingSuspended'をリセットする[#496](https://github.com/AdguardTeam/Scriptlets/issues/496)
* 未サポートのregexのlookbehindによるSafari 15のscriptletsコンパイルエラーを修正 [#519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.10

- 公表: 2025-06-25T17:22:52Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.10

Android v4.10用のAdGuardは、HTTPS証明書のインストールプロセスに重要な改善を導入し、ユーザーにとってより直感的でアクセスしやすいようにします。

AdGuardをインストールし、アプリを初めて起動すると、HTTPS証明書をインストールする必要があります。 このステップは、証明書がブラウザで効果的な広告フィルタリングを確実にするために重要な役割を果たしているので不可欠です。 それなしで、ろ過の質はかなり減ります。 そのため、すべてのユーザー、初心者、または上級者にとって重要な理由で、インストールを難しさずに完了することができます。

私たちは、プロセス全体の改善のための部屋があることを知っていた - 前の指示は、多くの場合、異なるメーカーからデバイス上で見つかった実際の設定を反映していないし、また、アプリを離れた後、ユーザーに指示に戻るのを防ぐバグがありました。

これらの問題に対処するため、Googleピクセル、Samsung、Huawei、Xiaomi、OnePlusなどの最も一般的なデバイス用のアプリ内ガイドを追加し、Android OSバージョンとユーザーロケールに基づいて調整します。 上記のバグも修正しました。

## 変更履歴

### 改善点
* LemurブラウザのデフォルトでHTTPSフィルタリングを追加 [#5577](https://github.com/AdguardTeam/AdguardForAndroid/issues/5577)

### フィックス
* WebViewが停止または更新されたときにAdGuardが無効になります [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)
* Tor との統合後、Orbot 経由の Tor はデフォルトのプロキシではありません [#4908](https://github.com/AdguardTeam/AdguardForAndroid/issues/4908)
* アプリが再起動した後に更新されたフィルタは表示されません [#5638](https://github.com/AdguardTeam/AdguardForAndroid/issues/5638)
* QUIC のフィルタリングは WeChat および AliExpress [#5497] のために無効になります(https://github.com/AdguardTeam/AdguardForAndroid/issues/5497)
* WeChat は、デフォルトで HTTPS フィルタリングから除外されます [#5689](https://github.com/AdguardTeam/AdguardForAndroid/issues/5689)
* アプリが完全に翻訳されていない [#5418](https://github.com/AdguardTeam/AdguardForAndroid/issues/5418)
* [#5701] を 2 回変更すると、フィルタリング状態が保存されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5701)
* 最近の活動ログはゆっくりとスクロールするときに遅れ [#5369] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5369)
* 誤ったブロックを報告するときにリンクにいくつかのパラメータは含まれていません [#5520](https://github.com/AdguardTeam/AdguardForAndroid/issues/5520)
* ブラウザでリンクを開くと、2つのAdGuardアプリがブラウザのリストに表示され、そのうちの1つは期待どおりに動作しません[#5592](https://github.com/AdguardTeam/AdguardForAndroid/issues/5592)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.17.157 に更新されました(#5725)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5725)

#### フィックス
* Naver Smartstore が正常にアクセスできない [#1971](https://github.com/AdguardTeam/CoreLibs/issues/1971)
* React ベースのウェブサイトが正しくロードされていないものもあります。`Minified React error` [#1953](https://github.com/AdguardTeam/CoreLibs/issues/1953)
* ドメインのユーザールールは完全にリクエストをブロックしない[#5539](https://github.com/AdguardTeam/AdguardForAndroid/issues/5539)

### DnsLibs (DNSのろ過エンジン)
* DnsLibs が v2.6.6 に更新 [#5724](https://github.com/AdguardTeam/AdguardForAndroid/issues/5724)

### スクリプト(フィルタリングルールのJavaScript強化)
* Scriptlets が v2.1.7 に更新されました。

#### 改善点
*  'prevent-addEventListener' — 特定の要素にマッチする機能を追加しました [#480](https://github.com/AdguardTeam/Scriptlets/issues/480)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.9

- 公表: 2025-04-03T18:22:43Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9

Android 用の AdGuard v4.9 で主要な機能を追加しました。: ユーザスタイルのためのネイティブサポート。 この機能は、しばらくの間、Mac用のWindowsとAdGuard用のAdGuardで利用可能であり、今ではAndroid用のAdGuardにそれを持参しています!

Userstyles は userscripts に似ていますが、CSS を使用してウェブサイトの外観を変更するだけに焦点を当てています。 今、ウェブサイトをカスタマイズ — 暗いテーマを追加するような - 簡単なタスクになります。 アプリ自体で独自のユーザースタイルを作成したり、信頼できる[オンラインソース]から既製のスタイルをインストールしたりできます。https://userstyles.world/).

![Wikipedia with userstyle](ユーザースタイル)https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.9/styled_wikipedia.jpg)

ユーザスタイルを追加するには、*Settings* → *Filtering* → *Extensions*→ *Add extension* → *ファイルやURL*からインポートします。 独自のスタイルを作成するには、*Add extension* → *Create userstyle* をタップします。

![アプリでユーザスタイルをインストール](https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.9/Userstyles_en.jpg)

また、一部のユーザーは最近、巨大な値を取り除くために統計量が増えていたバグに直面している可能性があります。 問題を修正し、Android 用の AdGuard v4.9 をインストールしたら、 *Statistics* タブの正規番号が表示されます。

> 過去24時間以上前に蓄積された統計は大きく剪定されますのでご注意ください。

この問題以外にも、小さなバグの修正にも取り組んでいます。 いつものように、アプリの機能性を改善するためにCoreLibsとScriptletsを更新しました。

## 変更履歴

### 改善点
* デフォルトでMSNブラウザのサポートを追加しました [#5533](https://github.com/AdguardTeam/AdguardForAndroid/issues/5533)
* com.irobot.home を追加 ルーティング 除外 [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### フィックス
* 統計的なカウンターの請求値が省略に変換されない[#5633](https://github.com/AdguardTeam/AdguardForAndroid/issues/5633)
* AdGuardの保護ステータス通知をクリックすると、Amazon Fire TV Stick [#5498] のモバイルビューが表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5498)
* DNS フィルターの切り替えが無効になっていれば、DNS フィルターの更新ができるようになりました [#5382](https://github.com/AdguardTeam/AdguardForAndroid/issues/5382)
* ドメインとドメイン`$app`modifier は HTTPS フィルタリングされたウェブサイトの除外 [#5587] に追加できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5587)
* オプション *Filter は、再起動後自身で DNS* の変更をセキュアにします [#5379](https://github.com/AdguardTeam/AdguardForAndroid/issues/5379)
* 統計バーは、 *Statistics* タブ [#5138] のカウンターの説明をオーバーラップします(https://github.com/AdguardTeam/AdguardForAndroid/issues/5138)
* Androidシステムの更新をダウンロードできません [#5651](https://github.com/AdguardTeam/AdguardForAndroid/issues/5651)
* Android TVでAdguard Ad Blockerアプリにログインできない
[#5669](https://github.com/AdguardTeam/AdguardForAndroid/issues/5669)

### CoreLibs (フィルタリングエンジン)
* CoreLibs が v1.17.118 に更新されました [#5654](https://github.com/AdguardTeam/AdguardForAndroid/issues/5654)

#### フィックス
* ハンドル付き ClientHello フラグメンテーション [#1968](https://github.com/AdguardTeam/CoreLibs/issues/1968)
* 大きいHTMLの訂正された長い処理の時間[#1886] (https://github.com/AdguardTeam/CoreLibs/issues/1886)

### スクリプト(フィルタリングルールのJavaScript強化)
* Scriptlets が v2.1.6 に更新

#### フィックス
* 固定式`json-prune`— 配列の内容が誤って削除された[#482](https://github.com/AdguardTeam/Scriptlets/issues/482)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7.2

- 公表: 2025-06-26T16:42:05Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7.2

このアップデートでは、以前のリリースでスリップした問題を完全に修正しました。AdGuard保護は、WebViewが停止または更新されたときにシャットオフされます。 このバージョンでは、Android 7 と 8 のユーザーは、最終的に途切れない保護を楽しむことができます。

## 変更履歴

### フィックス
* WebViewが停止または更新されたときにAdGuardが無効になります [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)

## 4.9 RC 1

- 公表: 2025-03-27T17:01:06Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9-rc-1

このRCでの主な機能を追加しました: ユーザスタイルのネイティブサポートを歓迎します。 この機能は、しばらくの間、Mac用のWindowsとAdGuard用のAdGuardで利用可能であり、今ではAndroid用のAdGuardにそれを持参しています!

Userstyles は userscripts の代わりに似ていますが、CSS を使ってウェブサイトの外観を変更することだけに焦点を当てています。 今、選択したウェブサイトをカスタマイズする - 暗いテーマを追加するような - 簡単なタスクになります。 アプリ自体で独自のユーザースタイルを作成したり、信頼できる[オンラインソース]から既製のスタイルをインストールしたりできます。https://userstyles.world/).

ユーザスタイルを追加するには、*Settings* → *Filtering* → *Extensions*→ *Add extension* → *ファイルやURL*からインポートします。 独自のスタイルを作成するには、*Add extension* → *Create userstyle* をクリックします。

バグの修正とCoreLibsの更新中にアプリをより良いものにし続けています。

## 変更履歴

### コアライブラリ

* CoreLibs は 1.17.118 [#5673] に更新されました。https://github.com/AdguardTeam/AdguardForAndroid/issues/5673)

#### フィックス

* 固定 ClientHello フラグメンテーション [#1968](https://github.com/AdguardTeam/CoreLibs/issues/1968)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.9 ベータ 1

- 公開日: 2025-03-20T17:35:30Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9-beta-1

このベータ版では、UIのバグや不具合を修正し、CoreLibsとScriptletsモジュールにタイムリーなアップデートをもたらすと、アプリをより良いものにするためのクエストを継続しています。 以下は、タンジェログの詳しい内容です。

## 変更履歴

### 改善点

* デフォルトでMSNブラウザのサポートを追加しました [#5533](https://github.com/AdguardTeam/AdguardForAndroid/issues/5533)
* 追加`com.irobot.home`AdGuardの除外によるトラフィックのルート化 [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### フィックス

* 統計的なカウンターの請求値が省略に変換されない[#5633](https://github.com/AdguardTeam/AdguardForAndroid/issues/5633)
* AdGuardの保護ステータス通知をクリックすると、Amazon Fire TV Stick [#5498] のモバイルビューが表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5498)
* DNS フィルターが無効になっている場合は、DNS フィルターが更新されます[#5382](https://github.com/AdguardTeam/AdguardForAndroid/issues/5382)
* ドメインとドメイン`$app`modifier は HTTPS フィルタリングされたウェブサイトの除外 [#5587] に追加できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5587)
* [#5379] を再起動した後、オプション "Filter secure DNS" 自体が変更されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/5379)
* 統計バーは、統計タブでカウンターの説明をオーバーラップ [#5138](https://github.com/AdguardTeam/AdguardForAndroid/issues/5138)

### CoreLibs (フィルタリングエンジン)
* CoreLibs が v1.17.108 に更新されました [#5654](https://github.com/AdguardTeam/AdguardForAndroid/issues/5654)

#### フィックス

* コンテンツスクリプトのエラー`$jsinject`例外は適用されます [#1960] (https://github.com/AdguardTeam/CoreLibs/issues/1960)
* スクリプトが正しく動作しない特別なホワイトリスト例外 [#1959](https://github.com/AdguardTeam/CoreLibs/issues/1959)

#### その他

* CoreLibs 1.17ブロックアクセス`ota.googlezip.net` [#1963](https://github.com/AdguardTeam/CoreLibs/issues/1963)

### スクリプト(フィルタリングルールのJavaScript強化)
* Scriptlets が v1.11.27 に更新

#### フィックス

* 固定式`json-prune`— 配列の内容が誤って削除される[#482](https://github.com/AdguardTeam/Scriptlets/issues/482)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.13 ベータ 1

- 公表: 2026-07-17T11:41:50Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13-beta-1

Android v4.13用のAdGuardのこのベータが少しのラジオサイレンス後に転がっている場合、私たちが設定した目標は、計画よりも現実的にさらに大きくなることを意味します。 ボード全体で多くの作業が行われ、次のステップの準備ができました。リリースバージョン。

このベータ版では、Android用のAdGuardに差動フィルタの更新を導入しました! これを実現するために、フィルタリストマネージャライブラリをアプリに統合しました。 これで、たくさんのトラフィックを消費せずに自動的にフィルタがロードされます。

また、DnsLibs にポスト量暗号化サポートを追加しました。 AdGuardは、他のフルアドブロック製品と同様に、将来の脅威からDNSリクエストを保護します。

もう1つの重要な変更は、MozillaによるCRLiteの採用によって、再発された証明書を検証することです。 より古いOCSP(オンライン証明書ステータスプロトコル)の代わりに、またはCRL(証明書の取消リスト)に対する各証明書を、Webサイトの読み込みをスピードアップするだけでなく、閲覧中にプライバシーと安全を向上させることができます。

そして最後に、しかし、少なくとも、我々は私たちのフィルタリングエンジンと時間をかけて蓄積した固定バグに多くの仕事をしてきました。 スクリプトとCoreLibsは、より良いアプリのパフォーマンスのために更新されました。

修正や改善の全てをご覧いただけます。

## 変更履歴


### 改善点
* フィルタリングログ [5637] で詳細に適用される規則をコピーする可能性を追加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5637)
* Googleバックアップのサポートを追加 [5879](https://github.com/AdguardTeam/AdguardForAndroid/issues/5879)
* デフォルトでフィルタリングから2ndLineアプリケーションを除外 [5116](https://github.com/AdguardTeam/AdguardForAndroid/issues/5116)
* DNS リストの DNS フィルターの更新に関する情報を表示 [5519](https://github.com/AdguardTeam/AdguardForAndroid/issues/5519)
* フィルタリングログ [5636] の詳細は、package name のリクエストをコピーする可能性を追加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5636)
* 更新チェック画面を改善しました。*更新チェックボタン [5923](https://github.com/AdguardTeam/AdguardForAndroid/issues/5923)
* 最近の活動タブ[5193]を経由して空のユーザールールを追加する可能性を排除しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5193)
* *Updates*画面に更新されたコンテンツのカラー差別化を追加 [5886](https://github.com/AdguardTeam/AdguardForAndroid/issues/5886)
* *プライベートブラウザ*のトークバックボイスアシスタントの要素の改善*
* *追跡保護*の入力/ダイアログを再構成しました
* クラッシュレポートとアプリの使用データ名とダイアログを更新
* 最近の活動で適用される規則によって要求を見つけるオプションを追加しました
* ※IP*アドレス画面をマークする
* *Webサイト保護*スイッチを*プライベートブラウザ*に切り替えた後、Webページの自動更新を追加
* ローカルプロキシの認証を追加
* クリアする可能性を追加`.hprof`必要なくない場合
* TV用のアプリ更新エラー画面を追加しました

### フィックス
* ブロックルール`$network`リクエスト詳細に規則*ボタンを許可する追加で追加されます[5390](https://github.com/AdguardTeam/AdguardForAndroid/issues/5390)
* *Disable all?* ポップアップは、ルールリストが空の場合でも、*ユーザールール*画面に表示されます[5175](https://github.com/AdguardTeam/AdguardForAndroid/issues/5175)
* CA 証明書のインストール手順は、ColorOS [5827] には関係ありません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5827)
* DNS フィルターの表示`null`最後の更新の代わりに [5902](https://github.com/AdguardTeam/AdguardForAndroid/issues/5902)
* *Usage access* システム許可[5927]を付与した後に自動的に防火壁が活動化します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5927)
* v4.12(5893)から始まる高電池消費量https://github.com/AdguardTeam/AdguardForAndroid/issues/5893)
* ドメインをブロックし、DNSフィルタでブロック解除し、フィルタリングログのみ[5880](https://github.com/AdguardTeam/AdguardForAndroid/issues/5880)
* 誤ったサブドメインが統計で表示されます [5868](https://github.com/AdguardTeam/AdguardForAndroid/issues/5868)
* 多くのアプリは、AdGuardがアクティブなときに動作を停止します [5617](https://github.com/AdguardTeam/AdguardForAndroid/issues/5617)
* 最近の活動ログはv4.12.1に更新した後に大きく遅れる [5882](https://github.com/AdguardTeam/AdguardForAndroid/issues/5882)
* 英語以外の言語モードで拡張機能を編集する際の問題 [5914](https://github.com/AdguardTeam/AdguardForAndroid/issues/5914)
* 最近の活動ログは、AdGuard v4.14 夜 4 で即座に消去されなかった [5908](https://github.com/AdguardTeam/AdguardForAndroid/issues/5908)
* *Statistics* [5840] で重複するサブドメイン (https://github.com/AdguardTeam/AdguardForAndroid/issues/5840)
* カスタムDNSサーバーは、単にエクスポートされた設定をインポートした後に消え [5892](https://github.com/AdguardTeam/AdguardForAndroid/issues/5892)
* 水平モード [5612] で共有ボタンをクリックすると、動画のタイトルが最小化されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5612)
* タイルを使用してAdGuardをオンにして通知パネルを閉じる[5915](https://github.com/AdguardTeam/AdguardForAndroid/issues/5915)
* 許可なしのフィルター更新 [5309](https://github.com/AdguardTeam/AdguardForAndroid/issues/5309)
* *Ad blocking* および *DNS filtering* のユーザレグテックスは、AdGuard v4.14 夜 5 [5916] 以降に動作します。https://github.com/AdguardTeam/AdguardForAndroid/issues/5916)
* ベータ版(RCなど)を更新しようとすると、アップデートは最新のリリース版[5920]に進みます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5920)
* 設定は、バージョンが一貫した場合でも、リンクを介してインポートできません[5912](https://github.com/AdguardTeam/AdguardForAndroid/issues/5912)
* *適用規則*セクションで自分自身を複製するルール
* AdGuard Personal CA をアプリの *Move* ボタンでシステムストアに移動できなかった
* カスタムコンテンツフィルタリストは時間後に消えます
* 保護は*HTTPSのろ過*および*FakeDNS*によって可能にされるあらゆる秒を再開します
* userscript を編集した後にエラースナックが表示されます
* 設定名をタップすると、拡張子設定のスイッチは応答しません
* 電話を再起動した後、ブロックされたURLは、ログにブロックされた理由を示すことはありません
* ※ホットスポットがアクティブである間、保護が正常に動作しない場合があります* 通知はAndroid 10以降で表示されます
* *Recent アクティビティ* から追加の修飾子でブロックルールを追加できません。
* *Saveとselect*をタップすることで、カスタムDNSサーバーを選択可能
* 実際の DNS プロトコルは、設定のインポート後に *DNS サーバの詳細* 画面に表示されているものと一致しません。
* 拡張エディタを開くと、ナビゲーションバーの下の空スペース
* AdGuardは再起動後に起動しません
* リンクを介して設定をインポートする際に、証明書のインストールのオンボーディングの誤った表示
* 統合モード対話は、アプリの最初の起動時に一貫して開いていません
* リクエスト詳細から返された後、ヘッダが崩壊しなかった場合は、*Recent アクティビティ*画面にクエリを検索しない
* DNS プロバイダーの *Open* ボタンは、ブラウザが開いているが、Xiaomi TV Box の Web サイトが表示されない
* ※ライセンスチェックタイムアウト後の*TVライセンス*画面にライセンス情報*スナックが表示されない
* TVの*License*スクリーンの*Refreshの状態*ボタンを押した後にデフォルトに焦点を合わせて下さい
* *証明書がインストールされていない*ダイアログは、設定共有による証明書のインストール後に表示されます。
* フィルター更新後にカスタムフィルタバージョンが更新されていない
* *Ruleエディタ*のキーボードによってカバーされるテキストのクリッピング、ヘッダーの重複、および内容
* AdGuardプレーヤーのYouTubeボタンが動画を再起動します
* *Quick action*画面ファイアウォール通知は、*Show blocked only*フィルタが選択されたときにブロックされたアプリと許可されたアプリの両方で表示されます。
* スクロール *ユーザールール* 別のビューを重ねる
* スクロールフォーカスは、テレビで*アプリ管理*の急激なスクロール中にビューポートから動き出します
* YouTube MusicからAdGuardプレーヤーへの共有は機能しません
* AdGuardの通知は、デバイスの画面をスリープモードから引き出します。
* *プライベートブラウザ*は、他のアプリはWebページから開くことはありません。
* フィルタルールエディタは、構文検証なしで有効なルールとして、任意の非空の文字列を受け入れます
* ※プライベートブラウザ*を閉じた後、動的テーマはアドガードアプリには適用されません。
* UI レイヤーは、AdGuard プレーヤーの PiP モードで修正されました
* Kazakh または Kyrgyz をシステム言語として使用して、AdGuard はロシアとしてそれを誤って表示します
* hieroglyphs を使用する言語の通知では、ブロックされたリクエストの数が誤って表示されます。

### DnsLibs (DNSのろ過エンジン)
* DnsLibsをv2.8.45に更新 [5961](https://github.com/AdguardTeam/AdguardForAndroid/issues/5961)

#### 改善点
* DnsLibs へのポスト量子暗号化サポートを追加 [245]()https://github.com/AdguardTeam/DnsLibs/issues/245)
* 削除するオプションを追加`h3`から`alpn`HTTPS RRのパラメーター [257](https://github.com/AdguardTeam/DnsLibs/issues/257)
 * テストの信頼性を改善しました。 DoT アップストリームの可用性 [263] (https://github.com/AdguardTeam/DnsLibs/issues/263)
* フィルターをリロードすることなくDNSアップストリームリストの更新を改善 [248](https://github.com/AdguardTeam/DnsLibs/issues/248)

#### フィックス
* DNSのブロック解除ルールは動作しません
* 時折、システム:// 上流応答は、Android上で受け入れられなかった [265](https://github.com/AdguardTeam/DnsLibs/issues/265)
* hitomi.laのような一部のウェブサイトでAdGuardの証明書を見逃す [2055](https://github.com/AdguardTeam/CoreLibs/issues/2055)

### CoreLibs (フィルターエンジン)

* CoreLibsをv1.21.38に更新

#### 改善点
* URL のデコードをサポート`$urltransform` [1915](https://github.com/AdguardTeam/CoreLibs/issues/1915)
* ベータ/ナイトリービルドでデフォルトで HTTP/3 フィルタリングを有効にしました [2014](https://github.com/AdguardTeam/CoreLibs/issues/2014)
* 例.org/path 化粧品規則 [2012] のサポートを追加しました。https://github.com/AdguardTeam/CoreLibs/issues/2012)
* 新しいサポートを追加`$reason`修飾子 [1986](https://github.com/AdguardTeam/CoreLibs/issues/1986)
* *Do Not Track* 動作改善 (1982)https://github.com/AdguardTeam/CoreLibs/issues/1982)
* 保護を有効にした後、 local.adguard.org DNS の漏洩を防止 [1854](https://github.com/AdguardTeam/CoreLibs/issues/1854)
* 安定ビルドでデフォルトで HTTP/3 フィルタリングを有効にしました [2015](https://github.com/AdguardTeam/CoreLibs/issues/2015)

#### フィックス
* 誤った証明書シリアル番号マーシャリングが偽陽性CRLiteマッチにつながり [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* リクエストの詳細では、AdGuard VPN との統合が有効になっている場合、*Destination アドレス* は 127.0.0.1 と表示されます。
* 高度なオプション*チェックウェブサイトの証明書の透明性*が有効になっている場合は、AdGuard証明書はありません[2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* CoreLibs v1.19の接続リセット
* localhost は v1.19 [2019] の手動プロキシモードでは到達できません。https://github.com/AdguardTeam/CoreLibs/issues/2019)
* AdGuard VPN との統合が有効になっている場合は、*Request の詳細* に間違った宛先アドレスが表示される [2021](https://github.com/AdguardTeam/CoreLibs/issues/2021)
* BOM(2009年)によるユーザスクリプトのインポート失敗https://github.com/AdguardTeam/CoreLibs/issues/2009)
* プロキシ設定でFakeDNSが使用されているときに壊れた注射[2017](https://github.com/AdguardTeam/CoreLibs/issues/2017)
* スペースでスクリプトタグを閉じる壊れた処理[2042](https://github.com/AdguardTeam/CoreLibs/issues/2042)
* エラー`$generichide`ドメインスコープルールの動作 [2041](https://github.com/AdguardTeam/CoreLibs/issues/2041)
* 高度なオプション*チェックウェブサイトの証明書の透明性*が有効になっている場合は、AdGuard証明書が不在です[2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* 誤った証明書シリアル番号マーシャリングが偽陽性CRLiteマッチにつながり [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* QUIC/HTTP/3 フィルタリングの高レイテンシは、プロトコルが HTTP/2 [2062] にフォールバックする原因https://github.com/AdguardTeam/CoreLibs/issues/2062)

### スクリプト(フィルタリングルールのJavaScript強化)
* スクリプトをv2.2.16に更新

#### 改善点
* 新しいスクリプトレットを追加 —`prevent-innerHTML` [488](https://github.com/AdguardTeam/Scriptlets/issues/488)
* 改善しました`fingerprintjs2`— サポートウィンドウ [541](https://github.com/AdguardTeam/Scriptlets/issues/541)
* 期間を増加させるパラメータを追加`trusted-click-element`scriptletの実行期間 [400](https://github.com/AdguardTeam/Scriptlets/issues/400)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12 RC 1

- 公表: 2025-09-30T22:36:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12-rc-1

AdGuard for Android v4.12のリリース候補が公開されました。 弊社では、RCバージョンのリリースは、公式リリース前の新機能をテストするための素晴らしい方法です。 ユーザにとっては、最初に試してみる機会です。 皆様のお越しをお待ちしております!

## 変更履歴

### 改善点
* アプリが正しく動作するように、com.bKash.customerapp 用の「AdGuard によるルートトラフィック」オプションを無効にしました [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### フィックス
* CA 証明書のインストール手順は、名誉 [#5779] には関係ありません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* アプリ固有の HTTPS 除外 [#5290] を追加できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* 更新セクション[#5821]にカスタムDNSフィルタが表示されない(https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* スナックバーにクロスをタッピングして、新しいアプリバージョンをダウンロードしてもダウンロードを停止しない[#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* AdGuard のフィルタリング [#5819] による銀行アプリで一部の画像が欠落しています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)
* プロキシサーバーに接続できない [#5794](https://github.com/AdguardTeam/AdguardForAndroid/issues/5794)
* DNS フィルターは適用しません [#5851] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### CoreLibs (フィルターエンジン)

* 更新されたCoreLibsにv1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### 改善点

* 改善された`$app`修飾語:ワイルドカードと正規表現のサポートを追加
[1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* ALPSエクステンションのサポートを追加 [1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### フィックス

* ログ[#5739]に表示されている間違った追跡保護オプション(https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* パフォーマンス警告(new.lewd.ninja)による一部のウェブサイトで無効なフィルタリング [1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* プロキシサーバーの「FakeDNS」オプションは、バイパスされたアプリの接続を中断 [5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* 更新後にv2.17 [1993]( 更新後、一部の拡張子は動作しません)https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHRタイムアウトとXHRタイムアウト`immersivetranslate`ユーザスクリプト [2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* コンテンツタイプの修飾子は機能しません`$urltransform`修飾子 [1978](https://github.com/AdguardTeam/CoreLibs/issues/1978)

### DnsLibs (DNSのろ過エンジン)

* DnsLibsをv2.6.20に更新 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### スクリプト(フィルタリングルールのJavaScript強化)

* スクリプトをv2.2.9に更新しました

#### 改善点
* 新しいスクリプトレットを追加 — 'trusted-replace-argument' [405]()https://github.com/AdguardTeam/Scriptlets/issues/405)

#### フィックス
* 'prevent-element-src-loading' — TrustedScriptURL は Firefox [514] で定義されていません。https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — 引用符は正しくエスケープされます [517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* 未サポートの正規表現によるSafari 15のコンパイルエラー [519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.12 ベータ 1

- 公開日: 2025-09-29T21:42:10Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12-beta-1

私たちはいつも言うように、あなたのフィードバックは私たちにとって本当に重要であり、今回は私たちが最も要求された機能の1つを追加しました。 タブレットでAdGuardを使うと、より便利になりました。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/tablet_en.png"幅="700">
</p>

リンクで設定インポートも導入しました。 この機能は時間を節約します。新しいデバイスですべてを再構成したり、ミスされた広告を報告するときにセットアップを記述する時間を費やす必要はありません。リンクを共有するだけです。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/share_en.png"幅="300">
</p>

## 変更履歴

### 改善点
* アプリが正しく動作するように、com.bKash.customerapp 用の「AdGuard によるルートトラフィック」オプションを無効にしました [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### フィックス
* CA 証明書のインストール手順は、名誉 [#5779] には関係ありません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* アプリ固有の HTTPS 除外 [#5290] を追加できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* 更新セクション[#5821]にカスタムDNSフィルタが表示されない(https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* スナックバーにクロスをタッピングして、新しいアプリバージョンをダウンロードしてもダウンロードを停止しない[#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* AdGuard のフィルタリング [#5819] による銀行アプリで一部の画像が欠落しています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)
* プロキシサーバーに接続できない [#5794](https://github.com/AdguardTeam/AdguardForAndroid/issues/5794)
* DNS フィルターは適用しません [#5851] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### CoreLibs (フィルターエンジン)

* 更新されたCoreLibsにv1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### 改善点

* 改善された`$app`修飾語:ワイルドカードと正規表現のサポートを追加
[1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* ALPSエクステンションのサポートを追加 [1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### フィックス

* ログ[#5739]に表示されている間違った追跡保護オプション(https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* パフォーマンス警告(new.lewd.ninja)による一部のウェブサイトで無効なフィルタリング [1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* プロキシサーバーの「FakeDNS」オプションは、バイパスされたアプリの接続を中断 [5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* 更新後にv2.17 [1993]( 更新後、一部の拡張子は動作しません)https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHRタイムアウトとXHRタイムアウト`immersivetranslate`ユーザスクリプト [2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* コンテンツタイプの修飾子は機能しません`$urltransform`修飾子 [1978](https://github.com/AdguardTeam/CoreLibs/issues/1978)

### DnsLibs (DNSのろ過エンジン)

* DnsLibsをv2.6.20に更新 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### スクリプト(フィルタリングルールのJavaScript強化)

* スクリプトをv2.2.9に更新しました

#### 改善点
* 新しいスクリプトレットを追加 — 'trusted-replace-argument' [405]()https://github.com/AdguardTeam/Scriptlets/issues/405)

#### フィックス
* 'prevent-element-src-loading' — TrustedScriptURL は Firefox [514] で定義されていません。https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — 引用符は正しくエスケープされます [517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* 未サポートの正規表現によるSafari 15のコンパイルエラー [519](https://github.com/AdguardTeam/Scriptlets/issues/519)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.11 ベータ 1

- 公開日: 2025-08-14T15:04:09Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.11-beta-1

このベータには、いくつかのアンダーフードの改善、大量のバグ修正、CoreLibsアップデートが含まれています。 その結果、アプリ全体の安定性が大幅に向上しました。

## 変更履歴

### フィックス
* Createボタンは、トライアルアクティベーション画面のチェックボックスをオーバーラップ [#5039](https://github.com/AdguardTeam/AdguardForAndroid/issues/5039)
* YouTubeアプリから動画を共有するときにAdGuardプレーヤーが開いていない[#5780](https://github.com/AdguardTeam/AdguardForAndroid/issues/5780)
* AdGuard は、統合モード [#5567] でサードパーティの VPN として AdGuard VPN を識別します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5567)
* UIDが除外するアプリは、AdGuard [#5731] を介してルーティングされています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5731)
* 日本語、韓国語、中国語の無効なフィルタ更新日フォーマット [#5703](https://github.com/AdguardTeam/AdguardForAndroid/issues/5703)
* プライベートブラウザ通知の文字列を欠く [#5741](https://github.com/AdguardTeam/AdguardForAndroid/issues/5741)
* 専用ブラウザのオンボーディングが2回表示されます[#5752](https://github.com/AdguardTeam/AdguardForAndroid/issues/5752)
* ブラウザの設定をタップした後、プライベートブラウザがクラッシュ [#5781](https://github.com/AdguardTeam/AdguardForAndroid/issues/5781)
* 「Nothing found」の警告は、いくつかの画面で欠落しています [#5038](https://github.com/AdguardTeam/AdguardForAndroid/issues/5038)
* 「プロキシで動作するアプリ」画面は、インテグレーションモード[#5732]()で灰色で表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5732)
* 許可が既に付与されているにもかかわらず、アプリはバックグラウンドで実行する許可を求める [#5560](https://github.com/AdguardTeam/AdguardForAndroid/issues/5560)
* DNS サーバー、拡張機能、およびフィルタのタイトルと説明は、AdGuard [#5709] で異なる言語が選択されている場合、システム言語に翻訳されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5709)
* 同じ時間に2つの類似のグラフを表示することができます [#4915](https://github.com/AdguardTeam/AdguardForAndroid/issues/4915)
* アプリのアイコンは、Amazon Fire TV Stick 4K Max [#5476] にデザインされた領域を埋めません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5476)
* `com.carshering`AdGuard [#5464] を経由してルーティングしたときに壊れています(https://github.com/AdguardTeam/AdguardForAndroid/issues/5464)
* 「ルールを削除」をタップした後、規則はファイアウォールから削除されません [#5613](https://github.com/AdguardTeam/AdguardForAndroid/issues/5613)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.18.28 に更新されました(#5792)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5792)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.10 ベータ 1

- 公表: 2025-06-17T11:54:02Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.10-beta-1

このベータは、HTTPS 証明書のインストールプロセスに重要な改善を導入し、より直感的でユーザーのためにアクセス可能にします。

AdGuardをインストールし、アプリを初めて起動すると、HTTPS証明書をインストールする必要があります。 このステップは、証明書がブラウザで効果的な広告フィルタリングを確実にするために重要な役割を果たしているので不可欠です。 それなしで、ろ過の質はかなり減ります。 そのため、すべてのユーザー、初心者、または上級者にとって重要な理由で、インストールを難しさずに完了することができます。

私たちは、プロセス全体の改善のための部屋があることを知っていた - 前の指示は、多くの場合、異なるメーカーからデバイス上で見つかった実際の設定を反映していないし、また、ユーザーがアプリから離れて切り替えた後、指示に戻るのを防ぐバグがありました。

これらの問題に対処するため、Googleピクセル、Samsung、Huawei、Xiaomi、OnePlusなどの最も一般的なデバイス用のアプリ内ビデオガイドを追加し、Android OSバージョンとユーザーロケールに基づいて調整します。 上記のバグも修正しました。

## 変更履歴

### 改善点
* LemurブラウザのデフォルトでHTTPSフィルタリングを追加 [#5577](https://github.com/AdguardTeam/AdguardForAndroid/issues/5577)

### フィックス
* WebViewが停止または更新されたときにAdGuardが無効になります [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)
* Tor との統合後、Orbot 経由の Tor はデフォルトのプロキシではありません [#4908](https://github.com/AdguardTeam/AdguardForAndroid/issues/4908)
* アプリが再起動した後に更新されたフィルタは表示されません [#5638](https://github.com/AdguardTeam/AdguardForAndroid/issues/5638)
* QUIC のフィルタリングは WeChat および AliExpress [#5497] のために無効になります(https://github.com/AdguardTeam/AdguardForAndroid/issues/5497)
* WeChat は、デフォルトで HTTPS フィルタリングから除外されます [#5689](https://github.com/AdguardTeam/AdguardForAndroid/issues/5689)
* アプリが完全に翻訳されていない [#5418](https://github.com/AdguardTeam/AdguardForAndroid/issues/5418)
* [#5701] を 2 回変更すると、フィルタリング状態が保存されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5701)
* 最近の活動ログはゆっくりとスクロールするときに遅れ [#5369] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5369)
* 誤ったブロックを報告するときにリンクにいくつかのパラメータは含まれていません [#5520](https://github.com/AdguardTeam/AdguardForAndroid/issues/5520)
* ブラウザでリンクを開くと、2つのAdGuardアプリがブラウザのリストに表示され、そのうちの1つは期待どおりに動作しません[#5592](https://github.com/AdguardTeam/AdguardForAndroid/issues/5592)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.17.157 に更新されました(#5725)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5725)

#### フィックス
* Naver Smartstore が正常にアクセスできない [#1971](https://github.com/AdguardTeam/CoreLibs/issues/1971)
* React ベースのウェブサイトが正しくロードされていないものもあります。`Minified React error` [#1953](https://github.com/AdguardTeam/CoreLibs/issues/1953)
* ドメインのユーザールールは完全にリクエストをブロックしない[#5539](https://github.com/AdguardTeam/AdguardForAndroid/issues/5539)

### DnsLibs (DNSのろ過エンジン)
* DnsLibs が v2.6.6 に更新 [#5724](https://github.com/AdguardTeam/AdguardForAndroid/issues/5724)

### スクリプト(フィルタリングルールのJavaScript強化)
* Scriptlets が v2.1.7 に更新されました。

#### 改善点
*  'prevent-addEventListener' — 特定の要素にマッチする機能を追加しました [#480](https://github.com/AdguardTeam/Scriptlets/issues/480)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.8

- 公開日: 2025-02-17T17:20:34Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8

今後も、製品のコードベースを統一し、Android用のAdGuardは例外ではありません。 アップデートは、より安定化され、新機能が追加されます。 また、新しいバージョンでは、統計データやCoreLibsやDnsLibsの更新など、大量のデータの読み込みを加速しました。

> このバージョンから、Android用のAdGuardは、Android 9以上をサポートしています。

## 変更履歴

### フィックス
* Beeline Wi-Fi 呼び出しは動作しません [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)
* CPU 背景値が大幅に増加し、いくつかのシリーズの終了/アプリの開始 [#5504](https://github.com/AdguardTeam/AdguardForAndroid/issues/5504)
* カスタムDNSは設定をインポートした後に動作しません[#5618](https://github.com/AdguardTeam/AdguardForAndroid/issues/5618)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.17.88 に更新されました(#5620)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5620)

### DnsLibs (DNSのろ過エンジン)
* dnsLibs が v2.5.63 に更新 [#5607](https://github.com/AdguardTeam/AdguardForAndroid/issues/5607)

#### 改善点
* 追加`matter._tcp.default.service.arpa`デフォルト除外リストへ [#230](https://github.com/AdguardTeam/DnsLibs/issues/230)
* ブロックRFC9462 ( dns.resolver.arpa) 問い合わせ [#228](https://github.com/AdguardTeam/DnsLibs/issues/228)
* 使用条件`pretty_str()`エラーで報告`DnsRequestProcessedEvent` [#223](https://github.com/AdguardTeam/DnsLibs/issues/223)

#### フィックス
* DNS[#1887]でブロックするときの応答のための長い待ち時間(https://github.com/AdguardTeam/CoreLibs/issues/1887)
* `$dnsrewrite=IPv4`ルールはIPv6解像度をブロックしません [#224](https://github.com/AdguardTeam/DnsLibs/issues/224)

### ユーザースクリプトWrapper

* UserscriptsWrapperがv2.0.1に更新

### スクリプト(フィルタリングルールのJavaScript強化)

* スクリプトはv2.1.4に更新しました

#### 改善点
* `trusted-click-element`— チェック`containsText`すべての一致したセレクター [#468](https://github.com/AdguardTeam/Scriptlets/issues/468)

#### フィックス
* `trusted-click-element`— 要素が削除され、[#391] をクリックする前に再び追加されました(https://github.com/AdguardTeam/Scriptlets/issues/391)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.8 RC 2

- 公開日: 2025-02-15T11:47:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-rc-2

広告ブロックは妥協していたが、長期間は許さない:[ユーザーによって報告された迷惑なバグ]を修正しました()https://github.com/AdguardTeam/AdguardForAndroid/issues/5604) ライブラリを更新し、その中にライブラリを更新します。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.8 RC 1

- 公表: 2025-02-11T17:31:57Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-rc-1

今後も、製品のコードベースを統一し、Android用のAdGuardは例外ではありません。 アップデートは、より安定化され、新機能が追加されます。 また、新しいバージョンでは、統計データやCoreLibsやDnsLibsの更新など、大量のデータの読み込みを加速しました。

>  このバージョンから、Android用のAdGuardは、Android 9以上をサポートしています。

## 変更履歴

### フィックス
* Beeline Wi-Fi 呼び出しは動作しません [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.17.82 に更新されました(#5610)(https://github.com/AdguardTeam/AdguardForAndroid/issues/5610)

### DnsLibs (DNSのろ過エンジン)
* dnsLibs が v2.5.63 に更新 [#5607](https://github.com/AdguardTeam/AdguardForAndroid/issues/5607)

#### 改善点
* デフォルト除外の一覧に問題. tcp.default.service.arpa を追加しました [#230](https://github.com/AdguardTeam/DnsLibs/issues/230 )
* ブロックRFC9462 ( dns.resolver.arpa) 問い合わせ [#228](https://github.com/AdguardTeam/DnsLibs/issues/228)
* 使用条件`pretty_str()`DnsRequestProcessedEvent [#223] で報告されたエラーでhttps://github.com/AdguardTeam/DnsLibs/issues/223)

#### フィックス
* DNS[#1887]でブロックするときの応答のための長い待ち時間(https://github.com/AdguardTeam/CoreLibs/issues/1887 )
* ルール`$dnsrewrite=IPv4`IPv6解像度をブロックしない [#224](https://github.com/AdguardTeam/DnsLibs/issues/224)
## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.8 ベータ 1

- 公表: 2025-02-07T17:27:43Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-beta-1

今後も、製品のコードベースを統一し、Android用のAdGuardは例外ではありません。 アップデートは、より安定化され、新機能が追加されます。 また、新しいバージョンでは、統計データと更新されたCoreLibsの大量のデータの読み込みを加速しました。

## 変更履歴

### フィックス

* Beeline Wi-Fi 呼び出しは動作しません [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)

### CoreLibs (フィルターエンジン)

* CoreLibs が v1.16.58 に更新されました [#5579](https://github.com/AdguardTeam/AdguardForAndroid/issues/5579)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7.1

- 公表: 2024-12-11T16:59:44Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7.1

このアップデートでは、アプリの安定性を改善し、いくつかのマイナーなバグを修正しました。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7

- 公表: 2024-12-03T15:41:02Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7

今日のバージョンはまさに私たちが大好きなものです。アプリで見るのを待つことができない新しい機能を紹介します。 小さなリリースはありません。アプリ内プライバシーブラウザをアプリに導入しています! 新しいものを詳しく見ていきましょう。

> AdGuard v4.7は、Android 7と8をサポートする最終バージョンです。 次のリリースから、Android 9 以降のみ対応いたします。

## あまりプライバシーがないため、プライベートブラウザ

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.7/agpb_en.png"幅="300">
</p>

多くのユーザーの日常生活において、プライバシーを念頭に置いています。 私たちは、アプリがそのルーチンの一部であることを望んでいます, そして、私たちはアドガードプライベートブラウザをロールアウトしている理由です, あなたの毎日のWeb体験に余分な層のプライバシーをもたらします.

それでは、このブラウザについてとてもクールなのでしょうか?

* 広告と追跡者ブロック(もちろん!)
* 目に見える、アクセス可能なボタンで簡単な履歴削除。 また、ブラウザを閉じるとブラウザの履歴が自動的に消去されます。

この新機能を探索するには、アプリのホーム画面で「*プライベートブラウザ*」をタップします。 *Protection*タブからブラウザにアクセスして、デフォルトの検索エンジンを設定したり、ブラウザウィジェットを作成したりすることもできます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.7/agmainpb_en.png"幅="300">
</p>

ヘッドアップ:当社のプライベートブラウザはまだ開発初期段階にあり、複数のセッションを一度に処理できないような制限がいくつかあります。 将来的には、より包括的なブラウジング体験を提供しますが、今では、交換ではなく、通常のブラウザのIncognito Modeの補足として使用することをお勧めします。 よく聞こえますか?

## 変更履歴

### 改善点
* FanboyのAnnoyanceリストの説明の誤った翻訳 [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### フィックス
* Android 9 [#4906] のシステム設定で対応するスイッチを有効にすると、ポップアップが消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* ほとんどすべてのアプリはフィルタリングされた [#5426] として記録されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* ダークテーマの検索バーにカーソルをひいて表示 [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* スイッチ「Trusted filter」の有効/無効化は、保護を再起動しない[#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* バグ画面のレポートに無効なメールでレポートを送信しようとすると、誤ったエラーメッセージ[#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* 保護がpausedならAdGuardの通知のマゼンタ色[#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* 問題のないアプリ [#4918] をオンにすると、グループ内の問題アプリのルーティングが有効になっています。https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* アウトゴットソケット画面のTCPは[#5415]をスクロールしません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* ユーザルールはエディタの中央にある[#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Annoyancesブロック通知の翻訳は欠落しています [#5388]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)
* Android WebViewがアンロードされたときにアプリがクラッシュ [#5521](https://github.com/AdguardTeam/AdguardForAndroid/issues/5521)

### その他
* `it.labfabrici.hub`保護が働いているとき、動作しません [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.5

- 公表: 2024-11-12T17:10:23Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.5

統計モジュールへのマイナーな改善。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7 RC 2

- 公表: 2024-11-30T08:51:08Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-rc-2

最終リリースに近づく1つのステップはRCの1つ。 今回は、フィルタリングルールのカウントと実装をすることで、プライベートブラウザの改善に注力しました。 また、アプリ全体のパフォーマンス向上にも取り組んできました。 お問い合わせ

## 変更履歴

### 改善点
* FanboyのAnnoyanceリストの説明の誤った翻訳 [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### フィックス
* Android 9 [#4906] のシステム設定で対応するスイッチを有効にすると、ポップアップが消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* AdGuard が Android WebView のアンロード時にクラッシュ [#5521](https://github.com/AdguardTeam/AdguardForAndroid/issues/5521)
* ほとんどすべてのアプリはフィルタリングされた [#5426] として記録されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* ダークテーマの検索バーにカーソルをひいて表示 [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* スイッチ「Trusted filter」の有効/無効化は、保護を再起動しない[#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* バグ画面のレポートに無効なメールでレポートを送信しようとすると、誤ったエラーメッセージ[#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* 保護がpausedならAdGuardの通知のマゼンタ色[#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* 問題のないアプリ [#4918] をオンにすると、グループ内の問題アプリのルーティングが有効になっています。https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* アウトゴットソケット画面のTCPは[#5415]をスクロールしません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* ユーザルールはエディタの中央にある[#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Annoyancesブロック通知の翻訳は欠落しています [#5388]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### その他
* `it.labfabrici.hub`保護が働いているとき、動作しません [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7 RC 1

- 公表: 2024-11-21T17:36:35Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-rc-1

リリースに近いので、シャンパンコルクのポップアップを実際に聞くことができます... 最後のベータ版以来、新機能は追加されていませんが、最終バージョンの準備が整っていないことを約束します。

## 変更履歴

### 改善点
* FanboyのAnnoyanceリストの説明の誤った翻訳 [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### フィックス
* Android 9 [#4906] のシステム設定で対応するスイッチを有効にすると、ポップアップが消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* ほとんどすべてのアプリはフィルタリングされた [#5426] として記録されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* ダークテーマの検索バーにカーソルをひいて表示 [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* スイッチ「Trusted filter」の有効/無効化は、保護を再起動しない[#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* バグ画面のレポートに無効なメールでレポートを送信しようとすると、誤ったエラーメッセージ[#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* 保護がpausedならAdGuardの通知のマゼンタ色[#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* 問題のないアプリ [#4918] をオンにすると、グループ内の問題アプリのルーティングが有効になっています。https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* アウトゴットソケット画面のTCPは[#5415]をスクロールしません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* ユーザルールはエディタの中央にある[#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Annoyancesブロック通知の翻訳は欠落しています [#5388]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### その他
* `it.labfabrici.hub`保護が働いているとき、動作しません [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### CoreLibs (フィルターエンジン)

#### CoreLibs が v1.16.53 に更新

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.7 ベータ 1

- 公表: 2024-11-15T15:23:10Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-beta-1

今日のベータ版はまさに私たちが大好きなものです。メインリリースでライブを見るのを待つことができない新しい機能を紹介します。 小さなベータがなくても、アプリにプライバシーブラウザを導入しています! それぞれ詳しく見ていきましょう。

> AdGuard v4.7は、Android 7と8のサポートを提供する最後のバージョンです。 次のリリースから、Android 9 以降のみ対応いたします。

## あまりプライバシーがないため、プライベートブラウザ

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/privatebrowser2.png"幅="300">
</p>

多くのユーザーの日常生活において、プライバシーを念頭に置いています。 AdGuardのプライベートブラウザをロールアウトし、毎日のWebエクスペリエンスにプライバシーの余剰レイヤーをもたらします。

それでは、このブラウザについてとてもクールなのでしょうか?

* 広告と追跡者ブロック(もちろん!)
* 目に見える、アクセス可能なボタンで簡単な履歴削除。 また、タブを閉じるとブラウザの履歴が自動的に消去されます。
* ブックマークを作成することで、閲覧セッションを保存するオプション — 通常の Incognito Mode は提供していません! すべてのタブを再開いたり、戻ってログインせずに退場する場所を選択したい場合は、この機能はあなたのためにあります。 そのためには、CookieやlocalStorageを保存します。

この新機能を探索するには、アプリのホーム画面で「*プライベートブラウザ*」をタップします。 *Protection*タブからブラウザにアクセスして、デフォルトの検索エンジンを設定したり、ブラウザウィジェットを作成したりすることもできます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/privatebrowser1.jpg"幅="300">
</p>

ヘッドアップ:当社のプライベートブラウザはまだ開発初期段階にあり、複数のセッションを一度に処理できないような制限がいくつかあります。 将来的には、より包括的なブラウジング体験を提供しますが、今では、交換ではなく、通常のブラウザのIncognito Modeの補足として使用することをお勧めします。 よく聞こえますか?

## 変更履歴

### 改善点
* FanboyのAnnoyanceリストの説明の誤った翻訳 [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### フィックス
* Android 9 [#4906] のシステム設定で対応するスイッチを有効にすると、ポップアップが消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* ほとんどすべてのアプリはフィルタリングされた [#5426] として記録されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* ダークテーマの検索バーにカーソルをひいて表示 [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* スイッチ「Trusted filter」の有効/無効化は、保護を再起動しない[#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* バグ画面のレポートに無効なメールでレポートを送信しようとすると、誤ったエラーメッセージ[#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* 保護がpausedならAdGuardの通知のマゼンタ色[#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* 問題のないアプリ [#4918] をオンにすると、グループ内の問題アプリのルーティングが有効になっています。https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* アウトゴットソケット画面のTCPは[#5415]をスクロールしません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* ユーザルールはエディタの中央にある[#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Annoyancesブロック通知の翻訳は欠落しています [#5388]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### その他
* `it.labfabrici.hub`保護が働いているとき、動作しません [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### CoreLibs (フィルターエンジン)

#### CoreLibs が v1.16.51 に更新

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.4 ホットフィックス

- 公表: 2024-11-05T11:13:36Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4-hotfix

このHotfix アップデートは、Java.util の使用によるバッテリーのドレインの問題が解決します。 特定のタイムゾーンのカレンダー。

## 4.6.4

- 公開日: 2024-10-31T15:57:15Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4

このリリースが UFC の戦闘機だったら、スクワッシュバグのすべてだから「バグフィクサー」という名前で行きます。 ここの達成したものを破壊してみましょう。

## DNS のバグ

DNS を引き起こした特に目を引くバグを解決しました。その結果、インターネットはネットワークの切り替え時にランダムに失敗します。 問題が予測不可能で、少数のユーザー数にしか影響を与えたため、私たちの部分にいくつかの探偵作品を取りました。 しかし、ねえ、DNS保護なしでは誰も残るべきではありません!

## バッテリードレインバグ

ベータテスト中に発見した別の刺激的なバグ:誤った統計計算は、過度のバッテリードレインにつながりました。 システムコードは、特定の値の下の正確な統計に必要な日付を計算できませんでした。 ありがたいことに、このオッズ動作をシステムコードで実行し、現在、統計は正しく計算されます。 彼らはまた、より高速にロードし、より少ないRAMを取ります.

この問題は、特定のバージョンのAndroidでユーザーに影響を与えるようです。 AdGuardのナイトバージョンやベータ版を使って、この問題に遭遇した場合は、安定的なリリースへのアップデートをお勧めします。

## その他の修正

バグ修正と改善の数は、CoreLibsの最新バージョンと改善されたフィルタリング品質で提供されます。変更ログの詳細は以下をご覧ください。

## 変更履歴

### フィックス
* AdGuard は、統計サイズ [#5458] によるログと設定をエクスポートできません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/5458)
* 最近の活動ログが分割画面で開くとAdGuardがクラッシュ [#5481](https://github.com/AdguardTeam/AdguardForAndroid/issues/5481)
* AdGuard は v4.6 [#5460] 以降、あまりにも多くのバッテリーを消費します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5460)

### CoreLibs (フィルターエンジン)
* CoreLibs が v1.16.44 に更新

#### 改善点
* フィルタリングされたアプリで使用されているとき、後量暗号化を有効にします [#1916](https://github.com/AdguardTeam/CoreLibs/issues/1916)
* サポート`strict-first-party`そして、`strict-third-party`uBOの修飾子 [#1874](https://github.com/AdguardTeam/CoreLibs/issues/1874)
* スクリプトレットを許可する可能性を追加 [#1862](https://github.com/AdguardTeam/CoreLibs/issues/1862)
* 追跡サービスなしで目的地へのリダイレクトをサポート ミドルマン [#1557](https://github.com/AdguardTeam/CoreLibs/issues/1557)


#### フィックス
* AdGuard コンテンツスクリプトは CSP によってブロックされます。`uber.com` [#1903](https://github.com/AdguardTeam/CoreLibs/issues/1903)
* ログインはFirefoxで壊れています`sony.de` [#1867](https://github.com/AdguardTeam/CoreLibs/issues/1867)
* GM xmlhttpRequest は、Referer ヘッダーをサポートしていません [#1899](https://github.com/AdguardTeam/CoreLibs/issues/1899)
*AdGuardは、ブラウザによって行われたユーザーエージェントの変更をオーバーライドし、プライバシーを低減します[#1910](https://github.com/AdguardTeam/CoreLibs/issues/1910)

### スクリプト(フィルタリングルールのJavaScript強化)
* Scriptlets が v1.11.27 に更新

#### 改善点
* `set-local-storage-item`— 追加した値`allowed`そして、`denied` [#445](https://github.com/AdguardTeam/Scriptlets/issues/445)
* `abort-on-stack-trace`— サポート行番号`inlineScript`そして、`injectedScript` [#439](https://github.com/AdguardTeam/Scriptlets/issues/439)
* `set cookie`— 追加した値`checked`そして、`unchecked` [#444](https://github.com/AdguardTeam/Scriptlets/issues/444)
* `trusted-click-element`— 追加`reload`オプション [#301](https://github.com/AdguardTeam/Scriptlets/issues/301)
* 新しいスクリプトレットを追加`trusted-set-session-storage-item` [#426](https://github.com/AdguardTeam/Scriptlets/issues/426)
* `set-cookie`— 追加`essential`そして、`nonessential`対応する値へ [#436](https://github.com/AdguardTeam/Scriptlets/issues/436)
* `trusted-set-cookie`そして、`trusted-set-cookie-reload`— 追加`$currentISODate$` [#435](https://github.com/AdguardTeam/Scriptlets/issues/435)
* `set-cookie`— 対応する値を追加 [#433](https://github.com/AdguardTeam/Scriptlets/issues/433)
* `set-local-storage-item`— 対応する値を追加 [#429](https://github.com/AdguardTeam/Scriptlets/issues/429)
* スクリプトでログアウトする [#411](https://github.com/AdguardTeam/Scriptlets/issues/411)
* フィルタリングログ[#180]で化粧品のルールを表示する(https://github.com/AdguardTeam/CoreLibs/issues/180)
* 新しいスクリプトレットを追加`trusted-dispatch-event` [#382](https://github.com/AdguardTeam/Scriptlets/issues/382)
* 新しいスクリプトレットを追加`trusted-replace-outbound-text` [#410](https://github.com/AdguardTeam/Scriptlets/issues/410)
* 完全なルールテキストなしでAdGuardの互換性のためのリダイレクトを検証する機能を追加 [#420](https://github.com/AdguardTeam/Scriptlets/issues/420)
* `trusted-click-element`— クローズドShadowRootのサポートを追加しました [#423](https://github.com/AdguardTeam/Scriptlets/issues/423)
* `trusted-click-element`— 与えられたテキストを含む要素をクリックする機能を追加しました [#409](https://github.com/AdguardTeam/Scriptlets/issues/409)

#### フィックス
* `log-on-stack-trace`— プレイヤーが壊れている`deltabit.co` [#384](https://github.com/AdguardTeam/Scriptlets/issues/384)
* `trusted-create-element`— 使用するとき`cleanupDelayMs`パラメータ、削除された要素は再追加され、数回[#434]を削除されます(https://github.com/AdguardTeam/Scriptlets/issues/434)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.4 ベータ 1

- 公開日: 2024-10-04T08:08:05Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4-beta-1

このリリースは、優れたバイブと改善されたフィルタリング品質に関するすべてです。CoreLibsの新しいバージョンはそれだけではありません。 また、統計処理の方法を最適化しました。そのため、アプリが実行している間、より高速に読み込み、RAMを削減します。 少数のバグも修正されました。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.3

- 公表: 2024-09-09T16:58:37Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.3

前回以降の技術アップデートです。 そこで、バグを修正し、アプリの安定性に取り組んできました。

&nbsp;
### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

### Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.2

- 公開日: 2024-08-21T15:01:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.2

新しく更新されたバージョンを持っている場合でも、アプリがクラッシュする方法に気づくことはありませんか? お問い合わせ このホットフィックスは、その問題を解決します。 今から、すべての方法を妨げる純粋な広告。

&nbsp;
### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

### Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6.1 

- 公表: 2024-07-26T10:36:02Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.1

フィルタリングエンジンは[敵のバグ]でヒットしました(https://github.com/AdguardTeam/AdguardForAndroid/issues/5405), しかし、AdGuardはそれよりも強いです. このホットフィックスにより、更新されたライブラリはクリーナーとより安全なWebを提供します。

&nbsp;
### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

### Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6

- 公表: 2024-07-24T16:16:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6

Vince Lombardi氏は次のように述べています。「Perfectionは達成できませんが、完璧を追いかけると卓越性をキャッチすることができます。」 私たちは彼が言うように、すべての更新をより良くするために最善を尽くします。 今日、私たちは、Android用のAdGuardの新しいバージョンをリリースするために満足しています。 より速く、より強く、より有効。 メジャーな変化を見てみましょう。

更新されたフィルタリングエンジンCoreLibsでは、フィルタリングエクスペリエンスを向上させる多くの新機能を実装できるようになりました。 まず、HTTPSフィルタリング速度を上げました。 第二に、当社のフィルター開発者と上級ユーザーのためのいくつかの便利な強化があります。 サポートを追加いたしました。`urltransform`](https://adguard.com/kb/general/ad-filtering/create-own-filters/#urltransform-modifier) と [`xmlprune`](https://adguard.com/kb/general/ad-filtering/create-own-filters/#xmlprune-modifier)修飾子。 ページの要素をさらに引き起こすとブロックされます。

よりユーザーフレンドリーにするために、UIの改善を行いました。 バッテリー使用量を最適化しようとすると、Xiaomiユーザーは困難に直面しています。 それについて考え、ガイドを追加することにしました。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.6/Xiaomi_guide_en.png"幅="300">
</p>

 
開発者は、そのラウレルに残りませんでしたので、DnsLibsとUserscriptsWrapperを更新し、アプリをより安定させるために多くのバグを修正しました。

## 変更履歴

### フィックス
* AdGuard YouTubeプレーヤーは、YouTubeリンクを開くか、プレイリストを再生することはできません [#5348](https://github.com/AdguardTeam/AdguardForAndroid/issues/5348)
* AdGuardを終了した後、保護通知をタップするとアプリがクラッシュ [#5366](https://github.com/AdguardTeam/AdguardForAndroid/issues/5366)
* 翻訳はフィールドに合わない [#5324](https://github.com/AdguardTeam/AdguardForAndroid/issues/5324)
* 警告テキスト “AdGuard を介してルーティングされていない” デフォルト [#5340] の設定をリセットした後、消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5340)

### CoreLibs (フィルタリングエンジン)
* 【コアリブ】(https://github.com/AdguardTeam/AdguardForAndroid/issues/5400)v1.15.59に更新

#### 改善点
* 追加`$urltransform`(信頼)修飾子サポート [#1364]()https://github.com/AdguardTeam/CoreLibs/issues/1364)
* 追加`$xmlprune`修飾子サポート [#473](https://github.com/AdguardTeam/CoreLibs/issues/473)
* サポートするユーザーエージェントのリストにモバイルブラウザを追加`:has()`ネイティブ [#1870](https://github.com/AdguardTeam/CoreLibs/issues/1870)
* ローカル側の ECDSA 暗号を許可 [#360](https://github.com/AdguardTeam/CoreLibs/issues/360)
* セットアップ`Sec-Fetch-Dest header: fencedframe` [#1853](https://github.com/AdguardTeam/CoreLibs/issues/1853)
* サポートuBO's`/regex/`化粧品の規則のフォーマット [#1844] (https://github.com/AdguardTeam/CoreLibs/issues/1844)

#### フィックス
* FQDN のアドブロックの構文ルールは [#210] は動作しません(https://github.com/AdguardTeam/DnsLibs/issues/210)
* AdGuardとFTP接続エラー[#1864](https://github.com/AdguardTeam/CoreLibs/issues/1864)
* ユーザスクリプト XHR エラー [#1876](https://github.com/AdguardTeam/CoreLibs/issues/1876)
* `$all`modifier は非ドメイン URL 部分で動作しません [#1860](https://github.com/AdguardTeam/CoreLibs/issues/1860)
* URLブロックルールは正しく機能しない`$generichide`修飾子 [#1857] (https://github.com/AdguardTeam/CoreLibs/issues/1857)

### DnsLibs (DNSのろ過エンジン)
* [DnsLibs](DnsLibs)https://github.com/AdguardTeam/AdguardForAndroid/issues/5357)v2.5.33に更新される

### ユーザースクリプトWrapper
* UserscriptsWrapperがv1.2.24に更新

#### フィックス
* `vk-metabot.user.js`AdGuard経由で動作しない [#1871](https://github.com/AdguardTeam/CoreLibs/issues/1871)

### コンテンツスクリプト
* コンテンツスクリプトがv2.0.6に更新

#### フィックス
* 要素の隠れる規則`##`そして、`#$#`申請しない`tv.rambler.ru` [#1865](https://github.com/AdguardTeam/CoreLibs/issues/1865)


&nbsp;
### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

### Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6 RC 1

- 公表: 2024-07-19T13:03:42Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6-rc-1

リリース前の最終調整だけ。 このバージョンでは、大きな問題が解決しました。 モバイルとWi-Fi接続を切り替えると、一部のユーザーは問題が発生していました。 AdGuard保護が停止するので、手動で起動する必要があります。 また、より安定したアプリケーションを作るために他のバグを修正しました。 よりアップデートをお待ちください。正式リリースはすぐ角にあります!

## 変更履歴

### CoreLibs (フィルタリングエンジン)
* 【コアリブ】(https://github.com/AdguardTeam/AdguardForAndroid/issues/5400)v1.15.59に更新


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.6 ベータ 1

- 公表: 2024-07-11T14:44:07Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/4.6-beta-1

Vince Lombardi氏は次のように述べています。「Perfectionは達成できませんが、完璧を追いかけると卓越性をキャッチすることができます。」 私たちは彼が言うように、すべての更新をより良くするために最善を尽くします。 今日は、Android用のAdGuardの新しいベータ版をリリースするのを嬉しく思います。 より速く、より強く、より有効。 メジャーな変化を見てみましょう。

更新されたフィルタリングエンジンCoreLibsでは、フィルタリングエクスペリエンスを向上させる多くの新機能を実装できるようになりました。 まず、HTTPSフィルタリング速度が向上しました。 第二に、サポートを追加`urltransform`そして、`xmlprune`修飾子。 ページの要素をさらに引き起こすとブロックされます。

開発者は、そのlaurelsに残りませんでしたので、DnsLibs、UserscriptsWrapperを更新し、アプリケーションをより安定させるために多くのバグを修正しました。

## 変更履歴

### フィックス
* AdGuard YouTubeプレーヤーは、YouTubeリンクを開くか、プレイリストを再生することはできません [#5348](https://github.com/AdguardTeam/AdguardForAndroid/issues/5348)
* AdGuardを終了した後、保護通知をタップするとアプリがクラッシュ [#5366](https://github.com/AdguardTeam/AdguardForAndroid/issues/5366)
* 翻訳はフィールドに合わない [#5324](https://github.com/AdguardTeam/AdguardForAndroid/issues/5324)
* 警告テキスト “AdGuard を介してルーティングされていない” デフォルト [#5340] の設定をリセットした後、消えません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5340)

### CoreLibs (フィルタリングエンジン)
* 【コアリブ】(https://github.com/AdguardTeam/AdguardForAndroid/issues/5381)v1.15.54に更新

#### 改善点
* 追加`$urltransform`(信頼)修飾子サポート [#1364]()https://github.com/AdguardTeam/CoreLibs/issues/1364)
* 追加`$xmlprune modifier`サポート [#473](https://github.com/AdguardTeam/CoreLibs/issues/473)
* サポートするユーザーエージェントのリストにモバイルブラウザを追加`:has()`ネイティブ [#1870](https://github.com/AdguardTeam/CoreLibs/issues/1870)
* ローカル側の ECDSA 暗号を許可 [#360](https://github.com/AdguardTeam/CoreLibs/issues/360)
* セットアップ`Sec-Fetch-Dest header: fencedframe` [#1853](https://github.com/AdguardTeam/CoreLibs/issues/1853)
* サポートuBO's`/regex/`化粧品の規則のフォーマット [#1844] (https://github.com/AdguardTeam/CoreLibs/issues/1844)

#### フィックス
* FQDN のアドブロックの構文ルールは [#210] は動作しません(https://github.com/AdguardTeam/DnsLibs/issues/210)
* AdGuardとFTP接続エラー[#1864](https://github.com/AdguardTeam/CoreLibs/issues/1864)
* ユーザスクリプト XHR エラー [#1876](https://github.com/AdguardTeam/CoreLibs/issues/1876)
* `$all`modifier は非ドメイン URL 部分で動作しません [#1860](https://github.com/AdguardTeam/CoreLibs/issues/1860)
* URLブロックルールは正しく機能しない`$generichide`修飾子 [#1857] (https://github.com/AdguardTeam/CoreLibs/issues/1857)

### DnsLibs (DNSのろ過エンジン)
* [DnsLibs](DnsLibs)https://github.com/AdguardTeam/AdguardForAndroid/issues/5357)v2.5.33に更新される

### ユーザースクリプトWrapper
* UserscriptsWrapperがv1.2.24に更新

#### フィックス
* `vk-metabot.user.js`AdGuard経由で動作しない [#1871](https://github.com/AdguardTeam/CoreLibs/issues/1871)

### コンテンツスクリプト
* コンテンツスクリプトがv2.0.6に更新

#### フィックス
* 要素の隠れる規則`##`そして、`#$#`申請しない`tv.rambler.ru` [#1865](https://github.com/AdguardTeam/CoreLibs/issues/1865)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.5

- 公表: 2024-06-11T12:09:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.5

このアップデートは、YouTubeプレーヤーのユーザビリティを新しいレベル全体に引き上げます。背景再生、推奨動画、品質設定などを追加しました。 今のところ、あなたは、広告ですか? その上、このバージョンには、Android TVバージョンを含む全体的なアプリのパフォーマンスのためのいくつかの素晴らしい修正が含まれています。

## AdGuardのYouTubeプレーヤーの改善のトン

今利用可能なものを見てみましょう:

* ギアを使用してビデオ品質、再生速度、およびサブタイトル設定を変更 ◀ ボタン

![AGプレーヤー動画設定](https://cdn.adtidy.org/blog/new/jdwr7AG-player-video-settings.png)

* ピクチャーインピクチャーモードがサポートされています。つまり、ビデオを小さなウィンドウに縮小し、他のアプリを使用してバックグラウンドで再生し続けることができます。 音楽やポッドキャストを聴くなど、素晴らしいこと

<p align="center">
<img src="">https://cdn.adtidy.org/blog/new/x31y3AG-player-picture-in-picture.png" 
幅="300" 高さ="600">

* ビデオの最後に推奨事項を表示し、パユース中、またはプレーヤーの右下隅をタップすることにより(ビデオに依存する)

![AGプレーヤー推奨動画](https://cdn.adtidy.org/blog/new/g64dbAG-player-recommended.png)

* 画面の右側または左サイドをダブルタップすると、10秒前後をスキップできます。

> クイックリマインダー:AdGuardプレーヤーを起動するには、YouTubeアプリで任意のビデオを選択し、*共有*をタップし、AdGuard Playerを選択します(右スクロールして、*詳細*を最初にタップする必要があります)。
>
> 注意: AdGuard プレーヤーは、YouTube を開く内部の Web ブラウザーに基づいており、内蔵されているアドブロック機能を備えています。 そのため、その機能の機能と可用性は、YouTubeのWebバージョンによって異なります。

## 変更履歴

### 改善点
* フォーカスは、Android TV用のAdGuardの左側のメニューを開き、それを閉じた後、同じ場所にとどまります [#5271](https://github.com/AdguardTeam/AdguardForAndroid/issues/5271)

### フィックス
* DNS 保護設定は、デフォルト [#5322] にリセットされません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5322)
* 「メイン画面でDevToolsを表示する」トグルは、同じ画面で他のトグルと相互作用した後、点滅を開始します[#5332](https://github.com/AdguardTeam/AdguardForAndroid/issues/5332)
* 言語固有のフィルタ「その他」 [#5232]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5232)
* 低レベルの設定で「メイン画面でDevToolsを表示する」オプションをデフォルトにリセットできなかった[#5331](https://github.com/AdguardTeam/AdguardForAndroid/issues/5331)
* 「adguard:add dns server?address="プレフィックス [#5264]」() と連携して、カスタム DNS サーバーを追加しようとすると、Android TV のアドガードがクラッシュします。https://github.com/AdguardTeam/AdguardForAndroid/issues/5264)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.4.1

- 公表: 2024-05-23T14:08:43Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4.1

アプリの安定性を高め、マイナーなバグを修正する技術アップデートです。


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.4

- 公表: 2024-05-20T12:58:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4

ファイアウォール機能とオンザフライDohフィルタリングは、Android用のAdGuard v4.4のハイライトです。 豊富なテストの後、新しいバージョンをあなたに紹介する準備ができています。

## 防火壁

私たちは、インターネットクリーナーを作り、ユーザーにとってより楽しくなると思います。 しかし、我々は時々、私たちは自分自身に迷惑な通知を送ることができることを認めるために恥ずかしいではありません。 ユーザーは、ファイアウォールの不便で見つけたことを報告しています:通知が多すぎるだけです。 その結果、システム環境設定で優れている人々をオフにします。

対応にあたっては、ファイアウォール機能を改善しました。 これで、すべてのアプリケーションや特定のアプリケーションにファイアウォール通知をカスタマイズしてオフにすることができます。
Chrome 接続に関する通知を受け取りたくないですか? 通知シェードを開き、Chromeに関する通知をタップし、*Mute*をタップします。 このアプリのすべてのファイアウォール通知は無効になります。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/mute.png" 
幅="300" 高さ="600">

あるいは、*Protection* → *Firewall* → *Notifications* にアクセスして、個々のアプリの通知を切り替えることができます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/settings.png" 
幅="300" 高さ="600">

## DoH リクエストは飛ぶ

更新されたフィルタリングエンジンでは、CoreLibs では、on-the-fly DNS-over-HTTPS (DoH) 接続フィルタリングを実行できます。 デスクトップアプリhttps://adguard.com/en/blog/adguard-v2-14-for-mac.html) 既にこのルートをなくなってきて、うまくいくようです。 なぜこの機能は必要ですか?
 
以前は、ユーザーがブラウザでDohを有効にしたが、AdGuardでない場合は、ブラウザに直接リクエストをフィルタリングし、暗号化されていないシステムDNSに送信し、セキュリティが低下しました。 現在、ON-the-fly DoH接続フィルタリングで、暗号化されていないサーバーに送信することなく、ブラウザでDNSリクエストをフィルタリングできます。

> *Settings* → *General* → *Advanced* → *Low-level設定* → *Filter は DNS* をしっかり確保します。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/dns_en.png" 
幅="300" 高さ="600">

また、いくつかのマイナーなバグを修正し、UserscriptsWrapperとDnsLibsを更新しました。

## 変更履歴

### 改善点
* ChromiteブラウザでHTTPSフィルタリングを有効にして、無料で[#4997](https://github.com/AdguardTeam/AdguardForAndroid/issues/4997)
* 開発者ツールのセクションの改善 [#5173](https://github.com/AdguardTeam/AdguardForAndroid/issues/5173)
* 空のユーザールールリストでルールをエクスポートしようとすると、「エクスポートする」スナックを追加する[#5176](https://github.com/AdguardTeam/AdguardForAndroid/issues/5176)
* com.klookアプリをデフォルトHTTPSフィルタリング除外に追加 [#5143](https://github.com/AdguardTeam/AdguardForAndroid/issues/5143)
* com.nekki.shadowfightarena を QUIC のバイパス パッケージにデフォルトで含める [#5158](https://github.com/AdguardTeam/AdguardForAndroid/issues/5158)

### フィックス
* ライセンスキーが隠されていない [#4496](https://github.com/AdguardTeam/AdguardForAndroid/issues/4496)
* 翻訳の修正`it`ロケール [#5180](https://github.com/AdguardTeam/AdguardForAndroid/issues/5180)
* AutorunはChromecastとSony TVを再起動した後に動作しません [#5156](https://github.com/AdguardTeam/AdguardForAndroid/issues/5156)
* 大きい電池の消費[#4960] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4960)
* キャッシュサイズが急速に成長 [#5125](https://github.com/AdguardTeam/AdguardForAndroid/issues/5125)
* Userscript の状態の変更を行い、戻ったときにアプリがクラッシュする [#5131](https://github.com/AdguardTeam/AdguardForAndroid/issues/5131)
* インドネシア語を選択するとアプリがクラッシュ [#5236](https://github.com/AdguardTeam/AdguardForAndroid/issues/5236)
* DNS サーバーの設定は、DNS フィルタ タブ [#5142] の設定をリセットした後にリセットされます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5142)
* 証明書のインストールの失敗に関するダイアログは、成功したインストール後に消えません [#5194](https://github.com/AdguardTeam/AdguardForAndroid/issues/5194)
* アプリケーション更新をダウンロードすると、バッテリー容量の400 mAh以上かかります[#5259](https://github.com/AdguardTeam/AdguardForAndroid/issues/5259)
* ケースの差[#5037]を使ってウェブサイトの許可者に重複を追加できます(https://github.com/AdguardTeam/AdguardForAndroid/issues/5037)
* 設定をエクスポートする際にエラー [#5069](https://github.com/AdguardTeam/AdguardForAndroid/issues/5069)
* 背景画像は、com.opera.browser [#5096] でブロックされます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5096)
* デバイスペアリングエラー(com.meross.meross) [#4989](https://github.com/AdguardTeam/AdguardForAndroid/issues/4989)
* 2つのコンポーネントを持つ選択した会社の最近の活動が表示されない[#5067](https://github.com/AdguardTeam/AdguardForAndroid/issues/5067)
* すべての DNS エントリの [#4824] (.) 文字を削除します。https://github.com/AdguardTeam/AdguardForAndroid/issues/4824)
* ブラウジングセキュリティ画面のスクロール領域の問題[#5195](https://github.com/AdguardTeam/AdguardForAndroid/issues/5195)
* スクロールバーの親指は、最近の活動の下部メニューの後ろに行きます [#4901](https://github.com/AdguardTeam/AdguardForAndroid/issues/4901)
* 申し込みを最小限にすることでスナックを閉じる [#5018](https://github.com/AdguardTeam/AdguardForAndroid/issues/5018)
* いくつかのカスタムフィルタプロパティが正しく更新しない[#5171](https://github.com/AdguardTeam/AdguardForAndroid/issues/5171)
* メイン画面のスタディティスティックカードはフルスクリーンの幅を埋めません [#5118](https://github.com/AdguardTeam/AdguardForAndroid/issues/5118)
* ポップアップはシステム言語で表示され、アプリケーション全体が英語[#5168]にある間(https://github.com/AdguardTeam/AdguardForAndroid/issues/5168)
* 無線ボタンの状態はBootstrapの上流の選択[#5239]のために輸入されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5239)
* 更新ローダーが正しく機能しない[#5028](https://github.com/AdguardTeam/AdguardForAndroid/issues/5028)
* 通知シェードを介して無効にすると、アプリの再オープン時に自動的に有効になります [#5146](https://github.com/AdguardTeam/AdguardForAndroid/issues/5146)
* AdGuard保護機能により、インターネット接続がない場合のアプリレポート[#5209](https://github.com/AdguardTeam/AdguardForAndroid/issues/5209)
* Santander と Sainsburys Bank アプリは HTTPS で [#5058] でフィルタリングします。https://github.com/AdguardTeam/AdguardForAndroid/issues/5058)
* 更新履歴バーに誤った色 [#5308] (https://github.com/AdguardTeam/AdguardForAndroid/issues/5308)

### CoreLibs (フィルターエンジン) を v1.14.59 に更新しました (#5316)()https://github.com/AdguardTeam/AdguardForAndroid/issues/5316)

#### 改善点
* DoH接続のon-the-flyフィルタリングを追加 [#198]()https://github.com/AdguardTeam/DnsLibs/issues/198)
* 追加`GM.xmlhttpRequest`エイリアスとして`GM_xmlhttpRequest` [#1785](https://github.com/AdguardTeam/CoreLibs/issues/1785)
* アウトバウンドプロキシは、リクエスト処理イベント(#1385)で使用されます。https://github.com/AdguardTeam/CoreLibs/issues/1385)
* アウトバウンドプロキシにホストを渡すためのサポートを追加 [#1386](https://github.com/AdguardTeam/CoreLibs/issues/1386)
* Firefox 121.0+ をユーザエージェントのリストに追加しました。`:has()` [#1840](https://github.com/AdguardTeam/CoreLibs/issues/1840)
* インターセプトされた DNS HTTPS クエリから ECH パラメータを追加 [#1794]()https://github.com/AdguardTeam/CoreLibs/issues/1794)
* 改善されたHTMLのろ過性能[#1855] (https://github.com/AdguardTeam/CoreLibs/issues/1855)
* 使用するオプションを追加`|`分離器として`$permissions` [#1850](https://github.com/AdguardTeam/CoreLibs/issues/1850)

#### フィックス
* お問い合わせ`$permissions`お問い合わせ`document` [#1856](https://github.com/AdguardTeam/CoreLibs/issues/1856)
* QUIC ClientHello を 2 つのパケットに分割できません。 [#1861](https://github.com/AdguardTeam/CoreLibs/issues/1861)
* VOTスクリプトはGoogle chromeで動作しません [#1665](https://github.com/AdguardTeam/CoreLibs/issues/1665)
* 正規化ヘッダでリクエストをリダイレクトしない[#1851](https://github.com/AdguardTeam/CoreLibs/issues/1851)
* 韓国の電気通信のためのサポート反DPIの特徴[#1789] (https://github.com/AdguardTeam/CoreLibs/issues/1789)
* クッキーに関するルール`[`そして、`]`お名前が無効です [#1843](https://github.com/AdguardTeam/CoreLibs/issues/1843)
* AdGuardがAdGuard VPNブラウザの拡張機能と一緒に動作する場合、化粧品のルールは適用されません[#1791](https://github.com/AdguardTeam/CoreLibs/issues/1791)
* サブドメインの1つは、異なるサイトの証明書[#1839]のためにフィルタリングされていません(https://github.com/AdguardTeam/CoreLibs/issues/1839)
* `$all`修飾子が正しく機能しない[#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)
* `mall.sk`コンテンツスクリプトは注入されません [#1834](https://github.com/AdguardTeam/CoreLibs/issues/1834)
* キャラクタークラスでエスラッシュをエスケープした正規表現のブロックは動作しません[#1831](https://github.com/AdguardTeam/CoreLibs/issues/1831)
* doctype宣言前のタグ(埋め込み属性)がある場合、コンテンツスクリプトは注入されません[#1825](https://github.com/AdguardTeam/CoreLibs/issues/1825)
* `$path`修飾子はクエリパラメータで動作しません [#1817](https://github.com/AdguardTeam/CoreLibs/issues/1817)
* `$removeparam`ポート付き url でポートなしで url にリダイレクト [#1818](https://github.com/AdguardTeam/CoreLibs/issues/1818)
* `android-hilfe.de`ブレーキサイト [#1800](https://github.com/AdguardTeam/CoreLibs/issues/1800)
* wiki.cemu.infoを安全に接続できません。 [#1821](https://github.com/AdguardTeam/CoreLibs/issues/1821)
* AdGuardはシステム的にクラッシュし、フリーズ [#1880] (https://github.com/AdguardTeam/CoreLibs/issues/1880)

### スクリプト(フィルタリングルールのJavaScriptの強化)をv1.10.25に更新

#### 改善点
* グーグルアナリティクスの改善、追加`ga.q`プロパティ [#355](https://github.com/AdguardTeam/Scriptlets/issues/355)
* google-ima3の改善、追加`OmidVerificationVendor`プロパティ [#353](https://github.com/AdguardTeam/Scriptlets/issues/353)
* uBO の set-cookie スクリプトレット [#332] との互換性を追加しました。https://github.com/AdguardTeam/Scriptlets/issues/332)
* 新しいスクリプトレットを追加`href-sanitizer` [#327](https://github.com/AdguardTeam/Scriptlets/issues/327)
* 新しいスクリプトレットを追加`json-prune-fetch-response` [#361](https://github.com/AdguardTeam/Scriptlets/issues/361)
* 新しいスクリプトレットを追加`json-prune-xhr-response` [#360](https://github.com/AdguardTeam/Scriptlets/issues/360)
* 新しいスクリプトレットを追加`trusted-suppress-native-method` [#383](https://github.com/AdguardTeam/Scriptlets/issues/383)
* 新しいスクリプトレットを追加`no-protected-audience` [#395](https://github.com/AdguardTeam/Scriptlets/issues/395)
* 改善しました`set-cookie`, 可能な数値を増加 [#388](https://github.com/AdguardTeam/Scriptlets/issues/388)
* 改善しました`trusted-click-element`, shadowRootでセレクターを見つけるためのサポートを追加しました [#323](https://github.com/AdguardTeam/Scriptlets/issues/323)
* リソースをスクリプトとしてリダイレクトするだけでなく、 [#300](https://github.com/AdguardTeam/Scriptlets/issues/300)
* スクリプトレットを許可する可能性を追加 [#377](https://github.com/AdguardTeam/Scriptlets/issues/377)
* 改善しました`prevent-fetch`, 追加`cors`responseType [#394]()https://github.com/AdguardTeam/Scriptlets/issues/394)
* 改善しました`set-cookie`, 追加`domain`パラメーター [#389](https://github.com/AdguardTeam/Scriptlets/issues/389)
* 新しいスクリプトレットを追加`call-nothrow.js` [#333](https://github.com/AdguardTeam/Scriptlets/issues/333)
* 新しいスクリプトレットを追加`spoof-css` [#317](https://github.com/AdguardTeam/Scriptlets/issues/317)
* 新しいスクリプトレットを追加`trusted-create-element` [#278](https://github.com/AdguardTeam/Scriptlets/issues/278)
* 改善しました`set-cookie`, よりサポートされている値を追加 [#379](https://github.com/AdguardTeam/Scriptlets/issues/379)
* 新しいスクリプトレットを追加`trusted-set-attr` [#281](https://github.com/AdguardTeam/Scriptlets/issues/281)

#### フィックス
* 固定式`set-constant`— setProxyTrap() [#403]()https://github.com/AdguardTeam/Scriptlets/issues/403)
* 固定式`set-cookie`, クッキー名をエンコードしません [#408](https://github.com/AdguardTeam/Scriptlets/issues/408)
* 固定式`set-local-storage-item`変換,`$remove$`パラメータ [#404](https://github.com/AdguardTeam/Scriptlets/issues/404)

### UserscriptsWrapperがv1.2.23に更新

### DnsLibs (DNS フィルタリングエンジン) v2.5.25 に更新 [#5306](https://github.com/AdguardTeam/AdguardForAndroid/issues/5306)

#### 改善点
* tcp-only と udp-only DNS 上流を指定できるようになりました [#208](https://github.com/AdguardTeam/DnsLibs/issues/208)
* ブートストラップの代わりに、ホスト名をアウトバウンドプロキシに渡すサポート [#197](https://github.com/AdguardTeam/DnsLibs/issues/197)
* HTTPS RRType [#215] の処理を改善しました(https://github.com/AdguardTeam/DnsLibs/issues/215)
* ホスト正規化を DoH にのみ制限する [#219](https://github.com/AdguardTeam/DnsLibs/issues/219)

#### フィックス
* v4.3 [#216] に更新した後に HTTP/1.1 を使用する DoH DNS サーバーを使用できません。https://github.com/AdguardTeam/DnsLibs/issues/216)
* DoHのIPv4/IPv6のための幸せな眼球を使用して下さい[#217] (https://github.com/AdguardTeam/DnsLibs/issues/217)
* FQDN のアドブロック構文ルールは [#210] は動作しません。https://github.com/AdguardTeam/DnsLibs/issues/210)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.5 ベータ 1

- 公開日: 2024-05-30T15:22:00Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.5-beta-1

このアップデートは、YouTubeプレーヤーのユーザビリティを新しいレベル全体に引き上げます。 このアップデートは、YouTubeプレーヤーのユーザビリティを新しいレベル全体に引き上げます。背景再生、推奨動画、品質設定などを追加しました。 今のところ、あなたは、広告ですか? その上、このバージョンには、Android TVバージョンを含む全体的なアプリのパフォーマンスのためのいくつかの素晴らしい修正が含まれています。

## AdGuardのYouTubeプレーヤーの改善のトン

今利用可能なものを見てみましょう:

ギアを使用してビデオ品質、再生速度、およびサブタイトル設定を変更 ◀ ボタン
ピクチャー・イン・ピクチャー・モードがサポートされています。つまり、ビデオを小さなウィンドウに縮小し、他のアプリを使用してバックグラウンドで再生し続けることができます。 音楽やポッドキャストを聴くなど、素晴らしいこと
ビデオの最後に、またはビデオのポーズで推奨ビデオを見る
画面の右側または左サイドをダブルタップすると、10秒前後をスキップできます。

> クイックリマインダー:AdGuardプレーヤーを起動するには、YouTubeアプリで任意のビデオを選択し、「共有」をタップし、AdGuard Playerを選択します(右スクロールして「もっと」をタップする必要があります)。

## 変更履歴

### 改善点
* フォーカスは、Android TV用のAdGuardの左側のメニューを開き、それを閉じた後、同じ場所にとどまります [#5271](https://github.com/AdguardTeam/AdguardForAndroid/issues/5271)

### フィックス
* DNS 保護設定は、デフォルト [#5322] にリセットされません。https://github.com/AdguardTeam/AdguardForAndroid/issues/5322)
* 言語固有のフィルタ "その他" [#5232](https://github.com/AdguardTeam/AdguardForAndroid/issues/5232)
* 低レベルの設定で「メイン画面でDevToolsを表示する」オプションをデフォルトにリセットできなかった[#5331](https://github.com/AdguardTeam/AdguardForAndroid/issues/5331)
* 「adguard:add dns server?address="プレフィックス [#5264]」() と連携して、カスタム DNS サーバーを追加しようとすると、Android TV のアドガードがクラッシュします。https://github.com/AdguardTeam/AdguardForAndroid/issues/5264)



## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.4 ベータ 1

- 公表: 2024-04-27T16:57:29Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4-beta-1

改善されたファイアウォール機能は、Androidベータ用のAdGuard v4.4のハイライトです。 長年に渡ってテストを続けてきましたが、今回ご紹介する準備が整いました。

通知したいアプリを選択できるようになりました。 Chrome 接続に関する通知を受け取りたくないですか? プルダウンメニューを開き、Chromeに関する通知をタップし、*Mute*をタップします。 このアプリのすべてのファイアウォール通知は無効になります。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/mute.png" 
幅="300" 高さ="600">
</p>

あるいは、*Protection* → *Firewall* → *Notifications* に行くこともできます。 アプリを選択し、オフに切り替えます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/settings.png" 
幅="300" 高さ="600">
</p>

また、いくつかのマイナーなバグを修正し、UserscriptsWrapper、CoreLibs、DNsLibsを更新しました。

## 変更履歴

### 改善点
* ChromiteブラウザでHTTPSフィルタリングを有効にして、無料で[#4997](https://github.com/AdguardTeam/AdguardForAndroid/issues/4997)
* 開発者ツールのセクションの改善 [#5173](https://github.com/AdguardTeam/AdguardForAndroid/issues/5173)
* 空のユーザールールリストでルールをエクスポートしようとすると、「エクスポートする」スナックを追加する[#5176](https://github.com/AdguardTeam/AdguardForAndroid/issues/5176)
* com.klookアプリをデフォルトHTTPSフィルタリング除外に追加 [#5143](https://github.com/AdguardTeam/AdguardForAndroid/issues/5143)
* com.nekki.shadowfightarena を QUIC のバイパス パッケージにデフォルトで含める [#5158](https://github.com/AdguardTeam/AdguardForAndroid/issues/5158)

### フィックス
* ライセンスキーが隠されていない [#4496](https://github.com/AdguardTeam/AdguardForAndroid/issues/4496)
* 翻訳の修正`it`ロケール [#5180](https://github.com/AdguardTeam/AdguardForAndroid/issues/5180)
* AutorunはChromecastとSony TVを再起動した後に動作しません [#5156](https://github.com/AdguardTeam/AdguardForAndroid/issues/5156)
* 大きい電池の消費[#4960] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4960)
* キャッシュサイズが急速に成長 [#5125](https://github.com/AdguardTeam/AdguardForAndroid/issues/5125)
* Userscript の状態の変更を行い、戻ったときにアプリがクラッシュする [#5131](https://github.com/AdguardTeam/AdguardForAndroid/issues/5131)
* インドネシア語を選択するとアプリがクラッシュ [#5236](https://github.com/AdguardTeam/AdguardForAndroid/issues/5236)
* DNS サーバーの設定は、DNS フィルタ タブ [#5142] の設定をリセットした後にリセットされます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5142)
* 証明書のインストールの失敗に関するダイアログは、成功したインストール後に消えません [#5194](https://github.com/AdguardTeam/AdguardForAndroid/issues/5194)
* アプリケーション更新をダウンロードすると、バッテリー容量の400 mAh以上かかります[#5259](https://github.com/AdguardTeam/AdguardForAndroid/issues/5259)
* ケースの差[#5037]を使ってウェブサイトの許可者に重複を追加できます(https://github.com/AdguardTeam/AdguardForAndroid/issues/5037)
* 設定をエクスポートする際にエラー [#5069](https://github.com/AdguardTeam/AdguardForAndroid/issues/5069)
* 背景画像は、com.opera.browser [#5096] でブロックされます。https://github.com/AdguardTeam/AdguardForAndroid/issues/5096)
* デバイスペアリングエラー(com.meross.meross) [#4989](https://github.com/AdguardTeam/AdguardForAndroid/issues/4989)
* 2つのコンポーネントを持つ選択した会社の最近の活動が表示されない[#5067](https://github.com/AdguardTeam/AdguardForAndroid/issues/5067)
* すべての DNS エントリの [#4824] (.) 文字を削除します。https://github.com/AdguardTeam/AdguardForAndroid/issues/4824)
* ブラウジングセキュリティ画面のスクロール領域の問題[#5195](https://github.com/AdguardTeam/AdguardForAndroid/issues/5195)
* スクロールバーの親指は、最近の活動の下部メニューの後ろに行きます [#4901](https://github.com/AdguardTeam/AdguardForAndroid/issues/4901)
* 申し込みを最小限にすることでスナックを閉じる [#5018](https://github.com/AdguardTeam/AdguardForAndroid/issues/5018)
* いくつかのカスタムフィルタプロパティが正しく更新しない[#5171](https://github.com/AdguardTeam/AdguardForAndroid/issues/5171)
* メイン画面のスタディティスティックカードはフルスクリーンの幅を埋めません [#5118](https://github.com/AdguardTeam/AdguardForAndroid/issues/5118)
* ポップアップはシステム言語で表示され、アプリケーション全体が英語[#5168]にある間(https://github.com/AdguardTeam/AdguardForAndroid/issues/5168)
* 無線ボタンの状態はBootstrapの上流の選択[#5239]のために輸入されません(https://github.com/AdguardTeam/AdguardForAndroid/issues/5239)
* 更新ローダーが正しく機能しない[#5028](https://github.com/AdguardTeam/AdguardForAndroid/issues/5028)
* 通知シェードを介して無効にすると、アプリの再オープン時に自動的に有効になります [#5146](https://github.com/AdguardTeam/AdguardForAndroid/issues/5146)
* AdGuard保護機能により、インターネット接続がない場合のアプリレポート[#5209](https://github.com/AdguardTeam/AdguardForAndroid/issues/5209)
* Santander と Sainsburys Bank アプリは HTTPS フィルタリング を [#5058] で括っています。https://github.com/AdguardTeam/AdguardForAndroid/issues/5058)

### CoreLibs (フィルターエンジン) を v1.14.51 [#5280] に更新しました。https://github.com/AdguardTeam/AdguardForAndroid/issues/5280)

#### 改善点
* 追加`GM.xmlhttpRequest`エイリアスとして`GM_xmlhttpRequest` [#1785](https://github.com/AdguardTeam/CoreLibs/issues/1785)
* アウトバウンドプロキシは、リクエスト処理イベント(#1385)で使用されます。https://github.com/AdguardTeam/CoreLibs/issues/1385)
* アウトバウンドプロキシにホストを渡すためのサポートを追加 [#1386](https://github.com/AdguardTeam/CoreLibs/issues/1386)
* Firefox 121.0+ をユーザエージェントのリストに追加しました。`:has()` [#1840](https://github.com/AdguardTeam/CoreLibs/issues/1840)
* インターセプトされた DNS HTTPS クエリから ECH パラメータを追加 [#1794]()https://github.com/AdguardTeam/CoreLibs/issues/1794)
* 改善されたHTMLのろ過性能[#1855] (https://github.com/AdguardTeam/CoreLibs/issues/1855)
* 使用するオプションを追加`|`分離器として`$permissions` [#1850](https://github.com/AdguardTeam/CoreLibs/issues/1850)

#### フィックス
* お問い合わせ`$permissions`お問い合わせ`document` [#1856](https://github.com/AdguardTeam/CoreLibs/issues/1856)
* QUIC ClientHello を 2 つのパケットに分割できません。 [#1861](https://github.com/AdguardTeam/CoreLibs/issues/1861)
* VOTスクリプトはGoogle chromeで動作しません [#1665](https://github.com/AdguardTeam/CoreLibs/issues/1665)
* 正規化ヘッダでリクエストをリダイレクトしない[#1851](https://github.com/AdguardTeam/CoreLibs/issues/1851)
* 韓国の電気通信のためのサポート反DPIの特徴[#1789] (https://github.com/AdguardTeam/CoreLibs/issues/1789)
* クッキーに関するルール`[`そして、`]`お名前が無効です [#1843](https://github.com/AdguardTeam/CoreLibs/issues/1843)
* AdGuardがAdGuard VPNブラウザの拡張機能と一緒に動作する場合、化粧品のルールは適用されません[#1791](https://github.com/AdguardTeam/CoreLibs/issues/1791)
* サブドメインの1つは、異なるサイトの証明書[#1839]のためにフィルタリングされていません(https://github.com/AdguardTeam/CoreLibs/issues/1839)
* `$all`修飾子が正しく機能しない[#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)
* `mall.sk`コンテンツスクリプトは注入されません [#1834](https://github.com/AdguardTeam/CoreLibs/issues/1834)
* キャラクタークラスでエスラッシュをエスケープした正規表現のブロックは動作しません[#1831](https://github.com/AdguardTeam/CoreLibs/issues/1831)
* doctype宣言前のタグ(埋め込み属性)がある場合、コンテンツスクリプトは注入されません[#1825](https://github.com/AdguardTeam/CoreLibs/issues/1825)
* `$path`修飾子はクエリパラメータで動作しません [#1817](https://github.com/AdguardTeam/CoreLibs/issues/1817)
* `$removeparam`ポート付き url でポートなしで url にリダイレクト [#1818](https://github.com/AdguardTeam/CoreLibs/issues/1818)
* `android-hilfe.de`ブレーキサイト [#1800](https://github.com/AdguardTeam/CoreLibs/issues/1800)
* wiki.cemu.infoを安全に接続できません。 [#1821](https://github.com/AdguardTeam/CoreLibs/issues/1821)

### スクリプト(フィルタリングルールのJavaScriptの強化)をv1.10.25に更新

#### 改善点
* グーグルアナリティクスの改善、追加`ga.q`プロパティ [#355](https://github.com/AdguardTeam/Scriptlets/issues/355)
* google-ima3の改善、追加`OmidVerificationVendor`プロパティ [#353](https://github.com/AdguardTeam/Scriptlets/issues/353)
* uBO の set-cookie スクリプトレット [#332] との互換性を追加しました。https://github.com/AdguardTeam/Scriptlets/issues/332)
* 新しいスクリプトレットを追加`href-sanitizer` [#327](https://github.com/AdguardTeam/Scriptlets/issues/327)
* 新しいスクリプトレットを追加`json-prune-fetch-response` [#361](https://github.com/AdguardTeam/Scriptlets/issues/361)
* 新しいスクリプトレットを追加`json-prune-xhr-response` [#360](https://github.com/AdguardTeam/Scriptlets/issues/360)
* 新しいスクリプトレットを追加`trusted-suppress-native-method` [#383](https://github.com/AdguardTeam/Scriptlets/issues/383)
* 新しいスクリプトレットを追加`no-protected-audience` [#395](https://github.com/AdguardTeam/Scriptlets/issues/395)
* 改善しました`set-cookie`, 可能な数値を増加 [#388](https://github.com/AdguardTeam/Scriptlets/issues/388)
* 改善しました`trusted-click-element`, shadowRootでセレクターを見つけるためのサポートを追加しました [#323](https://github.com/AdguardTeam/Scriptlets/issues/323)
* リソースをスクリプトとしてリダイレクトするだけでなく、 [#300](https://github.com/AdguardTeam/Scriptlets/issues/300)
* スクリプトレットを許可する可能性を追加 [#377](https://github.com/AdguardTeam/Scriptlets/issues/377)
* 改善しました`prevent-fetch`, 追加`cors`responseType [#394]()https://github.com/AdguardTeam/Scriptlets/issues/394)
* 改善しました`set-cookie`, 追加`domain`パラメーター [#389](https://github.com/AdguardTeam/Scriptlets/issues/389)
* 新しいスクリプトレットを追加`call-nothrow.js` [#333](https://github.com/AdguardTeam/Scriptlets/issues/333)
* 新しいスクリプトレットを追加`spoof-css` [#317](https://github.com/AdguardTeam/Scriptlets/issues/317)
* 新しいスクリプトレットを追加`trusted-create-element` [#278](https://github.com/AdguardTeam/Scriptlets/issues/278)
* 改善しました`set-cookie`, よりサポートされている値を追加 [#379](https://github.com/AdguardTeam/Scriptlets/issues/379)
* 新しいスクリプトレットを追加`trusted-set-attr` [#281](https://github.com/AdguardTeam/Scriptlets/issues/281)

#### フィックス
* 固定式`set-constant`— setProxyTrap() [#403]()https://github.com/AdguardTeam/Scriptlets/issues/403)
* 固定式`set-cookie`, クッキー名をエンコードしません [#408](https://github.com/AdguardTeam/Scriptlets/issues/408)
* 固定式`set-local-storage-item`変換,`$remove$`パラメータ [#404](https://github.com/AdguardTeam/Scriptlets/issues/404)

### UserscriptsWrapperがv1.2.23に更新

### DnsLibs (DNS フィルタリングエンジン) v2.5.4 [#5237] に更新https://github.com/AdguardTeam/AdguardForAndroid/issues/5237)

#### 改善点
* tcp-only と udp-only DNS 上流を指定できるようになりました [#208](https://github.com/AdguardTeam/DnsLibs/issues/208)
* ブートストラップの代わりに、ホスト名をアウトバウンドプロキシに渡すサポート [#197](https://github.com/AdguardTeam/DnsLibs/issues/197)
* HTTPS RRType [#215] の処理を改善しました(https://github.com/AdguardTeam/DnsLibs/issues/215)

#### フィックス
* v4.3 [#216] に更新した後に HTTP/1.1 を使用する DoH DNS サーバーを使用できません。https://github.com/AdguardTeam/DnsLibs/issues/216)
* DoHのIPv4/IPv6のための幸せな眼球を使用して下さい[#217] (https://github.com/AdguardTeam/DnsLibs/issues/217)


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.3.1

- 発行: 2023-12-27T16:46:42Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3.1

時々、リリースは非常に重要でエキサイティングで、バグが抜けるのが簡単です。 残りは、できるだけ早く新しいバージョンをリリースすることです。 このホットフィックスでは、HTTPSプロキシがブラウザで有効になっていると、メジャーな問題が修正されました。 また、必ずその旨をお伝えします。`$all`修飾子は正しく機能し、CoreLibs と DnsLibs をアップデートしました。私たちの最愛のフィルタリングエンジンは、いくつかの改善を加えました。 言うべきことはありますか? 更新して、自分で見る!

## 変更履歴

### フィックス
* ブラウザで HTTPS プロキシが設定されている場合、AdGuard がクラッシュ [#5130](https://github.com/AdguardTeam/AdguardForAndroid/issues/5130)
* Xiaomiデバイス上の「常に保護された」カード再登場[#5126](https://github.com/AdguardTeam/AdguardForAndroid/issues/5126)

### CoreLibs (フィルターエンジン)
* CoreLibs は v1.13.115 [#5124] に更新されました。https://github.com/AdguardTeam/AdguardForAndroid/issues/5124) 
* `$all`修飾子が正しく機能しない[#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)

### DnsLibs (DNSのろ過エンジン)
* DnsLibs が v2.4.37 に更新 [#5123](https://github.com/AdguardTeam/AdguardForAndroid/issues/5123) 


## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.3.1 ベータ 1

- 公開日: 2023-12-26T14:10:44Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3.1-beta-1

時々、リリースは非常に重要でエキサイティングで、バグが抜けるのが簡単です。 残りは、できるだけ早く新しいバージョンをリリースすることです。 このベータ版では、HTTPSプロキシがブラウザで有効になっていると、メジャーな問題が修正されました。 また、必ずその旨をお伝えします。`$all`修飾子は正しく機能し、CoreLibs と DnsLibs をアップデートしました。私たちの最愛のフィルタリングエンジンは、いくつかの改善を加えました。 言うべきことはありますか? 更新して、自分で見る!

## 変更履歴

### フィックス
* ブラウザでHTTPSプロキシが設定されている場合、AdGuardがクラッシュ [#5130](https://github.com/AdguardTeam/AdguardForAndroid/issues/5130)

### CoreLibs (フィルターエンジン)
* CoreLibs は v1.13.115 [#5124] に更新されました。https://github.com/AdguardTeam/AdguardForAndroid/issues/5124) 
* `$all`修飾子が正しく機能しない[#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)

### DnsLibs (DNSのろ過エンジン)
* DnsLibs が v2.4.37 に更新 [#5123](https://github.com/AdguardTeam/AdguardForAndroid/issues/5123)

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 4.3

- 公表: 2023-12-22T12:54:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3

Android用のAdGuard v4.3は、特別なだけでなく、前例のない何かをもたらします。 あなたが知っていると愛するのと同じAdGuardですが、今ではテレビサイズのツイストで - 私たちは、非常に文字通り:私たちは、Android TVのためのサポートを導入してうれしいです! 重要なアップデートと新しい開発者ツールセクションでは、アプリでユーザーエクスペリエンスを向上させることもできます。

## アンドロイドテレビのサポート

![Android TV用ガード]https://cdn.adguard.com/content/blog/articles/androidtv_en.png)

Android TVのフルサポートを提供するために、私たちはあなたのテレビ上での閲覧体験とコンテンツのフィルタリングを高めるために、最も必要な機能を備えたAndroid用のAdGuardのバージョンを開発しました。 新しいデザイン、完全にAndroid TVのために適応、以下を含みます:

* 適応オンボーディング
* 統計とホーム画面
* 適応保護画面
* 適応設定
* アプリ管理
* DNS保護

DNS保護は、Android TV用のAdGuardの重要な機能です。 暗号化によるDNSトラフィックの確保により、セキュリティとプライバシーの余剰レイヤーがあなたの閲覧体験に追加されます。 このアップデートでは、大きな画面でもこの安全にも恩恵を受けることができます。 DNS-over-HTTPS はデフォルトで選択されますが、異なるプロトコルが必要な場合は独自のサーバーを追加できます。

リモートに持ち込むと、経験するのが新しいアプリです! あなたは、Android TV用のAdGuardをインストールする方法についての詳細な手順を見つけることができます [私たちのブログ投稿](https://adguard.com/en/blog/adguard-for-android-tv.html).

> 注意: Android TV用のAdGuardを使用するライセンスが必要です。 しかし、無料で試してみることもできます。7日間のトライアル期間を提供します。

## 開発者ツール

<p align="center">
<img src="">https://cdn.adguard.com/content/blog/articles/developertools_en.jpg" 
幅="300" 高さ="600">
</p>

高度なユーザーを招待し、アプリと非常に積極的にやり取りする開発者をフィルタリングし、新しい開発者ツール、クイックナビゲーションと機能間の切り替え用に設計された専門セクションを探索します。 カスタムフィルタ、アクセスログ、異なるログの録画を有効にしたり、無効にしたりすることができます。 ※低レベル設定*でこの機能を有効にできます。

## CoreLibsとDnsLibsのアップデート

最近のCoreLibs v1.13 更新は、DnsLibs のアップデートが HTTP 基本認証をサポートすることで、閲覧体験を向上させます。

## HTTPS フィルタリングの透明性

HTTPS フィルタリングの透明性を高めるため、AdGuard は *Recent アクティビティ* で元の証明書を検査するオプションを提供します。 任意のWebリクエストの詳細を表示したり、AdGuardが使用する暗号化を調べたり、元の証明書を調べたりすることができます。

この機能は、HTTPS フィルタリングに大きな懸念を伴います。 AdGuardは証明書を検証します(そしてそれはうまくいきます!)が、元の証明書を自分で検査したい状況があるかもしれません。 「ナレッジベース」でこの問題についてもっと読むことができます(https://adguard.com/kb/general/https-filtering/known-issues/).  

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/tvapk)
- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 変更履歴

### 特徴:
* ブラウザの一覧に Fulguris を追加しました [#4969](https://github.com/AdguardTeam/AdguardForAndroid/issues/4969)
* 除外するロシアVoWiFi IPのリストを追加しました [#4992](https://github.com/AdguardTeam/AdguardForAndroid/issues/4992)
* Android TV OS対応追加 [#3597](https://github.com/AdguardTeam/AdguardForAndroid/issues/3597)
* DNS保護設定をリセットするボタンを追加[#4735](https://github.com/AdguardTeam/AdguardForAndroid/issues/4735)
* アンドロイド用のAdGuardにMacedonian(mk)のサポートを追加しました [#5086]()https://github.com/AdguardTeam/AdguardForAndroid/issues/5086)
* デフォルトで無効なcom.kantarworldpanel.shoppixのためのHTTPSのろ過[#4706](https://github.com/AdguardTeam/AdguardForAndroid/issues/4706)
* バック矢印ボタンのエリアをクリックすると、[#4789]が増加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/4789)
* ユーザルールの順序をソートする 改善 [#4779](https://github.com/AdguardTeam/AdguardForAndroid/issues/4779)
* フィルタリストサブスクリプションから'Title'メタデータをパース [#4760](https://github.com/AdguardTeam/AdguardForAndroid/issues/4760)
* オペレーティング・システム名 + ReportWebAppに送信されたバージョン [#5025](https://github.com/AdguardTeam/AdguardForAndroid/issues/5025)

### フィックス
* デバッグロギングレベルを有効にすると「スローワーク」通知が消えます [#5017](https://github.com/AdguardTeam/AdguardForAndroid/issues/5017)
* 製品の種類とAdGuardバージョンは「報告誤ったブロック」フォームで誤って検出されます[#4895](https://github.com/AdguardTeam/AdguardForAndroid/issues/4895)
* ブートストラップアップストリームの設定は、低レベルの設定をリセットした後にリセットされません [#4907](https://github.com/AdguardTeam/AdguardForAndroid/issues/4907)
* ブロックリストからWebサイトを削除しても正常に動作しない [#4902](https://github.com/AdguardTeam/AdguardForAndroid/issues/4902)
* 無料版では、更新チェック時に「無効なブラウジングセキュリティ」が「更新」と表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4844)
* フィルタは、英語のみで見つけることができます [#5026](https://github.com/AdguardTeam/AdguardForAndroid/issues/5026)
* ファイアウォールは無効なときに機能し、アプリ使用アクセスがない[#5012](https://github.com/AdguardTeam/AdguardForAndroid/issues/5012)
* Googleの演劇:`com.gpn.azs`アプリが動作しない [#4845](https://github.com/AdguardTeam/AdguardForAndroid/issues/4845)
* Google Play: de.dkb.portalapp が正しくブロックされていない [#3734](https://github.com/AdguardTeam/AdguardForAndroid/issues/3734)
* 別の言語で設定をインポートしても正しく機能しない[#5007](https://github.com/AdguardTeam/AdguardForAndroid/issues/5007)
* 「Orange Téléphone」アプリ「#4777」でボーカルメッセージのオープンとリスニングが可能https://github.com/AdguardTeam/AdguardForAndroid/issues/4777)
* すべての設定で表示されるスナックでは、「Undo」は他の言語に翻訳されていません [#4880](https://github.com/AdguardTeam/AdguardForAndroid/issues/4880)
* スイッチを押すとき機能の追跡の保護点滅で[#4879] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4879)
* アイコンをタップして保護セクションにリダイレクトすると、間違ったタブが強調表示されます[#4860](https://github.com/AdguardTeam/AdguardForAndroid/issues/4860)
* ウェブサイトのウィットリスト/ブロックリスト[#4843]からスナックをタップした後に無限のローダー()https://github.com/AdguardTeam/AdguardForAndroid/issues/4843)
* クリップボード[#5009]で2行ルールを作ることができます(https://github.com/AdguardTeam/AdguardForAndroid/issues/5009)
* 画面の上部を衝突した後、検索フィールドにキーボードのラグとテキストを入力することができません[#4979](https://github.com/AdguardTeam/AdguardForAndroid/issues/4979)
* ライセンス有効期限が正しく表示されていない[#4856](https://github.com/AdguardTeam/AdguardForAndroid/issues/4856)
* プロキシサーバー [#4884] で変更ログインとパスワードのアップロードをログに記録します(https://github.com/AdguardTeam/AdguardForAndroid/issues/4884)
* 長いオプション名はルール作成ダイアログに合わない [#4764](https://github.com/AdguardTeam/AdguardForAndroid/issues/4764)
* 「言語固有の広告ブロック」画面[#4891]に非関連性の結果も表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4891)
* アシスタントからのリダイレクトは、バー [#5001] の誤ったタブを強調します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5001)
* ユーザスクリプト link [#4913] で AdGuard にリダイレクトしたときに "Add userscript" ポップアップが表示されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4913)
* 検索フィールドのカーソル位置は、画面の上部を衝突した後にリセット [#4892](https://github.com/AdguardTeam/AdguardForAndroid/issues/4892)
* 最近の活動画面の検索フィールドに loader が表示されます [#5035](https://github.com/AdguardTeam/AdguardForAndroid/issues/5035)
* 関係のない目的のために同じアイコンが使用されます [#4737](https://github.com/AdguardTeam/AdguardForAndroid/issues/4737)
* チェックボックス「Send app logs...」がマークされたときにバグ報告を送信できない[#4894](https://github.com/AdguardTeam/AdguardForAndroid/issues/4894)
* ファイルを使用してシステムからDNSフィルタを追加すると、入力フィールドは[#4882]をグレーアウトします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4882)
* カスタムDNSフィルタやユーザースクリプトを追加すると、 "Browse" ボタンは [#4850] をグレーアウトします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4850)
* 無効なオプションの設定を変更すると、保護が再起動されます [#4762](https://github.com/AdguardTeam/AdguardForAndroid/issues/4762)
* 空の行を含むDNSユーザールールをインポートすると、これらの行が [#4888] に追加されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4888)
* ファイアウォールルールのスイッチを素早く切り替えると、ルールリスト行の不具合 [#4885](https://github.com/AdguardTeam/AdguardForAndroid/issues/4885)
* XiaomiでWi-Fiコールの問題:com.qualcomm.qti.cneを追加して除外をルーティングする[#5029](https://github.com/AdguardTeam/AdguardForAndroid/issues/5029)
* 統計をクリアすると、アプリや企業セクションをクリアするだけで、カウンターをゼロにリセットしません[#4748](https://github.com/AdguardTeam/AdguardForAndroid/issues/4748)
* AdGuard対応のONECTA-Daikinアプリにログイン可能[#4775]()https://github.com/AdguardTeam/AdguardForAndroid/issues/4775)
​
## DnsLibs (DNSのろ過エンジン)
​
### DnsLibs が v2.4.16 に更新
* DoH接続のオンザフライフィルタ [#198](https://github.com/AdguardTeam/DnsLibs/issues/198)
​
### DnsLibs が v2.4.0 に更新
* DoH エンドポイントの基本的なオース [#189]()https://github.com/AdguardTeam/DnsLibs/issues/189)
* プレーン DNS 上流 [#202] を使用しているときに、ローカル DNS プロキシに対して DoS 攻撃が可能https://github.com/AdguardTeam/DnsLibs/issues/202)
​
### DnsLibs が v2.3.4 に更新
* `127.0.0.1 local`mDNS [#207] を区切る、すべての .local アドレスに対して正しく解釈されます。https://github.com/AdguardTeam/DnsLibs/issues/207)
* ドメイン名規則でC#コメントを許可する [#196](https://github.com/AdguardTeam/DnsLibs/issues/196)
* DoH は、ステープル接続を長時間使用しようとします [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* 適切なフィルタtype=HTTPSリクエスト [#199]()https://github.com/AdguardTeam/DnsLibs/issues/199)
​
## CoreLibs (フィルターエンジン)

### CoreLibs が v1.13.98 に更新
* 追加する`!#else`プリプロセッサディレクティブ サポート [#1806](https://github.com/AdguardTeam/CoreLibs/issues/1806)
* 追加する`$extension`修飾子 特定のユーザスクリプトを無効に [#1706](https://github.com/AdguardTeam/CoreLibs/issues/1706)
* 新たなルール優先スキーム[#1768](https://github.com/AdguardTeam/CoreLibs/issues/1768)
* sec-ch-ua ヘッダーを変更して、Stealth モードがアクティブであるときにユーザエージェントにマッチする [#1764](https://github.com/AdguardTeam/CoreLibs/issues/1764)
* HTML フィルタリング性能を改善 [#1772](https://github.com/AdguardTeam/CoreLibs/issues/1772)
* HTMLフィルタリングルールを改善`$$`-- CSS のようなセレクターを許可します。 [#94](https://github.com/AdguardTeam/CoreLibs/issues/94)
* cap html filtering 条件のサポート [#1758](https://github.com/AdguardTeam/CoreLibs/issues/1758)
* $denyallow は文書のブロックを許可していません [#1809](https://github.com/AdguardTeam/CoreLibs/issues/1809)
* $stealth 例外は、STUN/TURN [#1737] をブロックする TCP スタックレベルで動作しません。https://github.com/AdguardTeam/CoreLibs/issues/1737)
* Edge Bing Chat [#1744] に画像が表示されません(https://github.com/AdguardTeam/CoreLibs/issues/1744)
* ザ・オブ・ザ・`网盘直链下载助手`ユーザスクリプトは、AdGuard [#1780] で動作していません。https://github.com/AdguardTeam/CoreLibs/issues/1780)
* SXGを使用したサイトでは、Google検索から開く際の化粧品のフィルタリングはありません[#1812](https://github.com/AdguardTeam/CoreLibs/issues/1812)
* AdGuard v4.0 で動作しないソックス5プロキシ [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* コンテンツスクリプトは読み込まれた要素に注入されない`object`タグ [#1769](https://github.com/AdguardTeam/CoreLibs/issues/1769)
* HTML "lang" 属性と言語リクエスト HTTP ヘッダ [#1736] に基づいてウェブサイトのロケールを検知します。https://github.com/AdguardTeam/CoreLibs/issues/1736)
* 限界を増加して下さい`$replace`ルール [#1802](https://github.com/AdguardTeam/CoreLibs/issues/1802)
* 移行証明書はもうオプションではありません [#277](https://github.com/AdguardTeam/CoreLibs/issues/277)
*  適切に ECH retry configs [#1793] を使用します。https://github.com/AdguardTeam/CoreLibs/issues/1793)
*  韓国の電気通信のためのサポート反DPIの特徴[#1789] (https://github.com/AdguardTeam/CoreLibs/issues/1789)
*  TcpIpStack [#1796] で UDP のタイムアウトが少なすぎる (https://github.com/AdguardTeam/CoreLibs/issues/1796)

## 4.3 ベータ 1

- 公表: 2023-12-15T19:07Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3-beta-1

Androidのベータ版のAdGuard v4.3は、特別なだけでなく、前例のない何かをもたらします。 あなたが知っていると愛するのと同じAdGuardですが、今ではテレビサイズのツイストで - 私たちは、非常に文字通り:私たちは、Android TVのためのサポートを導入してうれしいです! 重要なアップデートと新しい開発者ツールのセクションも、アプリでユーザーエクスペリエンスを向上させるためにここにあります

## アンドロイドテレビのサポート

Android TVのフルサポートを提供するために、私たちはあなたのテレビで閲覧経験とコンテンツのフィルタリングを高めるために最も必要な機能を備えたAndroid用のAdGuardのシンプルなバージョンを開発しました。 新しいデザイン、完全にAndroid TVに対応しました。

リモートに持ち込むと、経験するのが新しいアプリです!

> 注意: Android TV サポートは、AdGuard ライセンスを持つユーザーに排他的な機能です。

## 開発者ツール

高度なユーザーを招待し、アプリと非常に積極的にやり取りする開発者をフィルタリングし、新しい開発者ツール、クイックナビゲーションと機能間の切り替え用に設計された専門セクションを探索します。 カスタムフィルタ、アクセスログ、異なるログの録画を有効にしたり、無効にしたりすることができます。 ※低レベル設定*でこの機能を有効にできます。

## CoreLibsとDnsLibsのアップデート

最近のCoreLibs v1.13 更新は、DnsLibs のアップデートが HTTP 基本認証をサポートすることで、閲覧体験を向上させます。

## アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## Android TVの直接ダウンロードリンクのためのAdGuard:

- [ベータチャンネル ](https://agrd.io/ag_android_tv_beta)

## 変更履歴

### 特徴:
* ブラウザの一覧にブラウザを追加しました [#4969](https://github.com/AdguardTeam/AdguardForAndroid/issues/4969)
* 除外するロシアのVoWiFi IPのリスト [#4992](https://github.com/AdguardTeam/AdguardForAndroid/issues/4992)
* Android TV OS対応追加 [#3597](https://github.com/AdguardTeam/AdguardForAndroid/issues/3597)
* DNS保護設定をリセットするボタンを追加[#4735](https://github.com/AdguardTeam/AdguardForAndroid/issues/4735)
* アンドロイド用のAdGuardにMacedonian(mk)のサポートを追加 [#5086](https://github.com/AdguardTeam/AdguardForAndroid/issues/5086)
* デフォルトで無効なcom.kantarworldpanel.shoppixのためのHTTPSのろ過[#4706](https://github.com/AdguardTeam/AdguardForAndroid/issues/4706)
* バック矢印ボタンのエリアをクリックすると、[#4789]が増加しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/4789)
* ユーザルールの順序をソートする 改善 [#4779](https://github.com/AdguardTeam/AdguardForAndroid/issues/4779)
* フィルタリストサブスクリプションから'Title'メタデータをパース [#4760](https://github.com/AdguardTeam/AdguardForAndroid/issues/4760)
* オペレーティング・システム名 + ReportWebAppに送信されたバージョン [#5025](https://github.com/AdguardTeam/AdguardForAndroid/issues/5025)

### フィックス
* デバッグロギングレベルを有効にすると「スローワーク」通知が消えます [#5017](https://github.com/AdguardTeam/AdguardForAndroid/issues/5017)
* 製品の種類とAdGuardバージョンは「報告誤ったブロック」フォームで誤って検出されます[#4895](https://github.com/AdguardTeam/AdguardForAndroid/issues/4895)
* ブートストラップアップストリームの設定は、低レベルの設定をリセットした後にリセットされません [#4907](https://github.com/AdguardTeam/AdguardForAndroid/issues/4907)
* ブロックリストからWebサイトを削除しても正常に動作しない [#4902](https://github.com/AdguardTeam/AdguardForAndroid/issues/4902)
* 無料版では、更新チェック時に「無効なブラウジングセキュリティ」が「更新」と表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4844)
* フィルタは、英語のみで見つけることができます [#5026](https://github.com/AdguardTeam/AdguardForAndroid/issues/5026)
* ファイアウォールは無効なときに機能し、アプリ使用アクセスがない[#5012](https://github.com/AdguardTeam/AdguardForAndroid/issues/5012)
* Googleの演劇:`com.gpn.azs`アプリが動作しない [#4845](https://github.com/AdguardTeam/AdguardForAndroid/issues/4845)
* Google Play: de.dkb.portalapp が正しくブロックされていない [#3734](https://github.com/AdguardTeam/AdguardForAndroid/issues/3734)
* 別の言語で設定をインポートしても正しく機能しない[#5007](https://github.com/AdguardTeam/AdguardForAndroid/issues/5007)
* 「Orange Téléphone」アプリ「#4777」で音声メッセージが開けて聞こえる可能性が高いhttps://github.com/AdguardTeam/AdguardForAndroid/issues/4777)
* すべての設定で表示されるスナックでは、「Undo」は他の言語に翻訳されていません [#4880](https://github.com/AdguardTeam/AdguardForAndroid/issues/4880)
* スイッチを押すとき機能の追跡の保護点滅で[#4879] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4879)
* アイコンをタップして保護セクションにリダイレクトすると、間違ったタブが強調表示されます[#4860](https://github.com/AdguardTeam/AdguardForAndroid/issues/4860)
* ウェブサイトのウィットリスト/ブロックリスト[#4843]からスナックをタップした後に無限のローダー()https://github.com/AdguardTeam/AdguardForAndroid/issues/4843)
※クリップボード[#5009]で2行ルールを作ることができます(https://github.com/AdguardTeam/AdguardForAndroid/issues/5009)
* 画面の上部を衝突した後、検索フィールドにキーボードのラグとテキストを入力することができません[#4979](https://github.com/AdguardTeam/AdguardForAndroid/issues/4979)
* ライセンス有効期限が正しく表示されていない [#4856](https://github.com/AdguardTeam/AdguardForAndroid/issues/4856)
* プロキシサーバー [#4884] で変更ログインとパスワードのアップロードをログに記録します(https://github.com/AdguardTeam/AdguardForAndroid/issues/4884)
* 長いオプション名はルール作成ダイアログに合わない [#4764](https://github.com/AdguardTeam/AdguardForAndroid/issues/4764)
* 「言語固有の広告ブロック」画面[#4891]に非関連性の結果も表示されます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4891)
* アシスタントからのリダイレクトは、バー [#5001] の誤ったタブを強調します(https://github.com/AdguardTeam/AdguardForAndroid/issues/5001)
* ユーザスクリプト link [#4913] で AdGuard にリダイレクトしたときに "Add userscript" ポップアップが表示されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4913)
* 検索フィールドのカーソル位置は、画面の上部を衝突した後にリセット [#4892](https://github.com/AdguardTeam/AdguardForAndroid/issues/4892)
* 最近の活動画面の検索フィールドに loader が表示されます [#5035](https://github.com/AdguardTeam/AdguardForAndroid/issues/5035)
* 関係のない目的のために同じアイコンが使用されます [#4737](https://github.com/AdguardTeam/AdguardForAndroid/issues/4737)
* チェックボックス「Send app logs.」がマークされたときにバグ報告を送信できません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4894)
* ファイルを使用してシステムからDNSフィルタを追加すると、入力フィールドは[#4882]をグレーアウトします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4882)
* カスタムDNSフィルタやユーザースクリプトを追加すると、 "Browse" ボタンは [#4850] をグレーアウトします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4850)
* 無効なオプションの設定を変更すると、保護が再起動されます [#4762](https://github.com/AdguardTeam/AdguardForAndroid/issues/4762)
* 空の行を含むDNSユーザールールをインポートすると、これらの行が [#4888] に追加されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4888)
* ファイアウォールルールのスイッチを素早く切り替えると、ルールリスト行の不具合 [#4885](https://github.com/AdguardTeam/AdguardForAndroid/issues/4885)
* XiaomiでWi-Fiコールの問題:com.qualcomm.qti.cneを追加して除外をルーティングする[#5029](https://github.com/AdguardTeam/AdguardForAndroid/issues/5029)
* 統計をクリアすると、アプリや企業セクションをクリアするだけで、カウンターをゼロにリセットしません[#4748](https://github.com/AdguardTeam/AdguardForAndroid/issues/4748)
* AdGuard対応のONECTA-Daikinアプリにログイン可能[#4775]()https://github.com/AdguardTeam/AdguardForAndroid/issues/4775)
​
### DnsLibs が v2.4.16 に更新
​
* DoH接続のオンザフライフィルタ [#198](https://github.com/AdguardTeam/DnsLibs/issues/198)
* DoH エンドポイントの基本的なオース [#189](https://github.com/AdguardTeam/DnsLibs/issues/189)
* プレーン DNS 上流 [#202] を使用しているときに、ローカル DNS プロキシに対して DoS 攻撃が可能https://github.com/AdguardTeam/DnsLibs/issues/202)
* `127.0.0.1 local`mDNS [#207] を区切る、すべての .local アドレスに対して正しく解釈されます。https://github.com/AdguardTeam/DnsLibs/issues/207)
* ドメイン名規則でC#コメントを許可する [#196](https://github.com/AdguardTeam/DnsLibs/issues/196)
* DoH は、ステープル接続を長時間使用しようとします [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* 適切なフィルタtype=HTTPSリクエスト [#199]()https://github.com/AdguardTeam/DnsLibs/issues/199)
​
### CoreLibs が v1.13.98 に更新
​
* 追加する`!#else`プリプロセッサディレクティブ サポート [#1806](https://github.com/AdguardTeam/CoreLibs/issues/1806)
* 追加する`$extension`修飾子 特定のユーザスクリプトを無効に [#1706](https://github.com/AdguardTeam/CoreLibs/issues/1706)
* 新たなルール優先スキーム[#1768](https://github.com/AdguardTeam/CoreLibs/issues/1768)
* sec-ch-ua ヘッダーを変更して、Stealth モードがアクティブであるときにユーザエージェントにマッチする [#1764](https://github.com/AdguardTeam/CoreLibs/issues/1764)
* HTML フィルタリング性能を改善 [#1772](https://github.com/AdguardTeam/CoreLibs/issues/1772)
* HTMLフィルタリングルールを改善`$$`-- CSS のようなセレクターを許可します。 [#94](https://github.com/AdguardTeam/CoreLibs/issues/94)
* cap html filtering 条件のサポート [#1758](https://github.com/AdguardTeam/CoreLibs/issues/1758)
* $denyallow は文書のブロックを許可していません [#1809](https://github.com/AdguardTeam/CoreLibs/issues/1809)
* $stealth 例外は、STUN/TURN [#1737] をブロックする TCP スタックレベルで動作しません。https://github.com/AdguardTeam/CoreLibs/issues/1737)
* SXGを使用したサイトでは、Google検索から開く際の化粧品のフィルタリングはありません[#1812](https://github.com/AdguardTeam/CoreLibs/issues/1812)
* AdGuard v4.0 で動作しないソックス5プロキシ [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* コンテンツスクリプトは読み込まれた要素に注入されない`object`タグ [#1769](https://github.com/AdguardTeam/CoreLibs/issues/1769)
* HTML "lang" 属性と言語リクエスト HTTP ヘッダ [#1736] に基づいてウェブサイトのロケールを検知します。https://github.com/AdguardTeam/CoreLibs/issues/1736)
* 限界を増加して下さい`$replace`ルール [#1802](https://github.com/AdguardTeam/CoreLibs/issues/1802)
* 移行証明書はもうオプションではありません [#277](https://github.com/AdguardTeam/CoreLibs/issues/277)
*  適切に ECH retry configs [#1793] を使用します。https://github.com/AdguardTeam/CoreLibs/issues/1793)
*  韓国の電気通信のためのサポート反DPIの特徴[#1789] (https://github.com/AdguardTeam/CoreLibs/issues/1789)
*  TcpIpStack [#1796] で UDP のタイムアウトが少なすぎる (https://github.com/AdguardTeam/CoreLibs/issues/1796)

---

## 4.2

- 公表: 2023-10-23T12:02:32Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2

## AdGuard ダイナミクス

AdGuard for Android でダイナミックなエクスペリエンスを準備し、画面にエキサイティングな新機能が搭載されています。 このアプリは「動的アイコン」のみです。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4317)、ダイナミックなテーマもあります。

設定でこのオプションを有効にすると、AdGuardアプリインターフェイスとアイコンがスマートフォンインターフェイスの色にマッチします。

> これらの機能は、バージョン12以上を実行しているAndroidデバイスでのみ利用可能です。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/dynamicicon.png?mw=500" 
幅="300" 高さ="150">
</p>

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/themes/theme_en.png" 
幅="600" 高さ="600">
</p>

## HTTP/3 フィルタリングサポート [#487](https://github.com/AdguardTeam/CoreLibs/issues/487)

AdGuard は HTTP/1.1 と HTTP/2 トラフィックのみをフィルタリングするようになりました。 このリリースでは、HTTP/3 フィルタリング用の**experimental**サポートを追加しました。 QUICネットワークプロトコルを搭載した HTTP/3 プロトコルは、より安定した高速なインターネット接続だけでなく、より優れたプライバシーとセキュリティを提供します。 HTTP/3フィルタリングを有効にすると、QUICプロトコルを利用し、広告やトラッカーを効果的にブロックすることができます。

HTTP/3 フィルタリングを有効にするには、設定 → 全般 → 上級 → 低レベル設定 → *Filter HTTP/3* に移動し、スイッチを右に切り替えます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/HTTP3filtering_en.png" 
幅="300" 高さ="600">
</p>

## 2つのHTTPS証明書のサポート

2つのHTTPS証明書を実装することにより、Chrome 100以上のルートデバイスでHTTPSフィルタリングの問題を修正しました。 システムストアの証明書はほとんどのアプリでフィルタリングを担当しますが、ユーザストアの証明書は、ChromiumベースのブラウザでHTTPSトラフィックをフィルタリングすることができます。

証明書のインストールも容易になりました。ステップバイステップの指示を追加しました。

2番目の証明書をインストールするには、[設定] → [フィルタリング] → [ネットワーク] → [ HTTPS フィルタリング → *Security 認証*] に移動し、指示に従ってください。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/HTTP3filtering_en.png" 
幅="300" 高さ="600">
</p>

当社のフィルターはさらに強力になり、アプリの安定した性能を確保するために、たくさんのバグを修正しました。 更新までの流れ

## 変更履歴
​
### 特徴:
* Opera ブラウザのデフォルトで HTTPS フィルタリングを有効にしました。 [#4972](https://github.com/AdguardTeam/AdguardForAndroid/issues/4972)
​
### フィックス
* デフォルトでルーティングからINETCOM.TVを除外 [#4723](https://github.com/AdguardTeam/AdguardForAndroid/issues/4723)
* AdGuard は HTTPS の証明書の有効期限による保護を開始できません。 [#4896](https://github.com/AdguardTeam/AdguardForAndroid/issues/4896)
* カスタムフィルタの自動更新は動作しません [496#1](https://github.com/AdguardTeam/AdguardForAndroid/issues/4961)
* AdGuardはユーザーのアカウントからログアウト [#4959](https://github.com/AdguardTeam/AdguardForAndroid/issues/4959)
* AdGuard 通知は、ロックされた画面がスリープモード [#4778] でしばらくオンにする原因となります。https://github.com/AdguardTeam/AdguardForAndroid/issues/4778)
* 証明書がシステムストレージに移動されている場合、AdGuardの再発後にアプリでHTTPSフィルタリングが無効になります[#5008](https://github.com/AdguardTeam/AdguardForAndroid/issues/5008)
* メインスイッチの周りのシャドウはAndroid 8で欠落しています [#4858](https://github.com/AdguardTeam/AdguardForAndroid/issues/4858)
* TalkBack [#4809] では、いくつかの要素が正しく発表されていない (https://github.com/AdguardTeam/AdguardForAndroid/issues/4809)
* スイッチは10-30秒間消え、保護は長時間[#4862]のために再開します(https://github.com/AdguardTeam/AdguardForAndroid/issues/4862)
* 「YouTubeで広告をブロックする方法」画面の下部にあるスペースは、小さな画面でデバイスに欠落しています[#4866](https://github.com/AdguardTeam/AdguardForAndroid/issues/4866)
* 繁体字にアプリが設定されている場合は、更新後に簡体字中国語でフィルタが表示されます[#4949](https://github.com/AdguardTeam/AdguardForAndroid/issues/4949) 
* ファイアウォールタブ間の切り替えは、AdGuardがクラッシュする原因[#4999](https://github.com/AdguardTeam/AdguardForAndroid/issues/4999)
* 異なる言語で設定をインポートするとすぐに言語を変更しない[#4984](https://github.com/AdguardTeam/AdguardForAndroid/issues/4984)
* 設定をインポートする際にライセンスがインポートされていない[#4985](https://github.com/AdguardTeam/AdguardForAndroid/issues/4985)
* 無効な通知に関するスナックの非作業ボタン [#5002](https://github.com/AdguardTeam/AdguardForAndroid/issues/5002)
* 「HTTPSトラフィックをフィルタリングする」画面で、次いで前のアクションをキャンセル [#4993](https://github.com/AdguardTeam/AdguardForAndroid/issues/4993)
* クロスボタンは、言語固有の広告ブロック画面の検索バーにテキストを削除しません[#4978](https://github.com/AdguardTeam/AdguardForAndroid/issues/4978)
* インポート/エクスポートされた設定のテキストは、ダイアログボックス[#4981]に収まりません(https://github.com/AdguardTeam/AdguardForAndroid/issues/4981)

### CoreLibs (フィルターエンジン) を v1.12.80 に更新しました [#4966](https://github.com/AdguardTeam/AdguardForAndroid/issues/4966)

#### 改善点
* ユーザエージェント ストリッピング 改善 [#1345]()https://github.com/AdguardTeam/CoreLibs/issues/1345)
* TCP/IP:新しい拒絶モードを追加 - ICMP管理禁止 [#1774](https://github.com/AdguardTeam/CoreLibs/issues/1774)
* uBO メディアの問い合わせに対応しました [#1707](https://github.com/AdguardTeam/CoreLibs/issues/1707)

#### フィックス
* 応答状態のタイマーで接続が終了 [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180)
* ipTIMEホームルータを使用する際の秒数遅延[#1756](https://github.com/AdguardTeam/CoreLibs/issues/1756)
* AdGuardはWebページの読み込み時間を遅くします [#1522](https://github.com/AdguardTeam/CoreLibs/issues/1522)
* リクエストが[#1766]をクリックしたときに「検索クエリを非表示」オプションを有効にします(https://github.com/AdguardTeam/CoreLibs/issues/1766)
* SOCKS5 プロキシは AdGuard 4.0 で動作しません [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* ECH が有効になったときに ECH グリースを有効にしました [#1781](https://github.com/AdguardTeam/CoreLibs/issues/1781)
* 本テキストの復号化時にHTTPヘッダを削除したバグを修正しました[#1750](https://github.com/AdguardTeam/CoreLibs/issues/1750)
* XPCの準備 [#1675] (https://github.com/AdguardTeam/CoreLibs/issues/1675)
* DNSフォールバックヘルパーは、プロバイダーサーバーの代わりに127.0.0.1を返す[#1687](https://github.com/AdguardTeam/CoreLibs/issues/1687)
* TcpIpStack [#1796] で UDP のタイムアウトが少なすぎる (https://github.com/AdguardTeam/CoreLibs/issues/1796)
​
### DnsLibs (DNS フィルタリングエンジン) v2.2.24 [#4953] に更新https://github.com/AdguardTeam/AdguardForAndroid/issues/4953)

#### フィックス
* DoH は、余りに長い [#200] の stale 接続を使用するしようとします(https://github.com/AdguardTeam/DnsLibs/issues/200)
* CoreDNS DoQ サーバは DnsLibs [#204] では使用できません。https://github.com/AdguardTeam/DnsLibs/issues/204)
* sdns:// cert pinning が間違っている [#205](https://github.com/AdguardTeam/DnsLibs/issues/205)

### フィルターメンテナーの重要事項

* 追加`$referral-policy`修飾子 [#135] (https://github.com/AdguardTeam/CoreLibs/issues/135)
* 追加`$method`基本ルールの修飾語 [#1713](https://github.com/AdguardTeam/CoreLibs/issues/1713)
* 空のパターンで$stealthルールを許可 [#1762](https://github.com/AdguardTeam/CoreLibs/issues/1762)
* 追加`$to`修飾子 [#1714] (https://github.com/AdguardTeam/CoreLibs/issues/1714)
* `$jsonprune`, `$replace`と`$hls`非 GET/POST HTTP メソッドで動作しない [#1743](https://github.com/AdguardTeam/CoreLibs/issues/1743)
* 例外ルールは互いに干渉する [#1749](https://github.com/AdguardTeam/CoreLibs/issues/1749)
* `$path`修飾子はパスmarket.yandex.ru [#1726]で動作しません()https://github.com/AdguardTeam/CoreLibs/issues/1726)
* `$jsonprune`modifier は jsonp [#1734]() の引用符を扱うことができます。https://github.com/AdguardTeam/CoreLibs/issues/1734)
* お問い合わせ`:has()`, `:not()`と`:is()`extendCss の使用が強制されていない場合、標準擬似クラスとして`#?#`ルールマーカー [#1683](https://github.com/AdguardTeam/CoreLibs/issues/1683)
* 化粧品のルールはmypikpak.comで動作しません [#1767](https://github.com/AdguardTeam/CoreLibs/issues/1767)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.2 ベータ 2

- 公開日: 2023-10-13T13:10:35Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2-beta-2

ダイナミックなアイコンだけでなく、ダイナミックなテーマもあります。 設定でこのオプションを有効にすると、AdGuardアプリインターフェイスはスマートフォンインターフェイスの色と一致します。 外部の変化以外にも、よりスムーズなユーザー体験のためにいくつかのバグを修正しました。

<p align="center">
<img src="">https://cdn.adtidy.org/content/github/ad_blocker/android/protectiontheme1.png"幅="300" 高さ="600"> <img src="https://cdn.adtidy.org/content/github/ad_blocker/android/protectiontheme2.png"幅="300" 高さ="600">
</p>

## 変更履歴
​​
### フィックス
 
* ファイアウォールタブ間の切り替えは、AdGuardがクラッシュする原因[#4999](https://github.com/AdguardTeam/AdguardForAndroid/issues/4999)
* 異なる言語で設定をインポートするとすぐに言語を変更しない[#4984](https://github.com/AdguardTeam/AdguardForAndroid/issues/4984)
* 設定をインポートする際にライセンスがインポートされていない[#4985](https://github.com/AdguardTeam/AdguardForAndroid/issues/4985)
* 無効な通知に関するスナックの非作業ボタン [#5002](https://github.com/AdguardTeam/AdguardForAndroid/issues/5002)
* HTTPS トラフィックの画面をフィルタリングする理由で、次いで前のアクションをキャンセル [#4993](https://github.com/AdguardTeam/AdguardForAndroid/issues/4993)
* クロスボタンは、言語固有の広告ブロック画面の検索バーにテキストを削除しません[#4978](https://github.com/AdguardTeam/AdguardForAndroid/issues/4978)
* インポート/エクスポートされた設定のテキストは、ダイアログボックス[#4981]に収まりません(https://github.com/AdguardTeam/AdguardForAndroid/issues/4981)


### CoreLibs が v1.12.80 に更新されました [#5003](https://github.com/AdguardTeam/AdguardForAndroid/issues/5003)
* マイナーな安定性の改善


---

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.2 ベータ 1

- 発行: 2023-09-29T16:16:13Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2-beta-1

## 動的アイコン [#4317](https://github.com/AdguardTeam/AdguardForAndroid/issues/4317)

Android用のAdGuardは現在、動的アイコンを持っています。 スマートフォンでテーマアイコンを使用している場合、AdGuardアプリはシステムの色と一致します。

<p align="center">
<img src="">https://cdn.adtidy.org/content/github/ad_blocker/android/dynamicicon.png" 
幅="300" 高さ="150">
</p>

## HTTP/3 フィルタリングサポート [#487](https://github.com/AdguardTeam/CoreLibs/issues/487)

AdGuard は HTTP/1.1 と HTTP/2 トラフィックのみをフィルタリングします。 このベータでは、HTTP/3フィルタリングの実験サポートを追加しました。 QUICネットワークプロトコルを搭載した HTTP/3 プロトコルは、より安定した高速なインターネット接続だけでなく、より優れたプライバシーとセキュリティを提供します。 HTTP/3フィルタリングを有効にすると、QUICプロトコルを利用し、広告やトラッカーを効果的にブロックすることができます。

HTTP/3 フィルタリングを有効にするには、設定 → 全般 → 上級 → 低レベル設定 → *Filter HTTP/3* に移動し、スイッチを右に切り替えます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/github/ad_blocker/android/HTTP3.png" 
幅="300" 高さ="600">
</p>

## 2つのHTTPS証明書のサポート

2つのHTTPS証明書を実装することで、Chromeバージョン100以上でフィルタリングするHTTPSの問題を修正しました。 システムストアの証明書はほとんどのアプリでフィルタリングを担当しますが、ユーザストアの証明書は、ChromiumベースのブラウザでHTTPSトラフィックをフィルタリングすることができます。

証明書のインストールも簡単になりました:ステップバイステップの指示を追加しました。

2番目の証明書をインストールするには、[設定] → [フィルタリング] → [ネットワーク] → [ HTTPS フィルタリング → *Security 認証*] に移動し、指示に従ってください。

<p align="center">
<img src="">https://cdn.adtidy.org/content/github/ad_blocker/android/2certificates.png" 
幅="300" 高さ="600">
</p>

## 変更履歴
​
### 特徴:
* Opera ブラウザのデフォルトで HTTPS フィルタを有効にする [#4972](https://github.com/AdguardTeam/AdguardForAndroid/issues/4972)
​
### フィックス
* デフォルトでルーティングからINETCOM.TVを除外 [#4723](https://github.com/AdguardTeam/AdguardForAndroid/issues/4723)
* AdGuard は HTTPS の証明書の有効期限による保護を開始できません。 [#4896](https://github.com/AdguardTeam/AdguardForAndroid/issues/4896)
* カスタムフィルタの自動更新は動作しません [#4961](https://github.com/AdguardTeam/AdguardForAndroid/issues/4961)
* AdGuardはアカウントからログアウト [#4959](https://github.com/AdguardTeam/AdguardForAndroid/issues/4959)
* メインスイッチの周りのシャドウはAndroid 8で欠落しています [#4858](https://github.com/AdguardTeam/AdguardForAndroid/issues/4858)
* TalkBack [#4809] では、いくつかの要素が正しく発表されていない (https://github.com/AdguardTeam/AdguardForAndroid/issues/4809)
* スイッチは10-30秒間消え、保護は長時間[#4862]のために再開します(https://github.com/AdguardTeam/AdguardForAndroid/issues/4862)
* 「YouTubeで広告をブロックする方法」画面の下部にあるスペースは、小さな画面でデバイスに欠落しています[#4866](https://github.com/AdguardTeam/AdguardForAndroid/issues/4866)
* 繁体字にアプリが設定されている場合は、更新後に簡体字中国語でフィルタが表示されます[#4949](https://github.com/AdguardTeam/AdguardForAndroid/issues/4949)  

### コアライブラリ
* CoreLibs が v1.12.76 に更新されました(#4966)(https://github.com/AdguardTeam/AdguardForAndroid/issues/4966)
* 応答状態のタイマーで接続が終了 [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180)
* ユーザーエージェントのストリッピングを改善しました [#1345] ()https://github.com/AdguardTeam/CoreLibs/issues/1345)
* uBO メディアの問い合わせに対応しました [#1707](https://github.com/AdguardTeam/CoreLibs/issues/1707)
* ipTIMEホームルータを使用する際の秒数遅延[#1756](https://github.com/AdguardTeam/CoreLibs/issues/1756)
* AdGuardはWebページの読み込み時間を遅くします [#1522](https://github.com/AdguardTeam/CoreLibs/issues/1522)
* リクエストが[#1766]をクリックしたときに「検索クエリを非表示」オプションを有効にします(https://github.com/AdguardTeam/CoreLibs/issues/1766)
* SOCKS5 プロキシは AdGuard 4.0 で動作しません [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* ECH が有効になったときに ECH グリースを有効にしました [#1781](https://github.com/AdguardTeam/CoreLibs/issues/1781)
* 本テキストの復号化時にHTTPヘッダを削除したバグを修正しました[#1750](https://github.com/AdguardTeam/CoreLibs/issues/1750)
* XPCの準備 [#1675] (https://github.com/AdguardTeam/CoreLibs/issues/1675)
* DNSフォールバックヘルパーは、プロバイダーサーバーの代わりに127.0.0.1を返す[#1687](https://github.com/AdguardTeam/CoreLibs/issues/1687)
* TCP/IP:新しい拒絶モードを追加 - ICMP管理禁止 [#1774](https://github.com/AdguardTeam/CoreLibs/issues/1774)
* TcpIpStack [#1796] で UDP のタイムアウトが少なすぎる (https://github.com/AdguardTeam/CoreLibs/issues/1796)
​
### DnsLibs(ドングリブ)
* DnsLibs が v2.2.24 に更新されました [#4953](https://github.com/AdguardTeam/AdguardForAndroid/issues/4953)
* DoH は、余りに長い [#200] の stale 接続を使用するしようとします(https://github.com/AdguardTeam/DnsLibs/issues/200)
* CoreDNS DoQ サーバは DnsLibs [#204] では使用できません。https://github.com/AdguardTeam/DnsLibs/issues/204)
* sdns:// cert pinning が間違っている [#205](https://github.com/AdguardTeam/DnsLibs/issues/205)

### フィルターメンテナーの重要事項

* $referral-policy修飾子を追加 [#135]()https://github.com/AdguardTeam/CoreLibs/issues/135)
* 基本的なルールのための$method修飾子を追加 [#1713](https://github.com/AdguardTeam/CoreLibs/issues/1713)
* 空のパターンで$stealthルールを許可 [#1762](https://github.com/AdguardTeam/CoreLibs/issues/1762)
* 追加 $to修飾子 [#1714](https://github.com/AdguardTeam/CoreLibs/issues/1714)
* $jsonprune, $replace, $hls は GET-POST HTTP メソッドで動作しません [#1743](https://github.com/AdguardTeam/CoreLibs/issues/1743)
* 例外ルールは互いに干渉する [#1749](https://github.com/AdguardTeam/CoreLibs/issues/1749)
* $path修飾子はパスmarket.yandex.ruで動作しません [#1726](https://github.com/AdguardTeam/CoreLibs/issues/1726)
* $jsonprune修飾子は、jsonp [#1734] の引用符を扱うことができるはずです(https://github.com/AdguardTeam/CoreLibs/issues/1734)
* :has(), :not(), and :is() は、#?# ルールマーカー [#1683]() で、ExendCss の使用が強制されていない場合、標準の擬似クラスとして考慮してください。https://github.com/AdguardTeam/CoreLibs/issues/1683)
* 化粧品のルールはmypikpak.comで動作しません [#1767](https://github.com/AdguardTeam/CoreLibs/issues/1767)

---

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.1

- 公表: 2023-07-26T17:14:51Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.1

今回のリリースでは、アプリのUIや内部の作業に多くの改善を行いました。 たとえば、ライブストリームとショートを含むすべてのビデオフォーマットをサポートするためにYouTubeプレーヤーを再構築しました。 実は、YouTubeを開いた内部のWebブラウザに基づいており、内蔵のアドブロック機能があります。 この機能の詳細な説明については、保護セクションをご覧ください。 ※アプリ管理*にアクセスしやすくなりました。 一番下にあるタブバーメニューに追加されたボタンを経由してタップするだけでなりました。

## 変更履歴

### 特徴:
* 追加`com.homeretailgroup.myargoscard`除外するドメイン [#3480](https://github.com/AdguardTeam/AdguardForAndroid/issues/3480)
* com.quark.browserとcom.qihoo.contentsのサポートを追加しました [#3673](https://github.com/AdguardTeam/AdguardForAndroid/issues/3673)
* アプリ管理の簡単なアクセス [#4408](https://github.com/AdguardTeam/AdguardForAndroid/issues/4408)

### フィックス
* AdGuard プレーヤーは、ブラウザの [#3932] で [共有] ボタンをタップしたときに YouTube ビデオを再生しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3932)
* バグ報告と機能リクエスト画面の動作を改善し、重複を防ぐことができます。 [#4814](https://github.com/AdguardTeam/AdguardForAndroid/issues/4814)
* *一般設定のデフォルト*へのリセットは正しく動作しません [#4719](https://github.com/AdguardTeam/AdguardForAndroid/issues/4719)
* 追加`com.apple.movetoios`除外する [#3676](https://github.com/AdguardTeam/AdguardForAndroid/issues/3676)
* 頻繁にAndroid用のAdGuard v4.0は保護を再開します [#4707](https://github.com/AdguardTeam/AdguardForAndroid/issues/4707)
* バグ報告を提出した後に戻ろうとすると、無限のローダーが表示される[#4792](https://github.com/AdguardTeam/AdguardForAndroid/issues/4792)
* フィルターの更新後、更新されたフィルターは列[#4790]で表示されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4790)
* Chromeリモートデスクトップは、アプリのフィルタリングが[#4036]をオフにされていない限り動作しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4036)
* 追加`pl.tvn.player`除外をフィルタリングするには [#3646](https://github.com/AdguardTeam/AdguardForAndroid/issues/3646)
* ブロックされたキー[#4562]を入力すると、使用ライセンスキータブからの誤った遷移()https://github.com/AdguardTeam/AdguardForAndroid/issues/4562)
* スナックを経由して別のタブに切り替える作業はしない [#4502](https://github.com/AdguardTeam/AdguardForAndroid/issues/4502)
* 小さな表示では、ボタンはUserscript画面[#4750]のテキストをオーバーラップします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4750)
* com.rapido.passengerアプリは動作していません [#3976](https://github.com/AdguardTeam/AdguardForAndroid/issues/3976)
* アップデートの確認時、Browsing Security Databaseはアップデートがインストールされていない場合は「最新の状態まで」を「#4725」に報告する必要があります。https://github.com/AdguardTeam/AdguardForAndroid/issues/4725)
* 追加`com.inpost.fresh`除外をフィルタリングするには [#3979](https://github.com/AdguardTeam/AdguardForAndroid/issues/3979)

### デザイン
* テクニカル情報ダイアログ [#4717] の改善https://github.com/AdguardTeam/AdguardForAndroid/issues/4717)
* アプリの言語画面を改善しました [#4718](https://github.com/AdguardTeam/AdguardForAndroid/issues/4718)

### バージョン
* アップグレードされたCoreLibsにv1.11.113
* DnsLibs を v2.2.14 にアップグレード

#### DnsLibs(ドングリブ)

* 追加`lb._dns-sd._udp.*.in-addr.arpa`除外のデフォルトリストへ [#194](https://github.com/AdguardTeam/DnsLibs/issues/194)
* `$denyallow`追加の修飾子が追加されるまでルールが検証されていない[#191](https://github.com/AdguardTeam/DnsLibs/issues/191)
* フォールバックアップストリームが無効なプレーンDNS上流で有効化されていない[#4820](https://github.com/AdguardTeam/AdguardForAndroid/issues/4820)
* IP ベースの DoT/DoQ 接続の場合、IP アドレスは SNI [#186] に設定されます。https://github.com/AdguardTeam/DnsLibs/issues/186)
* 複数の上流を追加したときに全体的なタイムアウトが大きい [#105](https://github.com/AdguardTeam/DnsLibs/issues/105)
* XPC サポートを追加 [#174](https://github.com/AdguardTeam/DnsLibs/issues/174)
* 追加された`dnsproxy_settings::request_timeout setting`上流固有のものの代わりに [#163](https://github.com/AdguardTeam/DnsLibs/issues/163)
* DNS-over-QUIC 上流はrequid ip [#185] を尊重しません(https://github.com/AdguardTeam/DnsLibs/issues/185)
* トラフィックは、DNS 127.0.0.1からアウトバウンドプロキシサーバーにルーティングされます[#195](https://github.com/AdguardTeam/DnsLibs/issues/195)
* SPKI指紋認証機能を追加(#172)(https://github.com/AdguardTeam/DnsLibs/issues/172)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.1 ベータ 1

- 公表: 2023-07-21T18:37:51Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.1-beta-1

今回のリリースでは、アプリのUIや内部の作業に多くの改善を行いました。 たとえば、ライブストリーム、定期的なビデオ、ショートを含むすべてのビデオフォーマットをサポートするYouTubeプレーヤーを再設計しました。 この機能の詳細な説明については、保護セクションを参照してください。 また、Apps Managementにアクセスしやすくなりました。 一番下にあるタブバーメニューに追加したボタンでワンクリックでクリックします。

## 変更履歴

### 特徴:
* com.homeretailgroup.myargoscard と関連するドメインを除外に追加 [#3480](https://github.com/AdguardTeam/AdguardForAndroid/issues/3480 )
* com.quark.browserとcom.qihoo.contentsのサポートを追加しました [#3673](https://github.com/AdguardTeam/AdguardForAndroid/issues/3673)
* 使いやすいアプリ管理 [#4408](https://github.com/AdguardTeam/AdguardForAndroid/issues/4408)

### フィックス
* バグ報告と機能リクエスト画面の動作を改善し、重複を防ぐことができます。 [#4814](https://github.com/AdguardTeam/AdguardForAndroid/issues/4814)
* 一般設定の「デフォルト設定」は[#4719]()が動作しないhttps://github.com/AdguardTeam/AdguardForAndroid/issues/4719)
* com.apple.movetoios を除外に追加 [#3676](https://github.com/AdguardTeam/AdguardForAndroid/issues/3676)
* AdGuard 4 夜に頻繁に保護を再開 [#4707](https://github.com/AdguardTeam/AdguardForAndroid/issues/4707)
* バグ報告を提出した後に戻ろうとすると、無限のローダーが表示される[#4792](https://github.com/AdguardTeam/AdguardForAndroid/issues/4792)
* フィルターの更新後、更新されたフィルターは列[#4790]で表示されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4790)
* Chromeリモートデスクトップは、アプリのフィルタリングが[#4036]をオフにされていない限り動作しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4036)
* フィルタリング除外にpl.tvn.playerを追加 [#3646](https://github.com/AdguardTeam/AdguardForAndroid/issues/3646)
* ブロックされたキー[#4562]を入力すると、使用ライセンスキータブからの誤った遷移()https://github.com/AdguardTeam/AdguardForAndroid/issues/4562)
* スナックを経由して別のタブに切り替える作業はしない [#4502](https://github.com/AdguardTeam/AdguardForAndroid/issues/4502)
* 小さな表示では、ボタンはUserscript画面[#4750]のテキストをオーバーラップします(https://github.com/AdguardTeam/AdguardForAndroid/issues/4750)
* com.rapido.passengerアプリは動作していません [#3976](https://github.com/AdguardTeam/AdguardForAndroid/issues/3976)
* アップデートの確認時、Browsing Security Databaseはアップデートがインストールされていない場合は「最新の状態まで」を「#4725」に報告する必要があります。https://github.com/AdguardTeam/AdguardForAndroid/issues/4725)

* フィルタリング除外にcom.inpost.freshを追加しました [#3979](https://github.com/AdguardTeam/AdguardForAndroid/issues/3979)

### デザイン
* テクニカル情報ダイアログ [#4717] の改善https://github.com/AdguardTeam/AdguardForAndroid/issues/4717)
* アプリの言語画面を改善しました [#4718](https://github.com/AdguardTeam/AdguardForAndroid/issues/4718)

### バージョン
* アップグレードされたCoreLibsにv1.11.113
* DnsLibs を v2.2.14 にアップグレード

#### DnsLibs(ドングリブ)

* 除外のデフォルトリストに「lb. dns-sd. udp.*.in-addr.arpa」を追加しました[#194](https://github.com/AdguardTeam/DnsLibs/issues/194)
* 追加修飾子が追加されるまで$denyallowルールは検証されません[#191](https://github.com/AdguardTeam/DnsLibs/issues/191)
* 無効なプレーンDNS上流でフォールバックアップストリームが有効でない[#4820](https://github.com/AdguardTeam/AdguardForAndroid/issues/4820)
* IP ベースの DoT/DoQ 接続の場合、IP アドレスは SNI [#186] に設定されます。https://github.com/AdguardTeam/DnsLibs/issues/186)
* 複数の上流を追加したときに全体的なタイムアウトが大きい [#105](https://github.com/AdguardTeam/DnsLibs/issues/105)
* XPC サポートを追加 [#174](https://github.com/AdguardTeam/DnsLibs/issues/174)
* dnsproxy settings::request timeout の設定を上流の特定のものの代わりに追加しました [#163](https://github.com/AdguardTeam/DnsLibs/issues/163)
* Dns-over-QUIC 上流は、requid ip [#185] を尊重しません(https://github.com/AdguardTeam/DnsLibs/issues/185)
* トラフィックは、DNS 127.0.0.1からアウトバウンドプロキシサーバーにルーティングされます[#195](https://github.com/AdguardTeam/DnsLibs/issues/195)
* SPKI指紋認証機能を追加(#172)(https://github.com/AdguardTeam/DnsLibs/issues/172)

---

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.0

- 公開日: 2023-06-13T18:10:45Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0

## アンドロイド用のAdGuard v4.0で注目すべきチャンネル

最後に、ティタニックの努力の結果を明らかにする準備ができています! Android 用の AdGuard v4.0 を詳しく見て、バージョン 3.6 以降に何が変更されたかについて話しましょう。

### トータルリエンジニアリング

私たちは、アプリ全体をオーバーホールしました, 地面からコードのすべての行を慎重に書き換えます. この変換式刷新は、これまで以上に早くてもスムーズなアプリで起用しました。

### 完全な再設計

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/ca756813-86ae-428b-8302-12a37266900a"幅="300" 高さ="600">
</p>


アプリインターフェイスをシンプルにし、コア機能をフロントに持ち込むために設計を再開しました。 今度は、広告ブロック、追跡保護、Annoyanceブロック、またはDNS保護をフィルタとともにオンにするには、メインスイッチの上の対応するアイコンをタップするだけでOKです。

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/831280e2-06fc-4beb-b9f5-bb6ff087097a"幅="300" 高さ="600">
</p>



また、別々の *Protection* セクションを追加しました。 画面の下部にあるシールドアイコンをタップすることでアクセス可能で、このセクションではさらに多くの制御が可能になります。 上記の「コア」機能とは別に、このセクションでは、*Firewall*、*Browsing Security*、さらにはAdGuard VPNを管理することができます。 保護画面から、これらのモジュールをオンまたはオフにすることができます。

### 防火壁

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/55680f16-6c0f-4e0b-9c74-becd45d0966c"幅="300" 高さ="600">
</p>



私たちは、Android用のAdGuardの深さからエキサイティングな機能を発見しました - *ファイアウォール* - それは本格的な独立したステータスを与えました。 ドメインのマスターで、画面が消えるときにアプリがモバイルデータやWi-Fiに侵入できるかを決定します。 アプリアクティビティのリアルタイム通知で把握できるように設計されているため、注意をエスケープしません。

これらの超高速修正のために、ファイアウォールルールを更新する*クイックアクション*セクションに向かいます。 *Firewall*では、ローミング時にインターネットにアクセスし、貴重なメガバイトを海外に保存するアプリをブロックすることもできます。

### 詳細な統計情報

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/8cc898c9-685b-4afe-b63c-858e56c0d910"幅="300" 高さ="1350">
</p>




専用のタブは、すべてのアプリ、企業、ドメインに関する包括的な統計情報を提供します。 会社の要求が最も頻繁にブロックされるのはなぜですか? どのアプリがデータを送信しようとしているのか? 疑わしいものを素早く識別し、ブロックすることができます。

### AdGuard VPN との統合

上記のように、AdGuard VPN との統合モードは、Android 用の AdGuard v3.5 で導入されました。 それまで、ユーザーは、広告ブロッカーとVPNを同時に動作させるために、7つの地獄の円を通過しなければなりませんでした。 通常の2つの異なるネットワークフィルタリングアプリは、Android上で互いに動作することができないため、すべて。

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/e71cca1e-f1a6-4a06-87cb-0bebde89f1ab"幅="300" 高さ="600">
</p>



Android用のAdGuard v4.0のリリースでは、統合モードはこれまで以上に安定しています。 以前は、AdGuardまたはAdGuard VPNが更新または再インストールされたたびに、統合モードが再構成されなければなりませんでした。 これで、一度設定すると、統合を維持しながら更新と再インストールに耐えられます。 さらに、AdGuard Ad BlockerとAdGuard VPN間でより頻繁に情報交換が、パフォーマンスに影響を与えずに統合モードの安定性を高めます。

> 統合モードの変更は、Android および AdGuard VPN v2.3 の AdGuard v4.0 と Android 間で同期されます。 両方のアプリを最新バージョンに更新して、統合モードで最も安定したスムーズな同時操作を楽しむようにしてください。

### 選択型アプリプロキシ

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/5dd58f40-a43b-4814-b62b-6e7169631e31"幅="300" 高さ="600">
</p>




Android 用の AdGuard v4.0 以前は、指定されたプロキシサーバーを介してすべての Web トラフィックをルーティングできます。 *Settings → [フィルタリング] → [ネットワーク] → [プロキシ] にあるプロキシ*機能を使用して動作する *Appsを使用すると、プロキシを通じてどのアプリが動作するかを選択できます。 また、*プロキシ*で動作するアプリは、統合モードで動作する場合、AdGuard VPNを介してトラフィックをルートするアプリを指定することができます。

### ルートアクセス特典

そこにあるすべての技術愛好家にとって、「root」という用語は、あなたに見知らぬ人ではありません。 ルーティングは、デバイスがより特権的なコントロールを獲得するために不可欠です。 あなたのAndroidデバイスが根ざしている場合は、Android用のAdGuard v4.0は、以前のバージョンのAdGuard Ad Blockerを超えて、非推奨の機能を提供します。

伝統的に、AdGuard は、ローカル VPN を確立することで、コアリブのフィルタリングエンジンにネットワークトラフィックをルーティングします。 しかし、今ではrootアクセスで、AdGuardを*Automaticプロキシ*モードに切り替えることができます。 *Settings → フィルタリング → ネットワーク → ルーティング モード* に移動し、*Automatic プロキシ* に切り替えます。 このアクションは、ローカルVPNを画像から取り出し、代わりに、同じ目標を達成するためのiptablesを設定します。 この変更にはいくつかの利点があります。

まず、AdGuard は IPv6 リクエストに DNS フィルタリングを適用できるようになりました。以前は不可能なものでした。 次に、AdGuardが各アプリでWebリクエストを正確に関連付けるという問題がいくつかありました。 この微調整は、ファイアウォール、フィルタリングログなどの性能を強化します。 根ざしたデバイスをお持ちのお客様には、このAdGuardアップデートでは、制御とカスタマイズをまったく新しいレベルに引き上げます!

### 低レベルの設定作業

低レベルの設定の領域に潜入しますか? [設定] → [全般] → [詳細] で、これらのオプションは、技術に精通したユーザーを念頭に置いて設計されています。 パワフルな遊び場ですが、気にしないと物事を混乱させるのもとても簡単です。 私たちが配置したすべての警告にもかかわらず、それは人間の性質を探求し、実験することです。多くの場合、その結果を完全に理解することなく。

<p align="center">
<img src="">https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/723ce5f2-a8f5-474b-962d-67b82d552045"幅="300" 高さ="600">
</p>



これにより、ユーザーフレンドリーで直感的な低レベル設定を実現しました。 各設定が何であるかを理解しやすくなりましたが、間違いを犯す場合でも、入力した値の検証チェックなどのセキュリティ対策を実施して、大きな間違いから保護します。

設定自体は、新しいものを追加し、古いものを退職し、この高度なツールセットを改良し続けてきました。 知識ベースでは、低レベルの設定に関する総合ガイドがご利用いただけます。https://adguard.com/kb/adguard-for-android/solving-problems/low-level-settings/)。 そのため、AdGuardの高度な設定でカスタマイズの深さに強化された、まだより安全な深層ダイビングの準備ができました!

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.0 RC 1

- 公開日: 2023-06-01T16:30:03Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-rc-1

Android向けAdGuard v4.0の最初のリリース候補をプレゼント! 今回のアップデートでは、パフォーマンスとユーザーエクスペリエンスを向上させるために、いくつかの問題に対処しました。

## 変更履歴
### フィックス
* 「すべての企業を表示」をタップしたときに統計記録に関連する企業のリストを表示します。 [#4716](https://github.com/AdguardTeam/AdguardForAndroid/issues/4716)
* インテグレーションモードでは、プロキシが有効になっていると、通知は偽りプロキシサーバーの使用を報告します[#4739](https://github.com/AdguardTeam/AdguardForAndroid/issues/4739)
* Apps/Companies [#4730] の注文をソートする誤った動作 (https://github.com/AdguardTeam/AdguardForAndroid/issues/4730)
* サードパーティのVPNを有効にした後、AdGuardの誤った動作 [#4687](https://github.com/AdguardTeam/AdguardForAndroid/issues/4687)
* HTTPS フィルタリングされたアプリでアプリのスイッチの誤った動作 [#4729](https://github.com/AdguardTeam/AdguardForAndroid/issues/4729)
* 画面回転後の通知言語変更 [#4661](https://github.com/AdguardTeam/AdguardForAndroid/issues/4661)
* 最近の活動は、アプリを終了した後にクリアされます [#4705](https://github.com/AdguardTeam/AdguardForAndroid/issues/4705)
* 「DNSサーバーを追加」ダイアログから並列解決 [#4713](https://github.com/AdguardTeam/AdguardForAndroid/issues/4713)
* 場合によっては「ユーザールール」画面の「スナック」や「いいね」などが表示されます。[#4712](https://github.com/AdguardTeam/AdguardForAndroid/issues/4712)
* 「プロキシで動作するアプリ」のスナックブリンク [#4728](https://github.com/AdguardTeam/AdguardForAndroid/issues/4728)
* 一部の翻訳はフィールドに収まらない [#4623](https://github.com/AdguardTeam/AdguardForAndroid/issues/4623)
* 「What's new」ポップアップ[#4727]にテクニカルバージョンが表示されます。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4727)
* 最後のアイテムは、コンパクトなデバイスのプロキシ設定に合わない[#4738](https://github.com/AdguardTeam/AdguardForAndroid/issues/4738)
* AdGuardアカウントの一覧からデバイスを削除した後、ライセンスはリセットされません[#4710](https://github.com/AdguardTeam/AdguardForAndroid/issues/4710)
* 統計期間を変更するときにリクエストバーがバウンス [#4720](https://github.com/AdguardTeam/AdguardForAndroid/issues/4720)
* アプリが再起動するまでの更新チャネルは変更されません。 [#4741](https://github.com/AdguardTeam/AdguardForAndroid/issues/4741)
* プロキシを介して動作するHTTPSフィルタ付きアプリやアプリで Truncatedリスト [#4688]()https://github.com/AdguardTeam/AdguardForAndroid/issues/4688)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.0 ベータ 2

- 公表: 2023-05-25T14:23:44Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-beta-2

今、クリーンアップフェーズではあります。そのため、Android用のAdGuard v4.0の2番目のベータのchangelogはほぼ完全にバグ修正です。 このバージョンに問題がある場合は、ヘルプが必要な場合は、[Androidリポジトリ]のバグを報告してください。https://github.com/AdguardTeam/AdGuardforAndroid/issues) または既存のバグ修正の投票。

改善を忘れずに:CoreLibsとDnsLibsを更新し、いくつかの機能を追加し、統計画面で機能しました。

## 変更履歴

### 特徴:

* 最近の活動画面に高速スクロール機能を追加 [#4617](https://github.com/AdguardTeam/AdguardForAndroid/issues/4617)
* Brought バック`pref.proxy.disable.reconfigure` [#4636](https://github.com/AdguardTeam/AdguardForAndroid/issues/4636)
* 統計通知の文言変更 [#4630](https://github.com/AdguardTeam/AdguardForAndroid/issues/4630)
* AdGuard と AdGuard VPN が *Integrated mode* で実行されると、AdGuard VPN の *Exclusions* タブの *Apps* セクションをタップすると、AdGuard [#281] でプロキシ*画面で動作する *Apps が開きます。https://github.com/AdguardTeam/AdGuardVPNForAndroid/issues/281)
* メイン画面の統計番号をタップすると、*Statistics*画面[#4684]になります(https://github.com/AdguardTeam/AdguardForAndroid/issues/4684)
* AdGuardがフォアグラウンドに戻ると、メイン画面と統計画面の統計番号が更新されます[#4633](https://github.com/AdguardTeam/AdguardForAndroid/issues/4633)

### フィックス

* *「ブロックルールの追加」ダイアログ[#4685](https://github.com/AdguardTeam/AdguardForAndroid/issues/4685)
* *Buyライセンス* をクリックすると、*トライアルライセンス* ポップアップ [#4607] が既に使用済みです。https://github.com/AdguardTeam/AdguardForAndroid/issues/4607)
* フィルター詳細画面[#4647]の代わりにライセンスプロモーションが表示されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4647)
* Adguard Extra はデフォルト [#4602] にリセットした後は動作しません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4602)
* В строке уведомлений всегда указано, что *Прокси работает*, независимо от состояния прокси [#4545](https://github.com/AdguardTeam/AdguardForAndroid/issues/4545)
* 統計タブのテキストを点滅 [#4714](https://github.com/AdguardTeam/AdguardForAndroid/issues/4714)
* *Clear統計*ボタンをタップすると、*Recentアクティビティ*セクション[#4715]からデータを削除しません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4715)
* *Tracking Protection* を無効にすると、対応するフィルタリスト [#4599] を無効にしません(https://github.com/AdguardTeam/AdguardForAndroid/issues/4599)
* 電子メールの自動記入項目はパスワード マネージャーと働かなかった[#4627] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4627)
* デバイスストレージに証明書をエクスポートできなかった[#4609](https://github.com/AdguardTeam/AdguardForAndroid/issues/4609)
* ダウンロードバーの緑色部分は左[#4625]に若干シフトされます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4625)
* プレミアムアカウントのログインとアウトが保護を再起動しない[#4605](https://github.com/AdguardTeam/AdguardForAndroid/issues/4605)
* 保護が有効になっている通知は[#4612]を解除することができます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4612)
* プロキシ・スイッチをリストのプロキシ・サーバーなしで有効化した後の保護は再開します[#4681] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4681)
* 保護状態とグリッチの位置のアイコン [#4628](https://github.com/AdguardTeam/AdguardForAndroid/issues/4628)
* プロキシのホスト名文字列は正しいドメイン名を検証できません [#4603](https://github.com/AdguardTeam/AdguardForAndroid/issues/4603)
* プロキシサーバーのリストはスクロールできません [#4654](https://github.com/AdguardTeam/AdguardForAndroid/issues/4654)
* AdGuard が *Integration モード* [#4635]( ) で動作する場合、プロキシ設定は無効化されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4635)
* サムスンペイの互換性通知は韓国のユーザーにのみ表示されます [#4629](https://github.com/AdguardTeam/AdguardForAndroid/issues/4629)
* スクロール位置は、*Recent アクティビティ* ログがキーワード [#4699] によってフィルタリングされる場合、いくつかのケースでは保存されません。https://github.com/AdguardTeam/AdguardForAndroid/issues/4699)
* 検索フィールドは、デフォルトでAndroid 8 [#4618](https://github.com/AdguardTeam/AdguardForAndroid/issues/4618)
* 「プロキシを介して動作するアプリ」画面のスナックグリッチ[#4702](https://github.com/AdguardTeam/AdguardForAndroid/issues/4702)
* *追跡保護*の軽食は消えません[#4665] (https://github.com/AdguardTeam/AdguardForAndroid/issues/4665)
* スタートアップでAdGuardがクラッシュ [#4649](https://github.com/AdguardTeam/AdguardForAndroid/issues/4649)
* 統計は、GBからTBに変換できない [#4638](https://github.com/AdguardTeam/AdguardForAndroid/issues/4638)
* 会社の統計画面は、最後の24時間でその会社に統計が登録されていない場合は空白です[#4642](https://github.com/AdguardTeam/AdguardForAndroid/issues/4642)
* 小さな画面では、*Statistics* タブ [#4664] に重なるテキスト (https://github.com/AdguardTeam/AdguardForAndroid/issues/4664)
* 概要は、プロキシ*画面[#4696]を介して動作する*アプリで欠落しています(https://github.com/AdguardTeam/AdguardForAndroid/issues/4696)
* 画面上のスイッチは、統計をロードした後の位置を変更します [#4678](https://github.com/AdguardTeam/AdguardForAndroid/issues/4678)
* *Recent活動ログ*のツールチップは、間違った瞬間に表示されます[#4701](https://github.com/AdguardTeam/AdguardForAndroid/issues/4701)
* *Integrated mode* [#4682] のプロキシ画面で動作する *Apps のトランジティブ通知https://github.com/AdguardTeam/AdguardForAndroid/issues/4682)
* 更新ボタンはツールチップの後ろに隠されています [#4589](https://github.com/AdguardTeam/AdguardForAndroid/issues/4589)
* バージョン番号は、バージョン名[#4690]の代わりに*Updates画面*に表示されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/4690)
* 最近の活動画面を終了し、戻ってくると、スクロール位置が保持されます[#4644](https://github.com/AdguardTeam/AdguardForAndroid/issues/4644)
* *Recent アクティビティ* 画面のカスタム検索バーに入力されたテキストは、セクションを終了し、[#4643] を返すときに削除した後に残します(https://github.com/AdguardTeam/AdguardForAndroid/issues/4643)
* ホームタブのタブ間でスワイプすると、コントロールパネルのアイコン [#4592](https://github.com/AdguardTeam/AdguardForAndroid/issues/4592)
* 統計画面のダウン矢印の間違った配列[#4700](https://github.com/AdguardTeam/AdguardForAndroid/issues/4700)
* *Tracking Protection* レベル [#4632] のアンダーリング設定が間違っています。https://github.com/AdguardTeam/AdguardForAndroid/issues/4632)
* *アプリ言語*は、中国語でシステム言語[#4666]としてデバイスが消えます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4666)

### バージョン

* CoreLibsをv1.11.106に更新
* DnsLibsを2.1.41に更新 [#4675](https://github.com/AdguardTeam/AdguardForAndroid/issues/4675)


#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.0 ベータ 1

- 公表: 2023-04-24T15:04:42Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-beta-1

「アドガードv4.0の第1夜」について話した時を忘れないでください()https://adguard.com/blog/adguard-v4-0-for-android-nightly.html) ? 長い休憩の後の最初のバージョンでした - 再作業設計とテキスト、書き換えコード、および新機能。

開発、QA、デザイン、コンテンツチームのおかげで、最初のベータ版をリリースしています。

初めてのNightlyバージョンのリリース以来、100以上のバグを修正しました! しかし、これ以上残らないとは言えません(既知の問題は[GitHub]にまとめられています)https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)。 万が一遭遇した場合は、必ずお知らせください。 バグの報告方法の手順は以下の通りです。
## 最初の夜間更新

夜に投稿を読んでいないなら、【見てみる】(https://adguard.com/blog/adguard-v4-0-for-android-nightly.html)。 v3.6、v4.0以前の最後のAdGuardバージョンと比較して、変更について多く書いています。 テックに精通していない人や、詳細を理解している人や、低レベルの設定でも掘り下げることを喜んでいる人にとっては便利です。

改善の簡単な概要は次のとおりです。

  * **完全な再設計**。 より軽やかでミニマリストなデザインを作り、理解しやすく、別の画面に最も重要な機能を置くことで、アクセスがはるかに簡単になります。
<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/protection_en.jpg?0"幅="300" 高さ="600">
</p>

  * **ファイアウォール**。 今、あなたはすべてのあなたのアプリのためのインターネットへのアクセスを制御することができます - あなたが望むなら、あなたの知識なしでインターネットを使用してそれらを防ぐことができます。

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/firewall_en.jpg"幅="300" 高さ="600">
</p>


  * **統計**。 アプリ、企業、ドメインの詳細な統計情報を表示できるようになりました。 完全な透明性!

<p align="center">
<img src="">https://cdn.adtidy.org/content/release_notes/ad_blocker/android/statistics_en.jpg?0"幅="300" 高さ="600">
</p>


  * **AdGuard VPNとの統合**。 統合モードの安定性を大幅に向上させました。
  * **選択型アプリプロキシ**。 AdGuard VPNからアプリをプロキシから除外できるようになりました。
  * **ルートアクセス特典**。 ルートされたデバイスでは、他のものの間で、DNS フィルタリングを IPv6 リクエストに適用できるようになりました。 *Automatic プロキシ* モードによります。
  * **より簡単な低レベル設定**。 設計を更新し、明確な説明と入力検証を追加しました。そのため、すべてが動作していることを確認することができます。

## 最初の夜から何が変わったのか
### 複数の言語に対応

このアプリは15以上の言語に対応しています。 しかし、我々は改善されるべき多くがあることを知っている。 一部の翻訳が欠落しているか、アプリが言語に翻訳されていない場合は、Crowdinへの貢献に感謝します。 AdGuard製品を「ナレッジベース」に翻訳する方法について詳しく読む(https://adguard.com/kb/miscellaneous/contribute/translate/program/).
### 防火壁ローミングサポート

この機能は既に最初のNightlyバージョンではありましたが、実際には動作していませんでした。 しかし、ローミング時に特定のアプリでインターネットへのアクセスをブロックすることができます。 メガバイト、特に海外に旅行するときに価値のある、無駄にしないでください。
### ユーザールール、ブロックリスト、およびウィットリストのインポートとエクスポート

最初のナイトリーでは、設定を全体としてインポートすることができます。 ユーザールールを別々にインポートできるようになりました。 ルールを誰かと共有したり、他のAdGuardアプリに転送したりしたい場合に便利です。

## ベータ版をダウンロードする方法

[beta page]にアクセスしてください(https://adguard.com/beta.html?platform=android)、ベータ版のAPKファイルをダウンロードしてインストールします。 お問い合わせ 探す準備が整いました。

![ベータ版を取得する方法](https://cdn.adtidy.org/content/release_notes/ad_blocker/android/beta_en.png)

または、アプリでベータチャネルを右に配置することもできます。 ナイトリーチャンネルを使用する場合は、*Settings* → *General* → *App と filer update* に移動し、ベータに切り替えます。

リリースチャネルを使用している場合は、設定* → *一般* → *Updates* → *Update channel* を開き、*Beta* を選択します。

> リリースチャネルに戻すには、アプリを再インストールする必要があります。

## バグ報告と機能リクエストの投票

先ほど話してきたので、こちらは簡単なリマインダーです。

1. [Androidリポジトリ]をチェックします(https://github.com/AdguardTeam/AdGuardforAndroid/issues) 問題がまだ報告されていないことを確認してください。
2. 問題が新しくなった場合は、[新しい問題を作成するためのページ]を開きます。(https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose) を選択し、*Bug Report* を選択します。
3. [問題の記述](https://adguard.com/kb/guides/report-bugs/#how-to-describe-a-problem)。 可能であれば、スクリーンショットや画面録画を添付してください。

新機能やバグ修正の実装をサポートしたい場合は、GitHubで投票できます。 投票するには、いくつかの絵文字で反応するだけです。

> 統合モードでAdGuard VPNとAd Blockerを使用する場合は、[AdGuard VPNのベータ版]をダウンロードしてください。https://adguard-vpn.net/beta.html?platform=android&release=beta).

## 結論として

リリースの一歩を踏み出せば、楽しみたいと思っています。 私たちは、あなたの助けを借りて、バグが修正され、アプリがより良くなるため、ベータテスターと翻訳者に感謝したいと思います。

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 4.0 夜 39

- 発行: 2023-01-30T16:59:40Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-nightly-39

AdGuardのモバイルアプリを長時間使用しても話せませんが、現在、今後数えきれないアプリを準備中です。

誰もがその特典を楽しむことができるように、Androidアプリが改善されました。 技術的な背景がなく、データを完全に制御したい人のための機能が満載されている人のために使うのははるかに簡単です。

また、アプリを完全に書き換えて、より早くスムーズな方法を実行します。

> 免責事項: これはナイトリーバージョンです。そのため、アプリは通常のバグよりも多く含まれています(ここでは、既知の問題のリスト)(https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)。 バグを報告する準備が整っていない場合、リスクをとらず、リリースを待ってください。アプリをより安定させるために積極的に取り組んでいます。

## みんなに便利なアップデート

### 完全な再設計

<p align="center">
<img src="">https://cdn.adtidy.org/blog/new/iqfm6main.jpg"幅="300" 高さ="650">
</p>

もともと、Android用のAdGuardにはたくさんの機能があります。広告、トラッカー、その他の脅威をブロックするための汎用ツールとして機能します。 再設計中は「コア」機能へのアクセスを簡素化しようとしました。これにより、すべての機能が単一のタップで利用できます。 今度は、広告ブロック、追跡保護、Annoyanceブロック、またはDNS保護をフィルタとともにオンにするには、メインスイッチの上の対応するアイコンをタップするだけでOKです。

<p align="center">
<img src="">https://cdn.adtidy.org/blog/new/la0mnprotection.jpg"幅="300" 高さ="650">
</p>

*Protection*セクションも追加しました。 画面の下部にあるシールドアイコンをタップすることで見つけることができます。 上記の「コア」機能とは別に、このセクションでは、ファイアウォール、ブラウジングセキュリティ、さらにはアドガードVPNを管理することができます。 保護画面では、これらのモジュールをオンまたはオフにしたり、設定を簡単にアクセスすることができます。

### 詳細な統計情報

<p align="center">
<img src="">https://cdn.adtidy.org/blog/new/qv07vstatistics.jpg"幅="300" 高さ="1200">
</p>

最近、アプリが自分のデータでやりたいことや、その場で漏れるのはニュースではありません。 ユーザーが自分のデータを完全に制御したいという非常に論理的です。 AdGuardでは、すでに対応可能です。さらに、より透明性のある機能を導入しています! どのアプリや企業がデータを漏洩する可能性はありますか?
統計データでは、どのアプリがグローバル企業にデータを送信するかを追跡できるようになりました。また、一部のリクエストをブロックまたはブロックすることができます。

### 防火壁

<p align="center">
<img src="">https://cdn.adtidy.org/blog/new/40jm3firewall.jpg"幅="300" 高さ="650">
</p>

以前のファイアウォールと同様の機能を持つために使用されるAndroidアプリは、アプリ内の深く隠されていました。アプリ管理セクション。 今、それは完全にスタンドアローン機能になり、明確に定義された行動範囲。

ファイアウォールを使用すると、アプリのインターネットへのアクセスを制御することができます。モバイルデータやWi-Fiを画面オフで使用できるアプリを決定し、アプリアクティビティのリアルタイム通知を取得し、クイックアクションセクションでファイアウォールルールを更新します。

> ナイトリーバージョンは、新しい機能でブリムに埋め込まれています。 興味をそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそも「ブログ記事」を読んでくださいね(笑)https://adguard.com/en/blog/adguard-v4-0-for-android-nightly.html)—私達は高度の特徴を細部にカバーし、未来のための私達の計画を共有します。

## 自分でテストする

フィードバックが必要です! [ダウンロード]https://agrd.io/android_nightly) Android および (AdGuard VPN を使用している場合) の AdGuard v4.0 の夜間バージョンの [Nightly バージョンの AdGuard VPN](https://adguard-vpn.com/en/beta.html?platform=android&release=nightly)、報告問題、機能リクエストの送信 お問い合わせ

### 問題を報告する方法

バグに気付いた場合、【GitHub 課題】の作成でお伝えください。https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose)。 見つけたものを記述し、 devteam@adguard.com でログを共有します。これは問題に対処するために簡単にします。

ログを収集するには、*Settings* → *General* → *Advanced* をタップし、*Export ログとシステム情報*を選択します。

> 既に取り組んでいるものがありますが、報告する必要はありません。 ※「既知の問題のリスト」を参照してください。(https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)** バグ報告をお送りする予定

### 機能リクエストの投票

![GitHubの反応](https://cdn.adtidy.org/blog/new/go9q3github_reaction.png)

[GitHub] でhttps://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Feature+request%22+sort%3Areactions-%2B1-desc)、機能要求の反作用を残すことができます。 ほとんどの人が興味をそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそもそも 反応を離れるには、好きな機能のリクエストを選択し、 emoji を使用して実装をサポートしてください。

## 結論として

私たちは、この一晩バージョンにあまり注意を払っていません。 彼らは通常、小さな数のダイハード愛好家にのみ興味があります。 しかし、この時間は異なります。 このバージョンは、すぐに多くの人のためにAndroid用のAdGuard広告ブロッカーに来る巨大な変更をヘルドし、我々はそれを右にしたいです。

あなたの助けを借りて, コミュニティの助け, 私たちは、すべての単一のバグを追跡し、ちょうど右のすべてのノブを微調整することができます, 更新がリリースするために出荷されると, AdGuardユーザーの万人は、それが完璧に見つけます.

## 3.6.11

- 公表: 2023-01-23T13:18:23Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

あなたは、AndroidのアップデートのためにAdGuardを欠いている必要があります。 まあ、製品の新しいリリースで2023にブレイクしているので、今は飽きませんし、そこからトラクションを得るだけです。

アンドロイド用のAdGuard v3.6.11の主な変更は、コアフィルタリングエンジン - CoreLibsとDNSLibsで作られました。 残りは、コンテンツのフィルタリングを強化し、アプリケーションのパフォーマンスを向上させるために、マイナーな変更を加えました。

## 更新されたDnsLibsにv2.0.75 [#4324](https://github.com/AdguardTeam/AdguardForAndroid/issues/4324)

DNS フィルタリングライブラリのかなり更新されたバージョンはより少ないリソースを消費し、より速く実行します。 DNS-over-QUIC プロトコルの実装が [RFC 9250] に対応しました。https://datatracker.ietf.org/doc/rfc9250/)標準で、実験的な状態が DoQ サポートから削除されました。

### 暗号化された ClientHello サポート [DL#161] の最初のステップhttps://github.com/AdguardTeam/DnsLibs/issues/161)

まず、暗号化された ClientHello とは何ですか? 今日では、ほぼすべてのインターネット接続が暗号化され、この暗号化された接続内のものを見ることができます。 ただし、接続の初期パケットは、接続しているサーバーの名前を示しています。 あなたが開いてみたいと言う`www.google.com`, あなたのISPは、あなたが送信し、それから受け取るものを見ることができません, しかし、彼らはあなたが通信しているウェブサイトを知っています. ECH(Encrypted ClientHello)は、この問題を解決し、暗号化されていない情報の最後のビットを暗号化する新しい技術です。

AdGuardからサポートする最初のステップは? 驚くべきことに、ECHを抑制することです! 両方に切り替えることによってこれを行うことができます`pref.dns.block.ech`そして、`pref.https.redirect.doh`*低レベル設定*のフラグ。

しかし、私たちは達成したいことは、ECHサポートをグローバルに提供することです。**すべての**あなたのアプリは、あなたのブラウザだけでなく、ECHの恩恵を受けることができます。 これを実現するために、AdGuardはアプリがそれに定期的なHTTPS接続を確立し、その代わりにECHを有効にした接続を確立します。 この実験機能は、次の更新のために計画されているため、調整されたままです。

## CoreLibsをv1.10.186に更新

### DNS-over-HTTPSフィルタリング

**安全なDNS要求をローカルDNSプロキシにリダイレクトするオプションを追加 [#1563](https://github.com/AdguardTeam/CoreLibs/issues/1563)**

ChromeとFirefox DNSのクエリは、DNS-over-HTTPSサーバーを使用してDNSフィルタリングを回避する場合があります。 AdGuard は DNS-over-HTTPS を自動フィルタリングできます。

この機能は実験的であり、*低レベル設定*で有効にすることができます。`pref.https.redirect.doh`. 将来のバージョンでは、デフォルトで有効にする予定です。

### コンテンツフィルタの改良

次の新機能は、メンテナーをフィルタリングし、コンテンツをフィルタリングするための高度な機能を提供することが重要です。

#### 導入事例

* 新規追加 [`$jsonprune`基本的な規則の修飾子>(https://adguard.com/kb/general/ad-filtering/create-own-filters/#jsonprune-modifier)。 この修飾子はJSON応答のための高度のろ過を可能にします [#1447] (https://github.com/AdguardTeam/CoreLibs/issues/1447)
* 新規追加 [`$hls`基本的な規則の修飾子>(https://adguard.com/kb/general/ad-filtering/create-own-filters/#hls-modifier)。 この修飾子は、ビデオ広告の防止に役立つHTTPライブストリーミングファイルを変更するための高度なフィルタリング機能を提供します。 [#1434](https://github.com/AdguardTeam/CoreLibs/issues/1434)
* 拡張された機能`$stealth`修飾子。 フィルタメンテナは、指定した URL に対して、Steeth Mode の機能が無効になっているかを指定できるようになりました。 唯一のオプションを変更する前に、ステルスモードを完全に無効化しました。 [#1224](https://github.com/AdguardTeam/CoreLibs/issues/1224)
* 空のサポートを追加`$path`非基本ルールの修飾子。 [#1591](https://github.com/AdguardTeam/CoreLibs/issues/1591)
* `$removeparam`POST リクエストに適用できるようになりました。 [#1573](https://github.com/AdguardTeam/CoreLibs/issues/1573)

#### 固定式

* ※レファラーを第三者から隠す* ステルスモードオプションは、`$third-party`修飾子 [#1640] (https://github.com/AdguardTeam/CoreLibs/issues/1640)
* 化粧品のルールと`:where()`擬似クラスが拒否されます [#1609](https://github.com/AdguardTeam/CoreLibs/issues/1609)
* ルールとルール`$third-party`modifier は、サイトのサブドメイン [#1637] からリソースをブロックします。https://github.com/AdguardTeam/CoreLibs/issues/1637)
* ルールとルール`$all`修飾子は、明示的に訪問されたサイトをブロックしません [#1590](https://github.com/AdguardTeam/CoreLibs/issues/1590)

## その他の改善

* デフォルトでSoul Browser [#4202] で HTTPS フィルタリングを有効にしました。https://github.com/AdguardTeam/AdguardForAndroid/issues/4202)

## その他の修正

* 2FA確認時、コードエントリーページが消える
* AdGuard はローカル VPN を作成せず、保護は [#4269] 起動しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4269)
* Wi-Fiからモバイルデータにネットワークが変化しているときにインターネットが機能しない[#4265](https://github.com/AdguardTeam/AdguardForAndroid/issues/4265)
* iRobot Homeアプリとの互換性の問題 [#4273](https://github.com/AdguardTeam/AdguardForAndroid/issues/4273)

アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.11 ベータ 2

- 公表: 2023-01-18T16:58:16Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11-beta-2

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

リリース前の2つのベータは良い兆候であると言う。 今日は、AdGuard v3.6.11の2番目のベータを1つの変更のみでリリースしています。 DnsLibs.

## 変更履歴


### 導入事例
* 更新されたDnsLibsにv2.0.75 [#4324](https://github.com/AdguardTeam/AdguardForAndroid/issues/4324)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.11 ベータ 1

- 公表: 2023-01-13T17:12:36Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11-beta-1

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

あなたは、AndroidのアップデートのためにAdGuardを欠いている必要があります。 まあ、2023年に新製品のベータ版で破綻しているので、今は飽きませんし、そこからだけ牽引を得るでしょう。

Androidのベータ版のAdGuard v3.6.11の主な変更は、コアフィルタリングエンジン - CoreLibsとDNSLibsで作られました。 残りは、コンテンツのフィルタリングを強化し、アプリケーションのパフォーマンスを向上させるために、マイナーな変更を加えました。

## DnsLibsをv2.0.66に更新

DNS フィルタリングライブラリのかなり更新されたバージョンはより少ないリソースを消費し、より速く実行します。 DNS-over-QUIC プロトコルの実装が [RFC 9250] に対応しました。https://datatracker.ietf.org/doc/rfc9250/)標準で、実験的な状態が DoQ サポートから削除されました。

### 暗号化された ClientHello サポート [DL#161] の最初のステップhttps://github.com/AdguardTeam/DnsLibs/issues/161)

まず、暗号化された ClientHello とは何ですか? 今日では、ほぼすべてのインターネット接続が暗号化され、この暗号化された接続内のものを見ることができます。 ただし、接続の初期パケットは、接続しているサーバーの名前を示しています。 あなたが開いてみたいと言う`www.google.com`, あなたのISPは、あなたが送信し、それから受け取るものを見ることができません, しかし、彼らはあなたが通信しているウェブサイトを知っています. ECH(Encrypted ClientHello)は、この問題を解決し、暗号化されていない情報の最後のビットだけを暗号化する新しい技術です。

AdGuardからサポートする最初のステップは? 意外に、それを抑制することです! これは両方を転換することによってすることができます`pref.dns.block.ech`そして、`pref.https.redirect.doh`*Low Level Settings* のフラグ

しかし、私たちは達成したいことは、ECHサポートをグローバルに提供することです。**すべての**あなたのアプリは、あなたのブラウザだけでなく、ECHの恩恵を受けることができます。 これを実現するために、AdGuardはアプリがそれに定期的なHTTPS接続を確立し、その代わりにECHを有効にした接続を確立します。 この実験機能は、次の更新のために計画されているため、調整されたままです。

## CoreLibsをv1.10.186に更新

### DNS-over-HTTPSフィルタリング

**安全なDNS要求をローカルDNSプロキシにリダイレクトするオプションを追加 [#1563](https://github.com/AdguardTeam/CoreLibs/issues/1563)**

ChromeとFirefox DNSのクエリは、DNS-over-HTTPSサーバーを使用してDNSフィルタリングを回避する場合があります。 AdGuard は DNS-over-HTTPS を自動フィルタリングできます。

この機能は実験的であり、*Low Level Settings* で有効にすることができます。`pref.https.redirect.doh`. 将来のバージョンでは、デフォルトで有効にする予定です。

### コンテンツフィルタの改良

次の新機能は、メンテナーをフィルタリングし、コンテンツをフィルタリングするための高度な機能を提供することが重要です。

#### 導入事例

* 新規追加 [`$jsonprune`基本的な規則の修飾子>(https://adguard.com/kb/general/ad-filtering/create-own-filters/#jsonprune-modifier)。 この修飾子はJSON応答のための高度のろ過を可能にします [#1447] (https://github.com/AdguardTeam/CoreLibs/issues/1447)
* 新規追加 [`$hls`基本的な規則の修飾子>(https://adguard.com/kb/general/ad-filtering/create-own-filters/#hls-modifier)。 この修飾子は、ビデオ広告の防止に役立つHTTPライブストリーミングファイルを変更するための高度なフィルタリング機能を提供します。 [#1434](https://github.com/AdguardTeam/CoreLibs/issues/1434)
* 拡張された機能`$stealth`修飾子。 フィルタメンテナは、指定した URL に対して、Steeth Mode の機能が無効になっているかを指定できるようになりました。 唯一のオプションを変更する前に、ステルスモードを完全に無効化しました。 [#1224](https://github.com/AdguardTeam/CoreLibs/issues/1224)
* 空のサポートを追加`$path`非基本ルールの修飾子。 [#1591](https://github.com/AdguardTeam/CoreLibs/issues/1591)
* `$removeparam`POST リクエストに適用できるようになりました。 [#1573](https://github.com/AdguardTeam/CoreLibs/issues/1573)

#### 固定式

* ※レファラーを第三者から隠す* ステルスモードオプションは、`$third-party`修飾子 [#1640] (https://github.com/AdguardTeam/CoreLibs/issues/1640)
* 化粧品のルールと`:where()`擬似クラスが拒否されます [#1609](https://github.com/AdguardTeam/CoreLibs/issues/1609)
* ルールとルール`$third-party`modifier は、サイトのサブドメイン [#1637] からリソースをブロックします。https://github.com/AdguardTeam/CoreLibs/issues/1637)
* ルールとルール`$all`修飾子は、明示的に訪問されたサイトをブロックしません [#1590](https://github.com/AdguardTeam/CoreLibs/issues/1590)

## その他の改善

* デフォルトでSoul Browser [#4202] で HTTPS フィルタリングを有効にしました。https://github.com/AdguardTeam/AdguardForAndroid/issues/4202)

## その他の修正

* 2FA確認時、コードエントリーページが消える
* AdGuard はローカル VPN を作成せず、保護は [#4269] 起動しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/4269)
* Wi-Fiからモバイルデータにネットワークが変化しているときにインターネットが機能しない[#4265](https://github.com/AdguardTeam/AdguardForAndroid/issues/4265)
* iRobot Homeアプリとの互換性の問題 [#4273](https://github.com/AdguardTeam/AdguardForAndroid/issues/4273)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.10

- 公開日: 2022-08-26T16:36:40Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

このバージョンでは、コネクティビティチェックを改善しました。このアプリは、インターネット接続があるかどうかを判断します。

アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.10 ベータ 2

- 公表: 2022-08-25T18:14:18Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10-beta-2

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

マイナーなバグを修正する技術ベータアップデートです。

**Androidの直接ダウンロードリンクのためのAdGuard:**

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.10 ベータ 1

- 公表: 2022-08-23T14:23:22Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10-beta-1

>Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android用のAdGuard v3.6.10では、接続チェックを改善しました。このアプリは、インターネット接続があるかどうかを判断します。

**Androidの直接ダウンロードリンクのためのAdGuard:**

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.9

- 公開日: 2022-08-02T21:14:15Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.9

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

アプリの安定性を高め、マイナーなバグを修正する技術アップデートです。

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.9 ベータ 1

- 公開日: 2022-08-01T20:11:15Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.9-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

アプリの安定性を高め、マイナーなバグを修正する技術アップデートです。

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.8

- 公表: 2022-04-28T15:55:31Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.8

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

このバージョンでは、DPI の Protect という新機能を追加しました。 ナットシェルでは、ISPのディープパケット検査システムが訪問するウェブサイトを検出するのを防ぐため、発信トラフィックを変更します。 この機能が目に見えるようにし、有効にするには、Stealth Modeタブで「カスタム」を選択し、下にスクロールします。

また、Naver Whale Browser のデフォルトで、拡張機能の設定と HTTPS のフィルタリングを固定しました。 最後に、CoreLibs と DnsLibs が更新されました。

### 変更履歴

* [修正] AdGuardは、Samsung の安全なフォルダー、Android 12 [#4073] の中をオンにしないhttps://github.com/AdguardTeam/AdguardForAndroid/issues/4073)
* [修正済み] 推奨Magiskモジュール[#4126](「AdGuard証明書」で「証明書の移動」を置き換えます)https://github.com/AdguardTeam/AdguardForAndroid/issues/4126)
* [修正済み] "pref.dns.blocking.type" の翻訳をチェックし、[#4133] を外しているように見えます。https://github.com/AdguardTeam/AdguardForAndroid/issues/4133)
* [修正] 間違ったURLには、フロントワード(zh-TW) [#3654](https://github.com/AdguardTeam/AdguardForAndroid/issues/3654)
* [修正] サムスンデバイスに証明書をインストールするときに適切な設定セクションを開くことを確認してください [#4115](https://github.com/AdguardTeam/AdguardForAndroid/issues/4115) 
* [修正] DPI バイパスオプションをAdGuard Stealthモードに追加 [#4131](https://github.com/AdguardTeam/AdguardForAndroid/issues/4131)
* [その他] CoreLibs と DnsLibs を最新バージョンにアップデート

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.8 ベータ 1

- 公表: 2022-04-25T15:42:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.8-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

このベータでは、DPI の Protect という新機能を追加しました。 ナットシェルでは、ISPのディープパケット検査システムが訪問するウェブサイトを検出するのを防ぐため、発信トラフィックを変更します。 この機能が目に見えるようにし、有効にするには、Stealth Modeタブで「カスタム」を選択し、下にスクロールします。

また、Naver Whale Browser のデフォルトで、拡張機能の設定と HTTPS のフィルタリングを固定しました。 最後に、CoreLibs と DnsLibs が更新されました。

### 変更履歴

* [その他] CoreLibs を 1.9.57 に更新 [#4135](https://github.com/AdguardTeam/AdguardForAndroid/issues/4135)
* [その他] DnsLibsを1.7.11に更新 [#4121](https://github.com/AdguardTeam/AdguardForAndroid/issues/4121)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.7

- 公開日: 2022-02-02T13:37:47Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.7

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

突然、私たちのユーザーの何人かが不快感を経験した — 彼らはAndroid用のAdGuard v3.6.6が有効になっているとき、WhatsAppで音声通話を作成できませんでした。 CoreLibs チームはこの問題に対抗しました。
:books: ほかに、スクリプトライブラリにいくつかの修正を行いました()https://github.com/AdguardTeam/Scriptlets)。 要約するには、スクリプトは強力なブロックツールです。 特に、彼らは高貴な使命を実行します:アンチ広告ブロッカーを中和します。 以前のバージョンの AdGuard for Android は、ルールの正しい修正が含まれているスクリプトレットライブラリを持っていた`#%#/scriptlet(“abort-current-inline-script”, ...)`, いくつかのWebページを破ることができます。; 今問題は解決されます。.
すべての問題に対処するため、新しいバージョンを提示する準備ができています。 v3.6.7に会い、スムーズに機能するために最善を尽くしました。

### 変更履歴

* [修正] AdGuard は WhatsApp [#4080] で呼び出しを破る (https://github.com/AdguardTeam/AdguardForAndroid/issues/4080)
* [Enhancement] CoreLibs から v1.8.285 [#4089](https://github.com/AdguardTeam/AdguardForAndroid/issues/4089)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.7 ベータ 1

- 公表: 2022-01-25T12:13:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.7-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

突然、私たちのユーザーの何人かが不快感を経験した — 彼らはAndroid用のAdGuard v3.6.6が有効になっているとき、WhatsAppで音声通話を作成できませんでした。 CoreLibs チームはこの問題に対抗しました。
:books: ほかに、スクリプトライブラリにいくつかの修正を行いました()https://github.com/AdguardTeam/Scriptlets)。 要約するには、スクリプトは強力なブロックツールです。 特に、彼らは高貴な使命を実行します:アンチ広告ブロッカーを中和します。 以前のバージョンの AdGuard for Android は、ルールの正しい修正が含まれているスクリプトレットライブラリを持っていた`#%#/scriptlet(“abort-current-inline-script”, ...)`, いくつかのWebページを破ることができます。; 今問題は解決されます。.
すべての問題に対処するため、新しいバージョンを提示する準備ができています。 v3.6.7-betaに会い、スムーズに機能するために最善を尽くしました。

### 変更履歴

* [修正] AdGuard は WhatsApp [#4080] で呼び出しを破る (https://github.com/AdguardTeam/AdguardForAndroid/issues/4080)
* [Enhancement] CoreLibs から v1.8.285 [#4089](https://github.com/AdguardTeam/AdguardForAndroid/issues/4089)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.6

- 公開日: 2021-12-30T10:55:42Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.6

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android用のAdGuardの最後の更新後、一部のユーザーは、Firefoxブラウザの以前のバージョンを使用して、アプリのクラッシュの問題に遭遇した可能性があります。 さて、今年は全ての債務をクローズし、今日のパッチを解放することにしました。 CoreLibs はリリースなしでもできるものもしました。

### 変更履歴

* [修正] 以前のバージョンのFireFoxブラウザを使用して、AdGuardがクラッシュ [#4068](https://github.com/AdguardTeam/AdguardForAndroid/issues/4068)
* [Enhancement] CoreLibsをv1.8.281に更新しました [#4076](https://github.com/AdguardTeam/AdguardForAndroid/issues/4076)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.5

- 公表: 2021-12-17T11:39:26Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.5

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android用のAdGuard v3.6.5をリリースする時間です。 このバージョンの最大のことは、悪意のあるフィッシングサイトへのリクエストをブロックし、サイトをより速くする強化されたブラウジングセキュリティモジュールです! 重要なポイントは、CoreLibsとDNSLibsをアップデートして、アプリがより確実に実行し、さまざまなマイナーなバグを修正しました。 AndroidでAdGuard v3.6.5を楽しむことを願っています!

* **[Enhancement]セキュリティモジュールの強化**

新しいセーフブラウジングAPI v2の実装では、悪意のあるフィッシングサイトへのリクエストをブロックする責任のあるセキュリティモジュールがより効果的になりました。 このモジュールのアップグレードされたバージョンは、インターネットを安全に閲覧し、悪意のあるコードが実行される可能性はありません。

### 変更履歴

* [修正] アドガードとのケネティックなアプリの互換性の問題 [#4035](https://github.com/AdguardTeam/AdguardForAndroid/issues/4035)
* [修正] CosmoteギリシャキャリアVoWiFiブロック [#3821](https://github.com/AdguardTeam/AdguardForAndroid/issues/3821)
* [参加] ブラウザの一覧に360ブラウザを追加 [#4040](https://github.com/AdguardTeam/AdguardForAndroid/issues/4040)
* [Enhancement] コアリブを v1.8.274 に更新 [#4061](https://github.com/AdguardTeam/AdguardForAndroid/issues/4061)
* [Enhancement] DnsLibsをv1.6.70に更新 [#4051](https://github.com/AdguardTeam/AdguardForAndroid/issues/4051)


#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.5 ベータ

- 公開日: 2021-12-02T12:51:50Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.5-beta

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Androidのベータ版でAdGuard v.3.6.5を満たしています! 変化は殆どありませんが、とても大切です。 メインニュースは、Safebrowsingモジュールをアップグレードしたので、これまで以上にWebの気持ちを安全にサーフできるようになりました。 詳しくはこちら もちろん、CoreLibs と DNSLibs をアップデートしました(ただし、真のリリースではありません)。 新しいバージョンをお楽しみ下さい!

* **[Enhancement] セーフブラウジングv2.0**
悪意のあるフィッシングサイトへのリクエストをブロックする責任があるSafebrowsingは、アップグレードされています。 このモジュールの新しいバージョンでは、インターネットをより安全に閲覧できます。

### 変更履歴

* [修正] アドガードとのケネティックなアプリの互換性の問題 [#4035](https://github.com/AdguardTeam/AdguardForAndroid/issues/4035)
* [修正] CosmoteギリシャキャリアVoWiFiブロック [#3821](https://github.com/AdguardTeam/AdguardForAndroid/issues/3821)
* [参加] ブラウザの一覧に360ブラウザを追加 [#4040](https://github.com/AdguardTeam/AdguardForAndroid/issues/4040)
* [Enhancement] コアリブを v1.8.256 に更新 [#1000](https://github.com/AdguardTeam/AdguardForMac/issues/1000)
* [Enhancement] DnsLibsをv1.6.66に更新しました [#989](https://github.com/AdguardTeam/AdguardForMac/issues/989)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.4

- 公開日: 2021-09-17T13:02:29Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.4

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

このクイックアップデートは、長期的なユーザーに起こったバグを修正しました。 数年間AdGuardを使用していて、セキュリティ証明書が期限が切れた場合、HTTPSフィルタリングの失敗につながる可能性があります。 この更新後、アプリのメイン画面に通知が表示されます。 タップすると、画面上の指示に従って、証明書を再インストールし、HTTPSフィルタリングを再開します。

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.3

- 公開日: 2021-09-08T14:53:39Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.3

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

このバージョンでは、CoreLibs の更新に重点を置いています。 つまり、既存の修飾子の優先順位に対処し、いくつかの新しいものを追加しました。`$denyallow`, `$redirect-rule`, `$removeheader`と`$specifichide`. [自分の広告フィルタを作成する] にしたいユーザーに興味があるかもしれません(https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters)。 また、ユーザースクリプトの除外作業を適切に行い、見つかったすべての問題を修正しました。
v4.0をお待ちしていますので、お待ちしています。 私たちを信頼してください。

### 変更履歴

* [修正] プロキシは、各 AdGuard VPN 更新 [#3680] 後に無効になります(https://github.com/AdguardTeam/AdguardForAndroid/issues/3680)
* [修正済み] セットアップウィザードで設定されたステルスモードの設定は適用されません [#3747](https://github.com/AdguardTeam/AdguardForAndroid/issues/3747)
* [修正] AdGuard は [#3837] で MEGA アプリのログのユーザを許可しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3837)
* [修正] 「ネットワークコールバックが登録されていない」 保護を停止したときにエラー [#3870](https://github.com/AdguardTeam/AdguardForAndroid/issues/3870)
* [修正] Instagram はローカル HTTP プロキシ モード (root アクセス) [#3879] で動作しません。https://github.com/AdguardTeam/AdguardForAndroid/issues/3879)
* [修正済み] AdGuardが有効になったときにNektoMeが機能しません [#374](https://github.com/AdguardTeam/AdguardForAndroid/issues/374)
* [修正] 携帯電話がIPv6接続にアクセスしている場合, Android用のAdGuardは、IPv4経由でのみアクセス可能なDNS-over-QUICサーバーに接続できませんでした [#3927](https://github.com/AdguardTeam/AdguardForAndroid/issues/3927)
* [修正] DNS セクションで言語を変更する問題 [#3731](https://github.com/AdguardTeam/AdguardForAndroid/issues/3731)
* [修正] ルート + ローカル HTTP プロキシの減速 Android 7 [#3844](https://github.com/AdguardTeam/AdguardForAndroid/issues/3844)
* [修正済み] プロキシ接続ステータスエラーチェック [#3848](https://github.com/AdguardTeam/AdguardForAndroid/issues/3848)
* [修正済み] [#3866] を有効にしたときに TikTok が動作しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3866)
* [修正] 間違った除外を提案`$removeparam`フィルタリングログのルール [#3873](https://github.com/AdguardTeam/AdguardForAndroid/issues/3873)
* [修正] IPv4 ネットワーク インターフェイスが [#3886] の場合、DNS64 の設定を DNSLibs に渡さないでください(https://github.com/AdguardTeam/AdguardForAndroid/issues/3886)
* 【修正】富士通デバイスの接続問題
* [修正] 期限切れのセキュリティ証明書での問題
* [修正] IPv4のデフォルトルートを強制するパブリックネットワークリストを拡張する
* [修正]`com.android.browser`複数のデバイスへの接続の問題
* [修正] ステルスモード画面はスクロールできません
* [Enhancement] DnsLibsをv1.6.29に更新 [#3952](https://github.com/AdguardTeam/AdguardForAndroid/issues/3952)
* [Enhancement] DNS-over-QUIC (Removed "experimental" ラベル) [#3842]https://github.com/AdguardTeam/AdguardForAndroid/issues/3842)
* [Enhancement] トルコ - トルクセルVoWifi新しいIPアドレス [#3864]()https://github.com/AdguardTeam/AdguardForAndroid/issues/3864)
* [Enhancement] ファンボーイのAnnoyance ListのサブスクリプションURLが壊れています [#3865](https://github.com/AdguardTeam/AdguardForAndroid/issues/3865)
* [Enhancement] Edge Dev、Edge Beta、Styx Browser のデフォルトで HTTPS フィルタリングを有効にする [#3897](https://github.com/AdguardTeam/AdguardForAndroid/issues/3897)
* [参加] [#3923] をフィルタリングから AdGuard VPN パッケージを除外しないハードコードしないでください(https://github.com/AdguardTeam/AdguardForAndroid/issues/3923)
* [Enhancement] Yandex Browser をブラウザーの一覧に追加 [#3951](https://github.com/AdguardTeam/AdguardForAndroid/issues/3951)

### CoreLibs を v1.8.163 [#3945] に更新しました。https://github.com/AdguardTeam/AdguardForAndroid/issues/3945)

* [修正] ルールと`$important`修飾子はルールよりも高い優先度を持っている必要があります`$all`修飾子 [#1440] (https://github.com/AdguardTeam/CoreLibs/issues/1440)
* [修正済み] ユーザスクリプトの除外は [#1425] が動作しないhttps://github.com/AdguardTeam/CoreLibs/issues/1425)
* [参加] 追加する`$denyallow`修飾子 [#1304] (https://github.com/AdguardTeam/CoreLibs/issues/1304)
* [参加] 追加する`$redirect-rule`修飾子 [#1303] (https://github.com/AdguardTeam/CoreLibs/issues/1303)
* [参加] 追加する`$removeheader`修飾子 [#1427] (https://github.com/AdguardTeam/CoreLibs/issues/1427)
* [参加] 追加する`$specifichide`修飾子 [#1166] (https://github.com/AdguardTeam/CoreLibs/issues/1166)
* [参加] グローバル・プライバシー・コントロールの「Do NotSell」信号をStees Mode[#1451]に送信するオプションを追加します。https://github.com/AdguardTeam/CoreLibs/issues/1451)
* [参加] ネグエーションの仕組みを改善`$redirect`ルール [#1388](https://github.com/AdguardTeam/CoreLibs/issues/1388)
* [その他] ルール`$extension`修飾子ブロック解除リクエスト [#1350](https://github.com/AdguardTeam/CoreLibs/issues/1350)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.3 ベータ

- 公開日: 2021-08-31T15:11:34Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.3-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android用のAdGuard v4.0が来ていると発表したのは、いつか覚えていますか? 今日、新しい時代のしきい値に立ち、明るい見通しを予見し、ついにそれを解放しています... v3.6.3ベータ。 バダムッツ!

### 変更履歴

* [修正] プロキシは、各 AdGuard VPN 更新 [#3680] 後に無効になります(https://github.com/AdguardTeam/AdguardForAndroid/issues/3680)
* [修正済み] セットアップウィザードで設定されたステルスモードの設定は適用されません [#3747](https://github.com/AdguardTeam/AdguardForAndroid/issues/3747)
* [修正] AdGuard は [#3837] で MEGA アプリのログのユーザを許可しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3837)
* [修正] 「ネットワークコールバックが登録されていない」 保護を停止したときにエラー [#3870](https://github.com/AdguardTeam/AdguardForAndroid/issues/3870)
* [修正] Instagram はローカル HTTP プロキシ モード (root アクセス) [#3879] で動作しません。https://github.com/AdguardTeam/AdguardForAndroid/issues/3879)
* [修正済み] AdGuardが有効になったときにNektoMeが機能しません [#374](https://github.com/AdguardTeam/AdguardForAndroid/issues/374)
* [修正] 携帯電話がIPv6接続にアクセスしている場合, Android用のAdGuardは、IPv4経由でのみアクセス可能なDNS-over-QUICサーバーに接続できませんでした [#3927](https://github.com/AdguardTeam/AdguardForAndroid/issues/3927)
* [修正] DNS セクションで言語を変更する問題 [#3731](https://github.com/AdguardTeam/AdguardForAndroid/issues/3731)
* [修正] ルート + ローカル HTTP プロキシの減速 Android 7 [#3844](https://github.com/AdguardTeam/AdguardForAndroid/issues/3844)
* [修正済み] プロキシ接続ステータスエラーチェック [#3848](https://github.com/AdguardTeam/AdguardForAndroid/issues/3848)
* [修正済み] [#3866] を有効にしたときに TikTok が動作しません。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3866)
* [修正] フィルタリングログの $removeparam ルールのために提案された間違った除外 [#3873](https://github.com/AdguardTeam/AdguardForAndroid/issues/3873)
* [修正] IPv4 ネットワーク インターフェイスが [#3886] の場合、DNS64 の設定を DNSLibs に渡さないでください(https://github.com/AdguardTeam/AdguardForAndroid/issues/3886)
* 【修正】富士通デバイスの接続問題
* [修正] 期限切れのセキュリティ証明書での問題
* [修正] IPv4のデフォルトルートを強制するパブリックネットワークリストを拡張する
* [修正] 複数のデバイス上のcom.android.browser接続の問題
* [修正] ステルスモード画面はスクロールできません
* [Enhancement] CoreLibsをv1.8.163に更新 [#3945](https://github.com/AdguardTeam/AdguardForAndroid/issues/3945)
* [Enhancement] DnsLibsをv1.6.29に更新 [#3952](https://github.com/AdguardTeam/AdguardForAndroid/issues/3952)
* [Enhancement] DNS-over-QUIC (Removed "experimental" ラベル) [#3842]https://github.com/AdguardTeam/AdguardForAndroid/issues/3842)
* [Enhancement] トルコ - トルクセルVoWifi新しいIPアドレス [#3864]()https://github.com/AdguardTeam/AdguardForAndroid/issues/3864)
* [Enhancement] ファンボーイのAnnoyance ListのサブスクリプションURLが壊れています [#3865](https://github.com/AdguardTeam/AdguardForAndroid/issues/3865)
* [Enhancement] Edge Dev、Edge Beta、Styx Browser のデフォルトで HTTPS フィルタリングを有効にする [#3897](https://github.com/AdguardTeam/AdguardForAndroid/issues/3897)
* [参加] [#3923] をフィルタリングから AdGuard VPN パッケージを除外しないハードコードしないでください(https://github.com/AdguardTeam/AdguardForAndroid/issues/3923)
* [Enhancement] Yandex Browser をブラウザーの一覧に追加 [#3951](https://github.com/AdguardTeam/AdguardForAndroid/issues/3951)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.2

- 公開日: 2021-05-13T14:29:46Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

まあ、よく、3.6.2リリースが届きました。 1つのベータと2つのRCが成功を収めました。私たちは「Hooray」と述べ、最終バージョンをすぐにリリースしました。

それでは、その中のものは何ですか? 当社は、更新されたCoreLibsとDnsLibsについて書き込むことができ、SDNSがDoQサーバーのリンクを解析するなどのレポートとマイナーな問題のデータ収集を改善しましたが、正直に、多くの人がそれが何を意味するのかを理解しているわけではありません。 信頼して、アプリはより良いものばかりになりました!

P.S. v4.0 がリリースされました。 うまくいけば、v3.6.2は新しい時代の前に最後の方法の駅になります。

<img src="">https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/Starken.png">

### 変更履歴

* [Enhancement] サポートされているブラウザーの一覧に Microsoft Edge Canary ブラウザーを追加しました [#3808](https://github.com/AdguardTeam/AdguardForAndroid/issues/3808)
* [Enhancement] サポートされているブラウザーのリストに Iceraven Browser を追加しました [#3797](https://github.com/AdguardTeam/AdguardForAndroid/issues/3797)
* [Enhancement] サポートされているブラウザーのリストに QQ および UC ブラウザーを追加しました [#3707](https://github.com/AdguardTeam/AdguardForAndroid/issues/3707)
* [Enhancement] サポートされているブラウザの一覧にプライバシーブラウザを追加しました [#3677](https://github.com/AdguardTeam/AdguardForAndroid/issues/3677)
* [Enhancement] HTTPS フィルタリングリストに Vivaldi スナップショットを追加 [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)
* [Enhancement] 既定の除外リストに人気のWi-Fi呼び出しサーバーを追加しました [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Enhancement] posteitaliane.posteapp.appbpolを除外に追加しました [#3756](https://github.com/AdguardTeam/AdguardForAndroid/issues/3756)
* [修正] 組み込みのiptablesは、 "-p dport" [#3782] のサポートが不足しているhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3782)
* [修正] com.google.android.feedback [#3655] でフィルタリングを無効にするhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3655)
* [修正] 試用期間を取得することができません [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [修正] com.tomtom.amigo.huawei アプリの互換性 [#3767]()https://github.com/AdguardTeam/AdguardForAndroid/issues/3767)
* [修正] de.avm.android.fritzapp — VoIP/SIP の問題 [#3810](https://github.com/AdguardTeam/AdguardForAndroid/issues/3810)
* [修正] /proc/net/tcp6 [#3832] を読みながらバッファが疲れていました(https://github.com/AdguardTeam/AdguardForAndroid/issues/3832)
* [その他] クルディッシュローカリゼーションを追加 [#3774](https://github.com/AdguardTeam/AdguardForAndroid/issues/3774)
* [その他] DnsLibs を v1.5.26 に更新 [#3829](https://github.com/AdguardTeam/AdguardForAndroid/issues/3829)
* [その他] アプリ除外リストに「ユニファイネットワーク」を追加
#### CoreLibsをv1.7.211に更新
* [修正] CSS ルールと```URL```許可されていない[#1431](https://github.com/AdguardTeam/CoreLibs/issues/1431)
* [修正] hepsiburada.comでHTTPSフィルタリングの問題 [#1406]()https://github.com/AdguardTeam/CoreLibs/issues/1406)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.2 RC 2

- 公開日: 2021-05-11T11:31:40Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-rc-2

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

ここでは、Android用のAdGuard v3.6.2用の2番目のリリース候補があります。 AdGuard は複数のプロキシが使用しているデバイスでより良い実行できるようにしました。 さらに、DnsLibs は1回以上更新されました。

### 変更履歴

* [修正] /proc/net/tcp6 [#3832] を読みながらバッファが疲れていました(https://github.com/AdguardTeam/AdguardForAndroid/issues/3832)
* [その他] DnsLibsをv1.5.26に更新

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.2 RC 1

- 公表: 2021-04-30T13:35:19Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-rc-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android 用の AdGuard v3.6.2 のリリース候補をご紹介します。 最終バージョンから2つのタスクのみを分離します。 次の停止, リリース.

### 変更履歴

* [修正] hepsiburada.comでHTTPSフィルタリングの問題 [#1406]()https://github.com/AdguardTeam/CoreLibs/issues/1406)
* [その他] DnsLibsをv1.5.24に更新

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.2 ベータ 1

- 公表: 2021-04-27T19:02:59Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Androidのベータ版でAdGuard v3.6.2を満たしています! このバージョンでは、CoreLibs と DnsLibs を v1.7.211 に更新し、それぞれ v1.5.18 に更新しました。このバージョンでは、例外のリストにいくつかのアプリを追加し、レポートを提出するためのデータ収集を改善しました。 また、DoQサーバーのSDNSリンクを解析するなど、他のマイナーな問題を修正しました。

### 変更履歴

* [Enhancement] サポートされているブラウザーの一覧に Microsoft Edge Canary ブラウザーを追加しました [#3808](https://github.com/AdguardTeam/AdguardForAndroid/issues/3808)
* [Enhancement] サポートされているブラウザーのリストに Iceraven Browser を追加しました [#3797](https://github.com/AdguardTeam/AdguardForAndroid/issues/3797)
* [Enhancement] サポートされているブラウザーのリストに QQ および UC ブラウザーを追加しました [#3707](https://github.com/AdguardTeam/AdguardForAndroid/issues/3707)
* [Enhancement] HTTPS フィルタリングリストに Vivaldi スナップショットを追加 [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)
* [Enhancement] プライバシーブラウザのサポート [#3677](https://github.com/AdguardTeam/AdguardForAndroid/issues/3677)
* [Enhancement] 既定の除外リストに人気のWi-Fi呼び出しサーバーを追加しました [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Enhancement] posteitaliane.posteapp.appbpolを除外に追加しました [#3756](https://github.com/AdguardTeam/AdguardForAndroid/issues/3756)
* [Enhancement] コアリブを v1.7.180 に更新 [#3737](https://github.com/AdguardTeam/AdguardForAndroid/issues/3737)
* [修正] 組み込みのiptablesは、 "-p dport" [#3782] のサポートが不足しているhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3782)
* [修正] com.google.android.feedback [#3655] でフィルタリングを無効にするhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3655)
* [修正] 試用期間を取得することができません [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [修正] com.tomtom.amigo.huawei アプリの互換性 [#3767]()https://github.com/AdguardTeam/AdguardForAndroid/issues/3767)
* [修正] de.avm.android.fritzapp — VoIP/SIP の問題 [#3810](https://github.com/AdguardTeam/AdguardForAndroid/issues/3810)
* [その他] クルディッシュローカリゼーションを追加 [#3774](https://github.com/AdguardTeam/AdguardForAndroid/issues/3774)
* [その他] アプリ除外リストに「ユニファイネットワーク」を追加
* [その他] DnsLibsをv1.5.18に更新
* [その他] CoreLibsをv1.7.211に更新
* [修正] CSS ルールと```URL```許可されていない[#1431](https://github.com/AdguardTeam/CoreLibs/issues/1431)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.1

- 公開日: 2021-02-19T11:49:04Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

ソフトウェアリリースライフサイクルのもう1ラウンド完了! アンドロイド用のAdGuardのこのバージョンは、それ自体のアルファが自信を持ってリリースするのを確信しています。 CoreLibsを定期的に更新し、バグや互換性の問題のカップルを修正しました。 今回は、広告なしでYouTubeを見ているような衝撃的な機能はありませんが、このリリースは以前のものよりも重要ではありません。 結局のところ、私たちはすべての更新でより良い取得しています!

### 変更履歴

* [Enhancement] CoreLibs が v1.7.189 に更新されました [#3749](https://github.com/AdguardTeam/AdguardForAndroid/issues/3749)
* [修正] 4GとIPv6でフィルタリングが動作しません [#3527](https://github.com/AdguardTeam/AdguardForAndroid/issues/3527)
* [修正] アプリ経由で試用期間を取得しようとするとエラー [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [修正] hepsiburada.com - HTTPS フィルタリングの問題 [#1406]()https://github.com/AdguardTeam/CoreLibs/issues/1406)
* [修正]blockchain.comが壊れています [#1411](https://github.com/AdguardTeam/CoreLibs/issues/1411)
* [修正] 互換性の問題
* [その他] 既定の除外リストに複数の一般的なWi-Fi呼び出しサーバーを追加しました [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [その他] Vivaldi スナップショット ブラウザの HTTPS フィルタリングがデフォルトで有効になっています [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6.1 ベータ 1

- 公開日: 2021-02-15T16:15:08Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.1-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

これは、AdGuard v4.0 への最初のベータです。 バグのカップルを修正し、定期的なCoreLibs更新を行い、他のいくつかの変更を行いました。

### 変更履歴

* [Enhancement] CoreLibs が v1.7.188 に更新されました [#3743](https://github.com/AdguardTeam/AdguardForAndroid/issues/3743)
* [修正] 4GとIPv6でフィルタリングが動作しません [#3527](https://github.com/AdguardTeam/AdguardForAndroid/issues/3527)
* [修正] アプリ経由で試用期間を取得しようとするとエラー [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [修正] 互換性の問題
* [その他] 既定の除外リストに複数の一般的なWi-Fi呼び出しサーバーを追加しました [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [その他] Vivaldi スナップショット ブラウザの HTTPS フィルタリングがデフォルトで有効になっています [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.6

- 公開日: 2020-12-15T10:43:20Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android v3.6 用の AdGuard は 2 つのかなり大きな変更、新しい機能によって見出しられます。 アプリとDNS-over-QUICプロトコルのサポートで、YouTubeのアドフリーを視聴しています。 最初の1つは把握が容易で、2つ目は説明します。
​

**[活動内容] YouTubeの広告を視聴するオプション [#2994](https://github.com/AdguardTeam/AdguardForAndroid/issues/2994)**
​
AndroidでYouTubeで広告をブロックすることは、他のアプリのトラフィックをフィルタリングすることを妨げる制限のおかげで、長い間ブラウザに限定されています。 しかし、YouTubeアプリで広告を避けるための方法を見つけました。 これらの簡単な手順に従ってください:
​
<img src="">https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/share.gif"style="border: 1px ソリッド #efefefef; max-height: 700px; max-width: 350px; padding: 2px;">
​
1. YouTubeアプリを開き、視聴したい動画を始めます。
2. 共有ボタンをタップし、アプリのリストからAndroid用のAdGuardを選択します。
3. 広告を中断することなくビデオを見ることができる新しいウィンドウがポップアップ表示されます!
​

DNS-over-QUIC サポート
​
DNS-over-QUIC または単に DoQ は、DNS 暗号化プロトコルです。 DNS 暗号化プロトコルについては、DNS-over-HTTPS と DNS-over-TLS (DoH と DoT 対応) の最も一般的なプロトコルについて聞いたことがあります。 それでは、DoQを特別にするのは何か? 物事の束, 本当に: 受信トレイの暗号化, 接続時間を削減, 失われたデータパケットの場合、より良いパフォーマンス.
​
<img src="">https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/DNS-over-QUIC_en.png"幅="300">
​
機能はまだ実験的です — アンドロイド用のAdGuardは、DNS-over-QUICの最初のオープンソースの実装の1つですが、それは完全に機能しており、試してみることをお勧めします。 *DNS フィルタリング* で確認します。 AdGuard DNS を選択し、利用可能な暗号化プロトコルの中から DoQ を選択します。
​
### 変更履歴

* [Enhanced] Firefox Fenix ブラウザーの HTTPS フィルタリングが強制的に [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [参加] "What's new" ダイアログが更新されました [#3638](https://github.com/AdguardTeam/AdguardForAndroid/issues/3638) 
* [修正]シャドウ靴下プロキシは自動的に削除されます[#3641](https://github.com/AdguardTeam/AdguardForAndroid/issues/3641) 
​
#### DnsLibs が v1.4.14 に更新

* [Enhanced] DoQ/DoH/DoT クエリはフォールバック [#86] を使用する前に取得されます。https://github.com/AdguardTeam/DnsLibs/issues/86) 
* [その他] DNS スタンプ [#84] に DoQ サポートを追加しました(https://github.com/AdguardTeam/DnsLibs/issues/84) 
​
#### アンドロイド直接ダウンロードリンクのためのAdGuard:

- [リリースチャネル](https://agrd.io/apk)
- [ベータチャネル](https://agrd.io/apkb)
- [ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.5.2

- 公開日: 2020-11-20T14:16:26Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.2

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

今日は小さいですが、まだ非常に重要なホットフィックスを立ち上げています。 つまり、新しいChrome 87との互換性が改善され、CoreLibsが更新されました。

**[その他] ERR HTTP2 PROTOCOL ERROR 一部のウェブサイト #1374**

今週のChrome 87がリリースされました。この問題は、HTTP/2フィルタリングプロトコルを使用する際のAdGuardと互換性の問題です。一部のサイトでは、通常のハングとダウンロードエラーが発生することがあります。 このアップデートでは、Chrome 87 との互換性をフィルタリングする HTTP/2 が改善されました。新しい安定したバージョンにできるだけ早くアップグレードすることをお勧めします。 :)

### 変更履歴

- [参加] ブラウザのリストにcom.huawei.browserを追加 #3495
- [参加] Firefoxのフェニックスブラウザ #3617 用の強制 HTTP フィルタリングを有効にします。
- [その他] 互換性の問題

#### アップグレードされたCoreLibsからv1.7.150

- [Enhancement] 提供されているホスト名(プロキシモード用)#123とソケットを接続する
- [参加] ライブラリバージョン#1150
- [修正]`$badfilter`ルールはドメインリストに敏感です #1331
- [その他] $generichide ルールは、アシスタントが AdGuard が無効であることを示していることを引き起こします #7
- [その他] 睡眠モードからコンピュータをwakingした後の接続エラー #3412

#### アンドロイド直接ダウンロードリンクのためのAdGuard:

[リリースチャネル](https://agrd.io/apk)
[ベータチャネル](https://agrd.io/apkb)
[ナイトリーチャンネル](https://agrd.io/android_nightly)

## 3.5.1

- 公開日: 2020-10-02T11:20:59Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.1

> Android用の免責事項 AdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

Android用のAdGuardのリリースバージョン3.5.1を満たします。 AdGuard VPN との統合を改善し、シームレスな連携を維持するよう取り組んできました。 また、CoreLibs と Dnslibs を更新しました。

## 変更履歴

* [Enhancement] Fennec F-Droidをブラウザのリストに追加 [#3587](https://github.com/AdguardTeam/AdguardForAndroid/issues/3587)
* [Enhancement] ブラウザのリストにcom.huawei.browserを追加 [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
* [Enhancement] Firefox Fenix ブラウザーの強制 HTTP フィルタリングを有効にします。 [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [修正済み] Android 11 [#3564] で AdGuard アプリケーションの更新作業を行います(https://github.com/AdguardTeam/AdguardForAndroid/issues/3564)
* [修正] タイの広告フィルタは、言語フィルタグループが有効になっている場合に常に有効に [#3520](https://github.com/AdguardTeam/AdguardForAndroid/issues/3520)
* [その他] DnsLibs を 1.3.24 バージョンに更新 [#3578](https://github.com/AdguardTeam/AdguardForAndroid/issues/3578)
* [その他] ru.sogaz.tm - アプリが動作していません [#3573](https://github.com/AdguardTeam/AdguardForAndroid/issues/3573)

## アップグレードされたCoreLibsからv1.7.114

* [参加] Add $pingコンテンツタイプ[#1258](https://github.com/AdguardTeam/CoreLibs/issues/1258)
* [参加] 信頼できる型CSPがコンテンツスクリプトを破らないことを確認してください[#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320)
* [修正] AGFDVSocketは、アウトバウンドプロキシセットの場合、元のピアアドレスを返すことはありません[#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)
* [修正] AdGuard は HTTPS のフィルタリングが無効になったときにドメインをフィルタリングしません [#1343](https://github.com/AdguardTeam/CoreLibs/issues/1343)
* [修正] AdGuardはSafari macOS Big Sur (無限円ローダー)でYoutubeと連携しません [#727](https://github.com/AdguardTeam/AdguardForMac/issues/727)
* [修正] $ elemhide、jsinject、extension 無効な HTML フィルタリング規則 [#1337] による除外 (https://github.com/AdguardTeam/CoreLibs/issues/1337)
* [修正] ログをフィルタリングすると、クッキーに関する情報が表示されません [#3406](https://github.com/AdguardTeam/AdguardForWindows/issues/3406)
* [修正] 問題のあるユーザスクリプト [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [修正] local.adguard.org が非 HTTPS フィルタリング プロセスからアクセスしたときに冗長エラー [#1056](https://github.com/AdguardTeam/CoreLibs/issues/1056)
* [修正] RegexpルールはURLに一致しません [#1311](https://github.com/AdguardTeam/CoreLibs/issues/1311)
* [修正] 外部リクエストは、有効なDNSモジュール[#3411]でログをフィルタリングするようになります(https://github.com/AdguardTeam/AdguardForWindows/issues/3411)
* [修正] URL には、フィルタといくつかの規則に一致する間、追加のスラッシュが含まれています [#1338](https://github.com/AdguardTeam/CoreLibs/issues/1338)
* [修正済み] フィルタリングログ [#1312] に間違ったフィルタが表示されるhttps://github.com/AdguardTeam/CoreLibs/issues/1312)
* [修正] &#96;$badfilter&#96; ドメインリストに機密ルール [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331)
* [修正] hkclubs.samsung.com [#1340]()https://github.com/AdguardTeam/CoreLibs/issues/1340)
* [その他] Mac用のAdGuardは、インターネット接続なしで保護を開始しません[#1323](https://github.com/AdguardTeam/CoreLibs/issues/1323)
* [その他] Windows でエラーエンコーディングを修正 [#79](https://github.com/AdguardTeam/DnsLibs/issues/79)
* [その他] 一部のサイトでHTMLが検出されない[#1308](https://github.com/AdguardTeam/CoreLibs/issues/1308)
* [その他] ローカル adguard.org の証明書は [#1348] が期限切れしたときに再発行されません。(https://github.com/AdguardTeam/CoreLibs/issues/1348)

### **Androidの直接ダウンロードリンクのためのAdGuard:**

**[リースチャネル](https://agrd.io/apk)**

**[ベータチャンネル](https://agrd.io/apkb)**

**[ナイトリーチャンネル](https://agrd.io/android_nightly)**

## 3.5.1 ベータ 1

- 公開日: 2020-09-28T16:25:59Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.1-beta-1

これは、Android用のAdGuard v3.5.1の予定されていないアップデートです。 誰がそうしようと思ったんですが、ダブルチェックが痛くないんですか? このベータでは、いくつかの厄介なバグを修正しました, 更新されたCoreLibsとDnslibs. リリース準備はほぼ完了です。

## 変更履歴

* [Enhancement] Fennec F-Droidをブラウザのリストに追加 [#3587](https://github.com/AdguardTeam/AdguardForAndroid/issues/3587)
* [修正済み] グループが有効になっている場合は、タイの広告フィルタが常に有効になっています [#3520](https://github.com/AdguardTeam/AdguardForAndroid/issues/3520)
* [その他]CoreLibsを1.7.114に更新しました [#3596](https://github.com/AdguardTeam/AdguardForAndroid/issues/3596) 
* [その他] DnsLibs を 1.3.24 バージョンに更新 [#3578](https://github.com/AdguardTeam/AdguardForAndroid/issues/3578) 

## コアライブラリ

### アップグレードされたCoreLibsからv1.7.114

* [参加] Add $pingコンテンツタイプ[#1258](https://github.com/AdguardTeam/CoreLibs/issues/1258) 
* [参加] 信頼できる型CSPがコンテンツスクリプトを破らないことを確認してください[#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320) 
* [修正] AGFDVSocketは、アウトバウンドプロキシセットの場合、元のピアアドレスを返すことはありません[#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330) 
* [修正] AdGuard は HTTPS のフィルタリングが無効になったときにドメインをフィルタリングしません [#1343](https://github.com/AdguardTeam/CoreLibs/issues/1343) 
* [修正] AdGuardはSafari macOS Big Sur (無限円ローダー)でYoutubeと連携しません [#727](https://github.com/AdguardTeam/AdguardForMac/issues/727) 
* [修正] $elemhide、jsinject、拡張機能で除外する [#1337](https://github.com/AdguardTeam/CoreLibs/issues/1337) 
* [修正] ログをフィルタリングすると、クッキーに関する情報が表示されません [#3406](https://github.com/AdguardTeam/AdguardForWindows/issues/3406) 
* [修正] local.adguard.org が HTTPS 以外のプロセスからアクセスしたときに冗長エラー [#1056](https://github.com/AdguardTeam/CoreLibs/issues/1056) 
* [修正] 問題のあるユーザスクリプト [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273) 
* [修正] RegexpルールはURLに一致しません [#1311](https://github.com/AdguardTeam/CoreLibs/issues/1311) 
* [修正] URL には、フィルタといくつかの規則に一致する間、追加のスラッシュが含まれています [#1338](https://github.com/AdguardTeam/CoreLibs/issues/1338) 
* [修正] 外部リクエストは、有効なDNSモジュール[#3411]でログをフィルタリングするようになります(https://github.com/AdguardTeam/AdguardForWindows/issues/3411) 
* [修正] &#96;$badfilter&#96; ドメインリストに機密ルール [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331) 
* [修正] hkclubs.samsung.com [#1340]()https://github.com/AdguardTeam/CoreLibs/issues/1340) 
* [その他] 一部のサイトでHTMLが検出されない[#1308](https://github.com/AdguardTeam/CoreLibs/issues/1308) 
* [その他] ローカル adguard.org の証明書は [#1348] が期限切れしたときに再発行されません。(https://github.com/AdguardTeam/CoreLibs/issues/1348)

## 3.5 

- 公開日: 2020-09-08T13:12:00Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5

Android用のAdGuard v3.5をリリースする時間です。 今回は2つのベータをテストし、変更ログを拡張しました。 お問い合わせ Android用のAdGuard VPN、CoreLibsの更新、固定バグのロードトラックによる互換性モードを導入しました。

**[Enhancement] Androidアプリ用のAdGuard VPNと互換性モード #3441**

Android用のAdGuard VPNが最初に導入されたので、すでにAdGuard広告ブロッカーと一緒に動作させる方法がありました。 しかし、平和で共存する2つのアプリを作るためには、いくつかのフープをジャンプする必要があります。 先に行ってから100%をやり直した人は、以来、適切な統合を待っています。

2つのアプリをインストールし、一緒に作業を開始すると、最高の種類の互換性があります。 お問い合わせ すでにAdGuard広告ブロッカーがインストールされていると仮定して、Google PlayストアからAdGuard VPNをダウンロードしてください(広告ブロッカーアプリからすぐに入手できます。一般的な設定メニューに新しいアイテムがあります)。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/settings.gif"幅="300">

どちらのアプリも互いに検出し、スムーズなジョイントワークに必要なすべての操作を行います。 アドフリーのインターネットとVPNのすべての利点の両方を楽しむために残されます。 ちなみに、他の方法も機能します: 既に実行中のAdGuard VPNの上にAdGuard広告ブロッカーをインストールし、あなたは良いです。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/compatibility.gif"幅="300">

何らかの理由でCompatibility Modeを無効にしたい場合は、AdGuard広告ブロッカーの設定から、スイッチを切り替えるだけです。 さらに、デバイスの通知バーにAdGuard広告ブロッカーとAdGuard VPNタイルを追加し、自分の意志でワンタップでそれらを切り替えることができます。Compatibility Modeのおかげで、設定はすぐに変更され、静かに変更されます。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/tiles.png"幅="300">

## 変更履歴

- [Enhancement] アプリのショートカット [#2656] のための適応アイコン (https://github.com/AdguardTeam/AdguardForAndroid/issues/2656)
- [Enhancement] デフォルトブラウザの一覧にFirefox Fenixブラウザを追加しました [#2861](https://github.com/AdguardTeam/AdguardForAndroid/issues/2861)
- [参加] ユーザーフィルタ[#2962]の上に新しいルールが追加されました(https://github.com/AdguardTeam/AdguardForAndroid/issues/2962)
- [Enhancement] 'Block' ボタンは、フィルタリングログ[#3012]を介してカスタムルールを追加した後、すぐに「ブロック解除」に切り替えます(https://github.com/AdguardTeam/AdguardForAndroid/issues/3012)
- [Enhancement] ログをエクスポートしたときにstate.txtに書き込まれた拡張情報 [#3063](https://github.com/AdguardTeam/AdguardForAndroid/issues/3063)
- [参加] ウェブレポーティングツール [#3288] のクエリ文字列にユーザスクリプトを有効にしました。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3288)
- [参加] 「更新チェック」ショートカットが「#3318」で表示される画面を更新します(https://github.com/AdguardTeam/AdguardForAndroid/issues/3318)
- [Enhancement] プロキシサーバーの自動化 API [#3363](https://github.com/AdguardTeam/AdguardForAndroid/issues/3363)
- [Enhancement] デフォルトブラウザの一覧にMozilla Referenceブラウザを追加しました [#3408](https://github.com/AdguardTeam/AdguardForAndroid/issues/3408)
- [参加] DNSフォールバックを無効にするオプションを追加しました [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
- [Enhancement] AdGuardは、ドメインネームフィルタをAdGuard DNSフィルタにリネームしました [#3475](https://github.com/AdguardTeam/AdguardForAndroid/issues/3475)
- [Enhancement] adguard.crt を AdGuardCertificate.pem に変更 [#3489](https://github.com/AdguardTeam/AdguardForAndroid/issues/3489)
- [Enhancement] デフォルトブラウザの一覧にHuaweiブラウザを追加しました [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
- [参加] "What's new" ダイアログを追加します。 [#3532](https://github.com/AdguardTeam/AdguardForAndroid/issues/3532) 
- [Enhanced] v3.5リリース前のAdGuardの準備 [#3546](https://github.com/AdguardTeam/AdguardForAndroid/issues/3546) 
- [修正] 文の最初の文字が「メッセージがサポートする」画面に自動的に大文字化されていない[#3079](https://github.com/AdguardTeam/AdguardForAndroid/issues/3079)
- [修正] AdGuardは、制限されたアカウントでデバイス上で動作しません [#3299](https://github.com/AdguardTeam/AdguardForAndroid/issues/3299)
- [修正] 「更新のチェック」のトースト通知が遅く表示されます [#3343](https://github.com/AdguardTeam/AdguardForAndroid/issues/3343)
- [修正済み] Android 11 [#3478] で不要な "Android Private DNS が有効になっています" 通知https://github.com/AdguardTeam/AdguardForAndroid/issues/3478)
- [修正] Android 11で正常に動作しない一部のアプリでダウンロード [#3516](https://github.com/AdguardTeam/AdguardForAndroid/issues/3516)
- [修正] 無効なオプションの間違った状態 [#3538](https://github.com/AdguardTeam/AdguardForAndroid/issues/3538)
- [修正] 奇妙な小さな "m^" ルール [#3548] に関連するバグを修正しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/3548)
- [その他] デフォルト DNS のリゾルバ [#3428] のオプションを更新しました。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3428)

## DnsLibs(ドングリブ)

- [参加] ホストのルールの行の最後にコメントのサポートを追加しました [#75](https://github.com/AdguardTeam/DnsLibs/issues/75)
- [修正] LDNS ロギング [#73](https://github.com/AdguardTeam/DnsLibs/issues/73)
- [その他] RTT でソートする上流を追加 [#39](https://github.com/AdguardTeam/DnsLibs/issues/39)

## コアリブ

- [Enhancement] #@# 指定されたドメインなしで、ルールを完全に無効にする必要があります [#1296](https://github.com/AdguardTeam/CoreLibs/issues/1296)
- [Enhancement] 信頼されるタイプCSP [#1320]の検証を追加しました(https://github.com/AdguardTeam/CoreLibs/issues/1320)
- [修正済み] 接続は状態にタイムアウトしました [#1180]()https://github.com/AdguardTeam/CoreLibs/issues/1180)
- [修正] 問題のあるユーザスクリプト [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
- [修正] プロセス名検出は、Windows セキュリティの警告を引き起こします [#1316](https://github.com/AdguardTeam/CoreLibs/issues/1316)
- [修正] OCSP チェックは、選択した DNS [#1328] を通過しない (https://github.com/AdguardTeam/CoreLibs/issues/1328)
- [修正] AGFDVSocketは、アウトバウンドプロキシセットの場合、元のピアアドレスを返すことはありません[#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)
- [その他] AdGuardが有効になったときに接続速度がキャッピングされます[#702](https://github.com/AdguardTeam/CoreLibs/issues/702)

## 3.3.3 リリース

- 公開日: 2020-04-03T10:45:22Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.231

しかし、新しいベータがロールアウトする前に、別のとうまく最後の修正を願っています。 SSL例外に複数のドメインを追加し、特定のモバイルキャリアとの互換性の問題を修正しました。

* [変更] HTTPSの除外リストを更新しました

## 3.4 リリース

- 公開日: 2020-05-21T11:21:25Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-release

AndroidでAdGuard v3.4に会いましょう。世界を見るのは時間です! ベータを2つテストし、より広い聴衆にこのバージョンを提示することを確信しています。 春は更新に時間がかかり、ソフトウェアは例外ではありません。 古いバグを修正し、CoreLibs を更新し、Android TV とより互換性のあるアプリを作成しました。

**[修正] AdGuardブロックインターネット接続#2842**

このバグは割れにくいナットでした。 長い間、AdGuardユーザーのデバイス上でランダムに(少なくとも、それはそうだった)登場しました。 それでも、対応する症状:AdGuardがオンになった間にスマートフォンは完全にネットワークを失いました。 もちろん、この問題を解決するためには、この問題が重要でした。そして最後に、それを解決しました。 あとで気持ちを和らげる言葉を超えて、影響を受けたユーザーだけにしましょう!

**[固定] ファイアウォールの制限は、WiFiが有効になったときに無視されます #3313**

特別な注意に値する別の面倒なバグ。 以前のバージョン 3.3 では、モバイルデータを介してインターネットにアクセスするアプリが特に禁止されている場合は、意図した動作ではない Wi-Fi を有効にするまで、制限が正しく機能しました。

**[Enhancement] DnsLibs #3229** との統合

DnsLibs は DNS フィルタリングに必要な DNS プロキシライブラリです。 DNS-over-TLS、DNS-over-HTTPS、DNSCrypt などの既存の DNS プロトコルをサポートしています。 古いDNSproxyを置き換えるために開発しました。これは深刻な欠陥でした。それは高いバッテリーリソース消費を引き起こしました。 DnsLibsはより最適化され、DNSフィルタリングを多く使用している場合は、携帯電話のバッテリーの寿命が長くなります。

**[Enhancement] Android TV #3238**で機能を改善

アンドロイド用のAdGuardは、まず、携帯電話やタブレット用のアプリを偽装していますが、スマートテレビなどの他のAndroidデバイスにインストールすることができます。 この特定のケースでは、以下のようないくつかの改善を行いました。

- AdGuardは、リストでより良い作品を発表
- スマートテレビのAGメニュー間のより良いナビゲーション
- スナックバーをクリックするオプション
- プロモーション画面を終了するオプション
- すべてのダイアログの「閉じる」オプション

お使いのスマートテレビにインストールすることを決定した場合、Android用のAdGuardは、使用がはるかに簡単です。 それでもバグや矛盾する行動に遭遇した場合は、こちらに報告してください。

## 変更履歴

- [修正] アプリケーションは、デバイスの再起動後に起動しません #3286
- [修正] アップデート後のステルスモードプリセットの変更 #3287
- [修正] ローカル変更バグ #3301
- [修正] com.android.providers.downloads トラフィックが #3355 をルーティングされていない
- [修正] フィルタリングは、Android 11で有効になっているAdGuardで動作しません #3377
- [修正] SOCKS5プロキシ#3394を通じてUDPを有効にする不可
- [修正] DNS フィルタ #3187 を解除せずにホットスポットを作成する不可
- [修正] 「HTTPS フィルタリングがオフ」 スナックバーは、ホーム画面 #3292 の "データ保存" ステータスをカバー
- [修正] ローカル HTTP プロキシ モード #3431 で 4G から Wi-Fi に切り替えると、アプリがクラッシュします。
- [修正] 設定画面の「戻る」ボタンが正しく動作します #3427
- [修正] AdGuardが#3430を起動しない
- [Enhancement] カスタムアドガード: userscripts #3000 を追加するためにスキームが使われます
- [Enhancement] 「Cancel」ボタンを「Add proxy」画面に追加 #3093
- [Enhancement]ステルス.enabled=false は、Stealth Mode がレポート #3169 を送信したときにオフになっている場合、クエリ文字列に送信されます。
- [参加] レポート#3350を送信すると、すべてのアプリパラメータで広告をブロックできるようになりました
- [参加] HTTPS フィルタリングエラー通知を抑制するオプション #3225
- [Enhancement] HTTPS フィルタリング ダイアログが #3284 を改善しました
- [Enhancement] ルーマニア語とタイのローカリゼーションが #3341 を追加しました
- [その他] アクノレッジページが更新されました #82
- [その他] 開発者向けFirefox Preview Nightlyがサポートされているブラウザーの一覧に追加されました #3333
- [その他] Android 11の証明書のインストールシーケンス #3354
- [その他] サポートされているブラウザーの一覧に Cobra Browser を追加しました #3357
- [その他] フィルタリングログ詳細を開くとAndroid 11でアプリケーションがクラッシュ #3366
- [その他] Vivaldi スナップショットと Vivaldi Sopranos は、サポートされているブラウザーの一覧に追加されました。 #3400
- [その他] サポートされているブラウザの一覧にBrave Betaを追加 #3401
- [その他] ローカル HTTP プロキシモード #3416 で AdGuard がクラッシュ
- [その他] HTTPS除外リストが更新されました #3419, #3425
- [その他] ユズブラウザプラス 対応ブラウザの一覧に追加 #3424
- [その他] サポートされているブラウザーの一覧にBrave Nightly追加 #3432
- [その他] HTTPSの除外リストを更新しました
- [その他] 翻訳更新

## CoreLibs は v1.5.265 に更新されました。

- [修正] 化粧品のルールは、CSSのルール#1293として使用できます
- [修正] 規則の選択アルゴリズムは、HTTPS のフィルタリングが無効な場合意図されていないように動作します #1291
- [修正] 制限されたドメインのルールは、参照者なしで要求に一致しません #1286
- [修正] 「プロトコルフィルタの初期化に失敗しました」 エラー #1282
- [修正] 拡張CSSのルールが間違っているとJSのルール#1147に問題が生じます
- [修正] '予稿したとにかく' は、ウェブサイトが規則でブロックされている場合、正しく動作しません。`$all`修飾語 #1267

## DnsLibs が v1.2.26 に更新

- [その他] 'ブロック解除' ボタンは、ログのフィルタリングに表示されません #3429

## 3.6 ベータ 1

- 公開日: 2020-11-20T18:04:23Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6-beta-1

> **免責** Android向けAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

今日は小さいですが、まだ非常に重要なベータ版を立ち上げています。 つまり、新しいChrome 87との互換性が改善され、CoreLibsが更新されました。

**[その他] ERR HTTP2 PROTOCOL ERROR 一部のウェブサイト [#1374](https://github.com/AdguardTeam/AdguardForAndroid/issues/1374)**

今週のChrome 87がリリースされました。この問題は、HTTP/2フィルタリングプロトコルを使用する際のAdGuardと互換性の問題です。一部のサイトでは、通常のハングとダウンロードエラーが発生することがあります。 このアップデートでは、Chrome 87 との互換性をフィルタリングする HTTP/2 が改善されました。新しい安定したバージョンにできるだけ早くアップグレードすることをお勧めします。 :)

## 変更履歴

* [Enhancement] ブラウザのリストにcom.huawei.browserを追加 [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495) 
* [Enhancement] Firefox Fenix ブラウザーの強制 HTTP フィルタリングを有効にします。 [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [Enhancement] AdGuardにそれらを共有することにより、Youtubeのビデオ広告を視聴するためのオプション [#2994](https://github.com/AdguardTeam/AdguardForAndroid/issues/2994)
* [修正] 非標準ポート [#1366] を使用する場合は、プレーン HTTP をフィルタリングしません。https://github.com/AdguardTeam/CoreLibs/issues/1366)
* [修正] 互換性の問題

### アップグレードされたCoreLibsからv1.7.150

* [Enhancement] 提供されているホスト名 (プロキシモードの場合) [#123] とソケット接続を改善します(https://github.com/AdguardTeam/CoreLibs/issues/123) 
* [Enhancement] ライブラリバージョン [#1150] を示すhttps://github.com/AdguardTeam/CoreLibs/issues/1150) 
* [修正] &#96;$badfilter&#96; ドメインリストに機密ルール [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331) 
* [その他] $generichide ルールは、アシスタントが AdGuard が無効であることを示す原因 [#7](https://github.com/AdguardTeam/BrowserAssistant/issues/7) 
* [その他] スリープモードからコンピュータを目覚めた後の接続エラー[#3412](https://github.com/AdguardTeam/AdguardForWindows/issues/3412)

## 3.5 RC 1

- 公開日: 2020-08-26T14:28:28Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-rc-1

Android用のAdGuard v3.5のリリース候補が公開されました。 信頼できるユーザーにRCバージョンを公開することは、リリース前の新機能をテストするための素晴らしい方法です。

このアップデートには、小さな修正とCoreLibsのアップグレードのカップルが含まれています。輝きまですべてを磨くことに熱心です。

## 変更履歴

* [Enhanced] v3.5リリース前のAdGuardの準備 [#3546](https://github.com/AdguardTeam/AdguardForAndroid/issues/3546) 
* [修正] フォールバックを無効にするオプション [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
* [修正] 奇妙な小さな "m^" ルール [#3548] に関連するバグを修正しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/3548) 

## コアライブラリ

#### アップグレードされたCoreLibsからv1.7.64

* [修正] 問題のあるユーザスクリプト [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [修正] AGFDVSocketは、アウトバウンドプロキシセットの場合、元のピアアドレスを返すことはありません[#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)

## 3.5 ベータ 2

- 公開日: 2020-08-21T10:56:44Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-beta-2

このアップデートでは、いくつかの仕上げのタッチを追加し、CoreLibs フィルタリングエンジンを更新し、いくつかのバグを修正しました。 そこまで。

## 変更履歴

* [参加] "What's new" ダイアログを追加します。 [#3532](https://github.com/AdguardTeam/AdguardForAndroid/issues/3532)
* [Enhancement] adguard.crt を AdGuardCertificate.pem に変更 [#3489](https://github.com/AdguardTeam/AdguardForAndroid/issues/3489)
* [修正] 無効なオプションの間違った状態 [#3538](https://github.com/AdguardTeam/AdguardForAndroid/issues/3538)

## コアライブラリ

#### アップグレードされたCoreLibsからv1.7.58

* [Enhancement] #@# 指定されたドメインなしで、ルールを完全に無効にする必要があります [#1296](https://github.com/AdguardTeam/CoreLibs/issues/1296)
* [修正済み] 接続は状態にタイムアウトしました [#1180]()https://github.com/AdguardTeam/CoreLibs/issues/1180) 
* [修正] OCSP チェックは、選択した DNS [#1328] を通過しない (https://github.com/AdguardTeam/CoreLibs/issues/1328)

## 3.5 ベータ 1

- 公開日: 2020-08-14T17:11:03Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-beta-1

今日は、Android用のAdGuard v3.5の最初のベータ版をリリースしました。 それは、その変更ログにさまざまなインプラントの長いリストを備えていますが、主な焦点は、間違いなく、Android用のAdGuard VPNで新しく導入された互換性モードです。

**[Enhancement] AdGuard VPN Androidアプリとの互換性モード [#3441](https://github.com/AdguardTeam/AdguardForAndroid/issues/3441)**

AdGuard VPN for Android が初めて導入されました。https://adguard.com/en/blog/introducing-adguard-vpn-for-android.html)、すでにAdGuard広告ブロッカーと一緒に動作させる方法がありました。 しかし、平和で共存する2つのアプリを作るためには、いくつかのフープをジャンプする必要があります。 先に行ってから100%をやり直した人は、以来、適切な統合を待っています。

2つのアプリをインストールし、一緒に作業を開始すると、最高の種類の互換性があります。 お問い合わせ 既にAdGuard広告ブロッカーがインストールされていると仮定して、 [Playストア] から AdGuard VPN をダウンロードします()https://play.google.com/store/apps/details?id=com.adguard.vpn) (広告ブロッカーアプリからすぐに入手できます。一般設定メニューに新しい項目があります)。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/settings.gif"幅="300">

どちらのアプリも互いに検出し、スムーズなジョイントワークに必要なすべての操作を行います。 アドフリーのインターネットとVPNのすべての利点の両方を楽しむために残されます。 ちなみに、他の方法も機能します: 既に実行中のAdGuard VPNの上にAdGuard広告ブロッカーをインストールし、あなたは良いです。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/compatibility.gif"幅="300">

何らかの理由でCompatibility Modeを無効にしたい場合は、AdGuard広告ブロッカーの設定から、スイッチを切り替えるだけです。 さらに、デバイスの通知バーにAdGuard広告ブロッカーとAdGuard VPNタイルを追加し、自分の意志でワンタップでそれらを切り替えることができます。Compatibility Modeのおかげで、設定はすぐに変更され、静かに変更されます。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/tiles.png"幅="300">

* [Enhancement] アプリのショートカット [#2656] のための適応アイコン (https://github.com/AdguardTeam/AdguardForAndroid/issues/2656)
* [参加] ユーザーフィルタ[#2962]の上に新しいルールが追加されました(https://github.com/AdguardTeam/AdguardForAndroid/issues/2962)
* [Enhancement] デフォルトブラウザの一覧にHuaweiブラウザを追加しました [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
* [Enhancement] デフォルトブラウザの一覧にFirefox Fenixブラウザを追加しました [#2861](https://github.com/AdguardTeam/AdguardForAndroid/issues/2861)
* [Enhancement] デフォルトブラウザの一覧にMozilla Referenceブラウザを追加しました [#3408](https://github.com/AdguardTeam/AdguardForAndroid/issues/3408)
* [Enhancement] 'Block' ボタンは、フィルタリングログ[#3012]を介してカスタムルールを追加した後、すぐに「ブロック解除」に切り替えます(https://github.com/AdguardTeam/AdguardForAndroid/issues/3012)
* [Enhancement] プロキシサーバーの自動化 API [#3363](https://github.com/AdguardTeam/AdguardForAndroid/issues/3363)
* [参加] DNSフォールバックを無効にするオプションを追加しました [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
* [参加] 書面による拡張情報`state.txt`ログがエクスポートされるとき [#3063](https://github.com/AdguardTeam/AdguardForAndroid/issues/3063)
* [Enhancement] AdGuardは、ドメインネームフィルタをAdGuard DNSフィルタにリネームしました [#3475](https://github.com/AdguardTeam/AdguardForAndroid/issues/3475)
* [参加] ウェブレポーティングツール [#3288] のクエリ文字列にユーザスクリプトを有効にしました。(https://github.com/AdguardTeam/AdguardForAndroid/issues/3288)
* [参加] 「更新チェック」ショートカットが「#3318」で表示される画面を更新します(https://github.com/AdguardTeam/AdguardForAndroid/issues/3318)
* [修正] Android 11で正常に動作しない一部のアプリでダウンロード [#3516](https://github.com/AdguardTeam/AdguardForAndroid/issues/3516)
* [修正] AdGuardは、制限されたアカウントでデバイス上で動作しません [#3299](https://github.com/AdguardTeam/AdguardForAndroid/issues/3299)
* [修正] 文の最初の文字が「メッセージがサポートする」画面に自動的に大文字化されていない[#3079](https://github.com/AdguardTeam/AdguardForAndroid/issues/3079)
* [修正済み] Android 11 [#3478] で不要な "Android Private DNS が有効になっています" 通知https://github.com/AdguardTeam/AdguardForAndroid/issues/3478)
* [修正] 「更新のチェック」のトースト通知が遅く表示されます [#3343](https://github.com/AdguardTeam/AdguardForAndroid/issues/3343)
* [その他] 既定の DNS の決議のためのオプションを更新 [#3428](https://github.com/AdguardTeam/AdguardForAndroid/issues/3428)
* [その他] DnsLibs が v1.3.19 に更新
* [その他] CoreLibs が v1.7.49 に更新
* [その他] 互換性の問題

### DnsLibs(ドングリブ)

* [参加] ホストのルールの行の最後にコメントのサポートを追加しました [#75](https://github.com/AdguardTeam/DnsLibs/issues/75)
* [修正] LDNS ロギング [#73](https://github.com/AdguardTeam/DnsLibs/issues/73)
* [その他] RTT でソートする上流を追加 [#39](https://github.com/AdguardTeam/DnsLibs/issues/39)

### コアライブラリ

* [Enhancement] 信頼されるタイプCSP [#1320]の検証を追加しました(https://github.com/AdguardTeam/CoreLibs/issues/1320)
* [修正] 問題のあるユーザスクリプト [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [修正] プロセス名検出は、Windows セキュリティの警告を引き起こします [#1316](https://github.com/AdguardTeam/CoreLibs/issues/1316)
* [その他] AdGuardが有効になったときに接続速度がキャッピングされます[#702](https://github.com/AdguardTeam/CoreLibs/issues/702)

## 3.4 ベータ 2

- 公開日: 2020-05-14T13:18:29Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-beta-2

この実行-of-the-mill ベータでは、いくつかのバグを修正し、CoreLibs を更新します。 すべてがうまくいくと、次のリリースバージョンに変わります。

## 変更履歴

* [バグ] 設定画面の「戻る」ボタンが正しく動作します #3427
* [バグ] ローカル HTTP プロキシ モード #3431 で 4G から Wi-Fi に切り替えると、アプリがクラッシュします。
* [バグ] AdGuardが#3430を起動しない
* [その他] HTTPS除外リストが更新されました #3419, #3425
* [その他] サポートされているブラウザーの一覧にBrave Nightly追加 #3432
* [その他] ユズブラウザプラス 対応ブラウザの一覧に追加 #3424

### CoreLibs が v1.5.265 に更新

* [バグ] 拡張された CSS ルールが JS ルール #1147 に問題を引き起こします
* [バグ] 化粧品のルールは、CSSのルール#1293として使用できる
* [Bug] 'とにかく承認' オプションは、Webサイトが規則でブロックされている場合は正しく動作しません`$all`修飾語 #1267

### DnsLibs が v1.2.26 に更新

* [その他] 'ブロック解除' ボタンは、ログのフィルタリングに表示されません #3429

## 3.4 ベータ 1

- 公開日: 2020-04-27T11:49:40Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-beta-1

まずは、アドガードv3.4のベータ版をAndroid版にてご確認下さい。 物事オフを開始するには、最も古い既知のバグを修正し、Android TVの互換性を向上させるなど、いくつかの方向でアプリを強化しました。

**[Bug] AdGuardブロックインターネット接続 [#2842](https://github.com/AdguardTeam/AdguardForAndroid/issues/2842)**

このバグは非常に長い間私たちを驚かせていました。 AdGuardユーザーのさまざまなデバイスに登場し、ランダムに見えました。 しかし、この症状は同じでした。アドガードがオンになった間にスマートフォンは完全にネットワークを失いました。 言うまでもなく、この課題を解決する最優先事項であり、ついにそれを打ち負かしました。 信じるつもりではなく、影響を受けたユーザーだけでなく、私たちも大きな救済です!

**[Enhancement] DnsLibs との統合 [#3229](https://github.com/AdguardTeam/AdguardForAndroid/issues/3229)**

[DnsLibs](DnsLibs)https://github.com/AdguardTeam/DnsLibs)DNS フィルタリングを提供する必要がある DNS プロキシライブラリです。 DNS-over-TLS、DNS-over-HTTPS、DNSCrypt などの既存の DNS プロトコルをサポートしています。 古いDNSproxyを置き換えるために開発しました。これは深刻な流れでした。それは高いバッテリーリソース消費を引き起こしました。 DnsLibsはより最適化され、DNSフィルタリングを多く使用している場合は、携帯電話のバッテリーの寿命が長くなります。

**[Enhancement] Android TVで機能を改善しました [#3238](https://github.com/AdguardTeam/AdguardForAndroid/issues/3238)**

アンドロイド用のAdGuardは、まず、携帯電話やタブレット用のアプリを偽装していますが、スマートテレビなどの他のAndroidデバイスにインストールすることができます。 この特定のケースでは、以下のようないくつかの改善を行いました。

- AdGuardは、リストでより良い作品を発表
- スマートテレビのAGメニュー間のより良いナビゲーション
- スナックバーをクリックするオプション
- プロモーション画面を終了するオプション
- すべてのダイアログの「閉じる」オプション

お使いのスマートテレビにインストールすることを決定した場合、Android用のAdGuardは、使用がはるかに簡単です。 それでもバグや矛盾する行動に遭遇した場合は、その旨を報告してください。https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose).  

**[Bug] ファイアウォールの制限は、WiFiが有効になったときに無視されます[#3313](https://github.com/AdguardTeam/AdguardForAndroid/issues/3313)**

特別な言及に値する別の不快なバグ。 v3.3 では、モバイルデータを介してインターネットにアクセスするアプリが特に禁止されている場合、制限は、意図した行動ではなく、WiFi を有効にするまで、適切に機能しました。

## 変更履歴

* [バグ] デバイスの再起動後にアプリケーションが起動しません[#3286](https://github.com/AdguardTeam/AdguardForAndroid/issues/3286)
* [Bug] アップデート後のステルスモードプリセット変更 [#3287](https://github.com/AdguardTeam/AdguardForAndroid/issues/3287)
* [バグ] ロケール変更バグ [#3301](https://github.com/AdguardTeam/AdguardForAndroid/issues/3301)
* [バグ]`com.android.providers.downloads`トラフィックがルートされていない [#3355](https://github.com/AdguardTeam/AdguardForAndroid/issues/3355)
* [バグ] Android 11でAdGuardを有効にしてフィルタリングが動作しません [#3377](https://github.com/AdguardTeam/AdguardForAndroid/issues/3377)
* [バグ] UDP を SOCKS5 プロキシ経由で有効化可能 [#3394](https://github.com/AdguardTeam/AdguardForAndroid/issues/3394)
* [バグ] DNSフィルタリングを解除せずにホットスポットを作成することはできません[#3187](https://github.com/AdguardTeam/AdguardForAndroid/issues/3187)
* [バグ] 「HTTPS フィルタリングがオフ」スナックバーがホーム画面[#3292]の「データ保存」ステータスをカバーhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3292)
* [Enhancement] カスタム`adguard:`userscripts [#3000] を追加するためのスキームが使われます(https://github.com/AdguardTeam/AdguardForAndroid/issues/3000)
* [Enhancement] 「Cancel」ボタンを「Add proxy」画面に追加 [#3093](https://github.com/AdguardTeam/AdguardForAndroid/issues/3093)
* [参加]`stealth.enabled=false`レポート[#3169]を送信すると、Steeth Modeがオフになっている場合は、クエリ文字列に送信されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/3169)
* [参加]`Block ads in all apps`レポート[#3350]の送信時にパラメータが送信されます(https://github.com/AdguardTeam/AdguardForAndroid/issues/3350)
* [参加] HTTPS フィルタリングエラー通知を抑制するオプション [#3225](https://github.com/AdguardTeam/AdguardForAndroid/issues/3225)
* [Enhancement] HTTPS フィルタリング ダイアログが [#3284] を改善しました(https://github.com/AdguardTeam/AdguardForAndroid/issues/3284)
* [Enhancement] ルーマニア語とタイのローカリゼーションを追加しました [#3341](https://github.com/AdguardTeam/AdguardForAndroid/issues/3341)
* [その他] 開発者向けFirefox Preview Nightly がサポートされているブラウザーのリストに追加されました [#3333](https://github.com/AdguardTeam/AdguardForAndroid/issues/3333)
* [その他] サポートされているブラウザーのリストに Cobra Browser を追加しました [#3357](https://github.com/AdguardTeam/AdguardForAndroid/issues/3357)
* [その他] サポートされているブラウザのリストにBrave Betaを追加 [#3401](https://github.com/AdguardTeam/AdguardForAndroid/issues/3401)
* [その他] Vivaldi Snapshot と Vivaldi Sopranos は、サポートされているブラウザーのリストに追加されました [#3400](https://github.com/AdguardTeam/AdguardForAndroid/issues/3400)
* [その他] Android 11の証明書のインストールシーケンス [#3354](https://github.com/AdguardTeam/AdguardForAndroid/issues/3354)
* [その他] アクノレッジページが更新されました [#82](https://github.com/AdguardTeam/AdguardForAndroid/issues/82)
* [その他] ローカル HTTP プロキシモード [#3416] で AdGuard がクラッシュhttps://github.com/AdguardTeam/AdguardForAndroid/issues/3416)
* [その他] フィルタリングログ詳細を開くとAndroid 11でアプリケーションがクラッシュ [#3366](https://github.com/AdguardTeam/AdguardForAndroid/issues/3366)
* [その他] HTTPSの除外リストを更新しました
* [その他] 翻訳更新

## CoreLibs は v1.5.249 に更新されました

* [バグ] 化粧品のルールは、CSS ルール [#1293] として使用できます(https://github.com/AdguardTeam/CoreLibs/issues/1293)
* [バグ] 規則選択アルゴリズムは、HTTPS のフィルタリングが無効なときに意図しない [#1291](https://github.com/AdguardTeam/CoreLibs/issues/1291)
* [バグ] 制限ドメインのルールは、レファなしのリクエストに一致しません [#1286](https://github.com/AdguardTeam/CoreLibs/issues/1286)   
* [Bug] "プロトコルフィルタの初期化に失敗" エラー [#1282](https://github.com/AdguardTeam/CoreLibs/issues/1282)

## 3.3.2 リリース

- 公開日: 2020-02-13T16:26:35Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.230

この小さなアップデートでは、重要な修正と除外リストへのいくつかの追加があります。

* [修正] 除外アプリがインストールされている場合、保護は再起動しません #3340
* [変更] HTTPSの除外リストを更新しました

## 3.3.1 リリース

- 公開日: 2019-12-30T11:11:34Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.229

最近は、昨年のリリースを予定していたので、その年のリリースを予定していた。 このアップデートが'release' と呼ばれていると、'hotfix' の多くは無視されます。 この小さなホットフィックスがリリースを呼ばないので、正しいですか? バグ修正のカップルだけ、それだけです。

- [修正] 保護は、フィルタの更新#3286をチェックした後、電話を右に再起動すると、誤って起動しません
- [修正] Stealth Mode 設定はアプリ更新後保存されません #3287

## 3.3 リリース

- 公開日: 2019-12-26T13:21:38Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.228

過去10年間のAndroidリリースのためのAdGuard! 強固な音です。 とにかく、そのような大規模なアップデートがクリスマスに正しく落ちる他のものよりも、それは偶然の多くです。 そして、私たちを間違って取得しないでください:それは巨大です。 複数の主要な機能と50以上のもの - すべてがそれがy'allのための素敵なクリスマスギフトを作るために結合します!

**[改良済み] フィルタリングエンジン**

バージョン 3.3 は scriptlets と`$redirect`修飾子のサポート。 Scriptletsは、さまざまな回避技術を使用するウェブサイト上の広告をブロックするのに役立つ強力な広告ブロックツールです。`$redirect`修飾子は、ブロックするのではなく、特別な「リソース」で広告を置換できる別のツールです。 例えば、透明な1x1画像でバナーを交換できます。

**[変更] 搭載プロセス #2895**

再設計を心よりお待ちしております。 今回は、オンボーディングのシーケンスを刷新しました(基本的には、最初にアプリを起動したときに表示されるもの)。 主な変更:

- 'quick' または ‘long’ の設定を選択するためのオプション: キーの決定だけをするか、手動で設定の大部分を手動で設定するように求められます
- 弊社がAdGuardをさらに改善するのに役立つ技術的および相互作用情報を送信することを可能にする新しいオプション
- より良いグラフィックス!

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/welcome.png"<img src="300">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/create_vpn.png"幅="300">

**[追加] 新規アクティベーションフロー #2901**

多くのAndroidユーザーがiOSアプリのAdGuardを見る機会がなかったため、Premium機能の有効化のためにそこに使用されているシステムについて知らなかった可能性があります。 しかし、それはユーザーにとって便利なものとしてそれ自体を推薦しました、従って私達はまた人間の特徴をもつAdGuardのためにそれを採用しました。

<img src="">https://cdn.adguard.com/public/Adguard/screenshots/android/activation_En_account.png?123"<img src="300">https://cdn.adguard.com/public/Adguard/screenshots/android/activation_en_license.png"幅="300">

ご覧のとおり、ライセンスキーを直接入力するか、AdGuard個人アカウントにログインする2つのオプションがあります。 アカウントにPremiumを有効にするために使用できるライセンスキーがある場合、資格情報を入力すると自動的にピックアップされます。

### 広告ブロック

- [追加] Preset Stealth モード設定 #2625
- [追加] abp:subscribe and adguard:subscribe link interception #2918
- [追加]subscribe.adblockplus.orgリンクインターセプション#2930
- [変更] インターネット接続の可用性チェック方法 #3095
- [変更] 既知のブラウザリスト#3175にWhaleブラウザを追加しました
- [修正] DNS ユーザーフィルタのインポートバグ #2972
- [修正] 正当なホストリストが有効な#2982として認識されていないもの
- [修正] ローカルストレージ #2997 から追加されたリソースの更新を確認するときにエラー
- [修正] クイック設定は、異なるプライバシー保護レベルを選択することはできません #2768
- [修正] 「フィルタリングから除外する」ボタン動作 #3052
- [修正] Googleが「Always-on-VPN」を有効にして更新することはできません #3039
- [修正済み] AdGuard Extraは、利用可能なアップデート#3216がある場合に自動的に有効
- [修正] カスタムフィルタが有効になっている場合、アプリケーションはクラッシュを引き起こします #3258
- [修正] AdGuardは、Android 10でSamsung S10デバイス上のいくつかのUDP接続を分割します #3259
- [改善] AdGuardは、#2881時に保護を再起動することなく、設定の変更を適用する方法をオンザフライで使用できるようになりました
- [改善] クロークトラッカーをブロックするDNSフィルタリング #3228
- [Improved] Premiumがアクティブになったときに自動的に「Blockフィッシングとマルウェア」オプションが有効になっています #3249
- [Improved] AdGuardはIPv6インタフェース#3197なしでネットワークでAAAリクエストをブロックできるようになりました

### ログイン

- [追加] アプリ #2897 経由で新しいライセンスを購入するオプション
- [追加] OAuth #3081, #3244 による試用期間とライセンスの有効化
- [追加] アシスタントダイアログ#2853へのアプリオプションのホワイトリスト
- [追加] 一部の画面で「オン/オフ」スイッチ #2877
- [追加] 証明書のエラーに関する通知 #2722
- [追加] タップすることで現在のバージョン番号をコピーする能力 #2773
- [追加] タブ内のバージョン履歴へのリンク #2774
- [追加] システムデフォルトのテーマオプション #2174
- [追加] 更新ボタンの長タップとして無声更新アクション #2890
- [追加] Magisk ファームウェア #2941 で rooted デバイスの「証明書を移動する失敗」通知
- [追加] 新しい拡張子を追加するときにフィールド検証を空にします #2983
- [追加] 「リフレッシュライセンスステータス」ボタン #2988
- [追加] 購入ボタンを復元する: #2990を復元する何もない場合の通知
- [変更] インポートされたフィルタリストのURLは、コンテンツが使用されている場合は保存されません。リンクは#2813
- [変更] 同じウィンドウで開くChromeカスタムタブ #3019
- [変更] プレミアム画面がプレミアム#2843なしで表示できるようになりました
- [変更] 通知の動作を更新する #2922
- [変更] 回答がない場合でも、フィルタリングログに DNS リクエストタイプが表示されます #2961
- [変更] 検索中のフィルタカテゴリのタイトルをタップすると、各カテゴリの画面#3035が表示されます
- [変更] トースト通知パラメータ #3087
- [変更] プロキシ画面 UI #3092
- [変更] AdGuardは、選択したタイプのデータを記憶し、Apps Management #3140 に表示します。
- [変更] 活性化画面のフレーズ#3141
- [変更] 「DNS 統計をクリアする」 警告説明 #3194
- [変更] アプリ内購入設計を改良 #3252
- [修正] マイナーUIの問題 #2879
- [修正] メイン画面の分布グラフの問題 #2935
- [修正] アプリ管理画面で検索すると遅い #2951
- [修正] 予想外の接続がリセット #2980
- [修正] 言語変更後、正しくフィルタロケールが表示される #2971
- [修正] フィルタリングログ #2974 のスクローリング問題
- [修正] 間違ったフィルタの状態が #2987 を表示
- [修正] ネットワークが利用できなくなった場合の更新状況が適切でない #3020
- [修正] 「保護を開始する準備」通知 #3034
- [修正] 「フィルタの編集」オーバーレイバグ #3045
- [修正] アップデートがない場合、ディバイダーストライプはまだ表示されます #3047
- [修正] Cloudflare DNS 説明 #3062
- [修正] 中国語の日付形式が間違っている #3068
- [修正] アプリケーション更新アイコン #3098
- [修正] ミスボタンシャドウ #3109
- [修正] 最初の開始ダイアログ ボックスのボタンは、特定のデバイスモデル #3114 で表示できません
- [修正] カスタムフィルタのスイッチは誤ってフィルタグループ#3119の状態を表します
- [修正] 現在の画面を閉じる「複数のライセンスを購入」ボタンを押します #3136
- [修正] 証明書のインストールダイアログが欠落している #3176
- [修正] ライセンスが #3183 を期限切れると、トースト通知が表示されない
- [修正] フィードバックセクションの「Missed ad」オプションは、DuckDuckGoがデフォルトブラウザ#3128として選択されている場合、エラーになります
- [改善] HTTPS フィルタリング関連 UI 変更 #2896
- [改善] UI 要素が Android TV #2818 にフォーカスできるようになりました
- [改善] いくつかのモジュールの記述に追加された豊富なフォーマット #2878
- [改善] オンボーディング画面のフレーズ #3248
- [改善] アプリ管理の詳細アクティビティでフレーズ #3250
- [改善] ローカル化が更新されました: #3271, #3188, #3161

### ネットワーク

- [追加] 接続オーバーフロー防止システム #2989
- [追加]カスタムDNSサーバー用のTLS v1.3サポート #3132
- [変更] DNS-over-HTTPS接続数制限が廃止されました #3224
- [修正] 一部のアプリは、AdGuardローカルVPNが#2836であるときに利用可能なWiFiネットワークが表示されない
- [改善] AdGuard DNS設定とプライベートDNS #2797間のインタラクション
- [改善] AdGuardのネットワークの安全性と安定性 #2995
- [改善] 接続エラー処理 #3195

### その他

- [追加] ホワイトリストのエクスポート機能 #3069
- [修正] 短い非アクティブ期間の後に更新ウィンドウが表示されます #3055
- [修正] ユーザースクリプトの更新は、バッテリーサービス#3073によって追跡されません
- [修正] AdGuard 3.2 が #3076 を起動しない
- [修正] 「ライセンスデータを含める」オプションは、設定をエクスポートしようとすると誤って動作します #3067
- [修正] アプリがスケジュールされたタスクを実行するとクラッシュ #3164
- [修正] 更新アクティビティ #3165 のクラッシュ
- [修正] Android OSがアイコン#3166をロードしようとするとクラッシュ
- [修正] 一部のAndroidビルドでクラッシュ #3167
- [修正] メインアクティビティでクラッシュ #3168
- [修正済み] 拡張関数 #3171 と通信するときのクラッシュ
- [修正] ログが収集されるとクラッシュ #3212
- [修正]超バッテリーセーバー#3210でMIUI携帯電話上のクラッシュ
- [修正] 最大インポート設定ファイルサイズが10 Mb #3203に増加
- [改善] ターゲットSDKレベルは29 #3053に変更
- [改良] CoreLibs が v1.5.74 #3105 に更新されました

## 3.2.150

- 公開日: 2019-08-29T14:36:38Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.2.150

>免責事項: Android用のAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

以前のホットフィックスは、いくつかの緊急のバグに対処するので、我々は高速に行動し、少ない重要な問題の残りを修正することはできませんでした。 本日のアップデート以降は、すべて消えるべきです。

* [修正] DNS フィルタリングは HTC デバイス #3014 で定期的なフィルタリングを解除します
* [修正] AdGuardは完全にエクステンションを削除しません #3015
* [修正] ネットワークアクセスをグローバルにブロックする DNS リクエスト #3025
* [修正] DNS リクエストをバイパスすると、DNS フィルタリング #3026
* [修正済み] AdGuardは更新#3024後に保護を開始できません
* [修正] Facebook lite は IPv6 が到達できない #3031 を検出できません。
* [修正] ブロックされたアプリ通知は誤って動作します #3032
* [改善] dnsproxy ライブラリが更新されました #3016

## 3.2.140ホットフィックス

- 公開日: 2019-08-24T10:43:56Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.2.140

>免責事項: Android用のAdGuardはオープンソースプロジェクトではありません。 Github は、ユーザーがどの開発者が動作しているかを確認するために、オープンなバグトラッカーとして使用します。

これは、Androidリリース用の最近のAdGuard用の小さなホットフィックスです。 v3.2 で導入された新機能に関連したバグをほとんどスカッシュします。

* [修正] DNS フィルタリングは HTC デバイス #3014 で定期的なフィルタリングを解除します
* [修正] AdGuardは完全にエクステンションを削除しません #3015
* [改善] dnsproxy ライブラリが更新されました #3016

## 3.3 ベータ 3.1

- 公開日: 2019-12-09T21:49:53Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-3.1

カスタムフィルタが有効になっている場合、保護が開始されるときにアプリケーションのクラッシュを修正するクイックホットフィックス。

- [修正] カスタムフィルタが有効になっている場合、アプリケーションはクラッシュを引き起こします #3258

## 3.3 ベータ 3

- 公開日: 2019-12-09T17:13:16Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-3

Android用のAdGuardのこのベータは、それがv3.3の3分の1だという意味で、少しのアウターです。 通常、その点で変更ログが短くなり、大きなジューシーなタスクは後で残します。 リリースするほど、新しいバグを作成するのではなく、既存のバグを修正することに重点を置いています。

しかし、この時間ではありません! 私達はまだ私達で多くを残しました:新しい購入の流れ、質の改善を妨げる重大な広告。 もちろん、チョールのエスケープはありません:複数のバグフィックス、クラッシュハンティングなど。

**[追加] アプリ#2897**で新しいライセンスを購入するオプション

私たちはすでにそれを作ったので、あなたの個人的なアカウントをリンクするためにアプリを離れる必要はありません、そして今からあなたは今までにAdGuardを最小限に抑えることなくライセンスを購入することができます。 初めてアプリを起動する場合、またはPremiumを起動する時間を決めた場合は、よく馴染みのある画面に直面します。

<img src="">https://cdn.adguard.com/public/Adguard/screenshots/android/PremEN.png"<img src="300">https://cdn.adguard.com/public/Adguard/screenshots/android/SubEN.png"幅="299.5">

アプリは、希望するライセンスの種類とその期間を選択し、電子メールを入力するように要求します。 したがって、基本的には、ウェブサイト上で実行するだけでなく、ブラウザ内の追加のクリックや新しいタブなしで同じアクション。 追加する1つのことは、まだこの方法でライセンスを更新またはアップグレードすることはできませんが、heyです。 より多くのバージョンがあります。

### 広告ブロック

- [変更] 既知のブラウザリスト#3175にWhaleブラウザを追加しました
- [修正] 「フィルタリングから除外する」ボタン動作 #3052
- [修正] Googleが「Always-on-VPN」を有効にして更新することはできません #3039
- [修正済み] AdGuard Extraは、利用可能なアップデート#3216がある場合に自動的に有効
- [改善] クロークトラッカーをブロックするDNSフィルタリング #3228
- [Improved] Premiumがアクティブになったときに自動的に「Blockフィッシングとマルウェア」オプションが有効になっています #3249
- [Improved] AdGuardはIPv6インタフェース#3197なしでネットワークでAAAリクエストをブロックできるようになりました

### ログイン

- [追加] Magisk ファームウェア #2941 で rooted デバイスの「証明書を移動する失敗」通知
- [変更] AdGuardは、選択したタイプのデータを記憶し、Apps Management #3140 に表示します。
- [修正] アプリ管理画面で検索すると遅い #2951
- [修正] 証明書のインストールダイアログが欠落している #3176
- [修正] ライセンスが #3183 を期限切れると、トースト通知が表示されない
- [変更] 「DNS 統計をクリアする」 警告説明 #3194
- [改善] オンボーディング画面のフレーズ #3248
- [改善] アプリ管理の詳細アクティビティでフレーズ #3250
- [改善] 現地化が更新されました

### ネットワーク

- [追加] 接続オーバーフロー防止システム #2989
- [変更] DNS-over-HTTPS接続数制限が廃止されました #3224
- [修正] 一部のアプリは、AdGuardローカルVPNが#2836であるときに利用可能なWiFiネットワークが表示されない
- [修正] フィードバックセクションの「Missed ad」オプションは、DuckDuckGoがデフォルトブラウザ#3128として選択されている場合、エラーになります
- [修正] 互換性の問題
- [改善] 接続エラー処理 #3195

 ### その他

- [修正] アプリがスケジュールされたタスクを実行するとクラッシュ #3164
- [修正] 更新アクティビティ #3165 のクラッシュ
- [修正] Android OSがアイコン#3166をロードしようとするとクラッシュ
- [修正] 一部のAndroidビルドでクラッシュ #3167
- [修正] メインアクティビティでクラッシュ #3168
- [修正済み] 拡張関数 #3171 と通信するときのクラッシュ
- [修正] ログが収集されるとクラッシュ #3212
- [修正]超バッテリーセーバー#3210でMIUI携帯電話上のクラッシュ
- [修正] 最大インポート設定ファイルサイズが10 Mb #3203に増加

## 3.3 ベータ 2

- 公開日: 2019-10-24T16:44:48Z
- リリース:https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-2

第一次アドガードv3.3ベータがフラッドゲートをオープンしたようです。そして今では、開発者がより多くのリリースを阻止するために、世界中に電力はありません。 1週間に過ぎてから、次のいずれかを提示しています。 今回は、デザイナーの方もいらっしゃるし、見逃せないUI関連の変更に反映されています。

**[変更] 搭載プロセス #2895**

再設計を心よりお待ちしております。 今回は、オンボーディングのシーケンスを刷新しました(基本的には、最初にアプリを起動したときに表示されるもの)。 主な変更:

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/welcome.png"<img src="300">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/create_vpn.png"幅="300">

- 'quick' または ‘long’ の設定を選択するためのオプション: キーの決定だけをするか、手動で設定の大部分を手動で設定するように求められます
- 弊社がAdGuardをさらに改善するのに役立つ技術的および相互作用情報を送信することを可能にする新しいオプション
- より良いグラフィックス!

**[追加] HTTP フィルタリング ダイアログ #2967**

HTTPS フィルタリングは、Android 用の AdGuard のコーナーストーンです。 HTTPS プロトコルをフィルタリングする権限がなければ、AdGuard のアドブロッキング パワーは厳しく crippled です。 そのため、ユーザーの重要性を強調するために、追加のマイルを歩いています。

HTTPS フィルタリングがまだ有効になっていない場合、メインの AdGuard 画面に通知が表示され、クリックすると、HTTPS フィルタリングの仕組みと、なぜ強くそれをオンにするかを説明するシンプルで有益な GIF が表示されます。

<img src="">https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/https_dialog.gif"幅="300">

- [追加] 「リフレッシュライセンスステータス」ボタン #2988
- [追加]カスタムDNSサーバー用のTLS v1.3サポート #3132
- [追加] 購入ボタンを復元する: #2990を復元する何もない場合の通知
- [変更] 活性化画面のフレーズ#3141
- [変更] インターネット接続の可用性チェック方法 #3095
- [修正] 現在の画面を閉じる「複数のライセンスを購入」ボタンを押します #3136
- [修正] 最初の開始ダイアログ ボックスのボタンは、特定のデバイスモデル #3114 で表示できません
- [修正] カスタムフィルタのスイッチは誤ってフィルタグループ#3119の状態を表します
- [修正] 互換性の問題
- [改善] CoreLibs が v1.5.84 #3143 に更新されました
