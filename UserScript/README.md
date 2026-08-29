# UserScript

𝕏およびYouTubeの表示・操作を調整する個人用UserScriptです。Violentmonkey、Tampermonkeyなど、UserScriptメタデータを扱えるスクリプトマネージャーで使用します。

## インストール

1. 使用するブラウザに対応したUserScriptマネージャーを導入します。
2. 使用したい`.user.js`ファイルを下の一覧から開き、`Raw`を選択します。
3. UserScriptマネージャーのインストール画面で、`@match`／`@include`などの適用先、要求権限、更新元を確認してからインストールします。

> [!IMPORTANT]
> UserScriptは対象ページ上でJavaScriptを実行します。内容と権限を確認できるスクリプトだけをインストールしてください。

## スクリプト一覧

- [`x-auto-select-community-latest-sort.user.js`](x-auto-select-community-latest-sort.user.js)：𝕏コミュニティの投稿一覧で新しい投稿を優先する並べ替えを自動選択
- [`x-auto-select-following-latest-sort.user.js`](x-auto-select-following-latest-sort.user.js)：𝕏の対象タイムラインで新しい投稿を優先する並べ替えを自動選択
- [`x-spaces-and-live-broadcast-blocker.user.js`](x-spaces-and-live-broadcast-blocker.user.js)：𝕏のスペース／ライブ放送関連UIを非表示
- [`youtube-description-auto-expander.user.js`](youtube-description-auto-expander.user.js)：YouTubeの動画概要欄を自動展開
- [`youtube-shelf-force-expand.user.js`](youtube-shelf-force-expand.user.js)：YouTubeの対象シェルフを展開し、「もっと見る」操作を省略

## 更新と互換性

𝕏やYouTubeのDOM、属性、表示文言は予告なく変更されることがあり、サイト側の変更によってスクリプトが動作しなくなる可能性があります。問題が発生した場合は該当スクリプトを一時停止し、他のUserScriptや拡張機能との競合も含めて切り分けてください。

`@updateURL`や`@downloadURL`を持つスクリプトの更新確認・更新方法は、使用するUserScriptマネージャーの実装と設定に従います。メタデータに更新先が指定されていること自体は、すべてのマネージャーで同じ周期・同じ方法で自動更新されることを保証しません。

## 参考資料

- [Tampermonkey Documentation](https://www.tampermonkey.net/documentation.php)
- [Violentmonkey Documentation](https://violentmonkey.github.io/)
