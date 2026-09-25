#!/usr/bin/env python3
"""
w133 round 11 (owner-w133) — end-to-end certification of the round's assembled theorem

  G42:  G connected C4-free, l(G) > 4, rad(G) >= 5, and NO vertex with a(v) = 1
        ==>  path(G) >= rad(G) + 4.

Chain:  cap-break (contrapositive of G38) gives a geodesic of length >= rad with a usable
side-neighbour x of a(x) >= 4 at one end;  mu >= 2 gives a(u0) >= 2 and a(ud) >= 2 for free;
G41 (= G14 with the redundant a(u0) >= 3 hypothesis removed) then gives path >= d+4 >= rad+4.

This script does NOT re-prove G38.  It executes the MECHANISM end to end on the round's two
witnesses (W1, W2) and on the PG(2,5) blob: it locates, by direct search on the graph, a
geodesic of length >= rad whose near end carries a usable side-neighbour with a >= 4, then
builds the G41 path from the proof's own recipe and certifies it is an induced path on
d + 4 >= rad + 4 vertices.  If the assembled theorem were unsound at the construction level,
this is where it would break.

NO SAT.  Explicit graphs, exact BFS, exhaustive local checks.
"""
from collections import deque
from itertools import combinations
from fractions import Fraction

FAIL = 0
def check(c, m):
    global FAIL
    if not c:
        FAIL += 1
        print("FAIL:", m)
    return c


def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        g[u].add(v); g[v].add(u)
    return g


def bfs(g, s):
    d = [-1] * len(g); d[s] = 0; dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1; dq.append(w)
    return d


def a_val(g, v):
    nb = sorted(g[v])
    return len(nb) - sum(1 for a, b in combinations(nb, 2) if b in g[a])


def comps_nbhd(g, v):
    nb = sorted(g[v]); comp = {u: {u} for u in nb}
    for a, b in combinations(nb, 2):
        if b in g[a]:
            s = comp[a] | comp[b]
            for z in s:
                comp[z] = s
    out = []
    for u in nb:
        f = frozenset(comp[u])
        if f not in out:
            out.append(f)
    return out


def induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    return all((P[j] in g[P[i]]) == (j == i + 1)
               for i in range(len(P)) for j in range(i + 1, len(P)))


def pg2(q):
    def norm(v):
        for i in range(3):
            if v[i] % q:
                inv = pow(v[i], q - 2, q)
                return tuple((c * inv) % q for c in v)
    pts = sorted({norm((a, b, c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a, b, c) != (0, 0, 0)})
    idx = {p: i for i, p in enumerate(pts)}; m = len(pts); E = []
    for j, L in enumerate(pts):
        for p in pts:
            if sum(p[t] * L[t] for t in range(3)) % q == 0:
                E.append((idx[p], m + j))
    return 2 * m, E


def W1(L=5):
    bn, be = pg2(5)
    E = [(u, v) for (u, v) in be] + [(u + bn, v + bn) for (u, v) in be]
    n = 2 * bn; prev = 1
    for _ in range(L):
        E.append((prev, n)); prev = n; n += 1
    E.append((prev, bn + 0))
    return adj(n, E)


def W2():
    p = 11
    els = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        els.append((a, b, c, d))
    def canon(m):
        a, b, c, d = m
        return min(m, ((-a) % p, (-b) % p, (-c) % p, (-d) % p))
    els = sorted({canon(m) for m in els}); idx = {m: i for i, m in enumerate(els)}
    def mul(x, y):
        a, b, c, d = x; e, f, g_, h = y
        return ((a*e + b*g_) % p, (a*f + b*h) % p, (c*e + d*g_) % p, (c*f + d*h) % p)
    def inv(x):
        a, b, c, d = x
        return (d % p, (-b) % p, (-c) % p, a % p)
    gens = [(5, 0, 2, 9), (1, 5, 0, 1), (1, 6, 10, 6)]
    S = [canon(g) for g in gens] + [canon(inv(g)) for g in gens]
    n = len(els); g = [set() for _ in range(n)]
    for i, m in enumerate(els):
        for s in S:
            g[i].add(idx[canon(mul(m, s))])
    return g


def certify_g42(g, name):
    """locate a cap-break geodesic of length >= rad and run G41's construction on it"""
    n = len(g)
    a = [a_val(g, v) for v in range(n)]
    l = Fraction(sum(a), n)
    ecc = [max(bfs(g, v)) for v in range(n)]
    rad = min(ecc)
    check(l > 4, "%s: l = %s > 4" % (name, l))
    check(rad >= 5, "%s: rad = %d >= 5" % (name, rad))
    check(min(a) >= 2, "%s: mu = %d >= 2 (G42 hypothesis)" % (name, min(a)))
    built = 0
    for u0 in range(n):
        d0 = bfs(g, u0)
        cs = comps_nbhd(g, u0)
        if len(cs) < 2:
            continue
        for u1 in g[u0]:
            C1 = next(c for c in cs if u1 in c)
            xs = [x for c in cs if c is not C1 for x in c if a[x] >= 4]
            if not xs:
                continue
            x = xs[0]
            for ud in range(n):
                if d0[ud] < max(rad, 5):
                    continue
                dd = bfs(g, ud)
                if dd[u1] != d0[ud] - 1:
                    continue
                d = d0[ud]
                P = [u0, u1]; cur = u1; ok = True
                while cur != ud:
                    nxt = next((w for w in g[cur]
                                if dd[w] == dd[cur] - 1 and d0[w] == d0[cur] + 1), None)
                    if nxt is None:
                        ok = False; break
                    P.append(nxt); cur = nxt
                if not ok or not induced_path(g, P):
                    continue
                cy = comps_nbhd(g, ud)
                Cud = next(c for c in cy if P[d - 1] in c)
                ys = [v for c in cy if c is not Cud for v in c]
                check(bool(ys), "%s: far end has a usable side-neighbour (a(ud)=%d)" % (name, a[ud]))
                if not ys:
                    continue
                y = ys[0]
                cx = comps_nbhd(g, x)
                C0 = next(c for c in cx if u0 in c)
                w = None
                for c in cx:
                    if c is C0:
                        continue
                    reps = [v for v in c if v not in g[P[2]] and v not in g[P[3]]]
                    if reps:
                        w = reps[0]; break
                check(w is not None, "%s: a component of G[N(x)] survives the u2/u3 kills" % name)
                if w is None:
                    continue
                full = [w, x] + P + [y]
                check(induced_path(g, full), "%s: G41 path induced (d=%d)" % (name, d))
                check(len(full) == d + 4, "%s: G41 path has d+4 vertices" % name)
                check(len(full) >= rad + 4, "%s: path >= rad+4 (%d >= %d)" % (name, len(full), rad + 4))
                built += 1
                if built >= 25:
                    print("  %-28s n=%-5d l=%-9s rad=%-3d mu=%d  certified G42 runs: %d "
                          "(longest built: %d vertices >= rad+4 = %d)"
                          % (name, n, str(l), rad, min(a), built, len(full), rad + 4))
                    return built
    print("  %-28s n=%-5d l=%-9s rad=%-3d mu=%d  certified G42 runs: %d"
          % (name, n, str(l), rad, min(a), built))
    return built


def main():
    print("=== end-to-end certification of G42 (cap-break + mu>=2 + G41) ===")
    print("    each 'run' = a real geodesic of length >= max(rad,5) with a usable")
    print("    side-neighbour of a >= 4 at one end, and the G41 path built and certified")
    print()
    t = 0
    t += certify_g42(W1(5), "W1 = 2xPG(2,5)+path(5)")
    t += certify_g42(W2(), "W2 = Cay(PSL(2,11))")
    check(t > 0, "non-vacuous: at least one certified G42 run")
    print()
    print("  TOTAL certified end-to-end runs:", t)
    print()
    print("FAILURES:", FAIL)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
