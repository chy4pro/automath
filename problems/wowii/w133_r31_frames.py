#!/usr/bin/env python3
"""
w133 round 31 -- ITEM 1: THE PRESCRIBED CONSISTENCY CHECK IS UNSATISFIABLE, AND WHY.

WHAT r30 FOUND AND WHAT THIS FILE MEASURES.
    The Q41 brief's "A GUARD THAT CANNOT MOVE" paragraph told the reviewer to check
    "that a table's `N frames` is the product of the free bits it describes".
    832 = 2^6 * 13, 858 = 2*3*11*13, 872 = 2^3*109.  A product of free bits is a power
    of two (each free bit contributes a factor 2), so those three tables CANNOT pass a
    check the same brief prescribes -- and the returned verdict was that failure.

    r30 diagnosed this by FACTORING the printed numbers.  Factoring says the check
    fails; it does not say WHY, and a wrong reason is worth nothing (OPS-15).  This
    file establishes the MECHANISM by re-deriving the populations from scratch:

    *** A frame table's population is NOT a product.  It is a SUM over BRANCHES,     ***
    ***     N = SUM_b ( 2^{f_b} - dup_b ),                                           ***
    *** where a branch is (shape of N[v], shape of N[v'], whether v ~ v', which      ***
    *** far neighbours are IDENTIFIED), f_b is that branch's free-bit count, and     ***
    *** dup_b counts assignments whose edge list degenerates.  Different branches    ***
    *** have DIFFERENT f_b, so no single free-bit set describes the table at all.    ***

    Two consequences that factoring alone cannot see, and both matter:
      (a) the check is not merely FAILED by 832/858/872, it is ILL-POSED for every
          multi-branch table -- there is no "the free bits it describes";
      (b) (Z5)'s 32 PASSES the prescribed check BY ACCIDENT: 32 = 2^5 looks like a
          five-bit product, but the enumeration is 2^3 + 2^3 + 2^4 over three branches
          and no branch has five free bits.  A check that a table passes for a false
          reason is worse than one it fails.

    THIRD FINDING, not part of the assignment and against this line's own draft:
      the draft and the DISPATCHED brief both printed "384 frames" for (Z5)'s two-slot
      tables.  Both machines print 768.  The draft is corrected; the shipped brief is
      NOT, because it is evidence of what a reviewer actually saw.  See PART 4.

THIS IS A SECOND IMPLEMENTATION.  Nothing is imported from w133_r22/r23/r25; every
primitive below (C4-freeness, induced C6, induced P7, a = alpha(G[N(v)])) is written
here and positive-controlled in PART 0 before it is used.  Agreement with r25 is then
a cross-check, not a tautology.

No SAT.  No search beyond the bounded frame enumerations already in the draft.
Wall-clock self-limit 600 s, exit(2) on overrun -- never a silent `return`.
"""
import itertools, os, sys, time

T0 = time.time()
LIMIT = 600.0
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

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRAFT = os.path.join(REPO, "notes", "proofs", "wowii133_draft.md")
BRIEF = os.path.join(os.path.dirname(REPO), "automath-sandbox", "briefs", "w133_r29_q41.md")
R25OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w133_r25_zterm.out")

HEX = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
Z6 = [0, 1, 2, 3, 4, 5]


# ============================================================================
# PART 0 -- OWN PRIMITIVES, POSITIVE-CONTROLLED BEFORE USE
# ============================================================================
def bm(n, edges):
    """bitmask adjacency; raises on a self-loop or a repeated edge (frames must be simple)"""
    adj = [0] * n
    seen = set()
    for u, v in edges:
        if u == v:
            raise ValueError("self loop")
        k = (min(u, v), max(u, v))
        if k in seen:
            raise ValueError("repeated edge")
        seen.add(k)
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj

def c4free(adj, n):
    """no two DISTINCT vertices have two or more common neighbours"""
    for i in range(n):
        for j in range(i + 1, n):
            if bin(adj[i] & adj[j]).count("1") >= 2:
                return False
    return True

def induced_c6(adj, Z):
    if len(set(Z)) != 6:
        return False
    for i in range(6):
        for j in range(i + 1, 6):
            want = (j - i) % 6 in (1, 5)
            if bool(adj[Z[i]] >> Z[j] & 1) != want:
                return False
    return True

def has_induced_pk(adj, n, k):
    """is there an induced path on exactly k vertices?"""
    def ext(last, mask, length):
        if length == k:
            return True
        c = adj[last] & ~mask
        while c:
            b = c & -c
            c ^= b
            u = b.bit_length() - 1
            # u must see ONLY `last` inside the current path
            if adj[u] & mask & ~(1 << last):
                continue
            if ext(u, mask | b, length + 1):
                return True
        return False
    for s in range(n):
        if ext(s, 1 << s, 1):
            return True
    return False

def alpha_nbhd(adj, v):
    """independence number of G[N(v)]"""
    N = []
    m = adj[v]
    while m:
        b = m & -m
        m ^= b
        N.append(b.bit_length() - 1)
    best = 0
    for r in range(len(N), best, -1):
        if r <= best:
            break
        for S in itertools.combinations(N, r):
            if all(not (adj[x] >> y & 1) for x, y in itertools.combinations(S, 2)):
                best = r
                break
        if best >= r:
            break
    return best

def deg(adj, v):
    return bin(adj[v]).count("1")

def admit_frame(n, edges):
    """a FRAME is an induced subgraph of a host, so only INHERITED clauses are asserted:
    simple, C4-free, Z an induced C6, no induced P7.  Connectedness is NOT inherited."""
    try:
        adj = bm(n, edges)
    except ValueError:
        return None
    if not c4free(adj, n):
        return None
    if not induced_c6(adj, Z6):
        return None
    if has_induced_pk(adj, n, 7):
        return None
    return adj


def part0():
    print("\n=== PART 0 -- POSITIVE CONTROLS ON THIS FILE'S OWN PRIMITIVES ===")
    print("  Every predicate below ships with an input on which it MUST return True.")
    PET = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),
           (0,5),(1,6),(2,7),(3,8),(4,9)]
    pet = bm(10, PET)
    check("MUST-FIRE: Petersen is C4-free", c4free(pet, 10))
    check("MUST-FIRE: Petersen has an induced P5", has_induced_pk(pet, 10, 5))
    check("specificity: Petersen has NO induced P6 (so P_k is not a constant True)",
          not has_induced_pk(pet, 10, 6))
    check("MUST-FIRE: a(v) = 3 at every Petersen vertex",
          [alpha_nbhd(pet, v) for v in range(10)] == [3] * 10)
    c4 = bm(4, [(0,1),(1,2),(2,3),(3,0)])
    check("specificity: the 4-cycle IS detected as NOT C4-free", not c4free(c4, 4))
    hexa = bm(6, HEX)
    check("MUST-FIRE: the bare hexagon is an induced C6 on Z", induced_c6(hexa, Z6))
    bad = bm(6, HEX + [(0, 3)])
    check("specificity: a hexagon PLUS a chord is NOT an induced C6", not induced_c6(bad, Z6))
    check("specificity: the bare hexagon has no induced P7", not has_induced_pk(hexa, 6, 7))
    p7 = bm(7, [(i, i + 1) for i in range(6)])
    check("MUST-FIRE: the path on 7 vertices HAS an induced P7", has_induced_pk(p7, 7, 7))
    # a = d - t on C4-free graphs (G[N(v)] is a matching) -- an independent cross-check
    # of alpha_nbhd against a formula that does not enumerate subsets
    okdt = True
    for E, n in [(PET, 10), (HEX, 6), (HEX + [(6,0),(6,3),(7,6)], 8)]:
        ad = bm(n, E)
        for v in range(n):
            t = sum(1 for x, y in itertools.combinations(
                        [i for i in range(n) if ad[v] >> i & 1], 2) if ad[x] >> y & 1)
            if alpha_nbhd(ad, v) != deg(ad, v) - t:
                okdt = False
    check("cross-check: the subset-enumerating alpha AGREES with d - t on every C4-free "
          "control (two implementations of the same number)", okdt)
    check("MUST-FIRE: admit_frame ACCEPTS the bare hexagon", admit_frame(6, HEX) is not None)
    check("specificity: admit_frame REJECTS a repeated edge",
          admit_frame(6, HEX + [(0, 1)]) is None)
    check("specificity: admit_frame REJECTS a C4",
          admit_frame(7, HEX + [(6, 0), (6, 2)]) is None)
    tick("part0")


# ============================================================================
# PART 1 -- (Z3)/(Z4): THE BRANCH DECOMPOSITION OF THE TWO-LEAK FRAME TABLES
# ============================================================================
def leak_shapes(i):
    """(Z2)'s three a=3 shapes at anchor slot z_i: (far traces, internal edges).
    Taken as GIVEN here -- (Z2) is a separate enumeration, re-derived in r25 PART 2."""
    m = lambda d: (i + d) % 6
    return [((m(2), m(3)), ()),
            ((m(3), m(4)), ()),
            ((m(2), m(3), m(4)), ((0, 2),))]

def two_leak_branches(i, j):
    """Enumerate the frames Z + N[v] + N[v'] for a leak at z_i and a leak at z_j, and
    return one record PER BRANCH.  A branch is (X shape, Y shape, v~v'?, identification
    pattern).  Within a branch the only remaining freedom is the free bits between the
    two far-neighbour sets, so the branch's population is 2^f minus degenerate ones."""
    branches = []
    survivors = []
    for si, (Xt, Xe) in enumerate(leak_shapes(i)):
        for sj, (Yt, Ye) in enumerate(leak_shapes(j)):
            for adjvv in (False, True):
                # v ~ v' is possible only if each leak's far set contains the other's slot:
                # N(v) is EXACTLY {z_i} + far set, so v' adjacent to v forces v' in that set
                if adjvv and not (j in Xt and i in Yt):
                    continue
                A = [t for t in Xt if not (adjvv and t == j)]
                B = [t for t in Yt if not (adjvv and t == i)]
                common = [(a, b) for a in range(len(A)) for b in range(len(B)) if A[a] == B[b]]
                for r in range(len(common) + 1):
                    for match in itertools.combinations(common, r):
                        if len(set(x[0] for x in match)) != r:
                            continue
                        if len(set(x[1] for x in match)) != r:
                            continue
                        v, vp = 6, 7
                        Aid = {a: 8 + a for a in range(len(A))}
                        Bid = {}
                        nxt = 8 + len(A)
                        for (a, b) in match:
                            Bid[b] = Aid[a]
                        for b in range(len(B)):
                            if b not in Bid:
                                Bid[b] = nxt
                                nxt += 1
                        base = list(HEX) + [(v, i), (vp, j)]
                        if adjvv:
                            base.append((v, vp))
                        for a in range(len(A)):
                            base += [(Aid[a], v), (Aid[a], A[a])]
                        for b in range(len(B)):
                            base += [(Bid[b], vp), (Bid[b], B[b])]
                        Xn = [(vp if (adjvv and t == j) else Aid[A.index(t)]) for t in Xt]
                        Yn = [(v if (adjvv and t == i) else Bid[B.index(t)]) for t in Yt]
                        for (p, q) in Xe:
                            base.append((Xn[p], Xn[q]))
                        for (p, q) in Ye:
                            base.append((Yn[p], Yn[q]))
                        # the shapes also PROHIBIT the non-edges inside each neighbourhood
                        forb = set()
                        for p in range(len(Xt)):
                            for q in range(p + 1, len(Xt)):
                                if (p, q) not in Xe:
                                    forb.add(frozenset((Xn[p], Xn[q])))
                        for p in range(len(Yt)):
                            for q in range(p + 1, len(Yt)):
                                if (p, q) not in Ye:
                                    forb.add(frozenset((Yn[p], Yn[q])))
                        if any(frozenset(e) in forb for e in base):
                            continue          # the identification contradicts a shape
                        have = set(map(frozenset, base))
                        free = [(Aid[a], Bid[b])
                                for a in range(len(A)) for b in range(len(B))
                                if Aid[a] != Bid[b]
                                and frozenset((Aid[a], Bid[b])) not in forb
                                and frozenset((Aid[a], Bid[b])) not in have]
                        cnt = dup = 0
                        for bits in range(1 << len(free)):
                            ee = list(base)
                            for idx, fe in enumerate(free):
                                if (bits >> idx) & 1:
                                    ee.append(fe)
                            ee = [tuple(sorted(x)) for x in ee]
                            if len(set(ee)) != len(ee):
                                dup += 1
                                continue
                            cnt += 1
                            adj = admit_frame(nxt, ee)
                            if adj is None:
                                continue
                            if (alpha_nbhd(adj, v) >= 3 and alpha_nbhd(adj, vp) >= 3
                                    and deg(adj, v) == len(Xt) + 1
                                    and deg(adj, vp) == len(Yt) + 1):
                                survivors.append(sorted(set(ee)))
                        branches.append({"X": si, "Y": sj, "vv": adjvv, "id": r,
                                         "f": len(free), "pop": cnt, "dup": dup})
    return branches, survivors


def part1():
    print("\n=== PART 1 -- (Z3)/(Z4): WHAT A FRAME TABLE'S POPULATION ACTUALLY IS ===")
    print("  Re-derived here by a SECOND implementation, then compared to the draft.")
    print("  A branch = (X shape, Y shape, v~v'?, identification pattern).")
    print("  %-26s %8s %8s %10s %-28s" % ("table", "TOTAL", "survive", "branches", "free-bit counts f_b"))
    tables = {}
    for j, label in [(0, "same hexagon vertex z_0"), (1, "z_0 & z_1"), (2, "z_0 & z_2"),
                     (3, "z_0 & z_3 (antipodal)"), (4, "z_0 & z_4"), (5, "z_0 & z_5")]:
        br, sur = two_leak_branches(0, j)
        tot = sum(b["pop"] for b in br)
        fs = sorted(set(b["f"] for b in br))
        hist = {f: sum(1 for b in br if b["f"] == f) for f in fs}
        tables[j] = (tot, len(sur), br)
        print("  %-26s %8d %8d %10d %-28s"
              % (label, tot, len(sur), len(br),
                 " ".join("2^%d x%d" % (f, hist[f]) for f in fs)))
        tick("part1-%d" % j)
    print()
    print("  MECHANISM, printed in full for ONE table (z_0 & z_3, the live one):")
    print("      %-3s %-3s %-6s %-4s %-4s %-7s %-5s" % ("X", "Y", "v~v'", "ids", "f", "2^f", "dups"))
    for b in tables[3][2]:
        print("      %-3d %-3d %-6s %-4d %-4d %-7d %-5d"
              % (b["X"], b["Y"], b["vv"], b["id"], b["f"], 1 << b["f"], b["dup"]))
    tot3 = sum(b["pop"] for b in tables[3][2])
    print("      SUM over branches of (2^f - dups) = %d" % tot3)

    obs = [tables[j][0] for j in range(6)]
    draft = [832, 832, 858, 872, 858, 832]
    check("SECOND IMPLEMENTATION reproduces the draft's (Z3)/(Z4) populations "
          "832/832/858/872/858/832", obs == draft, "observed %r" % obs)
    sur = [tables[j][1] for j in range(6)]
    check("SECOND IMPLEMENTATION reproduces the draft's survivor counts 0/0/0/2/0/0 "
          "(so (Z3) and (Z4) themselves stand)", sur == [0, 0, 0, 2, 0, 0],
          "observed %r" % sur)
    multi = all(len(set(b["f"] for b in tables[j][2])) > 1 for j in range(6))
    check("MECHANISM: every (Z3)/(Z4) table spans SEVERAL DISTINCT free-bit counts, so "
          "there is no single 'the free bits it describes' to take a product of", multi)
    tick("part1")
    return tables


# ============================================================================
# PART 2 -- (Z5): the one-slot and two-slot tables, same treatment
# ============================================================================
def z5_branches(leak_slot, slots):
    """Frame = Z + N[v] + the W_anti vertices themselves.  Free bits: each w to each of
    N[v] = {v} + far set, plus (for two slots) the w-to-w' bit."""
    branches = []
    surv = 0
    for si, (Xt, Xe) in enumerate(leak_shapes(leak_slot)):
        v = 6
        X = [7 + t for t in range(len(Xt))]
        ws = [7 + len(Xt) + t for t in range(len(slots))]
        n = 7 + len(Xt) + len(slots)
        base = list(HEX) + [(v, leak_slot)]
        for u, z in zip(X, Xt):
            base += [(u, v), (u, z)]
        for (p, q) in Xe:
            base.append((X[p], X[q]))
        for t, (zi, zj) in enumerate(slots):
            base += [(ws[t], zi), (ws[t], zj)]
        cands = [v] + X
        nfree = len(slots) * len(cands) + (1 if len(slots) == 2 else 0)
        cnt = 0
        for bits in range(1 << nfree):
            ee = list(base)
            b = 0
            for t in range(len(slots)):
                for c in cands:
                    if (bits >> b) & 1:
                        ee.append((ws[t], c))
                    b += 1
            if len(slots) == 2 and (bits >> b) & 1:
                ee.append((ws[0], ws[1]))
            cnt += 1
            adj = admit_frame(n, ee)
            if adj is None:
                continue
            if alpha_nbhd(adj, v) >= 3 and deg(adj, v) == len(Xt) + 1:
                surv += 1
        branches.append({"X": si, "f": nfree, "pop": cnt})
    return branches, surv


def part2():
    print("\n=== PART 2 -- (Z5): the SAME structure, and 32 passes the check BY ACCIDENT ===")
    single = []
    for j in range(6):
        br, s = z5_branches(j, [(0, 3)])
        single.append((sum(b["pop"] for b in br), s, [b["f"] for b in br]))
        print("      leak at z_%d + ONE slot (z_0,z_3): %4d frames = %-22s  %d survive"
              % (j, single[-1][0], " + ".join("2^%d" % f for f in single[-1][2]), s))
        tick("part2a-%d" % j)
    check("SECOND IMPLEMENTATION reproduces (Z5)'s one-slot population 32 at all six "
          "leak positions", [x[0] for x in single] == [32] * 6,
          "observed %r" % [x[0] for x in single])
    check("SECOND IMPLEMENTATION reproduces the one-slot survivors 2,1,1,2,1,1 "
          "(so (Z5)'s liveness claim stands)", [x[1] for x in single] == [2, 1, 1, 2, 1, 1],
          "observed %r" % [x[1] for x in single])
    check("*** THE ACCIDENT: 32 is 2^3 + 2^3 + 2^4 over three branches, NOT 2^5 -- no "
          "branch has five free bits, so the prescribed product check PASSES this table "
          "for a reason that is false", single[0][2] == [3, 3, 4] and 8 + 8 + 16 == 32,
          "branch free-bit counts %r" % (single[0][2],))

    pairs = []
    for pr in [((0, 3), (1, 4)), ((0, 3), (2, 5)), ((1, 4), (2, 5))]:
        br, s = z5_branches(0, list(pr))
        pairs.append((sum(b["pop"] for b in br), s, [b["f"] for b in br]))
        print("      leak at z_0 + TWO slots %-18r: %4d frames = %-22s  %d survive"
              % (list(pr), pairs[-1][0], " + ".join("2^%d" % f for f in pairs[-1][2]), s))
        tick("part2b")
    check("(Z5)'s two-slot tables refute EVERY frame at all three slot pairs "
          "(so n_3 >= 1 => m <= 1 stands)", all(p[1] == 0 for p in pairs),
          "survivors %r" % [p[1] for p in pairs])
    tick("part2")
    return single, pairs


# ============================================================================
# PART 3 -- THE PRESCRIBED CHECK, DECIDED
# ============================================================================
def part3(tables, single, pairs):
    print("\n=== PART 3 -- THE PRESCRIBED CHECK, STATED FORMALLY AND DECIDED ===")
    print("  PRESCRIBED: \"a table's `N frames` is the product of the free bits it describes\".")
    print("  A free bit is a binary choice, so a product of free bits is a POWER OF TWO,")
    print("  and the check is  N = 2^f  for the f free bits of THE enumeration.")
    print("  %-26s %8s %-16s %-10s %s" % ("table", "N", "factorisation", "2-power?", "verdict"))
    rows = [("(Z3) z_0 & z_0", tables[0][0], tables[0][2]),
            ("(Z4) z_0 & z_1", tables[1][0], tables[1][2]),
            ("(Z4) z_0 & z_2", tables[2][0], tables[2][2]),
            ("(Z4) z_0 & z_3", tables[3][0], tables[3][2]),
            ("(Z4) z_0 & z_4", tables[4][0], tables[4][2]),
            ("(Z4) z_0 & z_5", tables[5][0], tables[5][2]),
            ("(Z5) one slot", single[0][0], [{"f": f} for f in single[0][2]]),
            ("(Z5) two slots", pairs[0][0], [{"f": f} for f in pairs[0][2]])]
    def fact(n):
        out, d, m = [], 2, n
        while d * d <= m:
            while m % d == 0:
                out.append(d)
                m //= d
            d += 1
        if m > 1:
            out.append(m)
        return out
    nfail = naccident = 0
    for label, N, br in rows:
        f = fact(N)
        ispow = set(f) <= {2}
        fs = sorted(set(b["f"] for b in br))
        exact = [x for x in fs if (1 << x) == N]
        if not ispow:
            verdict = "CANNOT PASS (odd prime factor %d)" % max(f)
            nfail += 1
        elif exact:
            verdict = "passes, and 2^%d IS a real branch" % exact[0]
        else:
            verdict = "PASSES BY ACCIDENT (no branch has %d free bits)" % (N.bit_length() - 1)
            naccident += 1
        print("  %-26s %8d %-16s %-10s %s"
              % (label, N, "*".join(map(str, f)), "yes" if ispow else "NO", verdict))
    # OWN DEFECT, LEFT VISIBLE: the first version of this line asserted `nfail == 6`.
    # I hand-counted the six (Z3)/(Z4) rows and forgot that (Z5)'s two-slot table is
    # 768 = 2^8 * 3, which also carries an odd prime factor.  The machine said 7 and the
    # hand-written expectation was the error -- for the NINTH consecutive round.
    check("the prescribed check CANNOT be passed by SEVEN of the eight tables, because "
          "their populations carry odd prime factors and a free-bit product cannot",
          nfail == 7, "%d tables cannot pass" % nfail)
    check("and of the two tables that CAN pass, at least one passes for a FALSE reason "
          "(no branch has that many free bits)", naccident >= 1,
          "%d accidental passes" % naccident)
    print()
    print("  SO: the check is not 'failed', it is ILL-POSED.  There is no 'the free bits")
    print("  it describes' -- each table is a SUM over branches with DIFFERENT free-bit")
    print("  counts.  The satisfiable form of the check is")
    print("        N  =  SUM over branches of ( 2^{f_b} - degenerate )")
    print("  which needs the branch list, and the branch list is not in the brief.")
    tick("part3")


# ============================================================================
# PART 4 -- AN ERROR IN THE DRAFT AND THE BRIEF, FOUND ON THE WAY
# ============================================================================
def part4(pairs):
    print("\n=== PART 4 -- (Z5) TWO-SLOT POPULATION: THE DRAFT AND THE BRIEF SAY 384 ===")
    obs = pairs[0][0]
    print("      this file (second implementation): %d" % obs)
    machine = None
    if os.path.exists(R25OUT):
        for line in open(R25OUT, encoding="utf-8"):
            if "TWO W_anti at slots" in line:
                machine = int(line.split(":")[1].split("frames")[0].strip())
                break
    print("      r25's own printed .out             : %s" % machine)
    def hits(path, tok):
        if not os.path.exists(path):
            return None
        return sum(1 for ln in open(path, encoding="utf-8")
                   if tok in ln and "occupied slots" in ln)
    d384, d768 = hits(DRAFT, "384"), hits(DRAFT, "768")
    b384 = hits(BRIEF, "384")
    print("      draft line saying '384 frames'     : %s occurrence(s)" % d384)
    print("      draft line saying '768 frames'     : %s occurrence(s)" % d768)
    print("      DISPATCHED brief, '384 frames'     : %s occurrence(s)" % b384)
    check("the two implementations AGREE on the (Z5) two-slot population", obs == machine,
          "second impl %r vs r25 .out %r" % (obs, machine))
    # This started as "assert the defect is PRESENT".  Once the draft was corrected that
    # form went FALSE -- an instrument that fails when its finding is fixed.  It is now a
    # REGRESSION check with both halves: the draft must be REPAIRED, and the DISPATCHED
    # bytes must still carry 384, because they are evidence and must never be rewritten.
    check("*** THE DEFECT, and its repair: the draft now says 768 and no longer says 384 "
          "(a hand-transcribed population that was wrong by a factor of two)",
          obs == 768 and d768 == 1 and d384 == 0,
          "obs=%r draft768=%r draft384=%r" % (obs, d768, d384))
    check("and the DISPATCHED brief still says 384 -- the shipped bytes are evidence and "
          "were NOT rewritten to hide what the reviewer actually saw", b384 == 1,
          "brief384=%r" % b384)
    print("      NOTE what this does and does NOT touch: the two-slot tables have 0")
    print("      survivors either way, so (Z5)'s CONCLUSION (n_3 >= 1 => m <= 1) is")
    print("      unaffected.  What is wrong is a printed population -- i.e. exactly the")
    print("      number the brief invited the reviewer to check, in the one table where")
    print("      the reviewer said it was not reconstructible.")
    tick("part4")
    return obs, machine, d384, b384


def main():
    print(__doc__)
    part0()
    tables = part1()
    single, pairs = part2()
    part3(tables, single, pairs)
    part4(pairs)
    print("\n=== SUMMARY ===")
    print("  checks run: %d, failures: %d %s" % (NCHECK, len(FAIL), FAIL if FAIL else ""))
    print("  wall clock: %.2f s (self-limit %.0f s)" % (time.time() - T0, LIMIT))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
