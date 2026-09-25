#!/usr/bin/env python3
"""
WOWII-133 round 38 -- (F11-ALL), the one live front.

Self-contained: every primitive is COPIED into this file, nothing is imported from another
round's script.  Pure stdlib -> runs on SYSTEM python3 (no networkx, no sympy).
Hard internal deadline; no SAT.  The only searches are a DEPTH-CAPPED anchored DFS (run
only on the RESIDUAL of PART 3, which is small) and a subset-enumeration oracle restricted
to n <= 13.  Everything else is a frame walk.  Enumerations that complete are CENSUSES and
the population is printed either way.

TARGET (draft section 42.1):
    (F11-ALL)   endpath(G,w) >= rad(G) + 4   for EVERY vertex w.

WHAT THIS FILE CERTIFIES (statements derived by hand in the round write-up):

  (TAIL-2''), (TAIL-3'')  THE COST IS A MAX OF TWO INVARIANTS, NOT ONE.
      Round 33/37 counted the dodge list at the frame and paid for it in a(.) alone:
          (TAIL-2')  a(y) >= 2 + k2,   k2 = #{ j in {d-2,d-3}         : N(y) cap N(u_j) != 0 }
          (TAIL-3')  a(z) >= 2 + k3,   k3 = #{ j in {d-1,d-2,d-3,d-4} : N(z) cap N(u_j) != 0 }
      The component argument throws the MATCHING EDGES of the neighbourhood away.  Counting
      the BAD VERTICES instead of the BAD COMPONENTS gives a second, INCOMPARABLE bound:
          (TAIL-2'')  a(y) >= 2 + k2   OR   deg(y) >= 3 + k2
          (TAIL-3'')  a(z) >= 2 + k3   OR   deg(z) >= 3 + k3
      i.e.  max( a(.), deg(.) - 1 ) >= 2 + k.   Proof in the round write-up; both halves are
      certified here BY BUILDING the ecc+3 / ecc+4 induced path and re-checking it with a
      checker independent of the search.

  (F11-DEG'')  min_v max( a(v), deg(v)-1 ) >= 6  =>  (F11-ALL).
      Strictly weaker hypothesis than r37's (F11-DEG) (min_v a(v) >= 6), and it names the
      residual more tightly: (F11-ALL) can fail only at a w every one of whose frames carries
      a vertex within distance 2 of the far end that is low in BOTH invariants.

  THE ATTAINABILITY CENSUS.  Section 42.3's blanket constants 4 and 6 are the counted forms
      with ALL indicators set to 1.  This file asks whether that worst case is ATTAINED at a
      real frame -- a minimum that is summed but never simultaneously attainable is a wrong
      constant, not a conservative one.

  THE PER-w COVERAGE CENSUS -- the front itself.  r37 counted FIRINGS PER FRAME (52807 of
      77724).  (F11-ALL) is a statement per (host, w): it needs ONE good frame, not all of
      them.  This file existentially quantifies over far ends, geodesics, y and z, and reports
      how much of the NEAR-CENTRAL stratum (where (F11-STRAT) says the target actually lives)
      the chain now settles, with the population printed and the direction of error stated.

PART 0 is a GUARD.  It DECLARES THE CLASS it claims and is tested against members of that
class it has NOT seen.  Classes already tested by this line: zero-step (r34), one-step (r35),
late-block (r36), off-by-one and anchor-drift (r37).  NONE of them is a COST-EVALUATOR defect
or a QUANTIFIER-SCOPE defect, which are what round 38 newly relies on.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 420.0
P1_CAP = 130          # host order cap for PART 1/2 (frame walk, cheap)
P3_CAP = 130          # host order cap for PART 3 (frame walk + build)
RES_DFS_CAP = 80      # host order cap for the residual-only anchored DFS in PART 4
MAXFAR = 6            # far ends sampled per w in PART 3's existential
MAXGEO = 3            # geodesics sampled per far end in PART 3's existential
CHECKS = 0
FAILS = 0
PARTS_RUN = []


def over():
    return (time.time() - T0) > DEADLINE


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


# ---------------------------------------------------------------- primitives
def adj(n, edges):
    g = [set() for _ in range(n)]
    for u, v in edges:
        if u != v:
            g[u].add(v)
            g[v].add(u)
    return g


def edges_of(g):
    return [(u, v) for u in range(len(g)) for v in g[u] if u < v]


def bfs(g, s):
    n = len(g)
    d = [-1] * n
    d[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in g[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def c4_free(g):
    """this line's sense: NO two vertices have two common neighbours."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
    """a(v) = alpha(G[N(v)]); C4-free => G[N(v)] is a matching => a = deg - #inside edges."""
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def t_val(g, v):
    """t(v) = #matching edges inside N(v) = deg(v) - a(v) (C4-free)."""
    nb = sorted(g[v])
    return sum(1 for x, y in combinations(nb, 2) if y in g[x])


def a_val_brute(g, v):
    """independent implementation, cross-check only: a maximum independent set in N(v)."""
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = max(best, k)
                break
        if best == k:
            break
    return best


def nbhd_components(g, v):
    nb = sorted(g[v])
    comp = {u: {u} for u in nb}
    for x, y in combinations(nb, 2):
        if y in g[x]:
            s = comp[x] | comp[y]
            for z in s:
                comp[z] = s
    out = []
    for u in nb:
        f = frozenset(comp[u])
        if f not in out:
            out.append(f)
    return out


def mean_a(g):
    n = len(g)
    return sum(a_val(g, v) for v in range(n)) / float(n)


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    return D, ecc, r


# --------------------------------------------------- INDEPENDENT path checker (guard)
def incidence_matrix(g):
    """built from edges_of(), i.e. from the edge LIST, not from the adjacency sets the
    frame walk uses -- the checker's independence lives here."""
    n = len(g)
    M = [[0] * n for _ in range(n)]
    for (u, v) in edges_of(g):
        M[u][v] = 1
        M[v][u] = 1
    return M


def checker_induced_anchored(g, P, w, need, M=None):
    """Independent of every search below.  Verifies P is an induced path, ANCHORED at w
    (P[0] == w), on exactly `need` vertices."""
    if P is None:
        return False
    if len(P) != need:
        return False
    if len(set(P)) != len(P):
        return False
    if P[0] != w:
        return False
    if M is None:
        M = incidence_matrix(g)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            want = 1 if j == i + 1 else 0
            if M[P[i]][P[j]] != want:
                return False
    return True


# --------------------------------------------------- anchored depth-capped DFS
def anchored_search(g, start, cap, node_budget=60000):
    """Longest induced path with `start` as an ENDPOINT, STOPPING once `cap` vertices are
    reached.  Returns (best_len, path_or_None, truncated).  If truncated is False and
    best_len < cap the search was COMPLETE, so endpath(g,start) = best_len exactly."""
    best = [0]
    bestP = [None]
    nodes = [0]
    trunc = [False]

    def rec(P, forb):
        if len(P) > best[0]:
            best[0] = len(P)
            bestP[0] = list(P)
        if best[0] >= cap:
            return True
        nodes[0] += 1
        if nodes[0] > node_budget or over():
            trunc[0] = True
            return True
        last = P[-1]
        for z in sorted(g[last]):
            if z in forb:
                continue
            P.append(z)
            if rec(P, forb | g[last] | {z}):
                P.pop()
                return True
            P.pop()
        return False

    rec([start], {start})
    return best[0], bestP[0], trunc[0]


# --------------------------------------------------- INDEPENDENT oracle (guard, n <= 13)
def oracle_endpath(g, start, cap):
    """Shares no code path with anchored_search: enumerates SUBSETS containing `start`, then
    tests whether the induced subgraph is a path with `start` as an endpoint."""
    n = len(g)
    others = [v for v in range(n) if v != start]
    best = 1
    for k in range(min(cap, n), 1, -1):
        if k <= best:
            break
        found = False
        for S in combinations(others, k - 1):
            vs = (start,) + S
            deg = {v: 0 for v in vs}
            ok = True
            for x, y in combinations(vs, 2):
                if y in g[x]:
                    deg[x] += 1
                    deg[y] += 1
            if any(d > 2 for d in deg.values()):
                ok = False
            if ok and deg[start] != 1:
                ok = False
            if ok and sum(deg.values()) // 2 != k - 1:
                ok = False
            if ok:
                seen = {start}
                cur = start
                for _ in range(k - 1):
                    nxt = [z for z in g[cur] if z in deg and z not in seen]
                    if len(nxt) != 1:
                        ok = False
                        break
                    cur = nxt[0]
                    seen.add(cur)
                if ok and len(seen) != k:
                    ok = False
            if ok:
                found = True
                break
        if found:
            best = k
            break
    return best


# ------------------------------------------------------------------ hosts
def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def theta333():
    return adj(8, [(0, 1), (1, 2), (2, 7), (0, 3), (3, 4), (4, 7), (0, 5), (5, 6), (6, 7)])


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def pathgraph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


def pg2(q):
    """incidence graph of PG(2,q), q prime: bipartite, girth 6, (q+1)-regular, a(v)=q+1."""
    def norm(v):
        for i in range(3):
            if v[i] % q:
                inv = pow(v[i], q - 2, q)
                return tuple((c * inv) % q for c in v)
    pts = sorted({norm((a, b, c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a, b, c) != (0, 0, 0)})
    idx = {p: i for i, p in enumerate(pts)}
    m = len(pts)
    E = []
    for j, L in enumerate(pts):
        for p in pts:
            if sum(p[t] * L[t] for t in range(3)) % q == 0:
                E.append((idx[p], m + j))
    return adj(2 * m, E)


def rand_c4free_dense(seed, n):
    """seeded C4-free PROCESS (r33's): random order over all pairs, add iff it keeps
    'no two vertices with two common neighbours'; then peel a=1 vertices."""
    st = seed

    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for i in range(len(pairs) - 1, 0, -1):
        j = nxt(i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = [set() for _ in range(n)]
    for (u, v) in pairs:
        if any(g[u] & g[x] for x in g[v] if x != u):
            continue
        if any(g[v] & g[y] for y in g[u] if y != v):
            continue
        g[u].add(v)
        g[v].add(u)
    alive = set(range(n))
    while True:
        gone = [v for v in alive
                if len(g[v] & alive) - sum(1 for x, y in combinations(sorted(g[v] & alive), 2)
                                           if y in g[x]) <= 1]
        if not gone:
            break
        alive -= set(gone)
        if not alive:
            return None
    idx = sorted(alive)
    pos = {v: i for i, v in enumerate(idx)}
    h = adj(len(idx), [(pos[u], pos[v]) for u in idx for v in g[u] if v in pos and u < v])
    if len(h) < 6 or not connected(h) or min(a_val(h, v) for v in range(len(h))) < 2:
        return None
    return h


def glue_cycle(g, at, k):
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(k - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, at))
    return adj(n, E)


def path_then_cycle(g, at, L, k):
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    tip = prev
    p = tip
    for _ in range(k - 1):
        E.append((p, n))
        p = n
        n += 1
    E.append((p, tip))
    return adj(n, E)


def blob_chain(q, L):
    b = pg2(q)
    bn = len(b)
    E = edges_of(b) + [(u + bn, v + bn) for (u, v) in edges_of(b)]
    n = 2 * bn
    prev = 1
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, bn + 0))
    return adj(n, E)


def build_family():
    """round 33's family, rebuilt here (COPIED, not imported).  Designed + seeded-random,
    NOT exhaustive."""
    fam = []
    b3, b5 = pg2(3), pg2(5)
    fam.append((b3, "PG(2,3)"))
    fam.append((b5, "PG(2,5)"))
    for k in (5, 7, 9, 11, 13, 15, 17, 19, 21, 25):
        fam.append((glue_cycle(b5, 0, k), "PG(2,5)+C%d glued" % k))
        fam.append((glue_cycle(b3, 0, k), "PG(2,3)+C%d glued" % k))
    for L, k in ((1, 5), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 9), (5, 9), (6, 11)):
        fam.append((path_then_cycle(b5, 0, L, k), "PG(2,5)+P%d+C%d" % (L, k)))
    for k1, k2 in ((7, 7), (9, 9), (11, 11), (13, 13), (9, 11)):
        g = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g, 1, k2), "PG(2,5)+C%d@0+C%d@1" % (k1, k2)))
        g2 = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g2, 5, k2), "PG(2,5)+C%d@0+C%d@5" % (k1, k2)))
    for L in (3, 5, 7, 9, 11):
        fam.append((blob_chain(5, L), "2xPG(2,5)+P%d" % L))
        fam.append((blob_chain(3, L), "2xPG(2,3)+P%d" % L))
    for n0 in (14, 18, 22, 26, 30, 34, 38, 44, 50):
        for s in range(1, 26):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                fam.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    for n0 in (26, 30, 34, 38, 44, 50):
        for s in (1, 2, 3, 4, 5, 6, 7, 8):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is None:
                continue
            for k in (5, 7, 9):
                fam.append((glue_cycle(h, 0, k), "dense(s=%d,n0=%d)+C%d" % (s, n0, k)))
    return fam


# ------------------------------------------------------------------ frames
def geodesics_from(g, D, w, ud, limit):
    """up to `limit` distinct geodesics w = u_0 ... u_d = ud, built back-to-front."""
    out = []
    stack = [[ud]]
    while stack and len(out) < limit:
        P = stack.pop()
        cur = P[-1]
        if cur == w:
            out.append(list(reversed(P)))
            continue
        step = D[w][cur] - 1
        for x in sorted(g[cur]):
            if D[w][x] == step:
                stack.append(P + [x])
                if len(stack) > 60:
                    break
    return out


def frames(g, D, ecc, w, max_far, max_geo, home_blind=False, dmin=3):
    """yields (P, ud, y): P a geodesic from w to a FARTHEST vertex ud, and y a neighbour of
    ud in a component of G[N(ud)] OTHER than u_{d-1}'s -- exactly (TAIL-1)'s frame.

    `dmin` is the shortest ecc(w) admitted.  Round 37 used 3 and PARTS 1/2 keep 3 so their
    numbers are head-to-head with r37's; PART 3 uses 2, because the dodge lists are clipped
    to the geodesic and every extension it accepts is CERTIFIED BY THE CHECKER, not asserted.

    `home_blind=True` is PART 0's planted QUANTIFIER-SCOPE defect: it lets y range over the
    HOME component too, which (TAIL-1) forbids."""
    n = len(g)
    d = ecc[w]
    if d < dmin:
        return
    fars = [v for v in range(n) if D[w][v] == d][:max_far]
    for ud in fars:
        for P in geodesics_from(g, D, w, ud, max_geo):
            if len(P) != d + 1:
                continue
            comps = nbhd_components(g, ud)
            home = None
            for C in comps:
                if P[-2] in C:
                    home = C
            for C in comps:
                if C is home and not home_blind:
                    continue
                for y in sorted(C):
                    if y == P[-2]:
                        continue
                    yield (P, ud, y)


def dodge_count(g, P, v, idxs):
    """#{ j in idxs (clipped to the geodesic) : N(v) cap N(u_j) != empty }."""
    d = len(P) - 1
    c = 0
    for j in idxs:
        if 0 <= j <= d:
            if g[v] & g[P[j]]:
                c += 1
    return c


IDX2 = None       # set per frame: (d-2, d-3)
IDX3 = None       # set per frame: (d-1, d-2, d-3, d-4)


def cost_fires(g, P, v, idxs, mode, blanket_const, defect=None):
    """Does the step condition fire at `v`?  Returns (fires, k, a, deg).

    mode 'blanket' : section 42.3's constant                     a(v) >= blanket_const
    mode 'sharp'   : r33/r37 counted form  (TAIL-2')/(TAIL-3')   a(v) >= 2 + k
    mode 'pp'      : round 38 form         (TAIL-2'')/(TAIL-3'') max(a, deg-1) >= 2 + k

    `defect` injects a deliberate fault -- used ONLY by PART 0's guard tests.
      'undercount' : counts the dodge list over only the first HALF of the index list
      'offbyone'   : pays one less than the proof demands
    """
    use = idxs
    if defect == "undercount":
        use = idxs[:max(1, len(idxs) // 2)]
    k = dodge_count(g, P, v, use)
    a = a_val(g, v)
    dg = len(g[v])
    need = 2 + k
    if defect == "offbyone":
        need = 1 + k
    if mode == "blanket":
        return (a >= blanket_const, k, a, dg)
    if mode == "sharp":
        return (a >= need, k, a, dg)
    return (a >= need or dg >= need + 1, k, a, dg)


def step2_build(g, P, y, w, M):
    """all z in N(y) that make w..u_d y z an induced anchored path on d+3 vertices."""
    d = len(P) - 1
    return [z for z in sorted(g[y])
            if checker_induced_anchored(g, P + [y, z], w, d + 3, M)]


def step3_build(g, P, y, z, w, M):
    d = len(P) - 1
    return [t for t in sorted(g[z])
            if checker_induced_anchored(g, P + [y, z, t], w, d + 4, M)]


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- THE GUARD.  CLASS DECLARED, TESTED AGAINST MEMBERS IT HAS NOT SEEN")
    print("=" * 78)
    print("CLASS CLAIMED: any COST EVALUATOR that mis-states what a frame extension costs")
    print("  (under- or over-counting the dodge list, or paying one less than the proof")
    print("  demands), and any QUANTIFIER-SCOPE defect that widens the legal set of frames.")
    print("GUARD: every firing must BUILD the induced anchored path and survive a checker")
    print("  built from the EDGE LIST, not from the adjacency sets the frame walk uses.")
    print("UNSEEN MEMBERS (none is zero-step / one-step / late-block / off-by-one-search /")
    print("  anchor-drift -- the five members r34..r37 tested):")
    print("    (D1) COST-UNDERCOUNT  -- dodge list counted over half the indices")
    print("    (D2) COST-OFFBYONE    -- pays 1+k where the proof demands 2+k")
    print("    (D3) HOME-BLIND       -- y allowed to range over u_{d-1}'s OWN component")
    print()
    ghosts = [(cycle(6), "C6"), (theta333(), "Theta(3,3,3)"), (petersen(), "Petersen"),
              (cycle(9), "C9"), (pg2(3), "PG(2,3)"), (blob_chain(3, 3), "2xPG(2,3)+P3")]
    # r37's OWN error 1: every guard host there was TRIANGLE-FREE, so a defect that needs a
    # triangle to express itself scored 0 and looked harmless.  (D3) HOME-BLIND is exactly
    # such a defect -- on a triangle-free host the home component is a singleton {u_{d-1}}
    # and widening to it adds NOTHING.  Two triangle-carrying hosts are therefore MANDATORY.
    for (s, n0) in ((2, 14), (1, 22)):
        h = rand_c4free_dense(s * 7919 + n0, n0)
        if h is not None:
            ghosts.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    tri_hosts = sum(1 for g, nm in ghosts if any(t_val(g, v) for v in range(len(g))))
    print("guard hosts: %d, of which TRIANGLE-CARRYING: %d" % (len(ghosts), tri_hosts))
    ck(tri_hosts > 0, "every guard host is triangle-free -- r37 error 1, recommitted")
    # -- cross-check the two a(.) implementations on every guard host
    ax = 0
    for g, nm in ghosts:
        for v in range(len(g)):
            ck(a_val(g, v) == a_val_brute(g, v), "a(.) implementations disagree on %s" % nm)
            ax += 1
    print("a(.) matching-formula vs brute independent-set, vertices agreeing: %d" % ax)

    rows = 0
    fires = {"D1": 0, "D2": 0, "D3": 0}
    extra = {"D1": 0, "D2": 0, "D3": 0}     # fires where the CORRECT evaluator does not
    caught = {"D1": 0, "D2": 0, "D3": 0}    # ... and the BUILD half refuses it
    invisible = {"D1": 0, "D2": 0, "D3": 0}  # fires extra, but a witness exists anyway
    correct_fire = 0
    correct_built = 0
    correct_false_alarm = 0
    for g, nm in ghosts:
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        for w in range(len(g)):
            for (P, ud, y) in frames(g, D, ecc, w, max_far=99, max_geo=3):
                d = len(P) - 1
                rows += 1
                idx2 = (d - 2, d - 3)
                ok_c, k, a, dg = cost_fires(g, P, y, idx2, "pp", 4)
                zs = step2_build(g, P, y, w, M)
                if ok_c:
                    correct_fire += 1
                    if zs:
                        correct_built += 1
                    else:
                        correct_false_alarm += 1
                        ck(False, "CORRECT (TAIL-2'') fired with no z on %s w=%d" % (nm, w))
                for tag, dfc in (("D1", "undercount"), ("D2", "offbyone")):
                    ok_d, _, _, _ = cost_fires(g, P, y, idx2, "pp", 4, defect=dfc)
                    if ok_d:
                        fires[tag] += 1
                    if ok_d and not ok_c:
                        extra[tag] += 1
                        if not zs:
                            caught[tag] += 1
                        else:
                            invisible[tag] += 1
            # (D3) HOME-BLIND: illegal frames, and the checker must refuse the path
            for (P, ud, y) in frames(g, D, ecc, w, max_far=99, max_geo=3, home_blind=True):
                d = len(P) - 1
                if y in g[P[d - 1]] or y == P[d - 1]:
                    fires["D3"] += 1
                    extra["D3"] += 1
                    ok = checker_induced_anchored(g, P + [y], w, d + 2, M)
                    if not ok:
                        caught["D3"] += 1
                    else:
                        invisible["D3"] += 1
    print("frame rows walked on the guard hosts:                    %d" % rows)
    print("CORRECT (TAIL-2'') firings / of which BUILT:             %d / %d"
          % (correct_fire, correct_built))
    print("CORRECT evaluator FALSE ALARMS (fired, nothing to build): %d" % correct_false_alarm)
    print()
    print("member  fires  fires-where-correct-does-not  CAUGHT by build  INVISIBLE")
    for tag in ("D1", "D2", "D3"):
        print("  %-4s  %5d  %27d  %15d  %9d"
              % (tag, fires[tag], extra[tag], caught[tag], invisible[tag]))
    print()
    print("THE THRESHOLD IS PART OF THE GUARD (r37's finding, re-measured here):")
    print("  an over-permissive cost defect is INVISIBLE at a frame that extends anyway --")
    print("  the INVISIBLE column counts exactly those.  A guard scored only where it fires")
    print("  cannot see them, which is why the extra/caught split is printed separately.")
    ck(correct_false_alarm == 0, "the correct cost evaluator raised a false alarm")
    ck(caught["D3"] > 0, "HOME-BLIND was never caught -- the checker is not doing its job")
    ck(rows > 0, "PART 0 walked an EMPTY set of frames (pass-by-emptiness)")
    ck(sum(extra.values()) > 0, "no planted defect ever fired extra -- the arms are no-ops")
    # non-vacuity of each arm, stated separately so a silent no-op arm cannot hide
    for tag in ("D1", "D2", "D3"):
        if extra[tag] == 0:
            print("  NOTE: arm %s NEVER fired where the correct evaluator did not -- on this"
                  % tag)
            print("        host set it is a NO-OP and scores nothing.  Reported, not hidden.")
    return rows


# ------------------------------------------------------------------ PART 1
def part1(fam):
    """(TAIL-2'') / (TAIL-3''): the cost is a MAX of two invariants.  Certified by BUILDING."""
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (TAIL-2'') AND (TAIL-3''), CERTIFIED BY *BUILDING* THE PATH")
    print("          convention: z is the FIRST constructible z, as in round 37, so the")
    print("          margin below is head-to-head with r37's numbers")
    print("=" * 78)
    skipped = 0
    used = 0
    fr = 0
    c2 = {"blanket": 0, "sharp": 0, "pp": 0}
    c3 = {"blanket": 0, "sharp": 0, "pp": 0}
    c3r37 = {"blanket": 0, "sharp": 0, "pp": 0}
    g3_r37 = 0
    g3_r38 = 0
    built2 = 0
    built3 = 0
    pp_beats_sharp2 = 0
    pp_beats_sharp3 = 0
    pp_beats_sharp2_built = 0
    pp_beats_sharp3_built = 0
    tri_free_frames = 0
    for g, nm in fam:
        if over():
            break
        n = len(g)
        if n > P1_CAP:
            skipped += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        used += 1
        for w in range(n):
            if over():
                break
            for (P, ud, y) in frames(g, D, ecc, w, max_far=2, max_geo=1):
                fr += 1
                d = len(P) - 1
                idx2 = (d - 2, d - 3)
                idx3 = (d - 1, d - 2, d - 3, d - 4)
                if t_val(g, y) == 0:
                    tri_free_frames += 1
                for m in ("blanket", "sharp", "pp"):
                    ok, k, a, dg = cost_fires(g, P, y, idx2, m, 4)
                    if ok:
                        c2[m] += 1
                ok_s, k2, a2, dg2 = cost_fires(g, P, y, idx2, "sharp", 4)
                ok_p, _, _, _ = cost_fires(g, P, y, idx2, "pp", 4)
                if not ok_p:
                    continue
                zs = step2_build(g, P, y, w, M)
                if zs:
                    built2 += 1
                else:
                    ck(False, "(TAIL-2'') FIRED BUT NO z ON %s w=%d" % (nm, w))
                    continue
                if ok_p and not ok_s:
                    pp_beats_sharp2 += 1
                    pp_beats_sharp2_built += 1
                z = zs[0]
                # HEAD-TO-HEAD GATE.  r37 reached step 3 ONLY through (TAIL-2'), so its
                # step-3 row is over that smaller frame set.  Counting step 3 behind the
                # WIDER (TAIL-2'') gate and calling the result head-to-head would be a
                # population swap -- exactly the defect r37 committed at its PART 3.  Both
                # gates are therefore carried, and both populations are printed.
                if ok_s:
                    g3_r37 += 1
                    for m in ("blanket", "sharp", "pp"):
                        ok, k, a, dg = cost_fires(g, P, z, idx3, m, 6)
                        if ok:
                            c3r37[m] += 1
                g3_r38 += 1
                for m in ("blanket", "sharp", "pp"):
                    ok, k, a, dg = cost_fires(g, P, z, idx3, m, 6)
                    if ok:
                        c3[m] += 1
                ok_s3, k3, a3, dg3 = cost_fires(g, P, z, idx3, "sharp", 6)
                ok_p3, _, _, _ = cost_fires(g, P, z, idx3, "pp", 6)
                if not ok_p3:
                    continue
                ts = step3_build(g, P, y, z, w, M)
                if ts:
                    built3 += 1
                else:
                    ck(False, "(TAIL-3'') FIRED BUT NO t ON %s w=%d" % (nm, w))
                    continue
                if ok_p3 and not ok_s3:
                    pp_beats_sharp3 += 1
                    pp_beats_sharp3_built += 1
    print("hosts entered (n <= %d) / skipped as too big:  %d / %d" % (P1_CAP, used, skipped))
    print("frames examined (geodesic, y):                 %d" % fr)
    print("  of them with t(y) = 0 (no triangle at y):    %d" % tri_free_frames)
    print()
    print("STEP 2 -- fires:  blanket a(y)>=4 : %d" % c2["blanket"])
    print("                  (TAIL-2')       : %d" % c2["sharp"])
    print("                  (TAIL-2'')      : %d" % c2["pp"])
    print("  (TAIL-2'') firings with the ecc+3 path BUILT and checked: %d" % built2)
    print("  frames (TAIL-2'') wins that (TAIL-2') LOSES:             %d" % pp_beats_sharp2)
    print("     ... every one of them BUILT:                          %d" % pp_beats_sharp2_built)
    print()
    print("STEP 3, HEAD-TO-HEAD GATE (r37's: step 2 reached through (TAIL-2') only)")
    print("  frames reaching step 3 under that gate:      %d" % g3_r37)
    print("           fires:  blanket a(z)>=6 : %d" % c3r37["blanket"])
    print("                   (TAIL-3')       : %d" % c3r37["sharp"])
    print("                   (TAIL-3'')      : %d" % c3r37["pp"])
    print()
    print("STEP 3, ROUND 38's OWN GATE (step 2 reached through (TAIL-2''))")
    print("  frames reaching step 3 under this gate:      %d" % g3_r38)
    print("           fires:  blanket a(z)>=6 : %d" % c3["blanket"])
    print("                   (TAIL-3')       : %d" % c3["sharp"])
    print("                   (TAIL-3'')      : %d" % c3["pp"])
    print("  (TAIL-3'') firings with the ecc+4 path BUILT and checked: %d" % built3)
    print("  frames (TAIL-3'') wins that (TAIL-3') LOSES:             %d" % pp_beats_sharp3)
    print("     ... every one of them BUILT:                          %d" % pp_beats_sharp3_built)
    print()
    print("WHERE THE GAIN CAN COME FROM, and it is a THEOREM about this family, not a hope:")
    print("  deg = a + t, so deg-1 >= 2+k with a <= 1+k forces t >= 2.  On a TRIANGLE-FREE")
    print("  vertex t = 0 and the degree half can NEVER win.  Every PG(2,q) incidence graph")
    print("  is bipartite, so on those hosts the sharpening is VACUOUS BY CONSTRUCTION.")
    ck(c2["pp"] >= c2["sharp"], "(TAIL-2'') fired less often than (TAIL-2') -- impossible")
    ck(c3["pp"] >= c3["sharp"], "(TAIL-3'') fired less often than (TAIL-3') -- impossible")
    ck(pp_beats_sharp2 == pp_beats_sharp2_built, "a (TAIL-2'') gain was not built")
    ck(pp_beats_sharp3 == pp_beats_sharp3_built, "a (TAIL-3'') gain was not built")
    ck(fr > 0, "PART 1 walked an EMPTY frame set (pass-by-emptiness)")
    ck(used > 0, "PART 1 entered an EMPTY host set (pass-by-emptiness)")
    return fr


# ------------------------------------------------------------------ PART 2
def part2(fam):
    """ATTAINABILITY: is the blanket's implied worst case ever attained at a real frame?"""
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- ARE THE SUMMED MINIMA SIMULTANEOUSLY ATTAINABLE?")
    print("          section 42.3's constants 4 and 6 are the counted forms with EVERY")
    print("          indicator set to 1.  A worst case that no frame attains is a WRONG")
    print("          constant, not a conservative one.")
    print("=" * 78)
    h2 = [0] * 3
    h3 = [0] * 5
    frames_seen = 0
    both_max = 0
    used = 0
    skipped = 0
    ex2 = None
    ex3 = None
    for g, nm in fam:
        if over():
            break
        n = len(g)
        if n > P1_CAP:
            skipped += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        used += 1
        for w in range(n):
            if over():
                break
            for (P, ud, y) in frames(g, D, ecc, w, max_far=2, max_geo=1):
                d = len(P) - 1
                frames_seen += 1
                k2 = dodge_count(g, P, y, (d - 2, d - 3))
                h2[k2] += 1
                if k2 == 2 and ex2 is None:
                    ex2 = (nm, w, d, k2)
                zs = step2_build(g, P, y, w, M)
                if not zs:
                    continue
                z = zs[0]
                k3 = dodge_count(g, P, z, (d - 1, d - 2, d - 3, d - 4))
                h3[k3] += 1
                if k3 == 4 and ex3 is None:
                    ex3 = (nm, w, d, k3)
                if k2 == 2 and k3 == 4:
                    both_max += 1
    print("hosts entered / skipped:                       %d / %d" % (used, skipped))
    print("frames with a step-2 index count k2:           %d" % frames_seen)
    for i in range(3):
        print("   k2 = %d :  %d" % (i, h2[i]))
    print("frames that reached a step-3 index count k3:   %d" % sum(h3))
    for i in range(5):
        print("   k3 = %d :  %d" % (i, h3[i]))
    print()
    kmax2 = max([i for i in range(3) if h2[i] > 0]) if sum(h2) else -1
    kmax3 = max([i for i in range(5) if h3[i] > 0]) if sum(h3) else -1
    print("MAX k2 ATTAINED on this family: %d   (blanket a(y)>=4 assumes k2 = 2)" % kmax2)
    print("MAX k3 ATTAINED on this family: %d   (blanket a(z)>=6 assumes k3 = 4)" % kmax3)
    print("frames attaining BOTH worst cases at once (k2=2 AND k3=4): %d" % both_max)
    if ex2 is not None:
        print("  witness for k2 = 2: host %s, w = %d, d = %d" % (ex2[0], ex2[1], ex2[2]))
    else:
        print("  NO frame on this family attains k2 = 2.")
    if ex3 is not None:
        print("  witness for k3 = 4: host %s, w = %d, d = %d" % (ex3[0], ex3[1], ex3[2]))
    else:
        print("  NO frame on this family attains k3 = 4.")
    print()
    print("READING, and the direction of the claim is stated: this family is DESIGNED plus")
    print("SEEDED-RANDOM and NOT exhaustive, so a k value not attained here is a")
    print("MEASUREMENT about the family, NOT a theorem that the blanket constant is wrong.")
    print("What it IS: the evidence needed before anyone sums those minima again.")
    ck(frames_seen > 0, "PART 2 walked an EMPTY frame set (pass-by-emptiness)")
    ck(sum(h3) > 0, "PART 2 reached NO step-3 frame (pass-by-emptiness at step 3)")
    return kmax2, kmax3, both_max


# ------------------------------------------------------------------ PART 3
def part3(fam, max_far, max_geo):
    """THE FRONT: per-(host,w) EXISTENTIAL coverage of the near-central stratum."""
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- THE PER-w COVERAGE CENSUS  (this is the front)")
    print("          (F11-STRAT): ecc(w) >= rad+2 is FREE from (TAIL-1).  The target lives")
    print("          on {w : ecc(w) <= rad+1}.  (F11-ALL) needs ONE good frame per w, not")
    print("          all of them -- so the quantifier is EXISTENTIAL over far ends,")
    print("          geodesics, y and z.  r37 counted FIRINGS PER FRAME; this counts w's.")
    print("=" * 78)
    print("sampling: max_far = %d far ends, max_geo = %d geodesics each" % (max_far, max_geo))
    print("DIRECTION OF ERROR, stated before the numbers: COVERED is certified by BUILDING")
    print("  the path, so COVERED is a LOWER bound on true coverage; RESIDUAL is therefore")
    print("  an UPPER bound on the true residual -- widening the sampling can only shrink it.")
    print()
    free = 0
    cov3 = 0
    cov4 = 0
    resid = []
    tooshort = 0
    pop = 0
    used = 0
    skipped = 0
    popL = 0
    residL = 0
    popLR = 0
    residLR = 0
    hostsL = 0
    hostsLR = 0
    named = []
    for g, nm in fam:
        if over():
            break
        n = len(g)
        if n > P3_CAP:
            skipped += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        l = mean_a(g)
        rich = l > 4.0
        richrad = rich and r >= 5
        used += 1
        if rich:
            hostsL += 1
        if richrad:
            hostsLR += 1
        for w in range(n):
            if over():
                break
            e = ecc[w]
            if e >= r + 2:
                free += 1
                continue
            pop += 1
            if rich:
                popL += 1
            if richrad:
                popLR += 1
            need = r + 4                     # vertices in the anchored induced path
            if e < 2:
                tooshort += 1
                resid.append((nm, w, r, e, l, "ecc<2: no (TAIL-1) frame exists at all"))
                if rich:
                    residL += 1
                if richrad:
                    residLR += 1
                continue
            done = False
            for (P, ud, y) in frames(g, D, ecc, w, max_far=max_far, max_geo=max_geo,
                                     dmin=2):
                d = len(P) - 1
                idx2 = (d - 2, d - 3)
                idx3 = (d - 1, d - 2, d - 3, d - 4)
                ok2, _, _, _ = cost_fires(g, P, y, idx2, "pp", 4)
                if not ok2:
                    continue
                zs = step2_build(g, P, y, w, M)
                if not zs:
                    ck(False, "(TAIL-2'') fired with no z on %s w=%d" % (nm, w))
                    continue
                if d + 3 >= need:
                    ck(checker_induced_anchored(g, P + [y, zs[0]], w, d + 3, M),
                       "covered-at-3 path failed the independent checker on %s" % nm)
                    cov3 += 1
                    done = True
                    break
                for z in zs:
                    ok3, _, _, _ = cost_fires(g, P, z, idx3, "pp", 6)
                    if not ok3:
                        continue
                    ts = step3_build(g, P, y, z, w, M)
                    if not ts:
                        ck(False, "(TAIL-3'') fired with no t on %s w=%d" % (nm, w))
                        continue
                    if d + 4 >= need:
                        ck(checker_induced_anchored(g, P + [y, z, ts[0]], w, d + 4, M),
                           "covered-at-4 path failed the independent checker on %s" % nm)
                        cov4 += 1
                        done = True
                        break
                if done:
                    break
            if not done:
                resid.append((nm, w, r, e, l, "no frame in the sample settles it"))
                if rich:
                    residL += 1
                if richrad:
                    residLR += 1
                    named.append((nm, w, r, e, l, len(g)))
    print("hosts entered (n <= %d) / skipped as too big:   %d / %d" % (P3_CAP, used, skipped))
    print("   of them with l > 4:                          %d" % hostsL)
    print("   of them with l > 4 AND rad >= 5:             %d" % hostsLR)
    print("vertices FREE by (TAIL-1) alone (ecc >= rad+2): %d" % free)
    print("NEAR-CENTRAL POPULATION the verdict is about:   %d" % pop)
    print("   of them on hosts with l > 4:                 %d" % popL)
    print("   of them on hosts with l > 4 AND rad >= 5:    %d" % popLR)
    print()
    print("COVERED by the chain, path BUILT at ecc+3:      %d" % cov3)
    print("COVERED by the chain, path BUILT at ecc+4:      %d" % cov4)
    print("RESIDUAL (chain does not settle w):             %d" % len(resid))
    print("   of the residual, ecc(w) < 3 so no frame exists at all: %d" % tooshort)
    print("   residual on hosts with l > 4:                %d" % residL)
    print("   residual on hosts with l > 4 AND rad >= 5:   %d" % residLR)
    if pop:
        print("COVERAGE of the near-central stratum:           %d / %d" % (cov3 + cov4, pop))
    print()
    print("THE RESIDUAL INSIDE F11's HYPOTHESIS CLASS, NAMED ONE BY ONE -- this is what")
    print("round 39 inherits, and if the list is EMPTY that is printed too:")
    if named:
        for (nm, w, r, e, l, n) in named:
            print("   host %s  n=%d  w=%d  rad=%d  ecc=%d  l=%.3f" % (nm, n, w, r, e, l))
    else:
        print("   (empty -- every near-central vertex on an l>4, rad>=5 host is COVERED)")
    ck(pop > 0, "PART 3 near-central population is EMPTY (pass-by-emptiness)")
    ck(popL > 0, "PART 3 l>4 sub-population is EMPTY and the verdict would be vacuous")
    ck(cov3 + cov4 + len(resid) == pop, "coverage census does not partition its population")
    ck(used > 0, "PART 3 entered an EMPTY host set")
    return resid, pop, popL, popLR, free


# ------------------------------------------------------------------ PART 4
def part4(fam, resid, max_far):
    """WHAT THE RESIDUAL IS: chain-insufficiency or statement-failure?  Plus the
    (F11-DEG'') prediction, and the LIVENESS test the round designed against itself."""
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE RESIDUAL, SEPARATED INTO 'THE CHAIN IS SHORT' AND 'THE STATEMENT")
    print("          FAILS' -- and the liveness test this round wrote against itself")
    print("=" * 78)
    print("(F11-DEG'')  min_v max( a(v), deg(v)-1 ) >= 6  =>  (F11-ALL).")
    print("  Strictly weaker than r37's (F11-DEG) (min_v a(v) >= 6), because deg >= a.")
    print("  PREDICTION it makes about every residual w: some vertex within distance 2 of")
    print("  the far end of EVERY frame from w is low in BOTH invariants.  Tested below.")
    print()
    byname = {}
    for g, nm in fam:
        byname.setdefault(nm, g)
    has_witness = 0
    proved_below = 0
    undecided = 0
    too_big = 0
    pred_ok = 0
    pred_tested = 0
    oracle_rows = 0
    oracle_agree = 0
    shown = 0
    liveness_hit = False
    for (nm, w, r, e, l, why) in resid:
        if over():
            break
        g = byname.get(nm)
        if g is None:
            continue
        n = len(g)
        if n > RES_DFS_CAP:
            too_big += 1
            continue
        need = r + 4
        best, P, trunc = anchored_search(g, w, need)
        if best >= need:
            ck(checker_induced_anchored(g, P, w, len(P)),
               "residual witness failed the independent checker on %s" % nm)
            has_witness += 1
        elif trunc:
            undecided += 1
        else:
            proved_below += 1
            if shown < 6:
                print("  PROVED BELOW: host %s  w=%d  rad=%d  ecc=%d  l=%.3f  endpath=%d < %d"
                      % (nm, w, r, e, l, best, need))
                shown += 1
            if nm.startswith("dense(s=5,n0=14)") and w == 7:
                liveness_hit = True
        if n <= 13:
            ob = oracle_endpath(g, w, need)
            oracle_rows += 1
            if (ob >= need) == (best >= need):
                oracle_agree += 1
            else:
                ck(False, "oracle disagrees with the DFS verdict on %s w=%d" % (nm, w))
        # ---- (F11-DEG'') prediction: a low vertex within distance 2 of some far end
        D = [bfs(g, v) for v in range(n)]
        ecc = [max(D[v]) for v in range(n)]
        d = ecc[w]
        fars = [v for v in range(n) if D[w][v] == d][:max_far]
        if fars and d >= 2:
            pred_tested += 1
            # the prediction is about EVERY far end the coverage walk actually sampled, so
            # the test is a MAX over far ends of the MIN over B_2 -- the weaker "some far
            # end is low" would be a test the prediction does not make.
            worst = max(min(max(a_val(g, u), len(g[u]) - 1)
                            for u in range(n) if D[f][u] <= 2) for f in fars)
            if worst < 6:
                pred_ok += 1
            else:
                ck(False, "(F11-DEG'') PREDICTION VIOLATED on %s w=%d: B2 max-min = %d"
                   % (nm, w, worst))
    print()
    print("residual entries examined (n <= %d):            %d"
          % (RES_DFS_CAP, has_witness + proved_below + undecided))
    print("residual entries skipped as too big for a DFS:  %d" % too_big)
    print("  ... the chain is SHORT (a rad+4 path exists): %d" % has_witness)
    print("  ... the STATEMENT FAILS (search COMPLETE):    %d" % proved_below)
    print("  ... UNDECIDED (search truncated):             %d" % undecided)
    print("independent subset oracle rows (n <= 13) / agreeing: %d / %d"
          % (oracle_rows, oracle_agree))
    print("(F11-DEG'') prediction tested / holding:        %d / %d" % (pred_tested, pred_ok))
    print()
    print("LIVENESS, designed against this round's own interest: r37 exhibited an explicit")
    print("  vertex where (F11-ALL) is FALSE without F11's hypotheses -- dense(s=5,n0=14),")
    print("  w=7, endpath 5 < 6.  A coverage census that CANNOT fail proves nothing, so this")
    print("  vertex MUST land in the residual and MUST come back PROVED BELOW.")
    print("  landed in the residual and proved below: %s" % ("YES" if liveness_hit else "NO"))
    ck(liveness_hit, "LIVENESS FAILED: the known false vertex was not left in the residual")
    ck(pred_tested == pred_ok, "(F11-DEG'') prediction violated somewhere")
    ck(oracle_rows == oracle_agree, "oracle and DFS disagreed on a residual verdict")
    return has_witness, proved_below, undecided


# ------------------------------------------------------------------ PART 5
def part5(fam):
    """(F11-DEG'') vs (F11-DEG): is the weakening NON-VACUOUS, and where?"""
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- IS (F11-DEG'') A REAL WEAKENING OF (F11-DEG), OR ONLY A FORMAL ONE?")
    print("=" * 78)
    pool = list(fam) + [(pg2(3), "PG(2,3)"), (pg2(5), "PG(2,5)"),
                        (pg2(7), "PG(2,7)"), (pg2(11), "PG(2,11)")]
    n_deg = 0
    n_degpp = 0
    n_only_pp = 0
    only_names = []
    vert_only = 0
    vert_total = 0
    for g, nm in pool:
        if over():
            break
        n = len(g)
        mina = min(a_val(g, v) for v in range(n))
        minpp = min(max(a_val(g, v), len(g[v]) - 1) for v in range(n))
        for v in range(n):
            vert_total += 1
            if a_val(g, v) < 6 <= max(a_val(g, v), len(g[v]) - 1):
                vert_only += 1
        if mina >= 6:
            n_deg += 1
        if minpp >= 6:
            n_degpp += 1
        if minpp >= 6 and mina < 6:
            n_only_pp += 1
            if len(only_names) < 5:
                only_names.append(nm)
    print("host slots in the pool:                                  %d" % len(pool))
    print("host slots satisfying (F11-DEG)   min a >= 6:            %d" % n_deg)
    print("host slots satisfying (F11-DEG'') min max(a,deg-1) >= 6: %d" % n_degpp)
    print("host slots satisfying (F11-DEG'') but NOT (F11-DEG):     %d" % n_only_pp)
    if only_names:
        print("   e.g. %s" % ", ".join(only_names))
    print("vertices with a(v) < 6 <= max(a(v),deg(v)-1):            %d of %d"
          % (vert_only, vert_total))
    print()
    print("STATED AGAINST THIS ROUND'S INTEREST: (F11-DEG'') is a THEOREM either way -- the")
    print("proof is the vertex count in place of the component count -- but if the two")
    print("columns above are EQUAL then on THIS pool the weakening buys nothing, and this")
    print("round says so rather than shipping a formal generalisation as progress.")
    ck(n_degpp >= n_deg, "(F11-DEG'') admitted fewer hosts than (F11-DEG) -- impossible")
    ck(len(pool) > 0, "PART 5 pool is EMPTY (pass-by-emptiness)")
    return n_deg, n_degpp, n_only_pp


# ------------------------------------------------------------------ main
def main():
    print("=" * 78)
    print("WOWII-133 round 38 -- (F11-ALL): the cost is a MAX of two invariants, and the")
    print("coverage census moves from FRAMES to VERTICES")
    print("=" * 78)
    print("interpreter:", sys.version.split()[0], "(pure stdlib; system python3)")
    print("hard internal deadline (s):", DEADLINE)
    fam = build_family()
    ok = 0
    for g, nm in fam:
        ck(connected(g), "host %s is not connected" % nm)
        ck(min(a_val(g, v) for v in range(len(g))) >= 2, "host %s has an a=1 vertex" % nm)
        ok += 1
    print("hosts built and certified connected + mu >= 2:", ok)
    small = [(g, nm) for g, nm in fam if len(g) <= 40][:12]
    for g, nm in small:
        ck(c4_free(g), "host %s is not C4-free" % nm)
    print("hosts re-certified C4-free (sample of the small ones):", len(small))

    part0()
    part1(fam)
    part2(fam)
    resid, pop, popL, popLR, free = part3(fam, max_far=MAXFAR, max_geo=MAXGEO)
    part4(fam, resid, max_far=MAXFAR)
    part5(fam)

    print()
    print("=" * 78)
    print("parts that self-registered:", ",".join(PARTS_RUN))
    print("CHECKS:", CHECKS, " FAILS:", FAILS)
    print("elapsed (s): %.1f" % (time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
