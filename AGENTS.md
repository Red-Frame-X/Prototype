# Repository editing safeguards

- Correct inaccurate descriptions to verified, accurate content rather than
  deleting them. Preserve their context and useful information. If a correction
  cannot be verified, report the uncertainty instead of removing the passage.
- Preserve all content outside the user's requested scope. Never substantially
  delete, shorten, consolidate, or replace Markdown or custom filters without
  explicit user authorization for that removal.
- For narrowly scoped deletion requests, start from the complete current file,
  remove only the exact requested lines or block, and compare before/after before
  writing. Abort the edit if the diff contains any unrelated deletion or change.
- Never use truncated fetch output as replacement file content. If the complete
  file cannot be obtained, do not perform a whole-file replacement.
- Make focused patches against the current file. Do not reconstruct existing
  documents from memory, summaries, or truncated tool output.
- Do not invent facts, citations, settings, or verification results. Check
  technical claims against authoritative sources; leave unverified claims
  unchanged unless the user asks for their review, and disclose uncertainty.
- Before committing and merging, inspect the complete diff, including deleted
  lines, and verify that no unrelated content was lost or changed. Run the
  relevant tests and content-loss guard. Do not weaken a guard merely to pass CI.
- Line-count checks cannot establish factual accuracy or detect every harmful
  rewrite. Review replacements for meaning as well as net line loss. A passing
  check does not authorize deletions or unsupported factual changes.
- When writing or revising Japanese documentation, prioritize clear, natural Japanese used in ordinary human communication. Avoid unnecessarily stiff, mechanical, or formulaic wording while preserving technical accuracy and the original meaning.

## Codex code review language

- Write all GitHub Codex code review findings, summaries, explanations, severity assessments, and recommended fixes in natural Japanese.
- Preserve code identifiers, file paths, commands, logs, and quoted error messages in their original form when accuracy requires it.
- Apply this language preference to automatic pull request reviews and reviews requested with `@codex review`.

## コミットタイトルの言語

- コミットメッセージのタイトル（1行目）は、変更内容が伝わる自然な日本語で書く。
- `docs:`、`fix:` などの種別、コード識別子、ファイル名、製品名、PR番号は必要に応じて原表記を保持する。
- 自動生成するコミット、マージコミット、取り消しコミットにも日本語のタイトルを使う。
- PRのタイトルも日本語で書き、マージ時に作成するコミットのタイトルを日本語にする。
- `npm run hooks:install` でコミットフックを有効にする。CIでも新しいコミットのタイトルを検査する。
