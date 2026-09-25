#!/bin/sh
# Publication feedback watch (user directive 08-18). Polled by the planner-session
# Monitor. Emits one line per NEW event since the last poll; silent when nothing new.
# State file keeps last-seen counts. Transient failures are swallowed (|| true).
STATE="$HOME/workspace/claudecode/automath/logs/pub_watch_state"
mkdir -p "$(dirname "$STATE")" 2>/dev/null || true
touch "$STATE"

check () { # key current_value label
  key="$1"; cur="$2"; label="$3"
  [ -z "$cur" ] && return 0
  prev=$(grep "^$key=" "$STATE" | tail -1 | cut -d= -f2)
  if [ -n "$prev" ] && [ "$cur" != "$prev" ]; then
    echo "PUBWATCH: $label changed: $prev -> $cur"
  fi
  grep -v "^$key=" "$STATE" > "$STATE.tmp" 2>/dev/null || true
  echo "$key=$cur" >> "$STATE.tmp"; mv "$STATE.tmp" "$STATE"
}

for pr in 5023 5027 5028 5029; do
  c=$(gh api "repos/google-deepmind/formal-conjectures/issues/$pr/comments" --jq 'length' 2>/dev/null) || true
  r=$(gh api "repos/google-deepmind/formal-conjectures/pulls/$pr/reviews" --jq 'length' 2>/dev/null) || true
  st=$(gh api "repos/google-deepmind/formal-conjectures/pulls/$pr" --jq '.state + "/" + (.merged|tostring)' 2>/dev/null) || true
  check "pr${pr}_comments" "$c" "PR #$pr comment count"
  check "pr${pr}_reviews" "$r" "PR #$pr review count"
  check "pr${pr}_state" "$st" "PR #$pr state(open-merged)"
done

for repo in automath-papers automath-lean-proofs; do
  i=$(gh api "repos/chy4pro/$repo" --jq '.open_issues_count' 2>/dev/null) || true
  check "${repo}_issues" "$i" "$repo open issues"
done

# 2026-08-23 (doctrine 89): Zenodo serves CONCEPT-LEVEL aggregate stats on every version
# record, so all versions of one work report identical numbers. The old loop therefore
# emitted N alerts for ONE event (four fired at 16:4x for the same 677 concept) and made
# outside interest look 4x larger than it is. Group by conceptrecid: one row per concept,
# keyed by the concept id, reporting the aggregate ONCE.
#
# Also recorded so it is never misread: these views/downloads are the CONCEPT total across
# every version since first publication. They CANNOT tell us whether the corrected version
# is the one being read. Do not quote them as evidence that a correction reached anyone.
declare -a SEEN_CONCEPTS=()
for rec in 21995453 21995604 21995715 21995800 22054651 22054835 22054879 22069069 22069570 22070405; do
  read -r concept stats <<<"$(curl -s --max-time 15 "https://zenodo.org/api/records/$rec" | python3 -c 'import sys,json
d=json.load(sys.stdin); s=d.get("stats",{})
print("%s %sv/%sd" % (d.get("conceptrecid","?"), s.get("views",0), s.get("downloads",0)))')" || true
  [ -z "$concept" ] && continue
  dup=0
  for c in "${SEEN_CONCEPTS[@]}"; do [ "$c" = "$concept" ] && dup=1 && break; done
  [ "$dup" = "1" ] && continue
  SEEN_CONCEPTS+=("$concept")
  check "zenconcept${concept}" "$stats" "Zenodo concept $concept (all versions) views/downloads"
done
exit 0
