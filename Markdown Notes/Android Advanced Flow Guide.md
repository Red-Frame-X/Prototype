# Android Advanced Flow Guide

Androidの未確認デベロッパー製アプリをインストールする「Advanced Flow」の概要です。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260822 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

> [!IMPORTANT]
> 本文は2026年8月22日時点の公開情報に基づきます。地域展開前後で画面、文言、対象端末、手順が変わる可能性があります。実機では画面上の案内を優先してください。

## 要点

Advanced Flowは、未登録アプリをインストールしたいパワーユーザー向けの一度限りの解除手順です。Googleは、詐欺師が通話や遠隔操作を使って被害者に保護機能を無効化させる「coercion scam（強要型詐欺）」への対策として、意図的な待機と再認証を組み込んでいます。

公式に示された流れは次のとおりです。

1. システム設定で開発者モードを有効にする。
2. 第三者から操作を指示されていないことを確認する。
3. 端末を再起動し、再認証する。
4. 1日間の保護待機時間後に、生体認証または端末PINで本人確認する。
5. リスク警告を確認し、7日間または無期限の許可を選んでインストールする。

GoogleはAdvanced Flowを2026年8月に開始し、2026年9月30日からブラジル、インドネシア、シンガポール、タイの認定Android端末で、参加ストアを対象に開発者確認を適用する予定です。2027年以降は世界展開が予定されています。ADBによる開発者向けインストール手順は変更されないと案内されています。

## 対象を混同しないための整理

| 経路 | 本人確認 | 配布範囲 | 利用者側の扱い |
| :--- | :--- | :--- | :--- |
| 通常配布 | 必要 | ストアやウェブサイトなど | 登録済みアプリとして通常どおりインストール |
| Limited distribution | 不要 | 最大20台 | 開発者から招待を受けてインストール |
| 未登録アプリ | 不要 | ストア外の任意チャネル | Advanced Flowの追加保護を経てインストール |
| ADB | 開発用途の設定が必要 | 接続端末 | 従来のADBワークフローを維持 |

「最大20台」はAdvanced Flowの上限ではなく、学生・趣味開発者向けのLimited distributionアカウントに関する上限です。

## 利点と注意点

### 利点

- 即時操作を迫る詐欺に対して、再起動と1日待機で時間的な障壁を設けます。
- 未確認デベロッパー製アプリを全面禁止せず、理解した利用者に選択肢を残します。
- ADBによる開発・テスト経路は維持されます。

### 注意点

- 正当なOSSや小規模開発者のアプリでも、未登録なら利用者側の手順が増えます。
- 開発者の身元確認は、個々のアプリのコードが安全であることを保証する仕組みではありません。
- 公式発表は待機、再起動、認証の大枠を示していますが、Pixel固有の画面遷移やすべての文言までは固定していません。本書では未確認のボタン名や設定パスを手順として断定しません。
- 生体認証の内部処理、収集テレメトリ、カスタムROMでの扱いは、Advanced Flowの公式説明だけからは判断できません。

## 利用時の安全確認

- 通話、画面共有、遠隔操作中に解除しない。
- APKの配布元、署名、ハッシュ、公開ソース、更新経路を確認する。
- 「今すぐ」「口座を守るため」などと急かされた場合は操作を中止する。
- ADBは保護の迂回手段としてではなく、内容を検証できる開発用途に限定する。

## 公式情報

- [Android developer verification](https://developer.android.com/developer-verification)
- [Android developer verification guides](https://developer.android.com/developer-verification/guides)
- [Balancing openness and choice with safety](https://android-developers.googleblog.com/2026/03/android-developer-verification.html)
- [Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)
