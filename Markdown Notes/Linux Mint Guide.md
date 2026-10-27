# Linux Mintガイド

Linux Mintの導入から初期設定、日常利用、ソフトウェア管理、セキュリティ、トラブル対処までを初心者向けに整理した実用ガイドです。

---

| <div align="center">Metadata</div> | <div align="center">情報</div> |
| :--- | :--- |
| **ホームページ** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **ライセンス** | CC0-1.0 |
| **Version** | 202610270844 |

ライセンス、第三者コンテンツの扱いおよび無保証については [`LICENSES.md`](../LICENSES.md) を参照してください。

## Linux Mintを使い始めるまでの全体の流れ

初めて導入する場合は、上から順に進めてください。すでに導入済みなら、初期設定・日常利用から読めます。途中で判断できない項目があれば、ディスクへ書き込む前に止まり、機種名と画面の表示を確認しましょう。

| 段階 | この段階ですること | 次へ進む目安 |
| :--- | :--- | :--- |
| 1. PC選び | エディション、必要な性能、機種・部品のLinux対応を確認 | 必須機能と不明点を整理できた |
| 2. 事前準備 | 個人データとWindowsの回復手段を確保し、ISOを検証 | バックアップを開けて、元のOSへ戻す方法も分かる |
| 3. Live USB | USBから試用し、実機の互換性を確認 | 日常利用に必要な機能が動く。未確認の機能も把握した |
| 4. インストール | 導入先と消去範囲を確認してOSを導入 | USBを外してLinux Mintが起動する |
| 5. 初期設定 | Timeshift、更新、ドライバー、日本語、個人データの保護 | 日本語で操作でき、復旧とバックアップの準備ができた |
| 6. 日常利用 | アプリを入れ、ファイル操作・外部機器を確認 | 自分の用途で一通り使える |
| 7. 更新・保守 | Update Managerで更新し、バックアップを継続 | 更新後の動作とバックアップの成功を確認できた |
| 8. バックアップ | システムと個人ファイルを別々に守る | 保存先と戻し方が分かる |
| 9. 問題の切り分け | GUIで確認し、症状を記録。必要ならログを読む | 直前の変更・機種・症状を説明できる |
| 10. 復旧 | 旧カーネル、Live USB、データ退避、Timeshiftを使う | データを守ったうえで復元方法を選べる |

バックアップは第8段階まで待たず、**導入前と初期設定の段階から**用意します。後半のKernel PanicとAdGuard for Linuxは、必要になったときに読む発展的な内容です。

本ガイドはUbuntuを基盤とする通常版のCinnamonを主な対象にします。Debianを基盤とするLMDEやChromebookのOS入れ替えは、同じ手順で導入できるとは扱いません。画面名は日本語訳やバージョンで異なるため、英語の機能名も併記しています。

確認日：2026年10月19日。以下のバージョン情報は、確認時に公式サイトへ掲載されていた内容です。購入・導入時にもダウンロードページとRelease Notesを読み直してください。

Linux Mintは、デスクトップ / ノートPC向けに使いやすさを重視したLinuxディストリビューションです。現在の標準系列であるLinux Mint 22.xはUbuntu 24.04 LTS（Noble）を基盤とし、Linux Mint 22.3 “Zena” は2029年4月までサポートされます。公式にはCinnamon / MATE / Xfceの3エディションが提供され、CinnamonはLinux Mintの主力デスクトップ、MATEはクラシックな操作感、Xfceは比較的軽量な構成です。

* [Linux Mint 公式サイト](https://linuxmint.com/)
* [Linux Mint 22.3 ダウンロード](https://linuxmint.com/download.php)
* [Linux Mint 全バージョンとサポート期間](https://linuxmint.com/download_all.php)

## エディションの選び方

| エディション | 特徴 | 向いている環境 |
| :--- | :--- | :--- |
| Cinnamon | Linux Mintの主力。機能が豊富で、Windowsからの移行でも操作を理解しやすい | 一般的な現行PC、Linux初心者 |
| MATE | GNOME 2系の流れを汲むクラシックなデスクトップ | 伝統的なUIを好む場合 |
| Xfce | 機能を絞った軽量デスクトップ | 比較的古いPC、リソース消費を抑えたい場合 |

Linux初心者が一般的な現行PCへ導入する場合は、特別な事情がなければCinnamonから検討すると分かりやすいです。ただし、実機との相性や好みがあるため、USBから起動したLive環境で画面表示、Wi-Fi、音声、Bluetooth、Webカメラなどを確認してから導入します。

### ブラウザでLinuxを試す（DistroSea）

[DistroSea](https://distrosea.com/) は、Linux Mintを含むさまざまなLinuxディストリビューションを、ブラウザ上で実際に起動して操作できるサービスです。PCへインストールせずに、デスクトップの見た目や基本操作を比較できます。手元のPCとの互換性や実機での動作は確認できないため、導入前にはLive USBでも確認してください。

## ハードウェア要件と実用上の目安

Linux Mint 22.3の公式要件は、**2 GB RAM（快適利用には4 GB推奨） / 20 GBストレージ（100 GB推奨） / 1024×768以上の画面解像度**です。

実際の快適性は用途で変わります。Webブラウザの多タブ利用、動画視聴、Office作業などを日常的に行うなら、RAM 8 GB以上とSSDを備えたPCの方が余裕があります。CPU、GPU、Wi-Fi、Bluetooth、USB、Webカメラ、指紋認証などは機種ごとにLinux対応状況が異なるため、購入前にメーカー情報やLinux Mint / Ubuntuでの実績を確認します。

NVIDIA GPUを使う場合は、導入後に **Driver Manager** で利用可能なドライバーを確認します。Linux Mint 22.2 / 22.3は新しいハードウェア向けにHWEカーネルを採用していますが、Linux Mint 22.3の公式リリースノートでは、古いNVIDIA 470ドライバーなど一部環境との互換性問題が案内されています。該当する場合は、LTSカーネルを採用するLinux Mint 22.1から導入する回避策が示されています。

* [Linux Mint 22.3のリリースノート](https://linuxmint.com/rel_zena.php)
* [ハードウェアドライバー](https://linuxmint-installation-guide.readthedocs.io/en/latest/drivers.html)

## Linux Mintを導入するPCの選び方

**機種名だけでなく、世代と部品構成まで確認します。** メーカーのUbuntu対応情報は有力な参考資料です。ただし、Ubuntu対応はLinux Mint公式認証を意味しません。カーネル（OSの中核）、ドライバー（機器を動かすソフト）、デスクトップ環境、パッケージの版やメーカー独自の調整が異なり、同じ結果になるとは限りません。

以下は「すべての機種で対応済み」という一覧ではなく、購入前に埋める確認表です。情報が見つからない機能は「未確認」として残し、販売店へ確認するか、実機で試せる条件を確保してください。

| 部品・機能 | 購入前に確認する内容 | 実機での確認 |
| :--- | :--- | :--- |
| CPU | 正確な型番とアーキテクチャ。通常版の64-bit PC向けISOを、Arm機へそのまま使えると判断しない | Live USBの起動と普段使うアプリ |
| 内蔵GPU / 外部GPU | 型番、複数GPUの有無、対応カーネル・ドライバー、Release Notesの既知の問題 | 解像度、明るさ、動画、外部画面。NVIDIAなどの追加ドライバーは導入後にも再確認 |
| Wi-Fi | 無線チップの型番と対応情報。同名PCでも選択構成が違わないか | 接続、通信、スリープ後の再接続 |
| Bluetooth | コントローラーの型番と必要な周辺機器との実績 | マウスやイヤホンの接続・復帰 |
| オーディオ | 音声チップ、スピーカー、イヤホン、マイクの対応 | 出力先の切替、録音、音量 |
| Webカメラ | カメラの方式・型番とLinux対応。搭載だけで動作保証とはしない | 映像とマイクを実際に使用 |
| タッチパッド | クリック、スクロール、必要なジェスチャーの対応 | 操作、誤反応、復帰後の動作 |
| キーボード | 日本語 / 英語配列、Fnキーや画面輝度キー | 記号、音量・明るさキーを確認 |
| USB | 必要な端子、ハブ、ドックの対応 | 手持ちの機器を接続 |
| HDMI / DisplayPort | 端子ごとの映像出力とUSB-C経由の出力条件 | 希望する解像度・リフレッシュレート、音声、抜き差し |
| 指紋認証 | センサーの型番とLinux側の対応。Windowsで使えることだけでは判断しない | Liveだけで判定できなければ未確認。使えない場合にパスワードで運用できるか |
| スリープ / 復帰 | その世代・BIOS・カーネルでの既知の問題 | 複数回試し、画面・無線・音声も復帰するか |
| バッテリー管理 | 充電・残量表示、消費電力、必要なら充電上限のメーカー対応 | AC接続 / 電池駆動、復帰後の消費。短いLive試用だけで駆動時間は保証できない |
| Secure Boot | 起動時の署名を検証する機能。機種のLinux向け手順・証明書設定 | まず現在の設定でUSB起動。必要性を確認せず無効化しない |
| UEFI | PCの起動方法を管理する仕組み。メーカーの起動メニュー手順と現在の起動モード | USBの起動項目を確認。Legacy / CSMへ一律変更しない |

候補の正確な構成はメーカー仕様表やサポートへ確認し、Linux Mintの [リリースノート](https://linuxmint.com/rel_zena.php) とメーカーの機種別資料を照合します。Ubuntuの認証を調べる場合も、 [Ubuntu Certified hardware](https://ubuntu.com/certified) の対象構成とUbuntuの版を確認してください。これは互換性を絞り込むための判断手順であり、本ガイドによる個別機種の動作保証ではありません。

### Lenovo製PCの確認手順

入口はLenovo公式の [個人向けシステム用Linux](https://lenovo.com/linux) です。この入口は [公式サポートの同資料（PD031426）](https://support.lenovo.com/us/en/solutions/pd031426) へ転送されます。 [日本語版の同資料（PD031426）](https://support.lenovo.com/jp/ja/solutions/pd031426) も参照できます。

> **確認上の制約**：今回、公式ページの転送先と日本語版URLを確認しましたが、取得できたページ本文には対応一覧が表示されず、ブラウザでは双方とも403（アクセス拒否）になりました。検索結果にはThinkPad、ThinkStation、その他のノートPC、Ubuntu、Fedora、Red Hat、SUSE等の記載が表示されましたが、一覧本文を確認できていません。個別機種・OSバージョン・掲載範囲は未確認であり、検索結果だけで対応機種を確定していません。提供された日本語ページの保存ソースも確認しましたが、本文データは空で、別のJavaScriptから読み込む構成でした。その公式ファイルもアクセス拒否となったため、保存ソースからも一覧を確認できていません。

一覧を開ける環境では、ThinkPad、ThinkStation、その他Lenovo製PCをそれぞれ探し、Ubuntu、Fedora、Red Hat Enterprise Linux（RHEL）、その他のLinuxの**どの版・構成が対象か**を読みます。ブランド全体や、他のLinuxの掲載をUbuntu対応へ読み替えないでください。空欄・未掲載だけを根拠に「動かない」と断定することもできません。

1. Lenovo公式Linux対応一覧で、候補の機種名・世代・Intel / AMD等の違いを確認する。
2. **Ubuntu対応の有無とバージョン**を確認し、リンク先の制約も読む。本文を開けなければ「未確認」にする。
3. 購入する構成のCPU、GPU、Wi-Fi、カメラ等が対象構成と一致するか確認する。
4. Linux MintのRelease Notes、UbuntuとLenovoの機種別資料で既知の問題を確認する。Issueや利用者の報告は、公式対応とは区別して読む。
5. 購入後は、インストール前にLive USBで必須機能を試す。購入前に試せない場合は、返品条件も先に確認する。
6. 問題がなく、バックアップと回復手段も用意できたらインストールする。

**Lenovo公式ページでUbuntu対応を確認できたThinkPadは、Linux Mint導入候補を絞る有力な材料になります。** これはUbuntuとの共通基盤からの合理的な判断であり、LenovoによるLinux Mintの認証・サポートや、全機能の動作確認を示すものではありません。ThinkStationや他シリーズにも同じ区別が必要です。

Lenovoには [Secured-core PCでLinux用のSecure Bootを有効にする公式資料](https://download.lenovo.com/pccbbs/mobiles_pdf/Enable_Secure_Boot_for_Linux_Secured-core_PCs.pdf) もあります。該当機種では第三者UEFI CAの許可設定が関係する場合がありますが、全機種への一括設定手順ではありません。購入機種の最新マニュアルと適用条件を確認してください。

## Linux Mint搭載済みPC

Linux Mint公式は、ハードウェア関連のパートナーとして **Framework** と **ThinkPenguin** を掲載しています。FrameworkについてはLinux Mint開発チームが実機テストを行い、互換性改善にもつながっていることが公式ブログで説明されています。

* [Linux Mintのパートナー](https://linuxmint.com/partners.php)
* [Linux Mintブログ：2025年5月の月例ニュース](https://blog.linuxmint.com/?p=4850)
* **[RayLink Inc（レイリンク株式会社）](https://raylink-inc.com/)** ：Ubuntu搭載の新品・再生PCやLinux関連機器を販売する国内事業者。Linux OSのインストール代行も提供し、[取扱ディストリビューション](https://raylink-inc.com/distribution/) にはLinux Mintも掲載している。Linux Mint搭載を希望する場合は、対象機種・導入可能な版・費用を購入前に相談する。
* [Ubuntu Laptop](https://raylink-inc.com/product-category/new-laptop/)
* **[Star Labs](https://jp.starlabs.systems/)** ：Linux向けに設計されたノートPCやMini PCを販売するメーカー。Linux Mintを含む複数のLinuxディストリビューションを、対応カーネル上で標準ISOから導入できる。

ただし、Linux Mintが「公式認定した完成品PC一覧」を常時提供しているわけではありません。日本から海外メーカー製PCを購入する場合は、Linux Mintプリインストールの有無だけでなく、送料、関税、保証対応、修理時の発送先、ACアダプター、キーボード配列、無線チップなども確認してください。販売状況は変化するため、購入時点でメーカー公式ページを確認します。

### Ubuntu Laptopを調達してLinux Mintへ換装する場合

[ChatGPT](https://chatgpt.com/ja-JP/) に手順を聞きながら、[RayLinkのUbuntu Laptop](https://raylink-inc.com/product-category/new-laptop/) を調達し、[Linux Mint](https://linuxmint.com) へ換装する進め方もあります。

1. **ChatGPTで手順を確認する**：購入前は用途と候補機種、購入後は正確な機種名・部品構成・Ubuntuのバージョンを伝え、準備から導入までの手順を一段階ずつ確認します。回答はLinux Mint公式のInstallation Guideやメーカーの機種別資料と照合します。
2. **Ubuntu Laptopを調達する**：上記のRayLinkの商品一覧を入口に、仕様、Ubuntuの搭載状況、OS換装後の保証・サポート条件を販売店へ確認します。Ubuntu搭載でもLinux Mintの全機能が動くとは限らないため、本ガイドの「Linux Mintを導入するPCの選び方」も確認してください。
3. **Linux Mintへ換装する**：必要な個人データをバックアップし、元のUbuntuへ戻すためのインストールメディアやメーカー固有の復旧手順を確保します。Linux Mint公式サイトからISOを入手し、検証・USB作成、Live USBでの動作確認を経て、導入先と消去範囲を確認してインストールします。具体的な操作は、以下の「インストール前の安全対策」「Live USBでインストール前に試す」「Linux Mintのインストール」の順に進めます。

Ubuntuを置き換える場合、ディスクの消去によって既存のUbuntuや個人データも失われます。ChatGPTへ相談しながら進める場合も、内容が分からないコマンドやディスク操作は実行せず、対象と変更内容を確認してから進めてください。

## インストール前の安全対策

**OSの入れ替えは、Windows上にアプリを追加する作業とは違います。** ディスクを消去すると、Windows、回復領域、写真・文書などを失う場合があります。まず次の準備を済ませましょう。

### 重要ファイルとWindowsの回復手段

* 文書、写真、デスクトップ、ダウンロード等を外付けストレージなど別の媒体へコピーし、数個のファイルを開いて確認します。クラウド上だけにあるファイルと、PC内だけにあるファイルを区別してください。
* ブラウザのブックマーク、必要なアプリのデータ、アカウントの回復方法も確認します。パスワードや回復コードは公開ログや生成AIへ貼り付けません。
* Windowsへ戻す可能性があれば、動いているうちに回復ドライブやメーカーの回復メディアを準備します。Windowsの再インストールと個人ファイルの復元は別です。アプリや設定まで元どおりに戻るとは限りません。
* Microsoftの [Windowsの回復オプション](https://support.microsoft.com/ja-jp/windows/experience/backup-recovery/recovery-options-in-windows) から回復ドライブ / 再インストール手順を確認します。メーカーの回復イメージには独自ドライバー等が含まれる場合があるため、機種別の回復手順も保管します。
* 回復用USBとLinux Mint用USBは分け、内容を書いたラベルを付けます。回復メディアの起動確認では、再インストールや消去を開始しないでください。

### BitLockerとWindows高速スタートアップ

BitLocker / デバイスの暗号化はWindowsのデータを暗号化する機能です。Windowsの設定で状態を確認し、**設定変更より先に回復キーをPC外へ保存し、別端末から参照できることを確かめます。** Microsoftは失われた回復キーを再作成できないと説明しています。 [BitLocker回復キーの公式案内](https://support.microsoft.com/ja-jp/windows/security/encryption/find-your-bitlocker-recovery-key) を参照してください。

回復キーの保存、「保護の一時停止」、暗号化の解除は別の操作です。Windowsとの併用や既存領域の変更を予定していて、インストーラーが暗号化を警告した場合は先へ進まず、その表示を確認します。Ubuntuにも [BitLocker併用時の注意](https://ubuntu.com/desktop/docs/en/latest/reference/bitlocker-during-ubuntu-installation/) がありますが、Ubuntuの画面や手順をLinux Mintと同一とは扱いません。Windowsを全消去する場合でも、必要なファイルを退避する前に消去してはいけません。

高速スタートアップは、Windowsの終了時に一部の状態を保存して次回起動を速める仕組みです。通常の完全終了とは異なります（ [Microsoftの電源状態の説明](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states) ）。Windowsを残して領域を共用する場合は、設定を確認し、高速スタートアップを無効にして終了する運用を検討します。休止中のWindows領域へLinuxから書き込む運用は避けてください。設定項目は一般にコントロールパネルの「電源オプション」→「電源ボタンの動作を選択する」にあります。表示はWindowsの版やPCによって異なります。

### UEFI・Secure Boot・BIOS設定

UEFIはPCの起動を管理する仕組み、BIOSは従来の仕組みを指しますが、設定画面をまとめて「BIOS」と呼ぶ場合もあります。Secure Bootは起動用ソフトの署名を検証する機能です。**まず現在の設定でUSB起動を試し、起動できるなら不要な変更をしません。** 起動メニューのキーはメーカー・機種の公式マニュアルで確認してください。

USB起動のためだけに、Legacy / CSMへの切替、ストレージのRAID / AHCI変更、TPMの初期化、Secure Boot鍵の消去などをまとめて行わないでください。変更が必要と分かった場合も、現在の値を写真に残し、BitLocker回復手段とメーカーの戻し方を確認してから、必要な項目だけを変更します。

`Secure Boot Violation` が出た場合のLinux Mint公式の案内は、後述のEFI / SecureBootを参照してください。公式ガイドにある無効化は特定の起動障害への対処候補であり、全PCで事前に必要という意味ではありません。Lenovoの第三者UEFI CA設定も機種限定の資料として参照し、証明書設定を無条件に変えないでください。

### ISOの検証とUSB作成

ISOはインストール用のディスク内容をまとめたファイルです。**整合性**はダウンロード破損がないこと、**真正性**はLinux Mintが署名した配布物であることを確認します。ハッシュ値の一致だけで、真正性まで確認したことにはなりません。

1. 公式ダウンロードページからCinnamonのISOと、同じ配布物の `sha256sum.txt`、`sha256sum.txt.gpg` を取得します。
2. [公式の検証手順](https://linuxmint-installation-guide.readthedocs.io/en/latest/verify.html) に従い、署名鍵のフィンガープリント、チェックサム一覧の署名、ISOのSHA256の一致を確認します。Linux Mint上ではISOの右クリックから「Verify」を使えます。Windowsでの検証は同ページから案内されるWindows用手順を使い、OSの違うコマンドをそのまま貼り付けないでください。
3. 一致しない・署名を確認できない場合はインストールへ進まず、取得元とファイルを確認します。
4. [公式USB作成手順](https://linuxmint-installation-guide.readthedocs.io/en/latest/burn.html) に従います。Windows等では公式ガイドが案内するEtcher、Linux MintではUSB Image Writerを利用できます。

> **USB作成時も消去に注意**：ISOをUSBへ単にコピーする操作とは異なり、選択したUSBの内容を書き換えます。不要な外付けドライブは外し、容量・機器名で対象を確認してください。バックアップ用ディスクやWindows回復用USBを選ばないようにします。

ChromeOSだけで準備する場合、上記のWindows向け手順をそのまま利用できるとは限りません。本ガイドではChromeOSでのUSB作成・署名検証手順を実機確認していません。利用できる作成環境を確保してから進めてください。

## Live USBでインストール前に試す

Live USBは、内蔵ディスクへLinux Mintをインストールする前に、USBから起動して操作できる試用環境です。 [公式の起動手順](https://linuxmint-installation-guide.readthedocs.io/en/latest/boot.html) に沿ってUSBを挿し、再起動時の起動メニューから選択します。最初は **Install Linux Mintを起動せず**、次の表を確認してください。

| 確認 | 試すこと | 結果の記録 |
| :--- | :--- | :--- |
| 起動 | デスクトップまで進み、再起動できる | 正常 / 問題あり / 未確認 |
| 画面 | 解像度、拡大率、明るさ、動画表示 | 同上 |
| Wi-Fi | 自宅の回線へ接続してWebを開く | 同上 |
| Bluetooth | 手持ちの機器を接続して操作 | 同上 |
| 音声出力 | 内蔵スピーカー・イヤホンで再生 | 同上 |
| マイク | 音声設定で入力を確認し、必要なら録音して再生 | 同上 |
| Webカメラ | カメラ対応アプリ等で映像を確認 | 同上 |
| タッチパッド | クリック、スクロール、必要な操作 | 同上 |
| キーボード | 日本語 / 英語配列、記号、Fnキー | 同上 |
| USB | マウス、USBメモリ、必要なハブ・ドック | 同上 |
| 外部画面 | HDMI / DisplayPort / USB-Cで実際の画面を接続 | 同上 |
| スリープ / 復帰 | 作業を保存し、スリープ後に復帰。無線・音・画面も再確認 | 同上 |
| 電源 | AC / バッテリーの切替と残量表示 | 同上 |

USBからの試用は内蔵SSDより遅く、通常のLive環境の設定変更は再起動後に残りません。一部アプリや追加ドライバーも導入後と条件が異なります（ [公式のLiveセッションの説明](https://linuxmint-installation-guide.readthedocs.io/en/latest/install.html) ）。長時間の電池持ちや指紋認証を含め、すべてを保証できるテストではありません。

Live環境でも内蔵ディスクを開いたり、ディスク管理ツールを操作したりすればデータを変更できるので、試用だけならフォーマット・修復・パーティション変更を行わないでください。必須機能に問題があれば、症状と機種・ISOの版を記録して導入を保留します。試用を終えて元のOSへ戻るときは、シャットダウンしてUSBを外し、起動し直します。

## Linux Mintのインストール

Linux Mint公式のInstallation Guideでは、ISOの入手、真正性・整合性確認、USBメディア作成、Live起動、インストール、ドライバー確認、Timeshift設定まで一連の手順が案内されています。

1. [Linux Mint公式サイト](https://linuxmint.com/download.php) から使用するエディションのISOを入手する。
2. `sha256sum.txt` と署名を利用し、ISOの整合性と真正性を確認する。
3. USBメモリへISOを書き込み、起動可能なインストールメディアを作成する。
4. USBからLinux MintをLive起動し、画面、Wi-Fi、音声、Bluetooth、USB機器などを確認する。
5. デスクトップ上の **Install Linux Mint** を起動する。
6. 言語、ネットワーク、必要に応じてマルチメディアコーデックを設定する。
7. インストール方式とディスク構成を確認する。
8. ユーザー名、パスワードなどを設定してインストールする。
9. 再起動後にUpdate ManagerとDriver Managerを確認する。
10. Timeshiftを設定して復旧用スナップショットを作成する。

* [Linux Mintのインストールガイド](https://linuxmint-installation-guide.readthedocs.io/en/latest/)
* [ISOイメージの検証](https://linuxmint-installation-guide.readthedocs.io/en/latest/verify.html)
* [起動メディアの作成](https://linuxmint-installation-guide.readthedocs.io/en/latest/burn.html)
* [Linux Mintの起動](https://linuxmint-installation-guide.readthedocs.io/en/latest/boot.html)
* [Linux Mintのインストール](https://linuxmint-installation-guide.readthedocs.io/en/latest/install.html)

> **❗️注意**：`Erase disk and install Linux Mint` は対象ディスク上の既存データを消去します。パーティション変更、既存OSとのデュアルブート、暗号化設定を行う場合は、先に重要ファイルを別媒体へバックアップしてください。Windowsと併用する場合は、BitLockerやWindows側の高速スタートアップ、EFI / Secure Bootの設定も事前に確認します。

Secure Bootで起動できない場合について、Linux Mint公式ガイドはインストール条件の見直しやBIOS/UEFI側でSecure Bootを無効化する方法を案内しています。安易に設定を変更せず、機種の公式手順を確認してください。

* [EFI・セキュアブート](https://linuxmint-installation-guide.readthedocs.io/en/latest/efi.html)

### インストーラーで迷いやすい操作

次の表は上記手順の補足です。電源アダプターを接続し、バックアップ先の外付けディスクは外してから開始します。

| 操作順 | 先に理解すること・画面での確認 |
| :--- | :--- |
| Install Linux Mintを開く | インストールの設定を開始する。試用を続けるだけなら開く必要はない |
| 言語とネットワーク | 表示言語を選び、必要なダウンロードのため接続する |
| コーデック | 一部の音声・動画を再生する追加ソフト。必要なら選択する |
| インストール方式 | 「ディスク消去」「既存OSと併用」「手動設定」は影響が違う。目的に一致するものだけを選ぶ |
| ディスク変更の確認 | 対象ディスクの機器名・容量と、消去 / 作成される領域を読む。分からなければ確定しない |
| タイムゾーン・配列 | 日本の時刻と、実際のキーボード配列を選び、入力欄で記号も試す |
| ユーザー設定 | ユーザー名・PC名・強いパスワードを設定し、復旧時に必要な情報を保管 |
| 完了・再起動 | 完了表示を待ち、USBを外す指示に従う。USBを外した状態で起動確認 |

> **消去前の最終確認**：`Erase disk and install Linux Mint` は「Windowsを残したまま試す」選択肢ではありません。選択したディスクの既存OS・個人ファイル・回復領域を失う操作です。**バックアップを開けること、Windowsの回復手段、対象ディスク**の3点を確認できるまで確定しないでください。

既存OSとの併用も領域を変更する操作です。併用の選択肢が出ない場合に、代わりに消去を選ばないでください。`Something else` はパーティション（ディスク内の区画）を手動設定する方式です。各領域の用途を説明できない段階では選ばず、画面を記録して相談します。

暗号化は盗難時のデータ保護に役立ちますが、解除用の情報を失えば読めなくなる場合があります。全ディスク暗号化とホーム暗号化は異なり、公式インストールガイドとRelease Notesにも配列・ドライバー・ログアウト時の制約が記載されています。一律に選ばず、対象版の注意と、Live USBでの解除・復旧方法を確認してから決めてください。

## インストール直後の推奨設定

| 優先度 | 項目 | 内容 |
| :--- | :--- | :--- |
| 必須 | Update Manager | OS・アプリ・セキュリティ更新を適用する |
| 必須 | Driver Manager | GPUやWi-Fiなどに追加ドライバーが必要か確認する |
| 推奨 | Timeshift | 更新や設定変更に備えてシステムスナップショットを作成する |
| 推奨 | 言語・日本語入力 | 日本語表示・入力環境を確認する |
| 推奨 | Software Manager | GUIからアプリを安全に導入する基本手段として利用する |
| 推奨 | 個人ファイルのバックアップ | Timeshiftとは別に、文書・写真などを外付けストレージ等へ保存する |
| 必要な場合のみ | Multimedia Codecs | インストール時に導入していない場合に追加する |
| 必要な場合のみ | Firewall | ネットワーク利用形態に応じて設定を確認する |

Linux Mintは更新時の不具合から戻せるよう、TimeshiftによるシステムスナップショットをUpdate Managerと組み合わせて利用することを推奨しています。

* [アップデートマネージャー](https://linuxmint-user-guide.readthedocs.io/en/latest/mintupdate.html)
* [マルチメディアコーデック](https://linuxmint-installation-guide.readthedocs.io/en/latest/codecs.html)

### 最初に行う作業の順番

上の表は必要度の一覧です。実際には次の順に進めると確認しやすくなります。GUIのアプリ名はメニューの検索欄からも探せます。

1. **Timeshift**を起動し、保存先と空き容量を確認して最初のスナップショットを作ります。OSの更新・設定から戻る準備です。作成が完了し、一覧に日時が表示されることを確認してから更新へ進みます。詳細は後述します。
2. **Update Manager（アップデートマネージャー）**を開き、更新内容を確認して適用します。更新は不具合・脆弱性を直すために必要です。初回を含め、更新前にTimeshiftのスナップショットを用意してください。再起動の案内が出たら、作業を保存して再起動します。
3. **Driver Manager（ドライバーマネージャー）**を開きます。追加ドライバーの要否を確認する作業で、全員が何かを追加する必要はありません。変更が必要な場合だけ適用し、指示に従って再起動します。ネット未接続時は公式ガイドのUSB利用手順も参照します。
4. **日本語表示と入力**を確認します。Languagesで不足する言語パックを確認し、入力方法 / キーボード設定で日本語入力を設定します。文字入力アプリで「日本語」と打ち、変換・切替・記号を試してください。Cinnamon 6.6ではIBus入力方式の統合とMozcによる日本語入力例が公式に説明されています。既存の入力方式が使えているなら、別方式を重ねて入れる必要はありません。
5. **個人ファイルのバックアップ**を用意し、ファイルを1つ戻して開けるか試します。Timeshiftを設定しても、この作業は必要です。
6. **Software Manager（ソフトウェアマネージャー）**から必要なアプリだけを導入します。最初から大量に追加せず、1つずつ起動を確認します。
7. **Multimedia Codecs**は、未導入で必要な場合にメニューから追加します。インストール時に導入済みなら繰り返す必要はありません。
8. **Firewall（ファイアウォール）**は通信の許可・拒否を管理します。使用する共有機能や接続先に合わせて状態を確認し、不要なポート開放を避けます。変更後にプリンターや共有が使えなくなった場合は、無条件に保護を切らずルールを見直してください。

* [公式：言語サポート](https://linuxmint-installation-guide.readthedocs.io/en/latest/locales.html)
* [公式：22.3の入力方法・System Information等の変更](https://linuxmint.com/rel_zena_whatsnew.php)
* [Ubuntu Wiki：UFWとGUIのGufw](https://wiki.ubuntu.com/UFW)

## 日常利用の基本

メニューからアプリを検索して起動し、ファイルマネージャーでホームフォルダー内の文書・写真等を管理します。最初に、文書を作成して保存し、閉じてからもう一度開くところまで試しましょう。外付けストレージはコピー完了を待ち、取り外し / アンマウントしてから抜きます。

Windowsで使っていたアプリは、Linux版やWeb版の提供元を確認してください。Windows用インストーラーがそのまま動くとは限りません。Office文書やプリンター、オンライン会議など、必要な用途を実際のファイル・機器で試し、問題がないことを確かめてから本格的に移行します。

設定変更は一度に1項目にとどめ、変更前の値を残します。管理者パスワードを求められたら、その操作が何を変更するのかを確認してください。普通の文書作成や閲覧で、常時管理者権限を使う必要はありません。

## アプリケーション管理

Linux Mintでは複数の配布方式があります。目的や配布元を確認し、必要以上に方式を混在させない方が管理しやすくなります。

| 方式 | 概要 | 注意点 |
| :--- | :--- | :--- |
| Software Manager | GUIからアプリを検索・導入する | 初心者が最初に使いやすい |
| APT | Ubuntu / Linux Mint系のパッケージ管理 | システムと統合しやすい |
| Flatpak / Flathub | アプリを比較的独立した環境で配布 | 容量や権限モデルがAPTと異なる |
| .deb | Debian系パッケージを直接導入 | 配布元の信頼性と依存関係を確認する |
| AppImage | 単体ファイルとして実行する方式 | 自動更新やシステム統合はアプリごとに異なる |

同じアプリが複数方式で提供される場合、公式配布元、更新頻度、サンドボックスの必要性、ディスク容量、テーマ統合などを比較して選びます。「常にAPT」「常にFlatpak」のように一律で決める必要はありません。

### GUIから入れ、更新方法まで確認する

Software Managerは配布形式そのものではなく、アプリを探して導入するための窓口です。検索してアプリの説明・配布元・形式を確認し、インストール後にメニューから起動します。同じ名前でも別形式のものを重ねて入れると、起動項目や設定を取り違える場合があるため、導入した形式を記録してください。

| 比較点 | APTのRepositoryパッケージ | Flatpak / Flathub | 配布元から直接入れる .deb | AppImage |
| :--- | :--- | :--- | :--- | :--- |
| 信頼性 | 有効なRepositoryの管理元を確認 | 配布者と権限を確認。Flathub掲載だけで無条件に安全とはしない | 本物の開発元・対応するOS版を確認 | 本物の開発元・取得元を確認 |
| 更新・保守 | 設定済みの配布元から更新を受ける | Flatpak側の更新も確認 | 更新用Repositoryを追加する製品と、手動で更新する製品がある | アプリ内更新や対応ツールの有無は製品ごとに違う |
| 権限・隔離 | 通常のパッケージ形式だけではサンドボックスを保証しない | サンドボックスを利用。ただしホーム全体など広い権限なら隔離範囲は弱まる | インストール処理がシステムを変更し得る。形式だけでは隔離されない | 単体ファイルというだけで隔離・安全を保証しない |
| 容量・統合 | システムのライブラリを共用しやすい | ランタイム等が容量を使う。アクセス権・連携に違いがある | 依存関係や他パッケージとの互換性を確認 | 依存物の同梱、メニュー登録、実行条件は製品ごとに違う |

初心者はSoftware Managerから始め、見つからない場合に開発元の公式Linux向け案内を確認します。APTの端末操作、外部Repository / PPAの追加は、更新と信頼の範囲を理解してから行ってください。容量・起動速度・テーマとの統合はアプリによって異なるため、配布方式だけで優劣は決められません。

* [Linux Mint公式：Software Managerのソース](https://github.com/linuxmint/mintinstall)
* [Ubuntu公式manpage：APT](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html)
* [Flatpak公式：サンドボックスと権限](https://docs.flatpak.org/en/latest/sandbox-permissions.html)
* [AppImage公式：基本的な使い方](https://docs.appimage.org/introduction/quickstart.html)

## 更新を続ける

日常の更新はUpdate Managerを基本にし、適用後は普段使う機能を確認します。カーネルやドライバーの変更前には、正常なTimeshiftスナップショット、個人ファイルのバックアップ、Live USBを用意します。更新を避け続ける代わりに、問題が出たときに戻れる準備をします。

カーネルはUpdate Managerの「View → Linux Kernels」で確認できます。通常の更新と、別のカーネル系列へ切り替える操作は区別してください。新しければ必ず互換性が高いとは限りません。旧カーネルで戻れることを確認する前に、正常に動いていたものを手動削除しないでください。

メジャーバージョンの更新は日常の更新と別に、対象版の公式アップグレード手順を確認して行います。 [公式User Guideの更新案内](https://linuxmint-user-guide.readthedocs.io/en/latest/upgrade.html) から該当する経路を探します。

## Timeshiftとバックアップ

[Timeshift](https://github.com/linuxmint/timeshift) は、Windowsの「システムの復元」に近い目的を持つシステムスナップショットツールです。RSYNCモードではrsyncとハードリンク、BTRFSモードではBTRFSのスナップショット機能を利用します。

Linux Mintは、Timeshiftで**日次スナップショットと起動時スナップショットを自動化することを推奨**しています。

主な使い方：

1. Timeshiftを起動する。
2. RSYNCまたはBTRFSモードを選択する。
3. 保存先を確認する。
4. 手動スナップショットを作成する。
5. 必要に応じてHourly / Daily / Weekly / Monthly / Bootのスケジュールを設定する。
6. システム更新や設定変更後に不具合が起きた場合は、正常だった時点のスナップショットから復元する。
7. OSが正常起動しない場合は、Linux Mint Live USBから起動して復元を試す。

BTRFSモードはUbuntu系の `@` / `@home` サブボリューム構成など、対応条件があります。通常のEXT4構成ではRSYNCモードを利用します。

> **重要**：Timeshiftは、文書・写真・動画などのユーザーファイルを保護する通常のバックアップツールではありません。ユーザーファイルは既定で除外されます。個人データは別途、外付けSSD/HDD、NAS、クラウド等へバックアップしてください。

### 2種類の保護を用意する

| 目的 | 用意するもの | 戻す対象・注意 |
| :--- | :--- | :--- |
| 更新や設定でOSが壊れた | Timeshiftのシステムスナップショット | システムの以前の状態。個人ファイルの世代管理の代わりにはしない |
| 文書・写真の誤削除、故障、紛失 | PCとは別の媒体への個人データバックアップ | 必要なファイル。クラウド同期だけでは誤削除も同期される場合があるため、履歴・復元方法を確認 |
| Windowsへ戻したい | Windows回復メディアと個人データのバックアップ | Windowsの再導入とファイルの復元。LinuxのTimeshiftだけでは代替できない |

Timeshiftでは、通常のEXT4構成なら公式ガイドが案内するRSYNCから始め、保存先とスケジュールを確認します。最初の作成が完了し、一覧に日時が表示されることを確かめてください。BTRFSへ変更するためだけに、ディスクを再フォーマットする必要はありません。

同じ内蔵ディスクにあるスナップショットだけでは、そのディスク自体の故障に備えられません。別媒体も検討し、保存先の対応ファイルシステムと空き容量を確認してください。Timeshift用に新たにフォーマットする場合は、その媒体の既存データを失います。保存先を選ぶ操作とフォーマットを混同しないでください。

個人ファイルは、最初はファイルマネージャーで文書・写真等を別媒体へコピーする方法でも構いません。定期的に保存し、複数世代を残す運用を検討します。「保存できた」だけで終えず、別の場所へ1ファイル戻して開けるかを試します。保存先と復元手順はPC外にもメモしておきます。

* [Linux Mint公式：システムスナップショットの設定](https://linuxmint-installation-guide.readthedocs.io/en/latest/timeshift.html)
* [Timeshift公式：除外対象・復元・保存先の条件](https://github.com/linuxmint/timeshift)

## セキュリティと保守

Linux Mintを安定して使うには、特別な「最適化」よりも、更新、バックアップ、信頼できる配布元、権限管理を基本にします。

* Update ManagerでOS・アプリ・セキュリティ更新を継続する。
* Driver Managerを利用し、必要なプロプライエタリドライバーを公式手順で導入する。
* ソフトウェアはSoftware Manager、公式Repository、公式配布元を優先する。
* `sudo` は管理者権限を与えるため、コマンド内容を確認してから実行する。
* Web上の不明なScriptやコマンドを、そのままコピー＆ペーストして実行しない。
* Timeshiftでシステム復元ポイントを用意する。
* Timeshiftとは別に個人ファイルをバックアップする。
* Secure Boot、ディスク暗号化、ファイアウォールはPCの用途と脅威モデルに応じて設定する。
* 大きなカーネル更新やドライバー変更の前後は、復旧手段を確認しておく。

Linux Mintの公式ドキュメントは、Installation Guide、User Guide、Troubleshooting Guideに分かれています。トラブル時は検索結果だけで判断せず、まず公式ドキュメントと公式リリースノートを確認してください。

* [Linux Mintのドキュメント](https://linuxmint.com/documentation.php)

## トラブルシューティングと復旧

Linux Mintで問題が発生した場合は、最初から再インストールするのではなく、症状・直前の変更・ハードウェア・ログを段階的に切り分けます。

### GUIで確認し、状況を記録する

1. ネットワーク、音声、画面等の設定画面と、System Informationで状況を確認します。更新直後ならUpdate Managerの履歴、機器の問題ならDriver Managerも確認します。
2. エラー文、発生日時、再現操作、直前の変更を記録します。再起動する前に、表示を写真等に残してください。
3. GUIだけで原因が分からず、調査に必要な場合に限って、以下の情報表示コマンドを使います。エラーが出たからといって、直ちに管理者権限を追加したり設定変更したりしません。

[Linux Mint公式Troubleshooting Guide](https://linuxmint-troubleshooting-guide.readthedocs.io/en/latest/) も、観察、再現性、環境、変更内容を確認するための資料です。

| コマンド | 主な用途 |
| :--- | :--- |
| `journalctl` | systemdのシステムログを確認する |
| `dmesg` | カーネル・デバイス・ドライバー関連のメッセージを確認する |
| `systemctl` | systemdサービスの状態確認・管理 |
| `inxi -Fxxxz` | OS、カーネル、CPU、GPU、ネットワーク等のシステム情報をまとめて確認する |

次の例は**情報を表示するため**のものです。4つすべてを毎回実行する必要はありません。

| 調べたいこと | 情報表示の例 | 変更の有無・注意 |
| :--- | :--- | :--- |
| 今回の起動のシステムログ | `journalctl -b` | 表示のみ。以前の起動の記録が残っているとは限らない。閲覧終了は `q` |
| カーネルや機器のメッセージ | `dmesg` | 引数なしなら表示。権限で読めない場合もある。クリア等のオプションを付けない |
| 失敗扱いのサービス | `systemctl --failed` | 状態表示。失敗表示だけで原因と断定しない |
| 機器・OSの概要 | `inxi -Fxxxz` | 情報表示。一部を伏せるが、完全な匿名化は保証しない |

`systemctl` は状態確認だけでなく、`start`、`stop`、`enable`、`disable` などでサービスを変更できるコマンドです。`journalctl` にもログ削除等のオプションがあります。**同じコマンド名でも引数によって作用が違います。** 上の表示例と、ネット上の修復コマンドを混同しないでください。

ログを送るときは必要な範囲に絞り、ユーザー名、ホスト名、IP、SSID、メールアドレス、パス、シリアル、認証情報等を目で確認して伏せます。写真にも個人情報が写っていないか確認してください。

* [systemd公式：journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
* [systemd公式：systemctl](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
* [util-linux：dmesgのマニュアル](https://man7.org/linux/man-pages/man1/dmesg.1.html)
* [inxi開発元：ドキュメント](https://smxi.org/docs/inxi.htm)

代表的な確認順序：

1. エラー表示や症状をそのまま記録する。
2. 問題発生直前に行った更新、ドライバー変更、アプリ導入、設定変更を確認する。
3. Update Manager、System Information、Driver ManagerなどGUIの情報を確認する。
4. 必要に応じて `journalctl`、`dmesg`、`systemctl`、`inxi` の結果を確認する。
5. 直前の更新が原因と考えられる場合は、GRUBから以前のカーネルで起動できるか確認する。
6. 起動できない場合はLive USBでデータ保全やTimeshift復元を試す。

Linux Mint 22.3では「System Reports」が「System Information」に改称・強化され、ハードウェアやドライバーの切り分けに役立つ情報が追加されています。

生成AIへログを提示する場合は、ユーザー名、ホスト名、IPアドレス、SSID、ファイルパス、シリアル番号などが含まれていないか確認してください。`inxi` の `-z` オプションは一部のセンシティブ情報を伏せるために役立ちます。

また、生成AIが提示したコマンドを意味を理解せず実行しないでください。特に `sudo`、`rm`、`dd`、パーティション操作、ファイルシステム操作、ブートローダー変更、カーネル変更、ドライバー変更は、誤ると起動不能やデータ消失につながる可能性があります。

### 起動しなくなったときの復旧経路

GRUBは、OSやカーネルを選んで起動するメニューです。以下は、むやみに修復コマンドを実行する前の判断手順です。

| 状態 | 次にすること | 止まる条件 |
| :--- | :--- | :--- |
| 更新後に起動しないがGRUBを開ける | Advanced options for Linux Mintから、以前に正常だったカーネルを選んで起動 | 旧カーネルがなければこの方法は使えない |
| GRUBが表示されない | 公式User Guideの表示手順を参照。22.3では正常時にSystem AdministrationのBoot menuで表示設定もできる | 起動項目や設定が不明ならGRUB編集・再インストールを始めない |
| 通常起動できない | 作成しておいたLive USBを、導入時と同じ起動モードで起動 | USBも起動しない場合は、媒体・機器・メーカー設定から再確認 |
| 内蔵ディスクとファイルを読める | ファイルマネージャーで重要データを別媒体へコピーし、開けるか確認 | 暗号化を解除できない、読み取りエラー、故障が疑われる場合は無理に修復しない |
| 正常なスナップショットがある | Live環境のTimeshiftから保存先と日時を選び、復元先・変更内容を確認して復元 | 保存先が見つからない、復元先を識別できない場合は確定しない |
| 復旧できた | 更新履歴・ドライバー・ログを確認し、原因を切り分ける | 同じ変更をまとめて再適用しない |

**Timeshiftの復元はシステムを書き換える操作**です。重要ファイルの退避を先に済ませ、Live環境のファイルマネージャーやTimeshiftに表示される容量・領域名を確認します。初回設定ウィザードが出ても、正常な既存スナップショットを探しているのか、新規作成しようとしているのかを区別してください。ディスクを初期化して見つけ直そうとしてはいけません。

TimeshiftをLive環境から使う場合の条件は [開発元の復元説明](https://github.com/linuxmint/timeshift) を確認します。公式ガイドもLive環境では一部アプリの挙動が通常環境と異なると説明しています。暗号化や特殊なパーティション構成は、本ガイドの一般手順だけで復元できるとは保証しません。

スナップショットがなくても、個人データを退避できる場合があります。再インストールやWindows回復メディアによる消去は、退避と回復方法を確認してから最後に検討してください。

### 意味の分からない修復コマンドは実行しない

Web検索や生成AIの回答が、そのPC・OSの版・ディスク構成に適しているとは限りません。次の操作を提案されたら、対象、変更内容、戻し方を説明できるまで実行を保留してください。

| 操作・コマンド | 理解しておくこと |
| :--- | :--- |
| `sudo` | 管理者権限で実行する。入力するパスワードが画面に出ないことがあっても、内容不明の操作を承認しない |
| `rm` | ファイル削除。ゴミ箱から戻せると考えない。対象・オプションを確認 |
| `dd` | コピー先を間違えるとディスク内容を上書きする。初心者のUSB作成はGUIを優先 |
| パーティション・ファイルシステム操作 | 消去、サイズ変更、フォーマット、修復にはデータ損失の可能性がある |
| GRUB変更 | 起動設定を変える。別PCの設定・ディスク名を流用しない |
| カーネル・ドライバー変更 | 起動、画面、無線等へ影響する。正常版と復旧手段を用意し、まず公式GUIを利用 |

以下のKernel PanicとAdGuardの項目は、必要な場合だけ読む発展的な内容です。基本導入の必須作業ではありません。

## カーネルパニック

Kernel Panicは、Linuxカーネルが安全に処理を継続できない重大な状態を検出したときに停止する仕組みです。WindowsのBSODと大まかには同じ「OSの中核で重大な問題が発生した状態」と理解できますが、原因や復旧手順は異なります。

主な原因候補には、カーネルやドライバーの不具合、カーネル更新との互換性、ファイルシステム障害、メモリエラー、ストレージ障害、GPUドライバーなどがあります。

**基本的な切り分け**

1. 画面に表示されたpanicメッセージを写真などで記録する。
2. GRUBの **Advanced options for Linux Mint** から直前の正常なカーネルを選択して起動できるか確認する。
3. 起動できた場合は、問題が起きたカーネルやドライバー更新との関連を調べる。
4. 通常起動できない場合は、Linux Mint Live USBから起動する。
5. ストレージやメモリのハードウェア異常も候補として切り分ける。
6. Timeshiftの正常なスナップショットがある場合は復元を検討する。
7. 復旧後に `journalctl`、`dmesg`、カーネルバージョン、GPU / Wi-Fiなどのドライバー情報を確認する。

生成AIへ相談するときは、Linux Mintのバージョン、カーネルバージョン、PC機種、CPU/GPU、直前に行った更新、panic画面、GRUBから旧カーネルで起動できるか、Live USBで起動できるか、Timeshiftの有無を提示すると原因を絞り込みやすくなります。

Kernel Panicが発生しても、直ちにOS再インストールが必要とは限りません。旧カーネル起動、ドライバー切り分け、Live USB、Timeshiftなどで復旧できる場合があります。

## AdGuard for Linux

この項目は、基本のネット接続・更新・バックアップを確認した後に利用を検討してください。以下のコマンド一覧は一括実行用ではありません。`status` は保護状態の表示、`check-update` は更新確認に加えて公式資料上はフィルター等の更新も扱います。`configure` は設定、`start` / `stop` / `restart` は保護動作の変更、`update` は更新です。適用前に公式資料とインストール済みの版のヘルプを確認します。

[AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/) （AdGuard CLI）は、Linux / macOS向けのコマンドライン広告ブロッカーです。AdGuard公式はDebian stable 10以降、Ubuntu LTS 22.04 / 24.04以降、RHEL 8以降、Fedora 35以降を対応対象として記載しています。Linux MintはUbuntu系ですが、公式対応一覧にLinux Mint名が個別掲載されているわけではないため、利用時はUbuntu互換環境として動作を確認します。

**基本操作**

```sh
adguard-cli configure
adguard-cli start
adguard-cli status
adguard-cli stop
adguard-cli restart
adguard-cli check-update
adguard-cli update
```

全コマンドは `adguard-cli --help-all` で確認できます。

自動モードではiptablesのnatテーブル、IPv4 / IPv6のREDIRECT・QUEUEチェイン、`sudo` など一定の条件が必要です。環境によってはネットワーク設定やVPN、他のローカルプロキシ / フィルタリングソフトとの競合確認が必要です。

AdGuard Browser Extensionがブラウザ内の通信や要素非表示を中心に扱うのに対し、AdGuard for LinuxはCLIアプリとしてプロキシを利用し、対応する通信をシステム側でフィルタリングします。両者を併用する場合は、重複ブロック、HTTPSフィルタリング、サイト互換性、トラブル時の切り分けを意識してください。

カスタムルールは作業ディレクトリの `user.txt` などで管理でき、ブラウザごとのHTTPSフィルタリング除外も設定できます。

* [AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/)
* [インストール・初期設定・削除](https://adguard.com/kb/ja/adguard-for-linux/installation/)
* [設定と保護機能の管理](https://adguard.com/kb/ja/adguard-for-linux/settings/)
* [アプリ除外とカスタムフィルタ](https://adguard.com/kb/adguard-for-linux/cli-exclusions-and-filters/)

> **セキュリティ上の注意**：公式インストール例は `curl ... | sh` 形式です。実行前にURLがAdGuard公式Repositoryのものであることを確認し、不明なサイトのScriptを同様の方法で実行しないでください。

## 情報の確認範囲と参考資料

* **公式資料で確認した事項**：22.3の掲載、2029年4月までのサポート、システム要件、ISO検証、USB作成・導入手順、ドライバー確認、Timeshiftと個人ファイルの区別、旧カーネルでの起動、22.3のSystem Information・入力方法の変更。
* **判断のための説明**：メーカーのUbuntu対応を候補選びに使うこと、構成照合とLiveテストを組み合わせること、バックアップの復元確認を先に行うことは、関連公式資料に基づく本ガイドの運用上の提案です。
* **未確認事項**：Lenovo PD031426の機種別一覧本文、個別PCでのLinux Mint動作、全機能・長時間の電池持ち、ChromeOSだけでのメディア作成、暗号化や特殊構成での実機復元。既存のStar Labs説明についても、現行の全製品・構成で同じ条件となることまでは確認できていません。購入時にメーカーへ確認してください。

追加の一次情報：

* [Ubuntu](https://x.com/ubuntu)
* [Ubuntu Japanese Team](https://www.ubuntulinux.jp/)
* [Linux Mint 22.3公式リリース発表・システム要件](https://blog.linuxmint.com/?p=4981)
* [Linux Mint公式User Guide](https://linuxmint-user-guide.readthedocs.io/en/latest/)
* [Linux Mint公式Troubleshooting Guide](https://linuxmint-troubleshooting-guide.readthedocs.io/en/latest/)

### コミュニティ・掲示板

* [Linux Mintスレ](https://ff5ch.syoboi.jp/?q=Linux+Mint)
* [Ubuntu Linuxスレ](https://ff5ch.syoboi.jp/?q=Ubuntu+Linux)

本ガイドのコマンド例は実機でのインストール・復旧試験済みという意味ではありません。特に復元や暗号化、追加ドライバーは、利用するバージョンと機種の一次情報を確認してください。
