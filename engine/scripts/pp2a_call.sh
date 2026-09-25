#!/bin/bash
# pp2a_call.sh <brief_file> <out_file> [max_tokens] [curl_timeout] [temperature]
#
# NEW FILE — does NOT modify the shared engine_call_big.sh / engine_batch.sh.
# Reason it exists (owner-w133 round 36): engine_call_big.sh hard-codes temperature 0.
# Five temperature-0 calls on a byte-identical brief are ONE judge replicated, so the
# PP2A power bound (>= 1/n) would be a fiction at any n. This dispatcher takes the
# temperature as an argument so the five draws per arm are genuinely independent.
# Recorded pre-dispatch in problems/wowii/w133_r36_pp2a_dispatch_prereg.md section 3.
#
# Everything else follows engine_call_big.sh: OpenRouter, key never echoed, empty-body
# retry with backoff (burst-rate drop is retryable, reasoning-burn is not), and a burned
# call preserves its reasoning trace as evidence rather than vanishing.
set -u
source "$HOME/.automath_engine_keys"
BRIEF="$1"; OUTF="$2"; MT="${3:-32000}"; TMO="${4:-900}"; TEMP="${5:-1.0}"
MODEL="stealth/ox-alpha"
URL="https://openrouter.ai/api/v1/chat/completions"; KEY="$OR_KEY"
HDRF=$(mktemp); chmod 600 "$HDRF"
printf 'Authorization: Bearer %s\n' "$KEY" > "$HDRF"
trap 'rm -f "$HDRF"' EXIT
RAW="${OUTF%.md}.raw.json"
mkdir -p "$(dirname "$OUTF")"

call () {
  jq -n --arg m "$MODEL" --rawfile p "$BRIEF" --argjson mt "$MT" --argjson t "$TEMP" \
    '{model:$m, max_tokens:$mt, temperature:$t,
      reasoning:{effort:"medium"},
      messages:[{role:"user",content:$p}]}' \
  | curl -sS --max-time "$TMO" "$URL" -H @"$HDRF" \
      -H "Content-Type: application/json" -d @-
}

backoffs=(15 45 135)
attempt=0
while :; do
  call > "$RAW"
  if [ -s "$RAW" ]; then
    content=$(jq -r '.choices[0].message.content // empty' "$RAW" 2>/dev/null)
    fin_now=$(jq -r '.choices[0].finish_reason // "?"' "$RAW" 2>/dev/null)
    if [ -n "$content" ] || [ "$fin_now" = "length" ]; then break; fi
  fi
  if [ "$attempt" -ge 3 ]; then break; fi
  sleep "${backoffs[$attempt]}"
  attempt=$((attempt+1))
done

content=$(jq -r '.choices[0].message.content // empty' "$RAW" 2>/dev/null)
fin=$(jq -r '.choices[0].finish_reason // "?"' "$RAW" 2>/dev/null)
ct=$(jq -r '.usage.completion_tokens // "?"' "$RAW" 2>/dev/null)
err=$(jq -r '.error.message // empty' "$RAW" 2>/dev/null)

if [ -n "$content" ]; then
  printf '%s\n' "$content" > "$OUTF"
  echo "OK $OUTF ($(wc -c < "$OUTF") bytes) finish=$fin ct=$ct temp=$TEMP retries=$attempt"
else
  { echo "# BURNED CALL — no content returned (NOT an API error)"
    echo "model: $MODEL  finish_reason: $fin  completion_tokens: $ct  max_tokens: $MT  temperature: $TEMP"
    [ -n "$err" ] && echo "api error message: $err"
    echo
    echo "## reasoning trace (verbatim) — evidence, NOT a deliverable"
    jq -r '.choices[0].message.reasoning // "(none)"' "$RAW"
  } > "$OUTF"
  echo "BURNED $OUTF finish=$fin ct=$ct temp=$TEMP retries=$attempt"
fi
