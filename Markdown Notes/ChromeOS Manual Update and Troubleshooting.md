# ChromeOSを安全に手動更新する方法

ChromeOSは、インターネットに接続していると、OSアップデートを自動的に確認してダウンロードします。手動で更新を確認する場合も、Googleが案内しているChromeOSの設定画面から実行します。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260826 |

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

### Chromebookをリセットする場合

初期状態へのリセット（Powerwash）では、Chromebookのハードドライブ上にある設定、アプリ、ダウンロードフォルダを含むローカルファイルなどのユーザーデータが消去されます。

実行前に、必要なファイルをGoogleドライブまたは外部ストレージへバックアップしてください。

職場や学校で管理されているChromebookは、ユーザー自身では初期状態にリセットできない場合があります。その場合は管理者に連絡してください。

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
