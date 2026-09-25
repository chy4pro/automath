#!/bin/bash
# Model capability probe for automath role fit. Keys via env: OR_KEY, META_KEY.
# Usage: model_probe.sh <provider: or|meta> <model_id> <label>
set -u
PROVIDER="$1"; MODEL="$2"; LABEL="$3"
OUT="$HOME/workspace/claudecode/automath/notes/case_intel/model_tests"
mkdir -p "$OUT"

if [ "$PROVIDER" = "or" ]; then
  URL="https://openrouter.ai/api/v1/chat/completions"; KEY="$OR_KEY"
else
  URL="https://opencode.ai/zen/go/v1/chat/completions"; KEY="$META_KEY"
fi

run_test () {
  local tname="$1"; local prompt="$2"
  local body resp content
  body=$(jq -n --arg m "$MODEL" --arg p "$prompt" \
    '{model:$m, max_tokens:2000, temperature:0, messages:[{role:"user",content:$p}]}')
  resp=$(curl -sS --max-time 180 "$URL" -H "Authorization: Bearer $KEY" \
    -H "Content-Type: application/json" -d "$body")
  content=$(echo "$resp" | jq -r '.choices[0].message.content // ("API-ERROR: " + (.error.message // "unknown"))')
  printf '%s\n' "$content" > "$OUT/${LABEL}_${tname}.md"
  echo "== ${LABEL} ${tname} (first 300 chars) =="
  printf '%s\n' "$content" | head -c 300; echo; echo
  sleep 3
}

T1='Compute 27*43. Reply with the number only.'

T2='Referee the following proof. Start your reply with exactly "VERDICT: CLEAN" or "VERDICT: FLAWED", then one short paragraph. If flawed, identify the exact flawed step and give a counterexample if one exists.

Theorem: Every group of order p^2 (p prime) is cyclic.
Proof: Let G have order p^2. The center Z(G) is nontrivial, so |Z(G)| is p or p^2. If |Z(G)| = p^2 then G is abelian. If |Z(G)| = p then G/Z(G) has order p, hence cyclic, and a group whose quotient by its center is cyclic is abelian; contradiction with |Z(G)| = p, so G is abelian in all cases. Now an abelian group of order p^2 contains an element of maximal order, and in an abelian p-group the maximal element order equals the group exponent, which for order p^2 must be p^2; hence G has an element of order p^2 and is cyclic. QED'

T3='How many positive integers n with 1 <= n <= 1000 satisfy 101 | n^2 + 1? Work it out rigorously. End your reply with the line "ANSWER: <number>".'

T4='Summarize the main lemma of the paper "Residue chains in bipartite towers" by T. Ordowski and R. Fernandes (Journal of Combinatorial Theory Series A, 2019). If you cannot verify that this paper exists, reply with exactly "UNKNOWN-SOURCE" and nothing else.'

run_test sanity "$T1"
run_test referee "$T2"
run_test solver "$T3"
run_test honesty "$T4"
echo "DONE ${LABEL}"
