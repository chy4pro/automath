#!/usr/bin/env python3
"""
w133 round 11 (owner-w133) — the refined fork (Q-RAD'):
does there exist a connected C4-free graph with l > 4, rad >= 5 AND diam <= rad + 2 ?

Route: a VERTEX-TRANSITIVE graph has rad = diam, so diam <= rad+2 is automatic.  Take a
Cayley graph of PSL(2,p) on 3 generators (degree 6).  If it is triangle-free and C4-free
then a(v) = d(v) = 6 for every v, so l = 6 > 4; one BFS from the identity gives
ecc = rad = diam by transitivity.  All we need is one such graph with ecc >= 5.

NO SAT.  Explicit constructions only; the generator triples are drawn from a fixed
deterministic list of seeds and every candidate is fully verified before being reported.
"""
import random
from collections import deque
from itertools import combinations

FAIL = 0


def check(cond, msg):
    global FAIL
    if not cond:
        FAIL += 1
        print("FAIL:", msg)
    return cond


def psl2(p):
    """elements of PSL(2,p) as canonical representatives of SL(2,p)/{+-I}"""
    els = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        els.append((a, b, c, d))

    def canon(m):
        a, b, c, d = m
        neg = ((-a) % p, (-b) % p, (-c) % p, (-d) % p)
        return min(m, neg)

    return sorted({canon(m) for m in els}), canon


def mul(x, y, p):
    a, b, c, d = x
    e, f, g, h = y
    return ((a * e + b * g) % p, (a * f + b * h) % p,
            (c * e + d * g) % p, (c * f + d * h) % p)


def inv(x, p):
    a, b, c, d = x
    return (d % p, (-b) % p, (-c) % p, a % p)   # det = 1


def cayley(p, gens, els, canon):
    idx = {m: i for i, m in enumerate(els)}
    S = []
    for g in gens:
        S.append(canon(g))
        S.append(canon(inv(g, p)))
    S = [s for s in S]
    if len(set(S)) != len(S):
        return None, None            # involution or repeated generator: degree drops
    n = len(els)
    g = [set() for _ in range(n)]
    for i, m in enumerate(els):
        for s in S:
            j = idx[canon(mul(m, s, p))]
            if j == i:
                return None, None
            g[i].add(j)
    if any(len(gg) != len(S) for gg in g):
        return None, None
    return g, idx


def connected_from(g, s):
    n = len(g)
    dist = [-1] * n
    dist[s] = 0
    dq = deque([s])
    seen = 1
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                seen += 1
                dq.append(w)
    return seen == n, dist


def triangle_free(g):
    for u in range(len(g)):
        for a, b in combinations(g[u], 2):
            if b in g[a]:
                return False
    return True


def c4_free(g):
    """no two distinct vertices with two common neighbours; checked by counting
    length-2 paths out of every vertex"""
    for u in range(len(g)):
        seen = {}
        for w in g[u]:
            for z in g[w]:
                if z == u:
                    continue
                seen[z] = seen.get(z, 0) + 1
                if seen[z] >= 2:
                    return False, (u, z)
    return True, None


def greedy_induced_path(g, start, rng, tries=200):
    """lower bound on path(G): randomized DFS-ish greedy, returns best length found"""
    n = len(g)
    best = 0
    for _ in range(tries):
        cur = start if best == 0 else rng.randrange(n)
        P = [cur]
        inP = {cur}
        blocked = set()          # neighbours of every path vertex EXCEPT the last one
        while True:
            cands = [w for w in g[P[-1]] if w not in inP and w not in blocked]
            if not cands:
                break
            nxt = rng.choice(cands)
            blocked |= set(g[P[-1]])   # P[-1] stops being the last vertex now
            P.append(nxt)
            inP.add(nxt)
        # certify: P must be an induced path
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                assert (P[j] in g[P[i]]) == (j == i + 1), "greedy produced a chord"
        best = max(best, len(P))
    return best


def main():
    rng = random.Random(20260822)
    print("=== (Q-RAD') hunt: vertex-transitive C4-free Cayley graphs of PSL(2,p) ===")
    print("    vertex-transitive => rad = diam => diam <= rad+2 automatic")
    print()
    found = []
    for p in (11, 13, 17, 19, 23):
        els, canon = psl2(p)
        n = len(els)
        nontriv = [m for m in els if m != canon((1, 0, 0, 1))]
        for attempt in range(60):
            gens = [nontriv[rng.randrange(len(nontriv))] for _ in range(3)]
            g, idx = cayley(p, gens, els, canon)
            if g is None:
                continue
            ok, dist = connected_from(g, idx[canon((1, 0, 0, 1))])
            if not ok:
                continue
            if not triangle_free(g):
                continue
            c4ok, wit = c4_free(g)
            if not c4ok:
                continue
            ecc = max(dist)
            deg = len(g[0])
            print("  p=%2d n=%-6d deg=%d  girth>=5 OK  ecc(id)=rad=diam=%d   l=%d"
                  % (p, n, deg, ecc, deg))
            found.append((p, n, deg, ecc, gens, g))
            break
    print()
    winners = [f for f in found if f[3] >= 5]
    if not winners:
        print("  no candidate with ecc >= 5 in this sweep")
    for (p, n, deg, ecc, gens, g) in winners[:2]:
        print("=== WITNESS W2: Cayley(PSL(2,%d), 3 gens), n=%d ===" % (p, n))
        print("    generators (as SL(2,%d) matrices [a b; c d]): %s" % (p, gens))
        # full independent re-verification
        ok, dist = connected_from(g, 0)
        check(ok, "W2 connected")
        check(triangle_free(g), "W2 triangle-free")
        c4ok, wit = c4_free(g)
        check(c4ok, "W2 C4-free (witness %r)" % (wit,))
        check(all(len(g[v]) == deg for v in range(n)), "W2 regular of degree %d" % deg)
        # a(v) = d(v) since triangle-free; l = deg
        l = deg
        check(l > 4, "W2: l = %d > 4" % l)
        # rad = diam = ecc(any vertex) by vertex-transitivity; verify on 3 vertices
        eccs = []
        for s in (0, n // 3, 2 * n // 3):
            okc, d2 = connected_from(g, s)
            eccs.append(max(d2))
        check(len(set(eccs)) == 1, "W2: ecc equal from sampled vertices %r (transitivity)" % eccs)
        rad = diam = eccs[0]
        check(rad >= 5, "W2: rad = %d >= 5" % rad)
        check(diam <= rad + 2, "W2: diam <= rad+2")
        lb = greedy_induced_path(g, 0, rng, tries=60)
        print("    n=%d  l=%d  rad=diam=%d   path(G) >= %d   (rad+4 = %d)  -> %s"
              % (n, l, rad, lb, rad + 4,
                 "conjecture (G+k) k=2 SATISFIED on this witness"
                 if lb >= rad + 4 else "NOT yet certified >= rad+4"))
        check(lb >= rad + 4, "W2: greedy induced path reaches rad+4")
        print("    HARD-WINDOW CHECK: diam+1 = %d < rad+4 = %d  ==> the (R1) device does NOT"
              % (diam + 1, rad + 4))
        print("    settle this graph; it is a genuine hard instance of pocket 2 at rad >= 5.")

    print()
    print("FAILURES:", FAIL)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
