#!/bin/bash
# engine_call.sh <or|meta> <model_id> <brief_file> <out_file> [max_tokens]
# Reusable single-call dispatcher for quarantined engines. Sources keys itself.
# Ops rules (summary_0822): max_tokens>=8000 default, retry once on 5xx/timeout,
# never echo keys, output lands in the sandbox only.
set -u
source "$HOME/.automath_engine_keys"
PROVIDER="$1"; MODEL="$2"; BRIEF="$3"; OUTF="$4"; MT="${5:-8000}"
if [ "$PROVIDER" = "or" ]; then
  URL="https://openrouter.ai/api/v1/chat/completions"; KEY="$OR_KEY"
else
  URL="https://opencode.ai/zen/go/v1/chat/completions"; KEY="$OC_GO_KEY"
fi
HDRF=$(mktemp)
chmod 600 "$HDRF"
printf 'Authorization: Bearer %s\n' "$KEY" > "$HDRF"
trap 'rm -f "$HDRF"' EXIT
call () {
  jq -n --arg m "$MODEL" --rawfile p "$BRIEF" --argjson mt "$MT" \
    '{model:$m, max_tokens:$mt, temperature:0, messages:[{role:"user",content:$p}]}' \
  | curl -sS --max-time "${TMO:-600}" "$URL" -H @"$HDRF" \
      -H "Content-Type: application/json" -d @-
}
resp=$(call)
content=$(echo "$resp" | jq -r '.choices[0].message.content // empty')
if [ -z "$content" ]; then
  sleep 10
  resp=$(call)
  content=$(echo "$resp" | jq -r '.choices[0].message.content // ("API-ERROR: " + (.error.message // "unknown"))')
fi
mkdir -p "$(dirname "$OUTF")"
printf '%s\n' "$content" > "$OUTF"
echo "wrote $OUTF ($(wc -c < "$OUTF") bytes)"
