#!/usr/bin/env python3
"""
w133 round 13 — INDEPENDENT verification of the Q32 (Qwen3.8-Max) refutation claim
against Problem B / (FAR-2).

Nothing is taken from the model's output except the RECIPE:
  core = PG(2,4) point/line incidence graph over GF(4)
  hairs = 2-vertex pendant paths s - h_s - f_s at
          S = {[1:0:0],[0:1:0],[0:0:1]} as POINTS and the same three triples as LINES.
Everything else (GF(4) tables, point/line lists, adjacency, a-values, rad, diam,
geodesic classification, peeling, induced-path search) is rebuilt here from scratch.

Assertions fire on any mismatch; exit 0 with 0 failures means the witness verifies.
"""
import itertools, sys
from collections import deque

FAIL = []
def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}" + (f"   [{detail}]" if detail else ""))
    else:
        print(f"  FAIL  {name}   [{detail}]")
        FAIL.append(name)

# ---------------------------------------------------------------- GF(4)
# elements 0,1,2,3  <->  0, 1, a, a^2   with a^2 = a+1, char 2.
# Represent as 2-bit polynomials over GF(2): bit0 = const, bit1 = coeff of a.
# 0=00, 1=01, a=10, a^2=a+1=11.
def gadd(x, y):
    return x ^ y

def gmul(x, y):
    # carryless multiply then reduce mod a^2+a+1
    r = 0
    for i in range(2):
        if (y >> i) & 1:
            r ^= x << i
    # reduce: bit2 (a^2) -> a+1 = 0b11
    if r & 0b100:
        r ^= 0b100
        r ^= 0b011
    return r & 0b11

# sanity on the field
els = [0, 1, 2, 3]
for x in els:
    check_mul_ok = True
# additive group
assert all(gadd(x, x) == 0 for x in els), "char 2 failed"
assert all(gmul(1, x) == x for x in els), "unit failed"
assert gmul(2, 2) == 3, "a^2 must be a+1"
assert gmul(2, 3) == 1, "a*a^2 must be 1"
assert gmul(3, 3) == 2, "a^2*a^2 must be a"
# every nonzero element invertible
for x in [1, 2, 3]:
    assert any(gmul(x, y) == 1 for y in [1, 2, 3]), "not a field"
print("GF(4) tables self-checked (char 2, a^2=a+1, all nonzero invertible).")

# ---------------------------------------------------------------- PG(2,4)
def normalize(t):
    """Canonical representative of the projective triple: scale so the first
    nonzero coordinate is 1."""
    for c in t:
        if c != 0:
            inv = next(y for y in [1, 2, 3] if gmul(c, y) == 1)
            return tuple(gmul(inv, u) for u in t)
    return None

triples = [t for t in itertools.product(els, repeat=3) if t != (0, 0, 0)]
PROJ = sorted(set(normalize(t) for t in triples))
check("PG(2,4) has 21 projective triples", len(PROJ) == 21, f"got {len(PROJ)}")

def dot(p, l):
    return gadd(gadd(gmul(p[0], l[0]), gmul(p[1], l[1])), gmul(p[2], l[2]))

points = [("P", t) for t in PROJ]
lines  = [("L", t) for t in PROJ]
core = points + lines
check("core size 42", len(core) == 42, f"got {len(core)}")

adj = {v: set() for v in core}
for p in points:
    for l in lines:
        if dot(p[1], l[1]) == 0:
            adj[p].add(l)
            adj[l].add(p)

# projective-plane axioms, verified (not assumed)
degs = sorted(set(len(adj[v]) for v in core))
check("core is 5-regular", degs == [5], f"degree set {degs}")
bad = 0
for a_, b_ in itertools.combinations(points, 2):
    if len(adj[a_] & adj[b_]) != 1:
        bad += 1
for a_, b_ in itertools.combinations(lines, 2):
    if len(adj[a_] & adj[b_]) != 1:
        bad += 1
check("any 2 points on exactly 1 line; any 2 lines meet in exactly 1 point", bad == 0,
      f"{bad} violations")

# ---------------------------------------------------------------- hairs
S = [("P", (1, 0, 0)), ("P", (0, 1, 0)), ("P", (0, 0, 1)),
     ("L", (1, 0, 0)), ("L", (0, 1, 0)), ("L", (0, 0, 1))]
for s in S:
    assert s in adj, f"attachment vertex {s} not in core"

G = {v: set(adj[v]) for v in core}
hair_h, hair_f = [], []
for s in S:
    h = ("h", s)
    f = ("f", s)
    G[h] = {s, f}
    G[f] = {h}
    G[s].add(h)
    hair_h.append(h)
    hair_f.append(f)

V = list(G)
n = len(V)
check("n = 54", n == 54, f"got {n}")
# symmetry + simplicity
assert all(u in G[w] for u in V for w in G[u]), "adjacency not symmetric"
assert all(u not in G[u] for u in V), "self loop"

# ---------------------------------------------------------------- C4-freeness (strong form)
viol = [(u, w) for u, w in itertools.combinations(V, 2) if len(G[u] & G[w]) >= 2]
check("C4-free (no two vertices share >=2 common neighbours)", not viol,
      f"{len(viol)} violating pairs")

# connectivity
def bfs(src):
    dist = {src: 0}
    q = deque([src])
    while q:
        x = q.popleft()
        for y in G[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist

D = {v: bfs(v) for v in V}
check("connected", all(len(D[v]) == n for v in V))

# ---------------------------------------------------------------- a-values
def independence_number(verts):
    """Exact independence number of G[verts] (verts are small: <=6)."""
    vs = list(verts)
    best = 0
    for k in range(len(vs), 0, -1):
        if k <= best:
            break
        for sub in itertools.combinations(vs, k):
            if all(y not in G[x] for x, y in itertools.combinations(sub, 2)):
                best = max(best, k)
                break
        if best == k:
            break
    return best

a = {v: independence_number(G[v]) for v in V}
# cross-check against F1 (a = d - t) since the graph should be C4-free
tri = {v: sum(1 for x, y in itertools.combinations(G[v], 2) if y in G[x]) for v in V}
check("F1 identity a(v) = d(v) - t(v) holds vertexwise",
      all(a[v] == len(G[v]) - tri[v] for v in V))
check("graph is triangle-free", all(tri[v] == 0 for v in V))

sa = sum(a.values())
check("Sum a(v) = 234", sa == 234, f"got {sa}")
check("l(G) = 13/3 > 4", sa * 3 == 13 * n and sa > 4 * n, f"l = {sa}/{n}")
from collections import Counter
avec = Counter(a.values())
check("a-profile {6:6, 5:36, 2:6, 1:6}", dict(avec) == {6: 6, 5: 36, 2: 6, 1: 6},
      str(dict(avec)))

# ---------------------------------------------------------------- rad / diam
ecc = {v: max(D[v].values()) for v in V}
rad = min(ecc.values())
diam = max(ecc.values())
check("rad(G) = 5", rad == 5, f"got {rad}")
check("diam(G) = 7", diam == 7, f"got {diam}")

# ---------------------------------------------------------------- (FAR-2) test
# A geodesic u0..ud with d >= rad.  Condition (i): some x in N(u0) OUTSIDE u1's
# component of G[N(u0)] with a(x) >= 4.  Condition (ii): a(ud) >= 2.
# The condition depends only on (u0, u1, ud), so enumerate those.
def comp_of(u0, u1):
    """u1's component of G[N(u0)] (matching-plus-isolates, but computed generally)."""
    nb = G[u0]
    seen, q = {u1}, deque([u1])
    while q:
        x = q.popleft()
        for y in nb:
            if y not in seen and y in G[x]:
                seen.add(y)
                q.append(y)
    return seen

def has_far2(u0, u1, ud):
    comp = comp_of(u0, u1)
    return (a[ud] >= 2) and any(a[x] >= 4 for x in G[u0] - comp)

far2_hits = []
capbreak_geodesics = []   # (u0,u1,ud,d) that satisfy (i) — cap-break at u0
for u in V:
    for w in V:
        if u == w:
            continue
        d = D[u][w]
        if d < rad:
            continue
        for u1 in G[u]:
            if D[u1][w] != d - 1:
                continue          # u1 not on any u->w geodesic
            comp = comp_of(u, u1)
            if any(a[x] >= 4 for x in G[u] - comp):
                capbreak_geodesics.append((u, u1, w, d))
                if a[w] >= 2:
                    far2_hits.append((u, u1, w, d))

check("NO geodesic of length >= rad satisfies (FAR-2)", not far2_hits,
      f"{len(far2_hits)} hits" if far2_hits else "0 hits")
check("the cap-break configuration is NON-VACUOUS (F4 executes)",
      len(capbreak_geodesics) > 0, f"{len(capbreak_geodesics)} cap-break (u0,u1,ud) frames")
lens = sorted(set(t[3] for t in capbreak_geodesics))
check("every non-3-capped geodesic of length >= rad has length EXACTLY rad (F12 demand)",
      lens == [rad], f"cap-break lengths {lens}")
farend_a = sorted(set(a[t[2]] for t in capbreak_geodesics))
check("every cap-break geodesic has an a=1 vertex at its far end",
      farend_a == [1], f"far-end a-values {farend_a}")

# ---------------------------------------------------------------- peeling (route A1)
Gp = {v: set(G[v]) for v in V}
ap = dict(a)
peeled = 0
while True:
    victims = [v for v in Gp if ap[v] == 1]
    if not victims:
        break
    v = victims[0]
    for w in Gp[v]:
        Gp[w].discard(v)
    del Gp[v]
    peeled += 1
    # recompute a on the peeled graph
    ap = {}
    for u in Gp:
        vs = list(Gp[u])
        best = 0
        for k in range(len(vs), 0, -1):
            if k <= best:
                break
            for sub in itertools.combinations(vs, k):
                if all(y not in Gp[x] for x, y in itertools.combinations(sub, 2)):
                    best = k
                    break
            if best == k:
                break
        ap[u] = best

check("peeling removed exactly the 12 hair vertices", peeled == 12, f"peeled {peeled}")
check("peeled graph is exactly the PG(2,4) incidence graph",
      set(Gp) == set(core) and all(Gp[v] == adj[v] for v in core))

def bfs2(g, src):
    dist = {src: 0}
    q = deque([src])
    while q:
        x = q.popleft()
        for y in g[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist

eccp = {v: max(bfs2(Gp, v).values()) for v in Gp}
radp, diamp = min(eccp.values()), max(eccp.values())
check("peeled radius = 3 (A1 REFUTED: 5 -> 3)", radp == 3, f"rad' = {radp}")
sap = sum(ap.values())
check("peeled graph still has l > 4", sap > 4 * len(Gp), f"l' = {sap}/{len(Gp)}")

# ---------------------------------------------------------------- induced 9-path claim
named = {
    "P0": ("P", (1, 0, 0)),
    "L1": ("L", (0, 1, 0)),
    "P1": ("P", (0, 0, 1)),
    "L2": ("L", (1, 1, 0)),
    "P2": ("P", (1, 1, 0)),
    "L3": ("L", (1, 1, 1)),
    "P3": ("P", (0, 1, 1)),
    "L4": ("L", (2, 1, 1)),     # [alpha:1:1]
    "P4": ("P", (1, 2, 0)),     # [1:alpha:0]
}
seq = ["P0", "L1", "P1", "L2", "P2", "L3", "P3", "L4", "P4"]
# the model writes projective triples in whatever scaling it likes (e.g. L4 = [a:1:1]);
# map each to OUR canonical representative before looking it up.
named = {k: (kind, normalize(t)) for k, (kind, t) in named.items()}
pv = [named[k] for k in seq]
check("the 9 named vertices are distinct core vertices",
      len(set(pv)) == 9 and all(v in G for v in pv))
cons = all(pv[i + 1] in G[pv[i]] for i in range(8))
chords = [(seq[i], seq[j]) for i in range(9) for j in range(i + 2, 9) if pv[j] in G[pv[i]]]
check("the 9 named vertices form an INDUCED path (consecutive adjacent, no chords)",
      cons and not chords, f"cons={cons} chords={chords}")
check("path(G) >= 9 = rad(G)+4, so Problem A is NOT refuted by this graph",
      cons and not chords and 9 == rad + 4)

# independent longest-induced-path lower bound inside the whole graph (DFS, capped)
best_len = [0]
def extend(path, pathset, forbidden):
    if len(path) > best_len[0]:
        best_len[0] = len(path)
    if len(path) >= 14:
        return
    last = path[-1]
    for y in G[last]:
        if y in pathset or y in forbidden:
            continue
        # y must not be adjacent to any path vertex except last
        if any(z in G[y] for z in path[:-1]):
            continue
        path.append(y); pathset.add(y)
        extend(path, pathset, forbidden)
        path.pop(); pathset.discard(y)

import sys as _s
_s.setrecursionlimit(10000)
for start in V:
    extend([start], {start}, set())
    if best_len[0] >= 14:
        break
check("independent search confirms an induced path on >= 9 vertices",
      best_len[0] >= 9, f"longest induced path found (search capped at 14): {best_len[0]}")

# ---------------------------------------------------------------- verdict
print()
print(f"vertices {n}, edges {sum(len(G[v]) for v in V)//2}, "
      f"Sum a = {sa}, l = {sa}/{n}, rad = {rad}, diam = {diam}, "
      f"rad(peeled) = {radp}, induced path >= {best_len[0]}")
print(f"FAILURES: {len(FAIL)}" + (f"  -> {FAIL}" if FAIL else ""))
sys.exit(1 if FAIL else 0)
