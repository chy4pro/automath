#!/usr/bin/env python3
"""w133_r20_briefcheck.py — owner-w133 round 20.

Re-derives EVERY factual claim the round-20 P7G32 brief makes about a control graph,
from printed edge lists only, BEFORE the brief is written.  Round 19 clause B6 makes an
argument resting on a false stated fact refusable; the standard has to bind the brief's
author too.  Round 12's P7G32 VOID was a fabricated path(Petersen); this round DISCLOSES
path(Q) and path(Petersen), so those two numbers must be right.

Also independently recomputes the held-out key rows V1-V9 on N1/N2 from their edge lists,
sharing no code with w133_r19_p7g32_key.py.

Self-limit 180s, exit(2) on overrun.  No SAT, no large exhaustive search: longest induced
path by DFS on <=12 vertices; on the 26-vertex PG(2,3) graph only EXISTENCE of an induced
P7 is asked, with early exit.
"""
import sys, time, itertools
from fractions import Fraction

T0 = time.time()
LIMIT = 180.0
FAILS = []
NCHK = [0]


def budget():
    if time.time() - T0 > LIMIT:
        print("WALL-CLOCK SELF-LIMIT EXCEEDED")
        sys.exit(2)


def check(label, cond, extra=""):
    NCHK[0] += 1
    budget()
    if cond:
        print(f"  PASS  {label}" + (f"   [{extra}]" if extra else ""))
    else:
        print(f"  FAIL  {label}" + (f"   [{extra}]" if extra else ""))
        FAILS.append(label)


# ---------- graph primitives (adjacency sets; independent of the r19 key script) ----------
def mk(n, edges):
    adj = {v: set() for v in range(n)}
    for a, b in edges:
        assert a != b
        adj[a].add(b)
        adj[b].add(a)
    return adj


def connected(adj):
    n = len(adj)
    seen = {0}
    st = [0]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                st.append(w)
    return len(seen) == n


def c4free(adj):
    """no two distinct vertices share >=2 common neighbours"""
    vs = sorted(adj)
    for u, v in itertools.combinations(vs, 2):
        if len(adj[u] & adj[v]) >= 2:
            return False, (u, v, sorted(adj[u] & adj[v]))
    return True, None


def alpha(adj, S):
    """independence number of the induced subgraph on S (S is small: a neighbourhood)"""
    S = list(S)
    best = 0
    for k in range(len(S), -1, -1):
        if k <= best:
            break
        for T in itertools.combinations(S, k):
            budget()
            ok = True
            for a, b in itertools.combinations(T, 2):
                if b in adj[a]:
                    ok = False
                    break
            if ok:
                best = max(best, k)
                break
    return best


def avec(adj):
    return tuple(alpha(adj, adj[v]) for v in sorted(adj))


def tri(adj, v):
    return sum(1 for a, b in itertools.combinations(sorted(adj[v]), 2) if b in adj[a])


def bfs(adj, s):
    d = {s: 0}
    q = [s]
    while q:
        nq = []
        for v in q:
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    nq.append(w)
        q = nq
    return d


def ecc_vec(adj):
    return tuple(max(bfs(adj, v).values()) for v in sorted(adj))


def induced_path_longest(adj):
    """longest induced path, vertices counted; DFS with pruning.  <=13 vertices only."""
    n = len(adj)
    best = [0, None]

    def ext(path, pset):
        budget()
        if len(path) > best[0]:
            best[0] = len(path)
            best[1] = list(path)
        last = path[-1]
        for w in sorted(adj[last]):
            if w in pset:
                continue
            # w must have exactly one neighbour in the path (namely last)
            if len(adj[w] & pset) != 1:
                continue
            path.append(w)
            pset.add(w)
            ext(path, pset)
            path.pop()
            pset.discard(w)

    for s in sorted(adj):
        ext([s], {s})
    return best[0], best[1]


def has_induced_path_atleast(adj, k):
    """existence only, early exit — for the 26-vertex control"""
    found = [None]

    def ext(path, pset):
        budget()
        if found[0]:
            return
        if len(path) >= k:
            found[0] = list(path)
            return
        for w in sorted(adj[path[-1]]):
            if w in pset:
                continue
            if len(adj[w] & pset) != 1:
                continue
            path.append(w)
            pset.add(w)
            ext(path, pset)
            path.pop()
            pset.discard(w)
            if found[0]:
                return

    for s in sorted(adj):
        ext([s], {s})
        if found[0]:
            break
    return found[0]


def induced_c6s(adj):
    """all induced 6-cycles, as canonical vertex frozensets, plus one cyclic order each"""
    out = {}
    for S in itertools.combinations(sorted(adj), 6):
        budget()
        Sset = set(S)
        if any(len(adj[v] & Sset) != 2 for v in S):
            continue
        # degree-2 everywhere inside + connected => a 6-cycle
        start = S[0]
        order = [start, sorted(adj[start] & Sset)[0]]
        while len(order) < 6:
            nxt = [x for x in adj[order[-1]] & Sset if x != order[-2]]
            if len(nxt) != 1:
                break
            order.append(nxt[0])
        if len(order) == 6 and order[0] in adj[order[-1]] and len(set(order)) == 6:
            out[frozenset(S)] = order
    return out


def trace_class(order, w, adj):
    hit = [i for i, z in enumerate(order) if w in adj[z]]
    if len(hit) == 0:
        return "none", hit
    if len(hit) == 1:
        return "one", hit
    if len(hit) == 2:
        d = (hit[1] - hit[0]) % 6
        d = min(d, 6 - d)
        return {1: "consecutive", 2: "distance-2", 3: "antipodal"}[d], hit
    return f"{len(hit)}-fold", hit


print("=" * 78)
print("[A] CONTROL 1 — Q  (= CE-2), n=10; every value the brief prints")
print("=" * 78)
Q_E = [(0, 1), (0, 4), (0, 5), (0, 8), (1, 2), (2, 3), (2, 6), (3, 5),
       (3, 7), (3, 9), (4, 6), (4, 7), (4, 8), (8, 9)]
Q = mk(10, Q_E)
ok, wit = c4free(Q)
check("Q is C4-free", ok, str(wit))
check("Q is connected", connected(Q))
qa = avec(Q)
qsum = sum(qa)
ql = Fraction(qsum, 10)
print(f"  a-vector(Q) = {qa}   sum = {qsum}   l(Q) = {ql} = {float(ql)}")
check("Q a-vector sum is 25 (matches r19 briefcheck for CE-2)", qsum == 25, f"sum={qsum}")
check("l(Q) = 5/2 exactly", ql == Fraction(5, 2), str(ql))
qp, qpw = induced_path_longest(Q)
print(f"  path(Q) = {qp}   witness {qpw}")
check("path(Q) = 6, so Q HAS NO INDUCED P7 and is a positive instance", qp == 6, f"path={qp}")
qe = ecc_vec(Q)
print(f"  ecc-vector(Q) = {qe}   diam = {max(qe)}   rad = {min(qe)}")
check("diam(Q) = 3 (NOT 2 — the round-18 false fact, corrected)", max(qe) == 3, str(qe))
qc6 = induced_c6s(Q)
print(f"  induced C6 count in Q = {len(qc6)}")
check("Q contains at least one induced C6", len(qc6) >= 1, f"count={len(qc6)}")
# pick a canonical C6 to print, the lexicographically smallest vertex set
Zset = sorted(qc6, key=lambda s: sorted(s))[0]
Zord = qc6[Zset]
print(f"  chosen induced C6 Z = {Zord} (cyclic)")
traces = {}
for w in sorted(Q):
    if w in Zset:
        continue
    cl, hit = trace_class(Zord, w, Q)
    traces[w] = (cl, [Zord[i] for i in hit])
    print(f"    w={w}: Z-neighbours {[Zord[i] for i in hit]}  -> {cl}")
Wset = [w for w in traces if traces[w][0] == "consecutive"]
print(f"  W (exactly two CONSECUTIVE Z-neighbours) = {Wset}")
check("Q carries at least one W-vertex, so 'W is empty' is FALSE under no-P7",
      len(Wset) >= 1, f"W={Wset}")
check("no vertex of Q has two Z-neighbours at cycle-distance 2 (F2/G15(b))",
      not any(v[0] == "distance-2" for v in traces.values()))
deg1a = [v for v in sorted(Q) if qa[v] == 1]
print(f"  vertices of Q with a(v)=1 (peelable) = {deg1a}")

print()
print("=" * 78)
print("[B] CONTROL 2 — PETERSEN, built as the Kneser graph K(5,2)")
print("=" * 78)
subs = [frozenset(s) for s in itertools.combinations(range(1, 6), 2)]
lab = {s: i for i, s in enumerate(subs)}
P_E = [(lab[a], lab[b]) for a, b in itertools.combinations(subs, 2) if not (a & b)]
P = mk(10, P_E)
print("  labelling: " + ", ".join(f"{lab[s]}={sorted(s)}" for s in subs))
print("  Petersen edges: " + ", ".join(f"{a}-{b}" for a, b in sorted(P_E)))
ok, wit = c4free(P)
check("Petersen is C4-free", ok, str(wit))
check("Petersen is 3-regular", all(len(P[v]) == 3 for v in P))
check("Petersen is triangle-free", all(tri(P, v) == 0 for v in P))
pa = avec(P)
psum = sum(pa)
pl = Fraction(psum, 10)
print(f"  a-vector(Petersen) = {pa}   sum = {psum}   l = {pl}")
check("l(Petersen) = 3 exactly (the tightness control for l <= 3)", pl == Fraction(3, 1), str(pl))
pp, ppw = induced_path_longest(P)
print(f"  path(Petersen) = {pp}   witness {ppw}")
check("path(Petersen) = 5 — NOT 6; this is the value round 12's return FABRICATED",
      pp == 5, f"path={pp}")
pc6 = induced_c6s(P)
print(f"  induced C6 count in Petersen = {len(pc6)}")
check("Petersen contains an induced C6", len(pc6) >= 1, f"count={len(pc6)}")
Pz = pc6[sorted(pc6, key=lambda s: sorted(s))[0]]
print(f"  one induced C6 of Petersen = {Pz} (cyclic)")
pe = ecc_vec(P)
check("diam(Petersen) = 2", max(pe) == 2, str(pe))

print()
print("=" * 78)
print("[C] CONTROL 3 — PG(2,3) incidence graph: must NOT execute (fails no-P7)")
print("=" * 78)
# PG(2,3): points = 13 nonzero vectors over GF(3) up to scaling; lines likewise; incidence = dot 0
pts = []
for a in range(3):
    for b in range(3):
        for c in range(3):
            v = (a, b, c)
            if v == (0, 0, 0):
                continue
            # canonical rep: first nonzero coordinate = 1
            fnz = next(i for i in range(3) if v[i])
            if v[fnz] != 1:
                continue
            pts.append(v)
check("PG(2,3) has 13 points", len(pts) == 13, str(len(pts)))
G3_E = []
for i, p in enumerate(pts):
    for j, L in enumerate(pts):
        if sum(p[k] * L[k] for k in range(3)) % 3 == 0:
            G3_E.append((i, 13 + j))
G3 = mk(26, G3_E)
ok, wit = c4free(G3)
check("PG(2,3) incidence graph is C4-free", ok, str(wit))
check("PG(2,3) incidence graph is 4-regular", all(len(G3[v]) == 4 for v in G3))
w7 = has_induced_path_atleast(G3, 7)
print(f"  induced P7 witness in PG(2,3): {w7}")
check("PG(2,3) HAS an induced P7, so 'no induced P7' is the FIRST hypothesis it fails",
      w7 is not None)
g3c6 = 1 if has_induced_path_atleast(G3, 3) else 0  # cheap sanity only
check("PG(2,3) is connected", connected(G3))

print()
print("=" * 78)
print("[D] HELD-OUT KEY V1-V9 — independently recomputed from the printed edge lists")
print("=" * 78)
N1_E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (3, 6), (1, 7),
        (4, 7), (2, 8), (5, 8), (6, 9), (7, 9), (8, 10), (9, 10), (6, 10)]
N2_E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (1, 7), (4, 8),
        (5, 9), (2, 9), (6, 10), (7, 10), (8, 11), (9, 11), (10, 11)]
N1 = mk(11, N1_E)
N2 = mk(12, N2_E)
ok1, w1 = c4free(N1)
ok2, w2 = c4free(N2)
check("V1  N1 is C4-free = YES", ok1, str(w1))
check("     N2 is C4-free", ok2, str(w2))
n1a = avec(N1)
check("V2  a(6) on N1 = 3", n1a[6] == 3, f"a(6)={n1a[6]}")
Zn = [0, 1, 2, 3, 4, 5]
isc6 = all(len(N1[v] & set(Zn)) == 2 for v in Zn)
check("V3  {0..5} induces a 6-cycle in N1 = YES", isc6)
d68 = bfs(N1, 6)[8]
check("V4  dist(6,8) on N1 = 2", d68 == 2, f"dist={d68}")
n9 = len(N1[9] & set(Zn))
check("V5  |N(9) cap {0..5}| on N1 = 0", n9 == 0, f"={n9}")
p1, p1w = induced_path_longest(N1)
check("V6  path(N1) = 7", p1 == 7, f"path={p1} witness {p1w}")
check("V7  sum_v a(v) on N1 = 31", sum(n1a) == 31, f"a={n1a} sum={sum(n1a)}")
p2, p2w = induced_path_longest(N2)
check("V8  path(N2) = 9", p2 == 9, f"path={p2} witness {p2w}")
c2 = len(induced_c6s(N2))
check("V9  induced C6 count in N2 = 4", c2 == 4, f"count={c2}")
check("N1 has path > 6, so N1 is OUTSIDE the target class — test graph only", p1 > 6)
check("N2 has path > 6, so N2 is OUTSIDE the target class — test graph only", p2 > 6)
check("neither N1 nor N2 equals Q or Petersen (the two BURNED graphs)",
      len(N1) != 10 and len(N2) != 10)

print()
print("=" * 78)
print("[E] V7 PROBES — the checkers must be refutable")
print("=" * 78)
Qbad = mk(10, Q_E + [(1, 4)])   # 1 and 4 now share common nbrs 0 and 2 -> a C4
ok, wit = c4free(Qbad)
check("V7-1 c4free() trips when edge 1-4 is planted into Q", not ok, str(wit))
Pbad = mk(10, P_E[:-1])
check("V7-2 the 3-regularity test trips on a Petersen with one edge removed",
      not all(len(Pbad[v]) == 3 for v in Pbad))
star = mk(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
sp, _ = induced_path_longest(star)
check("V7-3 induced_path_longest returns 3 on a star K1,4 (specificity: must NOT be 5)",
      sp == 3, f"path={sp}")
p6 = mk(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])
check("V7-4 has_induced_path_atleast(P6, 7) correctly finds NOTHING",
      has_induced_path_atleast(p6, 7) is None)
c6g = mk(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
check("V7-5 induced_c6s finds exactly 1 induced C6 in a bare C6", len(induced_c6s(c6g)) == 1)
c6chord = mk(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3)])
check("V7-6 induced_c6s finds 0 induced C6 once a long chord is planted",
      len(induced_c6s(c6chord)) == 0)

print()
print(f"CHECKS: {NCHK[0]}")
print(f"FAILURES: {len(FAILS)}")
for f in FAILS:
    print("   - " + f)
print(f"elapsed {time.time() - T0:.1f}s")
sys.exit(1 if FAILS else 0)
