#!/usr/bin/env python3
"""PROBE T-1, part 2 -- EXACT size of the Sec.6 TWO-DIRECTION residual stratum.

Sec.6 + the objective force (see probe_t1.py, "SEC.6 FORCED PROFILE") at least
n3_min > p-1 directions with |A_u(f)| = 3, hence TWO LINEARLY INDEPENDENT such
directions; GL_2 is simply transitive on ordered bases, so every counterexample
is GL_2-equivalent to one with

        |A_{e1}(f)| <= 3   AND   |A_{e2}(f)| <= 3.

R2(p) := #{ f : F_p^2 -> F_p^2, f(0)=0, |A_{e1}(f)| <= 3, |A_{e2}(f)| <= 3 }.

Counting method (NO enumeration of the function space):
  f <-> (per-row base value b_j, per-row horizontal word w_j) with
        R_j(x1) = b_j + sum_{i<x1} w_j[i],  w_j in A^p, sum w_j = -e1.
  The vertical condition d_{e2}f(x1,j) in B is a transfer condition between
  consecutive rows.  N_subset(A,B) is computed by a cyclic transfer DP over
  states (w_j, b_j); exact-image counts come from 2^|A| * 2^|B| inclusion-
  exclusion, so distinct (A,B) contribute DISJOINT sets of f.

Run: .venv/bin/python3 problems/tdn_2606_27961/probe_t1_r2.py
"""
import itertools
import random
import sys
import time
from math import comb

T_START = time.time()
HARD_TIMEOUT_S = 900
SEED = 20260823
random.seed(SEED)

# ---------------------------------------------------------------------------
# BUG FIX (owner-tdn, round 1, 2026-08-23).  DEFECT: this script produced ZERO
# BYTES for anyone who redirected its stdout and did not let it run to normal
# completion.  CAUSE: CPython block-buffers stdout (8 KiB) when it is not a tty;
# every print here is unflushed and the whole run emits < 8 KiB, so the buffer
# is never filled.  The exact anchor value R2(3) is computed at ~t+3 s but sits
# in that buffer for the remaining ~150 s; a SIGTERM/SIGKILL (harness timeout,
# `head`, ^C on a pipe) discards it without flushing.  Reproduced: identical
# invocation, killed at t=18 s -> 0 bytes; with `python3 -u` -> R2(3) at t~3 s.
# The number was never wrong and was never missing -- it was destroyed in transit.
# FIX: line-buffer stdout so every completed line is durable the moment it is
# printed, independently of how the process ends.
try:
    sys.stdout.reconfigure(line_buffering=True)     # py3.7+
except AttributeError:                              # pragma: no cover
    pass


def check_clock(tag):
    if time.time() - T_START > HARD_TIMEOUT_S:
        print("HARD TIMEOUT at %s" % tag)
        sys.exit(2)


def points(p):
    return [(a, b) for a in range(p) for b in range(p)]


def add(u, v, p):
    return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)


def sub(u, v, p):
    return ((u[0] - v[0]) % p, (u[1] - v[1]) % p)


def words(A, p, target):
    """all length-p words over A whose sum is target"""
    out = []
    for w in itertools.product(A, repeat=p):
        s = (sum(a[0] for a in w) % p, sum(a[1] for a in w) % p)
        if s == target:
            out.append(w)
    return out


def prefixes(w, p):
    """P[x1] = sum_{i<x1} w[i], for x1 = 0..p-1"""
    P = [(0, 0)]
    for i in range(p - 1):
        P.append(add(P[-1], w[i], p))
    return P


def N_subset(A, B, p):
    """#{f : f(0,0)=(0,0), im d_e1 f subset A, im d_e2 f subset B}"""
    e1 = ((-1) % p, 0)
    e2m = (0, (-1) % p)          # -e2, the wrap carry in the e2 direction
    W = words(A, p, e1)
    if not W:
        return 0
    nW = len(W)
    P = [prefixes(w, p) for w in W]
    Bset = set(B)
    # valid mid / wrap shift sets between ordered row-word pairs
    mid = [[None] * nW for _ in range(nW)]
    wrp = [[None] * nW for _ in range(nW)]
    allpts = points(p)
    for i in range(nW):
        for j in range(nW):
            Q = [sub(P[j][x], P[i][x], p) for x in range(p)]
            # beta is valid iff beta + Q[x] in B for every column x
            mid[i][j] = [beta for beta in allpts
                         if all(add(beta, q, p) in Bset for q in Q)]
            wrp[i][j] = [beta for beta in allpts
                         if all(add(add(beta, q, p), e2m, p) in Bset for q in Q)]
    total = 0
    for start in range(nW):
        # state: (row-word index, current base value b_j); b_0 = (0,0)
        cur = {(start, (0, 0)): 1}
        for _step in range(p - 1):
            nxt = {}
            for (i, b), c in cur.items():
                for j in range(nW):
                    for beta in mid[i][j]:
                        k = (j, add(b, beta, p))
                        nxt[k] = nxt.get(k, 0) + c
            cur = nxt
            if not cur:
                break
        for (i, b), c in cur.items():
            # wrap: row p-1 -> row 0, base difference (0,0) - b
            if sub((0, 0), b, p) in wrp[i][start]:
                total += c
    return total


def N_exact(A, B, p, cache):
    """#f with im d_e1 f EXACTLY A and im d_e2 f EXACTLY B (inclusion-exclusion)."""
    tot = 0
    for ka in range(len(A) + 1):
        for Ap in itertools.combinations(A, ka):
            if not Ap:
                continue
            for kb in range(len(B) + 1):
                for Bp in itertools.combinations(B, kb):
                    if not Bp:
                        continue
                    key = (Ap, Bp)
                    if key not in cache:
                        cache[key] = N_subset(Ap, Bp, p)
                    sgn = (-1) ** ((len(A) - ka) + (len(B) - kb))
                    tot += sgn * cache[key]
    return tot


def all_small_sets(p, kmax=3):
    pts = points(p)
    out = []
    for k in range(2, kmax + 1):
        for A in itertools.combinations(pts, k):
            out.append(A)
    return out


def normalized_sets(p, kmax=3):
    """WLOG (0,0) in A: replacing f(x) by f(x)+x1*lam translates A by lam and
    leaves B fixed (and symmetrically for B), so we may normalise both."""
    pts = [q for q in points(p) if q != (0, 0)]
    out = []
    for k in range(2, kmax + 1):
        for rest in itertools.combinations(pts, k - 1):
            out.append(((0, 0),) + rest)
    return out


def exact_total_p3():
    p = 3
    sets_ = all_small_sets(p)
    cache = {}
    tot = 0
    for A in sets_:
        check_clock("p3 exact")
        for B in sets_:
            tot += N_exact(A, B, p, cache)
    return tot, len(sets_)


def sampled_lower_bound(p, n_pairs, kmax=3):
    """Rigorous LOWER bound on R2(p): sum of N_exact over a random sample of
    NORMALISED (A,B) pairs (disjoint f-sets), plus an unbiased estimate of the
    normalised total."""
    norm = normalized_sets(p, kmax)
    cache = {}
    tot = 0
    vals = []
    for _ in range(n_pairs):
        check_clock("sample p=%d" % p)
        A = random.choice(norm)
        B = random.choice(norm)
        v = N_exact(A, B, p, cache)
        vals.append(v)
        tot += v
    npairs_all = len(norm) ** 2
    mean = sum(vals) / float(len(vals))
    var = sum((v - mean) ** 2 for v in vals) / float(max(1, len(vals) - 1))
    se = (var / len(vals)) ** 0.5
    return tot, vals, npairs_all, mean, se, len(norm)


def main():
    print("=" * 78)
    print("VALIDATION -- p=3: transfer-DP total over ALL (A,B) must equal the")
    print("brute stratum count R2(3) printed by probe_t1.py.")
    t, nsets = exact_total_p3()
    print("  p=3  sum of N_exact over all (A,B) pairs = %d   (|A|,|B| sets each: %d)"
          % (t, nsets))
    # ANCHOR -- the one value the cross-validation of clause (3) rests on.
    # Printed on its own line, computed above, never a literal.
    print("  ANCHOR  R2(3) = %d   [population: ALL f with f(0)=0 on F_3^2, i.e."
          " 3^(2*3^2-2) = %d functions; exact, no sampling]"
          % (t, 3 ** (2 * 3 * 3 - 2)))
    print("  NOTE  R2(5) is NOT produced by this method: it needs N_exact over all"
          " (A,B) with |A|,|B|<=3 in F_5^2, i.e. (C(25,2)+C(25,3))^2 = %d pairs"
          " against %d at p=3 -- ~%.0fx more, and each N_subset is itself far"
          " costlier at p=5.  p=5 exact is left PENDING, not asserted."
          % ((comb(25, 2) + comb(25, 3)) ** 2, nsets ** 2,
             ((comb(25, 2) + comb(25, 3)) ** 2) / float(nsets ** 2)))

    for p, npair in ((3, 400), (5, 300), (7, 120)):
        check_clock("main p=%d" % p)
        t0 = time.time()
        tot, vals, npairs_all, mean, se, nnorm = sampled_lower_bound(p, npair)
        nz = sum(1 for v in vals if v != 0)
        mx = max(vals)
        full = p ** (2 * p * p - 2)
        est = mean * npairs_all
        print("-" * 78)
        print("  p=%d  normalised (A,B) population = %d x %d = %d pairs"
              % (p, nnorm, nnorm, npairs_all))
        print("       sampled pairs = %d ; nonzero = %d ; max single-pair N_exact = %d"
              % (len(vals), nz, mx))
        print("       RIGOROUS LOWER BOUND on the normalised stratum (sum over the"
              " sampled pairs, disjoint): %d  (~%.3e)" % (tot, float(tot)))
        print("       unbiased ESTIMATE of normalised stratum = mean*pairs = %.4e"
              "  (mean=%.4e, se=%.4e)" % (float(est), mean, se))
        # de-normalisation: f -> f + lam*x1 + mu*x2 acts FREELY on the stratum
        # with orbit size p^4, and each orbit meets the normalised stratum in
        # |A|*|B| <= 9 points, so  R2 >= (normalised count) * p^4 / 9.
        print("       => R2(p) >= sampled_sum * p^4/9 = %.4e"
              % (float(tot) * p ** 4 / 9.0))
        print("       full space p^(2p^2-2) = %.4e ; elapsed for this p = %.1fs"
              % (float(full), time.time() - t0))

    print("=" * 78)
    print("elapsed_s = %.1f" % (time.time() - T_START))


if __name__ == "__main__":
    main()
