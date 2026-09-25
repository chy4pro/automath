#!/usr/bin/env python3
"""owner-w61: independent check of the J-pass findings (defects on the J-text).

D2 (the real one): the sentence trailing the T-b repair --
  "後續 'p <= 2 <= X-2 => Lemma U => m <= X+4 與 m=X+6 矛盾' 原樣有效"
-- is k=1-only.  Under J1's widening to k <= 1 it reads as valid at k=0 too, where
it is FALSE: the k=0 branch's own graph is the document's control instance
[3,3,3,3,3,2,1], on which Lemma U's second hypothesis fails.

D1: my "exactly 10 configurations" is a multiplicity-box artifact; the branch is the
infinite family K_{3,3} + t pendants at one B-vertex.  The judge's closed-form
disposal (all A-vertices share the neighbour x, hence diam <= 3) is checked here.
"""
import sys
from itertools import combinations
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w61_r5_rig import G, residue_seq

print("=== D2: the k=0 branch's unique graph, and Lemma U on it")
# k=0 bullet: A = {u1,u2 universal, w~{y,z}, l~{x}},  B = {x,y,z}, e_B = 0
x, y, z, u1, u2, w, l = 0, 1, 2, 3, 4, 5, 6
E = [(u1, x), (u1, y), (u1, z), (u2, x), (u2, y), (u2, z), (w, y), (w, z), (l, x)]
g = G(7, E)
seq = sorted(g.degseq(), reverse=True)
alpha, _ = g.independent_sets_max()
m = sum(g.degseq()) // 2
X = max(g.deg(b) for b in (x, y, z))
print(f"   deg={seq} n={g.n} m={m} alpha={alpha} tau={g.n-alpha} diam={g.diam()} "
      f"residue={residue_seq(seq)}")
R = sorted([g.deg(v) for v in (u1, u2, w, l)], reverse=True)
Delta = max(g.degseq())
print(f"   X = max deg over B = {X};  R (A-side degrees) = {R};  Delta = {Delta}")
print(f"   Lemma U 2nd hypothesis 'Delta >= #{{3s in R}}': {Delta} >= {R.count(3)} ? "
      f"{'holds' if Delta >= R.count(3) else 'FAILS'}")
print(f"   misapplied Lemma U would give m <= X+4 = {X+4}, but m = {m}  "
      f"=> a FALSE contradiction (slack {m-(X+4)})")
print(f"   the k=0 bullet's own ending instead computes HH directly: "
      f"D=(3,3,2), sum=8=m-1<m => s=4, residue={residue_seq(seq)}=alpha-1  [alpha={alpha}]")

print()
print("=== D1: is the branch k<=1, e_B=0, p=3 really an infinite family?")
print("    family: B={x,y,z} independent, 3 universal A-vertices, t pendants at x")
for t in range(0, 6):
    E2 = [(3 + i, b) for i in range(3) for b in (x, y, z)]
    E2 += [(6 + j, x) for j in range(t)]
    g2 = G(6 + t, E2)
    al2, _ = g2.independent_sets_max()
    k2 = sum(1 for b in (x, y, z) if g2.deg(b) >= 4)
    print(f"    t={t}: n={g2.n} diam={g2.diam()} k={k2} alpha={al2} tau={g2.n-al2} "
          f"{'OK (diam != 4)' if g2.diam() != 4 else 'DIAM 4 -- J1 BREAKS'}")
print("    closed form: every A-vertex is adjacent to x, so any two A-vertices are at")
print("    distance 2 through x, and dist(a,b) <= 3 for b in B; hence diam <= 3 for ALL t.")
print("done")
