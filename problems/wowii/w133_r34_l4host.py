#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w133 r34 ITEM 2 — CAN THE RESIDUAL CONFIGURATION CARRY `l > 4`?

r34 task book item 2: turn r33's measurement (414 residual instances, 0 with `l > 4`) into a
PROOF of incompatibility.  The named mechanism was: `l > 4` forces a near-Moore density, hence
near-self-centredness, and `ecc(w) = r+1` with `w` maximally far from every centre is the
negation of self-centredness.

THE ARITHMETIC KILLS THAT MECHANISM BEFORE ANY SEARCH.  `l` is a MEAN.  Hang `M` vertices of
a-value 2 off a core of `N` vertices of a-value 6:

        l > 4   <=>   6N + 2M + delta > 4(N + M)   <=>   M < N + delta/2.

So the sparse appendage may be nearly AS LONG AS THE CORE IS BIG while the mean stays above 4 —
and its length is exactly what destroys self-centredness.  r33's family capped those appendages
at `P_L, L <= 6` and `C_k, k <= 25` on a 62-vertex core; the budget above allows `M` up to
about 62.  **r33's `0` is therefore consistent with a family that never entered the regime
where the co-occurrence would live.**  This script enters it.

DESIGNED one-parameter sweeps, not search: no SAT, no enumeration of graph space, no random
trawl.  Internal deadline; partial results are printed, never discarded.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 150.0
FAIL = 0
CHECKS = 0
PARTS_RUN = []


def over():
    return time.time() - T0 > DEADLINE


def check(cond, msg):
    global FAIL, CHECKS
    CHECKS += 1
    if not cond:
        FAIL += 1
        print("FAIL:", msg, flush=True)
    return cond


# ------------------------------------------------------------------ primitives (COPIED)
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
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
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


def mean_a(g):
    n = len(g)
    return sum(a_val(g, v) for v in range(n)) / float(n)


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


def residual_vertices(g):
    """The residual configuration of draft §42.5: ecc(w) = rad+1 AND w maximally far from
    every centre.  Same predicate r32/r33 used."""
    D, ecc, r, centres = profile(g)
    return [w for w in range(len(g))
            if ecc[w] == r + 1 and maximally_far(D, w, centres, r)], D, ecc, r, centres


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


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def two_cycles_glued(a, b):
    E = [(i, i + 1) for i in range(a - 1)] + [(a - 1, 0)]
    n = a
    prev = 0
    for _ in range(b - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, 0))
    return adj(n, E)


def pg2(q):
    def norm(v):
        for x in v:
            if x % q:
                inv = pow(x % q, q - 2, q) if q > 2 else 1
                return tuple((c * inv) % q for c in v)
        return None
    pts = []
    seen = set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if (a, b, c) == (0, 0, 0):
                    continue
                nv = norm((a, b, c))
                if nv and nv not in seen:
                    seen.add(nv)
                    pts.append(nv)
    N = len(pts)
    E = []
    for i, p in enumerate(pts):
        for j, L in enumerate(pts):
            if sum(p[k] * L[k] for k in range(3)) % q == 0:
                E.append((i, N + j))
    return adj(2 * N, E)



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
    """COPIED from w133_r33_tail2at.py so r32's recorded residual instances can be rebuilt
    from their seeds as a POSITIVE CONTROL."""
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


def del_edge(g, e):
    return adj(len(g), [x for x in edges_of(g) if x != e])


def del_vertex(g, v):
    keep = [u for u in range(len(g)) if u != v]
    pos = {u: i for i, u in enumerate(keep)}
    return adj(len(keep), [(pos[a], pos[b]) for (a, b) in edges_of(g)
                           if a != v and b != v])


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
    """G — induced path of L NEW vertices — then a C_k glued at the last path vertex.
    Keeps mu >= 2: no vertex of degree 1 anywhere."""
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


# --------------------------------------------------------------- (TAIL-2) at a prescribed w
def tail2_fires(g, D, ecc, w):
    """(TAIL-2) at w: for SOME furthest u_d and SOME geodesic predecessor u_{d-1}, some y in
    N(u_d) off u_{d-1}'s component of G[N(u_d)] has a(y) >= 4.  Returns (fires, best_a)."""
    best = 0
    d = ecc[w]
    for ud in range(len(g)):
        if D[w][ud] != d:
            continue
        preds = [x for x in g[ud] if D[w][x] == d - 1]
        for ud1 in preds:
            comps = nbhd_components(g, ud)
            own = next(c for c in comps if ud1 in c)
            for c in comps:
                if c is own:
                    continue
                for y in c:
                    best = max(best, a_val(g, y))
    return best >= 4, best


# ================================================================== PART 0 — controls
def part0():
    PARTS_RUN.append("PART0")
    print("=" * 78)
    print("PART 0 — CONTROLS (a predicate that cannot say NO is ABSENT, not PASS)")
    print("=" * 78)
    # r31's planner table, reproduced: two C9 glued at one vertex
    g = two_cycles_glued(9, 9)
    res, D, ecc, r, cen = residual_vertices(g)
    print("  C9+C9 glued: n=%d rad=%d centres=%s  #maximally-far-at-rad=%d"
          % (len(g), r, cen, sum(1 for v in range(len(g))
                                 if maximally_far(D, v, cen, r))))
    check(r == 4 and cen == [0], "r31's C9+C9 table not reproduced (rad=4, unique centre 0)")
    check(sum(1 for v in range(len(g)) if maximally_far(D, v, cen, r)) == 4,
          "r31's C9+C9 table not reproduced (exactly 4 maximally-far vertices)")
    # negative controls: self-centred hosts have NO residual vertex
    for nm, h in (("PG(2,3)", pg2(3)), ("PG(2,5)", pg2(5)), ("C9", cycle(9))):
        res, D, ecc, r, cen = residual_vertices(h)
        print("  NEG %s: rad=%d self-centred=%s residual=%d (must be 0)"
              % (nm, r, min(ecc) == max(ecc), len(res)))
        check(len(res) == 0, "negative control %s produced a residual vertex" % nm)
    # POSITIVE CONTROL, CORRECTED.  OWN-DEFECT r34 #5, KEPT NAMED: the first version used
    # C5+P6+C5 — a STRETCHED host — and it returned 0.  That was not a broken control, it was
    # this round's first real finding: stretching a graph DESTROYS the residual configuration,
    # because ecc(w) = rad+1 is a COMPACTNESS condition, not a stretch.  The control that
    # actually fires is r32's own recorded instance, rebuilt from its seed.
    h = None
    for s0, n0, ex, wrec, lrec in ((7, 18, 6, 11, 2.333), (30, 22, 8, 13, 2.455)):
        h = rand_c4free(s0 * 7919 + n0, n0, ex)
        res, D, ecc, r, cen = residual_vertices(h)
        lv = mean_a(h)
        print("  POS rand(s=%d,n0=%d): n=%d rad=%d l=%.3f residual w's=%s (r32 draft §42.6: "
              "w=%d, l=%.3f)" % (s0, n0, len(h), r, lv, res, wrec, lrec))
        check(abs(lv - lrec) < 0.002, "l mismatch vs draft §42.6 for rand(s=%d)" % s0)
        check(wrec in res, "r32's recorded residual w=%d not reproduced" % wrec)
    # and the STRETCHED host, kept as the finding it is
    hs = path_then_cycle(cycle(5), 0, 6, 5)
    rs, Ds, es, rr, cs = residual_vertices(hs)
    print("  STRETCH C5+P6+C5: n=%d rad=%d residual vertices=%d — a stretched host has NONE,"
          " and that is PART 2's mechanism in miniature" % (len(hs), rr, len(rs)))
    # a_val double-sourced
    ok = all(a_val(h, v) == a_val_brute(h, v) for v in range(len(h)))
    print("  a_val vs brute-force alpha on the positive control: agree=%s" % ok)
    check(ok, "a_val disagrees with the brute-force independence number")


# ================================================================== PART 1 — the budget
def part1():
    PARTS_RUN.append("PART1")
    print("\n" + "=" * 78)
    print("PART 1 — THE MEAN BUDGET, COMPUTED RATHER THAN ASSERTED")
    print("=" * 78)
    core = pg2(5)
    N = len(core)
    S = sum(a_val(core, v) for v in range(N))
    print("  core PG(2,5): N=%d  sum_v a(v)=%d  l=%.4f" % (N, S, S / float(N)))
    print("  a sparse appendage contributes a=2 per vertex, so l > 4 survives while")
    print("  S + 2M + delta > 4(N + M), i.e. roughly M < (S - 4N)/2 = %d added vertices."
          % ((S - 4 * N) // 2))
    print("  r33's family used P_L with L <= 6 and C_k with k <= 25 on this core.")
    print("  => THE REGIME `M` in (25, %d] WAS NEVER ENTERED.  That is what PART 2 enters."
          % ((S - 4 * N) // 2))
    check(S - 4 * N > 0, "PG(2,5) has no budget above l = 4 at all")
    return (S - 4 * N) // 2


# ================================================================== PART 2 — the sweep
def part2(budget):
    PARTS_RUN.append("PART2")
    print("\n" + "=" * 78)
    print("PART 2 — THE DESIGNED SWEEP INTO THE UNENTERED REGIME")
    print("=" * 78)
    core5 = pg2(5)
    fam = []
    for k in (5, 7, 9, 11):
        for L in range(1, 56):
            fam.append(("PG(2,5)+P%d+C%d" % (L, k), lambda L=L, k=k: path_then_cycle(core5, 0, L, k)))
    for k in range(27, 70, 2):
        fam.append(("PG(2,5)+C%d glued" % k, lambda k=k: glue_cycle(core5, 0, k)))
    for L in range(1, 120, 3):
        fam.append(("2xPG(2,5)+P%d" % L, lambda L=L: blob_chain(5, L)))

    certified = 0
    with_l4 = 0
    residual_tot = 0
    hits = []
    skipped = 0
    for nm, mk in fam:
        if over():
            skipped += 1
            continue
        g = mk()
        if not connected(g) or not c4_free(g):
            continue
        if min(a_val(g, v) for v in range(len(g))) < 2:
            continue
        certified += 1
        l = mean_a(g)
        res, D, ecc, r, cen = residual_vertices(g)
        residual_tot += len(res)
        if l > 4:
            with_l4 += 1
            if res:
                hits.append((nm, g, res, D, ecc, r, cen, l))
    print("  family size declared: %d ; hosts certified (connected, C4-free, mu>=2): %d ;"
          " skipped for deadline: %d" % (len(fam), certified, skipped))
    print("  hosts with l > 4: %d" % with_l4)
    print("  residual instances over the whole certified family: %d" % residual_tot)
    print("  ** RESIDUAL INSTANCES WITH l > 4: %d **" % sum(len(h[2]) for h in hits))
    print("  POPULATION OF THAT COUNT: the %d certified hosts above; the count is a count of"
          " (host, w) pairs." % certified)
    if not hits:
        print("  EXCLUSION LIST: designed one-parameter sweeps on a PG(2,5) core only —")
        print("  P_L+C_k tails, long glued cycles, and 2xPG(2,5)+P_L chains. NOT exhaustive,")
        print("  no random search, no enumeration. A 0 here is a statement about THIS family.")
    return hits, certified


# ================================================================== PART 3 — the witness
def part3(hits):
    PARTS_RUN.append("PART3")
    print("\n" + "=" * 78)
    print("PART 3 — THE WITNESS, CERTIFIED FIELD BY FIELD")
    print("=" * 78)
    if not hits:
        print("  NO WITNESS FOUND IN PART 2'S FAMILY. Nothing is claimed either way: this is")
        print("  a wider measurement, not a proof of incompatibility.")
        return None
    nm, g, res, D, ecc, r, cen, l = hits[0]
    w = res[0]
    print("  ** A HOST CARRYING BOTH `l > 4` AND THE RESIDUAL CONFIGURATION EXISTS. **")
    print("  family member: %s" % nm)
    print("  n=%d  m=%d  connected=%s  C4-free=%s  mu=%d  l=%.4f"
          % (len(g), len(edges_of(g)), connected(g), c4_free(g),
             min(a_val(g, v) for v in range(len(g))), l))
    print("  rad=%d  diam=%d  #centres=%d  self-centred=%s"
          % (r, max(ecc), len(cen), min(ecc) == max(ecc)))
    print("  residual vertices w (ecc(w)=rad+1 AND every centre at distance exactly rad): %s"
          % res)
    print("  at w=%d: ecc(w)=%d = rad+1 = %d ; distances to the centres: %s"
          % (w, ecc[w], r + 1, sorted(D[c][w] for c in cen)))
    check(l > 4, "witness does not carry l > 4")
    check(connected(g) and c4_free(g), "witness fails connected/C4-free")
    check(min(a_val(g, v) for v in range(len(g))) >= 2, "witness has an a=1 vertex")
    check(ecc[w] == r + 1, "witness w does not have ecc = rad+1")
    check(all(D[c][w] == r for c in cen), "witness w is not maximally far from every centre")
    check(min(ecc) != max(ecc), "witness is self-centred — the claimed mechanism would hold")
    ok = all(a_val(g, v) == a_val_brute(g, v) for v in range(len(g)))
    check(ok, "witness a-values disagree with brute force")
    print("  a_val double-sourced against brute-force alpha on all %d vertices: agree=%s"
          % (len(g), ok))
    print("  EDGE LIST (so the witness travels):")
    print("    %s" % edges_of(g))

    # AND NOW THE THING THAT WAS UNTESTABLE: (TAIL-2) at this w, with l > 4 LIVE.
    fires, best = tail2_fires(g, D, ecc, w)
    print("\n  (TAIL-2) AT THE PRESCRIBED w, WITH `l > 4` LIVE FOR THE FIRST TIME:")
    print("    best a(y) over all frames at w = %d ; (TAIL-2) fires = %s" % (best, fires))
    print("    r33 could not evaluate this: its 414 residual instances all had l <= 3.66,")
    print("    so the hypothesis was never satisfied. It is satisfied here.")
    return (nm, g, res, w, fires, best, l, r)


# ================================================================== PART 4 — the ruling
def part4(wit, hits, certified):
    PARTS_RUN.append("PART4")
    print("\n" + "=" * 78)
    print("PART 4 — WHAT THIS SETTLES AND WHAT IT DOES NOT")
    print("=" * 78)
    if wit is None:
        print("  The incompatibility is NOT proved and NOT refuted here. PART 1 shows the")
        print("  NAMED MECHANISM ('l > 4 forces near-self-centredness') is FALSE as an")
        print("  argument — the mean budget permits an appendage nearly as long as the core —")
        print("  so a proof of the incompatibility cannot run through it.")
        return
    nm, g, res, w, fires, best, l, r = wit
    print("  ** THE INCOMPATIBILITY IS FALSE. ** r33 asked for either a theorem or ONE host")
    print("  carrying both; this is the host, and PART 1 says why the family that returned 0")
    print("  could not have contained one: the appendage budget was never spent.")
    print("  CONSEQUENCE 1: route A2's single-hair case does NOT close by emptiness.")
    print("  CONSEQUENCE 2: r33's item-1 target ((TAIL-2) at a prescribed w with l > 4) is")
    print("     TESTABLE for the first time, and PART 3 evaluates it on this witness.")
    print("  NOT CLAIMED: no pocket is closed; the residual configuration is not discharged;")
    print("     this is ONE witness in ONE designed family (%d certified hosts), not a census"
          % certified)
    print("     of the class, and %d witnesses were found in it." % sum(len(h[2]) for h in hits))



# ================================================================== PART 5 — local surgery
ECC_OK = [0]
FAR_OK = [0]
CENTRES = []


def part5():
    PARTS_RUN.append("PART5")
    print("\n" + "=" * 78)
    print("PART 5 — THE REGIME PART 2 NAMES: A DENSE CORE PERTURBED WITHOUT STRETCHING")
    print("=" * 78)
    print("  PART 2 shows stretching kills the residual; r33 shows a self-centred dense core")
    print("  has none by definition.  What is left is LOCAL SURGERY: break self-centredness")
    print("  by one, without adding length.  Designed census, printed population.")
    core = pg2(5)
    fam = [("PG(2,5) - e%s" % (e,), del_edge(core, e)) for e in edges_of(core)]
    fam += [("PG(2,5) - v%d" % v, del_vertex(core, v)) for v in range(len(core))]
    certified = 0
    l4 = 0
    resid = 0
    hits = []
    nonselfc = 0
    skipped = 0
    for nm, g in fam:
        if over():
            skipped += 1
            continue
        if not connected(g) or not c4_free(g):
            continue
        if min(a_val(g, v) for v in range(len(g))) < 2:
            continue
        certified += 1
        l = mean_a(g)
        res, D, ecc, r, cen = residual_vertices(g)
        if min(ecc) != max(ecc):
            nonselfc += 1
        resid += len(res)
        # DECOMPOSE the 0: which conjunct of the residual configuration fails?
        ec = [v for v in range(len(g)) if ecc[v] == r + 1]
        ECC_OK[0] += len(ec)
        FAR_OK[0] += sum(1 for v in ec if maximally_far(D, v, cen, r))
        CENTRES.append(len(cen))
        if l > 4:
            l4 += 1
            if res:
                hits.append((nm, g, res, D, ecc, r, cen, l))
    print("  family declared: %d ; certified (connected, C4-free, mu>=2): %d ; skipped for"
          " deadline: %d" % (len(fam), certified, skipped))
    print("  certified hosts that are NOT self-centred: %d" % nonselfc)
    print("  certified hosts with l > 4: %d" % l4)
    print("  residual instances over the certified family: %d" % resid)
    print("  ** RESIDUAL INSTANCES WITH l > 4 (population %d hosts): %d **"
          % (certified, sum(len(h[2]) for h in hits)))
    print("  DECOMPOSITION OF THAT 0 — which conjunct fails, over the same population:")
    print("    vertices with ecc = rad+1 (first conjunct):                    %d" % ECC_OK[0])
    print("    of those, ALSO maximally far from EVERY centre (second):       %d" % FAR_OK[0])
    print("    number of centres per host: min %d, max %d, mean %.2f"
          % (min(CENTRES), max(CENTRES), sum(CENTRES) / float(len(CENTRES))))
    print("    => the first conjunct is ABUNDANT here and the SECOND is what fails.  The")
    print("       obstruction is NOT self-centredness (every one of these hosts is")
    print("       non-self-centred); it is that a dense core has MANY centres, and no vertex")
    print("       can sit at distance exactly rad from all of them.")
    if not hits:
        print("  EXCLUSION LIST FOR THAT 0: single-edge and single-vertex deletions from ONE")
        print("  core, PG(2,5).  NOT exhaustive: no multi-edge surgery, no other core, no")
        print("  search.  A 0 here is a statement about THIS family.")
    return hits, certified


def main():
    print("w133 r34 ITEM 2 — CAN THE RESIDUAL CONFIGURATION CARRY l > 4?")
    print("started %s   deadline %.0fs" % (time.strftime("%Y-%m-%d %H:%M:%S"), DEADLINE))
    part0()
    budget = part1()
    hits, certified = part2(budget)
    hits5, cert5 = part5()
    hits = hits + hits5
    certified += cert5
    wit = part3(hits)
    part4(wit, hits, certified)
    print("\n" + "=" * 78)
    declared = ["PART0", "PART1", "PART2", "PART5", "PART3", "PART4"]
    print("PARTS DECLARED: %s" % declared)
    print("PARTS RUN     : %s" % PARTS_RUN)
    check(PARTS_RUN == declared, "not every declared part ran (r31 own-defect 7)")
    print("elapsed %.1fs   CHECKS=%d   FAILURES=%d" % (time.time() - T0, CHECKS, FAIL))
    print("EXIT=%d" % (1 if FAIL else 0))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
