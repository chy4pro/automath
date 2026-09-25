#!/bin/bash
# PP2A round-36 dispatch: 15 slots (5 judges x 3 arms) to the free engine channel.
# INTERLEAVED by design (A1,B1,D1,A2,B2,D2,...): running one arm to completion before the
# next would confound ARM with TIME-OF-DISPATCH, and any drift in channel state would then
# be indistinguishable from the plant effect. Cap 4 concurrent, 5s stagger (README rule 7).
set -u
SB="$HOME/workspace/claudecode/automath-sandbox"
BR="$SB/briefs/pp2a_r36"
OD="$SB/out/ox-alpha/pp2a_r36"
CALL="$SB/scripts/pp2a_call.sh"
CAP=4
mkdir -p "$OD"
n=0
for j in 1 2 3 4 5; do
  for arm in A B D; do
    while [ "$(jobs -rp | wc -l)" -ge "$CAP" ]; do sleep 3; done
    "$CALL" "$BR/pp2a_${arm}_j${j}.md" "$OD/pp2a_${arm}_j${j}_out.md" 32000 900 1.0 \
      > "$OD/pp2a_${arm}_j${j}.log" 2>&1 &
    n=$((n+1)); sleep 5
  done
done
wait
echo "PP2A batch done: $n slots dispatched -> $OD"
grep -h . "$OD"/*.log | sed 's#.*/pp2a_#pp2a_#'
