#!/usr/bin/env bash
# usage: src/certify_unsat.sh n m variant sb [cpu_sec]
# 1 encode; 2 independent CNF audit; 3 CaDiCaL with DRAT proof; 4 drat-trim backward check
# emitting a trimmed LRAT proof; 5 check the trimmed LRAT with cake_lpr (CakeML-verified) and
# with lrat-check (drat-trim repo); 6 store gzipped CNF + trimmed LRAT + logs in certs/;
# delete the raw DRAT.  Every tool runs under run_solver.py caps (2 GB address space, cpu_sec).
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
CADICAL=${CADICAL:-$HOME/.elan/toolchains/leanprover--lean4---v4.34.0-rc1/bin/cadical}
TB=${TOOLS:-/home/agent/tools/bin}
n=$1; m=$2; v=$3; sb=$4; cpu=${5:-1800}
tag=u_${n}_${m}_${v}_sb${sb}
R=runs/$tag; mkdir -p $R
python3 src/encode.py --sb "$sb" "$n" "$m" "$v" > $R/f.cnf
python3 check/audit_cnf.py "$n" "$m" "$v" "$sb" $R/f.cnf | tee $R/audit.txt
grep -q "AUDIT: PASS" $R/audit.txt
python3 src/run_solver.py --tag ${tag}_solve --cpu-sec "$cpu" --stdout $R/solve.out -- "$CADICAL" -q $R/f.cnf $R/raw.drat || true
head -1 $R/solve.out
if ! grep -q "^s UNSATISFIABLE" $R/solve.out; then echo "$tag: not UNSAT within cap"; rm -f $R/raw.drat; exit 3; fi
ls -l $R/raw.drat | awk '{print "raw DRAT bytes:", $5}' | tee $R/sizes.txt
python3 src/run_solver.py --tag ${tag}_dratrim --cpu-sec "$cpu" --stdout $R/dratrim.out -- $TB/drat-trim $R/f.cnf $R/raw.drat -L $R/trim.lrat -w || true
tr '\r' '\n' < $R/dratrim.out > $R/dratrim.txt   # drat-trim writes progress with carriage returns
grep -E "^s |core" $R/dratrim.txt
grep -q "^s VERIFIED" $R/dratrim.txt
rm -f $R/raw.drat
ls -l $R/trim.lrat | awk '{print "trimmed LRAT bytes:", $5}' | tee -a $R/sizes.txt
python3 src/run_solver.py --tag ${tag}_cakelpr --cpu-sec "$cpu" --stdout $R/cakelpr.out -- $TB/cake_lpr --CML_HEAP_SIZE=1400 --CML_STACK_SIZE=256 $R/f.cnf $R/trim.lrat || true
python3 src/run_solver.py --tag ${tag}_lratcheck --cpu-sec "$cpu" --stdout $R/lratcheck.out -- $TB/lrat-check $R/f.cnf $R/trim.lrat || true
grep "^s " $R/cakelpr.out; grep -x "c VERIFIED" $R/lratcheck.out
grep -q "^s VERIFIED UNSAT" $R/cakelpr.out
grep -qx "c VERIFIED" $R/lratcheck.out      # lrat-check prints 'c VERIFIED' iff the empty clause was checked
gzip -9 -n -c $R/f.cnf > certs/unsat_${n}_${m}_${v}_sb${sb}.cnf.gz
gzip -9 -n -c $R/trim.lrat > certs/unsat_${n}_${m}_${v}_sb${sb}.lrat.gz
{ echo "cell (${n},${m})_${v}, symmetry-breaking level sb=${sb}"; cat $R/audit.txt; echo "--- cadical"; head -1 $R/solve.out;
  echo "--- drat-trim"; grep -E "^s |core" $R/dratrim.txt; cat $R/sizes.txt;
  echo "--- cake_lpr"; cat $R/cakelpr.out; echo "--- lrat-check"; grep -E "VERIFIED|Added" $R/lratcheck.out;
  echo "--- sha256 (uncompressed)"; sha256sum $R/f.cnf $R/trim.lrat | sed "s#$R/##"; } > certs/unsat_${n}_${m}_${v}_sb${sb}.log.txt
rm -rf $R
echo "$tag CERTIFIED"
