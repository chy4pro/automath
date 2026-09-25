#!/usr/bin/env python3
"""owner-w61 round 5, post-T3B: independent verification of the T3 round-B findings.

tau = 3 family.  B = {x,y,z}; every A-vertex is determined by its type T (a non-empty
subset of B) and the graph by (e_B, multiplicities m_T).  k := #{b in B : deg(b) >= 4};
p := m_{xyz} (the number of B-universal A-vertices).

Check 1 (defect D1): in the branch k <= 1, e_B = 0, p = 3 — the branch the k=0 bullet
reaches via "同上" and which the T-b repair only wrote out for k = 1 — is diam = 4
really impossible, i.e. does the widened repair ("k <= 1") actually cover k = 0?
Check 2: no hard-core instance anywhere in a bounded box (Theorem T3 sanity).
"""
import sys
from itertools import combinations, product
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w61_r5_rig import G, residue_seq

Bv = [0, 1, 2]
TYPES = [t for r in (1, 2, 3) for t in combinations(Bv, r)]      # 7 non-empty types
PAIRS = list(combinations(Bv, 2))


def build(eB_mask, mult):
    edges = [PAIRS[i] for i in range(3) if eB_mask >> i & 1]
    nxt = 3
    for t, mt in zip(TYPES, mult):
        for _ in range(mt):
            for b in t:
                edges.append((b, nxt))
            nxt += 1
    return G(nxt, edges)


def analyse(eB_mask, mult, want_f=False):
    g = build(eB_mask, mult)
    if g.n < 4 or not g.connected():
        return None
    A = list(range(3, g.n))
    if not A:
        return None
    alpha, _ = g.independent_sets_max()
    if alpha != len(A):
        return None                      # A must be A MAXIMUM independent set
    tau = g.n - alpha
    if tau != 3:
        return None
    d = g.diam()
    k = sum(1 for b in Bv if g.deg(b) >= 4)
    p = mult[TYPES.index((0, 1, 2))]
    res = residue_seq(g.degseq())
    fv = g.f() if want_f else None
    return dict(g=g, n=g.n, alpha=alpha, tau=tau, diam=d, k=k, p=p,
                eB=bin(eB_mask).count('1'), residue=res, f=fv)


print("=== Check 1: branch k <= 1, e_B = 0, p = 3 — is diam = 4 impossible?")
tot = d4 = 0
by_k = {}
for mult in product(range(4), repeat=6):
    full = list(mult[:TYPES.index((0, 1, 2))]) + [3] + list(mult[TYPES.index((0, 1, 2)):])
    r = analyse(0, full)
    if r is None or r['k'] > 1 or r['p'] != 3:
        continue
    tot += 1
    by_k[r['k']] = by_k.get(r['k'], 0) + 1
    if r['diam'] == 4:
        d4 += 1
        if d4 <= 3:
            print("   diam=4 FOUND:", full, r['n'], r['diam'])
print(f"   configurations enumerated: {tot} (by k: {by_k}); with diam = 4: {d4}")
print("   => the repair's conclusion holds for k = 0 exactly as for k = 1"
      if d4 == 0 else "   => REPAIR FAILS AT k = 0")

print()
print("=== Check 2: any hard-core instance in the tau=3 box? (Theorem T3 says none)")
hc = 0
tested = 0
for eB in range(8):
    for mult in product(range(3), repeat=7):
        if sum(mult) == 0 or sum(mult) > 8:
            continue
        r = analyse(eB, list(mult), want_f=True)
        if r is None:
            continue
        tested += 1
        if (r['diam'] == 4 and r['f'] == r['alpha'] + 1 and r['residue'] == r['alpha']
                and not r['g'].is_acyclic(range(r['g'].n))):
            hc += 1
            print("   HARD CORE FOUND:", eB, mult, r)
print(f"   tau=3 graphs tested: {tested}; hard-core instances: {hc}")
print("done")
