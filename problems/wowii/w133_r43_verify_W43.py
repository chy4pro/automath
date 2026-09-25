#!/usr/bin/env python3
"""STANDALONE re-verification of round 43's witnesses W43a and W43b (rule 105).

This file shares NO code with the builder `w133_r43_caseA.py`.  It reads only the edge lists
`w133_r43_W43a.txt` / `w133_r43_W43b.txt` and re-derives every quantity by a DIFFERENT method:

  * distances      -- BITSET RELAXATION (ball_{k+1}(v) = ball_k(v) OR union of ball_k over
                      neighbours), not breadth-first search with a queue;
  * a(v)           -- BRUTE-FORCE maximum independent subset of N(v) by enumerating all
                      subsets, not the C4-free matching identity deg - (edges inside N(v));
  * C4-freeness    -- a nested loop counting |N(u) AND N(v)| over unordered pairs written
                      from scratch here;
  * every condition of brief E46 restated from its own text and checked separately.

If this file disagrees with the builder about anything, THE BUILDER IS WRONG.
Interpreter: system python3 (pure stdlib).
"""
import sys
from itertools import combinations

FAILS = 0
CHECKS = 0


def check(cond, label):
    global FAILS, CHECKS
    CHECKS += 1
    if cond:
        print("    ok   %s" % label)
    else:
        FAILS += 1
        print("    FAIL %s" % label)


def load(path):
    nn = None
    ed = []
    fh = open(path)
    for line in fh:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) == 1:
            nn = int(parts[0])
        else:
            ed.append((int(parts[0]), int(parts[1])))
    fh.close()
    return nn, ed


def neighbour_masks(nn, ed):
    """N(v) as a Python integer used as a bitset -- a representation the builder never uses."""
    nb = [0] * nn
    for (u, v) in ed:
        nb[u] |= (1 << v)
        nb[v] |= (1 << u)
    return nb


def bits(x):
    out = []
    i = 0
    while x:
        if x & 1:
            out.append(i)
        x >>= 1
        i += 1
    return out


def eccentricities(nn, nb):
    """distance layers by BITSET RELAXATION.  ball[v] grows one step at a time; the step at
    which vertex u enters ball[v] IS d(v,u).  No queue, no visited array."""
    full = (1 << nn) - 1
    ball = [(1 << v) | nb[v] for v in range(nn)]
    dist = [[-1] * nn for _ in range(nn)]
    for v in range(nn):
        dist[v][v] = 0
        for u in bits(nb[v]):
            dist[v][u] = 1
    step = 1
    while True:
        step += 1
        grew = False
        newball = []
        for v in range(nn):
            b = ball[v]
            acc = b
            for u in bits(b & ~(1 << v)):
                acc |= nb[u]
            if acc != b:
                grew = True
                for u in bits(acc & ~b):
                    dist[v][u] = step
            newball.append(acc)
        ball = newball
        if not grew:
            break
        if step > nn + 2:
            raise RuntimeError("relaxation did not converge")
    return dist


def alpha_of_neighbourhood(v, nb):
    """alpha(G[N(v)]) by enumerating EVERY subset of N(v) and keeping the largest independent
    one.  Exponential in deg(v) and that is deliberate: it assumes nothing about the class."""
    nbrs = bits(nb[v])
    k = len(nbrs)
    best = 0
    for size in range(k, 0, -1):
        if size <= best:
            break
        hit = False
        for S in combinations(nbrs, size):
            good = True
            for i in range(len(S)):
                for j in range(i + 1, len(S)):
                    if nb[S[i]] >> S[j] & 1:
                        good = False
                        break
                if not good:
                    break
            if good:
                hit = True
                break
        if hit:
            best = size
            break
    return best


def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


def verify(path, tag):
    print()
    print("=" * 74)
    print("VERIFYING %s  (%s)" % (tag, path))
    print("=" * 74)
    nn, ed = load(path)
    seen = set()
    for (u, v) in ed:
        if u == v:
            raise RuntimeError("loop")
        seen.add((min(u, v), max(u, v)))
    print("  n = %d, edges read = %d, distinct undirected edges = %d" % (nn, len(ed), len(seen)))
    nb = neighbour_masks(nn, ed)

    # --- condition 1a: C4-free in this line's sense (no two vertices with 2 common neighbours)
    worst = 0
    for u in range(nn):
        for v in range(u + 1, nn):
            c = popcount(nb[u] & nb[v])
            if c > worst:
                worst = c
    check(worst <= 1, "C4-FREE: max common neighbours over all pairs = %d (must be <= 1)"
          % worst)

    # --- condition 1b: mu(G) = min_v alpha(G[N(v)]) >= 2, and l(G) = mean alpha
    tot = 0
    mu = None
    for v in range(nn):
        a = alpha_of_neighbourhood(v, nb)
        tot += a
        if mu is None or a < mu:
            mu = a
    lval = tot / float(nn)
    check(mu >= 2, "mu(G) = min_v alpha(G[N(v)]) = %d (must be >= 2)" % mu)

    # --- distances, eccentricities, radius, diameter, centre
    dist = eccentricities(nn, nb)
    for v in range(nn):
        if min(dist[v]) < 0:
            raise RuntimeError("disconnected")
    ecc = [max(dist[v]) for v in range(nn)]
    rad = min(ecc)
    diam = max(ecc)
    ctr = [v for v in range(nn) if ecc[v] == rad]
    print("  rad = %d, diam = %d, |Ctr| = %d, l = %.6f" % (rad, diam, len(ctr), lval))

    # --- condition 2, 3, 5
    check(rad >= 5, "condition 2: rad = %d >= 5" % rad)
    check(diam == rad + 1, "condition 3: diam = %d = rad+1" % diam)
    check(lval > 4, "condition 5: l = %.6f > 4" % lval)

    # --- condition 4: a vertex maximally far from EVERY centre
    good = [w for w in range(nn) if all(dist[c][w] == rad for c in ctr)]
    check(len(good) > 0, "condition 4: %d vertices are at distance exactly rad from EVERY "
                         "centre" % len(good))
    if good:
        w = good[0]
        print("    witness w = %d ; distances to the %d centres: %s"
              % (w, len(ctr), sorted({dist[c][w] for c in ctr})))
        check(all(dist[c][w] == rad for c in ctr), "w = %d: d(c,w) = rad for every centre" % w)
        check(ecc[w] == rad + 1, "w = %d is peripheral, ecc(w) = %d = rad+1 (PER-A)"
              % (w, ecc[w]))
        check(w not in ctr, "w is not itself a centre")
    # --- the round's own claim (CA-EQ)/(FAR): the condition-4 set IS the sphere intersection
    inter = None
    for c in ctr:
        s = {v for v in range(nn) if dist[c][v] == rad}
        inter = s if inter is None else (inter & s)
    check(sorted(inter) == sorted(good), "(FAR): condition-4 set = intersection of the "
                                         "spheres S_rad(c), sizes %d and %d"
          % (len(inter), len(good)))

    # --- WHAT IT DOES NOT BREAK, printed BESIDE the result: (TAIL-2) needs an anchored
    #     induced path on >= ecc(w)+3 vertices.  A BUILT path is a LOWER bound on endpath.
    if good:
        w = good[0]
        want = ecc[w] + 3
        P, longest, trunc = anchored_induced_path(nn, nb, w, want)
        if P is not None:
            check(is_induced_path(nn, nb, P, w) and len(P) >= want,
                  "(TAIL-2): anchored induced path on %d >= ecc(w)+3 = %d vertices BUILT "
                  "and checked: %s" % (len(P), want, P))
        else:
            print("    NOT FOUND within the budget: longest anchored induced path built = %d,"
                  " wanted %d (truncated=%s).  This is a FAILURE TO BUILD, not a proof that "
                  "none exists." % (longest, want, trunc))
    return rad, diam, len(ctr), lval, len(good)


def anchored_induced_path(nn, nb, w, want, budget=300000):
    """ITERATIVE stack DFS for an induced path with ENDPOINT w and at least `want` vertices.
    Written from scratch here; a None means NOT FOUND WITHIN THE BUDGET, never 'none exists'.
    Returned paths are re-checked by `is_induced_path` below, which is the only thing that
    certifies them."""
    stack = [(w, iter(bits(nb[w])))]
    path = [w]
    inpath = {w}
    steps = 0
    longest = 1
    while stack:
        steps += 1
        if steps > budget:
            return None, longest, True
        _, it = stack[-1]
        nxt = None
        for x in it:
            if x in inpath:
                continue
            bad = False
            for y in path[:-1]:
                if nb[y] >> x & 1:
                    bad = True
                    break
            if not bad:
                nxt = x
                break
        if nxt is None:
            stack.pop()
            if path:
                inpath.discard(path.pop())
            continue
        path.append(nxt)
        inpath.add(nxt)
        if len(path) > longest:
            longest = len(path)
        if len(path) >= want:
            return list(path), longest, False
        stack.append((nxt, iter(bits(nb[nxt]))))
    return None, longest, False


def is_induced_path(nn, nb, P, w):
    if not P or P[0] != w or len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if not (nb[P[i]] >> P[i + 1] & 1):
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if nb[P[i]] >> P[j] & 1:
                return False
    return True


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "problems/wowii"
    out = []
    import os
    tags = [t for t in ("W43a", "W43b", "W43c")
            if os.path.exists("%s/w133_r43_%s.txt" % (base, t))]
    for tag in tags:
        out.append(verify("%s/w133_r43_%s.txt" % (base, tag), tag))
    print()
    print("=" * 74)
    for tag, (rad, diam, nc, lv, ng) in zip(tags, out):
        print("  %s : rad %d, diam %d, |Ctr| %d, l %.6f, condition-4 vertices %d"
              % (tag, rad, diam, nc, lv, ng))
    print("  CHECKS %d   FAILS %d" % (CHECKS, FAILS))
    print("=" * 74)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
