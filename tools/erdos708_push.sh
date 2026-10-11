#!/bin/bash
# Self-service push for the #708 Lean loop (formalizer or coordinator). Commits ONLY lean/** and
# .github/workflows/** inside the problems/erdos708/repo submodule and pushes its main branch.
# Usage: tools/erdos708_push.sh "commit message"
set -euo pipefail
cd /work/problems/erdos708/repo
TOK_FILE=/wb/creds/github-token/value
[ -r "$TOK_FILE" ] || { echo "no token mount at $TOK_FILE — ask the chat session to grant github-token to this workspace"; exit 2; }
AUTH="AUTHORIZATION: basic $(printf 'x-access-token:%s' "$(cat "$TOK_FILE")" | base64 | tr -d '\n')"
G=(git -c credential.helper= -c "http.https://github.com/.extraheader=$AUTH" -c user.name=chy4pro -c user.email=chy4pro@users.noreply.github.com)
git add lean
[ -d .github/workflows ] && git add .github/workflows
if git diff --cached --name-only | grep -v -E '^(lean/|\.github/workflows/)' | grep -q .; then echo "staged files outside lean/ and .github/workflows/ — unstage them first"; git diff --cached --name-only | grep -v -E '^(lean/|\.github/workflows/)'; exit 3; fi
git diff --cached --quiet && { echo "nothing to commit"; exit 0; }
if git diff --cached | grep -E -i "roychen|chatgpt\.com/c/|claude\.ai/.*session|gmail|chenhaoyu1995|/Users/" >/dev/null; then echo "privacy grep hit — fix before pushing"; exit 4; fi
git commit -q -m "${1:-erdos708: Lean update}

Co-Authored-By: GPT-6 Astra (Codex) <noreply@openai.com>"
if ! "${G[@]}" push -q origin HEAD:main 2>/dev/null; then
  "${G[@]}" fetch -q origin main
  "${G[@]}" -c rebase.autoStash=true rebase -q origin/main
  "${G[@]}" push -q origin HEAD:main
fi
git log --oneline -1
