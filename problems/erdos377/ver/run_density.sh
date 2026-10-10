#!/bin/bash
M=$1
S=$(date +%s.%N)
~/.venv-automath/bin/python /work/engine/harvest/erdos377_r1_astra_data/density_intervals.py --mesh $M --levels 64 --terms 8 > rerun_$M.txt
E=$(date +%s.%N)
python3 -c "print('wall_seconds',$E-$S)" > time_$M.txt
