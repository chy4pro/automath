#!/bin/bash
# Self-service push for the Lean loop (Codex or coordinator). Commits ONLY lean/sidon30/** and pushes to main.
# Usage: tools/sidon30_push.sh "commit message"
set -euo pipefail
cd /work
TOK_FILE=/wb/creds/github-token/value
[ -r "$TOK_FILE" ] || { echo "no token mount at $TOK_FILE — ask the owner to grant github-token to this session"; exit 2; }
AUTH="AUTHORIZATION: basic $(printf 'x-access-token:%s' "$(cat "$TOK_FILE")" | base64 | tr -d '\n')"
G=(git -c credential.helper= -c "http.https://github.com/.extraheader=$AUTH" -c user.name=chy4pro -c user.email=chy4pro@users.noreply.github.com)
git add lean/sidon30
# refuse anything staged outside lean/sidon30
if git diff --cached --name-only | grep -v '^lean/sidon30/' | grep -q .; then echo "staged files outside lean/sidon30 — unstage them first"; git diff --cached --name-only | grep -v '^lean/sidon30/'; exit 3; fi
git diff --cached --quiet && { echo "nothing to commit"; exit 0; }
# privacy grep on the staged diff
if git diff --cached | grep -E -i "roychen|chatgpt\.com/c/|claude\.ai/.*session|gmail|chenhaoyu1995" >/dev/null; then echo "privacy grep hit — fix before pushing"; exit 4; fi
git commit -q -m "${1:-sidon30: Lean update}

Co-Authored-By: GPT-6 Astra (Codex) <noreply@openai.com>"
"${G[@]}" pull -q --rebase origin main
"${G[@]}" push -q origin HEAD:main
git log --oneline -1
