#!/bin/bash
# engine_batch.sh <or|meta> <model_id> <max_tokens> <out_dir> <brief1> [brief2 ...]
# Rate-limit preset (dialogue 08-22): concurrency cap 4, staggered starts (5s),
# per-call retries live inside engine_call_big.sh. Step the cap up only after a
# clean batch. Logs land beside outputs.
set -u
PROVIDER="$1"; MODEL="$2"; MT="$3"; OUTDIR="$4"; shift 4
CAP=${ENGINE_BATCH_CAP:-4}
SCRIPT="$(dirname "$0")/engine_call_big.sh"
mkdir -p "$OUTDIR"
i=0
for b in "$@"; do
  while [ "$(jobs -rp | wc -l)" -ge "$CAP" ]; do sleep 3; done
  name=$(basename "${b%.md}")
  "$SCRIPT" "$PROVIDER" "$MODEL" "$b" "$OUTDIR/${name}_out.md" "$MT" \
     > "$OUTDIR/${name}.log" 2>&1 &
  i=$((i+1)); sleep 5
done
wait
echo "batch done: $i briefs -> $OUTDIR (cap $CAP)"
