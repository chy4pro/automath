#!/usr/bin/env python3
"""STANDALONE re-verification of round 44's witness `W44a` (rule 105).

Shares NO code with `w133_r44_row.py`: it reads the edge list and nothing else, and every
quantity is recomputed by a DIFFERENT algorithm from the one that built it --
  * distances by iterated BITSET RELAXATION, not BFS;
  * a(v) = alpha(G[N(v)]) by BRUTE-FORCE SUBSET ENUMERATION, not by the matching identity;
  * C4-freeness by a from-scratch nested common-neighbour count;
  * the anchored induced path checked edge by edge and non-edge by non-edge.
Every condition of the CASE A class is restated here from the draft's own text, not imported.
Interpreter: system python3 (pure stdlib).  Exit 0 iff every check passes.
"""
import sys
from itertools import combinations

CK = 0
BAD = 0


def ck(c, m):
    global CK, BAD
    CK += 1
    if not c:
        BAD += 1
        print("FAIL: " + m)


def read_edges(fn):
    n = None
    E = []
    for ln in open(fn):
        ln = ln.split("#")[0].strip()
        if not ln:
            continue
        t = ln.split()
        if len(t) == 1:
            n = int(t[0])
        elif len(t) == 2:
            E.append((int(t[0]), int(t[1])))
    return n, E


def main():
    fn = "problems/wowii/w133_r44_W44a.txt"
    n, E = read_edges(fn)
    ck(n is not None, "order line present")
    # ---------- adjacency as BITMASKS (a representation the builder never used)
    N = [0] * n
    for (u, v) in E:
        ck(0 <= u < n and 0 <= v < n and u != v, "edge %d-%d in range and not a loop" % (u, v))
        N[u] |= 1 << v
        N[v] |= 1 << u
    m = len(set((min(a, b), max(a, b)) for (a, b) in E))
    ck(m == len(E), "no repeated edge in the file")
    print("read %s: n = %d, |E| = %d" % (fn, n, m))

    # ---------- C4-freeness: no two distinct vertices with >= 2 common neighbours
    bad = 0
    for u in range(n):
        for v in range(u + 1, n):
            c = N[u] & N[v]
            if c and (c & (c - 1)):
                bad += 1
    ck(bad == 0, "C4-free: no pair of vertices has two common neighbours (%d offenders)" % bad)

    # ---------- distances by BITSET RELAXATION (reach_k = ball of radius k)
    full = (1 << n) - 1
    ecc = [0] * n
    dist = []
    for s in range(n):
        ball = 1 << s
        row = [-1] * n
        row[s] = 0
        k = 0
        while ball != full:
            nxt = ball
            b = ball
            while b:
                low = b & (-b)
                i = low.bit_length() - 1
                nxt |= N[i]
                b ^= low
            if nxt == ball:
                break
            k += 1
            new = nxt & ~ball
            b = new
            while b:
                low = b & (-b)
                row[low.bit_length() - 1] = k
                b ^= low
            ball = nxt
        ck(ball == full, "graph is connected from %d" % s if s < 1 else "connected")
        ecc[s] = k
        dist.append(row)
    rad = min(ecc)
    diam = max(ecc)
    Ctr = [v for v in range(n) if ecc[v] == rad]
    print("rad = %d, diam = %d, |Ctr| = %d, Ctr = %s" % (rad, diam, len(Ctr), Ctr[:12]))

    # ---------- a(v) by BRUTE-FORCE independent-set enumeration inside N(v)
    def alpha_nb(v):
        nb = [i for i in range(n) if (N[v] >> i) & 1]
        best = 0
        for k in range(len(nb), 0, -1):
            if k <= best:
                break
            for S in combinations(nb, k):
                ok = True
                for i in range(len(S)):
                    for j in range(i + 1, len(S)):
                        if (N[S[i]] >> S[j]) & 1:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    best = k
                    break
            if best >= k:
                break
        return best

    A = [alpha_nb(v) for v in range(n)]
    mu = min(A)
    l = sum(A) / float(n)
    print("mu = %d, l = %.6f, mean degree = %.6f" % (mu, l, 2.0 * m / n))

    # ---------- the CASE A class, restated from the draft's own text
    cond4 = [w for w in range(n) if all(dist[c][w] == rad for c in Ctr)]
    cond4 = [w for w in cond4 if ecc[w] == rad + 1]
    ck(diam == rad + 1, "condition 2: the host is ROUND (diam = rad+1) -- CASE A")
    ck(rad >= 5, "condition 3: rad >= 5")
    ck(l > 4, "condition 5: l > 4")
    ck(mu >= 2, "condition 1: mu >= 2 (no a = 1 vertex)")
    ck(len(cond4) > 0, "condition 4 is carried by at least one vertex")
    ck(mu <= 3, "THE POINT OF THIS WITNESS: mu <= 3, unlike W43a/W43b/W43c")
    print("condition-4 vertices with ecc = rad+1: %d  (first: %s)" % (len(cond4), cond4[:8]))

    # ---------- the pendant instance, and the target it has to meet
    #            G := H + one pendant at w.  a(pendant) = 1; a(w) rises by exactly 1 because
    #            the new neighbour is isolated in N(w).
    w0 = cond4[0]
    sumA_G = sum(A) + 1 + 1
    lG = sumA_G / float(n + 1)
    print("G = H + pendant at w=%d:  l(G) = %.6f, floor(l(G)) = %d, rad(G) = %d, target = %d"
          % (w0, lG, int(lG), rad + 1, rad + 1 + int(lG)))
    ck(int(lG) == 4, "floor(l(G)) = 4 -- the instance is in route A2's regime")

    # ---------- the (TAIL-2) certificate at w0, built here and checked here
    def build(w):
        far = [x for x in range(n) if dist[w][x] == ecc[w]]
        for x in far:
            # one geodesic, walked back from x
            P = [x]
            cur = x
            while cur != w:
                for p in range(n):
                    if ((N[cur] >> p) & 1) and dist[w][p] == dist[w][cur] - 1:
                        P.append(p)
                        cur = p
                        break
            P.reverse()
            d = len(P) - 1
            for y in range(n):
                if not ((N[P[d]] >> y) & 1):
                    continue
                if y == P[d - 1] or ((N[P[d - 1]] >> y) & 1):
                    continue
                if any(y == P[i] or ((N[P[i]] >> y) & 1) for i in range(d)):
                    continue
                for z in range(n):
                    if not ((N[y] >> z) & 1):
                        continue
                    R = P + [y, z]
                    if len(set(R)) != len(R):
                        continue
                    good = True
                    for i in range(len(R)):
                        for j in range(i + 2, len(R)):
                            if (N[R[i]] >> R[j]) & 1:
                                good = False
                                break
                        if not good:
                            break
                    if good:
                        return R
        return None

    R = build(w0)
    ck(R is not None, "an anchored induced path was BUILT at w=%d" % w0)
    if R is not None:
        ck(R[0] == w0, "the path starts at w")
        ck(len(R) == ecc[w0] + 3, "the path has ecc(w)+3 = %d vertices" % (ecc[w0] + 3))
        for i in range(len(R) - 1):
            ck((N[R[i]] >> R[i + 1]) & 1, "consecutive vertices adjacent")
        nb = 0
        for i in range(len(R)):
            for j in range(i + 2, len(R)):
                if (N[R[i]] >> R[j]) & 1:
                    nb += 1
        ck(nb == 0, "no chord: the path is INDUCED")
        print("anchored induced path on %d vertices: %s" % (len(R), R))
        print("so path(G) >= 1 + %d = %d >= target %d"
              % (len(R), 1 + len(R), rad + 1 + int(lG)))

    # ---------- it is genuinely a different host from W43a
    try:
        n2, E2 = read_edges("problems/wowii/w133_r43_W43a.txt")
        ck(n == n2 + 1, "W44a has exactly one vertex more than W43a")
        deg_last = bin(N[n - 1]).count("1")
        ck(deg_last == 2, "the extra vertex has degree 2 (it is the subdivision vertex)")
        ck(alpha_nb(n - 1) == 2, "and a(.) = 2 there, which is what pins mu at 2")
    except IOError:
        print("W43a not readable; the comparison checks were skipped")

    print("CHECKS %d  FAILS %d" % (CK, BAD))
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main())
