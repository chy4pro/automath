#!/usr/bin/env python3
"""WOWII-133 round 42, second script -- MINIMISE the E44 witness, then dump its edge list.

The first script (w133_r42_split.py) settled that E44's class is NON-EMPTY: 146 instances
over 34 necklace hosts, smallest n = 120.  A witness is only useful to other people if it is
small enough to check by hand, so this script sweeps the necklace family downwards in order
and prints the EDGE LIST of the smallest host carrying an E44 instance.

Self-contained: primitives COPIED from w133_r42_split.py, never imported.
Interpreter: system python3 (pure stdlib).  No SAT, no exhaustive graph enumeration --
the sweep is over a DESIGNED construction family with seeded-random matchings.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 900.0
CHECKS = 0
FAILS = 0


def over():
    return (time.time() - T0) > DEADLINE


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = k
                break
        if best == k:
            break
    return best


def a_val_matching(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    return D, ecc, min(ecc)


def centre_of(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] == r]


def pg2(q):
    def norm(v):
        for i in range(3):
            if v[i] % q:
                inv = pow(v[i], q - 2, q)
                return tuple((c * inv) % q for c in v)
    pts = sorted({norm((a, b, c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a, b, c) != (0, 0, 0)})
    idx = {p: i for i, p in enumerate(pts)}
    m = len(pts)
    E = []
    for j, L in enumerate(pts):
        for p in pts:
            if sum(p[t] * L[t] for t in range(3)) % q == 0:
                E.append((idx[p], m + j))
    return adj(2 * m, E)


class LCG(object):
    def __init__(self, seed):
        self.s = seed % (1 << 31)

    def nxt(self, k):
        self.s = (self.s * 1103515245 + 12345) % (1 << 31)
        return self.s % k

    def shuffled(self, xs):
        xs = list(xs)
        for i in range(len(xs) - 1, 0, -1):
            j = self.nxt(i + 1)
            xs[i], xs[j] = xs[j], xs[i]
        return xs


def necklace(qs, seed, fracs=None):
    """m >= 5 blocks in a cycle; sources are POINTS (an independent set of the block)."""
    m = len(qs)
    blocks = [pg2(q) for q in qs]
    off = []
    tot = 0
    for b in blocks:
        off.append(tot)
        tot += len(b)
    E = []
    for i, b in enumerate(blocks):
        for (u, v) in edges_of(b):
            E.append((off[i] + u, off[i] + v))
    rng = LCG(seed)
    for i in range(m):
        j = (i + 1) % m
        npts = len(blocks[i]) // 2
        srcs = rng.shuffled(range(npts))
        f = 1.0 if fracs is None else fracs[i % len(fracs)]
        k = max(1, int(round(npts * f)))
        k = min(k, len(blocks[j]))
        srcs = srcs[:k]
        tgts = rng.shuffled(range(len(blocks[j])))[:k]
        for s, t in zip(srcs, tgts):
            E.append((off[i] + s, off[j] + t))
    return adj(tot, E)


def e44_hits(g):
    """every w with ecc(w)=rad+1 AND d(c,w)=rad for every centre c."""
    D, ecc, r = profile(g)
    C = centre_of(ecc, r)
    out = []
    for w in range(len(g)):
        if ecc[w] == r + 1 and all(D[c][w] == r for c in C):
            out.append(w)
    return out, r, max(ecc), len(C)


def main():
    print("WOWII-133 round 42 (second script) -- MINIMISING THE E44 WITNESS")
    print("interpreter: %s" % sys.version.split()[0])
    print()
    print("SWEEP.  Necklaces of PG(2,q) blocks, q in {2,3}, m in 5..9, four matching-density")
    print("schedules, seeds 1..12.  DESIGNED family, seeded-random matchings, NOT exhaustive.")
    print("A host counts only if it is certified in class BY MACHINE: connected, C4-free by a")
    print("brute pair scan, mu >= 2, l > 4, rad >= 5.")
    patterns = []
    for m in (5, 6, 7, 8, 9):
        patterns.append(([3, 2] * m)[:m])
        patterns.append(([3] + [2] * (m - 1)))
        patterns.append(([3, 2, 2] * m)[:m])
        patterns.append(([2] * m))
        patterns.append(([3] * m))
    scheds = [None, (1.0, 0.4), (1.0, 0.6, 0.3), (0.9, 0.2, 0.7, 0.35)]
    built = inclass = 0
    hits = []
    for qs in patterns:
        for si, sched in enumerate(scheds):
            for s in range(1, 13):
                if over():
                    break
                g = necklace(qs, s * 6700417 + len(qs) * 31 + si * 7919, sched)
                built += 1
                if not connected(g) or not c4_free(g):
                    continue
                if min(a_val_matching(g, v) for v in range(len(g))) < 2:
                    continue
                lg = sum(a_val_matching(g, v) for v in range(len(g))) / float(len(g))
                if lg <= 4:
                    continue
                ws, r, diam, nc = e44_hits(g)
                if r < 5:
                    continue
                inclass += 1
                if ws:
                    hits.append((len(g), tuple(qs), si, s, tuple(ws), r, diam, lg, nc, g))
    print()
    print("  necklaces built                      : %d" % built)
    print("  certified IN CLASS (C4-free, mu>=2, l>4, rad>=5): %d" % inclass)
    print("  of those, CARRYING an E44 instance   : %d" % len(hits))
    print("  POPULATION RULE 90: the count that could have come out the other way is the %d"
          % inclass)
    print("  in-class hosts; every one of them was tested at every vertex.")
    hits.sort(key=lambda t: (t[0], -len(t[4])))
    print()
    print("  SMALLEST TEN HOSTS CARRYING AN E44 INSTANCE:")
    print("  %5s %-22s %4s %4s %5s %6s %7s %6s %s"
          % ("n", "blocks", "sch", "seed", "rad", "diam", "l", "|Ctr|", "w's"))
    for (n, qs, si, s, ws, r, diam, lg, nc, g) in hits[:10]:
        print("  %5d %-22s %4d %4d %5d %6d %7.4f %6d %s"
              % (n, "".join(str(q) for q in qs), si, s, r, diam, lg, nc, list(ws)[:6]))
    if not hits:
        print("  NO instance found in this sweep.  That does NOT contradict the first script:")
        print("  it would mean this sweep's sub-family misses them.")
        return 1 if FAILS else 0

    n, qs, si, s, ws, r, diam, lg, nc, g = hits[0]
    print()
    print("=" * 78)
    print("THE MINIMAL WITNESS OF THIS SWEEP -- graded as an OBJECT before it is quoted")
    print("=" * 78)
    ck(connected(g), "witness connected")
    ck(c4_free(g), "witness C4-free (brute pair scan over all vertex pairs)")
    aa = [a_val(g, v) for v in range(n)]     # BRUTE alpha, not the matching formula
    mu = min(aa)
    lbrute = sum(aa) / float(n)
    ck(mu >= 2, "witness mu >= 2 by BRUTE alpha")
    ck(lbrute > 4, "witness l > 4 by BRUTE alpha")
    D, ecc, rr = profile(g)
    C = centre_of(ecc, rr)
    ck(rr >= 5, "witness rad >= 5")
    print("  n = %d   |E| = %d   mu = %d   l = %.4f   rad = %d   diam = %d   |Ctr| = %d  Ctr = %s"
          % (n, len(edges_of(g)), mu, lbrute, rr, max(ecc), len(C), C))
    for w in ws:
        ck(ecc[w] == rr + 1, "witness w=%d has ecc = rad+1" % w)
        ck(all(D[c][w] == rr for c in C), "witness w=%d maximally far from EVERY centre" % w)
        print("  w = %d : ecc(w) = %d = rad+1 ; d(c,w) = %s for every centre ; CASE %s"
              % (w, ecc[w], sorted({D[c][w] for c in C}), "A" if max(ecc) == rr + 1 else "B"))
    print()
    print("  EDGE LIST (the object; everything above is a claim ABOUT it):")
    E = edges_of(g)
    for i in range(0, len(E), 14):
        print("    " + " ".join("(%d,%d)" % e for e in E[i:i + 14]))
    print()
    print("  PYTHON LITERAL, for an independent checker:")
    print("  EDGES = " + repr(E))

    # A SECOND witness, chosen for the LARGEST l -- because a witness at l = 4.02 uses the
    # l > 4 hypothesis by a hair, and a reader is entitled to one that does not.
    hits.sort(key=lambda t: -t[7])
    n2, qs2, si2, s2, ws2, r2, diam2, lg2, nc2, g2 = hits[0]
    print()
    print("=" * 78)
    print("THE LARGEST-l WITNESS OF THIS SWEEP (same grading)")
    print("=" * 78)
    aa2 = [a_val(g2, v) for v in range(n2)]
    ck(min(aa2) >= 2, "witness-2 mu >= 2 by BRUTE alpha")
    lb2 = sum(aa2) / float(n2)
    ck(lb2 > 4, "witness-2 l > 4 by BRUTE alpha")
    ck(c4_free(g2), "witness-2 C4-free")
    D2, ecc2, rr2 = profile(g2)
    C2 = centre_of(ecc2, rr2)
    print("  n = %d   |E| = %d   mu = %d   l = %.4f   rad = %d   diam = %d   |Ctr| = %d"
          % (n2, len(edges_of(g2)), min(aa2), lb2, rr2, max(ecc2), len(C2)))
    for w in ws2:
        ck(ecc2[w] == rr2 + 1 and all(D2[c][w] == rr2 for c in C2),
           "witness-2 w=%d satisfies conditions 2 and 3" % w)
        print("  w = %d : ecc(w) = %d = rad+1 ; d(c,w) = %s for every centre ; CASE %s"
              % (w, ecc2[w], sorted({D2[c][w] for c in C2}),
                 "A" if max(ecc2) == rr2 + 1 else "B"))
    print("  PYTHON LITERAL: EDGES2 = " + repr(edges_of(g2)))
    print()
    print("CHECKS: %d   FAILURES: %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
