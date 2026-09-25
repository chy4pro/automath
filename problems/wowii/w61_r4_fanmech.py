#!/usr/bin/env python3
"""
w61 round 4: MECHANISM adjudication of Qwen tab B's Lemma 1 (no escape) and
Lemma 2 (forced residual partition 1+1) for Fan(tau,L), L >= 2.

Companion to w61_r4_fanL.py (which decided the verdict: no Fan(tau,L>=2)
degree sequence has residue = alpha).  Here we check WHY, i.e. whether tab B's
two structural lemmas are the true mechanism, by running the actual (labelled)
Havel-Hakimi process on every Fan degree sequence in the box and testing:

  M1  the first p = tau - L heads are exactly the p high vertices B_hi
      (equivalently: no low vertex is a head before every high vertex is gone)
  M2  every vertex of C := B_lo u {a0} (the L+1 vertices of degree exactly tau)
      lies in block_j for every j <= p  ("no escape" during the high phase)
  M3  at the start of step p+1 the remaining multiset is exactly
      [L]*(L+1) + [1,1] (+ zeros)                       (tab B's Lemma 2)
  M4  the whole run takes exactly s = tau + 1 steps (overrun by EXACTLY one)

M1/M2 are what tab B derives from the inequality r + 2L <= 2; M3 is its
Lemma 2.  Note tab B proves them under the reductio (which is false here), so
these tests check the STRONGER unconditional versions -- if they hold in the
box, tab B's conditional versions certainly do.

ADVERSARIAL TIE-BREAKS: the canonical sort is not the only legal HH run.
Every instance is also run under randomised tie-breaks among equal values, so
that a tie-break-dependent mechanism cannot hide.
"""
import random
import sys
from collections import Counter

sys.setrecursionlimit(10000)


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
    if any(x > len(b) for x in a):
        return False
    if any(x > len(a) for x in b):
        return False
    for k in range(1, len(a) + 1):
        if sum(a[:k]) > sum(min(x, k) for x in b):
            return False
    return True


def labelled_hh(deg, labels, rng=None):
    """Labelled Havel-Hakimi.  Returns (heads, blocks, steps, snapshots).
    heads[i]  = (label, value) of the step-i head
    blocks[i] = set of labels decremented at step i
    snapshots[i] = sorted value multiset at the START of step i
    rng!=None -> randomised tie-break among equal current values."""
    cur = {lb: d for lb, d in zip(labels, deg)}
    alive = list(labels)
    heads, blocks, snaps = [], [], []
    while True:
        vals = sorted((cur[x] for x in alive), reverse=True)
        if not vals or vals[0] == 0:
            break
        snaps.append(vals)
        if rng is None:
            alive.sort(key=lambda x: (-cur[x], str(x)))
        else:
            rng.shuffle(alive)
            alive.sort(key=lambda x: -cur[x])
        h = alive[0]
        d = cur[h]
        heads.append((h, d))
        alive = alive[1:]
        if d > len(alive):
            return heads, blocks, None, snaps      # non-graphical
        blk = alive[:d]
        for x in blk:
            cur[x] -= 1
            if cur[x] < 0:
                return heads, blocks, None, snaps
        blocks.append(set(blk))
    return heads, blocks, len(heads), snaps


def fan_instance(tau, L, d_u, d_v, wv, adeg):
    """labels + degrees for Fan(tau,L)."""
    labels, deg = [], []
    for i in range(L):
        labels.append(("blo", i)); deg.append(tau)
    labels.append(("a0", 0)); deg.append(tau)
    labels.append(("u", 0)); deg.append(tau - 1 + d_u)
    labels.append(("v", 0)); deg.append(tau - 1 + d_v)
    for i, x in enumerate(wv):
        labels.append(("w", i)); deg.append(tau + x)
    for i, x in enumerate(adeg):
        labels.append(("ap", i)); deg.append(x)
    return labels, deg


def run(TAU_MAX=8, R_MAX=16, K_MAX=12, TRIALS=3, seed=20260818):
    rng = random.Random(seed)
    fails = Counter()
    stats = Counter()
    suffix_hist = Counter()
    sminustau = Counter()
    examples = {}
    for tau in range(4, TAU_MAX + 1):
        for L in range(2, tau - 1):
            p = tau - L
            nW = p - 2
            if nW < 0:
                continue
            wvecs = [()] if nW == 0 else [
                tuple(q) for tot in range(nW, R_MAX + 1)
                for q in parts(tot, nW, 1, R_MAX)]
            for d_u in range(2, R_MAX + 1):
                for d_v in range(2, d_u + 1):
                    for wv in wvecs:
                        R = d_u + d_v + sum(wv)
                        if R > R_MAX:
                            continue
                        for k in range(2, K_MAX + 1):
                            if k > R:
                                continue
                            for tail in parts(R - 2, k - 2, 1, p):
                                adeg = list(tail) + [1, 1]
                                rest_b = [d_u - 1, d_v - 1] + list(wv)
                                if min(rest_b) < 0:
                                    continue
                                if not gale_ryser(list(tail), rest_b):
                                    continue
                                labels, deg = fan_instance(tau, L, d_u, d_v,
                                                           wv, adeg)
                                for t in range(TRIALS):
                                    r = None if t == 0 else rng
                                    heads, blocks, s, snaps = labelled_hh(
                                        deg, labels, r)
                                    if s is None:
                                        stats["nongraphical"] += 1
                                        break
                                    stats["runs"] += 1
                                    sminustau[s - tau] += 1
                                    if s != tau + 1:
                                        fails["M4"] += 1
                                        examples.setdefault(
                                            "M4", (tau, L, d_u, d_v, wv,
                                                   tuple(adeg), s))
                                    # M1: first p heads are the high vertices
                                    hi = {("u", 0), ("v", 0)} | {
                                        ("w", i) for i in range(len(wv))}
                                    if set(h[0] for h in heads[:p]) != hi:
                                        fails["M1"] += 1
                                        examples.setdefault(
                                            "M1", (tau, L, d_u, d_v, wv,
                                                   tuple(adeg),
                                                   [h[0] for h in heads[:p]]))
                                    # M2: C never escapes a high-phase block
                                    C = {("blo", i) for i in range(L)} | {("a0", 0)}
                                    esc = False
                                    for j in range(min(p, len(blocks))):
                                        headlab = heads[j][0]
                                        for c in C:
                                            if c == headlab:
                                                continue
                                            if c not in blocks[j]:
                                                esc = True
                                    if esc:
                                        fails["M2"] += 1
                                        examples.setdefault(
                                            "M2", (tau, L, d_u, d_v, wv,
                                                   tuple(adeg)))
                                    # M3: suffix at start of step p+1
                                    if len(snaps) > p:
                                        suf = tuple(x for x in snaps[p] if x > 0)
                                        want = tuple([L] * (L + 1) + [1, 1])
                                        suffix_hist[
                                            "EXACT" if suf == want else "OTHER"] += 1
                                        if suf != want:
                                            fails["M3"] += 1
                                            examples.setdefault(
                                                "M3", (tau, L, d_u, d_v, wv,
                                                       tuple(adeg), suf, want))
                                    else:
                                        fails["M3_short"] += 1
    return fails, stats, suffix_hist, sminustau, examples


def control():
    """Counterfactual-availability control: the same residue test on shapes
    that BREAK one Fan hypothesis at a time must sometimes give residue=alpha,
    otherwise the whole scan is trivially always-negative and proves nothing."""
    from itertools import product

    def residue(seq):
        s = sorted(seq, reverse=True)
        while s and s[0] > 0:
            d = s[0]; s = s[1:]
            if d > len(s):
                return None
            for i in range(d):
                s[i] -= 1
                if s[i] < 0:
                    return None
            s.sort(reverse=True)
        return len(s)

    hits = Counter(); tried = Counter()
    # (i) drop 'a0 universal': only L entries of value tau, not L+1
    for tau in range(4, 9):
        for L in range(2, tau - 1):
            for d_u in range(2, 8):
                for d_v in range(2, d_u + 1):
                    nW = tau - L - 2
                    for wv in ([()] if nW == 0 else
                               [tuple(q) for tot in range(nW, 13)
                                for q in parts(tot, nW, 1, 8)]):
                        R = d_u + d_v + sum(wv)
                        if R > 14:
                            continue
                        for k in range(1, 12):
                            for ad in parts(R, k, 1, max(1, tau - L)):
                                for tag, deg in (
                                    ("noA0", [tau] * L
                                     + [tau - 1 + d_u, tau - 1 + d_v]
                                     + [tau + x for x in wv] + list(ad)),
                                    ("Bclique", [tau] * (L + 1)
                                     + [tau + d_u, tau + d_v]
                                     + [tau + x for x in wv] + list(ad)),
                                    ("lowdegA2", [tau + 1] * (L + 1)
                                     + [tau - 1 + d_u, tau - 1 + d_v]
                                     + [tau + x for x in wv] + list(ad)),
                                ):
                                    tried[tag] += 1
                                    res = residue(deg)
                                    if res is not None and res == 1 + k:
                                        hits[tag] += 1
    return tried, hits


if __name__ == "__main__":
    TAU_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    R_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 14
    K_MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    fails, stats, sufh, smt, ex = run(TAU_MAX, R_MAX, K_MAX)
    print(f"[MECHANISM SCAN] Fan(tau,L>=2), tau<={TAU_MAX} R<={R_MAX} k<={K_MAX}, "
          f"3 trajectories each (canonical + 2 randomised tie-breaks)")
    print(f"  labelled HH runs = {stats['runs']}")
    print(f"  s - tau histogram = {dict(sorted(smt.items()))}")
    print(f"  M1 (first p heads = B_hi)          fails = {fails['M1']}")
    print(f"  M2 (C never escapes high-phase blk) fails = {fails['M2']}")
    print(f"  M3 (suffix = [L]*(L+1)+[1,1])       fails = {fails['M3']}"
          f"   (short runs: {fails['M3_short']})")
    print(f"  M4 (s = tau+1 exactly)              fails = {fails['M4']}")
    print(f"  suffix histogram = {dict(sufh)}")
    for key in ("M1", "M2", "M3", "M4"):
        if key in ex:
            print(f"  first {key} counterexample: {ex[key]}")
    print()
    tried, hits = control()
    print("[CONTROL: counterfactual availability] same residue test on shapes "
          "that break ONE Fan hypothesis:")
    for tag in sorted(tried):
        print(f"   {tag:10s} tried={tried[tag]:7d}  residue==alpha hits={hits[tag]}")
    print("   (nonzero hits => the test discriminates; it is not vacuously "
          "always-negative)")
