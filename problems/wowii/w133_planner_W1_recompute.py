# Planner independent re-derivation for the w133 PROVED-S3 certification.
# W1 = two disjoint copies of the PG(2,5) point-line incidence graph, bridged by an
# internal path of L vertices.  Rebuild PG(2,5) from GF(5) first; trust nothing printed.
from fractions import Fraction as F
from itertools import combinations

q = 5
# points of PG(2,q) = 1-dim subspaces of GF(q)^3, normalised representatives
def norm(v):
    for c in v:
        if c % q:
            inv = pow(c, q - 2, q)
            return tuple((x * inv) % q for x in v)
    return None
pts = sorted({norm(v) for v in ((a, b, c) for a in range(q) for b in range(q) for c in range(q)) if norm(v)})
lines = pts[:]                      # self-dual: lines indexed by their coefficient vector
inc = lambda p, l: sum(p[i] * l[i] for i in range(3)) % q == 0

assert len(pts) == q*q + q + 1 == 31, len(pts)

# incidence graph: 31 + 31 = 62 vertices
V = [('P', p) for p in pts] + [('L', l) for l in lines]
adj = {v: set() for v in V}
for p in pts:
    for l in lines:
        if inc(p, l):
            adj[('P', p)].add(('L', l)); adj[('L', l)].add(('P', p))

deg = {v: len(adj[v]) for v in V}
assert set(deg.values()) == {q + 1} == {6}, sorted(set(deg.values()))
assert len(V) == 62

def c4_free(adjmap):
    vs = list(adjmap)
    for a, b in combinations(vs, 2):
        if len(adjmap[a] & adjmap[b]) >= 2:
            return False
    return True
def triangles(adjmap, v):
    return sum(1 for a, b in combinations(adjmap[v], 2) if b in adjmap[a])

assert c4_free(adj), "PG(2,5) incidence graph not C4-free"
assert all(triangles(adj, v) == 0 for v in V), "not triangle-free"
print(f"PG(2,5) incidence: n=62, {q+1}-regular, C4-free OK, triangle-free OK")

def build_W1(L):
    """two copies + a bridging path of L internal vertices"""
    A = {(0, v): {(0, w) for w in adj[v]} for v in V}
    B = {(1, v): {(1, w) for w in adj[v]} for v in V}
    G = {**A, **B}
    a0, b0 = (0, V[0]), (1, V[0])          # attachment vertices, one per copy
    path = [('m', i) for i in range(L)]
    for m in path: G[m] = set()
    chain = [a0] + path + [b0]
    for x, y in zip(chain, chain[1:]):
        G[x].add(y); G[y].add(x)
    return G

print()
print(" L |    n |  sum a |        l        | C4-free | a-profile check")
rows = {}
for L in [5, 8, 9, 10]:
    G = build_W1(L)
    n = len(G)
    a = {v: len(G[v]) - triangles(G, v) for v in G}      # a = d - t  (F1)
    s = sum(a.values())
    ok = c4_free(G)
    prof = {}
    for v in a: prof[a[v]] = prof.get(a[v], 0) + 1
    rows[L] = (n, s)
    print(f"{L:2d} | {n:4d} | {s:6d} | {str(F(s,n)):>15} | {ok!s:>7} | {dict(sorted(prof.items()))}")

print()
print("closed forms from the rebuild:  n = 124 + L ,  sum a = 746 + 2L")
for L in [5, 8, 9, 10]:
    n, s = rows[L]
    assert n == 124 + L and s == 746 + 2*L, (L, n, s)
print("  verified at L = 5, 8, 9, 10")

print()
print("=== the graded rows ===")
print(f"K1  L=9 : n={rows[9][0]}, sum={rows[9][1]}, l={F(*reversed((rows[9][0],rows[9][1])))} = {float(F(rows[9][1],rows[9][0])):.4f}")
print(f"K2  L=8 : n={rows[8][0]}, sum={rows[8][1]}, l={F(rows[8][1],rows[8][0])} = {float(F(rows[8][1],rows[8][0])):.4f}")
print(f"F5  L=5 : n={rows[5][0]}, sum={rows[5][1]}   <-- W1 as F5 states it")
print(f"    L=10: n={rows[10][0]}, sum={rows[10][1]}  <-- what 72k-10 / 394k-22 give at k=2")
print()
print("=== the B1 diagnosis: k-chain formula at k=2 ===")
print(f"  72*2-10  = {72*2-10}   vs  L=10 rebuild n   = {rows[10][0]}   match={72*2-10==rows[10][0]}")
print(f"  394*2-22 = {394*2-22}  vs  L=10 rebuild sum = {rows[10][1]}  match={394*2-22==rows[10][1]}")
print(f"  F5's W1 (L=5) = {rows[5]}  -> the formula is the L=10 chain, NOT F5's W1")
