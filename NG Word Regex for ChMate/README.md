# NG Word Regex for ChMate

Android用5ちゃんねるブラウザChMateのNG設定で自分が使用・検証している正規表現集です。特定の語句や投稿パターンをまとめて判定するための個人用設定であり、主な目的は設定のバックアップと検証記録を残すことです。5ちゃんねるやChMateの公式フィルタではありません。

> [!IMPORTANT]
> このREADMEは一般向けの導入手順を目的としていません。文章の下書きはChatGPTで推敲・整理しているため、説明に誤り、古い情報、環境依存の内容が含まれる可能性があります。正規表現の挙動は実際の投稿例と使用中のChMateで確認します。

## ファイル

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| NG Word Regex for ChMate | ChMateのNG設定で使用・検証しているJava正規表現集 | [`NG Word Regex for ChMate.txt`](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |

TXTファイルのリンクは、色分けのないRaw表示を開きます。

## 自分の環境での設定メモ

[`NG Word Regex for ChMate.txt`](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) に保存している正規表現を、必要なものだけChMateのNG設定へ登録し、正規表現として使用しています。変更時は一度に大量追加せず、意図した投稿だけが対象になることを確認してから常用します。

### 式を読む

`[A-Za-z]` は英字1文字、 `{50,}` は直前の条件の50回以上の繰り返しです。たとえば `[A-Za-z]{50,}+` は、半角英字が50文字以上連続する箇所を探します。末尾の `+` は、後続の条件に合わせて繰り返しを戻さないJavaの所有的量指定子です。 [JavaのPattern仕様](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html)

Javaの仕様で式の意味を調べ、NGを適用する欄や警告の表示はChMateで確認します。試すときは、NGにしたい投稿に加えて、手前の境界となる49文字の投稿など、残したい例も用意します。 [ChMate公式FAQ](https://chmate.airfront.co.jp/docs/faq/)

## 検証時の注意

複数の式を一度に変更すると、誤検出した式を特定しにくくなります。文字範囲、任意文字、繰り返し、選択肢などを広く指定する正規表現は、想定外の通常投稿にも一致する可能性があります。

NG対象を増やす場合は、式を単純に広げるより、実際の投稿例で一致範囲を確認しながら条件を調整します。ChMateのUIやNG機能の挙動はバージョンによって変わる可能性があるため、READMEの記述より使用中のアプリ表示と実際の挙動を優先します。

## 関連情報

- [RepositoryのルートREADME](../README.md)
- [NG Word Regex for ChMateディレクトリ](./)
