#!/usr/bin/env python3
"""WOWII-133 round 43 slice 2 -- THE COVER ON THE NEW CASE A INSTANCES, AND A SMALLER WITNESS.

Slice 1 (`w133_r43_caseA.py`) showed draft 42.4's residual row is non-empty in BOTH halves:
`W43a` (n = 420, l = 4.9952, rad 5, diam 6, |Ctr| = 1, 128 condition-4 vertices) and `W43b`.
Two things follow immediately and neither is cosmetic.

  PART A  THE ONLY QUESTION THAT CAN STILL BREAK WOWII-133 ON THIS ROW.  (TAIL-2)/(B2) covers
          an instance when endpath(G,w) >= ecc(w)+3.  Round 42 built such a path on all 146
          CASE B instances; round 41 found six rad = 2 instances where the cover FAILS, so it
          is not automatic.  `W43a` carries 128 condition-4 vertices on ONE host -- the first
          CASE A population big enough to test the cover on.  A BUILT path is a LOWER bound;
          a failure to build is a FAILURE TO BUILD, never a shortfall.
  PART B  `W43a` is sampler output at n = 420.  How small can an instance of conditions 1-5
          be made?  Note first that the degree cap 4 caps l at 4 EXACTLY (l = mean a(.) and
          a(v) <= deg(v)), so condition 5 (l > 4) needs cap >= 5: the frontier is not free.

Self-contained; primitives COPIED from slice 1, never imported.  Interpreter: system python3.
No SAT.  Every path is BUILT and then CHECKED; no exhaustive longest-path search anywhere.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 1500.0
CHECKS = 0
FAILS = 0


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


def over():
    return (time.time() - T0) > DEADLINE


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


def a_val_matching(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def l_of(g):
    return sum(a_val_matching(g, v) for v in range(len(g))) / float(len(g))


def profile(g):
    D = [bfs(g, v) for v in range(len(g))]
    ecc = [max(d) for d in D]
    return D, ecc, min(ecc)


def centre_of(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] == r]


def far_intersection(D, ecc, r):
    C = centre_of(ecc, r)
    return [w for w in range(len(ecc)) if all(D[c][w] == r for c in C)]


def rand_c4free_sparse(seed, n, cap):
    st = seed % (1 << 31)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for i in range(len(pairs) - 1, 0, -1):
        st = (st * 1103515245 + 12345) % (1 << 31)
        j = st % (i + 1)
        pairs[i], pairs[j] = pairs[j], pairs[i]
    g = [set() for _ in range(n)]
    for (u, v) in pairs:
        if len(g[u]) >= cap or len(g[v]) >= cap:
            continue
        if len(g[u] & g[v]) >= 1:
            continue
        if any(len(g[u] & g[x]) >= 1 for x in g[v] if x != u):
            continue
        if any(len(g[v] & g[y]) >= 1 for y in g[u] if y != v):
            continue
        g[u].add(v)
        g[v].add(u)
    h = adj(n, [(u, v) for u in range(n) for v in g[u] if u < v])
    return h if connected(h) else None


def is_anchored_induced_path(g, P, w):
    if not P or P[0] != w or len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if P[i + 1] not in g[P[i]]:
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if P[j] in g[P[i]]:
                return False
    return True


def build_anchored_path(g, w, cap, budget=200000):
    """DFS for an induced path with ENDPOINT w on >= cap vertices.  Capped: None means NOT
    FOUND WITHIN THE BUDGET, never 'does not exist'."""
    nodes = [0]
    best = [1]
    dw = bfs(g, w)

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > budget:
            return None
        if len(path) > best[0]:
            best[0] = len(path)
        if len(path) >= cap:
            return list(path)
        u = path[-1]
        for x in sorted(g[u] - pset, key=lambda z: -dw[z]):
            bad = False
            for y in path[:-1]:
                if x in g[y]:
                    bad = True
                    break
            if bad:
                continue
            path.append(x)
            pset.add(x)
            r = dfs(path, pset)
            if r is not None:
                return r
            path.pop()
            pset.discard(x)
        return None
    r = dfs([w], {w})
    return r, best[0], nodes[0] > budget


def load(path):
    nn = None
    ed = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split()
        if len(p) == 1:
            nn = int(p[0])
        else:
            ed.append((int(p[0]), int(p[1])))
    return adj(nn, ed)


def partA():
    print()
    print("=" * 78)
    print("PART A -- (TAIL-2) ON EVERY CONDITION-4 VERTEX OF THE NEW CASE A INSTANCES")
    print("=" * 78)
    print("""
  PREDICTION, REGISTERED BEFORE THE RUN: the ecc(w)+3 anchored induced path will be BUILT on
  every condition-4 vertex of W43a and W43b.  These hosts have girth >= 5 and 420 vertices, so
  long induced paths should be abundant; a failure would be the first CASE A candidate for a
  (TAIL-2) shortfall and would be reported as a FAILURE TO BUILD, not as a shortfall.
""")
    tot = built = failed = 0
    for tag in ("W43a", "W43b"):
        g = load("problems/wowii/w133_r43_%s.txt" % tag)
        D, ecc, r = profile(g)
        diam = max(ecc)
        C = centre_of(ecc, r)
        W = far_intersection(D, ecc, r)
        ck(c4_free(g), "%s is C4-free" % tag)
        ck(diam == r + 1 and r >= 5 and l_of(g) > 4, "%s meets conditions 2,3,5" % tag)
        print("  %s  n=%d rad=%d diam=%d |Ctr|=%d condition-4 vertices=%d"
              % (tag, len(g), r, diam, len(C), len(W)))
        worst = None
        for w in W:
            if over():
                print("    DEADLINE -- %d of %d tested" % (tot, len(W)))
                break
            tot += 1
            cap = ecc[w] + 3
            P, bl, trunc = build_anchored_path(g, w, cap)
            if P is not None and is_anchored_induced_path(g, P, w) and len(P) >= cap:
                built += 1
            else:
                failed += 1
                if worst is None or bl < worst[1]:
                    worst = (w, bl, trunc)
        print("    ecc(w)+3 anchored induced path BUILT and checker-verified on %d of %d"
              % (built, tot))
        if worst is not None:
            print("    ** NOT BUILT on w=%d: longest built %d, budget exhausted=%s.  This is a"
                  % worst)
            print("    ** FAILURE TO BUILD, not a shortfall; it needs an exact treatment.")
    print()
    print("  TOTAL: %d condition-4 vertices tested, %d covered by (TAIL-2), %d not built."
          % (tot, built, failed))
    print("  (TAIL-2) STILL COVERS EVERY INSTANCE THIS LINE HOLDS ABOVE rad = 2." if failed == 0
          else "  A CANDIDATE FOR A (TAIL-2) SHORTFALL EXISTS AT rad >= 5 -- see above.")
    return built, failed


def partB():
    print()
    print("=" * 78)
    print("PART B -- HOW SMALL CAN AN INSTANCE OF CONDITIONS 1-5 BE?")
    print("=" * 78)
    print("""
  FIRST, A PROOF THAT BOUNDS THE SEARCH.  a(v) <= deg(v) always, so l(G) <= mean degree.  A
  sampler with degree cap 4 therefore has l <= 4 and CANNOT satisfy condition 5 (l > 4) --
  slice 1's cap-4 rows printing l = 4.0000 exactly are that identity, not a coincidence.  So
  cap >= 5 is FORCED, and the question is how few vertices a cap-5 host needs to still have
  rad >= 5.

  PREDICTION, REGISTERED BEFORE THE RUN: an instance with n < 420 exists; NO prediction on how
  much smaller.  (Slice 1 only sampled n in {120,200,300,420,560} at three seeds each, so the
  minimum it reported is an artefact of that grid, and this part says so before running.)
""")
    best = None
    rows = []
    inclass = 0
    for n in (180, 220, 260, 300, 340, 380, 420):
        for cap in (5,):
            for sd in range(1, 15):
                if over():
                    break
                g = rand_c4free_sparse(sd * 15485863 + n * 41 + cap, n, cap)
                if g is None or not c4_free(g):
                    continue
                mu = min(a_val_matching(g, v) for v in range(len(g)))
                if mu < 2:
                    continue
                D, ecc, r = profile(g)
                diam = max(ecc)
                lg = l_of(g)
                if lg <= 4 or r < 5:
                    continue
                inclass += 1
                if diam != r + 1:
                    continue
                W = far_intersection(D, ecc, r)
                C = centre_of(ecc, r)
                rows.append((n, sd, lg, r, diam, len(C), len(W)))
                if W and (best is None or len(g) < len(best[1])):
                    best = ("SP5(%d,%d)" % (n, sd), g, r, diam, len(C), W[0], lg, mu)
    print("  %6s %4s %9s %5s %6s %7s %7s" % ("n", "sd", "l", "rad", "diam", "|Ctr|", "cond4"))
    for (n, sd, lg, r, diam, nc, nw) in rows:
        print("  %6d %4d %9.6f %5d %6d %7d %7d" % (n, sd, lg, r, diam, nc, nw))
    print()
    print("  THE POPULATION (rule 90): cap-5 hosts in class (C4-free, mu>=2, l>4, rad>=5): %d ;"
          % inclass)
    print("  ... of those ROUND (CASE A hosts): %d ; ... carrying condition 4: %d"
          % (len(rows), sum(1 for x in rows if x[6])))
    if best is None:
        print("  NO smaller instance found on this grid.  W43a (n = 420) stands as the")
        print("  smallest this line holds, and that is a statement about the GRID.")
        return None
    (nm, g, r, diam, nc, w, lg, mu) = best
    print()
    print("  SMALLEST INSTANCE ON THIS GRID: %s  n=%d |E|=%d mu=%d l=%.6f rad=%d diam=%d "
          "|Ctr|=%d w=%d" % (nm, len(g), len(edges_of(g)), mu, lg, r, diam, nc, w))
    D, ecc, rr = profile(g)
    ck(c4_free(g) and mu >= 2, "smallest: condition 1")
    ck(rr >= 5 and max(ecc) == rr + 1, "smallest: conditions 2 and 3")
    ck(l_of(g) > 4, "smallest: condition 5")
    ck(all(D[c][w] == rr for c in centre_of(ecc, rr)), "smallest: condition 4")
    cap = ecc[w] + 3
    P, bl, trunc = build_anchored_path(g, w, cap)
    ck(P is not None and is_anchored_induced_path(g, P, w) and len(P) >= cap,
       "smallest: (TAIL-2) path on %d >= ecc(w)+3 = %d vertices BUILT and checked" % (bl, cap))
    with open("problems/wowii/w133_r43_W43c.txt", "w") as fh:
        fh.write("# W43c = %s  n=%d rad=%d diam=%d |Ctr|=%d l=%.6f\n"
                 % (nm, len(g), r, diam, nc, lg))
        fh.write("%d\n" % len(g))
        for (u, v) in sorted(edges_of(g)):
            fh.write("%d %d\n" % (u, v))
    print("  written to problems/wowii/w133_r43_W43c.txt -- NOT certified by this file;")
    print("  the standalone `w133_r43_verify_W43.py` is what certifies it (rule 105).")
    return best


def main():
    print("WOWII-133 round 43 slice 2 -- the cover on the new CASE A instances, and n")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    partA()
    partB()
    print()
    print("=" * 78)
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
