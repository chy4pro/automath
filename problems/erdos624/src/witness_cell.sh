#!/usr/bin/env bash
# usage: src/witness_cell.sh n m variant sb [cpu_sec]
# Encode (n,m,variant) with symmetry-breaking level sb, solve with CaDiCaL under caps,
# decode the model to a full table of f, check it with the independent checker, gzip it into certs/.
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
CADICAL=${CADICAL:-$HOME/.elan/toolchains/leanprover--lean4---v4.34.0-rc1/bin/cadical}
n=$1; m=$2; v=$3; sb=$4; cpu=${5:-1800}
tag=w_${n}_${m}_${v}; mkdir -p runs
python3 src/encode.py --sb "$sb" "$n" "$m" "$v" > runs/$tag.cnf
python3 src/run_solver.py --tag $tag --cpu-sec "$cpu" -- "$CADICAL" -q runs/$tag.cnf || true
if head -1 runs/$tag.out | grep -q "^s SATISFIABLE"; then
  python3 src/encode.py --decode --sb "$sb" "$n" "$m" "$v" runs/$tag.out > runs/$tag.txt
  python3 check/check_witness.py "$n" "$m" "$v" runs/$tag.txt --selftest | tee runs/$tag.check
  gzip -9 -n -c runs/$tag.txt > certs/witness_${n}_${m}_${v}.txt.gz
  cp runs/$tag.check certs/witness_${n}_${m}_${v}.check.txt
  rm -f runs/$tag.cnf runs/$tag.out runs/$tag.txt
else
  echo "$tag: $(head -1 runs/$tag.out)"
fi
