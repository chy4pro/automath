#!/usr/bin/env python3
"""
w133 round 11 (owner-w133) — Lemma G43 (far-end truncation) certified on explicit graphs.

G43: C4-free, geodesic u0..ud with d >= 6, a(u0) >= 2 and a usable side-neighbour x of u0
with a(x) >= 4  ==>  path(G) >= d + 3, WITH NO HYPOTHESIS ON a(ud).
Mechanism: if a(ud) = 1 (leaf or triangle-leaf) then truncate to u0..u_{d-1} (length >= 5)
and use y := ud itself as the far-side vertex -- it is a neighbour of u_{d-1} lying outside
u_{d-2}'s component of G[N(u_{d-1})].  Then G41 gives (d-1)+4 = d+3.

This script builds W1 with leaves and triangle-leaves hung on it, finds geodesics whose far
end has a(ud) = 1, runs the truncation construction, and certifies the resulting path.
NO SAT.
"""
from collections import deque
from itertools import combinations
from fractions import Fraction
FAIL = 0
def check(c, m):
    global FAIL
    if not c: FAIL += 1; print("FAIL:", m)
def adj(n, E):
    g = [set() for _ in range(n)]
    for u, v in E: g[u].add(v); g[v].add(u)
    return g
def bfs(g, s):
    d = [-1]*len(g); d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for w in g[u]:
            if d[w] < 0: d[w] = d[u]+1; q.append(w)
    return d
def a_val(g, v):
    nb = sorted(g[v]); return len(nb) - sum(1 for x, y in combinations(nb, 2) if y in g[x])
def comps(g, v):
    nb = sorted(g[v]); c = {u: {u} for u in nb}
    for x, y in combinations(nb, 2):
        if y in g[x]:
            s = c[x] | c[y]
            for z in s: c[z] = s
    out = []
    for u in nb:
        f = frozenset(c[u])
        if f not in out: out.append(f)
    return out
def ind(g, P):
    return len(set(P)) == len(P) and all((P[j] in g[P[i]]) == (j == i+1)
                                         for i in range(len(P)) for j in range(i+1, len(P)))
def pg2(q):
    def norm(v):
        for i in range(3):
            if v[i] % q:
                iv = pow(v[i], q-2, q); return tuple((c*iv) % q for c in v)
    pts = sorted({norm((a,b,c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a,b,c) != (0,0,0)})
    idx = {p:i for i,p in enumerate(pts)}; m = len(pts); E = []
    for j,L in enumerate(pts):
        for p in pts:
            if sum(p[t]*L[t] for t in range(3)) % q == 0: E.append((idx[p], m+j))
    return 2*m, E

def build(L=8, mode="leaf"):
    """W1 with a hair, plus an a=1 vertex hung at the far end of the hair"""
    bn, be = pg2(5)
    E = [(u,v) for u,v in be] + [(u+bn, v+bn) for u,v in be]
    n = 2*bn; prev = 1
    for _ in range(L):
        E.append((prev, n)); prev = n; n += 1
    E.append((prev, bn))
    tip = prev                     # last internal hair vertex
    if mode == "leaf":             # a bare leaf hung on the hair
        E.append((tip, n)); n += 1
    else:                          # a triangle-leaf: two new vertices forming a triangle
        p, q_, r = tip, n, n+1     # p~q_, p~r, q_~r  -> a(q_) = a(r) = 1
        E += [(p, q_), (p, r), (q_, r)]; n += 2
    return adj(n, E)

def run(name, g):
    n = len(g); a = [a_val(g, v) for v in range(n)]
    l = Fraction(sum(a), n); ecc = [max(bfs(g, v)) for v in range(n)]
    rad = min(ecc)
    ones = [v for v in range(n) if a[v] == 1]
    check(l > 4, "%s: l = %s > 4" % (name, l))
    check(bool(ones), "%s: has a=1 vertices (the case G43 is for)" % name)
    built = 0
    for ud in ones:                                   # far end with a(ud) = 1
        dd = bfs(g, ud)
        for u0 in range(n):
            d = dd[u0]
            if d < 6: continue
            cs = comps(g, u0)
            if len(cs) < 2: continue
            d0 = bfs(g, u0)
            for u1 in g[u0]:
                if d0[u1] != 1 or dd[u1] != d-1: continue
                C1 = next(c for c in cs if u1 in c)
                xs = [x for c in cs if c is not C1 for x in c if a[x] >= 4]
                if not xs: continue
                x = xs[0]
                # geodesic u0..ud
                P = [u0, u1]; cur = u1; ok = True
                while cur != ud:
                    nx = next((w for w in g[cur] if dd[w] == dd[cur]-1 and d0[w] == d0[cur]+1), None)
                    if nx is None: ok = False; break
                    P.append(nx); cur = nx
                if not ok or not ind(g, P): continue
                # TRUNCATE: geodesic u0..u_{d-1}, far-side vertex y := ud
                T = P[:-1]; y = ud
                cT = comps(g, T[-1])
                Cprev = next(c for c in cT if T[-2] in c)
                check(y not in Cprev, "%s: y=ud is outside u_{d-2}'s component" % name)
                check(a_val(g, T[-1]) >= 2, "%s: truncated far end has a >= 2" % name)
                cx = comps(g, x); C0 = next(c for c in cx if u0 in c)
                w = None
                for c in cx:
                    if c is C0: continue
                    reps = [v for v in c if v not in g[T[2]] and v not in g[T[3]]]
                    if reps: w = reps[0]; break
                if w is None: continue
                full = [w, x] + T + [y]
                check(ind(g, full), "%s: truncated G41 path induced (d=%d)" % (name, d))
                check(len(full) == d + 3, "%s: path has d+3 = %d vertices" % (name, d+3))
                built += 1
                if built >= 12:
                    print("  %-26s n=%-5d l=%-9s rad=%-3d  a=1 vertices: %d  certified "
                          "truncation runs: %d (last: d=%d, path=%d)"
                          % (name, n, str(l), rad, len(ones), built, d, len(full)))
                    return built
    print("  %-26s n=%-5d l=%-9s rad=%-3d  a=1 vertices: %d  certified truncation runs: %d"
          % (name, n, str(l), rad, len(ones), built))
    return built

print("=== Lemma G43 (far-end truncation): certification on graphs WITH a=1 vertices ===")
t = 0
t += run("W1+leaf", build(8, "leaf"))
t += run("W1+triangle-leaf", build(8, "tri"))
check(t > 0, "non-vacuous")
print("\n  TOTAL certified truncation runs:", t)
print("\nFAILURES:", FAIL)
raise SystemExit(0 if FAIL == 0 else 1)
