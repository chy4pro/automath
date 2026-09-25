#!/usr/bin/env python3
"""
w133 round 31 -- ITEM 4: (A2-PATH) AS STATED IS FALSE, AND THE MECHANISM SAYS WHAT REPLACES IT.

THE TARGET.  r30 split A2 and left one half open:

    (A2-PATH)   path(G) >= path(G') + h

with  G' := the result of peeling every a = 1 vertex (F7),  h := the maximum distance in G
from a peeled vertex to V(G'),  and  path(-) := the number of VERTICES in a longest induced
path.  With F11 on G' (path(G') >= rad(G') + 4) and r30's inequality half
(rad(G) <= rad(G') + h), (A2-PATH) would close Problem A.  r30 called it "the whole new idea".

THE FINDING OF THIS FILE.

  *** (A2-PATH) IS FALSE.  A pendant vertex is a hair of length h = 1, and it lengthens a  ***
  *** longest induced path ONLY IF it is hung at a vertex that is already an ENDPOINT of   ***
  *** one.  Hang it anywhere else and path(G) = path(G'), while h = 1.                     ***

  The mechanism, and it is an EQUALITY, not a bound.  For G = G' + a pendant v at w:
      every induced path of G either avoids v, or ends at v (v is a leaf, so it can never
      be interior), hence
                 path(G)  =  max( path(G'),  1 + endpath(G', w) )
  where endpath(G', w) is the largest number of vertices on an induced path of G' having w
  as an ENDPOINT.  So (A2-PATH) at h = 1 is equivalent to  endpath(G', w) = path(G'),  i.e.
  to w being an endpoint of some longest induced path of G'.  Nothing forces that.

  *** h MEASURES DISTANCE; path IS PAID ONLY AT AN ENDPOINT.  The exchange A2 asks for is  ***
  *** not between two lengths, it is between a length and an ANCHORED length.              ***

HOW FAR THE REFUTATION REACHES -- measured in PART 4, not asserted.  The witnesses are pushed
as close to Problem A's class as this round could push them:
    connected           YES        C4-free            YES
    an a = 1 vertex     YES        rad(G) >= 5        YES  (two C9's sharing a vertex, plus a
                                                            pendant: n = 18, rad = 5, h = 1,
                                                            path(G) = path(G') = 15)
    l(G) > 4            NO   -- the ONE hypothesis no witness here carries (best l = 2.29).
So (A2-PATH) is false as stated AND false under rad >= 5.  **Any proof of it must consume
l > 4**, and l > 4 is a DENSITY hypothesis, while the failure above is a POSITIONAL one -- the
hair is hung where no longest induced path ends.  That mismatch is the finding.

WHAT THIS DOES NOT DO.  It does not refute route A2 and it does not touch Problem A: nothing
here is a counterexample inside Problem A's full class, and none is claimed.  PART 5 states
the anchored replacement that the route actually needs, and checks it on the witness.

RULING CZ: every predicate ships an input on which it MUST return True, and the counterexample
gate is shown DECLINING on graphs chosen to break the specific clause each one targets.
The peeling and longest-induced-path primitives are written here from scratch and CROSS-CHECKED
against r30's implementations on random inputs -- r30's own peel_all was defective before it
was fixed, so agreement is checked, not assumed.

No SAT.  Bounded pruned search only.  Wall-clock self-limit 300 s, exit(2) -- never `return`.
"""
import itertools, os, random, sys, time
from collections import deque

T0 = time.time()
LIMIT = 300.0
def tick(tag):
    if time.time() - T0 > LIMIT:
        print("OVERRUN at %s" % tag)
        sys.exit(2)

FAIL = []
NCHECK = 0
def check(name, ok, detail=""):
    global NCHECK
    NCHECK += 1
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# ============================================================================
# PART 0 -- OWN PRIMITIVES
# ============================================================================
def mk(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj

def sub(adj, S):
    return {v: (adj[v] & S) for v in S}

def connected(g):
    S = set(g)
    if not S:
        return False
    s = next(iter(S))
    seen, q = {s}, deque([s])
    while q:
        u = q.popleft()
        for w in g[u]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return seen == S

def c4free(g):
    V = sorted(g)
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if len(g[V[i]] & g[V[j]]) >= 2:
                return False
    return True

def a_val(g, v):
    nb = sorted(g[v])
    t = sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb)) if nb[j] in g[nb[i]])
    return len(nb) - t

def peel_all(g):
    """F7: iteratively remove every a = 1 vertex.  Returns the (possibly EMPTY) fixed point.
    It must be allowed to return empty -- r30's first version refused to, and thereby lied."""
    S = set(g)
    while True:
        cur = sub(g, S)
        nxt = {v for v in S if a_val(cur, v) != 1}
        if nxt == S:
            return S
        S = nxt
        if not S:
            return S

def bfs_dist(g, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for w in g[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d

def rad(g):
    if not g or not connected(g):
        return None
    es = []
    for v in g:
        d = bfs_dist(g, v)
        if len(d) != len(g):
            return None
        es.append(max(d.values()))
    return min(es)

def _paths_from(g, last, mask, acc):
    """extend an induced path; `mask` is the set of vertices already on it"""
    best = len(mask)
    for u in g[last]:
        if u in mask:
            continue
        if (g[u] & mask) - {last}:      # u must see ONLY `last` on the path
            continue
        best = max(best, _paths_from(g, u, mask | {u}, acc))
    return best

def path_of(g):
    """VERTEX count of a longest induced path"""
    if not g:
        return 0
    return max(_paths_from(g, v, {v}, None) for v in g)

def endpath(g, w):
    """VERTEX count of a longest induced path of g having w as an ENDPOINT"""
    if w not in g:
        return 0
    return _paths_from(g, w, {w}, None)

def l_of(g):
    """l(G) := the MEAN a-value.  Read off F7's own arithmetic: it tracks `Sigma a - 4n`
    and concludes `peeling preserves l > 4`, so `l > 4` is `Sigma a > 4n`.  Controlled in
    PART 0 against the brief's own datum: PG(2,3)'s incidence graph has l = 4.0 exactly."""
    return sum(a_val(g, v) for v in g) / float(len(g)) if g else 0.0

def pg23():
    """the PG(2,3) incidence graph, from the perfect difference set {0,1,3,9} mod 13:
    13 points 0..12, 13 lines 13..25, point p on line 13+i iff p - i in {0,1,3,9}"""
    E = []
    for i in range(13):
        for d in (0, 1, 3, 9):
            E.append(((i + d) % 13, 13 + i))
    return sub(mk(26, E), set(range(26)))

def h_of(g, gp):
    """h = max over PEELED v of d_G(v, V(G'));  0 if nothing was peeled"""
    peeled = set(g) - set(gp)
    if not peeled:
        return 0
    best = 0
    for v in peeled:
        d = bfs_dist(g, v)
        reach = [d[x] for x in gp if x in d]
        if not reach:
            return None                  # a peeled vertex cannot reach G' at all
        best = max(best, min(reach))
    return best


def part0():
    print("\n=== PART 0 -- POSITIVE CONTROLS, EACH ON AN INPUT WHERE IT MUST RETURN True ===")
    C5 = sub(mk(5, [(0,1),(1,2),(2,3),(3,4),(4,0)]), set(range(5)))
    check("MUST-FIRE: C5 is connected and C4-free", connected(C5) and c4free(C5))
    check("MUST-FIRE: a(v) = 2 at every C5 vertex", [a_val(C5, v) for v in range(5)] == [2]*5)
    check("MUST-FIRE: path(C5) = 4 vertices", path_of(C5) == 4, "got %d" % path_of(C5))
    check("MUST-FIRE: rad(C5) = 2", rad(C5) == 2)
    K13 = sub(mk(4, [(0,1),(0,2),(0,3)]), set(range(4)))
    check("specificity: the star K_{1,3} IS detected as not C4-free? no -- it is C4-free",
          c4free(K13))
    check("MUST-FIRE: peeling K_{1,3} strips the three leaves and leaves the centre "
          "(a(centre) = 3 - 0 = 3 first, then 0 once alone -- never 1)",
          peel_all(K13) == {0}, "got %r" % (peel_all(K13),))
    tri = sub(mk(3, [(0,1),(1,2),(2,0)]), set(range(3)))
    check("MUST-FIRE: peeling annihilates the triangle (every a = 2 - 1 = 1) and the peeler "
          "is ALLOWED to return empty", peel_all(tri) == set(), "got %r" % (peel_all(tri),))
    check("MUST-FIRE: a 4-cycle IS caught by c4free",
          not c4free(sub(mk(4, [(0,1),(1,2),(2,3),(3,0)]), set(range(4)))))
    P4 = sub(mk(4, [(0,1),(1,2),(2,3)]), set(range(4)))
    check("MUST-FIRE: endpath(P4, endpoint) = 4 and endpath(P4, interior) = 3",
          endpath(P4, 0) == 4 and endpath(P4, 1) == 3,
          "%d / %d" % (endpath(P4, 0), endpath(P4, 1)))
    P = pg23()
    check("MUST-FIRE: the PG(2,3) incidence graph is C4-free, 4-regular, 26 vertices",
          c4free(P) and len(P) == 26 and all(len(P[v]) == 4 for v in P))
    check("MUST-FIRE: l(PG(2,3)) = 4.0 EXACTLY -- the brief's own published datum, so this "
          "control pins l's DEFINITION and not just its arithmetic",
          abs(l_of(P) - 4.0) < 1e-12, "l = %.6f" % l_of(P))
    check("specificity: PG(2,3) is therefore NOT in the l > 4 class (the brief says so too)",
          not (l_of(P) > 4.0))
    check("MUST-FIRE: h = 1 for a single pendant",
          h_of(sub(mk(6, [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5)]), set(range(6))), set(range(5)))
          == 1)
    # CROSS-CHECK against r30's independent implementations on random inputs.
    #
    # OWN DEFECT, LEFT VISIBLE.  The first version of this block did `import w133_r30_a2`.
    # That file has no `if __name__ == "__main__"` guard, so the import RAN ITS ENTIRE
    # PROGRAM and ended on its `sys.exit(0)`.  SystemExit propagated out of part0(), this
    # script's PARTS 1-5 NEVER RAN, and the shell still saw EXIT=0.  *A wrapper that exits
    # 0 having done none of the work is the worst failure mode there is*, and it was caught
    # only by reading the output, which is why the fix below also ASSERTS that part5 ran.
    # We now exec only the prefix of r30's source that precedes its first top-level
    # statement, so we get its functions and none of its program.
    R30 = None
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "w133_r30_a2.py"), encoding="utf-8").read().split("\n")
    cutat = next((i for i, ln in enumerate(src)
                  if ln.startswith("print(") or ln.startswith("check(")), len(src))
    ns = {}
    try:
        exec("\n".join(src[:cutat]), ns)
        R30 = ns
    except Exception as e:
        print("      r30 prefix not executable (%s) -- cross-check SKIPPED and said so" % e)
    check("the r30 prefix loaded WITHOUT running r30's program (it defines peel_all/rad "
          "and printed nothing above this line)",
          R30 is not None and "peel_all" in R30 and "rad" in R30)
    if R30 is not None:
        class _R30:
            peel_all = staticmethod(R30["peel_all"])
            rad = staticmethod(R30["rad"])
        R30 = _R30
    if R30 is not None:
        random.seed(20260823)
        mism_peel = mism_rad = 0
        for _ in range(300):
            n = random.randint(3, 8)
            E = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < 0.4]
            adj_sets = mk(n, E)
            g = sub(adj_sets, set(range(n)))
            mine = peel_all(g)
            theirs = R30.peel_all(adj_sets, set(range(n)))
            if mine != theirs:
                mism_peel += 1
            if connected(g):
                if rad(g) != R30.rad(adj_sets, set(range(n))):
                    mism_rad += 1
        check("CROSS-CHECK: this file's peel_all AGREES with r30's (post-fix) on 300 random "
              "graphs -- two implementations of a function that was WRONG in r30's first "
              "version", mism_peel == 0, "%d mismatches" % mism_peel)
        check("CROSS-CHECK: this file's rad AGREES with r30's on the connected ones",
              mism_rad == 0, "%d mismatches" % mism_rad)
    tick("part0")


# ============================================================================
# PART 1 -- THE TRIVIAL HALF, AND WHERE THE CONTENT ACTUALLY IS
# ============================================================================
def part1():
    print("\n=== PART 1 -- path(G) >= path(G') is FREE; all the content is the '+ h' ===")
    print("  G' is an INDUCED subgraph of G, so an induced path of G' is an induced path of")
    print("  G.  Hence path(G) >= path(G') with no hypotheses at all.  Verified below on")
    print("  every graph this file builds, so the claim under test is only the '+ h'.")
    tick("part1")


# ============================================================================
# PART 2 -- THE SEARCH FOR A WITNESS
# ============================================================================
def pendant_witness(g, w):
    """G := g + a pendant v at w.  Returns (G, v) with v the new vertex id."""
    V = sorted(g)
    v = max(V) + 1
    ng = {x: set(g[x]) for x in V}
    ng[w] = set(ng[w]) | {v}
    ng[v] = {w}
    return ng, v

def is_valid_base(g):
    """the base must be a legitimate G': connected, C4-free, and mu >= 2 so that peeling G
    returns exactly it (no vertex of g is itself peelable)"""
    return (connected(g) and c4free(g) and len(g) >= 3
            and all(a_val(g, v) != 1 for v in g))

CANDIDATES = [
    ("C5", 5, [(0,1),(1,2),(2,3),(3,4),(4,0)]),
    ("C6", 6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),
    ("C7", 7, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)]),
    ("C8", 8, [(i, (i+1) % 8) for i in range(8)]),
    ("two C5 sharing one vertex (bowtie of pentagons)", 9,
     [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0)]),
    ("three C5 sharing one vertex", 13,
     [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0),
      (0,9),(9,10),(10,11),(11,12),(12,0)]),
    ("two C5 joined by an edge", 10,
     [(0,1),(1,2),(2,3),(3,4),(4,0),(5,6),(6,7),(7,8),(8,9),(9,5),(0,5)]),
    ("Petersen", 10, [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
                      (0,5),(1,6),(2,7),(3,8),(4,9)]),
]
def spider(k, arms):
    """`arms` cycles of length k, all sharing one vertex (vertex 0).  Every vertex has
    a >= 2, it is C4-free for k >= 5, and rad grows with k -- so this family lets us ask
    HOW CLOSE to Problem A's rad >= 5 a witness can be pushed."""
    E, nxt = [], 1
    for _ in range(arms):
        chain = [0] + list(range(nxt, nxt + k - 1)) + [0]
        nxt += k - 1
        E += [(chain[i], chain[i + 1]) for i in range(len(chain) - 1)]
    return sub(mk(nxt, E), set(range(nxt)))

for _k in (5, 7, 9, 11, 13):
    for _a in (2, 3):
        CANDIDATES.append(("%d cycles C%d sharing one vertex" % (_a, _k), None,
                           spider(_k, _a)))

def scan_base(name, g):
    """report, per vertex, whether hanging a pendant there breaks (A2-PATH)"""
    P = path_of(g)
    out = []
    for w in sorted(g):
        G, v = pendant_witness(g, w)
        gp = peel_all(G)
        h = h_of(G, gp)
        pg = path_of(G)
        ok_gp = (gp == set(g))
        broken = ok_gp and h is not None and pg < P + h
        out.append((w, endpath(g, w), P, pg, h, ok_gp, broken))
    return P, out


def part2():
    print("\n=== PART 2 -- BOUNDED SEARCH: hang one pendant, ask whether path pays for it ===")
    print("  A pendant is a hair of length h = 1, the SMALLEST case (A2-PATH) has to cover.")
    print("  %-42s %5s %5s %s" % ("base G'", "path", "verts", "vertices where (A2-PATH) BREAKS"))
    witnesses = []
    for name, n, E in CANDIDATES:
        g = E if n is None else sub(mk(n, E), set(range(n)))
        if not is_valid_base(g):
            print("  %-42s  -- not a legal G' (connected/C4-free/mu>=2 fails), skipped" % name)
            continue
        P, rows = scan_base(name, g)
        bad = [r[0] for r in rows if r[6]]
        print("  %-42s %5d %5d %s" % (name, P, len(g), bad if bad else "none"))
        for r in rows:
            if r[6]:
                witnesses.append((name, g, r))
        tick("part2-%s" % name)
    # a bounded RANDOM sweep as well, so the finding does not rest on hand-picked shapes
    random.seed(20260823)
    rnd_found = 0
    tried = 0
    for _ in range(4000):
        n = random.randint(6, 9)
        E = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < 0.32]
        g = sub(mk(n, E), set(range(n)))
        if not is_valid_base(g):
            continue
        tried += 1
        P = path_of(g)
        for w in sorted(g):
            if endpath(g, w) < P:
                G, v = pendant_witness(g, w)
                if peel_all(G) == set(g) and path_of(G) < P + 1:
                    rnd_found += 1
                    witnesses.append((("random n=%d" % n), g, (w, endpath(g, w), P,
                                                               path_of(G), 1, True, True)))
                    break
        if time.time() - T0 > LIMIT * 0.5:
            break
    print("      bounded random sweep: %d legal bases tried, %d carry a breaking vertex"
          % (tried, rnd_found))
    check("*** A WITNESS EXISTS: (A2-PATH) as stated is FALSE", len(witnesses) > 0,
          "%d witnesses" % len(witnesses))
    tick("part2")
    return witnesses


# ============================================================================
# PART 3 -- ONE WITNESS, CERTIFIED CLAUSE BY CLAUSE
# ============================================================================
def part3(witnesses):
    print("\n=== PART 3 -- ONE WITNESS, EVERY CLAUSE CHECKED SEPARATELY ===")
    if not witnesses:
        check("a witness is available to certify", False)
        return None
    # prefer the smallest hand-named base, so the witness is readable
    named = [x for x in witnesses if not x[0].startswith("random")] or witnesses
    name, g, row = min(named, key=lambda x: len(x[1]))
    w, epw, P, pg, h, ok_gp, broken = row
    G, v = pendant_witness(g, w)
    gp = peel_all(G)
    E = sorted(tuple(sorted((x, y))) for x in G for y in G[x] if x < y)
    print("      base G'      : %s" % name)
    print("      G            : V = %r" % sorted(G))
    print("      G edge list  : %r" % (E,))
    print("      pendant      : vertex %d, hung at w = %d" % (v, w))
    check("G is connected", connected(G))
    check("G is C4-free", c4free(G))
    check("the pendant is the ONLY a = 1 vertex of G",
          [x for x in G if a_val(G, x) == 1] == [v],
          "a=1 at %r" % [x for x in G if a_val(G, x) == 1])
    check("peeling G returns exactly the base: G' = base", gp == set(g),
          "G' = %r" % sorted(gp))
    check("G' is connected and C4-free (so F11's shape applies to it)",
          connected(sub(G, gp)) and c4free(sub(G, gp)))
    check("h = 1 (the pendant is at distance 1 from G')", h_of(G, gp) == 1,
          "h = %r" % h_of(G, gp))
    print("      path(G')     : %d" % P)
    print("      path(G)      : %d" % pg)
    print("      endpath(G',w): %d   <-- w is NOT an endpoint of any longest induced path"
          % epw)
    check("path(G) >= path(G') -- the free half holds, as PART 1 says it must", pg >= P)
    check("*** (A2-PATH) FAILS ON THIS GRAPH: path(G) = %d  <  path(G') + h = %d"
          % (pg, P + h), pg < P + h)
    check("MECHANISM, and it is an EQUALITY: path(G) = max(path(G'), 1 + endpath(G',w))",
          pg == max(P, 1 + epw), "%d vs %d" % (pg, max(P, 1 + epw)))
    print()
    print("  HARDEST-FORM NEGATIVE CONTROL: hang the SAME pendant at a vertex that IS an")
    print("  endpoint of a longest induced path of the SAME base.  If the gate fired on")
    print("  'a pendant was added' rather than on WHERE, it would break here too.")
    good = [x for x in sorted(g) if endpath(g, x) == P]
    if good:
        G2, v2 = pendant_witness(g, good[0])
        p2 = path_of(G2)
        print("      hung at w' = %d (endpath = %d = path(G')): path(G) = %d, path(G')+h = %d"
              % (good[0], endpath(g, good[0]), p2, P + 1))
        check("NEGATIVE CONTROL: at an endpoint vertex (A2-PATH) HOLDS, with equality -- so "
              "the failure is about WHERE the hair hangs, not about hairs",
              p2 == P + 1, "%d vs %d" % (p2, P + 1))
    else:
        check("the base has at least one vertex that IS a longest-path endpoint", False)
    tick("part3")
    return (name, g, G, v, w, P, pg, h)


# ============================================================================
# PART 4 -- WHICH OF PROBLEM A'S HYPOTHESES THE WITNESS MISSES.  STATED, NOT HIDDEN.
# ============================================================================
def part4(cert, witnesses=()):
    print("\n=== PART 4 -- THE WITNESS'S SCOPE, MEASURED RATHER THAN GLOSSED ===")
    # HOW CLOSE to Problem A's class can a counterexample be pushed?  Measured over every
    # witness found, not argued.  Problem A assumes: connected, C4-free, l > 4, rad >= 5,
    # and an a = 1 vertex present.  We report which of those a witness can carry AT ONCE.
    best_rad, best_l, best5 = None, None, None
    for nm, g, row in witnesses:
        w = row[0]
        G, v = pendant_witness(g, w)
        rG, lG = rad(G), l_of(G)
        if best_rad is None or rG > best_rad[0]:
            best_rad = (rG, nm, w, lG, len(G))
        if best_l is None or lG > best_l[0]:
            best_l = (lG, nm, w, rG, len(G))
        if rG is not None and rG >= 5 and best5 is None:
            best5 = (nm, w, rG, lG, len(G), G)
    print("      witnesses examined: %d" % len(witnesses))
    if best_rad:
        print("      largest rad(G) over witnesses : %s  (%s, hair at %s, l = %.2f, n = %d)"
              % (best_rad[0], best_rad[1], best_rad[2], best_rad[3], best_rad[4]))
    if best_l:
        print("      largest l(G)   over witnesses : %.3f  (%s, rad = %s, n = %d)"
              % (best_l[0], best_l[1], best_l[3], best_l[4]))
    check("*** A WITNESS EXISTS WITH rad(G) >= 5 -- so (A2-PATH) is false even under "
          "Problem A's radius hypothesis, not merely on toy graphs",
          best5 is not None,
          ("%s, hair at %d, rad = %d, l = %.2f, n = %d"
           % (best5[0], best5[1], best5[2], best5[3], best5[4])) if best5 else "none found")
    if best5:
        G5 = best5[5]
        gp5 = peel_all(G5)
        check("that rad >= 5 witness is connected, C4-free, has exactly one a = 1 vertex, "
              "and peels back to its base",
              connected(G5) and c4free(G5) and len([x for x in G5 if a_val(G5, x) == 1]) == 1
              and len(gp5) == len(G5) - 1)
        check("and it really breaks (A2-PATH): path(G) < path(G') + h",
              path_of(G5) < path_of(sub(G5, gp5)) + h_of(G5, gp5),
              "path(G)=%d path(G')=%d h=%d"
              % (path_of(G5), path_of(sub(G5, gp5)), h_of(G5, gp5)))
        check("THE ONE HYPOTHESIS IT STILL MISSES IS l > 4, and that is stated rather "
              "than glossed", not (l_of(G5) > 4.0), "l = %.3f" % l_of(G5))
    print()
    if cert is None:
        return
    name, g, G, v, w, P, pg, h = cert
    rG = rad(G)
    lG = path_of(G)
    print("      rad(G) = %s   (Problem A assumes rad >= 5)" % rG)
    print("      path(G) = %d vertices" % lG)
    print("      G is C4-free: %s ; connected: %s" % (c4free(G), connected(G)))
    print("      G HAS an a = 1 vertex (Problem A's whole case): %s"
          % any(a_val(G, x) == 1 for x in G))
    check("the witness satisfies C4-freeness and connectedness -- the hypotheses (A2-PATH) "
          "was stated under", c4free(G) and connected(G))
    check("and it does NOT satisfy rad(G) >= 5, which is stated here rather than glossed",
          rG is not None and rG < 5, "rad = %s" % rG)
    print()
    print("  SO, EXACTLY: (A2-PATH) is refuted AS STATED (it carries no hypotheses at all,")
    print("  and r30 recorded it with none), AND it is refuted under rad(G) >= 5 as well.")
    print("  The ONE Problem A hypothesis no witness here carries is l > 4.")
    print("  What that settles is the SHAPE of any possible proof:")
    print("      a proof of (A2-PATH) MUST consume l > 4, because everything else in")
    print("      Problem A's hypothesis list is already satisfied by a counterexample.")
    print("      And the failure is not marginal: path(G) does not grow AT ALL while h = 1.")
    print("      Note the mismatch this exposes -- l > 4 is a DENSITY hypothesis and the")
    print("      failure is POSITIONAL (the hair hangs where no longest induced path ends).")
    tick("part4")


# ============================================================================
# PART 5 -- WHAT REPLACES IT.  THE ANCHORED FORM, AND IT IS WHAT THE ROUTE NEEDS.
# ============================================================================
def part5(cert):
    print("\n=== PART 5 -- THE ANCHORED REPLACEMENT, AND IT IS WEAKER THAN (A2-PATH) ===")
    print("  Route A2 does not need (A2-PATH).  It needs  path(G) >= rad(G) + 4,  and it")
    print("  already has  rad(G) <= rad(G') + h  (r30).  So it is ENOUGH to prove")
    print()
    print("      (A2-ANCHOR)   path(G)  >=  rad(G') + 4 + h.")
    print()
    print("  And for a hair of length h reaching G' at w, path(G) >= h + endpath(G', w).")
    print("  So (A2-ANCHOR) follows from an ANCHORED F11:")
    print()
    print("      (F11-AT-w)   endpath(G', w)  >=  rad(G') + 4     for the attachment w")
    print("                   of a DEEPEST hair.")
    print()
    print("  F11 gives that number for SOME endpoint of G'.  (F11-AT-w) asks for it at a")
    print("  PRESCRIBED endpoint.  That is the real content of A2, it is strictly weaker")
    print("  than (A2-PATH), and it is where rad >= 5 / l > 4 would have to enter.")
    if cert is None:
        return
    name, g, G, v, w, P, pg, h = cert
    gp = sub(G, peel_all(G))
    rgp = rad(gp)
    print()
    print("      on the witness: rad(G') = %s, endpath(G',w) = %d, rad(G')+4 = %s"
          % (rgp, endpath(gp, w), (rgp + 4) if rgp is not None else None))
    check("the witness ALSO fails (F11-AT-w) -- consistent, and it shows the two forms fail "
          "together rather than the anchored one being vacuous",
          endpath(gp, w) < rgp + 4, "%d < %d" % (endpath(gp, w), rgp + 4))
    print("      NOTE the witness fails F11's own hypotheses too (rad(G') = %s < 5), so this" % rgp)
    print("      is a consistency observation, NOT evidence against (F11-AT-w).  Nothing")
    print("      here proves or refutes the anchored form; it is proposed, not claimed.")
    tick("part5")


RAN = []
def main():
    print(__doc__)
    part0(); RAN.append("part0")
    part1(); RAN.append("part1")
    wit = part2(); RAN.append("part2")
    cert = part3(wit); RAN.append("part3")
    part4(cert, wit); RAN.append("part4")
    part5(cert); RAN.append("part5")
    # the guard the import defect earns: exiting 0 having skipped parts is now impossible
    check("EVERY PART RAN -- no part was skipped by a SystemExit escaping from a helper",
          RAN == ["part0", "part1", "part2", "part3", "part4", "part5"], "ran %r" % RAN)
    print("\n=== SUMMARY ===")
    print("  checks run: %d, failures: %d %s" % (NCHECK, len(FAIL), FAIL if FAIL else ""))
    print("  wall clock: %.2f s (self-limit %.0f s)" % (time.time() - T0, LIMIT))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
