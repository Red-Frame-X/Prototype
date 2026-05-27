# How to Use Gists

GitHub Gistsを利用して、カスタムフィルタやUserScriptを各種拡張機能へ登録する手順です。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260527 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260527 |

この備忘録は CC0 ライセンスの下で提供します（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
- 引用等で示された第三者の文章
- 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
- リンク先のコンテンツ

記述内容は個人の検証に基づくものであり、正確性を保証するものではありません。

---

## Description 1：AdGuard > カスタムフィルタの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。

   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列/ファイル名.txt`

3. URLから `長い英数字の羅列/` の部分を削除し、以下のような形式にします。

   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.txt`
   
   > **補足**：
   > この処理を行うことで、特定の更新履歴に縛られず、常に最新版（HEAD）を参照するURLになります。

4. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
5. この短縮URLを、AdGuardの「カスタムフィルタ」として登録します。
6. 今後フィルタを更新する際は、ファイル内の `! Version:` の数値を、前回登録時より大きく書き換えてください（例：`2024010101` → `2024010201`）。
   * 数値が増えていることでAdGuardが変更を検知し、自動更新が行われます。
7. おすすめの運用方法
   * Gistではなく、GitHubに自分用のRepository（リポジトリ）を作成してフィルタを管理したほうが、リビジョン管理やLinter（構文チェック）の恩恵を受けられるため推奨されます。

---

## Description 2：Tampermonkey > UserScriptの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。
    
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列/ファイル名.user.js`
   
3. URLから `長い英数字の羅列/` の部分を削除し、以下のような形式にします。
   
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.user.js`
   
    > **補足**：
   > この処理を行うことで、特定の更新履歴に縛られず、常に最新版（HEAD）を参照するURLになります。

4. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
5. この短縮URLを、Tampermonkeyの管理画面の「URLからインポート」する欄へ貼り付けるか、直接ブラウザで開いて「インストール」をクリックします。
6. 今後スクリプトを更新する際は、コード内の `@version` の数値を、前回登録時より大きく書き換えてください（例：`1.0` → `1.1`）。
   * 数値が増えていることで拡張機能が変更を検知し、自動更新が行われます。

7. おすすめの運用方法
   * こちらも同様に、GitHubに自分用のRepositoryを作成してUserScriptを管理したほうが、保守性が高まり安全に運用できます。
