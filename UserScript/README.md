# UserScript

𝕏およびYouTubeの表示・操作を自分の環境向けに調整するための個人用UserScriptと、その設定メモです。主な目的は、学習・検証の記録と、再設定時に参照できるバックアップを残すことです。

> [!IMPORTANT]
> このディレクトリは一般向けの配布や導入ガイドを目的としていません。記述やコメントの下書きはChatGPTで推敲・整理しているため、内容に誤り、古い情報、環境依存の挙動が含まれる可能性があります。対象サイトのDOMや仕様は変化しやすいため、使用時は実際のページとUserScriptの内容を再確認します。

## UserScript一覧

| UserScript | 対象 | 主な内容 |
| --- | --- | --- |
| [`x-auto-select-community-latest-sort.user.js`](x-auto-select-community-latest-sort.user.js) | 𝕏 | コミュニティの投稿一覧で新しい投稿を優先する並べ替えを自動選択 |
| [`x-auto-select-following-latest-sort.user.js`](x-auto-select-following-latest-sort.user.js) | 𝕏 | 対象タイムラインで新しい投稿を優先する並べ替えを自動選択 |
| [`x-spaces-and-live-broadcast-blocker.user.js`](x-spaces-and-live-broadcast-blocker.user.js) | 𝕏 | スペース／ライブ放送関連UIを非表示 |
| [`youtube-description-auto-expander.user.js`](youtube-description-auto-expander.user.js) | YouTube | 動画概要欄を自動展開 |
| [`youtube-shelf-force-expand.user.js`](youtube-shelf-force-expand.user.js) | YouTube | 対象シェルフを展開し、「もっと見る」操作を省略 |

## 自分の環境での利用メモ

ViolentmonkeyやTampermonkeyなど、UserScript Metadataを扱えるUserScriptマネージャーで使用しています。再設定時は`.user.js`の`@match`／`@include`、要求権限、`@updateURL`、`@downloadURL`などを確認してから有効化します。

UserScriptは対象ページ上でJavaScriptを実行するため、保存したUserScriptであっても内容と権限を確認し、必要なものだけを有効にします。

UserScriptの日本語表示名は`@name:ja`に定義しています。更新時の識別に使われる`@name`と`@namespace`は保持します。実際の表示名は、使用するUserScriptマネージャーの言語設定と対応状況によって異なります。

## 更新と互換性

𝕏やYouTubeのDOM、属性、表示文言は予告なく変更されることがあり、サイト側の変更によってUserScriptが動作しなくなる可能性があります。問題が発生した場合は該当UserScriptを一時停止し、他のUserScriptや拡張機能との競合も含めて切り分けます。

`@updateURL`や`@downloadURL`を持つUserScriptの更新確認・更新方法は、使用するUserScriptマネージャーの実装と設定に従います。Metadataに更新先が指定されていること自体は、すべてのマネージャーで同じ周期・同じ方法で自動更新されることを意味しません。

## 関連情報

- [RepositoryのルートREADME](../README.md)
- [UserScriptディレクトリ](./)

## 参考資料

- [Tampermonkeyのドキュメント](https://www.tampermonkey.net/documentation.php)
- [Violentmonkeyのドキュメント](https://violentmonkey.github.io/)
