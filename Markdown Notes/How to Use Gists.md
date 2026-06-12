# How to Use Gists

GitHub Gistsを利用して、カスタムフィルタやUserScriptを各種拡張機能（AdGuard、Tampermonkeyなど）へ登録する手順です。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260612 |

この備忘録は CC0 ライセンスの下で提供します（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
* 引用等で示された第三者の文章
* 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
* リンク先のコンテンツ

※ 記述内容は個人の検証に基づくものであり、正確性を保証するものではありません。

---

## 運用に関する解説：GistsとGitHubリポジトリの使い分け

カスタムフィルタやUserScriptを公開・管理する際、GitHub Gistsはアカウントさえあれば手軽に作成できるため、単一のファイルを即座に共有する用途に非常に優れています。ただし、複数ファイルの管理には不向きであり、Linter（構文チェック）やIssueを用いたフィードバック機能など、高度な開発支援機能は利用できません。

一方で、GitHubに専用のリポジトリを作成して管理する手法は、Gitの基本操作（commitやpush）やディレクトリ構造の知識が求められるため、初期の学習コストはやや高くなります。しかし、厳密なリビジョン管理が可能になり、保守性が格段に向上するため、継続的かつ安全にルールやスクリプトを運用していく場合にはリポジトリの利用が推奨されます。

---

## Description 1：AdGuard > カスタムフィルタの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列(コミットハッシュ)/ファイル名.txt`

3. URLから `長い英数字の羅列/`（コミットハッシュ）の部分を削除し、以下のような形式にします。
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.txt`
   > **Note**: この処理を行うことで、特定の更新履歴に縛られず、常に最新版（HEAD）を参照するURLになります。

4. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
   * **運用上の注意点**: GistsのRaw URLにはCDNキャッシュが適用されているため、ファイルを編集・更新しても直後には反映されず、数分程度のタイムラグが発生する仕様となっています。
5. この短縮URLを、AdGuardの「カスタムフィルタ（またはDNSフィルタ）」として追加（インポート）します。
6. 今後フィルタを更新する際は、ファイル内の `! Version:`（または `! TimeUpdated:`）の数値を、前回登録時より大きく書き換えてください（例：`2026010101` → `2026010201`）。
   * 数値が増加していることでAdGuardが変更を検知し、自動更新が行われます。

---

## Description 2：Tampermonkey > UserScriptの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
   * **重要**: UserScriptとして正しく認識させるため、ファイル名は必ず `.user.js` で終わるようにしてください。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列(コミットハッシュ)/ファイル名.user.js`

3. URLから `長い英数字の羅列/`（コミットハッシュ）の部分を削除し、以下のような形式にします。
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.user.js`
   > **Note**: AdGuardのフィルタ登録時と同様に、常に最新版（HEAD）を参照させるための処理です。

4. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
5. この短縮URLを、Tampermonkeyの管理画面の「URLからインポート」する欄へ貼り付けるか、直接ブラウザで開いて「インストール」をクリックします。
6. 今後スクリプトを更新する際は、コード内のメタデータ `@version` の数値を、前回登録時より大きく書き換えてください（例：`1.0` → `1.1`）。
   * 数値が増加していることで拡張機能が変更を検知し、自動更新が行われます。
   * **確実な更新のために**: スクリプトのメタデータ（UserScriptヘッダ）内に `@updateURL` と `@downloadURL` を記述し、そこに上記「短縮したURL」を指定しておく運用を推奨します。これにより、更新チェックの挙動がより安定的になります。