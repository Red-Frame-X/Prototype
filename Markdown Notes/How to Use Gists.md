# How to Use Gists

GitHub Gistsを利用して、カスタムフィルタやUserScriptを各種拡張機能（AdGuard、Tampermonkeyなど）へ登録する手順です。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc](https://github.com/Red-Frame-X/AdGuard-Custom-Rules-UserScript-Regex-etc) |
| **License** | CC0 (Public Domain) |
| **Version** | 20260614 |

この備忘録は CC0 ライセンスの下で提供します。（This work is licensed under CC0 1.0 Universal）
* [CC0について ― “いかなる権利も保有しない”](https://creativecommons.jp/sciencecommons/aboutcc0/)

**【免責・例外】** ただし、以下の内容は本ライセンスの適用外であり、それぞれの権利者が著作権を保有しています。
* 引用等で示された第三者の文章
* 紹介しているソフトウェア、アプリ、拡張機能の名称および公式の製品説明文
* リンク先のコンテンツ

※ 記述内容は個人の検証に基づくものであり、正確性を保証するものではありません。

---

## 運用方法の比較：GistsとGitHubリポジトリ

フィルタやスクリプトを管理するにあたり、GistsとGitHubリポジトリのどちらを使用するかは一長一短があります。

### GitHub Gists を使用する場合
* **メリット**: アカウントさえあれば手軽に作成でき、単一のスクリプトやフィルタを即座に公開するのに向いています。
* **デメリット**: 複数ファイルの管理が煩雑になります。Linter（構文チェック）やCI/CD（自動テスト・デプロイ）、Issueやプルリクエストの機能が使用できません。また、Raw URLのキャッシュが強いため、更新が反映されるまでに数分間のタイムラグが発生します。

### GitHub リポジトリ を使用する場合
* **メリット**: バージョン管理（リビジョン管理）が厳密に行え、Linterの恩恵を受けられます。Issueを通じてユーザーからフィードバックを受けるなど、保守性が格段に高まり安全な運用が可能です。
* **デメリット**: Gitの基本操作（commit, pushなど）やディレクトリ構造の知識が必要となり、単一ファイルを置くだけの用途としては初期設定のハードルが少し上がります。

---

## Description 1：AdGuard > カスタムフィルタの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。

   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列(コミットハッシュ)/ファイル名.txt`

4. URLから `長い英数字の羅列/`（コミットハッシュ）の部分を削除し、以下のような形式にします。
   
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.txt`
   > **Note**: この処理を行うことで、特定の更新履歴に縛られず、常に最新版（HEAD）を参照するURLになります。

6. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
   * **注意**: GitHubのRaw URLはキャッシュ（CDN）が効いているため、編集直後は内容が反映されない場合があります（数分程度のタイムラグがあります）。
7. この短縮URLを、AdGuardの「カスタムフィルタ（またはDNSフィルタ）」として追加（インポート）します。
8. 今後フィルタを更新する際は、ファイル内の `! Version:`（または `! TimeUpdated:`）の数値を、前回登録時より大きく書き換えてください（例：`2026010101` → `2026010201`）。
   * 数値が増加していることでAdGuardが変更を検知し、自動更新が行われます。

---

## Description 2：Tampermonkey > UserScriptの登録

1. GitHub Gistsで対象ファイルの **[Raw]** ボタンをクリックします。
   * **重要**: UserScriptとして正しく認識させるため、ファイル名は必ず `.user.js` で終わるようにしてください。
2. ブラウザのアドレスバーでURLを確認します。通常は以下のようになっています。
   
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/長い英数字の羅列(コミットハッシュ)/ファイル名.user.js`

4. URLから `長い英数字の羅列/`（コミットハッシュ）の部分を削除し、以下のような形式にします。
   
   `https://gist.githubusercontent.com/ユーザー名/GistID/raw/ファイル名.user.js`
   > **Note**: この処理を行うことで、特定の更新履歴に縛られず、常に最新版（HEAD）を参照するURLになります。

6. 短縮したURLをブラウザで開き直し、最新の内容が表示されるか確認してください。
7. この短縮URLを、Tampermonkeyの管理画面の「URLからインポート」する欄へ貼り付けるか、直接ブラウザで開いて「インストール」をクリックします。
8. 今後スクリプトを更新する際は、コード内のメタデータ `@version` の数値を、前回登録時より大きく書き換えてください（例：`1.0` → `1.1`）。
   * 数値が増加していることで拡張機能が変更を検知し、自動更新が行われます。
   * **推奨事項**: スクリプトのメタデータ（UserScriptヘッダ）内に `@updateURL` と `@downloadURL` を記述し、そこに上記「短縮したURL」を指定しておくと、更新チェックの挙動がより確実になります。
