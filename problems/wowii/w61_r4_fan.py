#!/usr/bin/env python3
"""
w61 round 4 (rebuild): decide the Fan(tau,2) residual of draft Prop L2.

Proposition L2 pins every hard-core instance with L = 2 to ONE rigid shape:

  B = {b1,b2,u,v} u W,  |W| = tau-4,  G[B] = K_tau - uv,  u,v in B_hi
  b1,b2 B-universal, deg_A(b1)=deg_A(b2)=1 with the SAME A-neighbour a0,
  a0 adjacent to ALL of B, T1={u}, T2={v}, deg_A(u),deg_A(v) >= 3,
  every other A-vertex attaches only inside B_hi = {u,v} u W.

So the degree sequence is determined by
  tau ; r_x := #(A'-neighbours of x) for x in B_hi ; the A'-degree multiset,
where A' = A \ {a0} and
  deg(b1)=deg(b2)=deg(a0)=tau,  deg(u)=tau-1+r_u,  deg(v)=tau-1+r_v,
  deg(w)=tau+r_w (w in W),      deg(a)=|N(a)| in [1,tau-2] for a in A'.
Constraints: r_u,r_v >= 2 (Lemma C*: deg_A >= 3, a0 contributes 1);
r_w >= 1 (w in B_hi needs deg >= tau+1); at least two A'-vertices of degree 1
(the occurring types T1={u}, T2={v}); sum(A'-degrees) = sum(r_x).

residue() is a function of the degree sequence alone, and alpha = 1 + |A'|
EXACTLY (A is maximum by the hypothesis of Prop L2).  So an instance survives
only if residue(degseq) == 1 + |A'|.  This script enumerates the whole parameter
space in a bounded box and reports every survivor.

No SAT, no large exhaustive graph search: pure parameter scan + Gale-Ryser.
"""
import itertools, sys
from functools import lru_cache


# ---------- Havel-Hakimi residue (degree-sequence function) ----------
def residue(seq):
    """Number of zeros left by iterated Havel-Hakimi. None if not graphical."""
    s = sorted(seq, reverse=True)
    while s and s[0] > 0:
        d = s[0]
        s = s[1:]
        if d > len(s):
            return None
        for i in range(d):
            s[i] -= 1
            if s[i] < 0:
                return None
        s.sort(reverse=True)
    return len(s)


def hh_heads(seq):
    """The head values D_1..D_s of the HH process (canonical sort)."""
    s = sorted(seq, reverse=True)
    out = []
    while s and s[0] > 0:
        d = s[0]
        out.append(d)
        s = s[1:]
        for i in range(d):
            s[i] -= 1
        s.sort(reverse=True)
    return out


# ---------- Gale-Ryser: is the bipartite degree pair realizable? ----------
def gale_ryser(a, b):
    """a,b: degree lists of the two sides of a bipartite graph."""
    if sum(a) != sum(b):
        return False
    if any(x < 0 for x in a + b):
        return False
    a = sorted(a, reverse=True)
    nb = len(b)
    if any(x > nb for x in a):
        return False
    if any(x > len(a) for x in b):
        return False
    for k in range(1, len(a) + 1):
        lhs = sum(a[:k])
        rhs = sum(min(x, k) for x in b)
        if lhs > rhs:
            return False
    return True


# ---------- partitions of R into k parts, each in [lo,hi] ----------
def parts(R, k, lo, hi, cur=None, start=None):
    """non-increasing lists of length k, entries in [lo,hi], summing to R"""
    if cur is None:
        cur, start = [], hi
    if k == 0:
        if R == 0:
            yield list(cur)
        return
    if R < lo * k or R > hi * k:
        return
    top = min(start, R - lo * (k - 1))
    for v in range(top, lo - 1, -1):
        cur.append(v)
        yield from parts(R - v, k - 1, lo, hi, cur, v)
        cur.pop()


def scan(TAU_MAX=8, R_MAX=24, K_MAX=18, verbose=False):
    survivors = []
    stats = {"instances": 0, "realizable": 0, "res_lt": 0, "res_eq": 0, "res_gt": 0}
    per_tau_gap = {}
    for tau in range(4, TAU_MAX + 1):
        nW = tau - 4
        rmax = min(K_MAX, R_MAX)
        for r_u in range(2, rmax + 1):
            for r_v in range(2, rmax + 1):
                if r_v > r_u:          # symmetry u <-> v
                    continue
                for rw in (parts(s, nW, 1, rmax) if nW else [[]] ) if False else [None]:
                    pass
                # enumerate the W-vector as a non-increasing tuple
                wvecs = [()] if nW == 0 else None
                if nW:
                    wvecs = []
                    for total in range(nW, R_MAX + 1):
                        for p in parts(total, nW, 1, rmax):
                            wvecs.append(tuple(p))
                for wv in wvecs:
                    R = r_u + r_v + sum(wv)
                    if R > R_MAX:
                        continue
                    bside = [r_u, r_v] + list(wv)
                    # |A'| = k, degrees in [1, tau-2], >= two 1's, sum = R
                    for k in range(2, K_MAX + 1):
                        if k > R:
                            continue
                        for ad in parts(R - 2, k - 2, 1, tau - 2):
                            adeg = list(ad) + [1, 1]
                            stats["instances"] += 1
                            # forced: one deg-1 vertex -> u, another -> v
                            rest_b = [r_u - 1, r_v - 1] + list(wv)
                            rest_a = list(ad)
                            if min(rest_b) < 0:
                                continue
                            if not gale_ryser(rest_a, rest_b):
                                continue
                            stats["realizable"] += 1
                            alpha = 1 + k
                            deg = ([tau, tau, tau]
                                   + [tau - 1 + r_u, tau - 1 + r_v]
                                   + [tau + x for x in wv]
                                   + adeg)
                            res = residue(deg)
                            if res is None:
                                continue
                            gap = alpha - res
                            per_tau_gap.setdefault(tau, {})
                            per_tau_gap[tau][gap] = per_tau_gap[tau].get(gap, 0) + 1
                            if res < alpha:
                                stats["res_lt"] += 1
                            elif res == alpha:
                                stats["res_eq"] += 1
                                survivors.append((tau, r_u, r_v, wv, tuple(adeg), res, alpha))
                            else:
                                stats["res_gt"] += 1
    return survivors, stats, per_tau_gap


if __name__ == "__main__":
    TAU_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    R_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    K_MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    surv, stats, ptg = scan(TAU_MAX, R_MAX, K_MAX)
    print(f"[Fan(tau,2) scan] tau<={TAU_MAX} R<={R_MAX} k<={K_MAX}")
    print(f"  parameter tuples          = {stats['instances']}")
    print(f"  bipartite-realizable      = {stats['realizable']}")
    print(f"  residue <  alpha (killed) = {stats['res_lt']}")
    print(f"  residue == alpha (SURVIVOR, would be a hard-core L=2 instance) = {stats['res_eq']}")
    print(f"  residue >  alpha (impossible, would contradict Favaron)        = {stats['res_gt']}")
    print(f"  alpha - residue histogram per tau: ")
    for t in sorted(ptg):
        print(f"    tau={t}: {dict(sorted(ptg[t].items()))}")
    if surv:
        print("  SURVIVORS (first 20):")
        for s in surv[:20]:
            print("   ", s)
    else:
        print("  NO SURVIVOR: every Fan(tau,2) degree sequence in the box has residue <= alpha-1.")

    # --- control: the same scan with the Prop-L2 constraints RELAXED one at a
    # --- time, to confirm the scan is not vacuous / not accidentally empty.
    print()
    print("[control] same box, but WITHOUT the 'two A'-vertices of degree 1' type "
          "requirement and WITHOUT r_u,r_v >= 2 (i.e. shapes Prop L2 forbids):")
    got = 0
    tested = 0
    for tau in range(4, TAU_MAX + 1):
        nW = tau - 4
        for r_u in range(1, 8):
            for r_v in range(1, r_u + 1):
                wvs = [()] if nW == 0 else [tuple(p) for tot in range(nW, 12)
                                            for p in parts(tot, nW, 1, 8)]
                for wv in wvs:
                    R = r_u + r_v + sum(wv)
                    if R > R_MAX:
                        continue
                    for k in range(1, K_MAX + 1):
                        for ad in parts(R, k, 1, max(1, tau - 2)):
                            tested += 1
                            deg = ([tau, tau, tau]
                                   + [tau - 1 + r_u, tau - 1 + r_v]
                                   + [tau + x for x in wv] + list(ad))
                            res = residue(deg)
                            if res is not None and res == 1 + k:
                                got += 1
    print(f"  tested={tested}  residue==alpha count={got}"
          f"   (a nonzero count shows the residue test is not trivially always strict)")
