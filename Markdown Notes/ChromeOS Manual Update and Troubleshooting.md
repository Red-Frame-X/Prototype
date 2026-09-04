# ChromeOSを安全に手動更新する方法

ChromeOSは、インターネットに接続していると、OSアップデートを自動的に確認してダウンロードします。手動で更新を確認する場合も、Googleが案内しているChromeOSの設定画面から実行します。この文書では、自分の環境で更新やトラブル対応を行う際に再確認できるよう、公式手順と影響範囲をまとめて残しています。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260901 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 手動でアップデートを確認する

Google公式ヘルプでは、次の手順が案内されています。

1. Chromebookの電源を入れます。
2. ChromebookをWi-Fiに接続します。
3. 右下の時刻を選択し、**設定**を開きます。
4. 左下の**ChromeOSについて**を選択します。
5. **Google ChromeOS**で、現在のOSバージョンを確認します。
6. **アップデートの確認**を選択します。
7. アップデートが見つかった場合は、自動的にダウンロードが開始されます。

**アップデートの確認**が表示されない場合は、Chromebookが最新の状態になっている可能性があります。

更新中の中断を避けるため、GoogleはChromebookを電源に接続し、バッテリーが充電されていることを確認するよう案内しています。

## ダウンロード済みのアップデートを適用する

ソフトウェアアップデートのダウンロードが完了すると、右下の時刻の横に**アップデートが利用可能**という通知が表示されます。

通知内の**再起動**を選択すると、Chromebookが再起動してアップデートが適用されます。

## システムアップデートでエラーが発生する、またはダウンロードできない場合

Google公式ヘルプでは、次の順序で対処するよう案内されています。各手順の後に、問題が解決したか確認してください。

1. モバイルデータ通信を使用している場合は、Wi-Fiまたはイーサネットに接続してから、アップデートを再度ダウンロードします。
2. Chromebookの電源をいったんオフにしてからオンにします。
3. Chromebookをリセットします。
4. Chromebookを復元します。

### Chromebookをリセットする場合（Powerwash）

Powerwashは、Chromebookを初期状態に戻すためのリセットです。Google公式ヘルプによると、実行すると**ダウンロードフォルダ内のファイルを含む、Chromebookのハードドライブ上のユーザーデータがすべて消去されます**。設定、アプリ、ローカルファイルなども消去対象です。

一方、**Googleドライブや外部ストレージデバイス上のファイルはPowerwashでは削除されません**。

#### Powerwashを実行する前に

Googleは、リセット前に次の作業を行うよう案内しています。

1. 必要な情報と設定をGoogleアカウントに同期します。
2. `Downloads`フォルダなどに保存している必要なローカルファイルを、Googleドライブまたは外部ストレージへバックアップします。

#### Powerwashの実行手順

Google公式ヘルプでは、次の手順が案内されています。

1. Chromebookからログアウトします。
2. **Ctrl + Alt + Shift + R**キーを長押しします。
3. **再起動**を選択します。
4. 表示された画面で**Powerwash**を選択し、**続行**を選択します。
5. 画面の案内に沿って初期設定を行います。

> **重要:** 職場や学校で使用している管理対象Chromebookは、ユーザー自身ではPowerwashできません。データのワイプや組織への再登録が必要な場合は、管理者に連絡してください。

#### PowerwashとChromeOSの復元の違い

Powerwashは主にユーザーデータや設定を消去して端末を初期状態に戻す操作です。一方、**ChromeOSの復元はOS自体を削除して再インストールする処理**です。

Googleは、ChromeOSが正常に動作しない場合でも、可能であればまず再起動やPowerwashなどの影響が小さい手順を試し、それでも解決しない場合に復元へ進むよう案内しています。

### ChromeOSを復元する場合

リセットしても問題が解決しない場合、GoogleはChromeOSの復元を案内しています。復元ではChromeOSを削除して再インストールするため、Google公式の復元手順に従ってください。

## ハードウェアリセットについて

Googleは、キーボードやタッチパッドなどのハードウェアに関する一部の問題を解決する方法として、ハードウェアリセット（ハードリセット）を別途案内しています。

Googleは、ハードリセットを**他の方法で問題を解決できなかった場合にのみ試す**よう案内しています。また、機種によって手順が異なり、`Downloads`フォルダ内のファイルが一部削除される可能性があります。

ほとんどのChromebookでは、次の手順です。

1. Chromebookの電源を切ります。
2. **更新（Refresh）キーを押したまま、電源ボタンを押します。**
3. Chromebookが起動したら、更新キーを放します。

一部の機種では手順が異なるため、実行前にGoogle公式ヘルプで対象機種の手順を確認してください。

## 管理対象Chromebookについて

職場や学校で使用しているChromebookでは、アップデートが管理者によって管理されている場合があります。更新できない場合や設定を変更できない場合は、管理者に確認してください。

## 参照

* [Chromebookを更新する（Chromebookヘルプ）](https://support.google.com/chromebook/answer/15468740?hl=ja)
* [ハードウェアとシステムの問題を解決する（Chromebookヘルプ）](https://support.google.com/chromebook/answer/6309225?hl=ja)
* [Chromebookを初期状態にリセットする（Chromebookヘルプ）](https://support.google.com/chromebook/answer/183084?hl=ja)
* [Chromebookを復元する（Chromebookヘルプ）](https://support.google.com/chromebook/answer/1080595?hl=ja)
* [Chromebookのハードウェアをリセットする（Chromebookヘルプ）](https://support.google.com/chromebook/answer/3227606?hl=ja)
