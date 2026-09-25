#!/bin/bash
# engine_call_big.sh <or|meta> <model_id> <brief_file> <out_file> [max_tokens] [curl_timeout]
#
# Same contract as engine_call.sh, but sized for REASONING-HEAVY engines on long briefs.
#
# WHY THIS EXISTS (owner-w133, 2026-08-22 09:1x CDT, diagnosed from a raw response):
#   stealth/ox-alpha and muse-spark-1.2 both stream their chain of thought into
#   `.choices[0].message.reasoning` and only then start `.choices[0].message.content`.
#   On a ~14 KB brief with max_tokens=8000 the raw response came back with
#   `finish_reason: "length"`, `completion_tokens: 8000`, `reasoning` = 21 340 chars and
#   **content = empty string**. engine_call.sh then reports `API-ERROR: unknown`, because
#   it only looks at `.content`. So the "API error" was never an API error at all: the
#   budget was exhausted mid-thought. The README's `max_tokens >= 8000` floor is NOT
#   enough for briefs of this size.
#
# Fixes applied here:
#   * default max_tokens 64000 (not 8000)
#   * default curl timeout 1500s (a 64k-token generation outruns 600s)
#   * asks OpenRouter to cap reasoning effort, so budget goes to the answer
#   * on empty content it SAVES THE REASONING TRACE instead of discarding it, and writes a
#     diagnostic header, so a burned call is still evidence rather than a lost round
#   * never echoes keys
set -u
source "$HOME/.automath_engine_keys"
PROVIDER="$1"; MODEL="$2"; BRIEF="$3"; OUTF="$4"; MT="${5:-64000}"; TMO="${6:-1500}"
if [ "$PROVIDER" = "or" ]; then
  URL="https://openrouter.ai/api/v1/chat/completions"; KEY="$OR_KEY"
else
  URL="https://opencode.ai/zen/go/v1/chat/completions"; KEY="$OC_GO_KEY"
fi
HDRF=$(mktemp)
chmod 600 "$HDRF"
printf 'Authorization: Bearer %s\n' "$KEY" > "$HDRF"
trap 'rm -f "$HDRF"' EXIT
RAW="${OUTF%.md}.raw.json"
mkdir -p "$(dirname "$OUTF")"

call () {
  jq -n --arg m "$MODEL" --rawfile p "$BRIEF" --argjson mt "$MT" \
    '{model:$m, max_tokens:$mt, temperature:0,
      reasoning:{effort:"medium"},
      messages:[{role:"user",content:$p}]}' \
  | curl -sS --max-time "${TMO:-600}" "$URL" -H @"$HDRF" \
      -H "Content-Type: application/json" -d @-
}

# Rate-limit preset (dialogue diagnostic 08-22 09:2x): EMPTY raw body = burst-rate drop,
# a RETRYABLE event, never a verdict. Distinguish it from reasoning-burn (raw body
# non-empty, finish=length, content empty — do NOT retry that here; it needs a bigger
# budget or a shorter brief, and the trace is preserved below).
backoffs=(15 45 135)
attempt=0
while :; do
  call > "$RAW"
  if [ -s "$RAW" ]; then
    content=$(jq -r '.choices[0].message.content // empty' "$RAW" 2>/dev/null)
    fin_now=$(jq -r '.choices[0].finish_reason // "?"' "$RAW" 2>/dev/null)
    # retry only on empty-body-equivalent failures: no parse, or transient 5xx error field
    errnow=$(jq -r '.error.message // empty' "$RAW" 2>/dev/null)
    if [ -n "$content" ] || [ "$fin_now" = "length" ]; then break; fi
    if [ -z "$errnow" ] && [ "$fin_now" = "?" ]; then :; fi   # unparseable → retryable
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
  echo "wrote $OUTF ($(wc -c < "$OUTF") bytes)  finish=$fin completion_tokens=$ct"
else
  { echo "# BURNED CALL — no \`content\` returned (this is NOT an API error)"
    echo
    echo "model: $MODEL   finish_reason: $fin   completion_tokens: $ct   max_tokens: $MT"
    [ -n "$err" ] && echo "api error message: $err"
    echo
    echo "The engine spent the whole budget in hidden reasoning. The trace is preserved"
    echo "below as evidence; it is NOT a deliverable and must not be adjudicated as one."
    echo
    echo '## reasoning trace (verbatim)'
    echo
    jq -r '.choices[0].message.reasoning // "(none)"' "$RAW"
  } > "$OUTF"
  echo "BURNED: $OUTF  finish=$fin completion_tokens=$ct (raw kept at $RAW)"
fi
