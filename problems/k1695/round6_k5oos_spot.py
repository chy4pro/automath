#!/usr/bin/env python3
"""ROUND 6-J: spot-check K5-OOS witnesses (q = 11, 13; all n <= 30) with MY pair_candidate
(round4_reciprocal.py), which predates every K5 submission.  A witness must be CLEAN
(pair_candidate False).  Control: the all-ones placement on the same positions in a NONE cell
of the same (q,n,k) must be DIRTY when the NONE cell is k = n (full support)."""
import sys, csv, json
sys.stdout.reconfigure(line_buffering=True)
src = open("problems/k1695/round4_reciprocal.py").read()
G = {}
cut = src.index('print("ROUND 4-B')
exec(compile(src[:cut], "r4r", "exec"), G)
GF, pair_candidate = G['GF'], G['pair_candidate']
rows = list(csv.DictReader(open("problems/k1695/k5_oos/k5_gfq_oos_q11_13_16_n30.csv")))
tot = 0; clean = 0; dirty = 0; none_cells = 0; ctrl_dirty = 0; ctrl_tot = 0
for r in rows:
    q = int(r['q']); n = int(r['n']); k = int(r['k'])
    if q not in (11, 13): continue
    F = GF(q)
    if r['verdict'] == 'FOUND':
        w = json.loads(r['witness'])
        u_at = {p: c for p, c in zip(w['positions'], w['coeffs'])}
        assert len(u_at) == k and all(c != 0 for c in u_at.values())
        tot += 1
        if pair_candidate(u_at, n, F): dirty += 1
        else: clean += 1
    else:
        none_cells += 1
        if k == n:   # control: the only placement is all positions; all-ones must be dirty
            ctrl_tot += 1
            if pair_candidate({p: 1 for p in range(n)}, n, F): ctrl_dirty += 1
print("q in {11,13}: FOUND witnesses checked=%d clean=%d DIRTY=%d | NONE cells=%d | control (k=n all-ones must be dirty): %d/%d dirty"
      % (tot, clean, dirty, none_cells, ctrl_dirty, ctrl_tot))
