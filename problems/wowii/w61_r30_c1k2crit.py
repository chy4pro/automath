#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r30 -- the k=2 criterion that generalises Observation C1-E.

C1-E excluded lambda=(w,1), w odd >= 3.  The complement reformulation makes the
argument uniform and gives a criterion for EVERY two-part lambda:

  k=2, lambda=(w,c), N=w+3.  Complement degrees D = [2]^{w+2} u [w+2-c].
  alpha(G) <= 2  <=>  Gbar triangle-free.  Let u be the vertex of degree
  D0 := w+2-c.  Triangle-free => N(u) is independent; every vertex of N(u) has
  degree 2, so it spends exactly one edge OUTSIDE {u} u N(u); that set has
  N-1-D0 = c vertices, each of degree 2, so it absorbs at most 2c edge-ends.
  Hence  D0 <= 2c, i.e.  w + 2 <= 3c.                                     (NEC)

This script tests (NEC) as a NECESSARY-AND-SUFFICIENT criterion by brute
realizer search over every two-part lambda with N = w+3 <= 12.
"""
import sys
sys.setrecursionlimit(10000)
from importlib.machinery import SourceFileLoader
m = SourceFileLoader('c1k3', 'problems/wowii/w61_r30_c1k3.py').load_module()

print('lambda        N   w+2<=3c   alpha<=2 available   agree')
bad = 0; rows = 0
for w in range(1, 10):
    for c in range(1, w + 1):
        lam = (w, c)
        if (w + c) % 2: continue                 # Lemma C1-F: step sequence iff sum even
        M = m.M_of(lam)
        if m.steps_residue(M) is None: continue
        N = len(M); D = [N - 1 - d for d in M]
        if min(D) < 0: continue
        pred = (w + 2 <= 3 * c)
        got = m.implB(D, 2, m.clique_number)
        rows += 1
        ok = (pred == got)
        bad += (not ok)
        print(f'{str(lam):<12}{N:>3}   {str(pred):>7}   {str(got):>18}   {"OK" if ok else "*** MISS"}')
print()
print(f'rows: {rows}   misses: {bad}')
print('NECESSITY is hand-proved above.  SUFFICIENCY is a MEASUREMENT over N <= 12 --')
print('more cases is not a proof and is not offered as one.')
