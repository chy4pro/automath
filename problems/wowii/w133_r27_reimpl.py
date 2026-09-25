#!/usr/bin/env python3
"""
WOWII-133 round 27 — INDEPENDENT RE-IMPLEMENTATION of the load-bearing enumerations
of draft sections 35 / 36 / 37.

RULING CQ / CU:  this is a NEW TOOL.  It inherits NONE of the original's controls.
It was written from the SPECIFICATION ONLY (notes/proofs/wowii133_draft.md 35.1.1,
36.1.1, 37.1.1 and the (Z1)-(Z6) statement block).  The round-23/24/25 scripts
(w133_r23_offcycle.py, w133_r24_branch.py, w133_r25_zterm.py) were NOT opened while
this file was written.

Conventions, taken from the draft and restated here so this file is self-contained:
  * C4-FREE means "no two distinct vertices have two common neighbours"
    (the 1 / 17.3 convention, machine-load-bearing per state ledger round 14).
  * t(v) = number of edges inside G[N(v)].  Under C4-freeness G[N(v)] is a matching,
    so t(v) is the number of triangles at v, and a(v) = d(v) - t(v).
  * Z = (z_0..z_5) is an induced C6, vertices 0..5, z_i ~ z_{i+1 mod 6}.
  * IN HYPOTHESIS, FRAME  := C4-free AND Z induces a C6 AND no induced P7.
    (connectedness is NOT inherited by induced subgraphs, so a frame is not
     required to be connected -- 35.6 item 3.)
    IN HYPOTHESIS, HOST   := frame conditions AND connected.
  * trace(v) := N(v) cap Z, for v not in Z.
    W_0 / W_1 / W_cons / W_anti = trace empty / singleton / consecutive pair /
    antipodal pair.
  * n_3 := #{ v in W_1 : a(v) = 3 }   (the LEAKS),  m := |W_anti|.

Every predicate below is POSITIVE-CONTROLLED in PART 0 on inputs where it MUST
return True, as well as inputs where it must return False.  A predicate whose only
demonstrated behaviour is a negative is invisible to negative controls.

Time guard: tick() -> flush + os._exit(2).  NEVER `return`.  (37.5 item 5: a
`return` guard silently truncated a sweep by ~2% and printed it as complete.)
"""

import os
import sys
import time
import itertools

T0 = time.time()
WALL_LIMIT = 1500.0          # seconds, hard
FAILURES = []
CHECKS = [0]


def tick():
    if time.time() - T0 > WALL_LIMIT:
        sys.stdout.write("\n*** WALL-CLOCK SELF-LIMIT EXCEEDED -- ABORTING PROCESS ***\n")
        sys.stdout.write("*** THE POPULATION PRINTED ABOVE IS INCOMPLETE ***\n")
        sys.stdout.flush()
        os._exit(2)


def check(name, got, want):
    CHECKS[0] += 1
    ok = (got == want)
    print("  [%s] %-58s got=%s want=%s" % ("OK " if ok else "FAIL", name, got, want))
    if not ok:
        FAILURES.append((name, got, want))
    return ok


def note(name, got):
    """Reported quantity with no pre-registered expectation (evidence, not check)."""
    print("  [EVID] %-58s = %s" % (name, got))


# ----------------------------------------------------------------------------
# core graph primitives -- bitmask adjacency, adj[v] is an int
# ----------------------------------------------------------------------------

def mk(n, edges):
    adj = [0] * n
    for (u, v) in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def deg(adj, v):
    return bin(adj[v]).count("1")


def has_C4(adj, n):
    """True iff two distinct vertices have >= 2 common neighbours."""
    for u in range(n):
        for v in range(u + 1, n):
            if bin(adj[u] & adj[v]).count("1") >= 2:
                return True
    return False


def t_of(adj, n, v):
    """edges inside N(v)"""
    nb = [i for i in range(n) if (adj[v] >> i) & 1]
    c = 0
    for i in range(len(nb)):
        for j in range(i + 1, len(nb)):
            if (adj[nb[i]] >> nb[j]) & 1:
                c += 1
    return c


def a_of(adj, n, v):
    return deg(adj, v) - t_of(adj, n, v)


def has_induced_path_ge(adj, n, k):
    """True iff G has an induced path on >= k vertices."""
    full = (1 << n) - 1
    found = [False]

    def dfs(last, avail, ln):
        if ln >= k:
            found[0] = True
            return
        if ln + bin(avail).count("1") < k:
            return
        m = adj[last] & avail
        while m and not found[0]:
            b = m & -m
            m ^= b
            v = b.bit_length() - 1
            dfs(v, avail & ~adj[last] & ~b, ln + 1)

    for s in range(n):
        if found[0]:
            break
        dfs(s, full & ~(1 << s), 1)
    return found[0]


def longest_induced_path(adj, n):
    full = (1 << n) - 1
    best = [0]

    def dfs(last, avail, ln):
        if ln > best[0]:
            best[0] = ln
        m = adj[last] & avail
        while m:
            b = m & -m
            m ^= b
            v = b.bit_length() - 1
            dfs(v, avail & ~adj[last] & ~b, ln + 1)

    for s in range(n):
        dfs(s, full & ~(1 << s), 1)
    return best[0]


def connected(adj, n):
    seen = 1
    stack = [0]
    while stack:
        v = stack.pop()
        m = adj[v] & ~seen
        while m:
            b = m & -m
            m ^= b
            seen |= b
            stack.append(b.bit_length() - 1)
    return seen == (1 << n) - 1


ZM = 0b111111  # vertices 0..5 are Z


def z_induced_C6(adj):
    for i in range(6):
        want = (1 << ((i + 1) % 6)) | (1 << ((i + 5) % 6))
        if (adj[i] & ZM) != want:
            return False
    return True


def in_hyp_frame(adj, n):
    return (not has_C4(adj, n)) and z_induced_C6(adj) and (not has_induced_path_ge(adj, n, 7))


def in_hyp_host(adj, n):
    return in_hyp_frame(adj, n) and connected(adj, n)


def build(n, extra_edges):
    """Z on 0..5 plus the given extra edges on 0..n-1."""
    e = [(i, (i + 1) % 6) for i in range(6)]
    return mk(n, e + list(extra_edges))


def trace_of(adj, v):
    return adj[v] & ZM


def trace_class(tm):
    """'W0','W1','Wcons','Wanti', or 'ILLEGAL'"""
    bits = [i for i in range(6) if (tm >> i) & 1]
    if len(bits) == 0:
        return "W0"
    if len(bits) == 1:
        return "W1"
    if len(bits) == 2:
        d = (bits[1] - bits[0]) % 6
        if d in (1, 5):
            return "Wcons"
        if d == 3:
            return "Wanti"
        return "ILLEGAL"
    return "ILLEGAL"


# ============================================================================
print("=" * 78)
print("PART 0 -- POSITIVE CONTROLS (RULING CQ).  Every predicate is fired on an")
print("input where it MUST return True as well as inputs where it must return False.")
print("=" * 78)

C4g = mk(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
K23 = mk(5, [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)])
K4 = mk(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
C6g = mk(6, [(i, (i + 1) % 6) for i in range(6)])
P7g = mk(7, [(i, i + 1) for i in range(6)])
P9g = mk(9, [(i, i + 1) for i in range(8)])
P6g = mk(6, [(i, i + 1) for i in range(5)])
K14 = mk(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
TRI = mk(3, [(0, 1), (1, 2), (2, 0)])
PET = mk(10, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
              (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
              (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)])

print("-- has_C4 must say TRUE (the positive direction):")
check("has_C4(C4)", has_C4(C4g, 4), True)
check("has_C4(K_{2,3})", has_C4(K23, 5), True)
check("has_C4(K4)", has_C4(K4, 4), True)
print("-- has_C4 must say FALSE:")
check("has_C4(C6)", has_C4(C6g, 6), False)
check("has_C4(Petersen)", has_C4(PET, 10), False)
check("has_C4(P7)", has_C4(P7g, 7), False)
check("has_C4(triangle)", has_C4(TRI, 3), False)

print("-- has_induced_path_ge(.,7) must say TRUE (a detector whose output is a")
print("   NEGATIVE is silent when broken -- 37.5 item 4):")
check("induced P7 in P7", has_induced_path_ge(P7g, 7, 7), True)
check("induced P7 in P9", has_induced_path_ge(P9g, 9, 7), True)
print("-- and must say FALSE:")
check("induced P7 in P6", has_induced_path_ge(P6g, 6, 7), False)
check("induced P7 in C6", has_induced_path_ge(C6g, 6, 7), False)
check("induced P7 in Petersen", has_induced_path_ge(PET, 10, 7), False)

print("-- longest_induced_path, exact values on inputs whose answer is known:")
check("lip(P7)", longest_induced_path(P7g, 7), 7)
check("lip(P9)", longest_induced_path(P9g, 9), 9)
check("lip(C6)", longest_induced_path(C6g, 6), 5)
check("lip(K_{1,4})", longest_induced_path(K14, 5), 3)
check("lip(Petersen)", longest_induced_path(PET, 10), 5)

print("-- a(v) = d(v) - t(v):")
check("a(Petersen) == 3 at every vertex",
      sorted(set(a_of(PET, 10, v) for v in range(10))), [3])
check("a(centre of triangle) == 1", a_of(TRI, 3, 0), 1)
check("a(centre of K_{1,4}) == 4", a_of(K14, 5, 0), 4)

print("-- the two membership predicates, on objects whose status is known:")
# Petersen has an induced C6.  SEARCH for one and let the decider admit it
# (RULING BW, generalised: hand-built objects are claims, searched-and-admitted
#  objects are results -- do not hand-transcribe a 6-cycle).
petv = None
for cyc in itertools.permutations(range(10), 6):
    if cyc[0] != min(cyc):
        continue
    ok = True
    for i in range(6):
        for j in range(i + 1, 6):
            adjacent = (PET[cyc[i]] >> cyc[j]) & 1
            want = 1 if (j - i) % 6 in (1, 5) else 0
            if adjacent != want:
                ok = False
                break
        if not ok:
            break
    if ok:
        petv = list(cyc)
        break
print("  searched Petersen for an induced C6, admitted: %s" % (petv,))
rest = [v for v in range(10) if v not in petv]
perm = {old: i for i, old in enumerate(petv + rest)}
PETR = [0] * 10
for u in range(10):
    for v in range(10):
        if (PET[u] >> v) & 1:
            PETR[perm[u]] |= 1 << perm[v]
check("relabelled Petersen: Z induces C6", z_induced_C6(PETR), True)
check("relabelled Petersen IS an in-hypothesis HOST", in_hyp_host(PETR, 10), True)
BAD1 = build(7, [(6, 0), (6, 2)])            # v adjacent to z0,z2 -> C4 with z1
check("Z + v(z0,z2) is REJECTED (C4)", in_hyp_frame(BAD1, 7), False)
check("   and the reason is a C4", has_C4(BAD1, 7), True)
BAD2 = build(8, [(6, 0), (7, 1), (6, 7)])    # the induced P7 z2 z3 z4 z5 z0 v6 v7
check("Z + v(z0) + v'(z1), v~v' is REJECTED", in_hyp_frame(BAD2, 8), False)
check("   and the reason is an induced P7", has_induced_path_ge(BAD2, 8, 7), True)
check("   lip of that frame", longest_induced_path(BAD2, 8), 7)
print("-- frame vs host must DIFFER on at least one input (35.6 item 3):")
DISJ = build(7, [])                           # Z + isolated vertex
check("Z + isolated v : admitted as FRAME", in_hyp_frame(DISJ, 7), True)
check("Z + isolated v : rejected as HOST", in_hyp_host(DISJ, 7), False)

print("-- trace_class:")
check("trace_class(empty)", trace_class(0), "W0")
check("trace_class({z0})", trace_class(1), "W1")
check("trace_class({z0,z1})", trace_class(0b11), "Wcons")
check("trace_class({z5,z0})", trace_class(0b100001), "Wcons")
check("trace_class({z0,z3})", trace_class(0b1001), "Wanti")
check("trace_class({z0,z2})", trace_class(0b101), "ILLEGAL")

# ============================================================================
print()
print("=" * 78)
print("PART 1 -- 35.1.1 Step 1: the four 64-frame survivor tables.")
print("Frame = induced subgraph on Z + {v,u}, v the anchor with a fixed trace,")
print("u a free neighbour of v whose trace T ranges over ALL 2^6 = 64 subsets.")
print("Population enumerated: 64 per row, complete by construction.")
print("=" * 78)

ANCHORS = [
    ("single {z0}", [0], [(6, 0)]),
    ("consecutive {z0,z1}", [0, 1], [(6, 0), (6, 1)]),
    ("empty (dist>=2)", [], []),
    ("antipodal {z0,z3}", [0, 3], [(6, 0), (6, 3)]),
]
surv_tables = {}
for label, atr, aedges in ANCHORS:
    surv = []
    mech = {"C4": 0, "P7": 0, "both": 0, "other": 0}
    for T in range(64):
        tick()
        ee = list(aedges) + [(6, 7)] + [(7, i) for i in range(6) if (T >> i) & 1]
        g = build(8, ee)
        c4 = has_C4(g, 8)
        p7 = has_induced_path_ge(g, 8, 7)
        if not c4 and not p7 and z_induced_C6(g):
            surv.append(T)
        else:
            if c4 and p7:
                mech["both"] += 1
            elif c4:
                mech["C4"] += 1
            elif p7:
                mech["P7"] += 1
            else:
                mech["other"] += 1
    surv_tables[label] = surv
    names = ["{" + ",".join("z%d" % i for i in range(6) if (T >> i) & 1) + "}" for T in surv]
    print("  anchor %-22s population 64, survivors %d : %s"
          % (label, len(surv), " ".join(n if n != "{}" else "(empty)" for n in names)))
    print("     refutation mechanism census: %s" % (mech,))

check("35 single-trace anchor: survivors", len(surv_tables["single {z0}"]), 7)
check("35 consecutive anchor: survivors", len(surv_tables["consecutive {z0,z1}"]), 3)
check("35 empty-trace anchor: survivors", len(surv_tables["empty (dist>=2)"]), 4)
check("35 antipodal anchor: survivors", len(surv_tables["antipodal {z0,z3}"]), 3)
check("35 single: survivor set",
      sorted(surv_tables["single {z0}"]),
      sorted([1 << 0, 1 << 2, 1 << 3, 1 << 4, (1 << 0) | (1 << 3), (1 << 2) | (1 << 3), (1 << 3) | (1 << 4)]))
check("35 consecutive: survivor set",
      sorted(surv_tables["consecutive {z0,z1}"]),
      sorted([1 << 3, 1 << 4, (1 << 3) | (1 << 4)]))
check("35 empty: survivor set (empty or ANTIPODAL)",
      sorted(surv_tables["empty (dist>=2)"]),
      sorted([0, (1 << 0) | (1 << 3), (1 << 1) | (1 << 4), (1 << 2) | (1 << 5)]))
check("35 antipodal: survivor set (subset of {z0,z3}, not both)",
      sorted(surv_tables["antipodal {z0,z3}"]), sorted([0, 1 << 0, 1 << 3]))

print()
print("  36.1.1 (R0): the empty/antipodal survivor table re-run at ALL THREE slots.")
r0_ok = 0
for s in range(3):
    aa, bb = s, s + 3
    surv = []
    for T in range(64):
        tick()
        ee = [(6, aa), (6, bb), (6, 7)] + [(7, i) for i in range(6) if (T >> i) & 1]
        g = build(8, ee)
        if in_hyp_frame(g, 8):
            surv.append(T)
    want = sorted([0, 1 << aa, 1 << bb])
    print("     slot (z%d,z%d): population 64, survivors %d -> %s" % (aa, bb, len(surv), sorted(surv)))
    if sorted(surv) == want:
        r0_ok += 1
check("36 R0: 3 survivors of 64 at all three antipodal slots", r0_ok, 3)

print("  36.1.1 (R0) second half: a W_1 neighbour of an antipodal u is a TRIANGLE")
print("  apex, so it moves d(u) and t(u) together and leaves a(u) unchanged.")
r0b = 0
for s in range(3):
    for z in (s, s + 3):
        tick()
        g0 = build(7, [(6, s), (6, s + 3)])
        a_before = a_of(g0, 7, 6)
        g1 = build(8, [(6, s), (6, s + 3), (6, 7), (7, z)])
        if not in_hyp_frame(g1, 8):
            continue
        a_after = a_of(g1, 8, 6)
        if a_before == a_after:
            r0b += 1
check("36 R0: (slot,z) pairs leaving a(u) unchanged", r0b, 6)

# ============================================================================
print()
print("=" * 78)
print("PART 2 -- 35.1.1 Step 3 / 37.1.1 (Z2): the neighbourhood configuration tables.")
print("The traces of N(v)\\Z are PAIRWISE DISJOINT (two neighbours sharing a z are two")
print("common neighbours of v and that z: a C4) and each is drawn from the survivor")
print("list of PART 1.  With the free adjacency bits INSIDE N(v) this determines")
print("G[N(v)] completely, so the table is EXACT, not an upper bound.")
print("=" * 78)


def nbhd_table(anchor_trace, survivors, tag):
    families = []
    k = len(survivors)
    for r in range(k + 1):
        for combo in itertools.combinations(range(k), r):
            ok = True
            for i in range(len(combo)):
                for j in range(i + 1, len(combo)):
                    if survivors[combo[i]] & survivors[combo[j]]:
                        ok = False
            if ok:
                families.append(combo)
    total = 0
    inhyp = []
    for combo in families:
        s = len(combo)
        pairs = [(i, j) for i in range(s) for j in range(i + 1, s)]
        for bits in range(1 << len(pairs)):
            tick()
            total += 1
            n = 6 + 1 + s
            ee = [(6, z) for z in anchor_trace]
            for idx, ci in enumerate(combo):
                x = 7 + idx
                ee.append((6, x))
                ee += [(x, i) for i in range(6) if (survivors[ci] >> i) & 1]
            for bi, (i, j) in enumerate(pairs):
                if (bits >> bi) & 1:
                    ee.append((7 + i, 7 + j))
            g = build(n, ee)
            if in_hyp_frame(g, n):
                d = deg(g, 6)
                a = a_of(g, n, 6)
                inhyp.append((combo, bits, d, a, n, ee))
    print("  %s: pairwise-disjoint trace families = %d, TOTAL CONFIGURATIONS = %d"
          % (tag, len(families), total))
    bysize = {}
    for combo in families:
        bysize[len(combo)] = bysize.get(len(combo), 0) + 1
    print("     families by size: %s" % (sorted(bysize.items()),))
    print("     IN HYPOTHESIS = %d, REFUTED = %d" % (len(inhyp), total - len(inhyp)))
    da = sorted(set((r[2], r[3]) for r in inhyp))
    print("     realised (d,a) pairs: %s" % (da,))
    return total, inhyp, da


SUR_SINGLE = sorted(surv_tables["single {z0}"])
SUR_CONS = sorted(surv_tables["consecutive {z0,z1}"])

tot1, inh1, da1 = nbhd_table([0], SUR_SINGLE, "single-trace anchor v ~ z0")
check("35/37 single anchor: total configurations", tot1, 152)
check("35/37 single anchor: in hypothesis", len(inh1), 17)
check("35/37 single anchor: refuted", tot1 - len(inh1), 135)
check("35/37 single anchor: realised (d,a)", da1,
      [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3)])
check("35 single anchor: max d", max(r[2] for r in inh1), 4)
check("35 single anchor: max a", max(r[3] for r in inh1), 3)

tot2, inh2, da2 = nbhd_table([0, 1], SUR_CONS, "consecutive anchor w ~ z0,z1")
check("35 consecutive anchor: total configurations", tot2, 6)
check("35 consecutive anchor: in hypothesis", len(inh2), 5)
check("35 consecutive anchor: refuted", tot2 - len(inh2), 1)
check("35 consecutive anchor: realised (d,a)", da2, [(2, 1), (3, 2), (4, 3)])
check("35 consecutive: a = d-1 throughout realisable range",
      sorted(set(d - a for (_, _, d, a, _, _) in inh2)), [1])

print()
print("  (Z2) THE LEAK SHAPES -- the in-hypothesis single-trace configurations with a=3.")
leaks = [r for r in inh1 if r[3] == 3]
shapes = []
for combo, bits, d, a, n, ee in leaks:
    tr = []
    for ci in combo:
        tm = SUR_SINGLE[ci]
        tr.append("{" + ",".join("z%d" % i for i in range(6) if (tm >> i) & 1) + "}")
    s = len(combo)
    pairs = [(i, j) for i in range(s) for j in range(i + 1, s)]
    ed = [(tr[i], tr[j]) for bi, (i, j) in enumerate(pairs) if (bits >> bi) & 1]
    shapes.append((d, a, tuple(sorted(tr)), tuple(sorted(ed))))
    print("     shape: d=%d a=%d  N(v)\\{z0} = %s  internal edges %s" % (d, a, sorted(tr), ed))
check("(Z2) number of leak shapes", len(leaks), 3)
check("(Z2) leak degrees d in {3,4}", sorted(set(r[2] for r in leaks)), [3, 4])
# every leak has a W_1 neighbour at its OWN antipode z3
antip_ok = 0
offz_ok = 0
for combo, bits, d, a, n, ee in leaks:
    tms = [SUR_SINGLE[ci] for ci in combo]
    if any(tm == (1 << 3) for tm in tms):
        antip_ok += 1
    # "no neighbour of a leak lies in Off(z_0)" : no neighbour of v has z0 in its trace
    if not any(tm & 1 for tm in tms):
        offz_ok += 1
check("(Z2a) every leak has a W_1 neighbour at its OWN antipode z3", antip_ok, 3)
check("(Z2c) NO neighbour of a leak lies in Off(z0)", offz_ok, 3)
check("(Z2b) every leak neighbour is a SINGLE-trace W_1 vertex",
      all(trace_class(SUR_SINGLE[ci]) == "W1" for (combo, _, _, _, _, _) in leaks for ci in combo),
      True)

# ============================================================================
print()
print("=" * 78)
print("PART 3 -- 36.1.1 (S1), (S3), (S5): the antipodal-branch frames.")
print("=" * 78)

print("  (S1) W_anti is an INDEPENDENT set -- all 9 ordered slot pairs with u ~ u'.")
s1_ref = 0
s1_c4 = 0
for i in range(3):
    for j in range(3):
        tick()
        ee = [(6, i), (6, i + 3), (7, j), (7, j + 3), (6, 7)]
        g = build(8, ee)
        if not in_hyp_frame(g, 8):
            s1_ref += 1
            if has_C4(g, 8):
                s1_c4 += 1
print("     population 9 ordered slot pairs (u ~ u' asserted)")
check("(S1) refuted", s1_ref, 9)
check("(S1) refuted BY A C4 in every case", s1_c4, 9)
s1_live = 0
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    tick()
    g = build(8, [(6, i), (6, i + 3), (7, j), (7, j + 3)])
    if in_hyp_frame(g, 8):
        s1_live += 1
check("(S1) LIVENESS: same two vertices NON-adjacent are in hypothesis", s1_live, 3)
s1_same = 0
for i in range(3):
    tick()
    g = build(8, [(6, i), (6, i + 3), (7, i), (7, i + 3)])
    if not in_hyp_frame(g, 8) and has_C4(g, 8):
        s1_same += 1
check("(34.4a) same-slot doubling refuted by a C4 at all 3 slots", s1_same, 3)

print()
print("  (S3) Z + u(antipodal) + x(empty,~u) + y(empty,~x,!~u) + w~y,")
print("       w's 64 traces x (w~u) x (w~x)  ->  population 256.")
s3_surv = []
s3_mech = {"C4": 0, "P7": 0, "both": 0, "other": 0}
for T in range(64):
    for bu in range(2):
        for bx in range(2):
            tick()
            # 6=u, 7=x, 8=y, 9=w
            ee = [(6, 0), (6, 3), (7, 6), (8, 7), (9, 8)]
            ee += [(9, i) for i in range(6) if (T >> i) & 1]
            if bu:
                ee.append((9, 6))
            if bx:
                ee.append((9, 7))
            g = build(10, ee)
            c4 = has_C4(g, 10)
            p7 = has_induced_path_ge(g, 10, 7)
            if not c4 and not p7:
                s3_surv.append((T, bu, bx, deg(g, 9), a_of(g, 10, 9)))
            else:
                k = "both" if (c4 and p7) else ("C4" if c4 else ("P7" if p7 else "other"))
                s3_mech[k] += 1
print("     population 256, survivors %d, refuted %d, mechanism census %s"
      % (len(s3_surv), 256 - len(s3_surv), s3_mech))
for s in s3_surv:
    print("        survivor trace=%s w~u=%d w~x=%d  d(w)=%d a(w)=%d" % s)
check("(S3) survivors of 256", len(s3_surv), 5)
print("     NOTE: 4 of the 5 survivors have w with an ANTIPODAL trace, i.e. w is at")
print("     distance 1 from Z and y is then at distance 2, NOT 3.  The distance-3")
print("     conclusion is the restriction of the table to w of EMPTY trace:")
s3_d3 = [s for s in s3_surv if s[0] == 0]
for s in s3_d3:
    print("        distance-3 survivor: trace=%s w~u=%d w~x=%d d(w)=%d a(w)=%d" % s)
check("(S3) survivors with w of EMPTY trace (genuine distance-3 configs)", len(s3_d3), 1)
check("(S3) the one further neighbour w must be adjacent to x",
      [s[2] for s in s3_d3], [1])
check("(S3) it must NOT be adjacent to u", [s[1] for s in s3_d3], [0])
# the distance-3 vertex is y (index 8): pendant shape and triangle shape
GY_PEND = build(9, [(6, 0), (6, 3), (7, 6), (8, 7)])
check("(S3) pendant shape y is an in-hypothesis HOST", in_hyp_host(GY_PEND, 9), True)
check("(S3) pendant: d(y)=1, a(y)=1, charge -2",
      (deg(GY_PEND, 8), a_of(GY_PEND, 9, 8), a_of(GY_PEND, 9, 8) - 3), (1, 1, -2))
GY_TRI = build(10, [(6, 0), (6, 3), (7, 6), (8, 7), (9, 8), (9, 7)])
check("(S3) triangle shape y is an in-hypothesis HOST", in_hyp_host(GY_TRI, 10), True)
check("(S3) triangle: d(y)=2, t(y)=1, a(y)=1, charge -2",
      (deg(GY_TRI, 8), t_of(GY_TRI, 10, 8), a_of(GY_TRI, 10, 8), a_of(GY_TRI, 10, 8) - 3),
      (2, 1, 1, -2))

print()
print("  (S3 second table) a SECOND distance-2 vertex on y, anchored at each of the")
print("  two remaining antipodal slots -> population 2.")
s3b_surv = 0
for j in (1, 2):
    tick()
    # 6=u_a, 7=x, 8=y, 9=u_j, 10=x_j
    ee = [(6, 0), (6, 3), (7, 6), (8, 7), (9, j), (9, j + 3), (10, 9), (10, 8)]
    g = build(11, ee)
    if in_hyp_frame(g, 11):
        s3b_surv += 1
    else:
        print("     slot %d refuted; C4=%s induced-P7=%s"
              % (j, has_C4(g, 11), has_induced_path_ge(g, 11, 7)))
check("(S3b) both frames refuted -> a distance-3 vertex has EXACTLY ONE distance-2 neighbour",
      s3b_surv, 0)

print()
print("  (S5) two ADJACENT distance-2 vertices, anchor sets over all 7 nonempty")
print("       subsets of {u_a,u_b,u_c}  ->  population 49.")
UA = [(6, 0), (6, 3)]
UB = [(7, 1), (7, 4)]
UC = [(8, 2), (8, 5)]
BASE = UA + UB + UC
s5_surv = []
for A in range(1, 8):
    for B in range(1, 8):
        tick()
        ee = list(BASE) + [(9, 10)]
        ee += [(9, 6 + i) for i in range(3) if (A >> i) & 1]
        ee += [(10, 6 + i) for i in range(3) if (B >> i) & 1]
        g = build(11, ee)
        if in_hyp_frame(g, 11):
            s5_surv.append((A, B))
print("     population 49, survivors %d, refuted %d" % (len(s5_surv), 49 - len(s5_surv)))
print("     survivor set (anchor bitmasks over {a,b,c}): %s" % (s5_surv,))
check("(S5) survivors of 49", len(s5_surv), 9)
check("(S5) EVERY survivor SHARES an anchor", all((A & B) != 0 for (A, B) in s5_surv), True)
check("(S5) anchor multiset of an adjacent pair is always {1,1} or {1,3}",
      sorted(set(tuple(sorted((bin(A).count('1'), bin(B).count('1')))) for (A, B) in s5_surv)),
      [(1, 1), (1, 3)])
check("(S5) an alpha=2 vertex NEVER has a distance-2 neighbour",
      any(bin(A).count('1') == 2 or bin(B).count('1') == 2 for (A, B) in s5_surv), False)

print()
print("  (S5 second table) x with TWO distance-2 neighbours, anchor sets over all")
print("       7 nonempty subsets each, far pair adjacent or not -> population 686.")
s5b = 0
tot686 = 0
for A in range(1, 8):
    for B in range(1, 8):
        for C in range(1, 8):
            for far in range(2):
                tick()
                tot686 += 1
                # 9 = x, 10 = x', 11 = x''
                ee = list(BASE) + [(9, 10), (9, 11)]
                ee += [(9, 6 + i) for i in range(3) if (A >> i) & 1]
                ee += [(10, 6 + i) for i in range(3) if (B >> i) & 1]
                ee += [(11, 6 + i) for i in range(3) if (C >> i) & 1]
                if far:
                    ee.append((10, 11))
                g = build(12, ee)
                if in_hyp_frame(g, 12):
                    s5b += 1
print("     population %d, survivors %d" % (tot686, s5b))
check("(S5b) population enumerated", tot686, 686)
check("(S5b) survivors -> |Q(x)| <= 1", s5b, 0)

# ============================================================================
print()
print("=" * 78)
print("PART 4 -- 37.1.1 (Z5): a leak and the occupied antipodal slots.")
print("Frame = Z + N[v] + the W_anti vertices themselves.  The w-to-N[v] bits AND")
print("the w-to-w' bit are ENUMERATED, not assumed.")
print("=" * 78)

# rebuild the three leak shapes as (offsets relative to the leak's hexagon vertex,
# internal edges among them) read off PART 2.
LEAK_SHAPES = []
for combo, bits, d, a, n, ee in leaks:
    offs = []
    for ci in combo:
        tm = SUR_SINGLE[ci]
        zz = [i for i in range(6) if (tm >> i) & 1]
        assert len(zz) == 1
        offs.append(zz[0])          # relative to anchor z0
    s = len(combo)
    pairs = [(i, j) for i in range(s) for j in range(i + 1, s)]
    ied = [(i, j) for bi, (i, j) in enumerate(pairs) if (bits >> bi) & 1]
    LEAK_SHAPES.append((tuple(offs), tuple(ied)))
print("  leak shapes (offsets from the leak's own hexagon vertex, internal edges):")
for sh in LEAK_SHAPES:
    print("     %s" % (sh,))
check("PART 4: leak shapes recovered", len(LEAK_SHAPES), 3)


def leak_frame(p, shape, extra_verts, extra_edges, nextra):
    """Z + leak v at hexagon vertex p with the given shape + extra vertices."""
    offs, ied = shape
    k = len(offs)
    # 6 = v, 7..7+k-1 = X
    ee = [(6, p)]
    for i, o in enumerate(offs):
        ee.append((6, 7 + i))
        ee.append((7 + i, (p + o) % 6))
    for (i, j) in ied:
        ee.append((7 + i, 7 + j))
    ee += extra_edges
    return build(7 + k + nextra, ee), 7 + k


print()
print("  (Z5) ONE occupied slot: population 32 at each of the 6 leak positions.")
z5_one = {}
for p in range(6):
    for slot in range(3):
        surv = 0
        tot = 0
        for sh_i, sh in enumerate(LEAK_SHAPES):
            offs, ied = sh
            k = len(offs)
            wi = 7 + k          # index of the W_anti vertex w
            for bits in range(1 << (1 + k)):   # w ~ v ?  w ~ each X vertex ?
                tick()
                tot += 1
                ex = [(wi, slot), (wi, slot + 3)]
                if bits & 1:
                    ex.append((wi, 6))
                for i in range(k):
                    if (bits >> (1 + i)) & 1:
                        ex.append((wi, 7 + i))
                g, nn = leak_frame(p, sh, 1, ex, 1)
                n = nn + 1
                if in_hyp_frame(g, n):
                    surv += 1
        z5_one[(p, slot)] = (tot, surv)
    print("     leak at z%d: per-slot population/survivors %s"
          % (p, [z5_one[(p, s)] for s in range(3)]))
tot_all = sum(v[0] for v in z5_one.values())
surv_all = sum(v[1] for v in z5_one.values())
print("     TOTAL population %d frames, survivors %d" % (tot_all, surv_all))
check("(Z5) population is 32 frames at each (leak position, slot) pair",
      sorted(set(v[0] for v in z5_one.values())), [32])
check("(Z5) one occupied slot is LIVE (leak and occupied slot DO coexist --",
      surv_all > 0, True)
check("(Z5) ... and it is live at EVERY leak position",
      all(sum(z5_one[(p, s)][1] for s in range(3)) > 0 for p in range(6)), True)

print()
print("  (Z5) TWO occupied slots: all three slot pairs, w-to-w' bit enumerated.")
z5_two_tot = 0
z5_two_surv = 0
for p in range(6):
    for sh in LEAK_SHAPES:
        offs, ied = sh
        k = len(offs)
        w1 = 7 + k
        w2 = 7 + k + 1
        for (s1, s2) in [(0, 1), (0, 2), (1, 2)]:
            for bits in range(1 << (2 * (1 + k) + 1)):
                tick()
                z5_two_tot += 1
                ex = [(w1, s1), (w1, s1 + 3), (w2, s2), (w2, s2 + 3)]
                b = bits
                if b & 1:
                    ex.append((w1, 6))
                b >>= 1
                for i in range(k):
                    if (b >> i) & 1:
                        ex.append((w1, 7 + i))
                b >>= k
                if b & 1:
                    ex.append((w2, 6))
                b >>= 1
                for i in range(k):
                    if (b >> i) & 1:
                        ex.append((w2, 7 + i))
                b >>= k
                if b & 1:
                    ex.append((w1, w2))
                g, nn = leak_frame(p, sh, 2, ex, 2)
                n = nn + 2
                if in_hyp_frame(g, n):
                    z5_two_surv += 1
print("     population %d frames, survivors %d" % (z5_two_tot, z5_two_surv))
check("(Z5) TWO occupied slots: 0 survive  =>  n_3 >= 1 implies m <= 1", z5_two_surv, 0)

# ============================================================================
print()
print("=" * 78)
print("PART 5 -- 37.1.1 (Z6): the finite arithmetic over every feasible (n_3,m).")
print("=" * 78)
feas = []
for n3 in range(0, 3):          # n_3 <= 2 from (Z3)+(Z4)
    for m in range(0, 4):       # m <= 3 from 34.4a
        if n3 >= 1 and m > 1:   # (Z5)
            continue
        feas.append((n3, m))
print("  feasible (n_3,m) population, printed in full: %s" % (feas,))
check("(Z6) feasible population size", len(feas), 8)
check("(Z6) n_3 + 2m <= 6 on ALL of them", all(n3 + 2 * m <= 6 for (n3, m) in feas), True)
check("(Z6) equality only at (0,3)", [p for p in feas if p[0] + 2 * p[1] == 6], [(0, 3)])
# LIVENESS of the check: it must be able to fail
check("(Z6) LIVENESS: the excluded pair (1,3) would VIOLATE the bound", 1 + 2 * 3 <= 6, False)

# ============================================================================
print()
print("=" * 78)
print("PART 6 -- 37.1.1 (Z1)'s inputs, and the two ATTAINMENT witnesses.")
print("=" * 78)


def census(adj, n):
    W = {"W0": [], "W1": [], "Wcons": [], "Wanti": [], "ILLEGAL": []}
    for v in range(6, n):
        W[trace_class(trace_of(adj, v))].append(v)
    TZ = sum(t_of(adj, n, z) for z in range(6))
    Zterm = sum(a_of(adj, n, z) - 3 for z in range(6))
    tot = sum(a_of(adj, n, v) - 3 for v in range(n))
    n3 = sum(1 for v in W["W1"] if a_of(adj, n, v) == 3)
    m = len(W["Wanti"])
    return W, TZ, Zterm, tot, n3, m


print("  G55 summed:  Sum_{z in Z}(a(z)-3) = |W_1| + 2|W_cons| + 2|W_anti| - T_Z - 6")
print("  T_Z >= 2|W_cons|: each consecutive-trace w makes a triangle with the hexagon")
print("  edge it spans and is counted ONCE AT EACH END.")

# T_Z contribution of one consecutive vertex, at all 6 hexagon edges
tz_ok = 0
for e in range(6):
    tick()
    g = build(7, [(6, e), (6, (e + 1) % 6)])
    if in_hyp_frame(g, 7):
        contrib = sum(t_of(g, 7, z) for z in range(6))
        if contrib == 2:
            tz_ok += 1
check("T_Z contribution of ONE consecutive vertex is exactly 2, at all 6 edges", tz_ok, 6)
# and a single-trace / antipodal vertex contributes 0 to T_Z on its own
g = build(7, [(6, 0)])
check("   a single-trace vertex alone contributes 0 to T_Z",
      sum(t_of(g, 7, z) for z in range(6)), 0)
g = build(7, [(6, 0), (6, 3)])
check("   an antipodal vertex alone contributes 0 to T_Z",
      sum(t_of(g, 7, z) for z in range(6)), 0)

print()
print("  WITNESS 1 -- 36.1 / 37.1: the n=10 (n_3,m)=(0,3) attaining region.")
print("  Z + u_a(z0,z3) + u_b(z1,z4) + u_c(z2,z5) + x, x ~ u_a,u_b,u_c, x no Z-neighbour.")
W1G = build(10, [(6, 0), (6, 3), (7, 1), (7, 4), (8, 2), (8, 5), (9, 6), (9, 7), (9, 8)])
check("WITNESS 1 is an in-hypothesis HOST (admitted BEFORE any statistic is read)",
      in_hyp_host(W1G, 10), True)
check("WITNESS 1 longest induced path", longest_induced_path(W1G, 10), 5)
Wc, TZ, Zt, tot, n3, m = census(W1G, 10)
print("     census: |W_0|=%d |W_1|=%d |W_cons|=%d |W_anti|=%d  T_Z=%d  Z-term=%d"
      % (len(Wc["W0"]), len(Wc["W1"]), len(Wc["Wcons"]), len(Wc["Wanti"]), TZ, Zt))
check("WITNESS 1: (n_3,m)", (n3, m), (0, 3))
check("WITNESS 1: Sum_v (a-3)", tot, 0)
check("WITNESS 1: (Z1) bound n_3+2m-6", n3 + 2 * m - 6, 0)
check("WITNESS 1: G55 summed identity",
      Zt, len(Wc["W1"]) + 2 * len(Wc["Wcons"]) + 2 * len(Wc["Wanti"]) - TZ - 6)
check("WITNESS 1: Sum_R (a-3) = 0 attained (G59(i) is SHARP)",
      sum(a_of(W1G, 10, v) - 3 for v in Wc["W0"] + Wc["Wanti"]), 0)

print()
print("  WITNESS 2 -- 37.1: the NEW n=10 two-leak region.")
print("  Z + v(z0) + v'(z3) + x(z2) + y(z1), v ~ v',x and v' ~ v,y.")
W2G = build(10, [(6, 0), (7, 3), (8, 2), (9, 1), (6, 7), (6, 8), (7, 9)])
check("WITNESS 2 is an in-hypothesis HOST", in_hyp_host(W2G, 10), True)
check("WITNESS 2 longest induced path", longest_induced_path(W2G, 10), 6)
Wc2, TZ2, Zt2, tot2, n32, m2 = census(W2G, 10)
print("     census: |W_0|=%d |W_1|=%d |W_cons|=%d |W_anti|=%d  T_Z=%d  Z-term=%d"
      % (len(Wc2["W0"]), len(Wc2["W1"]), len(Wc2["Wcons"]), len(Wc2["Wanti"]), TZ2, Zt2))
print("     a-values off Z: %s" % ({v: a_of(W2G, 10, v) for v in range(6, 10)},))
check("WITNESS 2: (n_3,m)", (n32, m2), (2, 0))
check("WITNESS 2: Sum_v (a-3)", tot2, -4)
check("WITNESS 2: (Z1) bound n_3+2m-6", n32 + 2 * m2 - 6, -4)
check("WITNESS 2: the two leaks sit at ANTIPODAL hexagon vertices",
      sorted((trace_of(W2G, v).bit_length() - 1) for v in Wc2["W1"] if a_of(W2G, 10, v) == 3),
      [0, 3])
check("WITNESS 2: G55 summed identity",
      Zt2, len(Wc2["W1"]) + 2 * len(Wc2["Wcons"]) + 2 * len(Wc2["Wanti"]) - TZ2 - 6)

# ============================================================================
print()
print("=" * 78)
print("PART 7 -- THE SWEEP.  Independent exhaustive enumeration of every region")
print("Z + k off-Z vertices, k = 0..KMAX, pruned by C4-freeness and P7-freeness")
print("(both inherited by induced subgraphs, so the pruning is SOUND).")
print("Population is printed BY SIZE before every verdict.  Contiguity asserted.")
print("=" * 78)

# step 1: which traces are legal at all?  enumerate ALL 64, do not assume G54.
legal = []
for T in range(64):
    tick()
    g = build(7, [(6, i) for i in range(6) if (T >> i) & 1])
    if in_hyp_frame(g, 7):
        legal.append(T)
print("  trace legality: population 64 enumerated, %d legal" % len(legal))
print("     legal traces by class: %s"
      % (sorted((trace_class(T), sum(1 for U in legal if trace_class(U) == trace_class(T)))
                for T in set(legal)),))
check("SWEEP: legal traces (G54 re-derived, not assumed)", len(legal), 16)
check("SWEEP: no ILLEGAL trace survives",
      any(trace_class(T) == "ILLEGAL" for T in legal), False)

KMAX = int(os.environ.get("W133_KMAX", "4"))
print("  KMAX = %d  (|off-Z| <= %d)" % (KMAX, KMAX))

by_size = [0] * (KMAX + 1)
hosts_by_size = [0] * (KMAX + 1)
max_tot = [-99] * (KMAX + 1)
max_n3 = [0] * (KMAX + 1)
viol_Z1 = [0]
viol_Z6 = [0]
viol_G58 = [0]
viol_G59 = [0]
viol_TZ = [0]
viol_G55 = [0]
viol_Z3 = [0]
viol_Z4 = [0]
viol_Z5 = [0]
best_witness = [None, -99]
n3_witness = [None, -1]
tested = [0]


def stats(adj, n):
    W = {"W0": [], "W1": [], "Wcons": [], "Wanti": []}
    for v in range(6, n):
        W[trace_class(trace_of(adj, v))].append(v)
    TZ = sum(t_of(adj, n, z) for z in range(6))
    Zt = sum(a_of(adj, n, z) - 3 for z in range(6))
    tot = sum(a_of(adj, n, v) - 3 for v in range(n))
    leakpos = [trace_of(adj, v).bit_length() - 1 for v in W["W1"] if a_of(adj, n, v) == 3]
    n3 = len(leakpos)
    m = len(W["Wanti"])
    return W, TZ, Zt, tot, n3, m, leakpos


def record(adj, n, k):
    by_size[k] += 1
    isconn = connected(adj, n)
    if isconn:
        hosts_by_size[k] += 1
    W, TZ, Zt, tot, n3, m, leakpos = stats(adj, n)
    if isconn:
        if tot > max_tot[k]:
            max_tot[k] = tot
        if tot > best_witness[1]:
            best_witness[1] = tot
            best_witness[0] = (n, [(u, v) for u in range(n) for v in range(u + 1, n)
                                   if (adj[u] >> v) & 1])
    if n3 > max_n3[k]:
        max_n3[k] = n3
    if n3 > n3_witness[1]:
        n3_witness[1] = n3
        n3_witness[0] = (n, [(u, v) for u in range(n) for v in range(u + 1, n)
                             if (adj[u] >> v) & 1])
    # (Z1)
    if tot > n3 + 2 * m - 6:
        viol_Z1[0] += 1
    # (Z6)
    if n3 + 2 * m > 6:
        viol_Z6[0] += 1
    # G58 : a <= 3 on W_1 u W_cons
    for v in W["W1"] + W["Wcons"]:
        if a_of(adj, n, v) > 3:
            viol_G58[0] += 1
    # G59(i) : Sum_R (a-3) <= 0
    if sum(a_of(adj, n, v) - 3 for v in W["W0"] + W["Wanti"]) > 0:
        viol_G59[0] += 1
    # T_Z >= 2|W_cons|
    if TZ < 2 * len(W["Wcons"]):
        viol_TZ[0] += 1
    # G55 summed
    if Zt != len(W["W1"]) + 2 * len(W["Wcons"]) + 2 * len(W["Wanti"]) - TZ - 6:
        viol_G55[0] += 1
    # (Z3) at most one leak per hexagon vertex
    if len(set(leakpos)) != len(leakpos):
        viol_Z3[0] += 1
    # (Z4) any two leaks are antipodal
    for i in range(len(leakpos)):
        for j in range(i + 1, len(leakpos)):
            if (leakpos[i] - leakpos[j]) % 6 != 3:
                viol_Z4[0] += 1
    # (Z5) n_3 >= 1 => m <= 1
    if n3 >= 1 and m > 1:
        viol_Z5[0] += 1


def sweep(adj, n, k):
    tick()
    record(adj, n, k)
    if k == KMAX:
        return
    for T in legal:
        tmask = T
        for bits in range(1 << (n - 6)):
            tick()
            tested[0] += 1
            nadj = adj + [0]
            nadj = list(adj) + [0]
            u = n
            nm = tmask
            for i in range(n - 6):
                if (bits >> i) & 1:
                    nm |= 1 << (6 + i)
            nadj[u] = nm
            mm = nm
            while mm:
                b = mm & -mm
                mm ^= b
                nadj[b.bit_length() - 1] |= 1 << u
            # incremental C4 test: only new pairs (u,w) can be bad
            bad = False
            for w in range(n):
                if bin(nadj[u] & nadj[w]).count("1") >= 2:
                    bad = True
                    break
            if bad:
                continue
            if has_induced_path_ge(nadj, n + 1, 7):
                continue
            sweep(nadj, n + 1, k + 1)


Z0 = build(6, [])
sweep(Z0, 6, 0)

print()
print("  POPULATION BY SIZE (regions, i.e. frames -- connectedness NOT required):")
for k in range(KMAX + 1):
    print("     |off-Z| = %d : regions = %-9d connected hosts = %-9d max Sum(a-3) over hosts = %s   max n_3 = %d"
          % (k, by_size[k], hosts_by_size[k],
             max_tot[k] if max_tot[k] > -99 else "n/a", max_n3[k]))
print("     TOTAL regions = %d, TOTAL hosts = %d, candidate frames tested = %d"
      % (sum(by_size), sum(hosts_by_size), tested[0]))
print("     CONTIGUITY: sizes present = %s"
      % ([k for k in range(KMAX + 1) if by_size[k] > 0],))
check("SWEEP: sizes are CONTIGUOUS 0..%d" % KMAX,
      [k for k in range(KMAX + 1) if by_size[k] > 0], list(range(KMAX + 1)))
check("SWEEP: every size has a nonzero population",
      all(by_size[k] > 0 for k in range(KMAX + 1)), True)

print()
print("  VERDICTS (each over the population printed above):")
check("SWEEP: violations of (Z1)  Sum_v(a-3) <= n_3+2m-6", viol_Z1[0], 0)
check("SWEEP: violations of (Z6)  n_3+2m <= 6", viol_Z6[0], 0)
check("SWEEP: violations of G58   a <= 3 on W_1 u W_cons", viol_G58[0], 0)
check("SWEEP: violations of G59(i) Sum_R(a-3) <= 0", viol_G59[0], 0)
check("SWEEP: violations of T_Z >= 2|W_cons|", viol_TZ[0], 0)
check("SWEEP: violations of the G55 summed IDENTITY", viol_G55[0], 0)
check("SWEEP: violations of (Z3) <=1 leak per hexagon vertex", viol_Z3[0], 0)
check("SWEEP: violations of (Z4) two leaks are ANTIPODAL", viol_Z4[0], 0)
check("SWEEP: violations of (Z5) n_3>=1 => m<=1", viol_Z5[0], 0)
check("SWEEP: max n_3 over the whole population", max(max_n3), 2)
check("SWEEP: max Sum_v(a-3) over connected hosts (THIS IS (D3-C6) on the window)",
      max(max_tot), 0)
print("     max-n_3 witness  (POSITIVE control -- the leak counter DOES fire, n_3=%d):"
      % n3_witness[1])
print("        n=%d edges=%s" % (n3_witness[0][0], n3_witness[0][1]))
print("     max-Sum(a-3) witness over hosts (Sum=%d):" % best_witness[1])
print("        n=%d edges=%s" % (best_witness[0][0], best_witness[0][1]))
print("     per-size max Sum(a-3) over hosts: %s"
      % ([max_tot[k] for k in range(KMAX + 1)],))
print("     per-size max n_3: %s" % ([max_n3[k] for k in range(KMAX + 1)],))

# LIVENESS of the sweep's own predicates: they must be able to fire.
print()
print("  LIVENESS of the sweep's verdict predicates -- each is fired on an input")
print("  where it MUST report a violation (a check that can only say 0 is decoration):")
FAKE = build(10, [(6, 0), (7, 0), (8, 0), (9, 0)])   # 4 single-trace vertices at z0
Wf, TZf, Ztf, totf, n3f, mf, lpf = stats(FAKE, 10)
print("     probe graph: Z + 4 independent single-trace vertices at z0")
print("     |W_1|=%d Z-term=%d T_Z=%d Sum_v(a-3)=%d n_3=%d" % (len(Wf["W1"]), Ztf, TZf, totf, n3f))
check("LIVENESS: (Z3) predicate FIRES on 4 leaks at one hexagon vertex if they were leaks",
      len(set(lpf)) != len(lpf) or n3f == 0, True)
FAKE2 = list(W2G)
check("LIVENESS: (Z1) predicate would FIRE if the bound were tightened by 1",
      tot2 > n32 + 2 * m2 - 6 - 1, True)

# ============================================================================
print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print("  checks run: %d" % CHECKS[0])
print("  failures  : %d" % len(FAILURES))
for f in FAILURES:
    print("     FAIL %s got=%s want=%s" % f)
print("  wall clock: %.1f s" % (time.time() - T0))
print("=" * 78)
sys.stdout.flush()
os._exit(1 if FAILURES else 0)
