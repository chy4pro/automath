#!/bin/sh
# wait for the pre-scan (16 prefix lines) then SAT-check survivors per prefix, 9 in parallel
cd "$(dirname "$0")"
while [ "$(grep -c '^prefix' lscan_k8.log)" -lt 16 ]; do sleep 20; done
ls k8_surv_*.txt | xargs -P 9 -L 1 sh -c 'python3 sat_survivors_k8.py "$0" 3000 2000000' > k8_sat.log 2>&1
echo DONE >> k8_sat.log
