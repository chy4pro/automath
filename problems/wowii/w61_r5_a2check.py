#!/usr/bin/env python3
"""owner-w61 round 5 — independent verification of the §7.8 round-A2 judge's findings
(defects D-1, D-2, D-4, D-5 and the F1 wording point).  Own code; the graph/HH
routines are this round's own (`w61_r5_rig.py`), not the judge's and not a helper's.
"""
import sys
from itertools import combinations
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w61_r5_rig import G, residue_seq


def fan_graph(tau, L, dhi, aprime):
    """Fan(tau,L): B = K_tau - uv with u,v in B_hi; B_lo all B-universal with a single
    A-neighbour a0; a0 adjacent to all of B; A' vertices attach inside B_hi only.
    dhi = list of A'-attachment counts per B_hi vertex is NOT used; instead aprime is
    the list of A' degrees, and we attach greedily to B_hi.  Returns (G, A) or None."""
    p = tau - L
    B_hi = list(range(p))                     # 0..p-1 ; u = 0, v = 1
    B_lo = list(range(p, tau))
    a0 = tau
    Ap = list(range(tau + 1, tau + 1 + len(aprime)))
    edges = []
    for x, y in combinations(range(tau), 2):
        if (x, y) == (0, 1):
            continue                          # the single non-edge uv
        edges.append((x, y))
    for b in range(tau):
        edges.append((a0, b))
    for a, d in zip(Ap, aprime):
        if d > p:
            return None
        for w in B_hi[:d]:
            edges.append((a, w))
    g = G(tau + 1 + len(aprime), edges)
    return g, [a0] + Ap


def report(g, A, label):
    alpha, mis = g.independent_sets_max()
    n = g.n
    tau = n - alpha
    seq = sorted(g.degseq(), reverse=True)
    res = residue_seq(seq)
    # number of HH steps
    s = n - res
    print(f"{label}: deg={seq} n={n} alpha={alpha} tau={tau} residue={res} s={s} "
          f"| A is maximum? {'YES' if len(A) == alpha else 'NO (|A|=%d)' % len(A)} "
          f"| residue vs alpha: {'= alpha' if res == alpha else 'alpha-%d' % (alpha - res)}")
    return alpha, tau, res, s


print("=== D-1 / D-2 witness: Fan(4,2), d_u=d_v=2, A' = [2,2]")
g, A = fan_graph(4, 2, None, [2, 2])
report(g, A, "  Fan(4,2)")

print()
print("=== the judge's F1 witness from the brief, for comparison: A' = [2,1,1]")
g2, A2 = fan_graph(4, 2, None, [2, 1, 1])
report(g2, A2, "  Fan(4,2)")

print()
print("=== D-3: is |A'| = 1 possible?  R = sum of A'-attachments >= p+2 forces |A'| >= 2")
print("    (u,v miss the edge uv so each needs >= 2 A'-attachments; the other p-2 need >= 1)")
for tau in range(4, 9):
    for L in range(2, tau - 1):
        p = tau - L
        Rmin = 2 + 2 + max(0, p - 2)
        print(f"    tau={tau} L={L} p={p}: R >= {Rmin}, max A' degree <= p = {p} "
              f"=> |A'| >= {'2 (single A-vertex impossible)' if Rmin > p else 'NOT FORCED'}")

print()
print("=== D-4: at step j = L+1 the C-value equals p; how many A' entries TIE with it?")
print("    (the judge measured q = 0 always; q >= 2 would break Lemma FAN-2's proof)")


def high_phase(tau, L, aprime, tiebreak='C-last'):
    """run the labelled HH high phase on a Fan(tau,L) instance and report, at step
    j = L+1, the C-value and the number of A' entries at or above it."""
    p = tau - L
    gA = fan_graph(tau, L, None, aprime)
    if gA is None:
        return None
    g, A = gA
    n = g.n
    lab = [(g.deg(v), v) for v in range(n)]
    kind = {}
    for v in range(n):
        if v < p:
            kind[v] = 'hi'
        elif v < tau or v == tau:
            kind[v] = 'C'
        else:
            kind[v] = 'A'
    vals = {v: g.deg(v) for v in range(n)}
    alive = set(range(n))
    out = None
    for j in range(1, p + 1):
        order = sorted(alive, key=lambda v: (-vals[v], 0 if kind[v] == 'A' else 1))
        head = order[0]
        d = vals[head]
        blk = order[1:1 + d]
        if j == L + 1:
            cval = min(vals[v] for v in alive if kind[v] == 'C')
            q = sum(1 for v in alive if kind[v] == 'A' and vals[v] >= cval)
            out = (cval, q)
        alive.discard(head)
        for v in blk:
            if v in alive:
                vals[v] -= 1
    return out


tot = qmax = 0
rows = []
for tau in range(4, 11):
    for L in range(2, tau - 1):
        p = tau - L
        if L + 1 > p:
            continue
        for a1 in range(1, p + 1):
            for a2 in range(1, a1 + 1):
                for a3 in range(0, a2 + 1):
                    ap = [a1, a2] + ([a3] if a3 else [])
                    r = high_phase(tau, L, ap)
                    if r is None:
                        continue
                    tot += 1
                    qmax = max(qmax, r[1])
                    if r[1] >= 2:
                        rows.append((tau, L, ap, r))
print(f"    instances with a step j = L+1 in the high phase: {tot}; "
      f"max #A' entries at-or-above the C-value = {qmax}")
print(f"    instances with q >= 2 (which would break FAN-2's argument): {len(rows)}")
for r in rows[:5]:
    print("      ", r)
print()
print("done")
