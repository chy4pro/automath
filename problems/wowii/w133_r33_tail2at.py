#!/usr/bin/env python3
"""
WOWII-133 round 33 — (TAIL-2) AT A PRESCRIBED w, IN THE l > 4 REGIME.

r33 item 1 (state file §7.1): prove/refute that at a w with ecc_{G'}(w) = rad(G')+1 and
w maximally far from every centre of G' ("the residual configuration" of draft §42.5), some
y in N(u_d) off u_{d-1}'s component has a(y) >= 4 — the anchored cap-break, with l(G') > 4
as the hypothesis that has to do the work.
r33 item 3 (state file §7.3): can the residual configuration carry l > 4 AT ALL?  Every
residual instance r32 found carries l <= 2.5, so the hypothesis has never yet been live.

SAME SCRIPT, BOTH QUESTIONS: they are the same census.

DISCIPLINE
  * self-contained: primitives are COPIED from w133_r32_anchor.py, never imported
    (r31 own-defect 7 / r32 own-defect 7: importing a guard-less script runs its whole
    program and can exit 0 having skipped this one's work).
  * every PART registers itself; the final check asserts all declared parts ran.
  * internal hard deadline; partial results are printed as they land, never held.
  * NO SAT, no exhaustive graph generation.  Everything here is BFS + neighbourhood
    independence numbers (polynomial) on explicit hosts; the only search is a
    node-budgeted, capped induced-path DFS run on named witnesses only.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 200.0          # seconds, internal.  Nothing here may rely on an outside timeout.
FAIL = 0
CHECKS = 0
PARTS_DECLARED = ["PART0", "PART1", "PART2", "PART3", "PART4"]
PARTS_RUN = []
SHARP = []          # (host, w, (TAIL-2') fires?, +3 built?) on every (TAIL-2)-FAILING w


def over():
    return time.time() - T0 > DEADLINE


def check(cond, msg):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("FAIL:", msg, flush=True)
    return cond


# ------------------------------------------------------------------ primitives
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
    """NO two vertices have two common neighbours (this line's sense of C4-free)."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def c4_free_slow(g):
    """Independent implementation: no 4-cycle as a SUBGRAPH.  Cross-check only (O(n^4))."""
    n = len(g)
    for a, b, c, d in combinations(range(n), 4):
        for perm in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            p, q, r, s = perm
            if q in g[p] and r in g[q] and s in g[r] and p in g[s]:
                return False
    return True


def a_val(g, v):
    """a(v) = alpha(G[N(v)]); C4-free => G[N(v)] is a matching => a = deg - #edges inside."""
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def a_val_brute(g, v):
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


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    return all((P[j] in g[P[i]]) == (j == i + 1)
               for i in range(len(P)) for j in range(i + 1, len(P)))


def mean_a(g):
    n = len(g)
    return sum(a_val(g, v) for v in range(n)) / float(n)


def longest_induced_path(g, start, cap, node_budget=400_000):
    """Longest induced path with `start` as an ENDPOINT, stopping at `cap` vertices.
    Returns (best_len, path_or_None, truncated_flag).  UNDERESTIMATE if truncated."""
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
            # the neighbours of `last` become forbidden ONLY once `last` stops being the end
            newforb = forb | g[last] | {z}
            if rec(P, newforb):
                P.pop()
                return True
            P.pop()
        return False

    rec([start], {start})
    return best[0], bestP[0], trunc[0]


# ------------------------------------------------------------------ hosts
def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def two_cycles_glued(a, b):
    E = [(i, (i + 1) % a) for i in range(a)]
    n = a
    prev = 0
    for _ in range(b - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, 0))
    return adj(n, E)


def pg2(q):
    """Incidence graph of PG(2,q), q prime: bipartite, girth 6, (q+1)-regular, a(v)=q+1."""
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


def rand_c4free(seed, n, extra):
    st = seed

    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    g = cycle(n)
    for _ in range(extra):
        u, v = nxt(n), nxt(n)
        if u == v or v in g[u]:
            continue
        if len(g[u] & g[v]) >= 1:
            continue
        g[u].add(v)
        g[v].add(u)
        if not c4_free(g):
            g[u].discard(v)
            g[v].discard(u)
    alive = set(range(len(g)))
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


def rand_c4free_dense(seed, n):
    """Seeded C4-free PROCESS: random order over all pairs, add an edge iff it keeps
    'no two vertices with two common neighbours'.  Gives mean degree ~ sqrt(n), hence
    l well above 4 for n >= ~30 — the regime the residual has never been seen in.
    Then peel a=1 vertices and keep the largest component."""
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
    """G with a C_k glued at vertex `at` (they share exactly that one vertex)."""
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
    """G — induced path of L NEW vertices — then a C_k glued at the last path vertex."""
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


# ------------------------------------------------------------------ the predicates
def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    centres = [v for v in range(n) if ecc[v] == r]
    return D, ecc, r, centres


def maximally_far(D, w, centres, r):
    """(RAD-1P)'s condition: EVERY centre is at distance exactly r from w."""
    return all(D[c][w] == r for c in centres)


def tail2_fires(g, D, ecc, w):
    """(TAIL-2) AT w.  Exhaustive over: every furthest u_d, every geodesic predecessor
    u_{d-1}, every y in N(u_d) off u_{d-1}'s component.  Returns (fires, best_a, witness)."""
    d = ecc[w]
    best = -1
    wit = None
    for ud in range(len(g)):
        if D[w][ud] != d:
            continue
        comps = nbhd_components(g, ud)
        for pred in g[ud]:
            if D[w][pred] != d - 1:
                continue
            own = next(c for c in comps if pred in c)
            for c in comps:
                if c is own:
                    continue
                for y in sorted(c):
                    ay = a_val(g, y)
                    if ay > best:
                        best = ay
                        wit = (ud, pred, y, ay)
    return (best >= 4), best, wit


def geodesic(g, D, w, ud):
    """One w->ud geodesic as a vertex list [w=u_0, ..., u_d]."""
    P = [ud]
    cur = ud
    while cur != w:
        for x in sorted(g[cur]):
            if D[w][x] == D[w][cur] - 1:
                P.append(x)
                cur = x
                break
    P.reverse()
    return P


def plus3_constructive(g, D, ecc, w):
    """Is there an ACTUAL induced path w=u_0..u_d,y,z on ecc(w)+3 vertices with w an
    endpoint, built by the (TAIL) route?  (a(y)>=4 is sufficient, NOT necessary — §42.3.)"""
    d = ecc[w]
    for ud in range(len(g)):
        if D[w][ud] != d:
            continue
        G0 = geodesic(g, D, w, ud)
        if len(G0) != d + 1 or not is_induced_path(g, G0):
            continue
        for y in sorted(g[ud]):
            if y in G0:
                continue
            P1 = G0 + [y]
            if not is_induced_path(g, P1):
                continue
            for z in sorted(g[y]):
                if z in P1:
                    continue
                P2 = P1 + [z]
                if is_induced_path(g, P2):
                    return True, P2
    return False, None


def tail2p_fires(g, D, ecc, w):
    """(TAIL-2') — the SHARPENED anchored cap-break.  Same frames as (TAIL-2), but the dodge
    list is COUNTED AT THE FRAME instead of bounded at 2: the components of G[N(y)] that must
    be avoided are u_d's own, plus one for each of u_{d-2}, u_{d-3} that actually HAS a
    neighbour in N(y).  Requirement: a(y) >= 2 + #{those}.  Every YES is certified by
    BUILDING the induced path on ecc(w)+3 vertices — no assertion without a construction.
    EVERY frame is examined (no early return), so the lemma is on trial at all of them."""
    d = ecc[w]
    out = [None]
    for ud in range(len(g)):
        if D[w][ud] != d:
            continue
        G0 = geodesic(g, D, w, ud)
        if len(G0) != d + 1 or not is_induced_path(g, G0):
            continue
        comps = nbhd_components(g, ud)
        for pred in g[ud]:
            if D[w][pred] != d - 1:
                continue
            own = next(c for c in comps if pred in c)
            for c in comps:
                if c is own:
                    continue
                for y in sorted(c):
                    if y in G0:
                        continue
                    need = sharpened_cost(g, D, w, ud, pred, y)
                    if a_val(g, y) < need:
                        continue
                    P1 = G0 + [y]
                    if not is_induced_path(g, P1):
                        continue
                    hit = None
                    for z in sorted(g[y]):
                        if z in P1:
                            continue
                        P2 = P1 + [z]
                        if is_induced_path(g, P2):
                            hit = P2
                            break
                    # the LEMMA is on trial here: the sharpened condition holds at this
                    # frame, so a legal z MUST exist.  No construction => the claim is false.
                    check(hit is not None,
                          "(TAIL-2') VIOLATED: sharpened condition held at frame "
                          "(w=%d,u_d=%d,pred=%d,y=%d,a=%d,need=%d) and NO z exists"
                          % (w, ud, pred, y, a_val(g, y), need))
                    if hit is not None and out[0] is None:
                        out[0] = ((ud, pred, y, a_val(g, y), need), hit)
    return (out[0] is not None), (out[0][0] if out[0] else None), \
           (out[0][1] if out[0] else None)


def sharpened_cost(g, D, w, ud, pred, y):
    """(TAIL-2') — the dodge list COUNTED at the frame instead of bounded at 2.
    Cost = 1 (u_d's own component) + #{j in {d-2,d-3}: N(y) meets N(u_j)} ; the claim is
    that a(y) >= cost+1 suffices for the +3 extension."""
    G0 = geodesic(g, D, w, ud)
    d = len(G0) - 1
    js = [G0[d - 2]] if d >= 2 else []
    if d >= 3:
        js.append(G0[d - 3])
    hit = sum(1 for uj in js if (g[y] & g[uj]))
    return 1 + hit + 1          # components to dodge + 1 = required a(y)


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append("PART0")
    print("=" * 78)
    print("PART 0 — PRIMITIVE SELF-CHECKS AND REGRESSION CONTROLS AGAINST r31/r32 RECORDS")
    print("=" * 78, flush=True)

    for g, nm in [(cycle(6), "C6"), (two_cycles_glued(9, 9), "C9+C9"), (pg2(2), "Heawood"),
                  (pg2(3), "PG(2,3)")]:
        check(c4_free(g) == c4_free_slow(g), "c4_free disagreement on %s" % nm)
        for v in range(len(g)):
            check(a_val(g, v) == a_val_brute(g, v), "a_val disagreement %s v%d" % (nm, v))
    print("  c4_free vs c4_free_slow, a_val vs a_val_brute: agree on 4 hosts.", flush=True)

    # CONTROL A — the planner's own r31 table, reproduced (draft §42.4).
    g = two_cycles_glued(9, 9)
    D, ecc, r, centres = profile(g)
    mf = [w for w in range(len(g)) if maximally_far(D, w, centres, r)]
    print("  C9+C9 glued: n=%d rad=%d centres=%s |maximally-far|=%d  (r31 table: r=4, unique"
          " centre = the glue, FOUR attachments at distance 4)" % (len(g), r, centres, len(mf)),
          flush=True)
    check(r == 4 and centres == [0] and len(mf) == 4,
          "C9+C9 control: expected r=4, unique centre 0, 4 maximally-far vertices")

    # CONTROL B — r32's two recorded residual instances, rebuilt from their seeds.
    for s, n0, ex, wrec, lrec in ((7, 18, 6, 11, 2.333), (30, 22, 8, 13, 2.455)):
        h = rand_c4free(s * 7919 + n0, n0, ex)
        if h is None:
            check(False, "rand(s=%d,n0=%d) failed to rebuild" % (s, n0))
            continue
        D, ecc, r, centres = profile(h)
        res = [w for w in range(len(h))
               if ecc[w] == r + 1 and maximally_far(D, w, centres, r)]
        lv = mean_a(h)
        print("  rand(s=%d,n0=%d): n=%d rad=%d l=%.3f residual w's=%s   (r32 draft §42.6: "
              "w=%d, l=%.3f)" % (s, n0, len(h), r, lv, res, wrec, lrec), flush=True)
        check(abs(lv - lrec) < 0.002, "l mismatch vs draft §42.6 for rand(s=%d)" % s)
        check(wrec in res, "draft's residual w=%d not reproduced for rand(s=%d)" % (wrec, s))

    # NEGATIVE CONTROL — a self-centred host has NO residual vertex at all.
    for g, nm in [(pg2(3), "PG(2,3)"), (pg2(5), "PG(2,5)"), (cycle(9), "C9")]:
        D, ecc, r, centres = profile(g)
        res = [w for w in range(len(g)) if ecc[w] == r + 1 and maximally_far(D, w, centres, r)]
        print("  NEG %s: rad=%d self-centred=%s residual=%d (must be 0)"
              % (nm, r, all(e == r for e in ecc), len(res)), flush=True)
        check(len(res) == 0, "negative control %s produced a residual vertex" % nm)

    # LIVENESS — the residual predicate must be able to say YES (Control B already did),
    # and tail2_fires must be able to say NO.  A predicate that cannot decline is ABSENT.
    g = cycle(9)
    D, ecc, r, centres = profile(g)
    fired, best, _ = tail2_fires(g, D, ecc, 0)
    print("  LIVENESS: tail2_fires on C9 at v0 -> fires=%s best a(y)=%d (must be False/2)"
          % (fired, best), flush=True)
    check((not fired) and best == 2, "tail2_fires liveness: C9 must decline with best a=2")


# ------------------------------------------------------------------ PART 1
def build_family():
    """Hosts chosen to make the l > 4 hypothesis LIVE.  Every one is certified below."""
    fam = []
    fam.append((pg2(3), "PG(2,3)"))
    fam.append((pg2(5), "PG(2,5)"))
    b3, b5 = pg2(3), pg2(5)
    for k in (5, 7, 9, 11, 13, 15, 17, 19, 21, 25):
        fam.append((glue_cycle(b5, 0, k), "PG(2,5)+C%d glued" % k))
        fam.append((glue_cycle(b3, 0, k), "PG(2,3)+C%d glued" % k))
    for L, k in ((1, 5), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 9), (5, 9), (6, 11)):
        fam.append((path_then_cycle(b5, 0, L, k), "PG(2,5)+P%d+C%d" % (L, k)))
    # two sparse zones on one rich core: the shape that makes BOTH far ends poor
    for k1, k2 in ((7, 7), (9, 9), (11, 11), (13, 13), (9, 11)):
        g = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g, 1, k2), "PG(2,5)+C%d@0+C%d@1" % (k1, k2)))
        g2 = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g2, 5, k2), "PG(2,5)+C%d@0+C%d@5" % (k1, k2)))
    for L in (3, 5, 7, 9, 11):
        fam.append((blob_chain(5, L), "2xPG(2,5)+P%d" % L))
        fam.append((blob_chain(3, L), "2xPG(2,3)+P%d" % L))
    # THE DENSE C4-FREE PROCESS — the only family in which l > 4 and a non-self-centred
    # radius have ever been available at the same time.  Seeded, deterministic.
    for n0 in (14, 18, 22, 26, 30, 34, 38, 44, 50):
        for s in range(1, 26):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                fam.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    # HYBRID: dense C4-free core with a SPARSE far zone glued on — the shape in which the
    # far end from a residual w could be poor while the mean stays above 4.
    for n0 in (26, 30, 34, 38, 44, 50):
        for s in (1, 2, 3, 4, 5, 6, 7, 8):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is None:
                continue
            for k in (5, 7, 9):
                fam.append((glue_cycle(h, 0, k), "dense(s=%d,n0=%d)+C%d" % (s, n0, k)))
    return fam


def part1(fam):
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 — ITEM 3: CAN THE RESIDUAL CONFIGURATION CARRY l > 4 AT ALL?")
    print("         conjunct populations, printed BEFORE any verdict (r32 §2g discipline)")
    print("=" * 78)
    print("%-26s %5s %6s %5s %7s %7s %7s %7s" %
          ("host", "n", "l", "rad", "ecc=r+1", "maxfar", "BOTH", "l>4?"), flush=True)
    rows = []
    live = []
    for g, nm in fam:
        if over():
            print("  [DEADLINE] family truncated after %d hosts — partial results stand"
                  % len(rows), flush=True)
            break
        n = len(g)
        if not connected(g) or not c4_free(g):
            print("  SKIP %s: not connected / not C4-free" % nm, flush=True)
            continue
        if min(a_val(g, v) for v in range(n)) < 2:
            print("  SKIP %s: mu < 2" % nm, flush=True)
            continue
        D, ecc, r, centres = profile(g)
        lv = mean_a(g)
        A = [w for w in range(n) if ecc[w] == r + 1]
        B = [w for w in range(n) if maximally_far(D, w, centres, r)]
        C = [w for w in A if w in B]
        rows.append((nm, n, lv, r, len(A), len(B), len(C)))
        if len(C) or not nm.startswith("dense"):
            print("%-26s %5d %6.3f %5d %7d %7d %7d %7s" %
                  (nm, n, lv, r, len(A), len(B), len(C), "YES" if lv > 4 else "no"), flush=True)
        for w in C:
            live.append((g, nm, D, ecc, r, centres, w, lv))
    nlive4 = sum(1 for e in live if e[7] > 4)
    nlive45 = sum(1 for e in live if e[7] > 4 and e[4] >= 5)
    print()
    print("  hosts certified (connected, C4-free, mu>=2): %d   (dense-process hosts are"
          " printed only when they carry a residual instance)" % len(rows))
    print("  hosts with l > 4: %d ; hosts with l > 4 AND rad >= 5: %d"
          % (sum(1 for x in rows if x[2] > 4), sum(1 for x in rows if x[2] > 4 and x[3] >= 5)))
    print("  conjunct totals over the whole family: ecc=r+1 at %d vertices, maximally-far at"
          " %d, BOTH at %d" % (sum(x[4] for x in rows), sum(x[5] for x in rows),
                               sum(x[6] for x in rows)))
    print("  RESIDUAL INSTANCES FOUND: %d   of which with l > 4: %d   of which also rad >= 5:"
          " %d" % (len(live), nlive4, nlive45), flush=True)
    print("  EXCLUSION LIST for that count: hosts are exactly the %d listed above; the family"
          % len(rows))
    print("  is DESIGNED (PG(2,q) cores + glued cycles / pendant-path+cycle / blob chains),")
    print("  NOT exhaustive; no random search, no graph enumeration.  A 0 here is a statement")
    print("  about THIS family only.", flush=True)
    return live


# ------------------------------------------------------------------ PART 2
def part2(live):
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 — ITEM 1: (TAIL-2) AT THE PRESCRIBED w ON EVERY RESIDUAL INSTANCE")
    print("=" * 78, flush=True)
    if not live:
        print("  no residual instance in PART 1's family — nothing to evaluate here.",
              flush=True)
        return []
    print("%-26s %4s %5s %6s %4s %5s %8s %8s" %
          ("host", "w", "ecc", "l", "rad", "bestA", "TAIL-2", "+3 built"), flush=True)
    out = []
    for (g, nm, D, ecc, r, centres, w, lv) in live:
        if over():
            print("  [DEADLINE] stopped after %d instances — partial results stand" % len(out),
                  flush=True)
            break
        fires, best, wit = tail2_fires(g, D, ecc, w)
        built, P = plus3_constructive(g, D, ecc, w)
        f2, wit2, P2 = tail2p_fires(g, D, ecc, w)
        if not fires:
            SHARP.append((nm, w, f2, built))
        out.append((nm, w, lv, r, ecc[w], fires, best, built, g, D, wit, P))
        if (not fires) or (not built) or len(out) <= 25:
            print("%-26s %4d %5d %6.3f %4d %5d %8s %8s" %
                  (nm, w, ecc[w], lv, r, best, "FIRES" if fires else "FAILS",
                   "yes" if built else "NO"), flush=True)
    print("  evaluated %d residual instances; (TAIL-2) FAILS on %d, +3 NOT built on %d"
          % (len(out), sum(1 for x in out if not x[5]), sum(1 for x in out if not x[7])),
          flush=True)
    print("  restricted to l > 4: %d instances, (TAIL-2) FAILS on %d, +3 NOT built on %d"
          % (sum(1 for x in out if x[2] > 4), sum(1 for x in out if x[2] > 4 and not x[5]),
             sum(1 for x in out if x[2] > 4 and not x[7])), flush=True)
    return out


# ------------------------------------------------------------------ PART 3
def part3(res):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 — WITNESS CERTIFICATES, and what the underlying REQUIREMENT does")
    print("=" * 78, flush=True)
    shown = 0
    for (nm, w, lv, r, e, fires, best, built, g, D, wit, P) in res:
        if fires and built:
            continue                      # nothing to certify: route and statement both fine
        if shown >= 4 or over():
            break
        shown += 1
        print("  WITNESS %d: host %s, w=%d" % (shown, nm, w))
        print("    n=%d  C4-free=%s  mu=%d  l=%.4f  rad=%d  ecc(w)=%d  (residual: ecc=rad+1)"
              % (len(g), c4_free(g), min(a_val(g, v) for v in range(len(g))), lv, r, e))
        print("    (TAIL-2) at w: %s  (best a(y) over EVERY furthest u_d / geodesic pred /"
              " component = %d)" % ("FIRES" if fires else "FAILS", best))
        print("    constructive +3 by the TAIL route: %s" % ("yes" if built else "NO"))
        cap = e + 3
        L, PP, tr = longest_induced_path(g, w, cap)
        print("    endpath(G,w) >= %d (cap %d, truncated=%s)  vs the requirement ecc(w)+3 = %d"
              " -> requirement %s"
              % (L, cap, tr, e + 3, "HOLDS" if L >= e + 3 else "NOT SETTLED by this run"))
        if PP is not None:
            check(is_induced_path(g, PP), "witness endpath is not induced")
            check(PP[0] == w, "witness endpath does not start at w")
        print(flush=True)
    if shown == 0:
        if not res:
            print("  NOTHING TO CERTIFY AND NOTHING CLAIMED: PART 2 evaluated ZERO residual"
                  " instances, so this part is VACUOUS, not a pass.", flush=True)
        else:
            print("  no witness to certify: on all %d residual instances evaluated, (TAIL-2)"
                  " fires AND the +3 path is built." % len(res), flush=True)

    # (TAIL-2') — the sharpened cost, measured wherever a frame exists.
    print("  (TAIL-2') sharpened dodge count vs the blanket a(y) >= 4:")
    tot = 0
    beat = 0
    for (nm, w, lv, r, e, fires, best, built, g, D, wit, P) in res:
        if wit is None or over():
            continue
        ud, pred, y, ay = wit
        need = sharpened_cost(g, D, w, ud, pred, y)
        tot += 1
        if need < 4:
            beat += 1
        print("    %-24s w=%-3d frame(u_d=%d,pred=%d,y=%d) a(y)=%d  sharpened need a(y)>=%d"
              % (nm, w, ud, pred, y, ay, need), flush=True)
    print("    frames examined: %d ; sharpened requirement STRICTLY below 4 on: %d"
          % (tot, beat), flush=True)
    print()
    print("  (TAIL-2') AS A RESCUE, measured ONLY where the blanket (TAIL-2) FAILS:")
    print("    (TAIL-2) fails at %d prescribed w's; of those, (TAIL-2') FIRES at %d"
          % (len(SHARP), sum(1 for x in SHARP if x[2])))
    print("    ... and of the %d where BOTH decline, the +3 path exists anyway at %d"
          % (sum(1 for x in SHARP if not x[2]), sum(1 for x in SHARP if not x[2] and x[3])))
    print("    every (TAIL-2') YES above was CERTIFIED BY BUILDING the induced path on"
          " ecc(w)+3 vertices; every frame where the sharpened condition held was put on"
          " trial (a missing z would have raised a FAILURE).", flush=True)


# ------------------------------------------------------------------ PART 4
def part4(live, res):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 — SUMMARY")
    print("=" * 78)
    n4 = [e for e in live if e[7] > 4]
    print("  residual instances found: %d ; with l > 4: %d" % (len(live), len(n4)))
    if res:
        fails = [x for x in res if not x[5]]
        nob = [x for x in res if not x[7]]
        print("  (TAIL-2) FAILS at the prescribed w on: %d of %d evaluated" % (len(fails), len(res)))
        print("  constructive +3 NOT built on: %d of %d evaluated" % (len(nob), len(res)))
    print("  elapsed %.1fs of a %.0fs internal deadline" % (time.time() - T0, DEADLINE),
          flush=True)


def main():
    part0()
    fam = build_family()
    live = part1(fam)
    res = part2(live)
    part3(res)
    part4(live, res)
    print()
    for p in PARTS_DECLARED:
        check(p in PARTS_RUN, "declared part %s DID NOT RUN" % p)
    print("=" * 78)
    print("CHECKS=%d  FAILURES=%d  PARTS_RUN=%s  elapsed=%.1fs"
          % (CHECKS, FAIL, PARTS_RUN, time.time() - T0))
    print("=" * 78, flush=True)
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
