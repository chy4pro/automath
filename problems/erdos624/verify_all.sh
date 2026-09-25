#!/usr/bin/env bash
# Re-check every archived artefact in certs/ without re-running the SAT solver.
#   witnesses : check/check_witness.py (independent of the encoder)
#   UNSAT     : check/audit_cnf.py (CNF == specification), sha256 against the log,
#               cake_lpr (CakeML-verified LRAT checker) and lrat-check (drat-trim repository)
# usage: ./verify_all.sh        (TOOLS=/path/to/dir-with-cake_lpr-and-lrat-check to override)
set -uo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/.local/bin:$PATH"
TB=${TOOLS:-/home/agent/tools/bin}
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
fail=0
for w in certs/witness_*.txt.gz; do
  b=$(basename "$w" .txt.gz); IFS=_ read -r _ n m v <<< "$b"
  out=$(python3 check/check_witness.py "$n" "$m" "$v" "$w" | tail -1)
  echo "($n,$m)_$v witness: $out"; [[ $out == RESULT:\ PASS* ]] || fail=1
done
for c in certs/unsat_*.cnf.gz; do
  b=$(basename "$c" .cnf.gz); IFS=_ read -r _ n m v sbt <<< "$b"; sb=${sbt#sb}
  zcat "$c" > "$tmp/f.cnf"; zcat "certs/$b.lrat.gz" > "$tmp/trim.lrat"
  a=$(python3 check/audit_cnf.py "$n" "$m" "$v" "$sb" "$tmp/f.cnf" | tail -1)
  h=$( (cd "$tmp" && sha256sum f.cnf trim.lrat) | diff - <(grep -E " (f.cnf|trim.lrat)$" "certs/$b.log.txt") >/dev/null && echo "sha256 ok" || echo "sha256 MISMATCH")
  k=$(ulimit -v 2097152; "$TB/cake_lpr" --CML_HEAP_SIZE=1400 --CML_STACK_SIZE=256 "$tmp/f.cnf" "$tmp/trim.lrat" | grep "^s ")
  l=$(ulimit -v 2097152; "$TB/lrat-check" "$tmp/f.cnf" "$tmp/trim.lrat" | grep -x "c VERIFIED")
  echo "($n,$m)_$v sb=$sb UNSAT: $a | $h | cake_lpr: $k | lrat-check: $l"
  [[ $a == AUDIT:\ PASS* && $h == "sha256 ok" && $k == "s VERIFIED UNSAT" && $l == "c VERIFIED" ]] || fail=1
done
[[ $fail == 0 ]] && echo "ALL ARCHIVED ARTEFACTS VERIFIED" || { echo "SOME CHECK FAILED"; exit 1; }
