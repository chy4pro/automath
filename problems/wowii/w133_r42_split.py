#!/usr/bin/env python3
"""WOWII-133 round 42 -- E44's CLASS SPLITS IN TWO, AND THE FAMILY THAT COULD TEST HALF OF IT
DID NOT EXIST UNTIL THIS FILE.

Round 41 refuted (RXM-PERI) and proved the two forced-pass lemmas (PER-A)/(PER-B) and the
regime split (PER-C).  Brief E44 ("build draft 42.4's residual row inside route A2's class --
C4-free, mu >= 2, ecc(w) = rad+1, w maximally far from every centre, rad >= 5, l > 4 -- or
prove the class empty") was written from round 39 and is now STALE: it predates every one of
those lemmas.  This round settles what E44 should have asked.

  * PART 1 proves that at rad >= 2 the class E44 asks for splits into exactly TWO disjoint
    sub-classes, and names them:
        CASE A  diam = rad+1  -- and there condition 2 is FREE, implied by condition 3;
        CASE B  diam >= rad+2 -- and there the instance IS a counterexample to (RXM-PERI)
                                 restricted to l > 4 and rad >= 5, i.e. round 41's own
                                 surviving open question.
  * PART 2 then asks the question that decides whether round 39's control was worth what it
    was taken for: how many hosts of the 417-host family are CASE A hosts at all, and how
    many of the l>4 AND rad>=5 hosts are?  A control that contains no CASE A host cannot
    have tested CASE A.
  * PART 3 re-derives, from round 36's own base family, the two rad = 4 instances E44 quotes,
    and reports which CASE each of them is -- a datum E44 carries without knowing.
  * PART 4 builds a host family this line has never had: a NECKLACE of projective-plane
    blocks, C4-free BY CONSTRUCTION, with l > 4 and rad >= 5 and (unlike every previous
    in-class host) a chance of diam = rad+1.  Then it looks for E44's object on it.

Self-contained: primitives COPIED from round 41's file, never imported.
Interpreter: system python3 (pure stdlib).  No SAT.  No exhaustive graph enumeration --
every search here is a designed construction or a seeded-random sample.

PARTS
  0  primitive self-tests + the guard on THIS round's predicate
  1  (SPLIT): the two-case decomposition of E44's class, proved and asserted on live data
  2  the 417-host family, re-measured for CASE A hosts
  3  round 36's base family: the two rad = 4 instances, and which CASE they are
  4  the NECKLACE family: built, certified in-class, and searched for E44's object
"""
import sys
import time
from collections import deque
from itertools import combinations

T0 = time.time()
DEADLINE = 1500.0
CHECKS = 0
FAILS = 0
PARTS_RUN = []


def over():
    return (time.time() - T0) > DEADLINE


def ck(cond, msg):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL: " + msg, flush=True)


# ---------------------------------------------------------------- primitives (COPIED r41)


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
    """this line's sense: NO two vertices have two common neighbours."""
    n = len(g)
    for u, v in combinations(range(n), 2):
        if len(g[u] & g[v]) >= 2:
            return False
    return True


def a_val(g, v):
    """a(v) = alpha(G[N(v)]) by BRUTE independent-set search (correct off the class too)."""
    nb = sorted(g[v])
    best = 0
    for k in range(len(nb), 0, -1):
        if k <= best:
            break
        for S in combinations(nb, k):
            if all(y not in g[x] for x, y in combinations(S, 2)):
                best = k
                break
        if best == k:
            break
    return best


def a_val_matching(g, v):
    nb = sorted(g[v])
    t = sum(1 for x, y in combinations(nb, 2) if y in g[x])
    return len(nb) - t


def profile(g):
    n = len(g)
    D = [bfs(g, v) for v in range(n)]
    ecc = [max(D[v]) for v in range(n)]
    r = min(ecc)
    return D, ecc, r


def centre_of(ecc, r):
    return [v for v in range(len(ecc)) if ecc[v] == r]


def maximally_far(D, ecc, r, w):
    """(RAD-1P)'s condition 3, draft 42.4: d(c,w) == rad for EVERY centre c."""
    C = centre_of(ecc, r)
    return all(D[c][w] == r for c in C)


def l_of(g):
    n = len(g)
    return sum(a_val_matching(g, v) for v in range(n)) / float(n)


def cycle(n):
    return adj(n, [(i, (i + 1) % n) for i in range(n)])


def pathgraph(n):
    return adj(n, [(i, i + 1) for i in range(n - 1)])


def petersen():
    E = [(i, (i + 1) % 5) for i in range(5)]
    E += [(i, i + 5) for i in range(5)]
    E += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return adj(10, E)


def pg2(q):
    def norm(v):
        for i in range(3):
            if v[i] % q:
                inv = pow(v[i], q - 2, q)
                return tuple((c * inv) % q for c in v)
    pts = sorted({norm((a, b, c)) for a in range(q) for b in range(q) for c in range(q)
                  if (a, b, c) != (0, 0, 0)})
    idx = {p: i for i, p in enumerate(pts)}
    m = len(pts)
    E = []
    for j, L in enumerate(pts):
        for p in pts:
            if sum(p[t] * L[t] for t in range(3)) % q == 0:
                E.append((idx[p], m + j))
    return adj(2 * m, E)


def rand_c4free_dense(seed, n):
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
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(k - 1):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, at))
    return adj(n, E)


def path_then_cycle(g, at, L, k):
    E = edges_of(g)
    n = len(g)
    prev = at
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    tip = prev
    p = tip
    for _ in range(k - 1):
        E.append((p, n))
        p = n
        n += 1
    E.append((p, tip))
    return adj(n, E)


def blob_chain(q, L):
    b = pg2(q)
    bn = len(b)
    E = edges_of(b) + [(u + bn, v + bn) for (u, v) in edges_of(b)]
    n = 2 * bn
    prev = 1
    for _ in range(L):
        E.append((prev, n))
        prev = n
        n += 1
    E.append((prev, bn + 0))
    return adj(n, E)


def build_family():
    """round 33's family, rebuilt here (COPIED, not imported).  Designed + seeded-random,
    NOT exhaustive."""
    fam = []
    b3, b5 = pg2(3), pg2(5)
    fam.append((b3, "PG(2,3)"))
    fam.append((b5, "PG(2,5)"))
    for k in (5, 7, 9, 11, 13, 15, 17, 19, 21, 25):
        fam.append((glue_cycle(b5, 0, k), "PG(2,5)+C%d glued" % k))
        fam.append((glue_cycle(b3, 0, k), "PG(2,3)+C%d glued" % k))
    for L, k in ((1, 5), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 9), (5, 9), (6, 11)):
        fam.append((path_then_cycle(b5, 0, L, k), "PG(2,5)+P%d+C%d" % (L, k)))
    for k1, k2 in ((7, 7), (9, 9), (11, 11), (13, 13), (9, 11)):
        g = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g, 1, k2), "PG(2,5)+C%d@0+C%d@1" % (k1, k2)))
        g2 = glue_cycle(b5, 0, k1)
        fam.append((glue_cycle(g2, 5, k2), "PG(2,5)+C%d@0+C%d@5" % (k1, k2)))
    for L in (3, 5, 7, 9, 11):
        fam.append((blob_chain(5, L), "2xPG(2,5)+P%d" % L))
        fam.append((blob_chain(3, L), "2xPG(2,3)+P%d" % L))
    for n0 in (14, 18, 22, 26, 30, 34, 38, 44, 50):
        for s in range(1, 26):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                fam.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    for n0 in (26, 30, 34, 38, 44, 50):
        for s in (1, 2, 3, 4, 5, 6, 7, 8):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is None:
                continue
            for k in (5, 7, 9):
                fam.append((glue_cycle(h, 0, k), "dense(s=%d,n0=%d)+C%d" % (s, n0, k)))
    return fam


# ------------------------------------------------------- round 36's base family (COPIED)


def theta333():
    E = []
    nxt = 2
    for _ in range(3):
        a, b = nxt, nxt + 1
        nxt += 2
        E += [(0, a), (a, b), (b, 1)]
    return adj(nxt, E)


def two_c9():
    E = [(i, (i + 1) % 9) for i in range(9)]
    E += [(9 + i, 9 + (i + 1) % 9) for i in range(9)]
    E += [(0, 9)]
    return adj(18, E)


R36_BASES = [("C6", cycle(6)), ("C9", cycle(9)), ("Petersen", petersen()),
             ("Theta333", theta333()), ("P5", pathgraph(5)), ("2C9e", two_c9())]


def build_hairs(base, roots, hs):
    E = edges_of(base)
    n = len(base)
    for r, h in zip(roots, hs):
        prev = r
        for _ in range(h):
            E.append((prev, n))
            prev = n
            n += 1
    return adj(n, E)


# ------------------------------------------------------------------ THE NECKLACE (NEW)


class LCG(object):
    def __init__(self, seed):
        self.s = seed % (1 << 31)

    def nxt(self, k):
        self.s = (self.s * 1103515245 + 12345) % (1 << 31)
        return self.s % k

    def shuffled(self, xs):
        xs = list(xs)
        for i in range(len(xs) - 1, 0, -1):
            j = self.nxt(i + 1)
            xs[i], xs[j] = xs[j], xs[i]
        return xs


def w41():
    """round 41's NAMED in-class witness that (RXM-PERI) is false: n=10, C4-free, mu=2,
    rad 2, diam 4, centre {1}, and w in {4,7,8} is condition-3 with ecc(w) = 3 < 4."""
    return adj(10, [(0, 1), (0, 6), (0, 9), (1, 2), (1, 5), (1, 9), (2, 3), (3, 8),
                    (4, 5), (4, 6), (4, 7), (5, 7), (7, 8), (8, 9)])


def w9():
    """round 41's hand-built GENERAL witness (not in this line's class: mu = 1)."""
    # c=0 a1=1 a2=2 a3=3 a4=4 s=5 t=6 w=7 q=8
    return adj(9, [(0, 1), (0, 2), (0, 3), (0, 4), (3, 1), (3, 2), (1, 5), (2, 6),
                   (7, 3), (7, 4), (8, 4)])


def r32_rand_c4free(seed, n, extra):
    """round 32's own generator, COPIED verbatim in behaviour: a cycle plus `extra`
    random C4-preserving chords, then peeled to mu >= 2."""
    st = seed

    def nxt(k):
        nonlocal st
        st = (st * 1103515245 + 12345) % (1 << 31)
        return st % k
    g = cycle(n)
    for _ in range(extra):
        u, v = nxt(n), nxt(n)
        if u == v or v in g[u]:
            continue
        if len(g[u] & g[v]) >= 1:
            continue
        g[u].add(v)
        g[v].add(u)
        if not c4_free(g):
            g[u].discard(v)
            g[v].discard(u)
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
    if len(h) < 6 or not connected(h):
        return None
    if min(a_val(h, v) for v in range(len(h))) < 2:
        return None
    return h


def necklace(qs, seed, src_frac=1.0, tgt_mode="any", fracs=None):
    """m blocks in a CYCLE, block i an incidence graph of PG(2,q_i).

    Cross-block edges: a partial injection from an INDEPENDENT set of block i (its POINTS)
    into block i+1.  Sources independent is exactly what makes the whole thing C4-free:
    a cross-block C4 needs two matched vertices v ~ x in block i whose images are adjacent
    in block i+1, and independent sources make `v ~ x` impossible.  (Verified by machine
    below -- the argument is not what certifies the object, the checker is.)
    """
    m = len(qs)
    blocks = [pg2(q) for q in qs]
    off = []
    tot = 0
    for b in blocks:
        off.append(tot)
        tot += len(b)
    E = []
    for i, b in enumerate(blocks):
        for (u, v) in edges_of(b):
            E.append((off[i] + u, off[i] + v))
    rng = LCG(seed)
    for i in range(m):
        j = (i + 1) % m
        npts = len(blocks[i]) // 2
        srcs = rng.shuffled(range(npts))
        f = src_frac if fracs is None else fracs[i % len(fracs)]
        k = max(1, int(round(npts * f)))
        k = min(k, len(blocks[j]))
        srcs = srcs[:k]
        if tgt_mode == "points":
            pool = list(range(len(blocks[j]) // 2))
        else:
            pool = list(range(len(blocks[j])))
        tgts = rng.shuffled(pool)[:k]
        for s, t in zip(srcs, tgts):
            E.append((off[i] + s, off[j] + t))
    return adj(tot, E)


# ------------------------------------------------------------------ PART 0


def part0():
    PARTS_RUN.append("PART0")
    print()
    print("=" * 78)
    print("PART 0 -- primitive self-tests and the guard on THIS round's predicate")
    print("=" * 78)
    P = petersen()
    _, eP, rP = profile(P)
    ck(rP == 2 and len(centre_of(eP, rP)) == len(P), "Petersen self-centred, rad 2")
    C9 = cycle(9)
    _, e9, r9 = profile(C9)
    ck(r9 == 4 and max(e9) == 4, "C9 rad = diam = 4")
    P5 = pathgraph(5)
    D5, e5, r5 = profile(P5)
    ck(r5 == 2 and max(e5) == 4, "P5 rad 2 diam 4")
    b3 = pg2(3)
    ck(len(b3) == 26 and connected(b3) and c4_free(b3), "PG(2,3): 26 vertices, C4-free")
    _, e3, r3 = profile(b3)
    ck(r3 == 3 and max(e3) == 3, "PG(2,3) self-centred at rad 3")
    b5 = pg2(5)
    ck(len(b5) == 62 and connected(b5) and c4_free(b5), "PG(2,5): 62 vertices, C4-free")
    agree = 0
    for v in range(0, len(b5), 7):
        ck(a_val(b5, v) == a_val_matching(b5, v), "a(.) brute == matching formula on PG(2,5)")
        agree += 1
    for v in range(len(b3)):
        ck(a_val(b3, v) == a_val_matching(b3, v), "a(.) brute == matching formula on PG(2,3)")
        agree += 1
    print("  a(.) brute vs matching formula agreed at %d vertices of PG(2,3)/PG(2,5)" % agree)

    print()
    print("  GUARD.  CLASS CLAIMED: any evaluator of E44's membership predicate")
    print("    E44(G,w) := C4-free AND mu>=2 AND ecc(w)=rad+1 AND (d(c,w)=rad for EVERY")
    print("    centre c) AND rad>=5 AND l>4")
    print("  that (i) reads the ECCENTRICITY conjunct off the DIAMETER instead of off w, or")
    print("  (ii) computes l as a mean DEGREE instead of a mean a(.).  Neither is r34's")
    print("  zero-step, r35's one-step, r36's late-block, r37's off-by-one/anchor-drift,")
    print("  r38's cost-evaluator, r39's centre-widen/quantifier-swap/stratum-offset,")
    print("  r40's sphere-shift, nor r41's table-trust/peri-as-noncentral.")
    print("  (D7) DIAM-FOR-ECC: tests diam == rad+1 in place of ecc(w) == rad+1.")
    print("  (D8) MEAN-DEG-FOR-L: computes l as mean deg(v) in place of mean a(v).")
    ghosts = []
    for n0 in (14, 18, 22, 26):
        for s in (1, 2, 3, 4, 5, 6):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                ghosts.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    ghosts.append((glue_cycle(pg2(3), 0, 7), "PG(2,3)+C7"))
    ghosts.append((path_then_cycle(pg2(5), 0, 3, 7), "PG(2,5)+P3+C7"))
    # the two hosts that make (D7) distinguishable AT ALL: on a diam = rad+1 host (PER-A)
    # makes (D7) and the correct test agree by a THEOREM, so the guard needs a host where
    # a condition-3 vertex is NOT peripheral -- i.e. round 41's own (RXM-PERI) witnesses.
    ghosts.append((w41(), "W41 (r41 in-class)"))
    ghosts.append((w9(), "W9 (r41 general)"))
    d7_fires = d7_extra = d7_missed = 0
    d8_gap = d8_same = 0
    correct_fires = 0
    hosts_carrying = 0
    for g, nm in ghosts:
        D, ecc, r = profile(g)
        diam = max(ecc)
        carry = 0
        for w in range(len(g)):
            good = (ecc[w] == r + 1) and maximally_far(D, ecc, r, w)
            bad7 = (diam == r + 1) and maximally_far(D, ecc, r, w)
            if good:
                correct_fires += 1
                carry += 1
            if bad7:
                d7_fires += 1
            if bad7 and not good:
                d7_extra += 1
            if good and not bad7:
                d7_missed += 1
        if carry:
            hosts_carrying += 1
        lg = l_of(g)
        ld = sum(len(g[v]) for v in range(len(g))) / float(len(g))
        if abs(lg - ld) > 1e-9:
            d8_gap += 1
        else:
            d8_same += 1
    print("  correct predicate (conjuncts 2+3) fires on %d vertices over %d guard hosts,"
          % (correct_fires, len(ghosts)))
    print("  %d of which CARRY it." % hosts_carrying)
    print("  (D7) DIAM-FOR-ECC : fires %d | fires where correct does NOT %d | misses a real "
          "one %d" % (d7_fires, d7_extra, d7_missed))
    print("  (D8) MEAN-DEG-FOR-L: disagrees with the correct l on %d of %d guard hosts "
          "(agrees on %d)" % (d8_gap, len(ghosts), d8_same))
    ck(correct_fires > 0, "guard hosts must CARRY the predicate or the guard is free")
    ck(d7_extra > 0 or d7_missed > 0, "(D7) must be distinguishable from the correct test")
    ck(d8_gap > 0, "(D8) must be distinguishable from the correct l on some guard host")
    print("  NOTE, PRINTED BECAUSE IT MATTERS FOR PART 4: on a TRIANGLE-FREE host a(v) = deg(v),")
    print("  so (D8) is INVISIBLE there.  Every necklace host of PART 4 is triangle-free, so")
    print("  the l column of PART 4 is NOT protected by (D8); it is protected by the brute")
    print("  a(.) cross-check run on those hosts directly.")


# ------------------------------------------------------------------ PART 1


def part1():
    PARTS_RUN.append("PART1")
    print()
    print("=" * 78)
    print("PART 1 -- (SPLIT): E44's class is the DISJOINT UNION of two named sub-classes")
    print("=" * 78)
    print("""
  Round 41 proved, and this file re-asserts below on live data:
    (PER-A)  diam = rad+1 and w not a centre  =>  ecc(w) = diam.
    (PER-B)  ecc(w) = 2*rad                   =>  ecc(w) = diam.
    (PER-C)  so a condition-3 vertex can fail to be peripheral ONLY at
             diam >= rad+2 AND ecc(w) < 2*rad.

  (SPLIT).  Let (G,w) satisfy E44's conditions 1-4, i.e. G is C4-free with mu >= 2,
  ecc(w) = rad+1, d(c,w) = rad for every centre c, and rad = r >= 2.  Then EXACTLY ONE of

    CASE A   diam(G) = r+1.  Here ecc(w) = rad+1 is IMPLIED by condition 3 and needs no
             separate search: condition 3 forces w out of the centre (d(w,w)=0 != r), and
             (PER-A) then gives ecc(w) = diam = r+1.  So on a CASE A host the whole of
             E44's question is "is there a vertex maximally far from every centre?".

    CASE B   diam(G) >= r+2.  Here ecc(w) = r+1 < diam, so w is condition-3 and NOT
             peripheral: (G,w) is a COUNTEREXAMPLE to (RXM-PERI), and it carries rad >= 5
             and l > 4, so it is a counterexample to exactly the restricted form round 41
             left open.

  Proof that the cases are exhaustive and disjoint: diam >= ecc(w) = r+1 always, so
  diam = r+1 or diam >= r+2, never both.  Proof that CASE B is what it is said to be:
  w satisfies (RXM-PERI)'s hypothesis (condition 3) and ecc(w) = r+1 < diam denies its
  conclusion.  Proof of CASE A's freeness: (PER-A) above.  QED.

  TWO CONSEQUENCES, both new with round 41 and neither available to brief E44:
   (C1) If the restricted (RXM-PERI) (l > 4 AND rad >= 5) is TRUE, CASE B is EMPTY, and
        E44's question collapses to CASE A alone.  The two open questions round 41 left
        are not independent: one is half of the other.
   (C2) A CASE B instance would refute the restricted (RXM-PERI) -- so any engine that
        builds one has answered two questions, and must be told so.

  NOTE ON rad >= 2, which is where the split needs it: at r >= 2, ecc(w) = r+1 < 2r is
  automatic, so (PER-B) can NEVER force a pass in E44's class.  Only (PER-A) can.  E44
  asks for rad >= 5, so this is free there.
""")
    # the split, asserted at r >= 2
    for r in range(2, 40):
        ck(r + 1 < 2 * r, "(PER-B) cannot fire in E44's class: r+1 < 2r for r >= 2")
    print("  asserted: r+1 < 2r for r = 2..39, so (PER-B) never forces a pass in E44's class.")

    # (PER-A) and the split asserted on live hosts
    hosts = []
    for n0 in (14, 18, 22, 26, 30):
        for s in (1, 2, 3, 4, 5, 6, 7, 8):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is not None:
                hosts.append((h, "dense(s=%d,n0=%d)" % (s, n0)))
    hosts.append((pg2(3), "PG(2,3)"))
    hosts.append((glue_cycle(pg2(3), 0, 7), "PG(2,3)+C7"))
    hosts.append((path_then_cycle(pg2(5), 0, 3, 7), "PG(2,5)+P3+C7"))
    hosts.append((cycle(9), "C9"))
    hosts.append((petersen(), "Petersen"))
    pera = perb = 0
    split_a = split_b = 0
    for g, nm in hosts:
        D, ecc, r = profile(g)
        diam = max(ecc)
        C = set(centre_of(ecc, r))
        for w in range(len(g)):
            if diam == r + 1 and w not in C:
                ck(ecc[w] == diam, "(PER-A) at %s w=%d" % (nm, w))
                pera += 1
            if ecc[w] == 2 * r:
                ck(ecc[w] == diam, "(PER-B) at %s w=%d" % (nm, w))
                perb += 1
            if ecc[w] == r + 1 and maximally_far(D, ecc, r, w):
                if diam == r + 1:
                    split_a += 1
                    ck(w not in C, "CASE A instance must be non-central")
                else:
                    split_b += 1
                    ck(ecc[w] < diam, "CASE B instance must be non-peripheral")
    print("  (PER-A) asserted at %d (host,w) pairs; (PER-B) at %d." % (pera, perb))
    print("  conditions 2+3 instances on these %d hosts: CASE A %d | CASE B %d"
          % (len(hosts), split_a, split_b))
    print("  POPULATION: the %d hosts listed in this part's source, ALL of them, no filter."
          % len(hosts))
    if split_b == 0:
        print("  CASE B is empty here -- as it must be on any host set where (RXM-PERI) has no")
        print("  counterexample.  This is NOT evidence for the restricted (RXM-PERI): round 41")
        print("  already refuted the unrestricted one with 961 in-class violations.")


# ------------------------------------------------------------------ PART 2


def part2():
    PARTS_RUN.append("PART2")
    print()
    print("=" * 78)
    print("PART 2 -- the 417-host family, re-measured for CASE A HOSTS")
    print("=" * 78)
    print("  Round 39's control asked whether any l>4 AND rad>=5 host carries a condition-3")
    print("  vertex at offset +1.  PART 1 says such a vertex is CASE A if the host has")
    print("  diam = rad+1 and CASE B otherwise.  So the control's reach is decided by ONE")
    print("  number that round 39 never printed: how many of its in-class hosts are CASE A")
    print("  hosts at all.  PREDICTION REGISTERED BEFORE THIS RUN: zero, because every")
    print("  l>4 AND rad>=5 host of that family is a dense core with a long tail attached,")
    print("  and a tail of length L pushes diam to rad+L-ish.")
    fam = build_family()
    tot = casea = selfc = 0
    inclass = inclass_casea = 0
    inclass_hosts = []
    skipped = 0
    for g, nm in fam:
        if over():
            skipped += 1
            continue
        n = len(g)
        if n > 140:
            skipped += 1
            continue
        D, ecc, r = profile(g)
        diam = max(ecc)
        lg = l_of(g)
        tot += 1
        if diam == r:
            selfc += 1
        if diam == r + 1:
            casea += 1
        if lg > 4 and r >= 5:
            inclass += 1
            inclass_hosts.append((nm, n, r, diam, lg))
            if diam == r + 1:
                inclass_casea += 1
    print("  hosts measured: %d  (skipped as too big / out of time: %d)" % (tot, skipped))
    print("  self-centred (diam = rad)          : %d" % selfc)
    print("  CASE A hosts (diam = rad+1)        : %d" % casea)
    print("  in-class hosts (l > 4 AND rad >= 5): %d" % inclass)
    print("  ... of those, CASE A hosts         : %d" % inclass_casea)
    print("  offset diam-rad on the in-class hosts:")
    prof = {}
    for (nm, n, r, diam, lg) in inclass_hosts:
        prof[diam - r] = prof.get(diam - r, 0) + 1
    print("    " + ", ".join("+%d : %d" % (k, prof[k]) for k in sorted(prof)))
    print()
    if inclass_casea == 0:
        print("  ==> PREDICTION HELD.  NOT ONE in-class host of this family is a CASE A host.")
        print("  WHAT THAT MEANS, AND ONLY WHAT THIS RUN MEASURED: every condition-3 vertex on")
        print("  the in-class hosts OF THIS FAMILY is a CASE B candidate, so on this family the")
        print("  number that could have come out CASE A is ZERO.  Round 39's census is UNDAMAGED")
        print("  -- it says what it says -- but on this family its reach is HALF of what the row")
        print("  needs.  Read through (SPLIT), a 0 at offset +1 here is evidence that (RXM-PERI)")
        print("  HOLDS at rad>=5 and l>4, which is a different and strictly narrower statement")
        print("  than the one round 41 refuted.")
        print("  NOT MEASURED HERE, AND THEREFORE NOT ASSERTED: round 39 also built 24 EXTRA")
        print("  control hosts (PG(2,7) cores, long tails, two-root tails, two joined cores).")
        print("  This run does not rebuild them, so it says NOTHING about whether any of those")
        print("  24 is a CASE A host.  They are core-plus-tail shapes and I expect not; an")
        print("  expectation is not a measurement and is printed as an expectation.")
    else:
        print("  ==> PREDICTION FAILED: %d in-class CASE A hosts exist in this family."
              % inclass_casea)
    return inclass_hosts


# ------------------------------------------------------------------ PART 3


def part3():
    PARTS_RUN.append("PART3")
    print()
    print("=" * 78)
    print("PART 3 -- round 36's base family: the two rad = 4 instances, and WHICH CASE")
    print("=" * 78)
    print("  Brief E44 5(b) carries an inherited datum: 'on a different family of 145 base")
    print("  graphs we previously found exactly 2 vertices satisfying conditions 1-3, both at")
    print("  rad = 4' with l = 2.333 and 2.455.  E44 could not say which CASE they are because")
    print("  the split did not exist yet.  TWO THINGS ARE CHECKED HERE: where those two")
    print("  instances actually come from, and which CASE they are.")
    print()
    print("  3a.  THE TWO INSTANCES, REBUILT FROM ROUND 32's OWN GENERATOR (rand(s,n0)):")
    for (s, n0, ex) in ((7, 18, 6), (30, 22, 8)):
        h = r32_rand_c4free(s * 7919 + n0, n0, ex)
        if h is None:
            print("    rand(s=%d,n0=%d): generator returned None -- NOT REBUILT" % (s, n0))
            ck(False, "round 32's named instance rand(s=%d,n0=%d) must rebuild" % (s, n0))
            continue
        D, ecc, r = profile(h)
        diam = max(ecc)
        lg = l_of(h)
        mu = min(a_val_matching(h, v) for v in range(len(h)))
        ws = [w for w in range(len(h)) if ecc[w] == r + 1 and maximally_far(D, ecc, r, w)]
        ck(c4_free(h), "rand(s=%d,n0=%d) C4-free" % (s, n0))
        print("    rand(s=%d,n0=%d): n=%d mu=%d rad=%d diam=%d l=%.3f  conditions-1-3 w's=%s"
              % (s, n0, len(h), mu, r, diam, lg, ws))
        for w in ws:
            print("        w=%d -> CASE %s   (|Ctr|=%d, ecc(w)=%d)"
                  % (w, "A" if diam == r + 1 else "B", len(centre_of(ecc, r)), ecc[w]))
    print()
    print("  3b.  ROUND 36's BASE FAMILY -- the family E44 5(b) ATTRIBUTES them to:")
    cfgs = []
    for bname, base in R36_BASES:
        nb = len(base)
        if not connected(base):
            continue
        cfgs.append((bname, base, (), ()))
        for k in (1, 2, 3):
            for roots in combinations(range(min(nb, 4)), k):
                for hs in _prod((1, 2, 3), k):
                    if nb + sum(hs) > 16:
                        continue
                    cfgs.append((bname, base, roots, hs))
    print("  configurations generated: %d" % len(cfgs))
    n_c4 = n_mu2 = 0
    hits = []        # with mu >= 2, i.e. E44 condition 1 in full
    hits_nomu = []   # C4-free only -- mu >= 2 DROPPED, printed separately
    for (bname, base, roots, hs) in cfgs:
        g = build_hairs(base, roots, hs)
        if not connected(g) or not c4_free(g):
            continue
        n_c4 += 1
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        if mu >= 2:
            n_mu2 += 1
        D, ecc, r = profile(g)
        diam = max(ecc)
        for w in range(len(g)):
            if ecc[w] == r + 1 and maximally_far(D, ecc, r, w):
                row = (bname, roots, hs, len(g), w, r, diam, l_of(g), mu)
                hits_nomu.append(row)
                if mu >= 2:
                    hits.append(row)
    print("  of those: C4-free and connected %d ; and mu >= 2 as well %d" % (n_c4, n_mu2))
    print("  vertices satisfying conditions 1-3 IN FULL (C4-free, mu>=2, ecc=rad+1, cond 3): %d"
          % len(hits))
    print("  vertices satisfying them with mu >= 2 DROPPED (C4-free only)                  : %d"
          % len(hits_nomu))
    seen = set()
    shown = 0
    for (bname, roots, hs, n, w, r, diam, lg, mu) in hits_nomu:
        key = (bname, roots, hs, r, diam, round(lg, 3), mu)
        if key in seen:
            continue
        seen.add(key)
        shown += 1
        if shown > 20:
            continue
        case = "A" if diam == r + 1 else "B"
        print("    %-9s roots=%-9s hs=%-9s n=%2d w=%2d mu=%d rad=%d diam=%d l=%.3f  -> CASE %s"
              % (bname, roots, hs, n, w, mu, r, diam, lg, case))
    print("    (%d distinct (config,rad,diam,l,mu) rows; at most 20 shown)" % shown)
    ca = sum(1 for h in hits_nomu if h[6] == h[5] + 1)
    cb = len(hits_nomu) - ca
    print("  over the C4-free-only bucket: CASE A %d   CASE B %d" % (ca, cb))
    rad4 = [h for h in hits_nomu if h[5] == 4]
    print("  rows at rad = 4 (the ones E44 5(b) quotes): %d" % len(rad4))
    print("  POPULATION THAT COULD HAVE COME OUT THE OTHER WAY (rule 90): the %d C4-free"
          % n_c4)
    print("  configurations (%d of them with mu >= 2); every one tested at every vertex."
          % n_mu2)
    return hits


def _prod(vals, k):
    if k == 0:
        yield ()
        return
    for rest in _prod(vals, k - 1):
        for v in vals:
            yield rest + (v,)


# ------------------------------------------------------------------ PART 4


def part4():
    PARTS_RUN.append("PART4")
    print()
    print("=" * 78)
    print("PART 4 -- THE NECKLACE FAMILY: a shape that CAN be a CASE A host at rad >= 5")
    print("=" * 78)
    print("""
  PART 2 says every in-class host this line has ever run has diam >= rad+2, so CASE A has
  never been sampled at rad >= 5.  A family that could sample it must be ROUND (diam close
  to rad) and DENSE (l > 4) and LONG (rad >= 5) at the same time.  Cores with tails are
  round-2-and-long or dense-and-short; they are never both.

  THE NECKLACE.  Take m blocks in a CYCLE, block i the incidence graph of PG(2,q_i).  Join
  block i to block i+1 by a partial injection whose SOURCES form an independent set of
  block i (its points).  Every such graph is C4-free: a cross-block C4 would need two
  matched vertices adjacent inside block i, and independent sources forbid that.  Density
  comes from the blocks (a = 6 inside PG(2,5), 4 inside PG(2,3), plus the cross edges);
  length comes from m.  The construction argument is written down because a brief must
  carry it -- but NOTHING below is certified by it.  Every host is checked by machine.
""")
    print("  MY OWN CONSTRUCTION ARGUMENT WAS WRONG AT m = 4, AND THIS RUN CAUGHT IT.")
    print("  At m = 4 blocks i and i+2 are joined by TWO routes (through i+1 and through")
    print("  i-1 = i+3), so a vertex of block i and a vertex of block i+2 can pick up one")
    print("  common neighbour on each route: a C4 the independent-sources argument does not")
    print("  exclude.  The corrected statement needs m >= 5.  Measured, on m = 4 hosts only:")
    m4bad = m4ok = 0
    m4specs = []
    for s in (1, 2, 3):
        m4specs.append(([3] * 4, s * 104729 + 4, 1.0, "any"))
        m4specs.append(([5] * 4, s * 49979687 + 4, 1.0, "any"))
        m4specs.append(([3] * 4, s * 32452843 + 4, 1.0, "points"))
        m4specs.append(([3] * 4, s * 15485863 + 4, 0.5, "any"))
        m4specs.append(([5, 3, 5, 3], s * 67867967 + 4, 1.0, "any"))
    for (qs, sd, fr, md) in m4specs:
        g = necklace(qs, sd, fr, md)
        if c4_free(g):
            m4ok += 1
        else:
            m4bad += 1
    print("    m = 4 necklaces built: %d ; C4-FREE %d ; NOT C4-free %d"
          % (m4ok + m4bad, m4ok, m4bad))
    ck(m4bad > 0, "the m=4 defect must be exhibited, not merely asserted")
    print("    So m = 4 is EXCLUDED below by construction, and the exclusion is earned.")
    print()

    specs = []
    for m in (5, 6, 7, 8, 9, 10, 12):
        for s in (1, 2, 3):
            specs.append(([3] * m, s * 104729 + m, 1.0, "any", None, "NL(3^%d,s%d)" % (m, s)))
    for m in (5, 6, 7, 8):
        for s in (1, 2):
            specs.append(([3] * m, s * 15485863 + m, 0.5, "any", None,
                          "NLh(3^%d,s%d)" % (m, s)))
            specs.append(([3] * m, s * 32452843 + m, 1.0, "points", None,
                          "NLp(3^%d,s%d)" % (m, s)))
    for m in (5, 6, 7):
        for s in (1, 2):
            specs.append(([5] * m, s * 49979687 + m, 1.0, "any", None,
                          "NL(5^%d,s%d)" % (m, s)))
            specs.append(([5, 3] * (m // 2) + [5] * (m % 2), s * 67867967 + m, 1.0, "any",
                          None, "NLmix(%d,s%d)" % (m, s)))
    for m in (5, 6, 7, 8):
        for s in (1, 2):
            specs.append(([3] * m, s * 86028121 + m, 0.34, "any", None,
                          "NLt(3^%d,s%d)" % (m, s)))
    # JAGGED: per-block matching densities, built to BREAK the tie that makes the centre
    # set huge.  A big centre set is exactly what (CS-1') uses to kill condition 3, so a
    # family that only ever produces big centres cannot test condition 3 at all.
    for m in (5, 6, 7, 8, 9):
        for s in (1, 2, 3):
            for fr, tag in (((1.0, 0.4), "a"), ((1.0, 0.6, 0.3), "b"),
                            ((0.9, 0.2, 0.7, 0.35), "c")):
                specs.append(([3] * m, s * 27644437 + m * 13, 1.0, "any", fr,
                              "NLj%s(3^%d,s%d)" % (tag, m, s)))
    for m in (5, 6, 7):
        for s in (1, 2):
            specs.append(([5, 3, 5, 3, 3, 5, 3][:m], s * 39916801 + m, 1.0, "any",
                          (1.0, 0.35, 0.7), "NLjm(%d,s%d)" % (m, s)))
    # SMALL blocks, added to drive the order of any witness down: PG(2,2) = Heawood, n = 14.
    for m in (5, 6, 7, 8, 9, 10):
        for s in (1, 2, 3, 4, 5, 6):
            for fr, tag in (((1.0, 0.4), "a"), ((1.0, 0.6, 0.3), "b"),
                            ((0.9, 0.2, 0.7, 0.35), "c"), ((1.0,), "d")):
                qq = [3 if (i % 2 == 0) else 2 for i in range(m)]
                specs.append((qq, s * 6700417 + m * 31, 1.0, "any", fr,
                              "NLs%s(%d,s%d)" % (tag, m, s)))
                specs.append(([3] * m, s * 2971215073 % (1 << 31) + m * 7, 1.0, "any", fr,
                              "NLk%s(3^%d,s%d)" % (tag, m, s)))

    hosts = []
    for (qs, seed, frac, mode, fr, nm) in specs:
        if over():
            break
        g = necklace(qs, seed, frac, mode, fr)
        if not connected(g):
            print("  %-16s NOT CONNECTED -- discarded" % nm)
            continue
        hosts.append((g, nm))
    print("  necklace hosts built and connected (m >= 5 only): %d" % len(hosts))

    # certify the class membership of every host, by machine
    n_c4 = 0
    rows = []
    brute_agree = 0
    for g, nm in hosts:
        if over():
            break
        if not c4_free(g):
            print("  %-16s NOT C4-FREE -- construction argument is WRONG, host discarded" % nm)
            continue
        n_c4 += 1
        mu = min(a_val_matching(g, v) for v in range(len(g)))
        for v in range(0, len(g), max(1, len(g) // 5)):
            ck(a_val(g, v) == a_val_matching(g, v), "brute a(.) == matching a(.) on %s" % nm)
            brute_agree += 1
        D, ecc, r = profile(g)
        diam = max(ecc)
        lg = l_of(g)
        rows.append((nm, len(g), mu, lg, r, diam, D, ecc))
    ck(n_c4 == len(hosts), "EVERY necklace host must be C4-free")
    print("  C4-free: %d of %d   (brute a(.) cross-checked at %d vertices)"
          % (n_c4, len(hosts), brute_agree))

    print()
    print("  %-16s %5s %4s %7s %5s %6s %7s %6s" %
          ("host", "n", "mu", "l", "rad", "diam", "offset", "|Ctr|"))
    inclass = casea_inclass = 0
    for (nm, n, mu, lg, r, diam, D, ecc) in rows:
        C = centre_of(ecc, r)
        print("  %-16s %5d %4d %7.3f %5d %6d %7s %6d"
              % (nm, n, mu, lg, r, diam, "+%d" % (diam - r), len(C)))
        if lg > 4 and r >= 5 and mu >= 2:
            inclass += 1
            if diam == r + 1:
                casea_inclass += 1
    print()
    print("  THE POPULATION THIS PART'S VERDICT IS ABOUT (rule 90, stated before the verdict):")
    print("    necklace hosts certified C4-free with mu >= 2 : %d" % n_c4)
    print("    ... IN CLASS (l > 4 AND rad >= 5)             : %d" % inclass)
    print("    ... of those, CASE A hosts (diam = rad+1)     : %d" % casea_inclass)
    print("    On a CASE B host a condition-3 vertex at offset +1 is a counterexample to the")
    print("    restricted (RXM-PERI); on a CASE A host it is E44's object outright.  BOTH are")
    print("    findings, so no host in the table above is wasted -- but only the CASE A count")
    print("    measures the thing round 39's family could not reach.")

    # ---- (CS-1') as a DECISION PROCEDURE on the CASE A hosts, not as a census
    print()
    print("  (CS-1') AS A DECISION PROCEDURE, APPLIED HOST BY HOST BEFORE ANY COUNTING.")
    print("  (CS-1') says a condition-3 vertex w has Ctr contained in the sphere S_rad(w),")
    print("  hence |Ctr| <= |S_rad(w)|.  So if |Ctr| > max_w |S_rad(w)| the host CANNOT carry")
    print("  a condition-3 vertex AT ALL -- proved, not measured.  Counting condition-3")
    print("  vertices on such a host is counting in a class that is provably empty.")
    dec_a = live_a = 0
    live_rows = []
    live_names = set()
    for (nm, n, mu, lg, r, diam, D, ecc) in rows:
        if lg <= 4 or r < 5 or mu < 2 or diam != r + 1:
            continue
        C = centre_of(ecc, r)
        best = 0
        for w in range(n):
            if ecc[w] == r:
                continue
            sz = sum(1 for v in range(n) if D[w][v] == r)
            if sz > best:
                best = sz
        if len(C) > best:
            dec_a += 1
        else:
            live_a += 1
            live_names.add(nm)
            live_rows.append((nm, n, r, diam, lg, len(C), best))
    print("    in-class CASE A hosts                                   : %d"
          % (dec_a + live_a))
    print("    ... DECIDED EMPTY BY (CS-1') alone (|Ctr| > max_w |S_r(w)|): %d" % dec_a)
    print("    ... LIVE: condition 3 is not excluded by counting        : %d" % live_a)
    for row in live_rows[:14]:
        print("      %-16s n=%3d rad=%d diam=%d l=%.3f |Ctr|=%3d max|S_r(w)|=%3d" % row)
    print("    ** THE ONLY CASE A HOSTS ON WHICH A 0 BELOW MEANS ANYTHING ARE THESE %d. **"
          % live_a)
    lv_v = lv_nc = lv_c3 = 0
    for (nm, n, mu, lg, r, diam, D, ecc) in rows:
        if nm not in live_names:
            continue
        lv_v += n
        for w in range(n):
            if ecc[w] != r:
                lv_nc += 1
            if maximally_far(D, ecc, r, w):
                lv_c3 += 1
    print("    THE CONTENTFUL CASE A POPULATION, counted in vertices: %d vertices on those %d"
          % (lv_v, live_a))
    print("    hosts, of which %d are NON-CENTRAL and so could satisfy condition 3;" % lv_nc)
    print("    condition-3 vertices actually found on them: %d." % lv_c3)

    # now search for the object
    print()
    print("  SEARCH FOR E44's OBJECT (conditions 1-5) OVER EVERY VERTEX OF EVERY IN-CLASS HOST:")
    found = []
    cond3_tot = 0
    cond2_tot = 0
    noncentral_tot = 0
    off_prof = {}
    c3_on_a = c3_on_b = 0
    vert_on_a = vert_on_b = 0
    for (nm, n, mu, lg, r, diam, D, ecc) in rows:
        if lg <= 4 or r < 5 or mu < 2:
            continue
        isA = (diam == r + 1)
        C = centre_of(ecc, r)
        for w in range(n):
            if isA:
                vert_on_a += 1
            else:
                vert_on_b += 1
            if ecc[w] != r:
                noncentral_tot += 1
            if ecc[w] == r + 1:
                cond2_tot += 1
            if maximally_far(D, ecc, r, w):
                cond3_tot += 1
                if isA:
                    c3_on_a += 1
                else:
                    c3_on_b += 1
                off_prof[ecc[w] - r] = off_prof.get(ecc[w] - r, 0) + 1
                if ecc[w] == r + 1:
                    found.append((nm, n, w, r, diam, lg, len(C)))
    print("    vertices on in-class CASE A hosts / CASE B hosts: %d / %d"
          % (vert_on_a, vert_on_b))
    print("    non-central vertices on in-class hosts          : %d" % noncentral_tot)
    print("    vertices with ecc(w) = rad+1 (condition 2)      : %d" % cond2_tot)
    print("    vertices maximally far from EVERY centre (c3)   : %d" % cond3_tot)
    print("    ... of them on CASE A hosts / CASE B hosts      : %d / %d" % (c3_on_a, c3_on_b))
    if off_prof:
        print("    offset profile of the condition-3 vertices      : "
              + ", ".join("+%d : %d" % (k, off_prof[k]) for k in sorted(off_prof)))
    print("    **E44 INSTANCES (conditions 1-5 together)       : %d**" % len(found))
    for row in found[:12]:
        nm, n, w, r, diam, lg, nc = row
        case = "A" if diam == r + 1 else "B"
        print("      %-16s n=%d w=%d rad=%d diam=%d l=%.3f |Ctr|=%d -> CASE %s"
              % (nm, n, w, r, diam, lg, nc, case))

    # liveness: the detector must fire where instances are KNOWN to exist
    print()
    print("  LIVENESS OF THE DETECTOR, so a 0 above is not a broken detector:")
    lv = 0
    for n0 in (14, 18, 22):
        for s in (1, 2, 3, 4, 5, 6):
            h = rand_c4free_dense(s * 7919 + n0, n0)
            if h is None:
                continue
            D, ecc, r = profile(h)
            for w in range(len(h)):
                if ecc[w] == r + 1 and maximally_far(D, ecc, r, w):
                    lv += 1
    print("    the SAME detector, run on the dense seeded hosts, fires at %d vertices." % lv)
    ck(lv > 0, "detector must fire somewhere or a zero above means nothing")
    return found, casea_inclass, inclass, {nm: g for g, nm in hosts}


# ------------------------------------------------------------------ MAIN


def floyd(g):
    """all-pairs distances by an INDEPENDENT code path (no BFS, no deque)."""
    n = len(g)
    INF = 10 ** 6
    D = [[INF] * n for _ in range(n)]
    for v in range(n):
        D[v][v] = 0
        for u in g[v]:
            D[v][u] = 1
    for k in range(n):
        Dk = D[k]
        for i in range(n):
            dik = D[i][k]
            if dik >= INF:
                continue
            Di = D[i]
            for j in range(n):
                nd = dik + Dk[j]
                if nd < Di[j]:
                    Di[j] = nd
    return D


def is_anchored_induced_path(g, P, w):
    """INDEPENDENT checker: P is a list of distinct vertices, P[0] == w, consecutive
    adjacent, no other pair adjacent."""
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


def build_anchored_path(g, w, cap, budget=400000):
    """DFS for an induced path with ENDPOINT w and >= cap vertices.  Returns the path or
    None.  Capped: a None is 'not found within the budget', NEVER 'does not exist'."""
    nodes = [0]
    best = [[]]
    dw = bfs(g, w)

    def dfs(path, pset):
        nodes[0] += 1
        if nodes[0] > budget:
            return None
        if len(path) > len(best[0]):
            best[0] = list(path)
        if len(path) >= cap:
            return list(path)
        u = path[-1]
        cands = sorted(g[u] - pset, key=lambda x: -dw[x])
        for x in cands:
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
    return r, len(best[0]), nodes[0] > budget


def part5(found, hostmap):
    PARTS_RUN.append("PART5")
    print()
    print("=" * 78)
    print("PART 5 -- THE WITNESSES, GRADED AS OBJECTS (rule 91 applied to MY OWN output)")
    print("=" * 78)
    if not found:
        print("  PART 4 found no instance; nothing to grade.")
        return
    print("  Every witness below is re-verified from its EDGE LIST with independent code")
    print("  paths: c4-freeness by brute pair scan, mu and l by BRUTE alpha(G[N(v)]) at EVERY")
    print("  vertex (not the matching formula), and all distances by FLOYD-WARSHALL (not BFS).")
    seen_hosts = {}
    for (nm, n, w, r, diam, lg, nc) in found:
        seen_hosts.setdefault(nm, []).append(w)
    ordered = sorted(seen_hosts.items(), key=lambda kv: len(hostmap[kv[0]]))
    graded = 0
    for nm, ws in ordered:
        if over():
            print("  (deadline reached; %d witness hosts graded)" % graded)
            break
        g = hostmap[nm]
        n = len(g)
        ck(connected(g), "%s connected" % nm)
        ck(c4_free(g), "%s C4-free (brute pair scan)" % nm)
        aa = [a_val(g, v) for v in range(n)]
        mu = min(aa)
        lg = sum(aa) / float(n)
        D = floyd(g)
        ecc = [max(D[v]) for v in range(n)]
        r = min(ecc)
        diam = max(ecc)
        C = [v for v in range(n) if ecc[v] == r]
        ck(mu >= 2, "%s mu >= 2 by BRUTE alpha" % nm)
        ck(lg > 4, "%s l > 4 by BRUTE alpha" % nm)
        ck(r >= 5, "%s rad >= 5" % nm)
        graded += 1
        print()
        print("  %s : n=%d  m=%d  mu=%d  l=%.4f  rad=%d  diam=%d  |Ctr|=%d  Ctr=%s"
              % (nm, n, len(edges_of(g)), mu, lg, r, diam, len(C), C[:8]))
        for w in ws:
            ck(ecc[w] == r + 1, "%s w=%d has ecc = rad+1" % (nm, w))
            ck(all(D[c][w] == r for c in C), "%s w=%d maximally far from EVERY centre"
               % (nm, w))
            case = "A" if diam == r + 1 else "B"
            print("    w=%3d  ecc(w)=%d = rad+1  d(c,w) = %s for every centre  -> CASE %s"
                  % (w, ecc[w], sorted({D[c][w] for c in C}), case))
            if case == "B":
                print("           and therefore ALSO a counterexample to (RXM-PERI) restricted")
                print("           to l > 4 and rad >= 5: ecc(w) = %d < %d = diam." % (ecc[w], diam))
            cap = ecc[w] + 3
            P, bestlen, trunc = build_anchored_path(g, w, cap)
            if P is not None:
                ck(is_anchored_induced_path(g, P, w), "%s w=%d built path is induced+anchored"
                   % (nm, w))
                print("           endpath(G,w) >= %d = ecc(w)+3 : BUILT and checker-verified"
                      % len(P))
                print("           path = %s" % (P,))
            else:
                print("           NO ecc(w)+3 anchored induced path found; longest built %d;"
                      % bestlen)
                print("           search TRUNCATED = %s.  A truncated search proves NOTHING."
                      % trunc)
    # the smallest witness, printed as an edge list so anyone can rebuild it
    small = ordered[0][0]
    g = hostmap[small]
    print()
    print("  SMALLEST WITNESS, EXPLICIT EDGE LIST (%s, n=%d):" % (small, len(g)))
    E = edges_of(g)
    for i in range(0, len(E), 12):
        print("    " + " ".join("(%d,%d)" % e for e in E[i:i + 12]))


def main():
    print("WOWII-133 round 42 -- E44's CLASS SPLITS IN TWO")
    print("interpreter: %s" % sys.version.split()[0])
    part0()
    part1()
    part2()
    part3()
    found, ca, ic, hostmap = part4()
    part5(found, hostmap)
    print()
    print("=" * 78)
    print("PARTS RUN: %s" % ", ".join(PARTS_RUN))
    print("CHECKS: %d   FAILURES: %d   elapsed %.1fs" % (CHECKS, FAILS, time.time() - T0))
    print("=" * 78)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
