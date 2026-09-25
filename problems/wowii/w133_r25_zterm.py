#!/usr/bin/env python3
"""
w133 round 25 -- THE Z-TERM / THE W_1 LEAK: the last named gap in (D3-C6).

WHERE THE FRONT STOOD (round 24 / draft 36, planner cert r24).
    (D3-C6) hypotheses: connected, C4-FREE, contains an induced C6 Z=(z_0..z_5), NO
    INDUCED P7.  V = Z + W_1 + W_cons + W_anti + W_0 (G54).  G58 (round 23) bounds
    a(v) <= 3 on W_1 + W_cons; (B) (round 24) gives Sum_{R}(a-3) <= 0 on R := W_anti+W_0,
    hence the WHOLE off-cycle term is <= 0.  What was left, and what this file answers, is
    the Z-TERM: G55 summed carries a  +|W_1|  that is paid only if Sum_{W_1}(a(v)-2) fits
    in the slack -- and G58's value a = 3 IS ATTAINED on W_1, so a W_1 vertex CAN leak +1.

THE STATEMENT THIS FILE CERTIFIES.

    Write  n3 := #{ v in W_1 : a(v) = 3 }   (the LEAKING vertices)  and  m := |W_anti|.

    (Z1)  Sum_{v in V} (a(v)-3)  <=  n3 + 2m - 6.                [G55 + G58 + (B)]
    (Z2)  A leak has a SHAPE: a(v)=3 for v in W_1 with trace {z_i} forces d(v) in {3,4}
          and N(v)\{z_i} = 2 or 3 SINGLE-trace W_1 vertices at z_{i+2},z_{i+3} /
          z_{i+3},z_{i+4} / all three (with exactly the +2 ~ +4 edge).  In particular a
          leak ALWAYS has a W_1 neighbour at its own ANTIPODE.
    (Z3)  At most ONE leak per hexagon vertex.
    (Z4)  Two leaks can sit only at ANTIPODAL hexagon vertices.  With (Z3): n3 <= 2.
    (Z5)  A leak coexists with at most ONE occupied antipodal slot: n3 >= 1  =>  m <= 1.
    (Z6)  Hence  n3 + 2m <= 6,  and therefore

              *** Sum_{v in V} (a(v) - 3)  <=  0  for every graph in (D3-C6)'s class ***

          which is (D3-C6).  BOTH extremal regimes are attained: (n3,m) = (0,3) at the
          n=10 region of round 24, and (n3,m) = (2,0) at an n=10 region exhibited here.

RULING BW binds: every load-bearing bound below is an EXHAUSTIVE ENUMERATION with its
population printed BEFORE its verdict.  Round 24's own record is why: a hand claim there
was not weak but BACKWARDS.  This round's hand claims were wrong twice again -- see the
state file, and PART 3's note.
RULING BM: a Sample refuses to report a statistic before admit().
RULING BV: the membership test is written against the OBJECT it tests (frame vs host).
RULING CG: the string probes in PART 8 are EVIDENCE, NOT CHECKS -- a probe whose blind
spot is the ENCODING of the token it looks for cannot certify absence.  The inputs that
carry load are ASSERTED as graph facts, not as strings.

C4-FREE throughout means: NO TWO DISTINCT VERTICES HAVE TWO COMMON NEIGHBOURS.
Wall-clock self-limit 900 s, exit(2) on overrun.  No SAT.
"""
import itertools, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w133_r22_namespace import (mkadj, c4_all, c4_free, connected, longest_induced_path,
                                is_induced_c6, triangles_at, alpha_of_nbhd, trace)
from w133_r23_offcycle import Sample, induced_path_witness, trace_type, legal_trace

T0 = time.time()
LIMIT = 900.0
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

REPO  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRAFT = os.path.join(REPO, "notes", "proofs", "wowii133_draft.md")
STATE = os.path.join(REPO, "orchestration", "results", "w133_state.md")

HEX  = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
Z6   = [0,1,2,3,4,5]
ANTI = [(0,3),(1,4),(2,5)]
SINGLE_OK = [(0,), (2,), (3,), (4,), (0,3), (2,3), (3,4)]   # r23 PART 1A survivors


# ============================================================================
# PART 0 -- POSITIVE CONTROLS BEFORE ANY OF THE TOOLING IS USED
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
    ok = True
    for E, n in [(PET, 10), (HEX, 6), (HEX + [(6,0),(6,3),(7,6)], 8)]:
        ad = mkadj(n, E)
        for v in range(n):
            if alpha_of_nbhd(ad, v) != len(ad[v]) - triangles_at(ad, v): ok = False
    check("control: a(v) == d(v) - t(v) on every C4-free control (G[N(v)] is a matching)", ok)
    s = Sample("guard-probe", 8, HEX + [(6,0),(7,6)])
    fired = False
    try: s.a(6)
    except AssertionError as e: fired = ("BEFORE admit" in str(e))
    check("RULING BM: reading a statistic BEFORE admit() RAISES", fired)
    e_iso = HEX + [(6,7)]
    sf, sh = Sample("iso-frame", 8, e_iso, mode="frame"), Sample("iso-host", 8, e_iso, mode="host")
    okf, okh = sf.admit(verbose=False), sh.admit(verbose=False)
    check("RULING BV: the SAME edge list is admitted as a FRAME and rejected as a HOST",
          okf and not okh and any("connected" in w for w in sh.why))
    # the fast in-house P7 detector used by PART 7 is cross-checked against the trusted one
    import random
    random.seed(20260823)
    mism = 0
    for _ in range(400):
        n = random.randint(4, 9)
        edges = [(i,j) for i in range(n) for j in range(i+1,n) if random.random() < 0.35]
        bm = [0]*n
        for i,j in edges: bm[i] |= 1 << j; bm[j] |= 1 << i
        ref = longest_induced_path(mkadj(n, edges))
        for k in (5,6,7):
            if has_induced_pk(bm, n, k) != (ref >= k): mism += 1
    check("control: the fast bitmask induced-P_k detector AGREES with the trusted "
          "longest_induced_path on 400 random graphs x 3 lengths", mism == 0,
          "%d mismatches" % mism)
    tick("part0")


# ============================================================================
# fast primitives used only by PART 7's sweep (cross-checked in PART 0)
# ============================================================================
def has_induced_pk(adj, n, k):
    def ext(last, pathmask, length):
        if length == k: return True
        c = adj[last] & ~pathmask
        while c:
            b = c & -c; c ^= b
            u = b.bit_length() - 1
            if adj[u] & pathmask & ~(1 << last): continue
            if ext(u, pathmask | b, length + 1): return True
        return False
    for s in range(n):
        if ext(s, 1 << s, 1): return True
    return False

def new_c4(adj, n, v):
    for j in range(n):
        if j == v: continue
        if bin(adj[v] & adj[j]).count("1") >= 2: return True
    return False

def alpha_bm(adj, v):
    d = bin(adj[v]).count("1"); t = 0
    nb = []; m = adj[v]
    while m:
        b = m & -m; m ^= b; nb.append(b.bit_length() - 1)
    for i in range(len(nb)):
        for j in range(i+1, len(nb)):
            if adj[nb[i]] >> nb[j] & 1: t += 1
    return d - t


# ============================================================================
# PART 1 -- (Z1): the global count reduces to  n3 + 2m - 6
# ============================================================================
INSTANCES = [
    ("INSTANCE-D  n=9",  9,  HEX + [(6,0),(6,1),(7,2),(7,3),(8,4),(8,5)]),
    ("INSTANCE-E  n=12", 12, HEX + [(6,0),(6,1),(7,2),(7,3),(8,4),(8,5),
                                    (9,0),(9,3),(10,1),(10,4),(11,2),(11,5)]),
    ("r24 attaining region n=10", 10, HEX + [(6,0),(6,3),(7,1),(7,4),(8,2),(8,5),
                                             (9,6),(9,7),(9,8)]),
    ("34.4b fan k=7 n=13", 13, HEX + [(6+i, 0) for i in range(7)]),
    ("2-LEAK region n=10", 10, HEX + [(6,0),(7,3),(6,7),(8,2),(8,6),(9,1),(9,7)]),
]

def classify(s):
    W1 = [v for v in range(s.n) if v not in Z6 and len(s.tr(v)) == 1]
    Wc = [v for v in range(s.n) if v not in Z6 and trace_type(s.tr(v)) == "consecutive"]
    Wa = [v for v in range(s.n) if v not in Z6 and trace_type(s.tr(v)) == "antipodal"]
    W0 = [v for v in range(s.n) if v not in Z6 and len(s.tr(v)) == 0]
    return W1, Wc, Wa, W0

def part1():
    print("\n=== PART 1 -- (Z1): G55 summed + T_Z >= 2|W_cons| + G58 + (B) collapse the ===")
    print("===           global count to   Sum_v (a(v)-3)  <=  n3 + 2m - 6            ===")
    print("  The three inputs are USED, not re-proved: G55 (a(z) = 2+|Off(z)|-t(z)),")
    print("  G58 (a <= 3 on W_1 + W_cons), (B) (Sum_R (a-3) <= 0).  What is checked here")
    print("  is the ARITHMETIC that assembles them, on in-hypothesis instances.")
    bad_id = bad_tz = bad_z1 = 0
    print("  %-28s %4s %4s %4s %4s %4s | %6s %6s %5s %3s %3s | %7s %8s"
          % ("instance","n","|W1|","|Wc|","|Wa|","|W0|","Z-term","offterm","total","n3","m","T_Z","2|Wc|"))
    for tag, n, E in INSTANCES:
        s = Sample(tag, n, E, mode="host")
        if not s.admit(verbose=False):
            print("      %-28s OUT OF HYPOTHESIS: %s" % (tag, "; ".join(s.why))); bad_id += 1; continue
        W1, Wc, Wa, W0 = classify(s)
        TZ = sum(s.t(z) for z in Z6)
        zterm  = sum(s.a(z) - 3 for z in Z6)
        offterm= sum(s.a(v) - 3 for v in range(n) if v not in Z6)
        rhs    = len(W1) + 2*len(Wc) + 2*len(Wa) - TZ - 6
        n3     = sum(1 for v in W1 if s.a(v) == 3)
        m      = len(Wa)
        if zterm != rhs: bad_id += 1
        if TZ < 2*len(Wc): bad_tz += 1
        if zterm + offterm > n3 + 2*m - 6: bad_z1 += 1
        print("  %-28s %4d %4d %4d %4d %4d | %6d %6d %5d %3d %3d | %7d %8d"
              % (tag, n, len(W1), len(Wc), len(Wa), len(W0),
                 zterm, offterm, zterm+offterm, n3, m, TZ, 2*len(Wc)))
    check("G55 SUMMED is an identity on every in-hypothesis instance: "
          "Sum_Z(a(z)-3) = |W_1|+2|W_cons|+2|W_anti| - T_Z - 6", bad_id == 0,
          "%d discrepancies" % bad_id)
    check("T_Z >= 2|W_cons| on every instance (each consecutive-trace vertex makes a "
          "triangle with the hexagon edge it spans, once at EACH end)", bad_tz == 0)
    check("(Z1) holds on every instance:  Sum_v(a(v)-3) <= n3 + 2m - 6", bad_z1 == 0)
    # the inequality T_Z >= 2|W_cons| proved rather than sampled
    print("  PROOF of T_Z >= 2|W_cons|, machine-verified on the generic frame: for w with")
    print("  trace {z_i,z_{i+1}},  w and z_{i+1} lie in N(z_i) and are adjacent, and w and")
    print("  z_i lie in N(z_{i+1}) and are adjacent -- 2 distinct triangle edges per w.")
    per = []
    for i in range(6):
        e = list(HEX) + [(6, i), (6, (i+1) % 6)]
        s = Sample("cons at (z%d,z%d)" % (i, (i+1) % 6), 7, e, mode="frame")
        s.admit(verbose=False)
        per.append(s.t(i) + s.t((i+1) % 6))
    check("each W_cons vertex contributes EXACTLY 2 to T_Z, at all 6 hexagon edges",
          per == [2]*6, "observed %r" % per)
    tick("part1")


# ============================================================================
# PART 2 -- (Z2): THE SHAPE OF A LEAK.  Exhaustive over G[N(v)], so it is COMPLETE
# ============================================================================
def leak_configs(i):
    """The three a=3 shapes at anchor slot z_i, as (far traces, internal edges)."""
    m = lambda d: (i + d) % 6
    return [((m(2), m(3)), ()), ((m(3), m(4)), ()), ((m(2), m(3), m(4)), ((0, 2),))]

def part2():
    print("\n=== PART 2 -- (Z2) THE SHAPE OF A LEAK: a(v)=3 on W_1 is enumerated, not assumed ===")
    print("  N(v) = {z_0} + off-Z neighbours whose traces are PAIRWISE DISJOINT (two")
    print("  neighbours sharing a z would be two common neighbours of v and that z: a C4)")
    print("  and each drawn from r23 PART 1A's 7 survivors.  With the free adjacency bits")
    print("  INSIDE N(v) this determines G[N(v)] COMPLETELY, so the table below is exact.")
    nframes = admitted = 0
    shapes = []
    pareto = set()
    for r in range(0, len(SINGLE_OK) + 1):
        for combo in itertools.combinations(SINGLE_OK, r):
            flat = [z for T in combo for z in T]
            if len(flat) != len(set(flat)): continue
            for bits in range(1 << (r * (r - 1) // 2)):
                edges = list(HEX) + [(6, 0)]
                us = list(range(7, 7 + r))
                for u, T in zip(us, combo):
                    edges.append((u, 6)); edges += [(u, z) for z in T]
                b = 0; ue = []
                for x in range(r):
                    for y in range(x + 1, r):
                        if (bits >> b) & 1: edges.append((us[x], us[y])); ue.append((x, y))
                        b += 1
                nframes += 1
                s = Sample("leak-shape", 7 + r, edges, mode="frame")
                if not s.admit(verbose=False): continue
                admitted += 1
                pareto.add((s.d(6), s.a(6)))
                if s.a(6) == 3:
                    shapes.append((tuple(tuple(t) for t in combo), tuple(ue)))
        tick("part2-r%d" % r)
    print("      observed population: %d neighbourhood configurations enumerated, "
          "%d in hypothesis, %d refuted" % (nframes, admitted, nframes - admitted))
    print("      observed (d,a) realised: %r" % sorted(pareto))
    print("      observed a=3 SHAPES (%d of them):" % len(shapes))
    for sh in shapes: print("         far traces %r   internal edges %r" % ([list(t) for t in sh[0]], sh[1]))
    want = [((( 2,), ( 3,)), ()), ((( 3,), ( 4,)), ()), ((( 2,), ( 3,), ( 4,)), ((0, 2),))]
    check("(Z2) a leak has EXACTLY the three shapes {+2,+3}, {+3,+4}, {+2,+3,+4}(+2~+4)",
          sorted(shapes) == sorted(want), "observed %r" % sorted(shapes))
    check("(Z2a) EVERY leak has a SINGLE-trace W_1 neighbour at its OWN ANTIPODE z_{i+3}",
          all(any(t == (3,) for t in sh[0]) for sh in shapes))
    check("(Z2b) EVERY off-Z neighbour of a leak is a SINGLE-trace W_1 vertex, at a "
          "hexagon vertex at distance >= 2 from the leak's own",
          all(all(len(t) == 1 and min((t[0]-0) % 6, (0-t[0]) % 6) >= 2 for t in sh[0])
              for sh in shapes))
    check("(Z2c) NO neighbour of a leak lies in Off(z_0): a leak contributes 0 to E_off",
          all(all(0 not in t for t in sh[0]) for sh in shapes))
    check("liveness: a=3 IS realised on W_1 (so this is a real gap, not an accounting step)",
          (3, 3) in pareto and (4, 3) in pareto)
    tick("part2")
    return shapes


# ============================================================================
# PART 3/4 -- (Z3),(Z4): where two leaks may sit.  Frames = Z + N[v] + N[v'].
# ============================================================================
def two_leak_frames(i, j):
    """EVERY induced subgraph on Z + N[v] + N[v'] of a host carrying a leak at z_i and a
    leak at z_j: every shape pair, every identification pattern (v' may BE a neighbour of
    v; their far neighbours may coincide), every free bit between the two neighbourhoods.
    N(v) is exactly {z_i} + its far set, so v is non-adjacent to everything else in the
    frame -- that is what makes the free-bit set small and the enumeration complete."""
    tot = 0; surv = []
    for (Xt, Xe) in leak_configs(i):
        for (Yt, Ye) in leak_configs(j):
            for adjvv in (False, True):
                if adjvv and not (j in Xt and i in Yt): continue
                A = [t for t in Xt if not (adjvv and t == j)]
                B = [t for t in Yt if not (adjvv and t == i)]
                common = [(a, b) for a in range(len(A)) for b in range(len(B)) if A[a] == B[b]]
                for r in range(len(common) + 1):
                    for match in itertools.combinations(common, r):
                        if len(set(x[0] for x in match)) != r: continue
                        if len(set(x[1] for x in match)) != r: continue
                        v, vp = 6, 7
                        Aid = {a: 8 + a for a in range(len(A))}
                        Bid = {}; nxt = 8 + len(A)
                        for (a, b) in match: Bid[b] = Aid[a]
                        for b in range(len(B)):
                            if b not in Bid: Bid[b] = nxt; nxt += 1
                        edges = list(HEX) + [(v, i), (vp, j)]
                        if adjvv: edges.append((v, vp))
                        for a in range(len(A)): edges += [(Aid[a], v), (Aid[a], A[a])]
                        for b in range(len(B)): edges += [(Bid[b], vp), (Bid[b], B[b])]
                        Xnode = [(vp if (adjvv and t == j) else Aid[A.index(t)]) for t in Xt]
                        Ynode = [(v  if (adjvv and t == i) else Bid[B.index(t)]) for t in Yt]
                        for (p, q) in Xe: edges.append((Xnode[p], Xnode[q]))
                        for (p, q) in Ye: edges.append((Ynode[p], Ynode[q]))
                        forb = set()
                        for p in range(len(Xt)):
                            for q in range(p + 1, len(Xt)):
                                if (p, q) not in Xe: forb.add(frozenset((Xnode[p], Xnode[q])))
                        for p in range(len(Yt)):
                            for q in range(p + 1, len(Yt)):
                                if (p, q) not in Ye: forb.add(frozenset((Ynode[p], Ynode[q])))
                        if any(frozenset(e) in forb for e in edges): continue
                        have = set(map(frozenset, edges))
                        free = [(Aid[a], Bid[b]) for a in range(len(A)) for b in range(len(B))
                                if Aid[a] != Bid[b]
                                and frozenset((Aid[a], Bid[b])) not in forb
                                and frozenset((Aid[a], Bid[b])) not in have]
                        for bits in range(1 << len(free)):
                            ee = list(edges)
                            for idx, fe in enumerate(free):
                                if (bits >> idx) & 1: ee.append(fe)
                            ee = [tuple(sorted(x)) for x in ee]
                            if len(set(ee)) != len(ee): continue
                            tot += 1
                            s = Sample("2leak", nxt, ee, mode="frame")
                            if not s.admit(verbose=False): continue
                            if (s.a(v) >= 3 and s.a(vp) >= 3
                                    and s.d(v) == len(Xt) + 1 and s.d(vp) == len(Yt) + 1):
                                surv.append(sorted(set(ee)))
    return tot, surv

def part34():
    print("\n=== PART 3/4 -- (Z3),(Z4): WHERE TWO LEAKS MAY SIT ===")
    print("  a(v) is monotone under adding vertices, so a >= 3 read off the frame")
    print("  certifies a = 3 in the host (G58 caps it); and the frame Z+N[v]+N[v'] of a")
    print("  host carrying two leaks is IN HYPOTHESIS, so refuting every such frame")
    print("  refutes the host.  Population printed before every verdict.")
    tot0, sur0 = two_leak_frames(0, 0)
    print("      SAME hexagon vertex z_0: %d frames enumerated, %d survive" % (tot0, len(sur0)))
    check("(Z3) TWO leaks at the SAME hexagon vertex are REFUTED (so <= 1 leak per z_i)",
          len(sur0) == 0, "%d/%d survive" % (len(sur0), tot0))
    tick("part3")
    row = {}
    for j in range(1, 6):
        t, s = two_leak_frames(0, j)
        row[j] = (t, s)
        print("      z_0 & z_%d : %d frames enumerated, %d survive%s"
              % (j, t, len(s), ("   e.g. " + repr(s[0])) if s else ""))
        tick("part4-%d" % j)
    check("(Z4) two leaks at hexagon distance 1 are REFUTED (both sides)",
          len(row[1][1]) == 0 and len(row[5][1]) == 0)
    check("(Z4) two leaks at hexagon distance 2 are REFUTED (both sides)",
          len(row[2][1]) == 0 and len(row[4][1]) == 0)
    check("liveness: two leaks at ANTIPODAL hexagon vertices ARE in hypothesis -- so (Z4) "
          "is a restriction, not a vacuity", len(row[3][1]) > 0)
    check("(Z4)+(Z3) => n3 <= 2, and n3 = 2 forces the two leaks ANTIPODAL",
          len(sur0) == 0 and all(len(row[j][1]) == 0 for j in (1, 2, 4, 5)))
    return row


# ============================================================================
# PART 5 -- (Z5): a leak coexists with at most ONE occupied antipodal slot
# ============================================================================
def part5():
    print("\n=== PART 5 -- (Z5): A LEAK AND THE ANTIPODAL SLOTS ===")
    print("  Frame = Z + N[v] + the W_anti vertices themselves (their own neighbourhoods")
    print("  are NOT needed: refutation on a subframe refutes every host containing it).")
    print("  The w-to-N[v] bits AND the w-to-w' bit are enumerated, not assumed.")
    single = {}
    for j in range(6):
        tot = surv = 0
        for cfg in leak_configs(j):
            Xt, Xe = cfg
            v = 6; X = [7 + t for t in range(len(Xt))]; w = 7 + len(Xt)
            base = list(HEX) + [(v, j)]
            for u, z in zip(X, Xt): base += [(u, v), (u, z)]
            for (p, q) in Xe: base.append((X[p], X[q]))
            cands = [v] + X
            for bits in range(1 << len(cands)):
                edges = list(base) + [(w, 0), (w, 3)]
                for idx, c in enumerate(cands):
                    if (bits >> idx) & 1: edges.append((w, c))
                tot += 1
                s = Sample("leak+1anti", w + 1, edges, mode="frame")
                if s.admit(verbose=False) and s.a(v) >= 3 and s.d(v) == len(Xt) + 1: surv += 1
        single[j] = (tot, surv)
        print("      leak at z_%d  +  ONE W_anti at slot (z_0,z_3): %d frames, %d survive"
              % (j, tot, surv))
    check("liveness: a leak and ONE occupied slot DO coexist -- (Z5) is a restriction, "
          "not a vacuity", all(single[j][1] > 0 for j in range(6)))
    tick("part5a")
    pairs = {}
    for pair in [((0,3),(1,4)), ((0,3),(2,5)), ((1,4),(2,5))]:
        tot = surv = 0
        for cfg in leak_configs(0):
            Xt, Xe = cfg
            v = 6; X = [7 + t for t in range(len(Xt))]; ws = [7 + len(Xt), 8 + len(Xt)]
            base = list(HEX) + [(v, 0)]
            for u, z in zip(X, Xt): base += [(u, v), (u, z)]
            for (p, q) in Xe: base.append((X[p], X[q]))
            cands = [v] + X
            for bits in range(1 << (2 * len(cands) + 1)):
                edges = list(base)
                for t, (zi, zj) in enumerate(pair): edges += [(ws[t], zi), (ws[t], zj)]
                b = 0
                for t in range(2):
                    for c in cands:
                        if (bits >> b) & 1: edges.append((ws[t], c))
                        b += 1
                if (bits >> b) & 1: edges.append((ws[0], ws[1]))
                tot += 1
                s = Sample("leak+2anti", 9 + len(Xt), edges, mode="frame")
                if s.admit(verbose=False) and s.a(v) >= 3 and s.d(v) == len(Xt) + 1: surv += 1
        pairs[pair] = (tot, surv)
        print("      leak at z_0  +  TWO W_anti at slots %r: %d frames, %d survive"
              % (list(pair), tot, surv))
        tick("part5b")
    check("(Z5) a leak and TWO occupied antipodal slots are REFUTED, at ALL THREE slot "
          "pairs => n3 >= 1 implies m <= 1", all(p[1] == 0 for p in pairs.values()))
    return single, pairs


# ============================================================================
# PART 6 -- (Z6): the finite arithmetic, enumerated over every feasible (n3, m)
# ============================================================================
def part6():
    print("\n=== PART 6 -- (Z6) THE ARITHMETIC, over EVERY feasible (n3, m) ===")
    print("      constraints in force: n3 <= 2 (Z3+Z4); m <= 3 (34.4a); n3>=1 => m<=1 (Z5)")
    print("      %3s %3s %10s %10s" % ("n3", "m", "n3+2m", "bound on Sum(a-3)"))
    worst = -99; rows = 0
    for n3 in range(0, 3):
        for m in range(0, 4):
            if n3 >= 1 and m >= 2: continue
            rows += 1
            val = n3 + 2*m
            worst = max(worst, val - 6)
            print("      %3d %3d %10d %10d" % (n3, m, val, val - 6))
    print("      observed population: %d feasible (n3,m) pairs" % rows)
    check("(Z6) n3 + 2m <= 6 in EVERY feasible case, so Sum_v(a(v)-3) <= 0 -- (D3-C6)",
          worst <= 0, "worst bound %+d" % worst)
    # both extremal regimes exhibited as HOSTS
    for tag, n, E, want in [
        ("r24 attaining region n=10", 10, HEX + [(6,0),(6,3),(7,1),(7,4),(8,2),(8,5),
                                                 (9,6),(9,7),(9,8)], (0, 3)),
        ("2-LEAK region n=10", 10, HEX + [(6,0),(7,3),(6,7),(8,2),(8,6),(9,1),(9,7)], (2, 0))]:
        s = Sample(tag, n, E, mode="host")
        ok = s.admit(verbose=False)
        if not ok:
            check("extremal host %s admitted" % tag, False, "; ".join(s.why)); continue
        W1, Wc, Wa, W0 = classify(s)
        n3 = sum(1 for v in W1 if s.a(v) == 3); m = len(Wa)
        tot = s.sum_excess()
        print("      %-28s in hypothesis, n3=%d m=%d n3+2m=%d, Sum(a-3)=%d, bound %d"
              % (tag, n3, m, n3 + 2*m, tot, n3 + 2*m - 6))
        check("extremal regime (n3,m)=%r realised and (Z1) TIGHT on it" % (want,),
              (n3, m) == want and tot == n3 + 2*m - 6)
    tick("part6")


# ============================================================================
# PART 7 -- INDEPENDENT EXHAUSTIVE CONFIRMATION over a bounded window
# ============================================================================
def sweep(traces, maxk, tag):
    """Every in-hypothesis HOST of the form Z + k off-Z vertices with traces drawn from
    `traces`, generated by DFS pruned by C4-freeness and P7-freeness -- both INHERITED by
    induced subgraphs, so the pruning is sound.  Population printed by size."""
    pop = [0]*(maxk+1); hosts = [0]*(maxk+1)
    best = [-99, None]; bestn3 = [0, None]; badZ1 = [0]; badZ6 = [0]
    perS = [-99]*(maxk+1)
    def rec(adj, n, k):
        pop[k] += 1
        seen = 63; frontier = 63
        while frontier:
            nxt = 0; f = frontier
            while f:
                b = f & -f; f ^= b; nxt |= adj[b.bit_length()-1]
            nxt &= ~seen; seen |= nxt; frontier = nxt
        if seen == (1 << n) - 1:
            hosts[k] += 1
            S = sum(alpha_bm(adj, v) - 3 for v in range(n))
            n3 = 0; m = 0
            for v in range(6, n):
                tr = adj[v] & 63; c = bin(tr).count("1")
                if c == 1 and alpha_bm(adj, v) == 3: n3 += 1
                if c == 2 and (tr in (0b001001, 0b010010, 0b100100)): m += 1
            if S > n3 + 2*m - 6: badZ1[0] += 1
            if n3 + 2*m > 6: badZ6[0] += 1
            if S > best[0]: best[0] = S; best[1] = (list(adj[:n]), k)
            if n3 > bestn3[0]: bestn3[0] = n3; bestn3[1] = (list(adj[:n]), k)
            perS[k] = max(perS[k], S)
        if k == maxk: return
        tick("%s-k%d" % (tag, k))
        v = n
        for T in traces:
            for bits in range(1 << (n - 6)):
                a = list(adj) + [0]
                mask = 0
                for z in T: mask |= 1 << z
                for idx in range(n - 6):
                    if (bits >> idx) & 1: mask |= 1 << (6 + idx)
                a[v] = mask
                mm = mask
                while mm:
                    b = mm & -mm; mm ^= b; a[b.bit_length()-1] |= 1 << v
                if new_c4(a, v+1, v): continue
                if has_induced_pk(a, v+1, 7): continue
                rec(a, v+1, k+1)
    base = [0]*6
    for i in range(6): base[i] = (1 << ((i+1) % 6)) | (1 << ((i+5) % 6))
    rec(base, 6, 0)
    print("      %s: in-hypothesis regions by |off-Z| = 0..%d : %r" % (tag, maxk, pop))
    print("      %s: of which CONNECTED hosts                : %r" % (tag, hosts))
    print("      %s: max Sum(a-3) per size                   : %r" % (tag, perS))
    print("      %s: MAX Sum_v(a(v)-3) = %+d ; MAX n3 = %d"
          % (tag, best[0], bestn3[0]))
    return best, bestn3, badZ1[0], badZ6[0], sum(pop)

def part7():
    print("\n=== PART 7 -- INDEPENDENT EXHAUSTIVE CONFIRMATION over a bounded window ===")
    ALL16 = [()] + [(i,) for i in range(6)] + [(i, (i+1) % 6) for i in range(6)] \
            + [(i, i+3) for i in range(3)]
    best, bn3, b1, b6, tot = sweep(ALL16, 5, "ALL-TRACES k<=5")
    check("sweep A (every legal trace, |off-Z| <= 5, %d regions): MAX Sum(a-3) = 0, "
          "i.e. (D3-C6) holds with equality attained" % tot, best[0] == 0)
    check("sweep A: (Z1) Sum(a-3) <= n3+2m-6 on EVERY host, 0 violations", b1 == 0)
    check("sweep A: (Z6) n3 + 2m <= 6 on EVERY host, 0 violations", b6 == 0)
    check("sweep A: MAX n3 = 2, matching (Z3)+(Z4)", bn3[0] == 2)
    tick("part7a")
    SING = [(i,) for i in range(6)]
    best2, bn32, b12, b62, tot2 = sweep(SING, 6, "SINGLE-TRACE k<=6")
    check("sweep B (single traces only -- the class a leak's whole neighbourhood lives "
          "in -- |off-Z| <= 6, %d regions): MAX n3 = 2" % tot2, bn32[0] == 2)
    check("sweep B: (Z1) and (Z6) hold on EVERY host, 0 violations", b12 == 0 and b62 == 0)
    tick("part7b")


# ============================================================================
# PART 8 -- PROVENANCE.  RULING CG: these string probes are EVIDENCE, NOT CHECKS
# ============================================================================
def part8():
    print("\n=== PART 8 -- PROVENANCE against a PINNED corpus boundary (RULING BX) ===")
    print("  RULING CG: a probe whose blind spot is the ENCODING of the token it looks for")
    print("  cannot certify ABSENCE.  Everything printed below is EVIDENCE, not a CHECK.")
    print("  The load-bearing inputs are asserted as GRAPH facts in PARTS 1-7, not here.")
    lines = open(DRAFT, encoding="utf-8").read().split("\n")
    PIN = 4993          # HARD-PINNED: the draft's length immediately before §37 was appended
    print("      pinned corpus boundary: draft line %d (HARD-PINNED = the draft's length "
          "immediately before §37 was appended; recorded so the number is auditable)" % PIN)
    idx = [i for i, l in enumerate(lines) if l.startswith("# §37 ")]
    check("the pinned boundary is where it claims to be: no '# §37 ' heading at or before "
          "line %d, and one after it" % PIN,
          all(i > PIN for i in idx) and len(idx) <= 1,
          "§37 heading line(s) %r" % idx)
    corpus = "\n".join(lines[:PIN])
    import unicodedata, re
    def norm(s):
        s = unicodedata.normalize("NFKC", s).lower()
        for a, b in (("≤", "<="), ("≥", ">="), ("−", "-"), ("–", "-"),
                     ("—", "-"), ("‘", "'"), ("’", "'"), ("“", '"'),
                     ("”", '"'), (" ", " ")):
            s = s.replace(a, b)
        return re.sub(r"\s+", " ", s)
    ncorpus = norm(corpus)
    for tok in ["G59", "the W_1 leak", "n3 + 2m <= 6", "|W_anti| <= 3", "G58", "G55",
                "per-branch discharging bound", "leaking"]:
        raw = corpus.count(tok)
        nrm = ncorpus.count(norm(tok))
        print("      EVIDENCE  token %-32r raw=%-4d normalised(NFKC+casefold+unicode-math)=%d"
              % (tok, raw, nrm))
    print("      NOTE the two columns differ for '|W_anti| <= 3': that is exactly round 24's")
    print("      uncaught defect, now visible rather than silent.  It is still EVIDENCE.")
    print("\n  --- the MINT GATE, rebuilt so it cannot miss by ENCODING (RULING CG) ---")
    print("  A probe ASKS 'is G59 absent?' and answers 'yes' whenever it cannot read the")
    print("  token.  This instead ENUMERATES the whole address population and asserts it is")
    print("  CONTIGUOUS: an address written in an encoding the scanner misses would open a")
    print("  HOLE, and a hole is VISIBLE.  Absence is then a consequence of completeness,")
    print("  not a probe's silence.  This is the uniqueness claim RULING CG asked for.")
    nums = sorted(set(int(x) for x in re.findall(r"\bG(\d{1,3})\b", corpus)))
    holes = [i for i in range(0, max(nums)+1) if i not in nums]
    print("      observed G-address population: G%d..G%d, %d distinct, holes %r"
          % (min(nums), max(nums), len(nums), holes))
    check("mint gate (population form): the G-namespace is CONTIGUOUS G0..G%d, so the scan "
          "missed nothing" % max(nums), holes == [])
    occ = [(i+1, l.strip()[:96]) for i, l in enumerate(lines[:PIN]) if "G59" in l]
    print("      observed G59 occurrences before the boundary: %d" % len(occ))
    for ln, txt in occ: print("         line %d: %s" % (ln, txt))
    regd = [ln for ln, txt in occ if txt.startswith("#") or txt.startswith("**Lemma")]
    check("mint gate: EVERY G59 occurrence is PROSE ABOUT the next free address, none is a "
          "registration (0 in a heading or a Lemma line)", len(regd) == 0,
          "registration-shaped occurrences: %r" % regd)
    check("mint gate: G60 is unoccupied, so this round's own entry has a free address and "
          "does NOT need to self-promote to get one", 60 not in nums)
    tick("part8")


def main():
    print(__doc__)
    part0(); part1(); part2(); part34(); part5(); part6(); part7(); part8()
    print("\n=== SUMMARY ===")
    print("  checks run: %d, failures: %d %s" % (NCHECK, len(FAIL), FAIL if FAIL else ""))
    print("  wall clock: %.2f s (self-limit %.0f s)" % (time.time() - T0, LIMIT))
    sys.exit(1 if FAIL else 0)

if __name__ == "__main__":
    main()
