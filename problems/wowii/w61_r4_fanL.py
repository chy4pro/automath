#!/usr/bin/env python3
"""
w61 round 4 (owner-w61, seventh start): ADJUDICATION of Qwen tab B's claim
  "no graph of the form Fan(tau,L) with L >= 2 can satisfy the standing
   hypotheses (residue = alpha)".

Fan(tau,L) (draft Sec 7.6 G, closing note; L=2 case = Proposition L2):

  B = B_lo u B_hi,  |B| = tau,  B_lo = {b_1..b_L},  B_hi = {u,v} u W,
  p := |B_hi| = tau - L,  |W| = p - 2 = tau - L - 2   (so L <= tau-2),
  G[B] = K_tau - uv,
  every b_i is B-universal with deg_A(b_i) = 1, all sharing ONE A-neighbour a0,
  a0 adjacent to ALL of B, T1 = {u}, T2 = {v}, deg_A(u), deg_A(v) >= 3,
  every A-vertex other than a0 attaches only inside B_hi.

Write A' := A \ {a0}, k := |A'|, alpha = 1 + k, and for x in B_hi let
d_x := #(A'-neighbours of x)  (so deg_A(x) = 1 + d_x).  Degrees:

  deg(b_i) = (tau-1) + 1        = tau                      (L entries)
  deg(a0)  = tau                                           (1 entry)
  deg(u)   = (tau-2) + 1 + d_u  = tau-1+d_u,  d_u >= 2
  deg(v)   = (tau-2) + 1 + d_v  = tau-1+d_v,  d_v >= 2
  deg(w)   = (tau-1) + 1 + d_w  = tau+d_w,    d_w >= 1     (w in W)
  deg(a)   = |N(a)| in [1, p]                              (a in A')

with sum_{x in B_hi} d_x = sum_{a in A'} deg(a) =: R.

residue() is a function of the degree sequence alone and alpha = 1 + k is
EXACT here (A is the maximum independent set by hypothesis).  So a Fan(tau,L)
instance satisfies the reductio iff residue(degseq) == 1 + k.  This scans the
whole parameter box; ANY survivor refutes tab B, zero survivors reproduces it
(over the box).

Two modes:
  STRICT  - imposes the type requirement (>= 2 A'-vertices of degree 1, one
            attached to u and one to v, realising T1={u}, T2={v}) plus
            Gale-Ryser realizability of the A'-B_hi bipartite graph.
  SUPER   - drops the type requirement (a strict SUPERSET of Fan degree
            sequences).  No survivor here is a strictly stronger statement.

Also emits the per-instance HH diagnostics that tab B's Lemma 1 / Lemma 2 talk
about, on the instances that come CLOSEST to the reductio (alpha - residue
minimal), so the mechanism can be inspected, not just the verdict.
No SAT.  Pure parameter scan.
"""
import sys
from collections import Counter


# ---------- Havel-Hakimi ----------
def residue(seq):
    """Zeros left by iterated Havel-Hakimi (canonical: always take the max).
    None if not graphical."""
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


def hh_trace(seq):
    """(head values D_1..D_s, list of sorted remaining lists at each step)."""
    s = sorted(seq, reverse=True)
    heads, snaps = [], []
    while s and s[0] > 0:
        snaps.append(list(s))
        d = s[0]
        heads.append(d)
        s = s[1:]
        if d > len(s):
            return heads, snaps, None
        for i in range(d):
            s[i] -= 1
            if s[i] < 0:
                return heads, snaps, None
        s.sort(reverse=True)
    return heads, snaps, len(s)


def gale_ryser(a, b):
    """bipartite realizability of degree lists a (side 1) and b (side 2)."""
    if sum(a) != sum(b):
        return False
    if any(x < 0 for x in a) or any(x < 0 for x in b):
        return False
    a = sorted(a, reverse=True)
    if any(x > len(b) for x in a):
        return False
    if any(x > len(a) for x in b):
        return False
    for k in range(1, len(a) + 1):
        if sum(a[:k]) > sum(min(x, k) for x in b):
            return False
    return True


def parts(R, k, lo, hi, cur=None, start=None):
    """non-increasing length-k lists, entries in [lo,hi], summing to R."""
    if cur is None:
        cur, start = [], hi
    if k == 0:
        if R == 0:
            yield list(cur)
        return
    if R < lo * k or R > hi * k:
        return
    top = min(start, R - lo * (k - 1))
    for val in range(top, lo - 1, -1):
        cur.append(val)
        yield from parts(R - val, k - 1, lo, hi, cur, val)
        cur.pop()


def scan(TAU_MAX=9, LMIN=2, R_MAX=22, K_MAX=18, strict=True):
    survivors = []
    stats = Counter()
    gaphist = {}
    closest = []      # (gap, tau, L, dvec, adeg)
    for tau in range(4, TAU_MAX + 1):
        for L in range(LMIN, tau - 1):          # L <= tau-2
            p = tau - L
            nW = p - 2
            if nW < 0:
                continue
            for d_u in range(2, R_MAX + 1):
                for d_v in range(2, d_u + 1):   # symmetry u <-> v
                    wvecs = [()] if nW == 0 else [
                        tuple(q) for tot in range(nW, R_MAX + 1)
                        for q in parts(tot, nW, 1, R_MAX)
                    ]
                    for wv in wvecs:
                        R = d_u + d_v + sum(wv)
                        if R > R_MAX:
                            continue
                        bside = [d_u, d_v] + list(wv)
                        for k in range(1, K_MAX + 1):
                            if k > R:
                                continue
                            if strict:
                                if k < 2:
                                    continue
                                # two A'-vertices of degree 1 realise T1={u},T2={v}
                                gen = ([list(q) + [1, 1] for q in
                                        parts(R - 2, k - 2, 1, p)])
                            else:
                                gen = ([list(q) for q in parts(R, k, 1, p)])
                            for adeg in gen:
                                stats["tuples"] += 1
                                if strict:
                                    rest_b = [d_u - 1, d_v - 1] + list(wv)
                                    rest_a = adeg[:-2]
                                    if min(rest_b) < 0:
                                        continue
                                    if not gale_ryser(rest_a, rest_b):
                                        continue
                                else:
                                    if not gale_ryser(adeg, bside):
                                        continue
                                stats["realizable"] += 1
                                deg = ([tau] * (L + 1)
                                       + [tau - 1 + d_u, tau - 1 + d_v]
                                       + [tau + x for x in wv]
                                       + adeg)
                                res = residue(deg)
                                if res is None:
                                    stats["nongraphical"] += 1
                                    continue
                                alpha = 1 + k
                                gap = alpha - res
                                gaphist.setdefault((tau, L), Counter())[gap] += 1
                                if gap == 0:
                                    stats["SURVIVOR"] += 1
                                    survivors.append((tau, L, d_u, d_v, wv,
                                                      tuple(adeg), res, alpha))
                                elif gap > 0:
                                    stats["killed"] += 1
                                else:
                                    stats["res_gt_alpha"] += 1
                                closest.append((gap, tau, L, d_u, d_v, wv,
                                                tuple(adeg), res, alpha))
    closest.sort(key=lambda t: (t[0], t[1], t[2]))
    return survivors, stats, gaphist, closest[:8]


def mechanism_report(tau, L, d_u, d_v, wv, adeg):
    """Print the HH trajectory of one Fan instance and check tab B's Lemma 1/2
    claims (high-phase first, C = B_lo u {a0} never escapes the block)."""
    deg = ([tau] * (L + 1) + [tau - 1 + d_u, tau - 1 + d_v]
           + [tau + x for x in wv] + list(adeg))
    heads, snaps, res = hh_trace(deg)
    print(f"    Fan(tau={tau},L={L}) d_u={d_u} d_v={d_v} W={wv} A'={adeg}")
    print(f"      degseq={sorted(deg, reverse=True)}")
    print(f"      s={len(heads)} (tau={tau})  heads D={heads}  residue={res} "
          f"alpha={1+len(adeg)}")
    p = tau - L
    hi_heads = sum(1 for d in heads[:p] if d >= tau + 1 - 0)
    print(f"      first p={p} head values {heads[:p]}  "
          f"(tab B: these should be the high vertices)")
    if len(heads) > p:
        print(f"      post-high-phase head values {heads[p:]}")
    if len(snaps) > p:
        print(f"      list at start of step p+1: {snaps[p]}")
        print(f"      tab B Lemma 2 predicts [L]*(L+1) + [1,1] = "
              f"{[L]*(L+1) + [1,1]} as the forced bad suffix")


if __name__ == "__main__":
    TAU_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    R_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    K_MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 16

    for label, strict, lmin in (("STRICT L>=2", True, 2),
                                ("SUPERSET L>=2 (no type requirement)", False, 2),
                                ("CONTROL L=1 (draft says already impossible)", True, 1)):
        surv, stats, gh, closest = scan(TAU_MAX, lmin, R_MAX, K_MAX, strict)
        if label.startswith("CONTROL"):
            # restrict the L=1 control to L=1 only
            surv = [s for s in surv if s[1] == 1]
        print(f"[{label}] tau<={TAU_MAX} R<={R_MAX} k<={K_MAX}")
        print(f"  parameter tuples={stats['tuples']}  realizable={stats['realizable']}"
              f"  graphical-killed={stats['killed']}  SURVIVORS={stats['SURVIVOR']}"
              f"  res>alpha(impossible)={stats['res_gt_alpha']}")
        agg = Counter()
        for key, c in gh.items():
            for g, n in c.items():
                agg[g] += n
        print(f"  (alpha - residue) histogram, aggregated: {dict(sorted(agg.items()))}")
        per_L = {}
        for (t, L), c in gh.items():
            per_L.setdefault(L, Counter()).update({min(c.keys()): 0})
            per_L[L][min(c.keys())] += 1
        mins = {L: min(c.keys()) for L, c in
                {L: Counter({min(cc.keys()): 1 for (t, LL), cc in gh.items() if LL == L})
                 for L in sorted({LL for (t, LL) in gh})}.items()}
        print(f"  minimum (alpha - residue) per L: {mins}")
        if surv:
            print(f"  *** {len(surv)} SURVIVOR(S) — tab B REFUTED. First 10:")
            for s in surv[:10]:
                print("     ", s)
        else:
            print("  NO SURVIVOR in the box: every Fan degree sequence has "
                  "residue <= alpha-1, i.e. the reductio fails.")
        if closest:
            print("  closest-to-survival instances (gap, tau, L, d_u, d_v, W, A', res, alpha):")
            for c in closest[:4]:
                print("     ", c)
        print()

    print("[MECHANISM] HH trajectories of minimal Fan(tau,L) instances "
          "(tab B Lemma 1/2 inspection):")
    for (tau, L, d_u, d_v, wv, adeg) in [
        (4, 2, 2, 2, (), [1, 1, 1, 1]),
        (5, 2, 2, 2, (1,), [1, 1, 1, 1, 1]),
        (5, 3, 2, 2, (), [1, 1, 1, 1]),
        (6, 2, 2, 2, (1, 1), [1, 1, 1, 1, 1, 1]),
        (6, 4, 2, 2, (), [1, 1, 1, 1]),
        (7, 5, 2, 2, (), [1, 1, 1, 1]),
    ]:
        mechanism_report(tau, L, d_u, d_v, wv, adeg)
