#!/usr/bin/env python3
"""
w61 round 4: numerical backing for owner-w61's Lemma FAN-6 (draft Sec 7.8 E),
which PROVES that the A'-residual partition after the Fan high phase is 1+1 and
never a single 2.

The proof uses exactly four structural facts about the high phase; this script
checks all four on every Fan(tau,L>=2) degree sequence in the superset box
(no occurring-type requirement), with adversarial tie-breaks:

  H1  every remaining B_hi vertex lies in block_j            (DICH(b))
  H2  every C vertex lies in block_j                         (Problem D)
  H3  a_j := |block_j & A'| = D_j - (p-j) - (L+1) >= 1
  H4  block_j & A' is exactly the top a_j A'-entries, and in particular the
      MAXIMUM A'-entry is always decremented  (the prefix property, which is
      what drives the backward induction)
  H5  the A'-total is >= 2 at every step of the high phase (it lands on 2)

and reports the realized (max, second-max) of the A'-multiset at each step, to
exhibit the "v-1 is absent" pattern the induction turns on.
"""
import random
import sys
from collections import Counter


def parts(R, k, lo, hi, cur=None, start=None):
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


def gale_ryser(a, b):
    if sum(a) != sum(b):
        return False
    if any(x < 0 for x in a) or any(x < 0 for x in b):
        return False
    a = sorted(a, reverse=True)
    if any(x > len(b) for x in a) or any(x > len(a) for x in b):
        return False
    for k in range(1, len(a) + 1):
        if sum(a[:k]) > sum(min(x, k) for x in b):
            return False
    return True


def run_fan(tau, L, d_u, d_v, wv, adeg, rng=None):
    p = tau - L
    labels, deg = [], []
    for i in range(L):
        labels.append(("C", i)); deg.append(tau)
    labels.append(("C", L)); deg.append(tau)              # a0
    labels.append(("H", 0)); deg.append(tau - 1 + d_u)
    labels.append(("H", 1)); deg.append(tau - 1 + d_v)
    for i, x in enumerate(wv):
        labels.append(("H", 2 + i)); deg.append(tau + x)
    for i, x in enumerate(adeg):
        labels.append(("P", i)); deg.append(x)
    cur = dict(zip(labels, deg))
    alive = list(labels)
    f = Counter()
    for j in range(1, p + 1):
        if rng is None:
            alive.sort(key=lambda x: (-cur[x], str(x)))
        else:
            rng.shuffle(alive); alive.sort(key=lambda x: -cur[x])
        if not alive or cur[alive[0]] == 0:
            f["ran_out"] += 1
            return f, None
        h = alive[0]; D = cur[h]
        if h[0] != "H":
            f["H0_head_not_high"] += 1
        rest = alive[1:]
        if D > len(rest):
            return f, None
        blk = set(rest[:D])
        Ap = [x for x in rest if x[0] == "P" and cur[x] > 0]
        # H1 / H2
        for x in rest:
            if x[0] == "H" and x not in blk:
                f["H1"] += 1
            if x[0] == "C" and x not in blk:
                f["H2"] += 1
        # H3
        aj = len([x for x in blk if x[0] == "P"])
        if aj != D - (p - j) - (L + 1):
            f["H3_count"] += 1
        if aj < 1:
            f["H3_pos"] += 1
        # H4: block's A'-part is a top-a_j set, and the max A'-entry is in it
        if Ap:
            mx = max(cur[x] for x in Ap)
            if not any(x in blk for x in Ap if cur[x] == mx):
                f["H4_max_escapes"] += 1
            inb = sorted((cur[x] for x in Ap if x in blk), reverse=True)
            outb = sorted((cur[x] for x in Ap if x not in blk), reverse=True)
            if inb and outb and min(inb) < max(outb):
                f["H4_not_prefix"] += 1
        # H5
        if sum(cur[x] for x in rest if x[0] == "P") < 2:
            f["H5"] += 1
        for x in rest[:D]:
            cur[x] -= 1
            if cur[x] < 0:
                return f, None
        alive = rest
    resid = sorted((cur[x] for x in alive if x[0] == "P" and cur[x] > 0),
                   reverse=True)
    cpart = sorted((cur[x] for x in alive if x[0] == "C"), reverse=True)
    return f, (tuple(cpart), tuple(resid))


if __name__ == "__main__":
    TAU_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    R_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    K_MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    rng = random.Random(20260818)
    fails = Counter(); res = Counter(); runs = 0
    for tau in range(4, TAU_MAX + 1):
        for L in range(2, tau - 1):
            p = tau - L; nW = p - 2
            if nW < 0:
                continue
            wvecs = [()] if nW == 0 else [tuple(q) for t in range(nW, R_MAX + 1)
                                          for q in parts(t, nW, 1, R_MAX)]
            for d_u in range(2, R_MAX + 1):
                for d_v in range(2, d_u + 1):
                    for wv in wvecs:
                        R = d_u + d_v + sum(wv)
                        if R > R_MAX:
                            continue
                        bside = [d_u, d_v] + list(wv)
                        for k in range(1, K_MAX + 1):
                            if k > R:
                                continue
                            for adeg in parts(R, k, 1, p):
                                if not gale_ryser(adeg, bside):
                                    continue
                                for t in range(3):
                                    f, out = run_fan(tau, L, d_u, d_v, wv,
                                                     adeg,
                                                     None if t == 0 else rng)
                                    fails.update(f); runs += 1
                                    if out is not None:
                                        cp, rp = out
                                        res[(len(set(cp)) == 1
                                             and len(cp) == L + 1
                                             and cp[0] == L, rp)] += 1
    print(f"[Lemma FAN-6 structural hypotheses] Fan(tau,L>=2) superset box "
          f"tau<={TAU_MAX} R<={R_MAX} k<={K_MAX}, 3 tie-breaks each")
    print(f"  high-phase runs = {runs}")
    for key in ("H0_head_not_high", "H1", "H2", "H3_count", "H3_pos",
                "H4_max_escapes", "H4_not_prefix", "H5", "ran_out"):
        print(f"  {key:18s} failures = {fails[key]}")
    print(f"  (C-part == [L]^(L+1) ?, A'-residual partition) histogram:")
    for kk, vv in sorted(res.items(), key=lambda x: -x[1])[:8]:
        print(f"     {kk} : {vv}")
