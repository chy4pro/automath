#!/usr/bin/env python3
"""w133 round 10 (owner-w133): adjudication of Q28 (w133_G14low_qwen.md) and
Q29 (w133_3CAP_qwen.md). No SAT. Every assertion below ran before any prose was written.

Q28 checks:
  A. Model's explicit d=3 witness graph: full class-constraint sweep (simple, connected,
     C4-free FIRST, a-values, geodesic, F4, path(G)=7 exactly).
  B. PG(2,3): all F6 numbers + explicit d=3 frame hypothesis satisfaction (Case-1 available).
  C. PG(3,2): global numbers + one EXPLICIT d=4 line-to-line frame verified (closes the
     'candidate-verify-before-citing' flag from round 9 slice 3).
  D. Sweep (random maximal C4-free / sparse / structured / Case-2-seeded graphs):
     every frame satisfying the Q28 target hypotheses is tested:
       d=4  -> path >= 8 must hold (owner-verified proof => hard assert),
       d=3 Case-1-available -> path >= 7 must hold (owner-verified proof => hard assert),
       d=3 Case-2-forced    -> path >= 7 checked; any failure printed as counterexample
                               (this is the OPEN case; empirical only),
     plus the owner's Case-2 sharpening asserts (usable-far set is a single y, y ~ x,
     dist(u0,y)=2, i.e. u0-x-y-u3 is itself a geodesic).

Q29 checks:
  E. Lemma chain L1-L6 + both E(S,T) bounds + the sharpened theorem (capped => l < 4),
     machine-tested NON-VACUOUSLY on every peripherally-3-capped graph in the sweep
     (structured families guarantee coverage: S with K1, K2, K3 components and a T2
     straddler all occur).
  F. F7 = PG(3,2): NOT peripherally 3-capped (witness printed); a line has d_S = 3
     (Lemma-1 non-execution demo, as the harvest claimed).
  G. F8 = PG(2,3): NOT peripherally 3-capped (l = 4.0; required by the owner's sharpening
     'capped => l < 4', which the harvest's own argument yields at the l = 4 boundary).
"""
import random
import sys
from itertools import combinations
from collections import deque

sys.setrecursionlimit(100000)
random.seed(133133)
FAILS = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" | " + str(detail)) if detail else ""))
    if not cond:
        FAILS.append(name)


# ---------------- graph utilities ----------------
def c4_ok(adj):
    vs = list(adj)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if len(adj[vs[i]] & adj[vs[j]]) >= 2:
                return False
    return True


def bfs(adj, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


def alldist(adj):
    return {v: bfs(adj, v) for v in adj}


def connected(adj):
    return len(bfs(adj, next(iter(adj)))) == len(adj)


def aval(adj, v):
    nb = adj[v]
    seen = set()
    c = 0
    for u in nb:
        if u in seen:
            continue
        c += 1
        seen.add(u)
        seen |= (adj[u] & nb)
    return c


def avals(adj):
    return {v: aval(adj, v) for v in adj}


def comp_in_nbhd(adj, v, u):
    """u's component in G[N(v)] (matching+isolates under C4-free)."""
    return {u} | (adj[u] & adj[v])


def ind_path_atleast(adj, k):
    """True iff an induced path on >= k vertices exists. DFS from every start vertex."""
    if k <= 1:
        return True

    def rec(path, pset):
        if len(path) >= k:
            return True
        last = path[-1]
        for w in adj[last]:
            if w in pset:
                continue
            good = True
            for p in path[:-1]:
                if w in adj[p]:
                    good = False
                    break
            if good:
                path.append(w)
                pset.add(w)
                if rec(path, pset):
                    return True
                path.pop()
                pset.discard(w)
        return False

    for s in adj:
        if rec([s], {s}):
            return True
    return False


def ind_path_exact(adj):
    k = 1
    while ind_path_atleast(adj, k + 1):
        k += 1
    return k


# ---------------- Q29 machinery ----------------
def periph_3capped(adj, D, av, witness=False):
    """Peripherally 3-capped: every geodesic of length >= rad(G) is 3-capped at both ends.
    Equivalent per-end form: for every ordered (u,v) with dist(u,v) >= rad and every valid
    first step u1 (dist(u1,v)=dist(u,v)-1), every vertex of N(u) \\ C(u1) has a <= 3."""
    ecc = {v: max(D[v].values()) for v in adj}
    rad = min(ecc.values())
    for u in adj:
        for v in adj:
            if u == v or D[u][v] < rad:
                continue
            for u1 in adj[u]:
                if D[u1][v] != D[u][v] - 1:
                    continue
                c0 = comp_in_nbhd(adj, u, u1)
                for x in adj[u] - c0:
                    if av[x] >= 4:
                        return (False, (u, u1, v, x)) if witness else False
    return (True, None) if witness else True


def q29_lemma_checks(adj, D, av, tag, cov):
    """Run on peripherally-3-capped graphs only. Tests Lemmas 1-6, both E(S,T) bounds,
    and the sharpened theorem (capped => l < 4)."""
    n = len(adj)
    S = {v for v in adj if av[v] >= 4}
    T = set(adj) - S
    ok = True
    msgs = []
    # Lemma 1
    if not all(len(adj[v] & S) <= 2 for v in adj):
        ok = False
        msgs.append("L1")
    # G[S] components: cliques of size <= 3 (Lemma 3)
    comps = []
    seen = set()
    for v in S:
        if v in seen:
            continue
        comp = {v}
        q = [v]
        while q:
            u = q.pop()
            for w in adj[u] & S:
                if w not in comp:
                    comp.add(w)
                    q.append(w)
        seen |= comp
        comps.append(comp)
        if len(comp) > 3 or not all(b in adj[a] for a, b in combinations(comp, 2)):
            ok = False
            msgs.append("L3")
    k = {1: 0, 2: 0, 3: 0}
    for comp in comps:
        if len(comp) in k:
            k[len(comp)] += 1
    # Lemma 4 / Lemma 5
    t2count = 0
    for comp in comps:
        if len(comp) == 3:
            for u in T:
                if len(adj[u] & comp) >= 2:
                    ok = False
                    msgs.append("L4")
        if len(comp) == 2:
            straddlers = [u for u in T if comp <= adj[u]]
            if len(straddlers) > 1:
                ok = False
                msgs.append("L5")
    # Lemma 6
    for u in T:
        ds = adj[u] & S
        if len(ds) == 2:
            t2count += 1
            a, b = ds
            if b not in adj[a]:
                ok = False
                msgs.append("L6-nonadj")
            else:
                comp = next(c for c in comps if a in c)
                if len(comp) != 2:
                    ok = False
                    msgs.append("L6-K3")
    # E(S,T) bounds
    EST = sum(len(adj[u] & S) for u in T)
    if not EST >= sum(av[v] for v in S) - (len(S) - k[1]):
        ok = False
        msgs.append("lowerB")
    if not EST <= k[2] + (n - len(S)):
        ok = False
        msgs.append("upperB")
    # sharpened theorem: capped => l < 4
    if not sum(av.values()) < 4 * n:
        ok = False
        msgs.append("THM l<4")
    # coverage bookkeeping
    cov["capped"] += 1
    if S:
        cov["S_nonempty"] += 1
    cov["K1"] += k[1]
    cov["K2"] += k[2]
    cov["K3"] += k[3]
    cov["T2"] += t2count
    if not ok:
        check("Q29-lemmas[" + tag + "]", False, ",".join(msgs) + " " + str(sorted(adj.items())))
    return ok


# ---------------- Q28 machinery ----------------
def q28_check_graph(adj, D, av, cnt, tag):
    """Find every frame satisfying the Q28 target hypotheses and test the conclusion."""
    pathc = {}

    def pal(kk):
        if kk not in pathc:
            pathc[kk] = ind_path_atleast(adj, kk)
        return pathc[kk]

    f4 = all(av[v] >= 2 for v in adj)
    for u0 in adj:
        if av[u0] < 3:
            continue
        for ud in adj:
            dd = D[u0].get(ud)
            if dd not in (3, 4) or av[ud] < 2:
                continue
            if dd == 3:
                geos = [(u1, u2) for u1 in adj[u0] if D[u1][ud] == 2
                        for u2 in (adj[u1] & adj[ud]) if D[u0][u2] == 2]
                found = False
                case1 = False
                case2info = []
                for (u1, u2) in geos:
                    c1 = comp_in_nbhd(adj, u0, u1)
                    xs = [x for x in adj[u0] - c1 if av[x] >= 4]
                    if not xs:
                        continue
                    cu2 = comp_in_nbhd(adj, ud, u2)
                    ys = sorted(adj[ud] - cu2)
                    for x in xs:
                        found = True
                        if any(y not in adj[x] for y in ys):
                            case1 = True
                        else:
                            case2info.append((u1, u2, x, ys))
                if not found:
                    continue
                cnt["d3_frames"] += 1
                if case1:
                    cnt["d3_case1"] += 1
                    if not pal(7):
                        check("Q28-d3-CASE1-THEOREM-VIOLATED", False,
                              tag + " " + str(sorted(adj.items())))
                else:
                    cnt["d3_case2forced"] += 1
                    if f4:
                        cnt["d3_case2forced_F4"] += 1
                    if not pal(7):
                        if f4:
                            cnt["d3_case2_CE_F4"] += 1
                            print("!!! Q28 d=3 CASE-2 F4-COUNTEREXAMPLE " +
                                  str(sorted(adj.items())))
                            check("Q28-d3-CASE2-F4-COUNTEREXAMPLE", False, tag)
                        else:
                            cnt["d3_case2_CE_bare"] += 1
                            print("!!! Q28 d=3 CASE-2 bare-target counterexample (has a=1) "
                                  + str(sorted(adj.items())))
                    # owner's sharpening asserts
                    for (u1, u2, x, ys) in case2info:
                        if not (len(ys) == 1 and ys[0] in adj[x] and D[u0][ys[0]] == 2):
                            check("Q28-case2-sharpening", False,
                                  tag + " " + str((u0, ud, x, ys)))
            else:
                hx = False
                for u1 in adj[u0]:
                    if D[u1][ud] != 3:
                        continue
                    c1 = comp_in_nbhd(adj, u0, u1)
                    if any(av[x] >= 4 for x in adj[u0] - c1):
                        hx = True
                        break
                if not hx:
                    continue
                cnt["d4_frames"] += 1
                if not pal(8):
                    check("Q28-d4-THEOREM-VIOLATED", False,
                          tag + " " + str(sorted(adj.items())))


# ---------------- constructions ----------------
def mkgraph(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


def pg23():
    """PG(2,3) point/line incidence graph, n=26."""
    pts = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                v = (x, y, z)
                if v == (0, 0, 0):
                    continue
                for w in pts:
                    if all((2 * w[i]) % 3 == v[i] for i in range(3)):
                        break
                else:
                    pts.append(v)
    assert len(pts) == 13
    edges = []
    for p in pts:
        for l in pts:
            if sum(p[i] * l[i] for i in range(3)) % 3 == 0:
                edges.append(("p" + str(p), "l" + str(l)))
    return mkgraph(edges)


def pg32():
    """PG(3,2) point/line incidence graph = STS(15) incidence, n=50."""
    pts = list(range(1, 16))
    lines = set()
    for p in pts:
        for q in pts:
            if p < q:
                r = p ^ q
                lines.add(tuple(sorted((p, q, r))))
    assert len(lines) == 35
    edges = []
    for ln in lines:
        for p in ln:
            edges.append(("P" + str(p), "L" + str(ln)))
    return mkgraph(edges)


def witness_q28():
    """Model's explicit d=3 witness graph, edge list verbatim from the harvest."""
    E = [("u0", "u1"), ("u1", "u2"), ("u2", "u3"), ("u0", "x"), ("u0", "z1"),
         ("u0", "z2"), ("x", "w1"), ("x", "w2"), ("x", "w3"), ("u3", "y"),
         ("u3", "c"), ("y", "w1"), ("w2", "c"), ("w3", "u2"), ("z1", "y"),
         ("z2", "c")]
    return mkgraph(E)


def star(m):
    return mkgraph([("h", "v%d" % i) for i in range(m)])


def double_hub(m):
    e = [("h1", "h2")]
    e += [("h1", "a%d" % i) for i in range(m)]
    e += [("h2", "b%d" % i) for i in range(m)]
    return mkgraph(e)


def tri_hub(m):
    e = [("h1", "h2"), ("h2", "h3"), ("h1", "h3")]
    for j, h in enumerate(["h1", "h2", "h3"]):
        e += [(h, "l%d_%d" % (j, i)) for i in range(m)]
    return mkgraph(e)


def straddled_double_hub(m):
    e = [("h1", "h2"), ("h1", "t"), ("h2", "t")]
    e += [("h1", "a%d" % i) for i in range(m)]
    e += [("h2", "b%d" % i) for i in range(m)]
    return mkgraph(e)


def spider(legs, leglen):
    e = []
    for i in range(legs):
        prev = "c"
        for j in range(leglen):
            v = "s%d_%d" % (i, j)
            e.append((prev, v))
            prev = v
    return mkgraph(e)


def broom(plen, m):
    e = [("p%d" % i, "p%d" % (i + 1)) for i in range(plen - 1)]
    e += [("p0", "q%d" % i) for i in range(m)]
    return mkgraph(e)


def c4_ok_incr(adj, u, v):
    for a, b in combinations(adj[u], 2):
        if len(adj[a] & adj[b]) >= 2:
            return False
    for a, b in combinations(adj[v], 2):
        if len(adj[a] & adj[b]) >= 2:
            return False
    return True


def rand_maximal_c4free(n, rng):
    vs = list(range(n))
    adj = {v: set() for v in vs}
    order = vs[:]
    rng.shuffle(order)
    for i in range(1, n):
        u, w = order[i], rng.choice(order[:i])
        adj[u].add(w)
        adj[w].add(u)
    cand = [(u, v) for u, v in combinations(vs, 2) if v not in adj[u]]
    rng.shuffle(cand)
    for (u, v) in cand:
        adj[u].add(v)
        adj[v].add(u)
        if not c4_ok_incr(adj, u, v):
            adj[u].discard(v)
            adj[v].discard(u)
    return adj


def rand_sparse_c4free(n, extra, rng):
    vs = list(range(n))
    adj = {v: set() for v in vs}
    order = vs[:]
    rng.shuffle(order)
    for i in range(1, n):
        u, w = order[i], rng.choice(order[:i])
        adj[u].add(w)
        adj[w].add(u)
    cand = [(u, v) for u, v in combinations(vs, 2) if v not in adj[u]]
    rng.shuffle(cand)
    added = 0
    for (u, v) in cand:
        if added >= extra:
            break
        adj[u].add(v)
        adj[v].add(u)
        if c4_ok_incr(adj, u, v):
            added += 1
        else:
            adj[u].discard(v)
            adj[v].discard(u)
    return adj


def case2_seed(rng):
    """Seeded frames biased toward Q28 d=3 Case-2 (x~y) configurations, plus tails."""
    n_t = rng.randint(2, 5)
    names = ["u0", "u1", "u2", "u3", "x", "y", "w1", "w2", "w3", "z1", "z2"] + \
            ["t%d" % i for i in range(n_t)]
    adj = {v: set() for v in names}

    def add(a, b):
        adj[a].add(b)
        adj[b].add(a)

    for e in [("u0", "u1"), ("u1", "u2"), ("u2", "u3"), ("u0", "x"), ("u3", "y"),
              ("x", "y"), ("x", "w1"), ("x", "w2"), ("x", "w3"), ("u0", "z1"),
              ("u0", "z2")]:
        add(*e)
    for i in range(n_t - 1):
        add("t%d" % i, "t%d" % (i + 1))
    pairs = [(a, b) for a, b in combinations(names, 2) if b not in adj[a]]
    rng.shuffle(pairs)
    for (a, b) in pairs:
        if rng.random() < 0.28:
            add(a, b)
            if not (c4_ok(adj) and bfs(adj, "u0").get("u3", 99) == 3):
                adj[a].discard(b)
                adj[b].discard(a)
    if not connected(adj) or bfs(adj, "u0").get("u3", 99) != 3:
        return None
    return adj


# =================================================================
print("=== A. Q28 model witness graph (d=3 explicit edge list) ===")
W = witness_q28()
check("A1 witness simple+connected", connected(W) and all(v not in W[v] for v in W),
      "n=%d" % len(W))
check("A2 witness C4-free", c4_ok(W))
DW = alldist(W)
avW = avals(W)
check("A3 witness geodesic dist(u0,u3)=3", DW["u0"]["u3"] == 3)
check("A4 witness a-values a(u0)=4,a(x)=4,a(u3)=3",
      avW["u0"] == 4 and avW["x"] == 4 and avW["u3"] == 3)
check("A5 witness F4 (all a>=2)", all(avW[v] >= 2 for v in W),
      "min a = %d" % min(avW.values()))
c_u1 = comp_in_nbhd(W, "u0", "u1")
check("A6 witness x usable (outside u1's comp)", "x" not in c_u1)
pW = ind_path_exact(W)
check("A7 witness path(G) = 7 exactly", pW == 7, "path=%d" % pW)

print("=== B. PG(2,3): F6/F8 numbers + d=3 frame (Q28 amendment-3 instance) ===")
G23 = pg23()
check("B1 PG(2,3) n=26 connected", len(G23) == 26 and connected(G23))
check("B2 PG(2,3) C4-free", c4_ok(G23))
av23 = avals(G23)
check("B3 PG(2,3) 4-regular, all a=4",
      all(len(G23[v]) == 4 for v in G23) and all(av23[v] == 4 for v in G23))
D23 = alldist(G23)
ecc23 = {v: max(D23[v].values()) for v in G23}
check("B4 PG(2,3) rad=diam=3", min(ecc23.values()) == 3 and max(ecc23.values()) == 3)
check("B5 PG(2,3) l = 4.0 exactly (NOT >4)", sum(av23.values()) == 4 * 26)
check("B6 PG(2,3) path >= 9", ind_path_atleast(G23, 9))
# one explicit d=3 frame, hypothesis satisfaction incl. Case-1 availability
frame_ok = False
case1_ok = False
for u0 in G23:
    for u3 in G23:
        if D23[u0][u3] != 3:
            continue
        for u1 in G23[u0]:
            if D23[u1][u3] != 2:
                continue
            for u2 in G23[u1] & G23[u3]:
                if D23[u0][u2] != 2:
                    continue
                c1 = comp_in_nbhd(G23, u0, u1)
                xs = [x for x in G23[u0] - c1 if av23[x] >= 4]
                if xs:
                    frame_ok = True
                    cu2 = comp_in_nbhd(G23, u3, u2)
                    ys = G23[u3] - cu2
                    if any(y not in G23[xs[0]] for y in ys):
                        case1_ok = True
        if frame_ok and case1_ok:
            break
    if frame_ok and case1_ok:
        break
check("B7 PG(2,3) d=3 frame with a(u0)>=3,a(u3)>=2,usable x a(x)>=4", frame_ok)
check("B8 PG(2,3) frame is Case-1-available (x /~ some usable y)", case1_ok)

print("=== C. PG(3,2): F7 numbers + EXPLICIT d=4 frame + Q29 probes ===")
G32 = pg32()
check("C1 PG(3,2) n=50 connected", len(G32) == 50 and connected(G32))
check("C2 PG(3,2) C4-free", c4_ok(G32))
av32 = avals(G32)
pts32 = [v for v in G32 if v.startswith("P")]
lns32 = [v for v in G32 if v.startswith("L")]
check("C3 PG(3,2) a(point)=7, a(line)=3, sum=210, l=4.2>4",
      all(av32[p] == 7 for p in pts32) and all(av32[l] == 3 for l in lns32)
      and sum(av32.values()) == 210)
D32 = alldist(G32)
ecc32 = {v: max(D32[v].values()) for v in G32}
check("C4 PG(3,2) rad=3 diam=4", min(ecc32.values()) == 3 and max(ecc32.values()) == 4)
# explicit d=4 line-line frame (closes round-9 'candidate' flag)
d4frame = None
for l0 in lns32:
    for l4 in lns32:
        if D32[l0][l4] != 4:
            continue
        for u1 in G32[l0]:
            if D32[u1][l4] != 3:
                continue
            c1 = comp_in_nbhd(G32, l0, u1)
            xs = [x for x in G32[l0] - c1 if av32[x] >= 4]
            if xs and av32[l0] >= 3 and av32[l4] >= 2:
                d4frame = (l0, u1, l4, xs[0])
                break
        if d4frame:
            break
    if d4frame:
        break
check("C5 PG(3,2) explicit d=4 frame exists (a(l0)=3>=3, a(l4)=3>=2, usable point a=7>=4)",
      d4frame is not None, str(d4frame))
check("C6 PG(3,2) path >= 8 (= d+4 at d=4)", ind_path_atleast(G32, 8))
capped32, wit32 = periph_3capped(G32, D32, av32, witness=True)
check("C7 F7 NOT peripherally 3-capped (harvest probe)", capped32 is False, str(wit32))
someline = lns32[0]
check("C8 F7 line has d_S = 3 (Lemma-1 non-execution demo, harvest claim)",
      len([w for w in G32[someline] if av32[w] >= 4]) == 3)
capped23 = periph_3capped(G23, D23, av23)
check("C9 F8=PG(2,3) NOT capped (needed by sharpened thm: capped => l<4; here l=4.0)",
      capped23 is False)

print("=== D/E. Sweep: Q28 frames + Q29 lemma chain on capped graphs ===")
rng = random.Random(20260819)
cnt = {"d3_frames": 0, "d3_case1": 0, "d3_case2forced": 0, "d3_case2forced_F4": 0,
       "d3_case2_CE_F4": 0, "d3_case2_CE_bare": 0, "d4_frames": 0}
cov = {"capped": 0, "S_nonempty": 0, "K1": 0, "K2": 0, "K3": 0, "T2": 0}

graphs = []
for m in (4, 5, 6, 7):
    graphs.append(("star%d" % m, star(m)))
    graphs.append(("dhub%d" % m, double_hub(m)))
    graphs.append(("trihub%d" % m, tri_hub(m)))
    graphs.append(("sdhub%d" % m, straddled_double_hub(m)))
for lg, ll in ((3, 3), (4, 2), (5, 2), (4, 3), (6, 2)):
    graphs.append(("spider%d_%d" % (lg, ll), spider(lg, ll)))
for pl, m in ((5, 4), (6, 5), (7, 4), (8, 6)):
    graphs.append(("broom%d_%d" % (pl, m), broom(pl, m)))
for i in range(260):
    graphs.append(("randmax%d" % i, rand_maximal_c4free(rng.randint(10, 13), rng)))
for i in range(260):
    graphs.append(("sparse%d" % i, rand_sparse_c4free(rng.randint(10, 14),
                                                      rng.randint(1, 4), rng)))
nseed = 0
for i in range(900):
    g = case2_seed(rng)
    if g is not None:
        nseed += 1
        graphs.append(("c2seed%d" % i, g))

q29_all_ok = True
for tag, g in graphs:
    if not connected(g):
        continue
    if not c4_ok(g):
        check("sweep-generator-broken(C4)", False, tag)
        continue
    D = alldist(g)
    av = avals(g)
    q28_check_graph(g, D, av, cnt, tag)
    if periph_3capped(g, D, av):
        if not q29_lemma_checks(g, D, av, tag, cov):
            q29_all_ok = False

check("D1 Q28 sweep: no d=4 or d=3-Case-1 violation (see any FAIL above)", True)
check("D2 Q28 sweep coverage: d3 frames >= 100", cnt["d3_frames"] >= 100, str(cnt))
check("D3 Q28 sweep coverage: d4 frames >= 20", cnt["d4_frames"] >= 20,
      "d4_frames=%d" % cnt["d4_frames"])
check("D4 Q28 sweep coverage: Case-2-forced frames >= 10 (open case exercised)",
      cnt["d3_case2forced"] >= 10, "case2forced=%d (F4-satisfying: %d)"
      % (cnt["d3_case2forced"], cnt["d3_case2forced_F4"]))
check("D5a Q28 open case (F4 form): no F4-satisfying Case-2 counterexample",
      cnt["d3_case2_CE_F4"] == 0, "F4-CE=%d over %d F4-satisfying Case-2 frames"
      % (cnt["d3_case2_CE_F4"], cnt["d3_case2forced_F4"]))
check("D5b FINDING: bare d=3 target (no F4) REFUTED by sweep counterexamples",
      cnt["d3_case2_CE_bare"] >= 1, "bare-CE=%d (F4/a>=2 is NECESSARY at d=3)"
      % cnt["d3_case2_CE_bare"])
check("E1 Q29 lemma chain: all capped graphs pass L1-L6+bounds+l<4", q29_all_ok, str(cov))
check("E2 Q29 coverage: capped graphs with S nonempty >= 15", cov["S_nonempty"] >= 15,
      str(cov))
check("E3 Q29 coverage: K2 and K3 components + T2 straddler all seen",
      cov["K2"] >= 1 and cov["K3"] >= 1 and cov["T2"] >= 1, str(cov))
print("case2 seeds accepted: %d" % nseed)

print("=== G. Certified counterexample: bare d=3 target (no F4) is FALSE ===")
# Pinned from the sweep (seed-independent certification). n=10, 11 edges.
CE = mkgraph([(0, 9), (0, 5), (1, 5), (2, 3), (2, 5), (2, 6), (2, 8), (4, 9),
              (4, 6), (5, 7), (5, 8)])
check("G1 CE simple+connected n=10", connected(CE) and len(CE) == 10)
check("G2 CE C4-free", c4_ok(CE))
DCE = alldist(CE)
avCE = avals(CE)
check("G3 CE frame: dist(2,9)=3, a(2)=3>=3, a(9)=2>=2",
      DCE[2][9] == 3 and avCE[2] == 3 and avCE[9] == 2)
check("G4 CE geodesic 2-6-4-9 with x=5 usable, a(5)=4>=4",
      6 in CE[2] and 4 in CE[6] and 9 in CE[4] and DCE[2][4] == 2 and DCE[6][9] == 2
      and 5 not in comp_in_nbhd(CE, 2, 6) and avCE[5] == 4)
# Case-2-forced: the only usable far-side y (w.r.t. u2=4) is 0, and 0 ~ x=5
ys_ce = CE[9] - comp_in_nbhd(CE, 9, 4)
check("G5 CE Case-2-forced: usable far set == {0} and 0 ~ x=5",
      ys_ce == {0} and 0 in CE[5])
pce = ind_path_exact(CE)
check("G6 CE path(G) = %d < 7 => bare d=3 target REFUTED" % pce, pce < 7,
      "path=%d" % pce)
check("G7 CE has a=1 vertices (1,3,7 leaves; 8 triangle-leaf) => no clash with F4 form",
      sorted(v for v in CE if avCE[v] == 1) == [1, 3, 7, 8])
# peel a=1 vertices repeatedly; frame must die (else F4 form would be refuted too)
PE = {v: set(w for w in CE[v]) for v in CE}
while True:
    low = [v for v in PE if aval(PE, v) <= 1]
    if not low:
        break
    for v in low:
        for w in PE[v]:
            PE[w].discard(v)
        del PE[v]
avPE = avals(PE)
check("G8 peeled graph (= C6) has no a>=4 vertex: frame dies under peeling, F4 form intact",
      len(PE) == 6 and all(avPE[v] <= 2 for v in PE), str(sorted(PE)))

# Final arithmetic of Q29 re-derived independently (symbolic, exhaustive over small k's):
# 3|S|+k1 < k2 with |S|=3k3+2k2+k1  <=>  9k3+5k2+4k1 < 0  -- impossible.
bad = [(k3, k2, k1) for k3 in range(6) for k2 in range(6) for k1 in range(6)
       if 3 * (3 * k3 + 2 * k2 + k1) + k1 < k2]
check("F1 Q29 final inequality has no non-negative solution (k<=5 exhaustive + algebra)",
      bad == [], str(bad))

print("TOTAL FAILURES: %d" % len(FAILS))
sys.exit(0 if not FAILS else 1)
