#!/usr/bin/env python3
"""WOWII-133 round 45, slice 3 -- WIDENED RE-RUN of slice 2 -- (TAIL-2S): THE NECESSARY CONDITION FOR AN OPEN INSTANCE
IS ITSELF A RESOURCE.

Round 44's (ROW-HARD) and this round's (ROW-K) both say the same thing about an instance
that is still open: at EVERY admissible frame, `k2(y) >= 1`, i.e. N(y) must MEET N(u_{d-2})
or N(u_{d-3}).  That is stated as an obstruction.  It is also a HYPOTHESIS -- and it is
exactly the hypothesis a different construction needs.

  (TAIL-2S) -- the SIDESTEP.  Instead of extending the geodesic PAST u_d, leave it at
  u_{d-2}, cross to y through the very witness p that k2's first indicator asserts, come
  back to u_d, and THEN extend.  The path is
        u_0 ... u_{d-2},  p,  y,  u_d,  y'
  on (d-1) + 4 = d+3 = ecc(w)+3 vertices, anchored at w.  It needs NOTHING about a(y) or
  deg(y); it needs p !~ u_{d-3} and a(u_d) >= 3.

Consequence, and it is the point: an instance that is still open must have a(u_d) = 2 at
every far end u_d of w whose k2-witness p misses u_{d-3}.  Since mu >= 2 forces a >= 2, that
is EQUALITY -- the far ends of w have EXACTLY two matching components in their
neighbourhood.  Round 44 said the obstruction is "a low-a collar"; it is sharper than that.

WHY THIS SLICE EXISTS, AND WHAT IT INHERITS.  Slice 2 (`w133_r45b_sidestep.py` -> `.out`,
EXIT 0, 2 checks) ran (P1)/(P2)/(P3) on a sample of FOUR hosts and NINETEEN frames, because
its `rand_c4free_dense` had been RETYPED instead of copied and produced graphs that are NOT
C4-free -- the file's own `c4_free` filter threw all five of them away, which is why the
sample collapsed.  That is OWNER ERROR 1 of this round, and this slice is the repair BY
RUNNING (81): the builder below is the VERBATIM one.
  * (P3) HELD on slice 2 (19/19 BUILT) and is re-run here at scale.
  * (P1) was recorded FAILED on slice 2 -- on 19 frames, which cannot decide it.
  * (P2) was recorded FAILED on slice 2, and that verdict is NOT re-run: it is a fact about
    W43a/W43b/W43c/W44a, already measured, and re-predicting it would be dishonest.

REGISTERED BEFORE THIS RUN (81), both genuinely undecided:
  (P4) with at least ten times slice 2's frames, the guard variant that drops
       `p !~ u_{d-3}` OVER-CLAIMS on at least one frame -- i.e. the clause is load-bearing.
  (P5) among the CASE A instances that (TAIL-2S) does NOT close, the binding sub-condition
       is the MISSING WITNESS p, not `a(u_d) = 2`: at least 90% of them have some far end
       with a(u_d) >= 3.

Self-contained: primitives COPIED VERBATIM from `w133_r45_ladder.py` (which copied them
from round 44).  System python3, pure stdlib.  No SAT, no exhaustive search.
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
CHECKS = 0
FAILS = 0


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


# ---------------------------------------------------------------- primitives (COPIED)


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


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    return D, ecc, min(ecc)


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def is_induced_path(g, P):
    if len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if P[i + 1] not in g[P[i]]:
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if P[j] in g[P[i]]:
                return False
    return True


def geodesics(D, g, w, x, cap):
    d = D[w][x]
    out = []

    def back(cur, acc):
        if len(out) >= cap:
            return
        if cur == w:
            out.append(list(reversed(acc)))
            return
        for p in sorted(g[cur]):
            if D[w][p] == D[w][cur] - 1:
                acc.append(p)
                back(p, acc)
                acc.pop()
                if len(out) >= cap:
                    return
    back(x, [x])
    return [P for P in out if len(P) == d + 1]


def tail1_frames(g, D, w, x, ngeo=3):
    fr = []
    for P in geodesics(D, g, w, x, ngeo):
        d = len(P) - 1
        ud, um1 = P[-1], P[-2]
        for y in sorted(g[ud]):
            if y == um1 or y in g[um1]:
                continue
            if any(y == P[i] or y in g[P[i]] for i in range(d)):
                continue
            fr.append((P, y))
    return fr


def load_txt(path):
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



def connected(g):
    return all(x >= 0 for x in bfs(g, 0))


def rand_c4free_dense(seed, n):
    """round 42's greedy random C4-free host, COPIED: this is the family that produced round
    42's 414 condition-4 vertices at rad = 2, and it is used here ONLY as a POSITIVE CONTROL."""
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
    if len(h) < 6 or not connected(h) or min(a_val_matching(h, v) for v in range(len(h))) < 2:
        return None
    return h


def glue_cycle(g, at, k):
    """attach a cycle of length k through the vertex `at` -- round 42's lengthener, COPIED."""
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(k - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, at))
    return adj(n, E)


def theta(lens):
    """k >= 3 internally disjoint paths of the given lengths between two branch vertices.
    A CYCLE topology is what PART 4 says forces a spread centre; this is the smallest
    topology that is not a cycle."""
    E = []
    nxt = 2
    for L in lens:
        prev = 0
        for _ in range(L - 1):
            E.append((prev, nxt))
            prev = nxt
            nxt += 1
        E.append((prev, 1))
    return adj(nxt, E)



# ---------------------------------------------------------------- (TAIL-2S)


def sidestep_frames(g, D, ecc, w, ngeo=3, nfar=8, drop_cond=False):
    """every (TAIL-2S) frame from w.  Yields (P, y, p, hypotheses_hold, built_path_or_None).
    `drop_cond=True` is the GUARD: it drops the `p !~ u_{d-3}` condition."""
    n = len(g)
    e = ecc[w]
    fars = sorted(u for u in range(n) if D[w][u] == e)[:nfar]
    for x in fars:
        for (P, y) in tail1_frames(g, D, w, x, ngeo):
            d = len(P) - 1
            if d < 3:
                continue
            um2 = P[d - 2]
            um3 = P[d - 3] if d >= 3 else None
            for p in sorted(g[y] & g[um2]):
                if p in P or p == y:
                    continue
                if (not drop_cond) and um3 is not None and p in g[um3]:
                    continue
                # the sidestep prefix, then u_d, then one more from N(u_d)
                Q = P[:d - 1] + [p, y, P[d]]
                built = None
                if is_induced_path(g, Q) and Q[0] == w:
                    for yp in sorted(g[P[d]]):
                        if yp in Q:
                            continue
                        R = Q + [yp]
                        if is_induced_path(g, R) and R[0] == w and len(R) == e + 3:
                            built = R
                            break
                hyp = (a_val_matching(g, P[d]) >= 3)
                yield (P, y, p, hyp, built)


def part_a():
    print()
    print("=" * 78)
    print("PART A -- (TAIL-2S), the SIDESTEP, and its proof")
    print("=" * 78)
    print("""
  (TAIL-2S).  Let H be C4-free with mu(H) >= 2, w a vertex, u_0..u_d a geodesic from
  w = u_0 to a far end u_d (d = ecc(w) >= 3), and y in N(u_d) admissible for (TAIL-1)
  (y != u_{d-1} and y !~ u_{d-1}).  Suppose there is p in N(y) & N(u_{d-2}) with
  p !~ u_{d-3}, and a(u_d) >= 3.  Then endpath(H,w) >= ecc(w)+3.

  Proof.  Consider  Q := u_0 ... u_{d-2}, p, y, u_d  --  (d-1) + 3 = d+2 vertices.
   * p != u_i for every i: p ~ u_{d-2} rules out i = d-2 and, by distance, i <= d-4;
     p ~ y and y !~ u_{d-3} (distance from u_d) rule out i = d-3.
   * p !~ u_i for i <= d-4: p ~ u_{d-2} and p ~ u_i would put u_i and u_{d-2} at distance
     <= 2 through p; for i = d-4 that gives u_{d-4}, u_{d-2} the two common neighbours
     u_{d-3} and p -- a C4.  For i < d-4 it contradicts d(u_i,u_{d-2}) = d-2-i >= 3.
     p !~ u_{d-3} is the hypothesis.
   * p !~ u_d: otherwise u_{d-2} and u_d have the two common neighbours u_{d-1} and p
     (p != u_{d-1} because p ~ y and y !~ u_{d-1}) -- a C4.
   * y !~ u_i for i <= d-2: y !~ u_{d-2} is (TAIL-1)'s C4 argument, and i <= d-3 is
     distance (d(y,u_i) >= d(u_d,u_i) - 1 >= 2).
   * u_d !~ u_i for i <= d-2 is the geodesic.
  So Q is an induced path anchored at w.  Now extend by y' in N(u_d).  y' is forbidden only
  if y' = or ~ some vertex of Q other than u_d:
   * y' !~ u_{d-2}: N(u_d) & N(u_{d-2}) = {u_{d-1}} by C4-freeness -- ONE component.
   * y' !~ u_i, i <= d-3: automatic, d(u_d,u_i) >= 3.
   * y' !~ p: N(u_d) & N(p) has at most one element and y is in it, so it IS {y}.
   * y' != y and y' !~ y: y's own matching component of G[N(u_d)] -- ONE component, and it
     is NOT u_{d-1}'s, because y was chosen off u_{d-1}'s component.
  Exactly two matching components of G[N(u_d)] are excluded, so a(u_d) >= 3 leaves one. []

  WHY IT MATTERS.  (TAIL-2'') pays for the dodge list in a(y)/deg(y) AT y.  (TAIL-2S) pays
  nothing at y at all: it spends the k2-witness p, which (ROW-HARD)/(ROW-K) say an OPEN
  instance is obliged to provide at every frame.  The two conditions are therefore aimed at
  opposite regimes, and an instance that is still open must defeat BOTH:

    (ROW-HARD''').  An open offset-+1, k = 4 row instance has, at every far end u_d of w
    and every admissible frame:  max(a(y),deg(y)-1) <= 1 + k2(y)  [round 44]  AND
    k2(y) >= 1  [(ROW-K), from mu >= 2]  AND -- new -- either a(u_d) = 2 exactly, or every
    witness p in N(y) & N(u_{d-2}) satisfies p ~ u_{d-3}.
""")


def part_b():
    print("=" * 78)
    print("PART B -- (P3): does the construction actually BUILD, wherever it claims to?")
    print("          and (P1): is `p !~ u_{d-3}' load-bearing?")
    print("=" * 78)
    hosts = [("C9", cycle(9)), ("C11", cycle(11)), ("C13", cycle(13)),
             ("Theta(3,3,3)", theta([3, 3, 3])), ("Theta(4,4,4)", theta([4, 4, 4])),
             ("C9+glue", glue_cycle(cycle(9), 0, 9)),
             ("C11+glue", glue_cycle(cycle(11), 0, 11))]
    ndrop = 0
    for nn in (20, 26, 34, 40, 48):
        for s in (1, 2, 3, 5, 7, 11, 13, 17, 19, 23):
            g = rand_c4free_dense(s, nn)
            if g is None:
                ndrop += 1
                continue
            ck(c4_free(g), "dense(s=%d,n=%d) really is C4-free" % (s, nn))
            if c4_free(g) and min(a_val_matching(g, v) for v in range(len(g))) >= 2:
                hosts.append(("dense(s=%d,n=%d)" % (s, nn), g))
            else:
                ndrop += 1
    try:
        hosts.append(("W43a", load_txt("problems/wowii/w133_r43_W43a.txt")))
        hosts.append(("W44a", load_txt("problems/wowii/w133_r44_W44a.txt")))
    except IOError:
        pass
    hosts = [(nm, g) for (nm, g) in hosts
             if g is not None and c4_free(g)
             and min(a_val_matching(g, v) for v in range(len(g))) >= 2]
    print("  host slots dropped by the builder or the mu >= 2 screen: %d" % ndrop)

    claim = built = fail = 0
    gclaim = gbuilt = gfail = 0
    nfr = 0
    a_ud = {}
    for (nm, g) in hosts:
        D, ecc, r = profile(g)
        step = max(1, len(g) // 40)
        for w in range(0, len(g), step):
            if ecc[w] < 3:
                continue
            for (P, y, p, hyp, R) in sidestep_frames(g, D, ecc, w, 3, 8, drop_cond=False):
                nfr += 1
                ud = P[-1]
                a_ud[a_val_matching(g, ud)] = a_ud.get(a_val_matching(g, ud), 0) + 1
                if hyp:
                    claim += 1
                    if R is not None and is_induced_path(g, R) and len(R) == ecc[w] + 3:
                        built += 1
                    else:
                        fail += 1
            for (P, y, p, hyp, R) in sidestep_frames(g, D, ecc, w, 3, 8, drop_cond=True):
                if hyp:
                    gclaim += 1
                    if R is not None and is_induced_path(g, R) and len(R) == ecc[w] + 3:
                        gbuilt += 1
                    else:
                        gfail += 1
    print("  hosts: %d.  (TAIL-2S) frames examined: %d." % (len(hosts), nfr))
    print("  (TAIL-2S) CORRECT form (p !~ u_{d-3} required):")
    print("      hypotheses hold on %d frames; path BUILT %d; FAILED TO BUILD %d"
          % (claim, built, fail))
    print("  GUARD (D13) DROP-p-CONDITION (the `p !~ u_{d-3}' clause removed):")
    print("      hypotheses hold on %d frames; path BUILT %d; FAILED TO BUILD %d"
          % (gclaim, gbuilt, gfail))
    print("  a(u_d) histogram over the frames: %s"
          % "  ".join("%d:%d" % (k, a_ud[k]) for k in sorted(a_ud)))
    ck(fail == 0, "(P3): (TAIL-2S) BUILDS its path at every frame where it claims to")
    ck(nfr > 0, "PART B examined a non-empty set of (TAIL-2S) frames")
    print("  (P4) VERDICT: %s -- the dropped clause over-claims on %d frames."
          % ("HELD" if gfail > fail else "FAILED", gfail - fail))
    return fail, gfail


def part_c():
    print()
    print("=" * 78)
    print("PART C -- (P2): the new necessary condition `a(u_d) = 2 at every far end of w'")
    print("=" * 78)
    print("""
  (TAIL-2S) closes an instance as soon as ONE far end u_d of w has a(u_d) >= 3 together
  with a k2-witness p missing u_{d-3}.  So an OPEN instance needs a(u_d) = 2 at (almost)
  every far end of w.  DIRECTION OF THE SAMPLING ERROR, FIXED FIRST (129): far ends and
  geodesics are SAMPLED, so a printed `a(u_d) >= 3 somewhere' is SOUND (that far end really
  does have it) while `a = 2 everywhere' would be INCONCLUSIVE.
""")
    tot = 0
    hasge3 = 0
    a2only = []
    NOTCLOSED = []
    for tag, fn in (("W43a", "problems/wowii/w133_r43_W43a.txt"),
                    ("W43b", "problems/wowii/w133_r43_W43b.txt"),
                    ("W43c", "problems/wowii/w133_r43_W43c.txt"),
                    ("W44a", "problems/wowii/w133_r44_W44a.txt")):
        try:
            g = load_txt(fn)
        except IOError:
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        ctr = [v for v in range(len(g)) if ecc[v] == r]
        cond4 = [w for w in range(len(g))
                 if ecc[w] == r + 1 and all(D[c][w] == r for c in ctr)]
        amins = []
        nclose = 0
        for w in cond4:
            fars = [u for u in range(len(g)) if D[w][u] == ecc[w]]
            am = min(a_val_matching(g, u) for u in fars)
            aM = max(a_val_matching(g, u) for u in fars)
            amins.append((am, aM))
            tot += 1
            if aM >= 3:
                hasge3 += 1
            else:
                a2only.append((tag, w))
            got = False
            for (P, y, p, hyp, R) in sidestep_frames(g, D, ecc, w, 3, 8):
                if hyp and R is not None and len(R) == ecc[w] + 3:
                    got = True
                    break
            nclose += got
            if not got:
                NOTCLOSED.append((tag, w, am, aM))
        print("  %-5s condition-4 vertices %3d; min/max a(far end) over them: %s ; "
              "(TAIL-2S) closes %d"
              % (tag, len(cond4), "%d/%d" % (min(x[0] for x in amins),
                                             max(x[1] for x in amins)), nclose))
    print("  CASE A instances examined: %d; with SOME far end at a(u_d) >= 3: %d;"
          % (tot, hasge3))
    print("  with EVERY far end at a(u_d) = 2 (the only ones (TAIL-2S) cannot touch): %d"
          % len(a2only))
    print("  (P2, inherited from slice 2 and NOT re-predicted here) : %s%s"
          % ("some instance has every far end at a = 2" if a2only else
             "no instance has every far end at a = 2",
             "" if a2only else " -- every CASE A instance this line holds has a far end"
                               " with a >= 3, so the a(u_d) = 2 half of the necessary"
                               " condition is violated everywhere on this family."))
    nc = len(NOTCLOSED)
    nc_a3 = sum(1 for (t, w, am, aM) in NOTCLOSED if aM >= 3)
    print("  CASE A instances (TAIL-2S) does NOT close: %d" % nc)
    if nc:
        print("    ... of those, WITH a far end at a(u_d) >= 3 (so the binding sub-condition")
        print("        is the MISSING WITNESS p, not a(u_d) = 2): %d  (%.1f%%)"
              % (nc_a3, 100.0 * nc_a3 / nc))
        print("    ... with EVERY far end at a(u_d) = 2: %d" % (nc - nc_a3))
    print("  (P5) VERDICT: %s"
          % ("HELD" if nc and nc_a3 >= 0.9 * nc else
             ("FAILED" if nc else "UNDECIDED -- (TAIL-2S) closed everything")))
    return tot, hasge3, len(a2only)


def main():
    print("WOWII-133 round 45 slice 3 -- WIDENED RE-RUN of slice 2 (whose host builder had")
    print("                              been RETYPED, not copied, and was not C4-free)")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    part_a()
    part_b()
    part_c()
    print()
    print("=" * 78)
    print("CHECKS %d   FAILS %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
