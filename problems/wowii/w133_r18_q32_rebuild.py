#!/usr/bin/env python3
"""
w133 round 18 — DEBT-3: an INDEPENDENT rebuild of Q32-W.

Q32-W was single-sourced: only `problems/wowii/w133_r13_q32_verify.py` ever computed it,
and the paper had to disclose that (`rem:pocket2prov`). This file is the second source.

INDEPENDENCE IS THE WHOLE POINT, so nothing here is shared with the round-13 script:

  round 13 : PG(2,4) built from GF(4) ARITHMETIC — 2-bit polynomials mod a^2+a+1,
             projective triples normalised to leading 1, incidence by the dot product
             p . l = 0.
  here     : PG(2,4) built from a SINGER PLANAR DIFFERENCE SET — points are the residues
             mod 21, lines are the 21 translates D + i of D = {0,1,6,8,18}, incidence is
             p - i in D.  No field, no coordinates, no dot product, no shared code.

The difference-set property is VERIFIED, not assumed: the 20 nonzero differences of D
must be a permutation of the 20 nonzero residues mod 21. The plane axioms are then
verified again directly on the incidence relation.

The hairs: round 13 attaches 2-vertex pendant paths at the three points [1:0:0], [0:1:0],
[0:0:1] and the three lines with the same triples. That 6-set is a TRIANGLE: three
non-collinear points together with the three lines joining them in pairs, with
point_i on line_j iff i != j. Here the same combinatorial object is built from scratch —
three non-collinear residues and the three lines through them pairwise — and the
incidence pattern is ASSERTED to be exactly `i != j`. Since the collineation group of
PG(2,4) is transitive on triangles, the two hairy graphs are isomorphic, so every
quantity below is an isomorphism invariant and agreement is genuine two-sourcing rather
than a re-run.

HARD SELF-LIMIT: 300 s wall, enforced inside; exit(2) on overrun.
No SAT. The heaviest computation is 54 BFS runs on a 54-vertex 117-edge graph and a
depth-capped induced-path DFS under its own budget.
"""
import sys, time, itertools
from collections import deque, Counter
from fractions import Fraction

T0 = time.time(); BUDGET = 300.0
def tick(where):
    if time.time() - T0 > BUDGET:
        print(f"HARD TIMEOUT at {where}"); sys.exit(2)

FAIL = []
def check(name, cond, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + name + (f"   [{detail}]" if detail else ""))
    if not cond: FAIL.append(name)

# =============================================================== 1. the difference set
V21 = 21
D = (0, 1, 6, 8, 18)
diffs = Counter((x - y) % V21 for x in D for y in D if x != y)
check("D = {0,1,6,8,18} is a planar difference set mod 21 (every nonzero residue exactly once)",
      sorted(diffs) == list(range(1, V21)) and set(diffs.values()) == {1},
      f"{len(diffs)} distinct differences, multiplicities {sorted(set(diffs.values()))}")
check("k = 5, so the plane has order 4", len(D) == 5 and V21 == len(D)*len(D) - len(D) + 1,
      f"k={len(D)}, v={V21}")

# =============================================================== 2. PG(2,4) by translation
PTS  = [("pt", p) for p in range(V21)]
LNS  = [("ln", i) for i in range(V21)]
on   = lambda p, i: ((p - i) % V21) in D          # point p lies on line D+i

core = PTS + LNS
adj = {v: set() for v in core}
for p in range(V21):
    for i in range(V21):
        if on(p, i):
            adj[("pt", p)].add(("ln", i)); adj[("ln", i)].add(("pt", p))

check("core has 42 vertices", len(core) == 42, f"got {len(core)}")
degs = sorted({len(adj[v]) for v in core})
check("core is 5-regular", degs == [5], f"degree multiset {degs}")
bad = sum(1 for a_, b_ in itertools.combinations(PTS, 2) if len(adj[a_] & adj[b_]) != 1) \
    + sum(1 for a_, b_ in itertools.combinations(LNS, 2) if len(adj[a_] & adj[b_]) != 1)
check("plane axioms: any 2 points on exactly 1 line, any 2 lines meet in exactly 1 point",
      bad == 0, f"{bad} violations")

# =============================================================== 3. the triangle + hairs
def line_through(p, q):
    ls = [i for i in range(V21) if on(p, i) and on(q, i)]
    assert len(ls) == 1, (p, q, ls)
    return ls[0]

P1, P2, P3 = 0, 1, 2
collinear = any(on(P1, i) and on(P2, i) and on(P3, i) for i in range(V21))
check("the three chosen points are NON-COLLINEAR (they form a triangle)", not collinear,
      f"points {P1},{P2},{P3}")
L1, L2, L3 = line_through(P2, P3), line_through(P1, P3), line_through(P1, P2)
Ppts = [P1, P2, P3]; Llns = [L1, L2, L3]
check("the three joining lines are distinct and NON-CONCURRENT",
      len(set(Llns)) == 3 and not any(all(on(p, i) for i in Llns) for p in range(V21)),
      f"lines {Llns}")
pattern = [[on(Ppts[i], Llns[j]) for j in range(3)] for i in range(3)]
check("incidence pattern of the attachment 6-set is exactly `point_i on line_j iff i != j` "
      "(this is what makes it round 13's configuration)",
      all(pattern[i][j] == (i != j) for i in range(3) for j in range(3)), str(pattern))

S = [("pt", p) for p in Ppts] + [("ln", i) for i in Llns]
G = {v: set(adj[v]) for v in core}
hairs = []
for s in S:
    h, f = ("h", s), ("f", s)
    G[h] = {s, f}; G[f] = {h}; G[s].add(h)
    hairs += [h, f]
Vs = list(G); n = len(Vs)
check("n = 54", n == 54, f"got {n}")
assert all(u in G[w] for u in Vs for w in G[u]), "adjacency not symmetric"
assert all(u not in G[u] for u in Vs), "self loop"
check("12 hair vertices were attached", len(hairs) == 12, f"got {len(hairs)}")

# =============================================================== 4. basic structure
viol = [(u, w) for u, w in itertools.combinations(Vs, 2) if len(G[u] & G[w]) >= 2]
check("C4-free (strong form: no two vertices with >= 2 common neighbours)", not viol,
      f"{len(viol)} violating pairs, scan over {len(Vs)*(len(Vs)-1)//2} pairs")

def bfs(g, s):
    d = {s: 0}; q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if y not in d: d[y] = d[x]+1; q.append(y)
    return d
Dst = {v: bfs(G, v) for v in Vs}
check("connected", all(len(Dst[v]) == n for v in Vs), f"reach sizes {sorted({len(Dst[v]) for v in Vs})}")
E = sum(len(G[v]) for v in Vs)//2
check("edge count 117", E == 117, f"got {E}")

def alpha(g, verts):
    vs = list(verts); best = 0
    for k in range(len(vs), 0, -1):
        if k <= best: break
        for sub in itertools.combinations(vs, k):
            if all(y not in g[x] for x, y in itertools.combinations(sub, 2)):
                best = k; break
        if best == k: break
    return best
a = {v: alpha(G, G[v]) for v in Vs}
tri = {v: sum(1 for x, y in itertools.combinations(G[v], 2) if y in G[x]) for v in Vs}
check("triangle-free (scan over all neighbourhood pairs)", all(t == 0 for t in tri.values()),
      f"total triangle incidences {sum(tri.values())}")
check("F1 identity a(v) = d(v) - t(v) holds vertexwise, computed by two different routes",
      all(a[v] == len(G[v]) - tri[v] for v in Vs))
sa = sum(a.values())
check("Sum a(v) = 234", sa == 234, f"got {sa}")
check("l(G) = 13/3", Fraction(sa, n) == Fraction(13, 3), f"l = {Fraction(sa,n)}")
prof = dict(Counter(a.values()))
check("a-profile {6:6, 5:36, 2:6, 1:6}", prof == {6: 6, 5: 36, 2: 6, 1: 6}, str(prof))

ecc = {v: max(Dst[v].values()) for v in Vs}
rad, diam = min(ecc.values()), max(ecc.values())
check("rad = 5", rad == 5, f"got {rad}")
check("diam = 7", diam == 7, f"got {diam}")
check("ecc computed at ALL 54 vertices", len(ecc) == n, f"ecc multiset {sorted(Counter(ecc.values()).items())}")

# =============================================================== 5. (FAR-2) and cap-break
tick("FAR-2")
def comp_of(u0, u1):
    nb = G[u0]; seen, q = {u1}, deque([u1])
    while q:
        x = q.popleft()
        for y in nb:
            if y not in seen and y in G[x]: seen.add(y); q.append(y)
    return seen

far2_hits, capbreak = [], []
for u in Vs:
    for w in Vs:
        if u == w: continue
        d = Dst[u][w]
        if d < rad: continue
        for u1 in G[u]:
            if Dst[u1][w] != d - 1: continue
            comp = comp_of(u, u1)
            if any(a[x] >= 4 for x in G[u] - comp):
                capbreak.append((u, u1, w, d))
                if a[w] >= 2: far2_hits.append((u, u1, w, d))
check("NO geodesic of length >= rad satisfies (FAR-2)", not far2_hits, f"{len(far2_hits)} hits")
check("the cap-break configuration is NON-VACUOUS (the (FAR-2) verdict is over a NON-EMPTY scan)",
      len(capbreak) > 0, f"{len(capbreak)} cap-break (u0,u1,ud) frames")
check("cap-break frame count = 480", len(capbreak) == 480, f"got {len(capbreak)}")
lens = sorted({t[3] for t in capbreak})
check("every cap-break geodesic has length EXACTLY rad", lens == [rad], f"lengths {lens}")
fa = sorted({a[t[2]] for t in capbreak})
check("every cap-break geodesic has an a=1 vertex at its far end", fa == [1], f"far-end a-values {fa}")

# =============================================================== 6. peeling (route A1)
Gp = {v: set(G[v]) for v in Vs}
peeled = []
while True:
    ap = {u: alpha(Gp, Gp[u]) for u in Gp}
    vic = [v for v in Gp if ap[v] == 1]
    if not vic: break
    v = vic[0]
    for w in Gp[v]: Gp[w].discard(v)
    del Gp[v]; peeled.append(v)
ap = {u: alpha(Gp, Gp[u]) for u in Gp}
check("peeling removed exactly the 12 hair vertices, and nothing else",
      len(peeled) == 12 and set(peeled) == set(hairs), f"peeled {len(peeled)}")
check("the peeled graph is exactly the 42-vertex PG(2,4) incidence graph",
      set(Gp) == set(core) and all(Gp[v] == adj[v] for v in core))
eccp = {v: max(bfs(Gp, v).values()) for v in Gp}
check("peeled radius = 3 (route A1 is REFUTED: rad drops 5 -> 3)", min(eccp.values()) == 3,
      f"rad' = {min(eccp.values())}, diam' = {max(eccp.values())}")
sap = sum(ap.values())
check("peeled graph still has l > 4", Fraction(sap, len(Gp)) > 4, f"l' = {Fraction(sap,len(Gp))}")
check("peeled l = 5 exactly", Fraction(sap, len(Gp)) == 5, f"l' = {sap}/{len(Gp)}")

# =============================================================== 7. induced path >= rad + 4
tick("induced path")
PBUD = time.time() + 90.0
CAP = 12
best = [0, []]
def ext(path, pset):
    if len(path) > best[0]: best[0] = len(path); best[1] = list(path)
    if len(path) >= CAP or time.time() > PBUD: return
    for w in G[path[-1]]:
        if w in pset: continue
        if len(G[w] & pset) != 1: continue
        path.append(w); pset.add(w); ext(path, pset); path.pop(); pset.discard(w)
for s in Vs:
    if time.time() > PBUD: break
    ext([s], {s})
L, W = best
print(f"  longest induced path found (DFS capped at {CAP} vertices, 90 s budget): {L}")
check("path(G) >= rad + 4 = 9, so Problem A is NOT refuted by this graph", L >= rad + 4,
      f"found {L}")
# certify the witness from scratch, trusting nothing the builder did
consec = all(W[i+1] in G[W[i]] for i in range(len(W)-1))
chords = [(W[i], W[j]) for i in range(len(W)) for j in range(i+2, len(W)) if W[j] in G[W[i]]]
check("the exhibited path is certified INDUCED from scratch (consecutive adjacent, zero chords)",
      consec and not chords and len(set(W)) == len(W), f"len {len(W)}, {len(chords)} chords")

# =============================================================== 8. V7 falsifiability probes
tick("V7")
print("\n--- V7 probes: each injects a fault and REQUIRES the certifier above to trip ---")
# P1: the C4-freeness scan must be able to report a violation
Gx = {v: set(G[v]) for v in Vs}
p_, q_ = ("pt", P1), ("pt", P2)
common = next(iter(adj[p_] & adj[q_]))
extra = next(l for l in LNS if l not in adj[p_] and l != common)
Gx[p_].add(extra); Gx[extra].add(p_)
Gx[q_].add(extra); Gx[extra].add(q_)
viol_x = [(u, w) for u, w in itertools.combinations(Vs, 2) if len(Gx[u] & Gx[w]) >= 2]
check("P1  C4-free scan is LIVE (adding a second common line to two points trips it)",
      len(viol_x) > 0, f"{len(viol_x)} violating pairs after injection")
# P2: the chord certifier must be able to report chords
if len(W) >= 4:
    Gy = {v: set(G[v]) for v in Vs}
    Gy[W[0]].add(W[3]); Gy[W[3]].add(W[0])
    ch_y = [(W[i], W[j]) for i in range(len(W)) for j in range(i+2, len(W)) if W[j] in Gy[W[i]]]
    check("P2  induced-path chord certifier is LIVE (planting one chord trips it)",
          len(ch_y) > 0, f"{len(ch_y)} chords after injection")
# P3: the (FAR-2) verdict must be refutable — raise a far-end a-value and it must fire
hit_x = [t for t in capbreak if a[t[2]] >= 1]
check("P3  the (FAR-2) verdict is refutable, not vacuous: the same scan with the a(ud) >= 2 "
      "test relaxed to a(ud) >= 1 returns a NON-EMPTY hit set",
      len(hit_x) > 0, f"{len(hit_x)} hits under the relaxed test (vs 0 under the real one)")
# P4: the difference-set check must reject a non-difference-set
Dbad = (0, 1, 2, 8, 18)
db = Counter((x - y) % V21 for x in Dbad for y in Dbad if x != y)
check("P4  the difference-set certifier is LIVE (a non-difference-set is rejected)",
      not (sorted(db) == list(range(1, V21)) and set(db.values()) == {1}),
      f"multiplicities {sorted(set(db.values()))}")

print()
print(f"n = {n}, edges = {E}, Sum a = {sa}, l = {Fraction(sa,n)}, rad = {rad}, diam = {diam}, "
      f"rad(peeled) = {min(eccp.values())}, induced path >= {L}")
print(f"FAILURES: {len(FAIL)}" + ("" if not FAIL else "  -> " + "; ".join(FAIL)))
print(f"elapsed {time.time()-T0:.1f}s")
sys.exit(1 if FAIL else 0)
