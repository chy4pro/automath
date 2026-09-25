#!/bin/sh
cd "$(dirname "$0")"
cat k8_prefixes3.txt | xargs -P 9 -L 1 sh -c 'python3 lscan_k8_3.py "$0" "$1" "$2" 3000' > lscan_k8_3.log 2>&1
ls k8_surv_*.txt | xargs -P 9 -L 1 sh -c 'python3 irr_dfs_k8.py "$0" 2400' > k8_irr.log 2>&1
echo DONE >> k8_irr.log
