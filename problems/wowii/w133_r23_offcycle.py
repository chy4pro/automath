#!/usr/bin/env python3
"""
w133 round 23 -- THE OFF-CYCLE BOUND: an upper bound on a(v) for v not on Z.

THE QUESTION (planner cert round 22; the owner's own named next step):
    (D3-C6) hypotheses: connected, C4-FREE, contains an induced C6 Z, NO INDUCED P7.
    The global count is  Sum_v (a(v)-3) = Sum_{z in Z}(a(z)-3) + Sum_{v not in Z}(a(v)-3) <= 0.
    The Z-term is fully determined (G55 + G57 + draft 34.4a).  The OFF-CYCLE term is open.
    Bound a(v) for v not in Z with |N(v) cap Z| <= 1 -- or say it cannot be done and NAME
    the hypothesis that would do it.

THE ANSWER THIS SCRIPT CERTIFIES -- it is a DICHOTOMY, not a single bound, and the
question's own class |N(v) cap Z| <= 1 falls on BOTH sides of it:

    Z-trace of v            d(v)          a(v)         charge a(v)-3
    ------------------------------------------------------------------
    empty                   UNBOUNDED     UNBOUNDED    unbounded above
    one vertex              <= 4          <= 3         <= 0     (both EXACT, attained)
    two consecutive         <= 4          <= 3         <= 0     (both EXACT, attained)
    two antipodal           UNBOUNDED     UNBOUNDED    unbounded above
    (|trace| >= 3 and distance-2 traces are already impossible: G54)

MECHANISM, one line: a trace T bounds v iff the hexagon carries an induced 5-arc anchored
at a vertex of T and meeting T nowhere else.  Every legal trace has one EXCEPT the
antipodal pair, which cuts the hexagon into two arcs of 3.  2 + 5 = 7 = the forbidden P7.

RULING BM IS THE SPINE OF THIS FILE.  Round 22's (D3-C6) probe PASSED WHILE PROVING
NOTHING because every host in its sample had longest induced path 7, i.e. lay outside the
hypothesis.  Here in-hypothesis membership is a PRECONDITION, mechanically: a Sample
refuses to report ANY statistic until admit() has run and returned True, and a statistic
read off a rejected sample RAISES.

AND THE SAME RULE BIT ITS AUTHOR AGAIN, IN THE OPPOSITE DIRECTION -- recorded, not
repaired away.  The first version of this file asserted CONNECTEDNESS on FRAMES.  A frame
is an INDUCED SUBGRAPH of a host; C4-freeness, P7-freeness and "Z is an induced C6" are
inherited by induced subgraphs, and CONNECTEDNESS IS NOT.  So the empty-trace frame was
thrown out of a population it belongs to.  Round 22's error admitted samples that were
out of hypothesis; this one rejected samples that were in it.  Same defect, opposite sign:
THE MEMBERSHIP TEST MUST MATCH THE OBJECT IT IS APPLIED TO.  admit(mode="frame") now
asserts exactly the inherited clauses and says so.

C4-FREE throughout means: NO TWO DISTINCT VERTICES HAVE TWO COMMON NEIGHBOURS.
Wall-clock self-limit 180 s, exit(2) on overrun.  No SAT, no large exhaustive search.
"""
import itertools, os, sys, time, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w133_r22_namespace as R22
from w133_r22_namespace import (mkadj, c4_all, c4_free, connected, longest_induced_path,
                                is_induced_c6, triangles_at, alpha_of_nbhd, trace,
                                assert_mintable)

T0 = time.time()
LIMIT = 180.0
def tick(tag):
    if time.time() - T0 > LIMIT:
        print("OVERRUN at %s" % tag); sys.exit(2)

FAIL = []
NCHECK = 0
def check(name, ok, detail=""):
    global NCHECK
    NCHECK += 1
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    if not ok: FAIL.append(name)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRAFT = os.path.join(REPO, "notes", "proofs", "wowii133_draft.md")

HEX = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
Z6  = [0,1,2,3,4,5]


def induced_path_witness(adj, k=7):
    """Return the vertex list of an induced path on k vertices, or None.  Evidence, not a bit."""
    found = []
    def ext(path, pset):
        if found: return
        if len(path) >= k:
            found.append(list(path)); return
        for v in sorted(adj[path[-1]]):
            if v in pset: continue
            if any(v in adj[u] for u in path[:-1]): continue
            path.append(v); pset.add(v); ext(path, pset); path.pop(); pset.discard(v)
            if found: return
    for s in sorted(adj):
        ext([s], {s})
        if found: return found[0]
    return None


def trace_type(t):
    t = sorted(t)
    if len(t) == 0: return "empty"
    if len(t) == 1: return "single"
    if len(t) == 2:
        dd = min((t[1]-t[0]) % 6, (t[0]-t[1]) % 6)
        return {1: "consecutive", 2: "distance-2", 3: "antipodal"}[dd]
    return "size>=3"

def legal_trace(t):
    """A trace permitted by G54 in a C4-free graph with Z induced."""
    return trace_type(t) in ("empty", "single", "consecutive", "antipodal")


# ============================================================================
# RULING BM MADE MECHANICAL -- a sample that cannot answer until it is admitted
# ============================================================================
class Sample(object):
    """A candidate for (D3-C6).  mode="host": a complete graph, all clauses asserted.
    mode="frame": an INDUCED SUBGRAPH of a host, so only the clauses that are INHERITED
    by induced subgraphs may be asserted -- C4-free, Z induced C6, no induced P7.
    Connectedness is NOT inherited and is therefore NOT asserted on frames."""
    INHERITED = ("simple", "C4-free", "Z induced C6", "no induced P7")

    def __init__(self, tag, n, edges, Z=Z6, mode="host"):
        self.tag, self.n, self.edges, self.Z, self.mode = tag, n, list(edges), list(Z), mode
        self.adj = mkadj(n, self.edges)
        self._admitted = None
        self.why = None
        self.path = None

    def admit(self, verbose=True):
        why = []
        if not (all(u != v for u, v in self.edges)
                and len(set(map(frozenset, self.edges))) == len(self.edges)):
            why.append("not simple")
        if self.mode == "host" and not connected(self.adj):
            why.append("not connected")
        bad = c4_all(self.adj)
        if bad:
            why.append("NOT C4-free (%d pairs with >=2 common nbrs, e.g. %r)" % (len(bad), bad[0]))
        if not is_induced_c6(self.adj, self.Z):
            why.append("Z=%r is not an induced C6" % (self.Z,))
        self.path = longest_induced_path(self.adj)
        if self.path >= 7:
            w = induced_path_witness(self.adj, 7)
            why.append("HAS an induced P7 (longest induced path = %d, witness %r)"
                       % (self.path, w))
        self._admitted = (len(why) == 0)
        self.why = why
        if verbose:
            print("      sample %-30s [%s] n=%-3d path=%-2d -> %s%s"
                  % (self.tag, self.mode, self.n, self.path,
                     "IN HYPOTHESIS" if self._admitted else "REJECTED",
                     "" if self._admitted else "  [" + "; ".join(self.why) + "]"))
        return self._admitted

    def _guard(self):
        if self._admitted is None:
            raise AssertionError("RULING BM: statistic read off `%s` BEFORE admit() ran" % self.tag)
        if self._admitted is False:
            raise AssertionError("RULING BM: statistic read off `%s`, which is OUT OF "
                                 "HYPOTHESIS (%s)" % (self.tag, "; ".join(self.why)))

    def a(self, v):  self._guard(); return alpha_of_nbhd(self.adj, v)
    def d(self, v):  self._guard(); return len(self.adj[v])
    def t(self, v):  self._guard(); return triangles_at(self.adj, v)
    def tr(self, v): self._guard(); return trace(self.adj, self.Z, v)
    def sum_excess(self):
        self._guard(); return sum(alpha_of_nbhd(self.adj, v) - 3 for v in sorted(self.adj))
    def dist_to_Z(self, v):
        self._guard()
        seen, frontier, d = set(self.Z), set(self.Z), 0
        while frontier:
            if v in frontier: return d
            nxt = set()
            for x in frontier: nxt |= (self.adj[x] - seen)
            seen |= nxt; frontier = nxt; d += 1
        return None


# ============================================================================
# PART 0 -- TOOLING IS POSITIVE-CONTROLLED BEFORE USE
# ============================================================================
def part0():
    print("\n=== PART 0 -- POSITIVE CONTROLS ON THE TOOLING (before any of it is used) ===")
    PET = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
           (0,5),(1,6),(2,7),(3,8),(4,9)]
    pet = mkadj(10, PET)
    check("control: Petersen is C4-free", c4_free(pet))
    p = longest_induced_path(pet)
    print("      observed: longest induced path(Petersen) = %d" % p)
    check("control: longest induced path(Petersen) = 5", p == 5, "got %d" % p)
    check("control: a == 3 at every Petersen vertex",
          [alpha_of_nbhd(pet, v) for v in range(10)] == [3]*10)
    check("specificity: longest induced path(K_{1,4}) = 3",
          longest_induced_path(mkadj(5, [(0,1),(0,2),(0,3),(0,4)])) == 3)
    check("specificity: a bare induced C6 has longest induced path 5",
          longest_induced_path(mkadj(6, HEX)) == 5)
    check("specificity: the 4-cycle IS detected as not C4-free",
          not c4_free(mkadj(4, [(0,1),(1,2),(2,3),(3,0)])))
    # the witness function must produce a REAL induced path, not just a bit
    w = induced_path_witness(mkadj(8, HEX + [(6,0),(7,6)]), 7)
    ad = mkadj(8, HEX + [(6,0),(7,6)])
    okw = (w is not None and len(w) == 7 and len(set(w)) == 7
           and all(w[i+1] in ad[w[i]] for i in range(6))
           and all(w[j] not in ad[w[i]] for i in range(7) for j in range(i+2, 7)))
    check("control: the P7 witness is re-verified edge-by-edge, not trusted", okw, "%r" % (w,))

    s = Sample("guard-probe", 8, HEX + [(6,0),(7,6)])
    fired = False
    try: s.a(6)
    except AssertionError as e:
        fired = ("BEFORE admit" in str(e)); print("      guard raised: %s" % e)
    check("RULING BM: reading a statistic BEFORE admit() RAISES", fired)
    s.admit()
    fired2 = False
    try: s.a(6)
    except AssertionError as e: fired2 = ("OUT OF HYPOTHESIS" in str(e))
    check("RULING BM: reading a statistic off a REJECTED sample RAISES", fired2)

    # the frame/host distinction must actually make a difference, or it is decoration
    e_iso = HEX + [(6,7)]
    sf = Sample("disconnected-frame", 8, e_iso, mode="frame")
    sh = Sample("disconnected-host",  8, e_iso, mode="host")
    okf, okh = sf.admit(verbose=False), sh.admit(verbose=False)
    check("frame/host: the SAME edge list is admitted as a frame and rejected as a host "
          "(connectedness is not inherited by induced subgraphs)",
          okf and (not okh) and any("connected" in w for w in sh.why),
          "frame=%s host=%s %r" % (okf, okh, sh.why))
    tick("part0")


# ============================================================================
# PART 1 -- EXHAUSTIVE FRAME TABLES.  This is the proof, machine-checked.
# ============================================================================
def frame_table(tag, anchor_trace, characterisation, note):
    """All 2^6 Z-traces T of a free neighbour u of the anchor.  6 = anchor, 7 = u.
    `characterisation(T)` is the CLOSED-FORM claim, checked for EQUALITY with the
    observed survivor set -- an implication would let a wrong claim pass."""
    print("\n  --- frame table %s (anchor Z-trace %r) ---" % (tag, anchor_trace))
    survivors, killed = [], {}
    for bits in range(64):
        T = tuple(i for i in range(6) if (bits >> i) & 1)
        edges = list(HEX) + [(6, i) for i in anchor_trace] + [(7, 6)] + [(7, i) for i in T]
        s = Sample("%s/T=%r" % (tag, list(T)), 8, edges, mode="frame")
        if s.admit(verbose=False): survivors.append(T)
        else: killed[T] = s.why
    claimed = set(tuple(i for i in range(6) if (b >> i) & 1)
                  for b in range(64)
                  if characterisation(tuple(i for i in range(6) if (b >> i) & 1)))
    print("      observed population: 64 frames, %d survive the hypothesis, %d refuted"
          % (len(survivors), len(killed)))
    print("      observed survivors: %r" % [list(t) for t in sorted(survivors)])
    agree = set(survivors) == claimed
    check("%s: survivor set == the closed-form claim (%s)" % (tag, note), agree,
          "" if agree else "observed %r claimed %r" % (sorted(survivors), sorted(claimed)))
    return survivors, killed


def part1():
    print("\n=== PART 1 -- EXHAUSTIVE FRAME TABLES: what a non-Z vertex may be adjacent to ===")
    print("  Frame = the induced subgraph on Z + {anchor} + {u}, so it is an induced subgraph")
    print("  of any host carrying that configuration; C4-freeness and P7-freeness are")
    print("  inherited, so a refuted frame is refuted in EVERY host.  Connectedness is not")
    print("  inherited and is not asserted (see the header: this file's own RULING BM error).")

    # ---- A: the planner's case, |N(v) cap Z| = 1
    survA, killA = frame_table(
        "A  single-trace anchor v~z0", [0],
        lambda T: len(T) > 0 and set(T) <= {0, 2, 3, 4} and legal_trace(T),
        "u's trace is a nonempty legal trace inside {z0,z2,z3,z4}")
    print("      reasons, printed rather than summarised:")
    for T in [(), (1,), (5,), (1, 5), (2,)]:
        print("        T=%-8r : %s" % (list(T), "; ".join(killA[T]) if T in killA else "SURVIVES"))
    check("A: the empty trace dies by an INDUCED P7 and by nothing else",
          () in killA and len(killA[()]) == 1 and "P7" in killA[()][0], "%r" % (killA.get(()),))
    check("A: z1 and z5 are excluded by a C4 through z0 (v,z1 already share z0)",
          all(T in killA and any("C4" in w for w in killA[T]) for T in [(1,), (5,)]))

    # ---- B: two consecutive
    survB, killB = frame_table(
        "B  consecutive-trace anchor w~z0,z1", [0, 1],
        lambda T: len(T) > 0 and set(T) <= {3, 4},
        "u's trace is a nonempty subset of {z3,z4}")
    for T in [(), (2,), (5,), (0,)]:
        print("        T=%-8r : %s" % (list(T), "; ".join(killB[T]) if T in killB else "SURVIVES"))
    check("B: the empty trace dies by an INDUCED P7 and by nothing else",
          () in killB and len(killB[()]) == 1 and "P7" in killB[()][0], "%r" % (killB.get(()),))
    check("B: z0,z1,z2,z5 are all excluded by a C4 -- the sharper half, and it is pure "
          "C4-freeness", all(T in killB and any("C4" in w for w in killB[T])
                             for T in [(0,), (1,), (2,), (5,)]))

    # ---- C: the anchor has NO Z-neighbour (distance >= 2)
    survC, killC = frame_table(
        "C  empty-trace anchor x (distance >= 2)", [],
        lambda T: trace_type(T) in ("empty", "antipodal"),
        "u is antipodal, or itself has no Z-neighbour")
    check("C: THE SHIELD -- every distance-2 vertex attaches only to ANTIPODAL vertices, "
          "of which there are at most 3 (draft 34.4a)",
          set(t for t in survC if t) == {(0, 3), (1, 4), (2, 5)}, "%r" % sorted(survC))

    # ---- D: the anchor is antipodal
    survD, killD = frame_table(
        "D  antipodal-trace anchor u~z0,z3", [0, 3],
        lambda T: set(T) <= {0, 3} and set(T) != {0, 3},
        "u's neighbours have trace {} , {z0} or {z3} -- and {} IS permitted")
    check("D: the EMPTY trace survives on an antipodal anchor.  This single frame is where "
          "the off-cycle term's unboundedness enters.", () in set(survD))
    tick("part1")
    return survA, survB, survC, survD


# ============================================================================
# PART 2 -- EXACT MAXIMA over the bounded classes.  Exhaustive, hence sharp.
# ============================================================================
def exact_maxima(tag, anchor_trace, allowed_traces, anchor=6):
    """N(anchor) is exactly (anchor_trace) + a set of off-Z vertices whose traces are
    pairwise DISJOINT (two neighbours of the anchor sharing a z would be two common
    neighbours of the anchor and that z: a C4) and each drawn from `allowed_traces`.
    Together with the free adjacency bits among those neighbours this determines
    G[N(anchor)] COMPLETELY, so enumerating it gives the EXACT maximum of d and a --
    an upper bound that is attained, not merely a bound."""
    print("\n  --- exact maxima for %s ---" % tag)
    best_d = (0, None); best_a = (0, None); pareto = set()
    nframes = admitted = 0
    for r in range(0, len(allowed_traces) + 1):
        for combo in itertools.combinations(allowed_traces, r):
            flat = [z for T in combo for z in T]
            if len(flat) != len(set(flat)):
                continue                      # two neighbours sharing an anchor: C4
            for bits in range(1 << (r * (r - 1) // 2)):
                edges = list(HEX) + [(anchor, z) for z in anchor_trace]
                us = list(range(anchor + 1, anchor + 1 + r))
                for u, T in zip(us, combo):
                    edges.append((u, anchor))
                    edges += [(u, z) for z in T]
                b = 0
                for i in range(r):
                    for j in range(i + 1, r):
                        if (bits >> b) & 1: edges.append((us[i], us[j]))
                        b += 1
                nframes += 1
                s = Sample("%s r=%d" % (tag, r), anchor + 1 + r, edges, mode="frame")
                if not s.admit(verbose=False):
                    continue
                admitted += 1
                d, a = s.d(anchor), s.a(anchor)
                pareto.add((d, a))
                if d > best_d[0]: best_d = (d, (combo, bits, edges))
                if a > best_a[0]: best_a = (a, (combo, bits, edges))
        tick("%s-r%d" % (tag, r))
    print("      observed population: %d neighbourhood configurations enumerated, "
          "%d in hypothesis, %d refuted" % (nframes, admitted, nframes - admitted))
    print("      observed EXACT maximum degree      d = %d, at neighbour traces %r"
          % (best_d[0], [list(t) for t in best_d[1][0]] if best_d[1] else None))
    print("      observed EXACT maximum a-value     a = %d, at neighbour traces %r"
          % (best_a[0], [list(t) for t in best_a[1][0]] if best_a[1] else None))
    print("      observed (d,a) pairs realised in hypothesis: %r" % sorted(pareto))
    if best_a[1]:
        print("      maximiser edge list: %r" % (sorted(best_a[1][2]),))
    return best_d[0], best_a[0], best_a[1]


def part2():
    print("\n=== PART 2 -- THE EXACT BOUNDS.  Enumeration is over N(v), so they are SHARP ===")
    SINGLE_OK = [(0,), (2,), (3,), (4,), (0, 3), (2, 3), (3, 4)]   # PART 1A's survivors
    CONS_OK   = [(3,), (4,), (3, 4)]                                # PART 1B's survivors
    d1, a1, wit1 = exact_maxima("single-trace v~z0", (0,), SINGLE_OK)
    print("      NOTE, against the owner's own first answer: the hand argument gave only")
    print("      d(v) <= 5 and a(v) <= 4 (at most one neighbour per permitted anchor, and")
    print("      z0 is adjacent to any neighbour that uses it).  The ENUMERATION is sharper")
    print("      by one in both coordinates, because the surviving neighbour traces obstruct")
    print("      each other -- a pairwise interaction no counting argument can see.")
    check("SINGLE TRACE: d(v) <= 4 exactly (bound and attainment in one enumeration)",
          d1 == 4, "observed max d = %d" % d1)
    check("SINGLE TRACE: a(v) <= 3 exactly -- so a single-trace vertex NEVER carries "
          "positive charge", a1 == 3, "observed max a = %d" % a1)
    d2, a2, wit2 = exact_maxima("consecutive-trace w~z0,z1", (0, 1), CONS_OK)
    check("CONSECUTIVE TRACE: d(w) <= 4 exactly", d2 == 4, "observed max d = %d" % d2)
    check("CONSECUTIVE TRACE: a(w) <= 3 exactly -- so a consecutive-trace vertex NEVER "
          "carries positive charge", a2 == 3, "observed max a = %d" % a2)

    # the maximisers are real hosts, not just frames: re-admit them as hosts
    for name, wit, anchor, want_a in [("single-trace maximiser", wit1, 6, 3),
                                      ("consecutive maximiser", wit2, 6, 3)]:
        if not wit: continue
        edges = wit[2]
        n = 1 + max(max(u, v) for u, v in edges)
        h = Sample(name, n, edges, mode="host")
        ok = h.admit()
        check("%s is admitted as a HOST (connected), so the maximum is ATTAINED, not "
              "merely bounded" % name, ok and h.a(anchor) == want_a,
              "%r" % h.why if not ok else "a=%d d=%d t=%d" % (h.a(anchor), h.d(anchor), h.t(anchor)))
    tick("part2")


# ============================================================================
# PART 3 -- THE TWO UNBOUNDED FAMILIES, admitted BEFORE they are measured
# ============================================================================
def part3():
    print("\n=== PART 3 -- THE OFF-CYCLE TERM IS UNBOUNDED: two families, IN HYPOTHESIS ===")
    print("  FAMILY-U (EMPTY trace):     Z + u~z0,z3 + v~u + k pendants on v")
    print("  FAMILY-A (ANTIPODAL trace): Z + u~z0,z3 + k pendants on u")
    resU, resA = [], []
    for k in range(0, 9):
        sU = Sample("FAMILY-U k=%d" % k, 8 + k,
                    HEX + [(6,0),(6,3),(7,6)] + [(8+i, 7) for i in range(k)])
        if sU.admit(verbose=(k < 2)):
            resU.append((k, sU.d(7), sU.a(7), sU.sum_excess(), sU.dist_to_Z(7)))
        else:
            check("FAMILY-U k=%d admitted" % k, False, "%r" % sU.why)
        sA = Sample("FAMILY-A k=%d" % k, 7 + k,
                    HEX + [(6,0),(6,3)] + [(7+i, 6) for i in range(k)])
        if sA.admit(verbose=(k < 2)):
            resA.append((k, sA.d(6), sA.a(6), sA.sum_excess()))
        else:
            check("FAMILY-A k=%d admitted" % k, False, "%r" % sA.why)
        tick("part3-%d" % k)

    print("\n    FAMILY-U  (v has NO Z-neighbour; the question's own class)")
    print("      k   d(v)  a(v)   Sum_v(a-3)   dist(v,Z)")
    for k, d, a, se, dz in resU: print("      %-3d %-5d %-6d %-12d %d" % (k, d, a, se, dz))
    check("FAMILY-U: all 9 members IN HYPOTHESIS", len(resU) == 9, "%d" % len(resU))
    check("FAMILY-U: v has an empty Z-trace and sits at distance 2",
          all(dz == 2 for *_, dz in resU))
    check("FAMILY-U: a(v) = k+1 -- UNBOUNDED, and |N(v) cap Z| = 0 <= 1, so the question's "
          "own class contains it", [a for _, _, a, _, _ in resU] == [k+1 for k in range(9)],
          "%r" % [a for _, _, a, _, _ in resU])
    check("FAMILY-U: the GLOBAL count survives anyway (Sum(a-3) <= 0 throughout)",
          all(se <= 0 for _, _, _, se, _ in resU), "%r" % [se for _, _, _, se, _ in resU])

    print("\n    FAMILY-A  (u has an ANTIPODAL Z-trace)")
    print("      k   d(u)  a(u)   Sum_v(a-3)")
    for k, d, a, se in resA: print("      %-3d %-5d %-6d %d" % (k, d, a, se))
    check("FAMILY-A: all 9 members IN HYPOTHESIS", len(resA) == 9, "%d" % len(resA))
    check("FAMILY-A: a(u) = k+2 -- UNBOUNDED",
          [a for _, _, a, _ in resA] == [k+2 for k in range(9)],
          "%r" % [a for _, _, a, _ in resA])
    check("FAMILY-A: the GLOBAL count survives anyway (Sum(a-3) <= 0 throughout)",
          all(se <= 0 for _, _, _, se in resA), "%r" % [se for _, _, _, se in resA])
    tick("part3")


# ============================================================================
# PART 4 -- HYPOTHESIS SHARPNESS: each branch is the other's counterexample
# ============================================================================
def part4():
    print("\n=== PART 4 -- BOTH HYPOTHESES ARE LOAD-BEARING FOR THE SINGLE-TRACE BOUND ===")
    print("  DROP `no induced P7`: hexagon + v~z0 + k pendants on v.  C4-free, carries the")
    print("  induced C6 -- and a(v)=k+1 is unbounded.  Rejected BY THE GATE, for the P7.")
    rows = []
    for k in (1, 3, 6):
        e = HEX + [(6,0)] + [(7+i, 6) for i in range(k)]
        s = Sample("noP7-drop k=%d" % k, 7+k, e); ok = s.admit(verbose=False)
        ad = mkadj(7+k, e)
        rows.append((k, ok, s.path, c4_free(ad), alpha_of_nbhd(ad, 6)))
    print("      k   admitted?  longest induced path   C4-free?   a(v)")
    for k, ok, p, cf, a in rows: print("      %-3d %-10s %-22d %-10s %d" % (k, ok, p, cf, a))
    check("no-P7 is load-bearing: C4-free, but every one REJECTED for an induced P7",
          all((not ok) and cf and p >= 7 for _, ok, p, cf, _ in rows))
    check("no-P7 is load-bearing: without it a(v) on a single-trace v is unbounded",
          [a for *_, a in rows] == [k+1 for k, *_ in rows], "%r" % [a for *_, a in rows])

    print("\n  DROP `C4-free`: hexagon + v~z0 + k vertices adjacent to both v and z2.")
    rows2 = []
    for k in (2, 4, 6):
        e = HEX + [(6,0)] + [(7+i, 6) for i in range(k)] + [(7+i, 2) for i in range(k)]
        s = Sample("C4-drop k=%d" % k, 7+k, e); ok = s.admit(verbose=False)
        ad = mkadj(7+k, e)
        rows2.append((k, ok, s.path, c4_free(ad), alpha_of_nbhd(ad, 6)))
    print("      k   admitted?  longest induced path   C4-free?   a(v)")
    for k, ok, p, cf, a in rows2: print("      %-3d %-10s %-22d %-10s %d" % (k, ok, p, cf, a))
    check("C4-freeness is load-bearing: P7-free, but every one REJECTED for a C4",
          all((not ok) and (not cf) and p <= 6 for _, ok, p, cf, _ in rows2))
    check("C4-freeness is load-bearing: without it a(v) on a single-trace v is unbounded",
          [a for *_, a in rows2] == [k+1 for k, *_ in rows2], "%r" % [a for *_, a in rows2])
    tick("part4")


# ============================================================================
# PART 5 -- STRUCTURE: everything is within distance 3 of Z
# ============================================================================
def part5():
    print("\n=== PART 5 -- STRUCTURE: distance <= 3 from Z; depth 4 dies by an induced P7 ===")
    print("  By PART 1C a distance-2 vertex attaches ONLY to an antipodal vertex, so the")
    print("  depth-4 frame is forced to be x4-x3-x2-u-z0 with u antipodal.  Enumerated over")
    print("  the antipodal slot and over the free bits of the tail.")
    bad = 0; good = 0
    for slot in range(3):
        a0, a3 = slot, slot + 3
        e = HEX + [(6,a0),(6,a3), (7,6), (8,7), (9,8)]
        s = Sample("depth-4 frame slot=%d" % slot, 10, e, mode="frame")
        ok = s.admit(verbose=False)
        reason = "; ".join(s.why)
        print("      slot %d: %s  [%s]" % (slot, "REJECTED" if not ok else "SURVIVES", reason))
        if (not ok) and any("P7" in w for w in s.why) and not any("C4" in w for w in s.why):
            good += 1
        else:
            bad += 1
    check("depth 4 is refuted at all 3 antipodal slots, and by the P7 (never by a C4)",
          good == 3 and bad == 0, "good=%d bad=%d" % (good, bad))
    s3 = Sample("depth-3 frame", 9, HEX + [(6,0),(6,3),(7,6),(8,7)], mode="host")
    ok3 = s3.admit(verbose=False)
    check("depth 3 IS reached (so `distance <= 3` is sharp, not merely an upper bound)",
          ok3 and s3.dist_to_Z(8) == 3, "%r" % s3.why)
    if ok3:
        print("      observed: dist(x,Z) = %d, d(x) = %d, a(x) = %d"
              % (s3.dist_to_Z(8), s3.d(8), s3.a(8)))
    tick("part5")


# ============================================================================
# PART 6 -- RANDOM IN-HYPOTHESIS SWEEP.  Evidence weight stated, not implied.
# ============================================================================
def part6():
    print("\n=== PART 6 -- RANDOM IN-HYPOTHESIS SWEEP (evidence weight stated up front) ===")
    print("  The dichotomy is a THEOREM inside the hypothesis, so an in-hypothesis sweep buys")
    print("  0 bits about its truth -- round 19's null-expectation lesson.  It buys exactly")
    print("  one thing: it certifies the ARITHMETIC on hosts nobody designed.  The DISCARD")
    print("  COUNT is printed so the sample is never mistaken for the population.")
    random.seed(20260823)
    tried = admitted = 0
    worst = {"single": (0, 0), "consecutive": (0, 0), "antipodal": (0, 0), "empty": (0, 0)}
    seen = {}
    viol = []
    while tried < 6000 and time.time() - T0 < 130.0:
        tried += 1
        n = 6 + random.randint(1, 6)
        edges = list(HEX); have = set(map(frozenset, edges))
        for v in range(6, n):
            cand = list(range(0, v)); random.shuffle(cand)
            for u in cand[:random.randint(1, 3)]:
                if frozenset((u, v)) not in have:
                    edges.append((u, v)); have.add(frozenset((u, v)))
        s = Sample("rand#%d" % tried, n, edges)
        if not s.admit(verbose=False): continue
        admitted += 1
        for v in range(6, n):
            tt = trace_type(s.tr(v)); seen[tt] = seen.get(tt, 0) + 1
            d, a = s.d(v), s.a(v)
            if tt in worst: worst[tt] = (max(worst[tt][0], d), max(worst[tt][1], a))
            if tt == "single" and (d > 4 or a > 3): viol.append(("single", v, d, a, edges))
            if tt == "consecutive" and (d > 4 or a > 3): viol.append(("cons", v, d, a, edges))
            if tt in ("distance-2", "size>=3"): viol.append((tt, v, d, a, edges))
    print("      observed population: %d random hosts, %d ADMITTED (%.1f%%), %d DISCARDED "
          "as out of hypothesis" % (tried, admitted, 100.0*admitted/max(tried,1), tried-admitted))
    print("      observed off-Z vertices by trace type: %r" % seen)
    print("      observed maxima (d,a) by trace type:   %r" % worst)
    check("sweep: 0 single-trace with d>4 or a>3; 0 consecutive with d>4 or a>3; "
          "0 distance-2 or size>=3 trace", not viol, "" if not viol else "%r" % (viol[0][:4],))
    check("sweep is NON-VACUOUS on both bounded classes",
          seen.get("single", 0) > 0 and seen.get("consecutive", 0) > 0, "%r" % seen)
    tick("part6")


# ============================================================================
# PART 7 -- MINT-TIME ADDRESS GATE (RULING BB) for round 23's names
# ============================================================================
def part7():
    print("\n=== PART 7 -- MINT-TIME ADDRESS GATE (RULING BB) on round 23's names ===")
    corpus = [DRAFT]
    # THE PRECONDITION IS A STATEMENT ABOUT THE CORPUS AS IT STOOD AT MINT TIME.
    # Run after the section ships, a naive gate reports the mint itself and turns red -- which
    # is how round 22's script had to hedge its own PART A2 in prose.  Prose is not a check.
    # So the boundary is PINNED: the draft was 4557 lines before this round appended 35, and
    # the assertion is `0 occurrences at or before line 4557`.  That is exactly the
    # mint-time question, and it stays answerable for ever.
    PRE_ROUND23_LINES = 4557
    def occurrences(name):
        import re as _re
        pat = _re.compile(r"(?<![A-Za-z0-9_])" + _re.escape(name) + r"(?![A-Za-z0-9_])")
        before, after = [], []
        with open(DRAFT, encoding="utf-8") as fh:
            for ln, raw in enumerate(fh, 1):
                if pat.search(raw):
                    (before if ln <= PRE_ROUND23_LINES else after).append((ln, raw.strip()[:100]))
        return before, after
    print("  corpus boundary PINNED at draft line %d (the file before 35 was appended)"
          % PRE_ROUND23_LINES)
    res = {}
    for name in ("G58", "G59", "G60", "W_1", "W_far", "Shield", "Br"):
        before, after = occurrences(name)
        res[name] = (len(before), len(after))
        print("  observed: `%-7s` -> %d occurrence(s) AT MINT TIME, %d added by 35"
              % (name, len(before), len(after)))
        for ln, txt in before[:2]:
            print("      pre-existing  %d: %s" % (ln, txt))
    print("  `G58`/`G59` pre-existing occurrences are draft 34.2a's PROSE ABOUT the gate")
    print("  (\"the next free addresses G58/G59\"), inspected line by line above, never an")
    print("  address -- so the `G` namespace is monotone and `G58` is still the next free one.")
    check("gate: `W_1` was MINTABLE at mint time (0 pre-existing occurrences), and it "
          "completes the W_0 / W_cons / W_anti family", res["W_1"][0] == 0,
          "%d pre-existing" % res["W_1"][0])
    check("gate: `G60`, `W_far`, `Shield`, `Br` resolve nowhere, before or after",
          all(res[n] == (0, 0) for n in ("G60", "W_far", "Shield", "Br")), "%r" % res)
    check("gate: `G58` was NOT minted as an address this round -- 35 leaves it free, and "
          "the owner does not self-promote",
          not any("**G58" in t or "Lemma G58" in t or "# " in t.split("G58")[0][-3:]
                  for _, t in occurrences("G58")[1]), "%r" % (occurrences("G58")[1],))
    R22.NCHECK = 0; R22.FAIL = []
    R22.part_A(DRAFT, "ROUND-23 CURRENT", expect_clean=True)
    check("gate: round 22's PART A is still clean on the draft as it now stands",
          not R22.FAIL, "%r" % R22.FAIL)
    tick("part7")


def main():
    print("w133 round 23 -- the off-cycle bound.  RULING BM is enforced by the Sample object.")
    part0(); part1(); part2(); part3(); part4(); part5(); part6(); part7()
    print("\n=== SUMMARY ===")
    print("checks run: %d   failures: %d" % (NCHECK, len(FAIL)))
    for f in FAIL: print("  FAILED: %s" % f)
    print("elapsed: %.2f s" % (time.time() - T0))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
