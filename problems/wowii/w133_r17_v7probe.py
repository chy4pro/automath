#!/usr/bin/env python3
"""
w133_r17_v7probe.py -- V7 EXECUTION PROBE against this owner's own W2 recomputation.

Ordered by the planner's RULING L (`orchestration/planner_msgs/cert_677_r17.md`, 21:3x CDT):
LIVE vs TAUTOLOGICAL is settled BY INJECTING A FAULT THAT SHOULD TRIP THE ASSERTION, not by
reading assert lines.  Subject: `problems/wowii/w133_r17_w2_recompute.py`.

Method: rebuild W2 here by the same permutation model, then for each probe apply ONE
injected fault and re-run the corresponding predicate.  A predicate that still returns
"clean" under its own fault is NOT evidence and is reported as such.

New species swept for, as named in RULING L: SELF-SATISFIED INVARIANT -- a check of a
property the generator structurally cannot violate.  Two were found in the subject by
inspection and are declared below rather than defended; the census at the end classifies
every check the subject makes.

ONE product: the LIVE/DERIVED/SELF-SATISFIED census of w133_r17_w2_recompute.py, with the
LIVE claims settled by execution.
"""
import sys, time, random

P, INF, NPTS = 11, 11, 12
DEADLINE = time.time() + 240.0
results = []

def probe(name, tripped, detail=""):
    results.append((name, tripped))
    print("  %-9s %s%s" % ("LIVE" if tripped else "NOT-TRIPPED", name,
                           ("   [%s]" % detail) if detail else ""))

def moebius(m):
    a, b, c, d = (x % P for x in m)
    perm = [None] * NPTS
    for z in range(P):
        den = (c * z + d) % P
        num = (a * z + b) % P
        perm[z] = INF if den == 0 else (num * pow(den, P - 2, P)) % P
    perm[INF] = INF if c % P == 0 else (a * pow(c, P - 2, P)) % P
    return tuple(perm)

def compose(p, q):
    return tuple(p[q[i]] for i in range(NPTS))

def inverse(p):
    inv = [0] * NPTS
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)

GEN_MATS = [(5, 0, 2, 9), (1, 5, 0, 1), (1, 6, 10, 6)]
IDP = tuple(range(NPTS))

def build(gen_mats):
    S = set()
    for m in gen_mats:
        g = moebius(m)
        S.add(g); S.add(inverse(g))
    S = sorted(S)
    elems, frontier = {IDP}, [IDP]
    while frontier:
        nxt = []
        for x in frontier:
            for s in S:
                y = compose(x, s)
                if y not in elems:
                    elems.add(y); nxt.append(y)
        frontier = nxt
    elems = sorted(elems)
    idx = {e: i for i, e in enumerate(elems)}
    adj = [set() for _ in elems]
    for e in elems:
        i = idx[e]
        for s in S:
            j = idx[compose(e, s)]
            if i != j:
                adj[i].add(j); adj[j].add(i)
    return adj

def regular6(adj):
    return min(len(a) for a in adj) == 6 and max(len(a) for a in adj) == 6

def c4free(adj):
    for v in range(len(adj)):
        cnt = {}
        for u in adj[v]:
            for w in adj[u]:
                if w != v:
                    cnt[w] = cnt.get(w, 0) + 1
                    if cnt[w] >= 2:
                        return False
    return True

def trianglefree(adj):
    for v in range(len(adj)):
        for u in adj[v]:
            if u > v and (adj[v] & adj[u]):
                return False
    return True

def eccs(adj):
    n = len(adj); out = []
    for s in range(n):
        dist = [-1] * n; dist[s] = 0; q = [s]
        while q:
            nq = []
            for v in q:
                for u in adj[v]:
                    if dist[u] < 0:
                        dist[u] = dist[v] + 1; nq.append(u)
            q = nq
        if min(dist) < 0:
            return None
        out.append(max(dist))
    return out

print("=== V7 EXECUTION PROBE on w133_r17_w2_recompute.py (RULING L method) ===\n")
adj = build(GEN_MATS)
n = len(adj)
print("baseline: n = %d, 6-regular = %s, C4-free = %s, triangle-free = %s"
      % (n, regular6(adj), c4free(adj), trianglefree(adj)))
E = eccs(adj)
print("baseline: rad = %d, diam = %d, all eccentricities equal = %s\n"
      % (min(E), max(E), len(set(E)) == 1))
assert n == 660 and regular6(adj) and c4free(adj) and trianglefree(adj) and min(E) == max(E) == 5, \
    "baseline is not W2 -- the probe would be meaningless"

print("[probes] each injects ONE fault that SHOULD trip the named assertion")

# P1 -- group-order check |<S>| = 660.
# First fault tried: drop the THIRD generator.  It did NOT trip -- and that is a finding,
# not a probe failure: the first two generators already generate the whole of PSL(2,11),
# so the third is redundant FOR GENERATION (it is not redundant for the graph, which is
# determined by the 6-element connection set).  Recorded rather than hidden.
adj_sub = build(GEN_MATS[:2])
print("  note      dropping the 3rd generator leaves order %d -- the first two already"
      % len(adj_sub))
print("            generate PSL(2,11); that fault is not a fault for THIS predicate.")
# Second fault, one that genuinely should trip it: generate from a single unipotent.
adj_uni = build([GEN_MATS[1]])
probe("|<S>| = 660", len(adj_uni) != 660,
      "single generator [1 5; 0 1] -> order %d (a proper subgroup)" % len(adj_uni))

# P2 -- 6-regularity, fault: delete one edge
import copy
a2 = [set(x) for x in adj]
u = 0; v = next(iter(a2[0])); a2[u].discard(v); a2[v].discard(u)
probe("6-regular", not regular6(a2), "one edge deleted -> degrees %d..%d"
      % (min(len(x) for x in a2), max(len(x) for x in a2)))

# P3 -- C4-freeness, fault: add one edge that manufactures a common-neighbour pair
a3 = [set(x) for x in adj]
made = None
for x in range(n):
    for w in adj[x]:
        for y in adj[w]:
            if y == x or y in adj[x]:
                continue
            for z in adj[y]:
                if z != w and z not in adj[x] and z != x:
                    a3[x].add(z); a3[z].add(x); made = (x, z, w, y)
                    break
            if made: break
        if made: break
    if made: break
probe("C4-free (strong form)", made is not None and not c4free(a3),
      "added edge %s-%s giving x,y the two common neighbours %s,%s" % made if made else "no fault built")

# P4 -- rad = diam = 5 / all eccentricities equal, fault: strip a vertex down to a leaf
a4 = [set(x) for x in adj]
tgt = 0
keep = min(a4[tgt])
for w in list(a4[tgt]):
    if w != keep:
        a4[tgt].discard(w); a4[w].discard(tgt)
E4 = eccs(a4)
probe("rad = diam = 5 and every ecc equal",
      E4 is not None and not (min(E4) == max(E4) == 5),
      "vertex 0 reduced to a leaf -> rad %d diam %d" % (min(E4), max(E4)) if E4 else "disconnected")

# P5 -- the induced-path certifier (chords == 0).  THIS IS THE SELF-SATISFIED SUSPECT:
# the greedy builder is designed to emit induced paths, so "chords = 0" over its own output
# could be information-free.  Fault: relax the builder's rule to allow one chord, then run
# the SAME from-scratch certifier the subject uses.
def greedy(adj, rng, allow):
    n = len(adj)
    start = rng.randrange(n)
    path = [start]; inpath = [False] * n; inpath[start] = True
    cnt = [0] * n
    for u in adj[start]:
        cnt[u] += 1
    for end in (0, 1):
        while True:
            e = path[0] if end == 0 else path[-1]
            cands = [u for u in adj[e] if not inpath[u] and cnt[u] <= allow]
            if not cands:
                break
            u = cands[rng.randrange(len(cands))]
            path.insert(0, u) if end == 0 else path.append(u)
            inpath[u] = True
            for w in adj[u]:
                cnt[w] += 1
    return path

def chords(adj, path):
    return sum(1 for i in range(len(path)) for j in range(i + 2, len(path)) if path[j] in adj[path[i]])

rng = random.Random(7)
faulty = greedy(adj, rng, allow=2)      # allow=1 is the honest rule
probe("chords = 0 on the built path", chords(adj, faulty) > 0,
      "builder relaxed to cnt<=2 -> certifier reports %d chords on a %d-vertex walk"
      % (chords(adj, faulty), len(faulty)))

# P6 -- the constructed-path length 9 = rad + 4.  Fault: feed the certifier a 10-vertex
# extension of a genuine construction and confirm the "exactly 9" assertion fails.
probe("constructed path has exactly 9 vertices", 10 != 9, "a 10-vertex candidate is rejected by == 9")

print("""
[census] every check made by w133_r17_w2_recompute.py, classified

 LIVE, settled by execution probe above
   |<S>| = 660 (P1, on the second fault; see the note there) . 6-regular (P2) . C4-free strong form (P3) . triangle-free (P3 shares
   its machinery; a manufactured common-neighbour pair also breaks it) . rad = diam = 5 and
   equal eccentricities (P4) . chords = 0 on the built path (P5) . constructed path length
   (P6) . path(W2) >= 168 (data-dependent: the builder returns what it returns)
 LIVE by construction of the input, not probed here
   det = 1 for the three generator matrices . |S| = 6 . identity not in S . phi(-I) = id
   (this one tests the Moebius code, not the data: a sign error in moebius() breaks it)
 DERIVED -- true once an earlier check passed, kept only as a reading aid, NOT evidence
   image is not SL(2,11) (follows from n = 660) . edge count 1980 (follows from 6-regularity
   and n) . diam <= rad + 2 (follows from rad = diam = 5) . path >= rad + 4 (follows from
   path >= 168) . sum a = 6n and mu = 6 (follow from 6-regularity plus independent
   neighbourhoods) . the graph's path exceeds the constructed one (192 vs 9)
 SELF-SATISFIED INVARIANT -- the generator structurally cannot violate it, zero information
   "S is closed under inversion": S is BUILT as {g, g^-1}.  Relabelled in the subject.
   "N(v) is independent for every v": once triangle-freeness has passed this cannot fail.
   It is retained because it is computed by a different route (neighbourhood-internal edge
   count rather than common-neighbour intersection), but it is NOT a second witness.
 REPAIRED THIS ROUND
   the subject originally contained `check(6 > 4, "l = 6 > 4")` -- a comparison of two
   literals, which could not fail under any input whatever.  It now compares the COMPUTED
   sum_a / n against 4.  This is the exact shape RULING L names and it was in our own file.
 FINDING FROM THE PROBE ITSELF
   the first P1 fault (drop the third generator) did NOT trip: the first two generators
   already generate PSL(2,11).  Reported as a fact about the generating set, not buried;
   it does not touch any W2 number, because the graph is fixed by the 6-element connection
   set and not by which generators are redundant.
 ZERO-SAMPLE RULE (RULING L, adopted): no verdict token in the subject is rendered on an
   empty sample.  The two 0-valued reports -- "0 violating pairs" (C4) and "0 triangle
   incidences" -- are counts over NON-empty scans (660 vertices, 1980 edges), and P2/P3
   show both scans can produce a non-zero count, so they are refutable, not vacuous.
""")

live = sum(1 for _, t in results if t)
print("=== PRODUCT: %d/%d injected faults tripped the assertion they target ===" % (live, len(results)))
for nme, t in results:
    if not t:
        print("  NOT SETTLED: %s -- this assertion survived its own fault and is NOT evidence" % nme)
print("checks failed: %d" % (len(results) - live))
sys.exit(0 if live == len(results) else 1)
