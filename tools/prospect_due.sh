#!/bin/sh
# Prospecting cadence + coverage reporter. Parses orchestration/PROSPECTING.md's AREA TABLE.
# Emits a DUE line when the stalest areas need a sweep; prints coverage counts for STATUS.
# Zero quota, no network. Polled by the planner-session Monitor.
LEDGER="$HOME/workspace/claudecode/automath/orchestration/PROSPECTING.md"
STAMP="$HOME/workspace/claudecode/automath/logs/prospect_last_round"
DUE_AFTER_MIN=${1:-90}

[ -f "$LEDGER" ] || { echo "PROSPECT: ledger missing at $LEDGER"; exit 0; }

# Area rows: | math.XX | name | last_swept | sources | surfaced | in_pool |
rows=$(grep -E '^\| (math|cs)\.' "$LEDGER")
total=$(echo "$rows" | grep -c .)
never=$(echo "$rows" | awk -F'|' '{gsub(/ /,"",$4); if ($4=="NEVER") c++} END {print c+0}')
partial=$(echo "$rows" | awk -F'|' '{gsub(/ /,"",$4); if ($4=="PARTIAL?") c++} END {print c+0}')
swept=$((total - never - partial))

# The two stalest: NEVER first (alphabetical), then oldest date.
next=$(echo "$rows" | awk -F'|' '{gsub(/ /,"",$2); gsub(/ /,"",$4);
        if ($4=="NEVER") print "0000-00-00", $2;
        else if ($4=="PARTIAL?") print "0000-00-01", $2;
        else print $4, $2}' | sort | head -2 | awk '{printf "%s ", $2}')

echo "PROSPECT-COVERAGE: ${swept}/${total} areas swept, ${never} NEVER, ${partial} PARTIAL?; next up: ${next}"

now=$(date +%s)
last=0
[ -f "$STAMP" ] && last=$(cat "$STAMP" 2>/dev/null || echo 0)
case "$last" in *[!0-9]*|"") last=0 ;; esac
age_min=$(( (now - last) / 60 ))

if [ "$last" -eq 0 ]; then
  echo "PROSPECT-DUE: no sweep round recorded yet; dispatch sweep for: ${next}"
elif [ "$age_min" -ge "$DUE_AFTER_MIN" ]; then
  echo "PROSPECT-DUE: last sweep round ${age_min} min ago (threshold ${DUE_AFTER_MIN}); dispatch sweep for: ${next}"
fi
exit 0
