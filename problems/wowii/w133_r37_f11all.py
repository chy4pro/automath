#!/usr/bin/env python3
"""
WOWII-133 round 37 -- (F11-ALL), the one live target after (MH-GAP).

Self-contained: every primitive is COPIED into this file, nothing is imported from
another round's script.  Pure stdlib -> runs on SYSTEM python3 (no networkx, no sympy).
Hard internal deadline; no SAT; the only searches are DEPTH-CAPPED anchored DFS
(cap = rad+4 vertices) and a subset-enumeration oracle restricted to n <= 13.

TARGET (draft section 42.1):
    (F11-ALL)   endpath(G,w) >= rad(G) + 4   for EVERY vertex w.

WHAT THIS FILE CERTIFIES (statements derived by hand in the round write-up):

  (TAIL-3')  the THIRD-step dodge list, COUNTED at the frame instead of bounded at 4
             -- the exact analogue of (TAIL-2') one step further out:
                 a(z) >= 2 + #{ j in {d-1,d-2,d-3,d-4} : N(z) cap N(u_j) != empty }
             suffices for endpath(G,w) >= ecc(w) + 4.
             Section 42.3's blanket a(z) >= 6 is this with all four indicators set to 1.

  (F11-STRAT) the ECCENTRICITY STRATIFICATION of (F11-ALL): at every w with
             ecc(w) >= rad+2 the target is FREE from (TAIL-1); only the near-central
             stratum {w : ecc(w) <= rad+1} can ever need work.  MEASURED here, including
             against this round's interest on self-centred hosts.

  (F11-DEG)  min_v a(v) >= 6  =>  endpath(G,w) >= ecc(w) + 4 for EVERY w, hence (F11-ALL).
             Unconditional; the proof touches a(.) only at two vertices within distance 2
             of the far end, so the hypothesis localises.

  the FREE exclusions the three proofs lean on (F1..F4), asserted frame by frame.

  a (F11-ALL) WITNESS CENSUS over round 33's host family: witness found / proved-below by a
  COMPLETE depth-capped search / undecided (truncated), each with its population.

PART 0 is a GUARD.  It DECLARES THE CLASS it claims and is tested against members of that
class it has NOT seen (doctrine: cert_w133_r35 section 5, owner r35 error 1).
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 420.0
P1_CAP = 130          # host order cap for PART 1 (frames are cheap)
P3_CAP = 130          # host order cap for PART 3 (depth-capped anchored DFS)
P4_CAP = 280          # host order cap for PART 4 (no DFS at all, only construction)
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


def c4_free_slow(g):
    """independent implementation, cross-check only: no 4-cycle as a subgraph."""
    n = len(g)
    for a, b, c, d in combinations(range(n), 4):
        for perm in ((a, b, c, d), (a, b, d, c), (a, c, b, d)):
            p, q, r, s = perm
            if q in g[p] and r in g[q] and s in g[r] and p in g[s]:
                return False
    return True


def a_val(g, v):
    """a(v) = alpha(G[N(v)]); C4-free => G[N(v)] is a matching => a = deg - #inside edges."""
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
    searches walk -- the checker's independence lives here."""
    n = len(g)
    M = [[0] * n for _ in range(n)]
    for (u, v) in edges_of(g):
        M[u][v] = 1
        M[v][u] = 1
    return M


def checker_induced_anchored(g, P, w, need, M=None):
    """Independent of every search below: shares no code path with them.
    Verifies P is an induced path, ANCHORED at w (P[0] == w), on exactly `need` vertices."""
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


# --------------------------------------------------- the anchored depth-capped search
def anchored_search(g, start, cap, node_budget=30000, defect=None):
    """Longest induced path with `start` as an ENDPOINT, STOPPING once `cap` vertices are
    reached.  Returns (best_len, path_or_None, truncated).  If truncated is False and
    best_len < cap the search was COMPLETE, so endpath(g,start) = best_len exactly.

    `defect` injects a deliberate fault -- used ONLY by PART 0's guard tests."""
    best = [0]
    bestP = [None]
    nodes = [0]
    trunc = [False]
    goal = cap - 1 if defect == "offbyone" else cap
    root = start
    if defect == "anchordrift":
        root = (start + 1) % len(g)

    def rec(P, forb):
        if len(P) > best[0]:
            best[0] = len(P)
            bestP[0] = list(P)
        if best[0] >= goal:
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
            if defect == "zerostep":
                newforb = forb | {z}
            elif defect == "lateblock" and len(P) >= 4:
                # r35's shape, faithfully: from depth 4 on it blocks only the PATH's own
                # vertices and forgets the accumulated neighbour set, so chords back to
                # earlier path vertices are admitted.  (An earlier version of this defect
                # blocked {last, z}; on a TRIANGLE-FREE host that is a no-op, which is why
                # it scored 0 everywhere -- see the round write-up.)
                newforb = set(P)
            else:
                newforb = forb | g[last] | {z}
            if rec(P, newforb):
                P.pop()
                return True
            P.pop()
        return False

    rec([root], {root})
    return best[0], bestP[0], trunc[0]


# --------------------------------------------------- INDEPENDENT oracle (guard, n <= 13)
def oracle_endpath(g, start, cap):
    """Shares no code path with anchored_search: enumerates SUBSETS containing `start`,
    then tests every ordering that begins at `start` for being an induced path.
    Affordable only for very small n; returns the largest anchored induced-path order
    found, capped at `cap`."""
    n = len(g)
    others = [v for v in range(n) if v != start]
    best = 1
    for k in range(min(cap, n), 1, -1):
        if k <= best:
            break
        found = False
        for S in combinations(others, k - 1):
            vs = (start,) + S
            # a set of k vertices supports an anchored induced path iff the induced
            # subgraph is a path with `start` as an endpoint
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
                if len(stack) > 40:
                    break
    return out


def frames(g, D, ecc, w, max_far, max_geo):
    """yields (P, ud, y): P a geodesic from w to a FARTHEST vertex ud, and y a neighbour
    of ud in a component of G[N(ud)] OTHER than u_{d-1}'s -- exactly (TAIL-1)'s frame."""
    n = len(g)
    d = ecc[w]
    if d < 3:
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
                if C is home:
                    continue
                for y in sorted(C):
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


# ------------------------------------------------------------------ PART 0
def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- THE GUARD.  CLASS DECLARED, TESTED AGAINST MEMBERS IT HAS NOT SEEN")
    print("=" * 78)
    print("CLASS CLAIMED: any ANCHORED DEPTH-CAPPED search that mis-reports the verdict")
    print("  'endpath(G,w) >= K' -- by reporting a witness that is not an induced path, is")
    print("  not anchored at w, or is short; or by blocking the wrong set at ANY depth.")
    print("GUARD = (i) an independent checker re-verifies EVERY returned witness")
    print("  (distinctness, anchoring, exact order, inducedness from a freshly built")
    print("  adjacency matrix), and (ii) on n <= 13 an independent SUBSET-ENUMERATION")
    print("  oracle recomputes the anchored value and must agree with the verdict.")
    print("UNSEEN MEMBERS USED AS THE TEST: 'offbyone' (accepts at K-1 vertices) and")
    print("  'anchordrift' (searches from the wrong root).  r34's guard was written for")
    print("  the ZERO-step defect, r35's real defect was the ONE-step defect, r36's unseen")
    print("  member was LATE-BLOCKING -- none of them is a length or an anchor defect.")
    print()
    hosts = [(cycle(6), "C6"), (theta333(), "Theta(3,3,3)"), (petersen(), "Petersen"),
             (pathgraph(5), "P5"), (cycle(9), "C9")]
    rows = []
    vdis = {"offbyone": 0, "anchordrift": 0, "zerostep": 0, "lateblock": 0}
    # TWO thresholds, and the SECOND one is the point.  At a cap the host already meets,
    # an over-permissive defect returns a genuine witness first and is INVISIBLE to both
    # halves of the guard.  CAP_HI is deliberately above what these hosts can reach.
    CAPS = (5, 7)
    for g, nm in hosts:
      for K in CAPS:
        n = len(g)
        fires_off = 0
        fires_drift = 0
        fires_zero = 0
        fires_late = 0
        false_alarm = 0
        agree = 0
        disagree = 0
        for w in range(n):
            # (i) witness checker, on each defect
            for tag in ("offbyone", "anchordrift", "zerostep", "lateblock", None):
                bl, P, tr = anchored_search(g, w, K, defect=tag)
                claims = (bl >= (K - 1 if tag == "offbyone" else K))
                good = checker_induced_anchored(g, P, w, K) if claims else True
                if tag is None:
                    if claims and not good:
                        false_alarm += 1
                elif tag == "offbyone":
                    if claims and not good:
                        fires_off += 1
                elif tag == "anchordrift":
                    if claims and not good:
                        fires_drift += 1
                elif tag == "zerostep":
                    if claims and not good:
                        fires_zero += 1
                else:
                    if claims and not good:
                        fires_late += 1
            # (ii) oracle agreement on the CORRECT search, and VERDICT disagreement on
            #      each defective one -- this is the half that catches UNDER-reporting,
            #      which a witness checker structurally cannot see.
            if n <= 13:
                bl, P, tr = anchored_search(g, w, K)
                ov = oracle_endpath(g, w, K)
                if (bl >= K) == (ov >= K):
                    agree += 1
                else:
                    disagree += 1
                for tag in ("offbyone", "anchordrift", "zerostep", "lateblock"):
                    bd, Pd, td = anchored_search(g, w, K, defect=tag)
                    goal = K - 1 if tag == "offbyone" else K
                    if (bd >= goal) != (ov >= K):
                        vdis[tag] += 1
        rows.append((nm + "@K=%d" % K, n, fires_off, fires_drift, fires_zero,
                     fires_late, false_alarm, agree, disagree))
    print("%-16s %3s %8s %8s %8s %8s %8s %7s %8s" %
          ("host", "n", "OFFBY1", "ANCHOR", "zerostep", "lateblk", "falseAL",
           "oracle=", "oracle!="))
    tot = [0] * 7
    for (nm, n, a, b, c, d, e, f, h) in rows:
        print("%-16s %3d %8d %8d %8d %8d %8d %7d %8d" % (nm, n, a, b, c, d, e, f, h))
        for i, v in enumerate((a, b, c, d, e, f, h)):
            tot[i] += v
    print("%-16s %3s %8d %8d %8d %8d %8d %7d %8d" %
          ("TOTAL", "-", tot[0], tot[1], tot[2], tot[3], tot[4], tot[5], tot[6]))
    ck(tot[4] == 0, "guard FALSE-ALARMED on the correct search")
    ck(tot[6] == 0, "oracle DISAGREED with the correct anchored search")
    ck(tot[0] > 0, "guard never fired on the UNSEEN off-by-one member")
    ck(tot[1] > 0, "guard never fired on the UNSEEN anchor-drift member")
    print()
    print("(host, cap) rows: %d = %d hosts x %d caps %s" % (len(rows), len(hosts),
          len(CAPS), str(CAPS)))
    print("rows on which the guard caught the unseen OFF-BY-ONE member: %d of %d"
          % (sum(1 for r in rows if r[2] > 0), len(rows)))
    print("rows on which the guard caught the unseen ANCHOR-DRIFT member: %d of %d"
          % (sum(1 for r in rows if r[3] > 0), len(rows)))
    print("rows on which the guard caught the known ZERO-STEP member:     %d of %d"
          % (sum(1 for r in rows if r[4] > 0), len(rows)))
    print("rows on which the guard caught the known LATE-BLOCK member:    %d of %d"
          % (sum(1 for r in rows if r[5] > 0), len(rows)))
    lo = [r for r in rows if r[0].endswith("@K=%d" % CAPS[0])]
    hi = [r for r in rows if r[0].endswith("@K=%d" % CAPS[1])]
    print("   ... at the LOW cap (%d):  %d of %d rows" %
          (CAPS[0], sum(1 for r in lo if r[5] > 0), len(lo)))
    print("   ... at the HIGH cap (%d): %d of %d rows" %
          (CAPS[1], sum(1 for r in hi if r[5] > 0), len(hi)))
    print("   THE SPLIT IS THE FINDING: a guard test run at a threshold the host ALREADY")
    print("   MEETS cannot see an over-permissive defect, because the defective search")
    print("   returns a genuine witness first.  The threshold is part of the guard.")
    print()
    print("HALF THREE OF THE GUARD -- oracle VALUE disagreement, cap raised to n so the")
    print("search computes the TRUE anchored value instead of answering a threshold:")
    vval = {"offbyone": 0, "anchordrift": 0, "zerostep": 0, "lateblock": 0, "CORRECT": 0}
    vpop = 0
    for g, nm in hosts:
        n = len(g)
        if n > 13:
            continue
        for w in range(n):
            ov = oracle_endpath(g, w, n)
            vpop += 1
            for tag in ("offbyone", "anchordrift", "zerostep", "lateblock", "CORRECT"):
                d = None if tag == "CORRECT" else tag
                bd, Pd, td = anchored_search(g, w, n, node_budget=200000, defect=d)
                if bd != ov:
                    vval[tag] += 1
    for tag in ("offbyone", "anchordrift", "zerostep", "lateblock", "CORRECT"):
        print("   %-12s value-disagreements with the oracle: %d of %d (host,w) pairs"
              % (tag, vval[tag], vpop))
    ck(vval["CORRECT"] == 0, "the CORRECT search disagrees with the oracle on a VALUE")
    ck(vval["lateblock"] > 0, "guard blind to the late-blocking member on all three halves")
    print()
    print("HALF TWO OF THE GUARD -- oracle VERDICT disagreement, per defect")
    print("(the witness checker can only see OVER-reporting with a bad witness; the")
    print(" oracle sees a wrong VERDICT in either direction):")
    for tag in ("offbyone", "anchordrift", "zerostep", "lateblock"):
        print("   %-12s verdict-disagreements with the oracle: %d" % (tag, vdis[tag]))
    print("   ratio of value-half to verdict-half detections for the late-block member:")
    print("   %d value-disagreements vs %d verdict-disagreements over the same %d pairs"
          % (vval["lateblock"], vdis["lateblock"], vpop))
    print("double-source: a_val vs a_val_brute over all these hosts' vertices:")
    n_dbl = 0
    for g, nm in hosts:
        for v in range(len(g)):
            ck(a_val(g, v) == a_val_brute(g, v), "a_val mismatch on %s v=%d" % (nm, v))
            n_dbl += 1
    print("   pairs double-sourced: %d" % n_dbl)
    print("c4_free vs c4_free_slow on the same hosts:")
    n_c4 = 0
    for g, nm in hosts:
        ck(c4_free(g) == c4_free_slow(g), "c4-free implementations disagree on %s" % nm)
        n_c4 += 1
    print("   hosts double-sourced: %d" % n_c4)


# ------------------------------------------------------------------ PART 1
def part1(fam):
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (TAIL-2') AND (TAIL-3'), CERTIFIED BY *BUILDING* THE PATH")
    print("          plus the FREE exclusions F1..F4 the proofs lean on")
    print("=" * 78)
    hosts_skipped = [0]
    fr_total = 0
    t2_fire = 0
    t2_built = 0
    t3_fire = 0
    t3_built = 0
    blanket2 = 0
    blanket3 = 0
    sharp_beats_blanket2 = 0
    sharp_beats_blanket3 = 0
    f1 = f2 = f3 = f4 = 0
    hosts_used = 0
    for g, nm in fam:
        if over():
            break
        n = len(g)
        if n > P1_CAP:
            hosts_skipped[0] += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        hosts_used += 1
        for w in range(n):
            if over():
                break
            for (P, ud, y) in frames(g, D, ecc, w, max_far=2, max_geo=1):
                fr_total += 1
                d = len(P) - 1
                # ---- F1: every z in N(y)\{u_d} is NON-adjacent to u_{d-1}  (C4-forced)
                for z in g[y]:
                    if z != ud and z != P[d - 1]:
                        if P[d - 1] in g[z]:
                            ck(False, "F1 violated on %s" % nm)
                f1 += 1
                # ---- F2: every z in N(y) is non-adjacent to and distinct from u_i, i<=d-4
                for z in g[y]:
                    for i in range(0, max(0, d - 3)):
                        if z == P[i] or P[i] in g[z]:
                            ck(False, "F2 violated on %s" % nm)
                f2 += 1
                # ---- (TAIL-2'): counted cost at y
                cost2 = 2 + dodge_count(g, P, y, (d - 2, d - 3))
                if a_val(g, y) >= 4:
                    blanket2 += 1
                if a_val(g, y) >= cost2:
                    t2_fire += 1
                    if a_val(g, y) < 4:
                        sharp_beats_blanket2 += 1
                    zs = [z for z in sorted(g[y])
                          if checker_induced_anchored(g, P + [y, z], w, d + 3, M)]
                    if zs:
                        t2_built += 1
                    else:
                        ck(False, "(TAIL-2') FIRED BUT NO z ON %s w=%d" % (nm, w))
                        continue
                    z = zs[0]
                    # ---- F3: t !~ u_d is FORCED once t !~ y and z !~ u_d
                    for t in g[z]:
                        if t != y and t not in P:
                            if ud in g[t] and y not in g[t]:
                                ck(False, "F3 violated on %s" % nm)
                    f3 += 1
                    # ---- F4: t !~ u_i and t != u_i for i <= d-5
                    for t in g[z]:
                        for i in range(0, max(0, d - 4)):
                            if t == P[i] or P[i] in g[t]:
                                ck(False, "F4 violated on %s" % nm)
                    f4 += 1
                    # ---- (TAIL-3'): counted cost at z
                    cost3 = 2 + dodge_count(g, P, z, (d - 1, d - 2, d - 3, d - 4))
                    if a_val(g, z) >= 6:
                        blanket3 += 1
                    if a_val(g, z) >= cost3:
                        t3_fire += 1
                        if a_val(g, z) < 6:
                            sharp_beats_blanket3 += 1
                        ts = [t for t in sorted(g[z])
                              if checker_induced_anchored(g, P + [y, z, t], w, d + 4, M)]
                        if ts:
                            t3_built += 1
                        else:
                            ck(False, "(TAIL-3') FIRED BUT NO t ON %s w=%d" % (nm, w))
    print("hosts entered (n <= %d):                        %d" % (P1_CAP, hosts_used))
    print("hosts skipped as too big:                        %d" % hosts_skipped[0])
    print("frames examined (geodesic, y) pairs:             %d" % fr_total)
    print("F1 free-exclusion frames asserted:               %d" % f1)
    print("F2 free-exclusion frames asserted:               %d" % f2)
    print("F3 free-exclusion frames asserted:               %d" % f3)
    print("F4 free-exclusion frames asserted:               %d" % f4)
    print()
    print("(TAIL-2') counted condition FIRES:               %d" % t2_fire)
    print("   ... and the ecc+3 path was BUILT and checked: %d" % t2_built)
    print("   section 42.3's blanket a(y)>=4 would fire:    %d" % blanket2)
    print("   frames the SHARP form wins that the blanket loses: %d" % sharp_beats_blanket2)
    print("(TAIL-3') counted condition FIRES:               %d" % t3_fire)
    print("   ... and the ecc+4 path was BUILT and checked: %d" % t3_built)
    print("   section 42.3's blanket a(z)>=6 would fire:    %d" % blanket3)
    print("   frames the SHARP form wins that the blanket loses: %d" % sharp_beats_blanket3)
    ck(t2_fire == t2_built, "(TAIL-2') fired without a constructible witness")
    ck(t3_fire == t3_built, "(TAIL-3') fired without a constructible witness")
    return fr_total


# ------------------------------------------------------------------ PART 2
def part2(fam):
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- (F11-STRAT): THE ECCENTRICITY STRATIFICATION, MEASURED")
    print("          stratum 2+ is FREE from (TAIL-1); only strata 0 and 1 can need work")
    print("=" * 78)
    s0 = s1 = s2 = 0
    s0L = s1L = s2L = 0
    s0H = s1H = s2H = 0
    hostsL = 0
    hostsH = 0
    hosts = 0
    selfc = 0
    selfcL = 0
    for g, nm in fam:
        if over():
            break
        n = len(g)
        D, ecc, r = profile(g)
        l = mean_a(g)
        hosts += 1
        rich = (l > 4.0)
        hyp = rich and r >= 5
        if rich:
            hostsL += 1
        if hyp:
            hostsH += 1
        if max(ecc) == r:
            selfc += 1
            if rich:
                selfcL += 1
        for w in range(n):
            k = ecc[w] - r
            if k == 0:
                s0 += 1
                if rich:
                    s0L += 1
                if hyp:
                    s0H += 1
            elif k == 1:
                s1 += 1
                if rich:
                    s1L += 1
                if hyp:
                    s1H += 1
            else:
                s2 += 1
                if rich:
                    s2L += 1
                if hyp:
                    s2H += 1
    tot = s0 + s1 + s2
    totL = s0L + s1L + s2L
    totH = s0H + s1H + s2H
    print("POPULATION: %d hosts; %d with l > 4; %d with l > 4 AND rad >= 5"
          % (hosts, hostsL, hostsH))
    print("self-centred hosts: %d of %d   (of the l>4 hosts: %d)" % (selfc, hosts, selfcL))
    print()
    print("%-34s %9s %9s %9s %9s" % ("stratum (ecc - rad)", "ALL", "l>4", "l>4&r>=5", "%ALL"))
    for nm, a, b, c in (("0  needs +4 at w  (TAIL-2'+3')", s0, s0L, s0H),
                        ("1  needs +3 at w  (TAIL-2')", s1, s1L, s1H),
                        ("2+ FREE from (TAIL-1)", s2, s2L, s2H)):
        pct = (100.0 * a / tot) if tot else 0.0
        print("%-34s %9d %9d %9d %8.1f%%" % (nm, a, b, c, pct))
    print("%-34s %9d %9d %9d" % ("TOTAL vertices", tot, totL, totH))
    if totL:
        print()
        print("AGAINST THIS ROUND'S INTEREST -- share of the l>4 vertices that (TAIL-1)")
        print("already settles: %.1f%% ; share still needing an extension: %.1f%%"
              % (100.0 * s2L / totL, 100.0 * (s0L + s1L) / totL))
    return (s0, s1, s2, hostsH)


# ------------------------------------------------------------------ PART 3
def part3(fam):
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- (F11-ALL) WITNESS CENSUS: is there an anchored induced path on")
    print("          rad+4 vertices at EVERY vertex?  witness / proved-below / undecided")
    print("=" * 78)
    found = 0
    below = 0
    undec = 0
    below_rows = []
    hosts = 0
    hosts_rich = 0
    hosts_hyp = 0
    verts_hyp = 0
    skipped_big = 0
    for g, nm in fam:
        if over():
            break
        n = len(g)
        if n > P3_CAP:
            skipped_big += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        l = mean_a(g)
        hosts += 1
        if l > 4.0:
            hosts_rich += 1
            if r >= 5:
                hosts_hyp += 1
                verts_hyp += n
        cap = r + 4
        for w in range(n):
            if over():
                break
            bl, P, tr = anchored_search(g, w, cap, node_budget=20000)
            if bl >= cap:
                ck(checker_induced_anchored(g, P, w, cap, M),
                   "witness failed the independent checker on %s w=%d" % (nm, w))
                found += 1
            elif not tr:
                below += 1
                below_rows.append((nm, n, w, r, l, bl, ecc[w]))
            else:
                undec += 1
    print("hosts entered (n <= %d):           %d" % (P3_CAP, hosts))
    print("hosts skipped as too big:           %d" % skipped_big)
    print("  of the hosts ENTERED, with l > 4:              %d" % hosts_rich)
    print("  of the hosts ENTERED, with l > 4 AND rad >= 5: %d   (%d vertices)"
          % (hosts_hyp, verts_hyp))
    print("  ^^ THIS is the population the 'no counterexample' line below is about.")
    print("(host,w) with a rad+4 WITNESS:      %d" % found)
    print("(host,w) PROVED BELOW rad+4:        %d   (complete depth-capped search)" % below)
    print("(host,w) UNDECIDED (truncated):     %d" % undec)
    print()
    inhyp = [row for row in below_rows if row[4] > 4.0 and row[3] >= 5]
    rich = [row for row in below_rows if row[4] > 4.0]
    print("of the PROVED-BELOW instances, how many satisfy F11's own hypotheses?")
    print("   with l > 4:                      %d" % len(rich))
    print("   with l > 4 AND rad >= 5:         %d" % len(inhyp))
    if below_rows:
        lmax = max(row[4] for row in below_rows)
        rmax = max(row[3] for row in below_rows)
        print("   largest l among them:            %.3f" % lmax)
        print("   largest rad among them:          %d" % rmax)
        print()
        print("   a sample of the failing configurations:")
        print("   %-24s %4s %4s %4s %7s %8s %6s" %
              ("host", "n", "w", "rad", "l", "endpath", "ecc"))
        seen = set()
        shown = 0
        for (hn, n, w, r, l, bl, e) in below_rows:
            if hn in seen:
                continue
            seen.add(hn)
            print("   %-24s %4d %4d %4d %7.3f %8d %6d" % (hn, n, w, r, l, bl, e))
            shown += 1
            if shown >= 8:
                break
    ck(True, "part3 completed")
    return found, below, undec, len(inhyp)


# ------------------------------------------------------------------ PART 4
def part4(fam):
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- (F11-DEG): min_v a(v) >= 6  =>  endpath(G,w) >= ecc(w)+4 for EVERY w")
    print("          hosts satisfying the hypothesis, and the conclusion BUILT at every w")
    print("=" * 78)
    hosts_in = 0
    verts_in = 0
    built = 0
    missed = 0
    hosts_out = 0
    names = []
    ctrl_hosts = 0
    ctrl_verts = 0
    ctrl_built = 0
    mu_hist = {}
    # the family's own hosts are all min a(v) < 6 (the cycles glued on carry a = 2), so the
    # hypothesis would be EMPTY on it -- r33's pass-by-emptiness defect.  The incidence
    # graphs of PG(2,q) are the natural live members: a(v) = q+1 at every vertex.
    pool = list(fam) + [(pg2(5), "PG(2,5)"), (pg2(7), "PG(2,7)"), (pg2(11), "PG(2,11)")]
    for g, nm in pool:
        if over():
            break
        n = len(g)
        if n > P4_CAP:
            continue
        mu = min(a_val(g, v) for v in range(n))
        mu_hist[mu] = mu_hist.get(mu, 0) + 1
        if mu < 6:
            hosts_out += 1
            if mu >= 4 and n <= 70:
                # CONTROL: just outside the hypothesis -- does the conclusion still hold?
                D, ecc, r = profile(g)
                M = incidence_matrix(g)
                ctrl_hosts += 1
                for w in range(n):
                    if over():
                        break
                    ctrl_verts += 1
                    ok = False
                    for (P, ud, y) in frames(g, D, ecc, w, max_far=2, max_geo=1):
                        d = len(P) - 1
                        for z in sorted(g[y]):
                            if not checker_induced_anchored(g, P + [y, z], w, d + 3, M):
                                continue
                            if any(checker_induced_anchored(g, P + [y, z, t], w, d + 4, M)
                                   for t in sorted(g[z])):
                                ok = True
                                break
                        if ok:
                            break
                    if ok:
                        ctrl_built += 1
            continue
        D, ecc, r = profile(g)
        M = incidence_matrix(g)
        hosts_in += 1
        names.append(nm)
        for w in range(n):
            if over():
                break
            verts_in += 1
            need = ecc[w] + 4
            ok = False
            for (P, ud, y) in frames(g, D, ecc, w, max_far=2, max_geo=1):
                d = len(P) - 1
                zs = [z for z in sorted(g[y])
                      if checker_induced_anchored(g, P + [y, z], w, d + 3, M)]
                for z in zs:
                    ts = [t for t in sorted(g[z])
                          if checker_induced_anchored(g, P + [y, z, t], w, d + 4, M)]
                    if ts:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                built += 1
            else:
                missed += 1
                ck(False, "(F11-DEG) hypothesis held but ecc+4 NOT BUILT on %s w=%d"
                   % (nm, w))
    print("pool: the certified family PLUS PG(2,5), PG(2,7), PG(2,11)")
    print("min a(v) histogram over the pool (n <= %d): %s"
          % (P4_CAP, ", ".join("a=%d:%d" % (k, mu_hist[k]) for k in sorted(mu_hist))))
    print("hosts with min a(v) >= 6:            %d" % hosts_in)
    print("hosts outside the hypothesis:        %d" % hosts_out)
    print("vertices tested inside it:           %d" % verts_in)
    print("ecc(w)+4 anchored path BUILT:        %d" % built)
    print("NOT built (would refute (F11-DEG)):  %d" % missed)
    if names:
        print("host names inside the hypothesis: %s" % ", ".join(names[:8]))
    print()
    print("CONTROL -- hosts JUST OUTSIDE the hypothesis (4 <= min a(v) <= 5, n <= 70):")
    print("   hosts %d, vertices %d, ecc(w)+4 still BUILT at %d of them"
          % (ctrl_hosts, ctrl_verts, ctrl_built))
    print("   (F11-DEG) is therefore SUFFICIENT and visibly NOT necessary.")
    ck(missed == 0, "(F11-DEG) failed somewhere")
    ck(hosts_in > 0, "(F11-DEG) certified on an EMPTY hypothesis class")
    return hosts_in, verts_in, built


# ------------------------------------------------------------------ PART 5
def part5():
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- LIVENESS: (F11-ALL) IS FALSIFIABLE ON THIS MACHINERY")
    print("          (a census that cannot fail measures nothing -- r33's pass-by-emptiness)")
    print("=" * 78)
    neg = [(cycle(6), "C6"), (cycle(9), "C9"), (theta333(), "Theta(3,3,3)"),
           (petersen(), "Petersen"), (cycle(12), "C12")]
    fails = 0
    tested = 0
    print("%-14s %4s %4s %7s %9s %9s %8s" %
          ("host", "n", "rad", "l", "min end", "rad+4", "F11-ALL?"))
    for g, nm in neg:
        n = len(g)
        D, ecc, r = profile(g)
        l = mean_a(g)
        cap = r + 4
        mn = min(anchored_search(g, w, cap, node_budget=20000)[0] for w in range(n))
        holds = mn >= cap
        tested += 1
        if not holds:
            fails += 1
        print("%-14s %4d %4d %7.3f %9d %9d %8s" % (nm, n, r, l, mn, cap, "yes" if holds else "NO"))
    print()
    print("hosts on which (F11-ALL) FAILS: %d of %d  -- the predicate is LIVE" % (fails, tested))
    print("all of them carry l <= 4 and are OUTSIDE F11's hypotheses, so no counterexample")
    print("to F11 or to (F11-ALL)-under-hypotheses is claimed here.")
    ck(fails > 0, "no falsifying host found: the (F11-ALL) test may be vacuous")


# ------------------------------------------------------------------ main
def main():
    print("WOWII-133 round 37 -- (F11-ALL)")
    print("interpreter:", sys.version.split()[0], "(system python3; pure stdlib)")
    print("hard internal deadline (s):", DEADLINE)
    part0()
    fam = build_family()
    cert = []
    skip_c4 = 0
    skip_mu = 0
    skip_con = 0
    for g, nm in fam:
        if not connected(g):
            skip_con += 1
            continue
        if not c4_free(g):
            skip_c4 += 1
            continue
        if min(a_val(g, v) for v in range(len(g))) < 2:
            skip_mu += 1
            continue
        cert.append((g, nm))
    print()
    print("FAMILY (round 33's, rebuilt here): generated %d, CERTIFIED %d"
          % (len(fam), len(cert)))
    print("  skipped: disconnected %d, not C4-free %d, min a(v) < 2 %d"
          % (skip_con, skip_c4, skip_mu))
    print("  EXCLUSIONS: designed families plus a seeded C4-free process; NOT exhaustive,")
    print("  no random trawl beyond the recorded seeds, order capped by the generators.")
    part1(cert)
    part2(cert)
    part3(cert)
    part4(cert)
    part5()
    print()
    print("=" * 78)
    print("PARTS RUN:", ",".join(PARTS_RUN))
    print("CHECKS:", CHECKS, " FAILURES:", FAILS)
    print("elapsed (s): %.1f" % (time.time() - T0))
    print("EXIT=%d" % (1 if FAILS else 0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
