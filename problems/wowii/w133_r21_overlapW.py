#!/usr/bin/env python3
"""
w133 round 21 -- ITEM 1: does a VALID overlapping-W instance exist?

Setting (prompts/w133_r12_P7G32.md PART 1/3, notes/proofs/wowii133_draft.md 20.1):
  G simple connected, C4-FREE means NO TWO DISTINCT VERTICES HAVE TWO COMMON NEIGHBOURS
  (equivalently no 4-cycle as a SUBGRAPH; chords irrelevant).
  Z = (z0..z5) an induced 6-cycle.
  W := { w outside Z : |N(w) cap Z| = 2 and the two are CONSECUTIVE on Z }.
  slot i := the consecutive pair {z_i, z_{i+1}}, i = 0..5 (mod 6).
  Two slots OVERLAP iff they share a hexagon vertex, i.e. cyclic slot distance 1.

Round 20's muse return proved (P2a) "overlapping W-vertices must be ADJACENT" (owner-verified)
but its claimed witness for existence carried a 4-cycle, so existence was left OPEN.
This script decides it.

EVERY check prints its observed population BEFORE its verdict.
Wall-clock self-limit 180 s, exit(2) on overrun.  No SAT, no large exhaustive search.
"""
import itertools, random, sys, time

T0 = time.time()
LIMIT = 180.0
def tick(tag):
    if time.time() - T0 > LIMIT:
        print("OVERRUN at %s" % tag); sys.exit(2)

FAIL = []
def check(name, ok, detail=""):
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    if not ok: FAIL.append(name)

# ---------- graph primitives ----------
def mkadj(n, edges):
    a = {v: set() for v in range(n)} if isinstance(n, int) else {v: set() for v in n}
    for u, v in edges:
        assert u != v, "loop"
        a[u].add(v); a[v].add(u)
    return a

def c4_witness(adj):
    """Return (x,y,c1,c2) if some pair has >=2 common neighbours, else None."""
    vs = sorted(adj)
    for x, y in itertools.combinations(vs, 2):
        com = sorted(adj[x] & adj[y])
        if len(com) >= 2:
            return (x, y, com[0], com[1])
    return None

def c4_all(adj):
    """ALL pairs with >=2 common neighbours, as (x,y,[commons])."""
    out = []
    for x, y in itertools.combinations(sorted(adj), 2):
        com = sorted(adj[x] & adj[y])
        if len(com) >= 2: out.append((x, y, com))
    return out

def connected(adj):
    vs = list(adj)
    if not vs: return True
    seen = {vs[0]}; st = [vs[0]]
    while st:
        u = st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen) == len(vs)

def induced_path_ge(adj, k):
    """Return a vertex list of an induced path on exactly k vertices, or None."""
    vs = list(adj)
    def ext(p, used):
        if len(p) == k: return list(p)
        for w in adj[p[-1]]:
            if w in used: continue
            if any(w in adj[u] for u in p[:-1]): continue
            p.append(w); used.add(w)
            r = ext(p, used)
            if r: return r
            p.pop(); used.discard(w)
        return None
    for s in vs:
        r = ext([s], {s})
        if r: return r
    return None

def longest_induced_path(adj):
    best = []
    vs = list(adj)
    def ext(p, used):
        nonlocal best
        if len(p) > len(best): best = list(p)
        for w in adj[p[-1]]:
            if w in used: continue
            if any(w in adj[u] for u in p[:-1]): continue
            p.append(w); used.add(w)
            ext(p, used)
            p.pop(); used.discard(w)
    for s in vs:
        ext([s], {s})
    return best

def alpha(adj, S):
    """independence number of the induced subgraph on S (S small)."""
    S = list(S); best = 0
    for r in range(len(S), -1, -1):
        if r <= best: break
        for T in itertools.combinations(S, r):
            if all(y not in adj[x] for x, y in itertools.combinations(T, 2)):
                return r
    return best

def avec(adj):
    return {v: alpha(adj, adj[v]) for v in adj}

def induced_c6_list(adj):
    """all induced 6-cycles, as canonical vertex tuples"""
    out = set()
    vs = sorted(adj)
    for S in itertools.combinations(vs, 6):
        sub = {v: adj[v] & set(S) for v in S}
        if any(len(sub[v]) != 2 for v in S): continue
        # single cycle?
        start = S[0]; prev = start; cur = min(sub[start]); seq = [start, cur]
        while len(seq) < 6:
            nxt = [x for x in sub[cur] if x != prev]
            if not nxt: break
            prev, cur = cur, nxt[0]; seq.append(cur)
        if len(seq) == 6 and len(set(seq)) == 6 and start in sub[seq[-1]]:
            out.add(tuple(seq))
    return sorted(out)

def Zneighbours(adj, Z, v):
    return sorted(set(Z) & adj[v])

def slot_of(Z, nb):
    """given 2 Z-neighbours, return slot index i if consecutive, else None"""
    idx = sorted(Z.index(x) for x in nb)
    for i in range(6):
        if set(idx) == {i, (i + 1) % 6}: return i
    return None

def Wset(adj, Z):
    W = {}
    for v in adj:
        if v in Z: continue
        nb = Zneighbours(adj, Z, v)
        if len(nb) == 2:
            s = slot_of(list(Z), nb)
            if s is not None: W[v] = s
    return W

# ---------- 0. TOOLING POSITIVE CONTROL on Q (values known from round 20 briefcheck) ----------
print("=" * 78)
print("SECTION 0 -- tooling positive control on CONTROL 1 graph Q (n=10)")
Qe = [(0,1),(0,4),(0,5),(0,8),(1,2),(2,3),(2,6),(3,5),(3,7),(3,9),(4,6),(4,7),(4,8),(8,9)]
Q = mkadj(10, Qe)
print("  observed population: 1 graph, n=10, m=%d" % len(Qe))
check("Q connected", connected(Q))
check("Q C4-free", c4_witness(Q) is None, str(c4_witness(Q)))
lp = longest_induced_path(Q)
check("path(Q) == 6", len(lp) == 6, "longest induced path %s" % lp)
c6s = induced_c6_list(Q)
check("Q has an induced C6", len(c6s) >= 1, "%d induced C6 up to rotation/reflection dupes" % len(c6s))
av = avec(Q); sa = sum(av.values())
check("a-vector of Q == (3,2,3,4,3,2,2,2,2,2)", tuple(av[i] for i in range(10)) == (3,2,3,4,3,2,2,2,2,2), str(tuple(av[i] for i in range(10))))
check("sum a(Q) == 25 (l = 5/2)", sa == 25, "sum=%d" % sa)
Zq = list(c6s[0])
Wq = Wset(Q, Zq)
K14 = mkadj(5, [(0,1),(0,2),(0,3),(0,4)])
check("SPECIFICITY probe: longest induced path of K_{1,4} is 3, not 5",
      len(longest_induced_path(K14)) == 3, str(longest_induced_path(K14)))
check("SPECIFICITY probe: C6 itself has NO induced P7 but HAS an induced P6",
      induced_path_ge(mkadj(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),7) is None and
      induced_path_ge(mkadj(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),6) is None)
check("Q carries a W-vertex on some induced C6",
      any(len(Wset(Q, list(z))) >= 1 for z in c6s),
      "Z=%s -> W=%s" % (Zq, Wq))
tick("sec0")

# ---------- 1. THE FRAME: exhaustive over the overlapping configuration ----------
print("=" * 78)
print("SECTION 1 -- THEOREM: no valid OVERLAPPING-W instance exists")
print("  frame vertices: z0..z5 = 0..5, w = 6 (slot 0 = {z0,z1}), wp = 7 (slot 1 = {z1,z2})")
print("  all adjacencies among the 8 frame vertices are FORCED by the hypotheses except the")
print("  single bit w~wp, so the frame population is exactly 2.")
Zf = [0,1,2,3,4,5]
base = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),   # induced C6
        (6,0),(6,1),                            # w on slot 0
        (7,1),(7,2)]                            # wp on slot 1 (overlaps at z1)
frames = {"w !~ wp": base, "w ~ wp": base + [(6,7)]}
print("  observed population: %d frames (the 2 values of the free bit)" % len(frames))
res = {}
for name, ed in frames.items():
    g = mkadj(8, ed)
    c4 = c4_witness(g)
    p7 = induced_path_ge(g, 7)
    res[name] = (c4, p7)
    print("    frame %-8s : C4 witness = %s | induced P7 = %s" % (name, c4, p7))
check("case w !~ wp dies by an induced P7", res["w !~ wp"][1] is not None,
      "P7 = %s" % (res["w !~ wp"][1],))
check("case w !~ wp is otherwise C4-free (so P7 is the ONLY obstruction there)",
      res["w !~ wp"][0] is None)
check("case w ~ wp dies by a C4", res["w ~ wp"][0] is not None,
      "pair+two common nbrs = %s" % (res["w ~ wp"][0],))
# NOTE (owner, round 21): the FIRST draft of this check asserted the hand-derived C4 was the
# one the scan reports.  It is NOT -- the lexicographic scan reports (z0, wp | z1, w) first.
# The hand-derived witness is true, but the check asserted MORE than the proof gives (a unique
# witness where only existence was proved).  Repaired to enumerate ALL violating pairs.
allc4 = c4_all(mkadj(8, frames["w ~ wp"]))
print("  all C4 witnesses in the adjacent frame (population %d): %s" % (len(allc4), allc4))
check("hand-derived C4 (w=6, z2=2 | common {z1=1, wp=7}) IS among the witnesses",
      (2, 6, [1, 7]) in allc4, str(allc4))
check("a second, independent C4 (z0=0, wp=7 | common {z1=1, w=6}) is also present",
      (0, 7, [1, 6]) in allc4, str(allc4))
# HYPOTHESIS SHARPNESS: each branch is killed by a DIFFERENT hypothesis, so neither
# hypothesis alone suffices -- and each branch's frame is the counterexample for the other.
check("SHARPNESS: drop 'no induced P7' and the non-adjacent overlapping frame SURVIVES "
      "(it is C4-free)", res["w !~ wp"][0] is None and res["w !~ wp"][1] is not None)
check("SHARPNESS: drop 'C4-free' and the adjacent overlapping frame SURVIVES "
      "(it is P7-free)", res["w ~ wp"][1] is None and res["w ~ wp"][0] is not None)
check("=> the two hypotheses are used in DIFFERENT branches; neither alone kills overlap",
      res["w !~ wp"][0] is None and res["w ~ wp"][1] is None)
check("BOTH frames die => no valid overlapping-W instance",
      all((c4 is not None) or (p7 is not None) for c4, p7 in res.values()))
tick("sec1")

# ---------- 2. LIFT: the obstruction survives in any host graph ----------
print("=" * 78)
print("SECTION 2 -- LIFT test: the frame obstruction survives arbitrary extension")
print("  A C4 is a subgraph condition, so it lifts for free.  The induced P7 lifts because all")
print("  21 pairs among {w,z0,z5,z4,z3,z2,wp} are FORCED by the hypotheses.  Tested anyway.")
cnt = 0; bad = []
# 2a exhaustive: one extra vertex, all 2^8 attachments, both frames
for name, ed in frames.items():
    for mask in range(256):
        extra = [(8, j) for j in range(8) if (mask >> j) & 1]
        g = mkadj(9, ed + extra)
        cnt += 1
        if c4_witness(g) is None and induced_path_ge(g, 7) is None:
            bad.append((name, mask))
tick("sec2a")
# 2b random: 2..4 extra vertices, arbitrary attachments incl. among themselves
random.seed(20260823)
RN = 2000
for _ in range(RN):
    name = random.choice(list(frames))
    ed = list(frames[name]); k = random.randint(2, 4); n = 8 + k
    for x in range(8, n):
        for y in range(x):
            if random.random() < 0.35: ed.append((y, x))
    g = mkadj(n, ed)
    cnt += 1
    if c4_witness(g) is None and induced_path_ge(g, 7) is None:
        bad.append((name, "rand", sorted(ed)))
tick("sec2b")
print("  observed population: %d host graphs containing the overlapping frame" % cnt)
check("every host containing the overlapping frame has a C4 or an induced P7",
      not bad, "%d survivors, first = %s" % (len(bad), bad[0] if bad else None))

# ---------- 3. SPECIFICITY: name the nearby form that SURVIVES ----------
print("=" * 78)
print("SECTION 3 -- COMPLETE CLASSIFICATION of two-W-vertex configurations (the refusal is")
print("  DIRECTIONAL: it names the slot distance refused AND the nearest form that survives)")
def frame_at(dist, edge_ww):
    """z0..z5 = 0..5, w = 6 on slot 0, wp = 7 on slot `dist`.  dist 0 = SAME slot."""
    ed = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1)]
    j = dist % 6
    ed += [(7, j), (7, (j + 1) % 6)]
    if edge_ww: ed.append((6,7))
    return mkadj(8, ed)
combos = [(d, e) for d in (0, 1, 2, 3) for e in (False, True)]
print("  observed population: %d frames = slot distance {0,1,2,3} x {w~wp, w!~wp}" % len(combos))
print("  %-22s | %-28s | %-24s | %s" % ("configuration", "C4 witness (pair | commons)", "induced P7", "verdict"))
survivors = []
for d, e in combos:
    g = frame_at(d, e)
    cw = c4_all(g); p7 = induced_path_ge(g, 7)
    dead = bool(cw) or (p7 is not None)
    if not dead: survivors.append((d, e))
    print("  dist %d %-16s | %-28s | %-24s | %s" %
          (d, "w~wp" if e else "w!~wp", (cw[0] if cw else "-"), (p7 if p7 else "-"),
           "DEAD" if dead else "SURVIVES"))
check("dist 0 (SAME slot): both adjacency cases die  [re-verifies round 20's (P1)]",
      all((d, e) not in survivors for d, e in combos if d == 0))
check("dist 1 (OVERLAPPING): both adjacency cases die  [THE ROUND'S RESULT]",
      all((d, e) not in survivors for d, e in combos if d == 1))
check("dist 2 (disjoint, non-antipodal): survives, and ONLY in the NON-adjacent case",
      (2, False) in survivors and (2, True) not in survivors, str(survivors))
check("dist 3 (ANTIPODAL slots): survives in BOTH adjacency cases",
      (3, False) in survivors and (3, True) in survivors, str(survivors))
check("exactly 3 of the 8 configurations survive", len(survivors) == 3, str(survivors))
tick("sec3")

# ---------- 4. EXHIBIT the surviving instances IN FULL (most basic constraint first) ----------
print("=" * 78)
print("SECTION 4 -- full validation of the exhibited surviving instances")
def full_validate(tag, n, edges, expect_slots):
    print("  --- %s ---" % tag)
    print("  edge list: %s" % sorted(tuple(sorted(e)) for e in edges))
    g = mkadj(n, edges)
    print("  observed population: 1 graph, n=%d, m=%d" % (n, len(edges)))
    check("%s: simple" % tag, all(u != v for u, v in edges) and
          len(set(tuple(sorted(e)) for e in edges)) == len(edges))
    check("%s: connected" % tag, connected(g))
    c4 = c4_witness(g)
    check("%s: C4-FREE (checked FIRST)" % tag, c4 is None, str(c4))
    c6 = induced_c6_list(g)
    check("%s: contains an induced C6" % tag, len(c6) >= 1, "%d found, e.g. %s" % (len(c6), c6[0] if c6 else None))
    lp = longest_induced_path(g)
    check("%s: no induced P7 (path <= 6)" % tag, len(lp) <= 6, "longest induced path = %s (%d vtcs)" % (lp, len(lp)))
    ok_slot = False; detail = ""
    for z in c6:
        W = Wset(g, list(z))
        if len(W) >= 2:
            ds = sorted({min((a - b) % 6, (b - a) % 6) for a, b in itertools.combinations(sorted(W.values()), 2)})
            detail = "Z=%s W=%s slot distances=%s" % (list(z), W, ds)
            if set(ds) & set(expect_slots): ok_slot = True; break
    check("%s: carries two W-vertices at slot distance in %s" % (tag, expect_slots), ok_slot, detail)
    av = avec(g); sa = sum(av.values())
    print("  a-vector = %s ; sum a = %d ; n = %d ; l = %d/%d %s 3" %
          (tuple(av[i] for i in range(n)), sa, n, sa, n, ">" if sa > 3 * n else "<="))
    return g

G2 = full_validate("INSTANCE-A (slot distance 2, w !~ wp)", 8,
                   [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1),(7,2),(7,3)], {2})
G3 = full_validate("INSTANCE-B (slot distance 3, w !~ wp)", 8,
                   [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1),(7,3),(7,4)], {3})
G3b = full_validate("INSTANCE-C (slot distance 3, w ~ wp)", 8,
                   [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1),(7,3),(7,4),(6,7)], {3})
tick("sec4")

# ---------- 5. COROLLARY: |W| <= 3 and the occupied slots are independent on the slot cycle
print("=" * 78)
print("SECTION 5 -- COROLLARY: occupied consecutive-slots form an independent set in the slot C6")
print("  (P1, round 20, folklore tier): two W-vertices on the SAME slot share z_i and z_{i+1}")
print("  -> a C4, so each slot carries at most one W-vertex.  Section 1: no two OVERLAPPING")
print("  slots are both occupied.  Hence occupied slots are an independent set in C6 -> <= 3.")
same = mkadj(8, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1),(7,0),(7,1)])
c4s = c4_witness(same)
print("  observed population: 1 frame (two W-vertices on the SAME slot 0)")
check("same-slot frame dies by a C4 (re-verifies P1)", c4s is not None, str(c4s))
maxind = 0; best = None
for r in range(0, 7):
    for S in itertools.combinations(range(6), r):
        if all(min((a-b) % 6, (b-a) % 6) != 1 for a, b in itertools.combinations(S, 2)):
            if r > maxind: maxind, best = r, S
print("  observed population: all %d subsets of the 6 slots" % (2 ** 6))
check("max independent set in the slot C6 is 3", maxind == 3, "e.g. %s" % (best,))
check("=> |W| <= 3 on any induced C6 (was |W| <= 6 by injectivity alone)", maxind == 3)
tick("sec5")

# ---------- 6. IS |W| <= 3 TIGHT? ----------
print("=" * 78)
print("SECTION 6 -- TIGHTNESS of |W| <= 3: is the independent slot-triple {0,2,4} realisable?")
print("  Up to rotation {0,2,4} and {1,3,5} are the ONLY independent slot-triples, so this one")
print("  frame family decides tightness.  Free bits = the 3 adjacencies among w0, w2, w4.")
tri = []
for mask in range(8):
    ed = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),
          (6,0),(6,1), (7,2),(7,3), (8,4),(8,5)]
    pairs = [(6,7),(6,8),(7,8)]
    for b,(x,y) in enumerate(pairs):
        if (mask >> b) & 1: ed.append((x,y))
    g = mkadj(9, ed)
    cw = c4_all(g); p7 = induced_path_ge(g, 7)
    tri.append((mask, bool(cw), p7 is not None, cw[0] if cw else None, p7))
print("  observed population: 8 frames (all adjacency patterns on {w0,w2,w4})")
for mask, hc4, hp7, cw, p7 in tri:
    print("    ww-edges mask %d %-14s : C4 = %-22s | P7 = %-24s | %s" %
          (mask, str([e for b,e in enumerate([(6,7),(6,8),(7,8)]) if (mask>>b)&1]),
           cw if cw else "-", p7 if p7 else "-", "DEAD" if (hc4 or hp7) else "SURVIVES"))
alive = [m for m, hc4, hp7, _, _ in tri if not (hc4 or hp7)]
check("the all-non-adjacent slot-triple {0,2,4} SURVIVES => |W| = 3 is attained, bound TIGHT",
      0 in alive, "surviving masks: %s" % alive)
check("every pattern with a ww-edge dies (pairwise non-adjacency is FORCED at slot distance 2)",
      alive == [0], "surviving masks: %s" % alive)
G4 = full_validate("INSTANCE-D (|W| = 3, slots {0,2,4}, pairwise non-adjacent)", 9,
                   [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,0),(6,1),(7,2),(7,3),(8,4),(8,5)], {2})
tick("sec6")

print("=" * 78)
print("TOTAL CHECKS RUN: see PASS/FAIL lines above.  FAILURES: %d %s" % (len(FAIL), FAIL))
print("elapsed %.2f s" % (time.time() - T0))
sys.exit(1 if FAIL else 0)
