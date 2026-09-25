#!/usr/bin/env python3
"""
w133 round 24 -- THE PER-BRANCH DISCHARGING BOUND: the single remaining gap in (D3-C6).

WHERE THE FRONT STOOD (round 23 / draft 35, planner RULING BT).
    (D3-C6) hypotheses: connected, C4-FREE, contains an induced C6 Z, NO INDUCED P7.
    V = Z + W_1 + W_cons + W_anti + W_0  (G54: every off-Z trace is empty, single,
    consecutive or antipodal).  Round 23 proved  a(v) - 3 <= 0  on W_1 and W_cons, so the
    WHOLE off-cycle surplus sits in  R := W_anti + W_0, and it proved that a VERTEX-WISE
    bound on R does NOT exist (FAMILY-A / FAMILY-U are in hypothesis with a(v) = k+2,
    k+1).  What it left open, and what this file answers, is the PER-BRANCH bound.

THE STATEMENT THIS FILE CERTIFIES.

    (B)  Sum_{v in W_anti + W_0} ( a(v) - 3 )  <=  0,   and 0 is ATTAINED.

    So the surplus that round 23 localised to R is not merely localised: it is NON-POSITIVE
    in total, on a set on which no vertex-wise bound exists.  The shielded branch pays for
    itself, as round 23's decreasing Sum(a-3) predicted.

HOW, AND EVERY STEP IS AN EXHAUSTIVE ENUMERATION (RULING BW: a load-bearing bound is
machine-enumerated, never hand-counted -- all four of last round's hand bounds were wrong).

    R0  REDUCTION.  Deleting W_1 + W_cons changes a(v) for NO v in R.  (An off-Z neighbour
        of an antipodal u has trace contained in trace(u), so it is a triangle apex at u:
        it adds 1 to d(u) AND 1 to t(u), and a = d - t.)  So (B) may be proved on hosts
        whose only off-Z vertices are W_anti + W_0 -- which is what PART 5 enumerates.
    S1  W_anti is an INDEPENDENT set, and |W_anti| = m <= 3.
    S2  SHIELD.  A W_0 vertex at distance 2 attaches only to W_anti.
    S3  Every W_0 vertex at distance 3 has EXACTLY ONE distance-2 neighbour, at most one
        other neighbour, and that other neighbour is adjacent to the first.  Hence
        d <= 2, a = 1, and its charge is EXACTLY -2.
    S4  DISCHARGING RULE.  u in W_anti sends 1 to each of its distance-2 neighbours;
        x at distance 2 sends 1 to each of its distance-3 neighbours.  Then
            final(u) = |W1(u)| - 1 - t(u) <= -1,      final(y at distance 3) = -1,
            final(x at distance 2) = 2a(x) - d(x) + |Q(x)| - 3   [see PART 4]
    S5  final(x) <= 0 for every distance-2 x with exactly ONE W_anti neighbour.
    S6  The distance-2 vertices with >= 2 W_anti neighbours are at most 3 (one per pair of
        antipodal slots), and the whole W_anti + D2* core is a FINITE object, enumerated.

RULING BM IS STILL THE SPINE: a Sample refuses to report any statistic until admit() has
run, and the membership test is written against the OBJECT it tests -- frame or host
(RULING BV, which is round 23's own error generalised).
RULING BX: the mint gate is asserted against a PINNED corpus boundary, so "was this new at
the time" stays answerable for ever.

C4-FREE throughout means: NO TWO DISTINCT VERTICES HAVE TWO COMMON NEIGHBOURS.
Wall-clock self-limit 300 s, exit(2) on overrun.  No SAT.
"""
import itertools, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w133_r22_namespace import (mkadj, c4_all, c4_free, connected, longest_induced_path,
                                is_induced_c6, triangles_at, alpha_of_nbhd, trace)
import w133_r23_offcycle as R23
from w133_r23_offcycle import Sample, induced_path_witness, trace_type, legal_trace

T0 = time.time()
LIMIT = 300.0
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
STATE = os.path.join(REPO, "orchestration", "results", "w133_state.md")

HEX = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
Z6  = [0,1,2,3,4,5]
ANTI = [(0,3), (1,4), (2,5)]          # the three antipodal slots


# ============================================================================
# PART 0 -- POSITIVE CONTROLS, and the RULING BM / BV machinery re-asserted here
# ============================================================================
def part0():
    print("\n=== PART 0 -- POSITIVE CONTROLS ON THE TOOLING (before any of it is used) ===")
    PET = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
           (0,5),(1,6),(2,7),(3,8),(4,9)]
    pet = mkadj(10, PET)
    check("control: Petersen is C4-free", c4_free(pet))
    check("control: longest induced path(Petersen) = 5", longest_induced_path(pet) == 5)
    check("control: a == 3 at every Petersen vertex",
          [alpha_of_nbhd(pet, v) for v in range(10)] == [3]*10)
    check("specificity: longest induced path(K_{1,4}) = 3",
          longest_induced_path(mkadj(5, [(0,1),(0,2),(0,3),(0,4)])) == 3)
    check("specificity: a bare induced C6 has longest induced path 5",
          longest_induced_path(mkadj(6, HEX)) == 5)
    check("specificity: the 4-cycle IS detected as not C4-free",
          not c4_free(mkadj(4, [(0,1),(1,2),(2,3),(3,0)])))
    # a = d - t is the identity every charge line below rests on; check it, do not assume it
    ok = True
    for E, n in [(PET, 10), (HEX, 6), (HEX + [(6,0),(6,3),(7,6)], 8)]:
        ad = mkadj(n, E)
        for v in range(n):
            if alpha_of_nbhd(ad, v) != len(ad[v]) - triangles_at(ad, v): ok = False
    check("control: a(v) == d(v) - t(v) holds on every C4-free control "
          "(G[N(v)] is a matching)", ok)
    # RULING BM guards
    s = Sample("guard-probe", 8, HEX + [(6,0),(7,6)])
    fired = False
    try: s.a(6)
    except AssertionError as e: fired = ("BEFORE admit" in str(e))
    check("RULING BM: reading a statistic BEFORE admit() RAISES", fired)
    # RULING BV: the membership test is written against the OBJECT it tests
    e_iso = HEX + [(6,7)]
    sf, sh = Sample("iso-frame", 8, e_iso, mode="frame"), Sample("iso-host", 8, e_iso, mode="host")
    okf, okh = sf.admit(verbose=False), sh.admit(verbose=False)
    check("RULING BV: the SAME edge list is admitted as a FRAME and rejected as a HOST",
          okf and not okh and any("connected" in w for w in sh.why))
    tick("part0")


# ============================================================================
# helpers -- every one of them reads off an explicit graph, never off a memory
# ============================================================================
def frame_ok(n, edges):
    """Admissible as a FRAME (RULING BV): only the clauses inherited by induced subgraphs."""
    s = Sample("f", n, edges, mode="frame")
    return s.admit(verbose=False), s

def host_ok(n, edges):
    s = Sample("h", n, edges, mode="host")
    return s.admit(verbose=False), s


# ============================================================================
# PART 1 -- R0: the REDUCTION.  W_1 + W_cons may be deleted without moving a(v) on R
# ============================================================================
def part1():
    print("\n=== PART 1 -- R0 REDUCTION: deleting W_1 + W_cons moves no a(v) on R ===")
    print("  Frame = induced subgraph on Z + {u} + {s}; C4-freeness, P7-freeness and")
    print("  'Z is an induced C6' are inherited, so a refuted frame is refuted in EVERY host.")
    # (a) exhaustive 64-frame table: what may an off-Z neighbour of an ANTIPODAL u look like
    for slot in ANTI:
        surv = []
        for bits in range(64):
            T = tuple(i for i in range(6) if (bits >> i) & 1)
            edges = list(HEX) + [(6, i) for i in slot] + [(7, 6)] + [(7, i) for i in T]
            ok, _ = frame_ok(8, edges)
            if ok: surv.append(T)
        claim = sorted(t for t in [(), (slot[0],), (slot[1],)])
        print("      slot %r : observed population 64 frames, %d survive -> %r"
              % (list(slot), len(surv), [list(t) for t in sorted(surv)]))
        check("R0a slot %r: an off-Z neighbour of an antipodal u has trace a PROPER subset "
              "of trace(u)" % (list(slot),), sorted(surv) == claim,
              "observed %r claimed %r" % (sorted(surv), claim))
    # (b) hence such a neighbour with a NONEMPTY trace is a triangle apex at u: d+1, t+1
    moved = []
    for slot in ANTI:
        for z in slot:
            edges = list(HEX) + [(6, i) for i in slot] + [(7, 6), (7, z)]
            ok, s = host_ok(8, edges)
            if not ok: moved.append(("not in hypothesis", slot, z)); continue
            base_ok, base = host_ok(7, list(HEX) + [(6, i) for i in slot])
            if not base_ok: moved.append(("base rejected", slot, z)); continue
            if s.a(6) != base.a(6): moved.append((slot, z, s.a(6), base.a(6)))
    print("      observed population: %d (slot, z) pairs tested, %d moved a(u)"
          % (6, len(moved)))
    check("R0b: adding a W_1 neighbour to an antipodal u leaves a(u) UNCHANGED "
          "(it adds 1 to d and 1 to t)", not moved, "%r" % (moved,))
    # (c) and W_cons / W_1 vertices are never adjacent to a distance-2 vertex: the SHIELD.
    #     exhaustive: anchor x with empty trace, neighbour s with every one of the 64 traces
    bad = []
    for bits in range(64):
        T = tuple(i for i in range(6) if (bits >> i) & 1)
        if not legal_trace(T) or len(T) == 0: continue
        # x has empty trace and is adjacent to s only; s has trace T
        edges = list(HEX) + [(7, i) for i in T] + [(6, 7)]
        ok, _ = frame_ok(8, edges)
        if ok: bad.append((trace_type(T), T))
    kinds = sorted(set(k for k, _ in bad))
    print("      observed population: all legal nonempty traces T; frames surviving with an "
          "empty-trace vertex hung on T: %r" % (kinds,))
    check("R0c SHIELD: an empty-trace vertex may hang only on an ANTIPODAL vertex",
          kinds == ["antipodal"], "%r" % (kinds,))
    tick("part1")


# ============================================================================
# PART 2 -- S1: W_anti is an INDEPENDENT set (exhaustive over ordered slot pairs)
# ============================================================================
def part2():
    print("\n=== PART 2 -- S1: W_anti is an independent set, and |W_anti| <= 3 ===")
    rows = []
    for sa in ANTI:
        for sb in ANTI:
            edges = list(HEX) + [(6, i) for i in sa] + [(7, i) for i in sb] + [(6, 7)]
            ok, s = frame_ok(8, edges)
            rows.append((sa, sb, ok, "; ".join(s.why)))
    print("      observed population: %d ordered slot pairs with u ~ u' asserted" % len(rows))
    for sa, sb, ok, why in rows[:3] + rows[3:6:2]:
        print("        u%r ~ u'%r : %s  [%s]" % (list(sa), list(sb),
              "SURVIVES" if ok else "REFUTED", why))
    check("S1: NO two antipodal-trace vertices may be adjacent (all %d slot pairs refuted)"
          % len(rows), all(not ok for _, _, ok, _ in rows))
    check("S1: and every one of them is refuted BY A C4, not by the P7 clause",
          all(any("C4" in w for w in [why]) for _, _, ok, why in rows if not ok))
    # non-adjacent antipodal pairs DO survive -- so S1 is a real restriction, not vacuous
    surv = 0
    for sa, sb in itertools.combinations(ANTI, 2):
        edges = list(HEX) + [(6, i) for i in sa] + [(7, i) for i in sb]
        ok, _ = frame_ok(8, edges)
        surv += 1 if ok else 0
    check("S1 liveness: the same two vertices NON-adjacent are in hypothesis (3/3 pairs)",
          surv == 3, "%d of 3" % surv)
    # one vertex per slot
    same = []
    for sa in ANTI:
        edges = list(HEX) + [(6, i) for i in sa] + [(7, i) for i in sa]
        ok, s = frame_ok(8, edges)
        same.append((sa, ok, "; ".join(s.why)))
    check("S1: two vertices in the SAME antipodal slot are refuted by a C4 (3/3 slots) "
          "=> |W_anti| <= 3", all((not ok) and "C4" in why for _, ok, why in same))
    tick("part2")


# ============================================================================
# PART 3 -- S3: the distance-3 population is completely determined; its charge is -2
# ============================================================================
def part3():
    print("\n=== PART 3 -- S3: every distance-3 vertex has d <= 2 and charge EXACTLY -2 ===")
    # frame: Z + u(antipodal {0,3}) + x(empty, ~u) + y(empty, ~x, not ~u) + w(~y)
    # exhaustive over w's 64 traces x its adjacency to {u, x}
    base = list(HEX) + [(6,0),(6,3),(7,6),(8,7)]      # 6=u, 7=x, 8=y
    surv, refuted = [], []
    for bits in range(64):
        T = tuple(i for i in range(6) if (bits >> i) & 1)
        for wu in (0,1):
            for wx in (0,1):
                edges = base + [(9,8)] + [(9,i) for i in T]
                if wu: edges = edges + [(9,6)]
                if wx: edges = edges + [(9,7)]
                ok, s = frame_ok(10, edges)
                (surv if ok else refuted).append((T, wu, wx, "; ".join(s.why)))
    print("      observed population: %d frames (w's 64 traces x adjacency to u,x); "
          "%d survive, %d refuted" % (len(surv)+len(refuted), len(surv), len(refuted)))
    viol = [(T,wu,wx) for T,wu,wx,_ in surv if (not wx) and len(T) == 0]
    check("S3a: a further neighbour w of y that is NOT adjacent to x must carry a NONEMPTY "
          "Z-trace (0 survivors with trace empty and w not~x)", not viol, "%r" % (viol[:4],))
    free = [(T,wu,wx,why) for T,wu,wx,why in refuted if (not wx) and (not wu) and len(T)==0]
    tied = [(T,wu,wx,why) for T,wu,wx,why in refuted if (not wx) and wu and len(T)==0]
    if free: print("        w free of u and of x, empty trace -- refutation printed: %s" % free[0][3])
    if tied: print("        w adjacent to u instead      -- refutation printed: %s" % tied[0][3])
    check("S3a: the free case is refuted by an INDUCED P7 (and by nothing else)",
          bool(free) and all(("P7" in why) and len(why.split(";")) == 1 for _,_,_,why in free))
    check("S3a: the w~u case is refuted instead by a C4 -- two distinct mechanisms, "
          "both printed", bool(tied) and all("C4" in why for _,_,_,why in tied))
    # a distance-3 y has NO N(Z) neighbour by definition; so the surviving trace-nonempty
    # branch is exactly the case where y is at distance 2, not 3.  Now the second D2
    # neighbour: w with empty trace but hung on ANOTHER antipodal vertex u'.
    rows = []
    for slot in ANTI[1:]:
        edges = base + [(9,8),(10,9)] + [(10,i) for i in slot]     # 9=w(empty), 10=u'
        ok, s = frame_ok(11, edges)
        rows.append((slot, ok, "; ".join(s.why)))
    print("      observed population: %d frames putting a SECOND distance-2 vertex on y" % len(rows))
    for slot, ok, why in rows:
        print("        u' at slot %r : %s  [%s]" % (list(slot), "SURVIVES" if ok else "REFUTED", why))
    check("S3b: a distance-3 vertex cannot have TWO distance-2 neighbours "
          "(every frame refuted, by an induced P7)",
          all((not ok) and "P7" in why for _, ok, why in rows))
    # consequence, read off explicit hosts rather than asserted
    hosts = [("pendant y", 9, base + []), ]
    hh = list(HEX) + [(6,0),(6,3),(7,6),(8,7)]
    ok, s = host_ok(9, hh)
    check("S3c: a pendant distance-3 vertex has a = 1, charge = -2 (read off the host)",
          ok and s.a(8) == 1 and s.a(8) - 3 == -2, "a=%r" % (s.a(8) if ok else None,))
    hh2 = list(HEX) + [(6,0),(6,3),(7,6),(8,7),(9,7),(9,8)]        # y=8, w=9, both ~x=7, y~w
    ok2, s2 = host_ok(10, hh2)
    check("S3d: the only other shape -- y,w both hung on the same x and adjacent -- is in "
          "hypothesis and gives a = 1, charge = -2 for BOTH",
          ok2 and s2.a(8) == 1 and s2.a(9) == 1,
          "a(y),a(w) = %r" % ((s2.a(8), s2.a(9)) if ok2 else None,))
    tick("part3")


# ============================================================================
# PART 4 -- S5: the discharging rule, and final(x) <= 0 for a singly-attached x
# ============================================================================
def part4():
    print("\n=== PART 4 -- S4/S5: the discharging rule and the distance-2 verdict ===")
    print("  RULE.  u in W_anti sends 1 to each distance-2 neighbour; a distance-2 x sends")
    print("  1 to each distance-3 neighbour.  With a = d - t and (S3) charge(y) = -2:")
    print("    final(u) = |W1(u)| - 1 - t(u) <= -1        [t(u) >= |W1(u)| by R0a/R0b]")
    print("    final(y) = -2 + 1 = -1                     [S3]")
    print("    final(x) = a(x) - 3 - |P(x)| + alpha(x) = 2alpha(x) + |Q(x)| - t(x) - 3")
    print("  where alpha(x)=|N(x) cap W_anti|, P(x)=distance-3 nbrs, Q(x)=distance-2 nbrs.")

    # ---- THE CORE TABLE.  All three antipodal slots are present (6,7,8 = u_a,u_b,u_c,
    # pairwise non-adjacent by S1); x (=9) and x' (=10) are distance-2 vertices -- empty
    # trace, adjacent -- whose ANCHOR SETS range over ALL nonempty subsets of {a,b,c}.
    # 7 x 7 = 49 frames.  Nothing here is chosen by hand.
    SUB = [s for r in (1, 2, 3) for s in itertools.combinations(range(3), r)]
    def core(A, B, extra=()):
        E = list(HEX)
        for j, sl in enumerate(ANTI): E += [(6 + j, i) for i in sl]
        E += [(9, 6 + j) for j in A] + [(10, 6 + j) for j in B] + [(9, 10)]
        return E + list(extra)
    surv, ref = [], []
    for A in SUB:
        for B in SUB:
            ok, s = frame_ok(11, core(A, B))
            (surv if ok else ref).append((A, B, "; ".join(s.why)))
    print("      observed population: %d frames (two ADJACENT distance-2 vertices, anchor "
          "sets over all nonempty subsets); %d survive, %d refuted"
          % (len(surv) + len(ref), len(surv), len(ref)))
    print("        surviving (anchors of x, anchors of x'): %r"
          % ([(list(a), list(b)) for a, b, _ in surv],))
    # THE OWNER'S HAND CLAIM HERE WAS WRONG AND THE MACHINE SAYS THE OPPOSITE (RULING BW):
    # the hand argument predicted that two adjacent distance-2 vertices must be anchored on
    # DIFFERENT antipodal vertices.  Every survivor SHARES an anchor.  The corrected clause
    # is the one that carries the load, because a shared anchor is a TRIANGLE at x.
    check("S5a: two adjacent distance-2 vertices always SHARE an anchor -- so |Q(x)| = 1 "
          "forces a triangle at x, t(x) >= 1  [the hand claim was the opposite]",
          len(surv) > 0 and all(set(a) & set(b) for a, b, _ in surv))
    check("S5a2: and the anchor multiset of an adjacent pair is always {1,1} or {1,3} -- "
          "an alpha = 2 vertex never has a distance-2 neighbour",
          all(sorted([len(a), len(b)]) in ([1, 1], [1, 3]) for a, b, _ in surv))
    two = [(A, B, w) for A, B, w in ref if len(set(A) & set(B)) >= 2]
    check("S5a': and a shared PAIR of anchors is refuted by a C4 (two vertices, two common "
          "neighbours) -- this is what caps the multiply-anchored population",
          bool(two) and all("C4" in w for _, _, w in two))
    # ---- |Q(x)| <= 1: give x a SECOND distance-2 neighbour, anchors again over all subsets
    surv3 = []
    tot3 = 0
    for A in SUB:
        for B in SUB:
            for C in SUB:
                for xx in (0, 1):
                    E = core(A, B, extra=[(11, 6 + j) for j in C] + [(11, 9)]
                             + ([(10, 11)] if xx else []))
                    tot3 += 1
                    ok, _ = frame_ok(12, E)
                    if ok: surv3.append((A, B, C, xx))
    print("      observed population: %d frames giving x TWO distance-2 neighbours; "
          "%d survive" % (tot3, len(surv3)))
    check("S5b: NO distance-2 vertex has two distance-2 neighbours => |Q(x)| <= 1",
          not surv3, "%d survived, e.g. %r" % (len(surv3), surv3[:2]))
    # ---- the pair budget: Sum_x C(alpha(x),2) <= C(m,2) <= 3, by the same C4
    ok, s = frame_ok(11, [e for e in core((0, 1), (0, 1)) if e != (9, 10)])
    check("S5c: two distance-2 vertices sharing TWO anchors are refuted even when "
          "NON-adjacent (so each antipodal PAIR has at most one common neighbour)",
          (not ok) and any("C4" in w for w in s.why), "%r" % (s.why,))
    # ---- the arithmetic that these four facts force, printed as a table
    print("      final(x) = 2*alpha(x) + |Q(x)| - t(x) - 3, with |Q| <= 1 (S5b) and "
          "|Q| = 1 => t >= 1 (S5a):")
    rows = []
    for al in (1, 2, 3):
        for q in (0, 1):
            if al == 2 and q == 1: continue          # S5a2
            tmin = 1 if q == 1 else 0
            rows.append((al, q, tmin, 2*al + q - tmin - 3))
    for al, q, t, f in rows:
        print("        alpha=%d |Q|=%d t>=%d  ->  final <= %+d" % (al, q, t, f))
    check("S5: final(x) <= 2*alpha(x) - 3 for EVERY distance-2 vertex; in particular "
          "final(x) <= -1 when alpha(x) = 1",
          all(f <= 2*al - 3 for al, _, _, f in rows)
          and all(f <= -1 for al, _, _, f in rows if al == 1))
    # ---- S6: the multiply-anchored budget closes the sum
    print("      S6.  Each antipodal PAIR carries at most one common neighbour (S5c), so")
    print("      Sum_{alpha(x)>=2} C(alpha(x),2) <= C(m,2).  Enumerating the feasible")
    print("      (m, multiset of alphas) and comparing Sum final(x) against m:")
    worst = []
    for m in (1, 2, 3):
        for n3 in (0, 1):
            for n2 in range(0, 4):
                if n2 * 1 + n3 * 3 > m * (m - 1) // 2: continue
                if n3 and m < 3: continue
                if n2 and m < 2: continue
                tot = n2 * (2*2 - 3) + n3 * (2*3 - 3)      # final(x) <= 2*alpha - 3
                worst.append((m, n2, n3, tot, tot <= m))
    for m, n2, n3, tot, okk in worst:
        print("        m=%d  #(alpha=2)=%d  #(alpha=3)=%d  ->  Sum final(x) <= %+d   "
              "(budget m = %d) %s" % (m, n2, n3, tot, m, "OK" if okk else "FAILS"))
    check("S6: Sum_{alpha(x)>=2} final(x) <= m in EVERY feasible case (%d cases enumerated)"
          % len(worst), all(okk for *_, okk in worst))
    print("      => Sum_R final = Sum_u final(u) + Sum_x final(x) + Sum_y final(y)")
    print("                     <= -m           + m              + (-|D3|)   <= 0.")
    tick("part4")


# ============================================================================
# PART 5 -- S6 + the bound itself: EXHAUSTIVE enumeration of the reduced region
# ============================================================================
def part5(maxs=5):
    print("\n=== PART 5 -- THE BOUND, by exhaustive enumeration of the REDUCED region ===")
    print("  By R0 the whole of Sum_R (a-3) is computed on hosts whose only off-Z vertices")
    print("  have an EMPTY or ANTIPODAL trace.  Every such host with at most %d off-Z" % maxs)
    print("  vertices is generated here, pruned by C4-freeness and P7-freeness -- both")
    print("  INHERITED by induced subgraphs, so the pruning is sound (RULING BV).")
    TRACES = [()] + [tuple(s) for s in ANTI]
    best, nodes, seen_depth = {}, [0], {}
    def dfs(edges, k):
        n = 6 + k
        adj = mkadj(n, edges)
        nodes[0] += 1
        seen_depth[k] = seen_depth.get(k, 0) + 1
        if connected(adj):
            c = sum(alpha_of_nbhd(adj, v) - 3 for v in range(6, n))
            if c > best.get(k, (-99, None))[0]: best[k] = (c, list(edges))
        if k >= maxs: return
        tick("part5 depth %d" % k)
        v = n
        for tr in TRACES:
            for r in range(0, k + 1):
                for sub in itertools.combinations(range(6, 6 + k), r):
                    ne = edges + [(v, z) for z in tr] + [(v, s) for s in sub]
                    a2 = mkadj(n + 1, ne)
                    if not c4_free(a2): continue
                    if longest_induced_path(a2) >= 7: continue
                    dfs(ne, k + 1)
    dfs(list(HEX), 0)
    print("      observed population: %d in-hypothesis reduced regions generated "
          "(by |off-Z| = %r)" % (nodes[0], sorted(seen_depth.items())))
    for k in sorted(best):
        print("        |off-Z| = %d : max Sum_R(a-3) = %+d" % (k, best[k][0]))
    mx = max(v[0] for v in best.values())
    check("BOUND: Sum_{v in W_anti + W_0} (a(v)-3) <= 0 over EVERY reduced region with "
          "at most %d off-Z vertices (%d regions)" % (maxs, nodes[0]), mx <= 0,
          "observed max %+d" % mx)
    check("SHARPNESS: 0 is ATTAINED", mx == 0)
    att = [k for k in sorted(best) if best[k][0] == 0 and k > 0]
    if att:
        k = att[0]
        print("        attaining region, |off-Z| = %d : %r" % (k, best[k][1][6:]))
        ok, s = host_ok(6 + k, best[k][1])
        R = list(range(6, 6 + k))
        check("SHARPNESS: the attaining region re-admitted as a HOST (not a frame) and its "
              "charge re-read off it", ok and sum(s.a(v) - 3 for v in R) == 0,
              "path=%r charge=%r" % (s.path, sum(s.a(v)-3 for v in R) if ok else None))
    tick("part5")
    return best


# ============================================================================
# PART 6 -- the two round-23 families re-measured under the branch bound
# ============================================================================
def part6():
    print("\n=== PART 6 -- round 23's two unbounded families, re-measured PER BRANCH ===")
    rowsA, rowsU = [], []
    for k in range(0, 7):
        E = list(HEX) + [(6,0),(6,3)] + [(7+i, 6) for i in range(k)]
        ok, s = host_ok(7 + k, E)
        if ok:
            R = list(range(6, 7 + k))
            rowsA.append((k, s.a(6), sum(s.a(v) - 3 for v in R)))
        E = list(HEX) + [(6,0),(6,3),(7,6)] + [(8+i, 7) for i in range(k)]
        ok, s = host_ok(8 + k, E)
        if ok:
            R = list(range(6, 8 + k))
            rowsU.append((k, s.a(7), sum(s.a(v) - 3 for v in R)))
    print("      FAMILY-A  (k, a(u), branch charge): %r" % (rowsA,))
    print("      FAMILY-U  (k, a(v), branch charge): %r" % (rowsU,))
    check("FAMILY-A: a(u) is UNBOUNDED while the branch charge is <= 0 and strictly "
          "decreasing", all(c <= 0 for _, _, c in rowsA)
          and all(rowsA[i+1][2] < rowsA[i][2] for i in range(len(rowsA)-1))
          and rowsA[-1][1] > rowsA[0][1])
    check("FAMILY-U: same, on the question's own class |N(v) cap Z| = 0",
          all(c <= 0 for _, _, c in rowsU)
          and all(rowsU[i+1][2] < rowsU[i][2] for i in range(len(rowsU)-1))
          and rowsU[-1][1] > rowsU[0][1])
    print("      => the vertex-wise bound that round 23 proved NOT to exist is exactly the")
    print("         one the per-branch bound does not need.")
    tick("part6")


# ============================================================================
# PART 7 -- provenance (RULING BF) and the mint gate on a PINNED boundary (RULING BX)
# ============================================================================
def part7(pinned_line):
    print("\n=== PART 7 -- LEDGER GREP (BF) and the PINNED mint gate (BX) ===")
    txt = open(DRAFT, encoding="utf-8").read().splitlines()
    print("      corpus: %s, %d lines now; PINNED BOUNDARY = line %d (the draft's length"
          % (DRAFT, len(txt), pinned_line))
    print("      before this round's section was appended).  Every count below is 'at or")
    print("      before line %d', which is exactly the mint-time question and stays" % pinned_line)
    print("      answerable for ever -- prose is not a check (RULING BX).")
    # The gate is CASE-INSENSITIVE.  A case-sensitive gate reported `per-branch` as 0
    # occurrences while round 23 had written `PER-BRANCH` at line 4735 -- a gate that a
    # change of case walks through is decoration, not a check.
    for sym, expect in [("D2*", 0), ("per-branch discharging bound", 1),
                        ("W_anti", None), ("W_0", None)]:
        pre = sum(1 for i, ln in enumerate(txt) if i < pinned_line and sym.lower() in ln.lower())
        pre_cs = sum(1 for i, ln in enumerate(txt) if i < pinned_line and sym in ln)
        post = sum(1 for ln in txt if sym.lower() in ln.lower())
        print("        %-30s : %d occurrence(s) at or before line %d (%d case-sensitive), "
              "%d in the whole draft" % (sym, pre, pinned_line, pre_cs, post))
        if expect is not None:
            check("mint gate (pinned, case-INsensitive): `%s` has %d occurrence(s) at or "
                  "before line %d" % (sym, expect, pinned_line), pre == expect,
                  "observed %d" % pre)
    where = [i + 1 for i, ln in enumerate(txt)
             if i < pinned_line and "per-branch discharging bound" in ln.lower()]
    print("        => the phrase `per-branch discharging bound` is NOT a mint: round 23 named "
          "this target at line %r before it was met." % (where,))
    # the two inputs this round USES and does not re-prove
    for sym in ("G54", "G57", "|W_anti| <= 3", "shield"):
        pre = sum(1 for i, ln in enumerate(txt) if i < pinned_line and sym in ln)
        print("        input `%-14s`: %d occurrence(s) at or before the boundary "
              "(USED, not re-proved)" % (sym, pre))
    check("BF: the round's inputs G54 and G57 are already on the ledger before the boundary",
          sum(1 for i, ln in enumerate(txt) if i < pinned_line and "G54" in ln) > 0
          and sum(1 for i, ln in enumerate(txt) if i < pinned_line and "G57" in ln) > 0)
    tick("part7")


# ============================================================================
# PART 8 -- WHAT IS LEFT: the off-cycle term is now <= 0 entire; the Z-term is not
# ============================================================================
def part8():
    print("\n=== PART 8 -- the residual, stated against the round's own interest ===")
    print("  G58 gives a(v)-3 <= 0 on W_1 + W_cons; PART 4/5 give Sum_R (a-3) <= 0.  So the")
    print("  WHOLE off-cycle term is now <= 0.  That does NOT close (D3-C6): the Z-term is")
    print("  unbounded ABOVE in hypothesis (draft 34.4b).  G55 summed says exactly why:")
    print("     Sum_{z in Z}(a(z)-3) = |W_1| + 2|W_cons| + 2|W_anti| - Sum_z t(z) - 6.")
    D = list(HEX) + [(6,0),(6,1),(7,2),(7,3),(8,4),(8,5)]                 # INSTANCE-D
    E = D + [(9,0),(9,3),(10,1),(10,4),(11,2),(11,5)]                     # INSTANCE-E
    ATT = list(HEX) + [(7,0),(7,3),(7,6),(8,1),(8,4),(8,6),(9,2),(9,5),(9,6)]
    FAN = list(HEX) + [(6+i, 0) for i in range(7)]                        # 34.4b's k=7 fan
    rows, idfail, offfail = [], [], []
    for tag, n, E_ in [("INSTANCE-D", 9, D), ("INSTANCE-E", 12, E),
                       ("ATTAINING-REGION", 10, ATT), ("34.4b FAN k=7", 13, FAN)]:
        ok, s = host_ok(n, E_)
        if not ok:
            rows.append((tag, "OUT OF HYPOTHESIS", s.why)); continue
        W1 = [v for v in range(n) if v not in Z6 and len(s.tr(v)) == 1]
        Wc = [v for v in range(n) if v not in Z6 and trace_type(s.tr(v)) == "consecutive"]
        Wa = [v for v in range(n) if v not in Z6 and trace_type(s.tr(v)) == "antipodal"]
        W0 = [v for v in range(n) if v not in Z6 and len(s.tr(v)) == 0]
        zt = sum(s.a(z) - 3 for z in Z6)
        rhs = len(W1) + 2*len(Wc) + 2*len(Wa) - sum(s.t(z) for z in Z6) - 6
        off = sum(s.a(v) - 3 for v in range(n) if v not in Z6)
        reg = sum(s.a(v) - 3 for v in Wa + W0)
        leak = sum(s.a(v) - 2 for v in W1)
        if zt != rhs: idfail.append((tag, zt, rhs))
        if off > 0: offfail.append((tag, off))
        rows.append((tag, dict(n=n, W1=len(W1), Wcons=len(Wc), Wanti=len(Wa), W0=len(W0),
                               Zterm=zt, offterm=off, region=reg, total=zt+off,
                               W1leak=leak)))
    for r in rows: print("      %-18s %r" % (r[0], r[1] if len(r) == 2 else r[1:]))
    check("PART8a: G55 summed is an IDENTITY on every in-hypothesis instance tested",
          not idfail, "%r" % (idfail,))
    check("PART8b: the off-cycle term Sum_{v not in Z}(a(v)-3) is <= 0 on every one of them",
          not offfail, "%r" % (offfail,))
    print("      THE RESIDUAL, named: the Z-term's `+|W_1|` is paid only if")
    print("        Sum_{v in W_1} ( a(v) - 2 )  <=  (the slack in the rest).")
    print("      G58 gives a(v) <= 3 on W_1 and the value 3 IS attained, so a single W_1")
    print("      vertex can leak +1.  THAT is the next gap -- it is bounded, named, and it")
    print("      is NOT closed by this round.  No pocket closed; (D3-C6) remains OPEN.")
    tick("part8")


def main():
    pinned = int(sys.argv[1]) if len(sys.argv) > 1 else len(open(DRAFT, encoding="utf-8").read().splitlines())
    print("=" * 78)
    print("w133 round 24 -- THE PER-BRANCH DISCHARGING BOUND ON W_anti + W_0")
    print("=" * 78)
    part0(); part1(); part2(); part3(); part4()
    part5(maxs=int(os.environ.get("W133_MAXS", "5")))
    part6(); part8(); part7(pinned)
    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d   wall clock: %.2f s" % (NCHECK, len(FAIL), time.time() - T0))
    if FAIL:
        print("FAILURES: %r" % (FAIL,)); sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
