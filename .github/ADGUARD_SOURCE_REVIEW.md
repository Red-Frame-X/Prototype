# AdGuard Custom Rules の編集・Source査読チェックリスト

この手順は、Sourceの過剰収録、Version更新漏れ、未検証マージを防ぐためのものです。既存のルール・コメント・Sourceを無断で削除しません。

## Sourceを収録する条件

1. 既存の対象ルールと、公式Issue・Commitの対象ドメインだけでなく、**セレクタ、通信先、問題の種類、対処目的**が直接対応することを確認する。
2. 公式Commitの差分（追加・変更されたルール）を実際に確認し、IssueのClosed状態だけで「対処済み」と判断しない。
3. 対応が確証できないSourceや、同じドメインでも別件の資料は収録しない。必要ならPRの説明に候補と除外理由を記録する。
4. 無効化中のルールとの一致は「無効化中」と明記する。構文が異なる場合は完全一致と表現せず、差異を確認する。
5. 既存のSourceを削除する場合は、ユーザーが明示的に許可した範囲に限定する。Source以外の既存内容は維持する。

## Commit・CI・マージ

1. AdGuard Custom RulesまたはAdGuard DNS Custom Rulesを変更する**同じCommit内**で、対象ファイルの `! Version: YYYYMMDDHHMM` をJSTで更新する。PRの後続Commitで補うだけでは、Commit単位のVersion検査に失敗する。
2. PR作成前に差分を確認し、追加・削除した行、変更対象外の行、有効ルールの内容・順序を照合する。コメントのみの変更なら有効ルールが完全一致することを確認する。
3. PRのhead SHAに対する `check-adguard-version` と `quality` の**成功**を確認する。実行中・未取得・失敗は成功とみなさない。
4. マージ直前にPRのhead SHA・競合・レビュー状況を再確認する。許可された方法でマージする。
5. マージ後はPRのmerged状態、mainのファイル内容、マージCommitのWorkflowを確認する。実行中のWorkflowは未完了として報告する。
6. エラー発生時は失敗したStepと原因を特定し、最小限の修正・回帰検証を行う。検査の無効化や `continue-on-error` による隠蔽をしない。

## 過去の事例（2026-11-10）

- PR #279：Source追記CommitでVersionが未更新のため、`check-adguard-version` が失敗。Versionを同じCommitに含めた後継PR #280で解消。
- PR #280：同一ドメインの別問題までSourceとして収録。直接の関連性を再査読し、明示的な削除許可を得たPR #281でSource 12行と説明コメント6行を整理。
- PR #281：PRの両CI成功後にマージし、main反映とマージ後の `quality`・`update-version-timestamps` 成功を確認。

このチェックリストは査読の補助であり、実際のWebサイト上での動作確認や、Sourceの意味的な一致を自動保証するものではありません。
