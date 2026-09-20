# Linux Mint Guide

Linux Mintに関する導入、設定、運用、バックアップ、トラブルシューティングなどをまとめたガイドです。

---

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202609201600 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

Linux Mintは、デスクトップ／ノートPC向けに使いやすさを重視したLinuxディストリビューションです。現在の標準系列であるLinux Mint 22.xはUbuntu 24.04 LTS（Noble）を基盤とし、Linux Mint 22.3 “Zena” は2029年4月までサポートされます。公式にはCinnamon／MATE／Xfceの3エディションが提供され、CinnamonはLinux Mintの主力デスクトップ、MATEはクラシックな操作感、Xfceは比較的軽量な構成です。

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

## ハードウェア要件と実用上の目安

Linux Mint 22.3の公式要件は、**2 GB RAM（快適利用には4 GB推奨）／20 GBストレージ（100 GB推奨）／1024×768以上の画面解像度**です。

実際の快適性は用途で変わります。Webブラウザの多タブ利用、動画視聴、Office作業などを日常的に行うなら、RAM 8 GB以上とSSDを備えたPCの方が余裕があります。CPU、GPU、Wi-Fi、Bluetooth、USB、Webカメラ、指紋認証などは機種ごとにLinux対応状況が異なるため、購入前にメーカー情報やLinux Mint／Ubuntuでの実績を確認します。

NVIDIA GPUを使う場合は、導入後に **Driver Manager** で利用可能なドライバーを確認します。Linux Mint 22.2／22.3は新しいハードウェア向けにHWEカーネルを採用していますが、Linux Mint 22.3の公式リリースノートでは、古いNVIDIA 470ドライバーなど一部環境との互換性問題が案内されています。該当する場合は、LTSカーネルを採用するLinux Mint 22.1から導入する回避策が示されています。

* [Linux Mint 22.3 Release Notes](https://linuxmint.com/rel_zena.php)
* [Hardware drivers](https://linuxmint-installation-guide.readthedocs.io/en/latest/drivers.html)

## Linux Mint搭載済みPC

Linux Mint公式は、ハードウェア関連のパートナーとして **Framework** と **ThinkPenguin** を掲載しています。FrameworkについてはLinux Mint開発チームが実機テストを行い、互換性改善にもつながっていることが公式ブログで説明されています。

* [Linux Mint Partners](https://linuxmint.com/partners.php)
* [Linux Mint Blog: Monthly News – May 2025](https://blog.linuxmint.com/?p=4850)
* **[Star Labs](https://jp.starlabs.systems/)**：Linux向けに設計されたノートPCやMini PCを販売するメーカー。Linux Mintを含む複数のLinuxディストリビューションを、対応カーネル上で標準ISOから導入できる。

ただし、Linux Mintが「公式認定した完成品PC一覧」を常時提供しているわけではありません。日本から海外メーカー製PCを購入する場合は、Linux Mintプリインストールの有無だけでなく、送料、関税、保証対応、修理時の発送先、ACアダプター、キーボード配列、無線チップなども確認してください。販売状況は変化するため、購入時点でメーカー公式ページを確認します。

## Linux Mintのインストール

Linux Mint公式のInstallation Guideでは、ISOの入手、真正性・整合性確認、USBメディア作成、Live起動、インストール、ドライバー確認、Timeshift設定まで一連の手順が案内されています。

1. [Linux Mint公式サイト](https://linuxmint.com/download.php)から使用するエディションのISOを入手する。
2. `sha256sum.txt` と署名を利用し、ISOの整合性と真正性を確認する。
3. USBメモリへISOを書き込み、起動可能なインストールメディアを作成する。
4. USBからLinux MintをLive起動し、画面、Wi-Fi、音声、Bluetooth、USB機器などを確認する。
5. デスクトップ上の **Install Linux Mint** を起動する。
6. 言語、ネットワーク、必要に応じてマルチメディアコーデックを設定する。
7. インストール方式とディスク構成を確認する。
8. ユーザー名、パスワードなどを設定してインストールする。
9. 再起動後にUpdate ManagerとDriver Managerを確認する。
10. Timeshiftを設定して復旧用スナップショットを作成する。

* [Linux Mint Installation Guide](https://linuxmint-installation-guide.readthedocs.io/en/latest/)
* [Verify your ISO image](https://linuxmint-installation-guide.readthedocs.io/en/latest/verify.html)
* [Create the bootable media](https://linuxmint-installation-guide.readthedocs.io/en/latest/burn.html)
* [Boot Linux Mint](https://linuxmint-installation-guide.readthedocs.io/en/latest/boot.html)
* [Install Linux Mint](https://linuxmint-installation-guide.readthedocs.io/en/latest/install.html)

> **❗️注意**：`Erase disk and install Linux Mint` は対象ディスク上の既存データを消去します。パーティション変更、既存OSとのデュアルブート、暗号化設定を行う場合は、先に重要ファイルを別媒体へバックアップしてください。Windowsと併用する場合は、BitLockerやWindows側の高速スタートアップ、EFI／Secure Bootの設定も事前に確認します。

Secure Bootで起動できない場合について、Linux Mint公式ガイドはインストール条件の見直しやBIOS/UEFI側でSecure Bootを無効化する方法を案内しています。安易に設定を変更せず、機種の公式手順を確認してください。

* [EFI / SecureBoot](https://linuxmint-installation-guide.readthedocs.io/en/latest/efi.html)

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

* [Update Manager](https://linuxmint-user-guide.readthedocs.io/en/latest/mintupdate.html)
* [Multimedia codecs](https://linuxmint-installation-guide.readthedocs.io/en/latest/codecs.html)

## アプリケーション管理

Linux Mintでは複数の配布方式があります。目的や配布元を確認し、必要以上に方式を混在させない方が管理しやすくなります。

| 方式 | 概要 | 注意点 |
| :--- | :--- | :--- |
| Software Manager | GUIからアプリを検索・導入する | 初心者が最初に使いやすい |
| APT | Ubuntu／Linux Mint系のパッケージ管理 | システムと統合しやすい |
| Flatpak / Flathub | アプリを比較的独立した環境で配布 | 容量や権限モデルがAPTと異なる |
| .deb | Debian系パッケージを直接導入 | 配布元の信頼性と依存関係を確認する |
| AppImage | 単体ファイルとして実行する方式 | 自動更新やシステム統合はアプリごとに異なる |

同じアプリが複数方式で提供される場合、公式配布元、更新頻度、サンドボックスの必要性、ディスク容量、テーマ統合などを比較して選びます。「常にAPT」「常にFlatpak」のように一律で決める必要はありません。

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

## トラブルシューティングと復旧

Linux Mintで問題が発生した場合は、最初から再インストールするのではなく、症状・直前の変更・ハードウェア・ログを段階的に切り分けます。

| コマンド | 主な用途 |
| :--- | :--- |
| `journalctl` | systemdのシステムログを確認する |
| `dmesg` | カーネル・デバイス・ドライバー関連のメッセージを確認する |
| `systemctl` | systemdサービスの状態確認・管理 |
| `inxi -Fxxxz` | OS、カーネル、CPU、GPU、ネットワーク等のシステム情報をまとめて確認する |

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

## Kernel Panic

Kernel Panicは、Linuxカーネルが安全に処理を継続できない重大な状態を検出したときに停止する仕組みです。WindowsのBSODと大まかには同じ「OSの中核で重大な問題が発生した状態」と理解できますが、原因や復旧手順は異なります。

主な原因候補には、カーネルやドライバーの不具合、カーネル更新との互換性、ファイルシステム障害、メモリエラー、ストレージ障害、GPUドライバーなどがあります。

**基本的な切り分け**

1. 画面に表示されたpanicメッセージを写真などで記録する。
2. GRUBの **Advanced options for Linux Mint** から直前の正常なカーネルを選択して起動できるか確認する。
3. 起動できた場合は、問題が起きたカーネルやドライバー更新との関連を調べる。
4. 通常起動できない場合は、Linux Mint Live USBから起動する。
5. ストレージやメモリのハードウェア異常も候補として切り分ける。
6. Timeshiftの正常なスナップショットがある場合は復元を検討する。
7. 復旧後に `journalctl`、`dmesg`、カーネルバージョン、GPU／Wi-Fiなどのドライバー情報を確認する。

生成AIへ相談するときは、Linux Mintのバージョン、カーネルバージョン、PC機種、CPU/GPU、直前に行った更新、panic画面、GRUBから旧カーネルで起動できるか、Live USBで起動できるか、Timeshiftの有無を提示すると原因を絞り込みやすくなります。

Kernel Panicが発生しても、直ちにOS再インストールが必要とは限りません。旧カーネル起動、ドライバー切り分け、Live USB、Timeshiftなどで復旧できる場合があります。

## AdGuard for Linux

[AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/)（AdGuard CLI）は、Linux／macOS向けのコマンドライン広告ブロッカーです。AdGuard公式はDebian stable 10以降、Ubuntu LTS 22.04／24.04以降、RHEL 8以降、Fedora 35以降を対応対象として記載しています。Linux MintはUbuntu系ですが、公式対応一覧にLinux Mint名が個別掲載されているわけではないため、利用時はUbuntu互換環境として動作を確認します。

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

自動モードではiptablesのnatテーブル、IPv4／IPv6のREDIRECT・QUEUEチェイン、`sudo` など一定の条件が必要です。環境によってはネットワーク設定やVPN、他のローカルプロキシ／フィルタリングソフトとの競合確認が必要です。

AdGuard Browser Extensionがブラウザ内の通信や要素非表示を中心に扱うのに対し、AdGuard for LinuxはCLIアプリとしてプロキシを利用し、対応する通信をシステム側でフィルタリングします。両者を併用する場合は、重複ブロック、HTTPSフィルタリング、サイト互換性、トラブル時の切り分けを意識してください。

カスタムルールは作業ディレクトリの `user.txt` などで管理でき、ブラウザごとのHTTPSフィルタリング除外も設定できます。

* [AdGuard for Linux](https://adguard.com/kb/ja/adguard-for-linux/)
* [インストール・初期設定・削除](https://adguard.com/kb/ja/adguard-for-linux/installation/)
* [設定と保護機能の管理](https://adguard.com/kb/ja/adguard-for-linux/settings/)
* [アプリ除外とカスタムフィルタ](https://adguard.com/kb/adguard-for-linux/cli-exclusions-and-filters/)

> **セキュリティ上の注意**：公式インストール例は `curl ... | sh` 形式です。実行前にURLがAdGuard公式リポジトリのものであることを確認し、不明なサイトのスクリプトを同様の方法で実行しないでください。

## セキュリティと保守

Linux Mintを安定して使うには、特別な「最適化」よりも、更新、バックアップ、信頼できる配布元、権限管理を基本にします。

* Update ManagerでOS・アプリ・セキュリティ更新を継続する。
* Driver Managerを利用し、必要なプロプライエタリドライバーを公式手順で導入する。
* ソフトウェアはSoftware Manager、公式リポジトリ、公式配布元を優先する。
* `sudo` は管理者権限を与えるため、コマンド内容を確認してから実行する。
* Web上の不明なスクリプトやコマンドを、そのままコピー＆ペーストして実行しない。
* Timeshiftでシステム復元ポイントを用意する。
* Timeshiftとは別に個人ファイルをバックアップする。
* Secure Boot、ディスク暗号化、ファイアウォールはPCの用途と脅威モデルに応じて設定する。
* 大きなカーネル更新やドライバー変更の前後は、復旧手段を確認しておく。

Linux Mintの公式ドキュメントは、Installation Guide、User Guide、Troubleshooting Guideに分かれています。トラブル時は検索結果だけで判断せず、まず公式ドキュメントと公式リリースノートを確認してください。

* [Linux Mint Documentation](https://linuxmint.com/documentation.php)
