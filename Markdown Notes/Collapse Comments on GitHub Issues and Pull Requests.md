# GitHubのIssue・Pull Requestコメントを折りたたむ方法

IssueやPull Requestで、結論の下に長いログや検証結果を添えるときに使います。`<summary>` に開く前に見える見出しを書き、 `<details>` の中に補足を置きます。下のコードブロックからタグと本文をコピーし、外側のバッククォートを外してコメントに貼り付けます。送信前にPreviewで見出しと展開後の内容を確認します。 [GitHub Docsの折りたたみ構文](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections)

### 冒頭文

（あなたの書いた導入文など）

| Metadata | 情報 |
| :--- | :--- |
| **ホームページ** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **ライセンス** | CC0-1.0 |
| **Version** | 202611280535 |

```
<details>
<summary> Screenshot (クリックで展開) </summary>

アップロードしたScreenshotのURL

</details>
```

```  
<details>
<summary> レポートのタイトル（クリックで展開）</summary>

レポートの全文

</details>
```

### 手動での動作検証結果
（あなたがやった検証結果を書く）

### 私の見解
（あなたの見解を書く）
