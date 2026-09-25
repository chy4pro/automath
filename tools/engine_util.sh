#!/bin/sh
# engine_util.sh -- engine utilization DIAGNOSTIC.
#
# ⚠️ NOT A SCORE. NOT A TARGET. There is no floor and there is no "violation".
# User correction 2026-08-23 (inbox/directive_engine_saturation_CORRECTION.md):
# a utilization floor "turns a KPI into a goal and invites make-work". Withdrawn.
#
# Idle engines are a SIGNAL TO DIAGNOSE, in this order:
#   1. DISPATCH GAP    -- real work exists but nobody sent it  -> dispatch the WORK
#   2. PROSPECTING GAP -- the pool is thin                      -> fix the finding line
#   3. VERIFICATION BOTTLENECK -- Claude capacity consumed      -> say so; it is a
#                                                                  prioritization question
#   4. NOTHING VALUABLE TO DO -- then IDLE IS CORRECT. Zero output is fine.
# Never dispatch filler to move this number.
SB="$HOME/workspace/claudecode/automath-sandbox"
[ -d "$SB/out" ] || { echo "ENGINE: sandbox out/ missing at $SB"; exit 0; }

now=$(date +%s)
inflight=$(ps axo command | grep -E "engine_call|engine_batch" | grep -v grep | wc -l | tr -d ' ')
last=$(find "$SB/out" -type f -name "*_out.md" -exec stat -f "%m" {} \; 2>/dev/null | sort -n | tail -1)
if [ -z "$last" ]; then idle_min="n/a"; else idle_min=$(( (now - last) / 60 )); fi
# NOTE: `-newermt "-6H"` FAILS on this system's find (bfs): "Invalid timestamp".
# With 2>/dev/null it returned 0 silently -- a swallowed error reported as a measurement,
# the exact species doctrine 54 was written about, in a tool written AFTER writing 54.
# `-mmin -360` is portable. Errors are NOT suppressed here on purpose.
# 2026-08-23 (doctrine 133/134): counting *_out.md counts FILES, not ANSWERS. Three of the
# last six hours' "outputs" were two API-ERROR strings and a burned call -- the meter read
# healthy while the channel was returning errors. Apply the same POSITIVE test the landing
# monitor uses: an answer clears a size floor AND opens with no known non-answer marker.
six_files=$(find "$SB/out" -type f -name "*_out.md" -mmin -360 | wc -l | tr -d ' ')
six=0; six_bad=0
for f in $(find "$SB/out" -type f -name "*_out.md" -mmin -360 2>/dev/null); do
  sz=$(stat -f '%z' "$f" 2>/dev/null); sz=${sz:-0}
  if head -c 400 "$f" 2>/dev/null | grep -qiE "BURNED CALL|^API-ERROR|^ERROR:|Provider returned error|rate.?limit|quota"; then
    six_bad=$((six_bad+1))
  elif [ "$sz" -lt 800 ]; then
    six_bad=$((six_bad+1))
  else
    six=$((six+1))
  fi
done
pend=$(grep -c "| PENDING |" "$HOME/workspace/claudecode/automath/orchestration/ENGINE_BACKLOG.md" 2>/dev/null || echo "?")

echo "ENGINE-DIAG: last6h=${six} ANSWERS (+${six_bad} non-answers of ${six_files} files) | in-flight=${inflight} | idle=${idle_min}min | real backlog items PENDING=${pend}"
# Recency guard (08-23): a 6h count reports HISTORY. After the 20:4x outage the meter kept
# warning "channel is failing" while two clean briefs had already landed. What decides whether the
# channel works NOW is the NEWEST output, not the 6h tally. Same defect as the failure-watcher's
# missing age filter (doctrine 87b/95) -- in the instrument I use to judge the others.
newest=$(find "$SB/out" -type f -name "*_out.md" -mmin -360 -exec stat -f "%m %N" {} \; 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
newest_ok=1
if [ -n "$newest" ]; then
  nsz=$(stat -f '%z' "$newest" 2>/dev/null); nsz=${nsz:-0}
  if head -c 400 "$newest" 2>/dev/null | grep -qiE "BURNED CALL|^API-ERROR|^ERROR:|Provider returned error|rate.?limit|quota"; then newest_ok=0
  elif [ "$nsz" -lt 800 ]; then newest_ok=0; fi
fi
if [ "${six_bad:-0}" -gt 0 ] && [ "$newest_ok" = "0" ]; then echo "ENGINE-DIAG: ⚠️ CHANNEL FAILING NOW -- the most recent output is a non-answer, and ${six_bad} of the last ${six_files} were. Check RESOURCES.md before dispatching (doctrine 133/134)."
elif [ "${six_bad:-0}" -gt 0 ]; then echo "ENGINE-DIAG: ${six_bad} of the last ${six_files} outputs were non-answers, but the NEWEST output is a real answer -- that is HISTORY (an earlier outage), not a current fault. Channel currently OK."
fi
if false; then echo "ENGINE-DIAG: ⚠️ ${six_bad} of the last ${six_files} outputs were NOT answers (burned call / API-ERROR / below size floor). A non-zero count here means the CHANNEL is failing, not that work was done -- check RESOURCES.md before dispatching (doctrine 133/134)."; fi
echo "ENGINE-DIAG: this is a diagnostic, not a score. FIFTH CAUSE, added 08-23: a BLOCKED CHANNEL -- work exists and is dispatchable but the endpoint refuses it. Check the non-answer count above and RESOURCES.md BEFORE concluding dispatch gap; idle with parked briefs and a failing channel is CORRECT, not a gap. If idle and PENDING>0 -> dispatch gap. If idle and PENDING=0 -> ask whether the pool is thin, whether Claude-side adjudication is the bottleneck, or whether there is genuinely nothing worth sending (in which case idle is correct)."
exit 0
