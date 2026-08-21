# UserScript

𝕏およびYouTubeの表示・操作を調整する個人用UserScriptです。TampermonkeyなどのUserScriptマネージャーで使用します。

## インストール

1. 対応するUserScriptマネージャーをブラウザへ導入します。
2. 使用したい`.user.js`ファイルを開き、`Raw`を選択します。
3. 表示されたインストール画面で対象サイト、権限、ソースを確認して承認します。

## スクリプト一覧

- `x-auto-select-community-latest-sort.user.js`：𝕏コミュニティの並べ替えで「直近／Latest」を選択
- `x-auto-select-following-latest-sort.user.js`：𝕏ホームタイムラインの並べ替えで「最新」を選択
- `x-spaces-and-live-broadcast-blocker.user.js`：𝕏のスペース／ライブ放送UIを非表示
- `youtube-description-auto-expander.user.js`：YouTubeの動画概要欄を自動展開
- `youtube-shelf-force-expand.user.js`：YouTubeのシェルフを展開して「もっと見る」を非表示

サイト側のDOM変更により動作しなくなることがあります。問題が発生した場合は、該当スクリプトを一時停止して切り分けてください。`@updateURL`と`@downloadURL`が設定されたスクリプトは、マネージャーの設定に従って更新されます。
