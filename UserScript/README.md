# UserScript

𝕏およびYouTubeの表示・操作を自分の環境向けに調整するための個人用UserScriptと、その設定メモです。主な目的は、学習・検証の記録と、再設定時に参照できるバックアップを残すことです。

> [!IMPORTANT]
> このディレクトリは一般向けの配布や導入ガイドを目的としていません。記述やコメントの下書きはChatGPTで推敲・整理しているため、内容に誤り、古い情報、環境依存の挙動が含まれる可能性があります。対象サイトのDOMや仕様は変化しやすいため、使用時は実際のページとスクリプト内容を再確認します。

## スクリプト一覧

- [`x-auto-select-community-latest-sort.user.js`](x-auto-select-community-latest-sort.user.js)：𝕏コミュニティの投稿一覧で新しい投稿を優先する並べ替えを自動選択
- [`x-auto-select-following-latest-sort.user.js`](x-auto-select-following-latest-sort.user.js)：𝕏の対象タイムラインで新しい投稿を優先する並べ替えを自動選択
- [`x-spaces-and-live-broadcast-blocker.user.js`](x-spaces-and-live-broadcast-blocker.user.js)：𝕏のスペース／ライブ放送関連UIを非表示
- [`youtube-description-auto-expander.user.js`](youtube-description-auto-expander.user.js)：YouTubeの動画概要欄を自動展開
- [`youtube-shelf-force-expand.user.js`](youtube-shelf-force-expand.user.js)：YouTubeの対象シェルフを展開し、「もっと見る」操作を省略

## 自分の環境での利用メモ

ViolentmonkeyやTampermonkeyなど、UserScriptメタデータを扱えるスクリプトマネージャーで使用しています。再設定時は`.user.js`の`@match`／`@include`、要求権限、`@updateURL`、`@downloadURL`などを確認してから有効化します。

UserScriptは対象ページ上でJavaScriptを実行するため、保存したスクリプトであっても内容と権限を確認し、必要なものだけを有効にします。

## 更新と互換性

𝕏やYouTubeのDOM、属性、表示文言は予告なく変更されることがあり、サイト側の変更によってスクリプトが動作しなくなる可能性があります。問題が発生した場合は該当スクリプトを一時停止し、他のUserScriptや拡張機能との競合も含めて切り分けます。

`@updateURL`や`@downloadURL`を持つスクリプトの更新確認・更新方法は、使用するUserScriptマネージャーの実装と設定に従います。メタデータに更新先が指定されていること自体は、すべてのマネージャーで同じ周期・同じ方法で自動更新されることを意味しません。

## 参考資料

- [Tampermonkey Documentation](https://www.tampermonkey.net/documentation.php)
- [Violentmonkey Documentation](https://violentmonkey.github.io/)
