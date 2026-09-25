#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROUND 5 INDEPENDENT RE-VERIFICATION (charter sec.105) -- owner-zc1a7.

Imports NOTHING from r5_a6.py, meataxe.py, or any earlier round's script, and reads
no JSON.  Different multiplication convention.  Different algorithms throughout:

  V1  A_6 rebuilt with (x*y)(i) = y(x(i));  classes by brute-force conjugation orbits;
      centraliser orders by COUNTING COMMUTING ELEMENTS
  V2  the ordinary character table verified as a WITNESS in exact Z[phi] arithmetic:
      row orthogonality (all 28 pairs), column orthogonality against the brute-force
      centraliser orders, and the class-algebra identity with structure constants
      recomputed in the opposite convention
  V3  the NUMBER of 2-blocks with NO CHARACTER TABLE AT ALL: every one of the 4^7 =
      16384 elements of Z(F_4 A_6) tested for idempotency (and all 2^7 = 128 of
      Z(F_2 A_6)).  r4 did this over F_2 only and inferred F_4 by an argument;
      here F_4 is done directly.
  V4  the block partition from the explicitly computed primitive idempotents
  V5  the two 4-dimensional Brauer characters MODULE-FREE, by counting fixed points
      of the two 6-point actions; decomposition matrix and Cartan matrix from those
  V6  the Z_2C_4 lattice bounds re-derived by BRUTE-FORCE enumeration over multisets
      of indecomposable-lattice supports, not by the closed formulas
  V7  the HeLP multiplicities by inverting the 4x4 Vandermonde over Q(i)
  V8  the A_6 global killer rebuilt MODULE-FREE from the exterior-square identity
  V9  the A_6 -> A_7 fusion re-checked in the opposite convention

Exact arithmetic only.  No floating point.
"""
from fractions import Fraction
from itertools import combinations, permutations, product

OUT = []
def say(s=""):
    print(s); OUT.append(s)
def hdr(s):
    say(""); say("-" * 78); say(s); say("-" * 78)

# ---------------------------------------------------------------- V1
hdr("V1  A_6 rebuilt, OPPOSITE convention  (x*y)(i) = y(x(i))")

def mul(a, b):
    return tuple(b[a[i]] for i in range(len(a)))
def inv(a):
    r = [0] * len(a)
    for i, x in enumerate(a):
        r[x] = i
    return tuple(r)
def order(a):
    e = tuple(range(len(a))); r = a; k = 1
    while r != e:
        r = mul(r, a); k += 1
    return k
def ctype(a):
    seen = [0] * len(a); out = []
    for i in range(len(a)):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]:
                seen[j] = 1; j = a[j]; L += 1
            out.append(L)
    return tuple(sorted(out, reverse=True))

gens = [(1, 2, 3, 4, 0, 5), (0, 1, 2, 4, 5, 3)]
G = {tuple(range(6))}
fr = [tuple(range(6))]
while fr:
    nf = []
    for x in fr:
        for g in gens:
            y = mul(x, g)
            if y not in G:
                G.add(y); nf.append(y)
    fr = nf
G = sorted(G)
say("|A_6| = %d" % len(G))
assert len(G) == 360

left = set(G); CLS = []
while left:
    x0 = min(left)
    orb = {x0}
    st = [x0]
    while st:
        x = st.pop()
        for g in G:
            y = mul(mul(inv(g), x), g)
            if y not in orb:
                orb.add(y); st.append(y)
    CLS.append(sorted(orb)); left -= orb
CLS.sort(key=lambda c: (order(c[0]), len(c), ctype(c[0])))
reps = [c[0] for c in CLS]
sizes = [len(c) for c in CLS]
say("classes: %s" % [(ctype(r), len(c)) for r, c in zip(reps, CLS)])
# centraliser orders by COUNTING commuting elements
cents = [sum(1 for g in G if mul(mul(inv(g), r), g) == r) for r in reps]
say("centraliser orders by counting commuting elements: %s" % cents)
assert all(cents[i] * sizes[i] == 360 for i in range(len(CLS)))
CLOF = {}
for i, c in enumerate(CLS):
    for x in c:
        CLOF[x] = i
NM = []
cnt = {}
for i, r in enumerate(reps):
    o = order(r); cnt[o] = cnt.get(o, 0) + 1
    NM.append("%d%s" % (o, "ab"[cnt[o] - 1]))
say("names: %s" % NM)
INVC = [CLOF[inv(r)] for r in reps]
nc = len(CLS)

# structure constants, opposite convention
A = [[[0] * nc for _ in range(nc)] for _ in range(nc)]
for k in range(nc):
    for l in range(nc):
        cnt2 = [0] * nc
        for x in CLS[k]:
            for y in CLS[l]:
                cnt2[CLOF[mul(x, y)]] += 1
        for m in range(nc):
            assert cnt2[m] % sizes[m] == 0
            A[k][l][m] = cnt2[m] // sizes[m]
say("class-algebra structure constants recomputed in the opposite convention: OK")

# ---------------------------------------------------------------- V2
hdr("V2  the ordinary character table verified as a WITNESS, exactly in Z[phi]")
# element of Z[phi]:  (a,b) = a + b*phi,  phi^2 = phi + 1
def zadd(x, y): return (x[0] + y[0], x[1] + y[1])
def zmul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def zconj(x):            # phi -> 1 - phi   (the non-trivial Galois automorphism)
    a, b = x
    return (a + b, -b)
def zsc(n, x): return (n * x[0], n * x[1])

# the CLAIMED table, in the class order  1a 2a 3a 3b 4a 5a 5b, as produced by the builder
PHI_ = (0, 1)
CLM = [[(1, 0)] * 7,
       [(5, 0), (1, 0), (-1, 0), (2, 0), (-1, 0), (0, 0), (0, 0)],
       [(5, 0), (1, 0), (2, 0), (-1, 0), (-1, 0), (0, 0), (0, 0)],
       [(8, 0), (0, 0), (-1, 0), (-1, 0), (0, 0), PHI_, zconj(PHI_)],
       [(8, 0), (0, 0), (-1, 0), (-1, 0), (0, 0), zconj(PHI_), PHI_],
       [(9, 0), (1, 0), (0, 0), (0, 0), (1, 0), (-1, 0), (-1, 0)],
       [(10, 0), (-2, 0), (1, 0), (1, 0), (0, 0), (0, 0), (0, 0)]]
DEGS = [1, 5, 5, 8, 8, 9, 10]
order_check = [(ctype(reps[i]), sizes[i]) for i in range(nc)]
say("class order used by the witness: %s" % [NM[i] for i in range(nc)])
assert [sizes[i] for i in range(nc)] == [1, 45, 40, 40, 90, 72, 72]
assert sum(d * d for d in DEGS) == 360
# row orthogonality, all 28 pairs
bad = 0
for r in range(nc):
    for s in range(r, nc):
        acc = (0, 0)
        for k in range(nc):
            # all classes of A_6 are real (INVC is the identity, checked in V1), so the
            # inner product is  sum_k |C_k| chi(g_k) psi(g_k^{-1})  with no conjugation
            acc = zadd(acc, zsc(sizes[k], zmul(CLM[r][k], CLM[s][INVC[k]])))
        expect = (360 if r == s else 0, 0)
        if acc != expect:
            bad += 1
            say("   row orthogonality FAILS at (%d,%d): %s" % (r, s, acc))
say("V2a row orthogonality, all %d pairs: %d failures" % (nc * (nc + 1) // 2, bad))
assert bad == 0
bad = 0
for k in range(nc):
    acc = (0, 0)
    for r in range(nc):
        acc = zadd(acc, zmul(CLM[r][k], CLM[r][INVC[k]]))
    if acc != (cents[k], 0):
        bad += 1; say("   column orthogonality FAILS at %s: %s vs %d" % (NM[k], acc, cents[k]))
say("V2b column orthogonality against the BRUTE-FORCE centraliser orders: %d failures" % bad)
assert bad == 0
# class-algebra identity for the central characters
bad = 0
for r in range(nc):
    om = []
    for k in range(nc):
        num = zsc(sizes[k], CLM[r][k])
        assert num[0] % DEGS[r] == 0 and num[1] % DEGS[r] == 0
        om.append((num[0] // DEGS[r], num[1] // DEGS[r]))
    for k in range(nc):
        for l in range(nc):
            lhs = zmul(om[k], om[l])
            rhs = (0, 0)
            for m in range(nc):
                rhs = zadd(rhs, zsc(A[k][l][m], om[m]))
            if lhs != rhs:
                bad += 1
say("V2c omega(k)omega(l) = sum a_klm omega(m) in Z[phi]: %d failures of %d"
    % (bad, nc ** 3))
assert bad == 0
say("    (the three tests together pin the table up to the order of the rows.)")

# ---------------------------------------------------------------- V3
hdr("V3  the NUMBER of 2-blocks with NO CHARACTER TABLE: brute-force idempotents")
# F_4 = {0,1,w,1+w} encoded 0,1,2,3 with w^2 = w+1
F4MUL = [[0] * 4 for _ in range(4)]
def f4m(a, b):
    if a == 0 or b == 0: return 0
    # 1->0, w->1, 1+w->2 as discrete logs base w
    lg = {1: 0, 2: 1, 3: 2}; ex = {0: 1, 1: 2, 2: 3}
    return ex[(lg[a] + lg[b]) % 3]
for a in range(4):
    for b in range(4):
        F4MUL[a][b] = f4m(a, b)
def f4a(a, b): return a ^ b        # F_4 additive group is (Z/2)^2 = XOR on 2 bits
# check the field axioms actually hold for this encoding
for a in range(4):
    for b in range(4):
        for c in range(4):
            assert F4MUL[a][f4a(b, c)] == f4a(F4MUL[a][b], F4MUL[a][c])
            assert F4MUL[F4MUL[a][b]][c] == F4MUL[a][F4MUL[b][c]]
say("F_4 arithmetic table built and its axioms checked exhaustively (64 + 64 cases)")

A2 = [[[A[k][l][m] % 2 for m in range(nc)] for l in range(nc)] for k in range(nc)]
def square_coeffs(x, field_mul, field_add, q):
    out = [0] * nc
    for k in range(nc):
        if x[k] == 0: continue
        for l in range(nc):
            if x[l] == 0: continue
            c = field_mul(x[k], x[l])
            for m in range(nc):
                if A2[k][l][m]:
                    out[m] = field_add(out[m], c)
    return out
def count_idems(q, field_mul, field_add):
    n = 0; prim = []
    for x in product(range(q), repeat=nc):
        if square_coeffs(list(x), field_mul, field_add, q) == list(x):
            n += 1; prim.append(x)
    return n, prim
n2, idem2 = count_idems(2, lambda a, b: a * b % 2, lambda a, b: (a + b) % 2)
say("Z(F_2 A_6): %d elements tested, %d idempotents  ==>  2^r = %d  ==>  r = %d blocks"
    % (2 ** nc, n2, n2, n2.bit_length() - 1))
n4, idem4 = count_idems(4, lambda a, b: F4MUL[a][b], f4a)
say("Z(F_4 A_6): %d elements tested, %d idempotents  ==>  2^r = %d  ==>  r = %d blocks"
    % (4 ** nc, n4, n4, n4.bit_length() - 1))
assert n2 == 4 and n4 == 8
say("    => 2 blocks over F_2, 3 blocks over F_4.  NO character table was used.")

# ---------------------------------------------------------------- V4
hdr("V4  the block partition of Irr(A_6) from the explicit primitive idempotents")
prim4 = []
for e in idem4:
    if all(x == 0 for x in e): continue
    # primitive = not a sum of two smaller nonzero orthogonal idempotents in the list
    is_prim = True
    for f in idem4:
        if all(x == 0 for x in f) or f == e: continue
        # f <= e  iff  e*f = f
        prod = [0] * nc
        for k in range(nc):
            if e[k] == 0: continue
            for l in range(nc):
                if f[l] == 0: continue
                c = F4MUL[e[k]][f[l]]
                for m in range(nc):
                    if A2[k][l][m]:
                        prod[m] = f4a(prod[m], c)
        if tuple(prod) == f:
            is_prim = False; break
    if is_prim:
        prim4.append(e)
say("primitive idempotents of Z(F_4 A_6): %d found" % len(prim4))
assert len(prim4) == 3
# omega_chi(e) mod (2) tells which block chi lies in
def om_mod2(r):
    out = []
    for k in range(nc):
        num = zsc(sizes[k], CLM[r][k])
        a, b = num[0] // DEGS[r], num[1] // DEGS[r]
        a %= 2; b %= 2
        out.append({(0, 0): 0, (1, 0): 1, (0, 1): 2, (1, 1): 3}[(a, b)])
    return out
part = {}
for r in range(nc):
    om = om_mod2(r)
    hit = []
    for ei, e in enumerate(prim4):
        v = 0
        for k in range(nc):
            v = f4a(v, F4MUL[e[k]][om[k]])
        if v:
            hit.append(ei)
    assert len(hit) == 1, (r, hit)
    part.setdefault(hit[0], []).append(r)
for ei in sorted(part):
    say("  block %d : chi = %s  degrees %s" %
        (ei, [x + 1 for x in part[ei]], [DEGS[x] for x in part[ei]]))
assert sorted(map(sorted, part.values())) == sorted([[0, 1, 2, 5, 6], [3], [4]])
say("  matches the builder's Osima partition {1,5,5,9,10} | {8} | {8}.")
i2a = 1; i4a = 4
blind = [ei for ei in part if all(CLM[r][i2a] == CLM[r][i4a] for r in part[ei])]
say("  BLIND blocks (chi(2a) = chi(4a) throughout): %s  ==> %d of %d blocks can obstruct"
    % (sorted(blind), len(part) - len(blind), len(part)))
assert len(part) - len(blind) == 1

# ---------------------------------------------------------------- V5
hdr("V5  the two 4-dimensional 2-modular Brauer characters, MODULE-FREE")
# natural 6-point action
def fix6(g): return sum(1 for x in range(6) if g[x] == x)
pi6 = [fix6(r) for r in reps]
# second 6-point action: cosets of a transitive A_5 = PSL(2,5) on P^1(F_5)
Ht = {tuple(range(6))}
fr = [tuple(range(6))]
Hg = [(1, 2, 3, 4, 0, 5), (5, 4, 2, 3, 1, 0)]   # PSL(2,5) on P^1(F_5), inf = 5
while fr:
    nf = []
    for x in fr:
        for g in Hg:
            y = mul(x, g)
            if y not in Ht:
                Ht.add(y); nf.append(y)
    fr = nf
say("transitive A_5 inside A_6: order %d, transitive = %s"
    % (len(Ht), len({h[0] for h in Ht}) == 6))
assert len(Ht) == 60
cos = []
seen = set()
for g in G:
    if g in seen: continue
    c = frozenset(mul(h, g) for h in Ht)     # right cosets Hg in the opposite convention
    cos.append(c); seen |= c
assert len(cos) == 6
def fix6b(g):
    n = 0
    for c in cos:
        rep = next(iter(c))
        if frozenset(mul(h, mul(rep, g)) for h in Ht) == c:
            n += 1
    return n
pi6b = [fix6b(r) for r in reps]
say("permutation characters by counting fixed points: pi_6 = %s, pi_6' = %s" % (pi6, pi6b))
reg2 = [i for i in range(nc) if order(reps[i]) % 2 == 1]
say("2-regular classes: %s" % [NM[i] for i in reg2])
phi1 = [1] * len(reg2)
phi4a = [pi6[i] - 2 for i in reg2]
phi4b = [pi6b[i] - 2 for i in reg2]
say("  phi_1  = %s" % phi1)
say("  phi_4a = %s   (= pi_6  - 2, the 4-dim section of the 6-point module)" % phi4a)
say("  phi_4b = %s   (= pi_6' - 2)" % phi4b)
assert sorted([phi4a, phi4b]) == sorted([[4, 1, -2, -1, -1], [4, -2, 1, -1, -1]])
prin = sorted(part[[k for k in part if len(part[k]) == 5][0]])
DEC = {}
for r in prin:
    tgt = [CLM[r][i][0] for i in reg2]
    assert all(CLM[r][i][1] == 0 for i in reg2)
    sols = [(a, b, c) for a in range(12) for b in range(12) for c in range(12)
            if all(a * phi1[j] + b * phi4a[j] + c * phi4b[j] == tgt[j]
                   for j in range(len(reg2)))]
    assert len(sols) == 1, (r, sols)
    DEC[r] = sols[0]
    say("  chi%d (deg %2d) = %d[1] + %d[4a] + %d[4b]" % (r + 1, DEGS[r], *sols[0]))
CART = [[sum(DEC[r][i] * DEC[r][j] for r in prin) for j in range(3)] for i in range(3)]
say("  Cartan = %s ; det = %d ; basic-algebra rank = %d ; block rank = %d"
    % (CART,
       CART[0][0] * (CART[1][1] * CART[2][2] - CART[1][2] * CART[2][1])
       - CART[0][1] * (CART[1][0] * CART[2][2] - CART[1][2] * CART[2][0])
       + CART[0][2] * (CART[1][0] * CART[2][1] - CART[1][1] * CART[2][0]),
       sum(sum(r) for r in CART), sum(DEGS[r] ** 2 for r in prin)))
assert sum(sum(r) for r in CART) == 34 and sum(DEGS[r] ** 2 for r in prin) == 232
say("  ==> basic algebra rank 34, block rank 232 -- MATCHES the builder.")

# ---------------------------------------------------------------- V7 (before V6)
hdr("V7  HeLP multiplicities by inverting the 4x4 Vandermonde over Q(i)")
# work in Q(i): pairs (a,b) of Fractions meaning a + b i
def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
Z4 = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]
# V[j][k] = zeta^{jk} ; chi(u^j) = sum_k mu_k zeta^{jk} ; solve for mu
def mults_vandermonde(chi_of_powers):
    mu = []
    for k in range(4):
        acc = (Fraction(0), Fraction(0))
        for j in range(4):
            acc = cadd(acc, cmul(chi_of_powers[j], Z4[(-j * k) % 4]))
        mu.append((acc[0] / 4, acc[1] / 4))
    return mu
def helpvec(deg, c2a, c4a, t):
    cu = t * c2a + (1 - t) * c4a
    powers = [(Fraction(deg), Fraction(0)), (Fraction(cu), Fraction(0)),
              (Fraction(c2a), Fraction(0)), (Fraction(cu), Fraction(0))]
    return mults_vandermonde(powers)
vals = [(DEGS[r], CLM[r][i2a][0], CLM[r][i4a][0]) for r in range(nc)]
res = {}
for t in range(-6, 7):
    kill = []
    for r in range(nc):
        mu = helpvec(*vals[r], t)
        for j, (a, b) in enumerate(mu):
            assert b == 0
            if a < 0 or a.denominator != 1:
                kill.append("chi%d:mu%d=%s" % (r + 1, j, a))
    cong = ((1 - t) - 1) % 2 == 0
    res[t] = (kill, cong)
surv = [t for t in res if not res[t][0] and res[t][1]]
say("  2-local admissible eps_2a(u): %s   (Vandermonde route)" % sorted(surv))
assert sorted(surv) == [0, 2]
say("  t = -2 killers: %s" % res[-2][0])
say("  t = +-1 killed only by the p=2 congruence (ordinary kills %d, %d)"
    % (len(res[1][0]), len(res[-1][0])))
say("  positive control t = 0 (a genuine g in 4a): 0 kills, congruence OK")
assert not res[0][0] and res[0][1]

# ---------------------------------------------------------------- V10
hdr("V10 the support-free 2-local enumeration, re-run independently")
say("Claim under test: given only u^2 ~ 2a, the ordinary Luthar-Passi system plus the")
say("p=2 congruence leaves 300 vectors in Z_(2)^7, of which 4 are integral and 2 have")
say("support inside {2a,4a}.  Re-run here with the Vandermonde multiplicities of V7 and")
say("an eps-inversion built from the WITNESS table and the BRUTE-FORCE centraliser orders.")
i1a = 0
# power map on classes, computed here
POWc = [[CLOF[tuple(_p for _p in _pw)] for _pw in [reps[i]]] for i in range(nc)]
def cls_pow(i, k):
    x = reps[i]; y = tuple(range(6))
    for _ in range(k):
        y = mul(y, x)
    return CLOF[y]
SQ = [cls_pow(i, 2) for i in range(nc)]
say("  power map C -> C^2 : %s" % [(NM[i], NM[SQ[i]]) for i in range(nc)])
optsV = []
for r in range(nc):
    m1 = (DEGS[r] - CLM[r][i2a][0])
    assert m1 % 4 == 0 and CLM[r][i2a][1] == 0
    m1 //= 4
    tot = DEGS[r] - 2 * m1
    optsV.append([1] if r == 0 else [tot - 2 * k for k in range(tot + 1)])
say("  chi(u) ranges: %s" % optsV)
def eps_of(cu):
    out = []
    for k in range(nc):
        a = Fraction(0); b = Fraction(0)
        for r in range(nc):
            va, vb = CLM[r][k]
            a += cu[r] * va; b += cu[r] * vb
        out.append((Fraction(a, cents[k]), Fraction(b, cents[k])))
    return out
n_all = n_z2 = 0
surv = []
for cu in product(*optsV):
    if cu[3] != cu[4]:
        continue
    n_all += 1
    ev = eps_of(cu)
    if any(b != 0 for (a, b) in ev):
        continue
    if any(a.denominator % 2 == 0 for (a, b) in ev):
        continue
    e = [a for (a, b) in ev]
    if sum(e) != 1:
        continue
    n_z2 += 1
    ok = True
    for D in range(nc):
        lhs = sum(e[C] for C in range(nc) if SQ[C] == D)
        num = lhs - (1 if D == i2a else 0)
        if num.denominator % 2 == 0 or num.numerator % 2 != 0:
            ok = False; break
    if ok:
        surv.append((cu, e))
ints = [(cu, e) for cu, e in surv if all(x.denominator == 1 for x in e)]
supp = [(cu, e) for cu, e in surv if all(e[k] == 0 for k in range(nc) if k not in (i2a, i4a))]
say("  chi4(u) = chi5(u) candidates                  : %5d" % n_all)
say("  ... with all eps in Z_2 (odd denominators)    : %5d" % n_z2)
say("  ... and satisfying the p=2 congruence          : %5d" % len(surv))
say("  ...... integral                                : %5d" % len(ints))
say("  ...... support inside {2a,4a}                  : %5d" % len(supp))
assert (n_all, n_z2, len(surv), len(ints), len(supp)) == (2400, 600, 300, 4, 2)
say("  the four integral vectors:")
for cu, e in sorted(ints, key=lambda x: [int(v) for v in x[1]]):
    say("     %s" % {NM[k]: int(e[k]) for k in range(nc) if e[k] != 0})
say("  ==> counts and vectors REPRODUCED exactly.  The two extra integral vectors are")
say("      supported on classes of order 3 and 5, which is precisely what Hertweck's")
say("      ord(C) | n kills over Z G and what has no verified Z_2 analogue.")
say("  CONTROL: a genuine g in 4a (eps_4a = 1) is among the survivors: %s"
    % any(all(e[k] == (1 if k == i4a else 0) for k in range(nc)) for cu, e in surv))
say("  CONTROL: %d of the %d candidates are REJECTED, so the system is not vacuous."
    % (n_all - len(surv), n_all))

# ---------------------------------------------------------------- V6
hdr("V6  the Z_2C_4 lattice bounds by BRUTE-FORCE enumeration of indecomposable supports")
# An indecomposable Z_2C_4-lattice contains each of T, Sg, W at most once (Berman-Gudkov,
# as quoted in the sourcing paper).  Enumerate all multisets of supports realising the
# rational character (m0 copies of T, m2 of Sg, m1 of W) and maximise / minimise the
# F_2 ranks summand by summand, using only the elementary facts r3 proved:
#   (b1) a summand without W has ubar^2 = 1, so contributes 0 to r_2
#   (b2) a summand with W contributes at most a+b to r_2 where a,b in {0,1} count T,Sg
#   (b4) every W-summand has ubar != 1, so contributes >= 1 to r_1
#   (b5) r_1 <= rank - 1 on each summand
#   (b6) an r_3 contribution needs a rank-4 summand, support {T,Sg,W}
SUPPORTS = [s for s in
            [("T",), ("S",), ("W",), ("T", "S"), ("T", "W"), ("S", "W"), ("T", "S", "W")]]
def rankof(s):
    return sum({"T": 1, "S": 1, "W": 2}[x] for x in s)
def enum_decomps(m0, m1, m2):
    """all multisets of supports with the given multiplicities of T, Sg, W"""
    out = []
    maxn = m0 + m1 + m2
    def rec(i, rem0, rem1, rem2, cur):
        if rem0 == rem1 == rem2 == 0:
            out.append(tuple(cur)); return
        if i == len(SUPPORTS):
            return
        s = SUPPORTS[i]
        a = 1 if "T" in s else 0
        b = 1 if "W" in s else 0
        c = 1 if "S" in s else 0
        k = 0
        while a * k <= rem0 and b * k <= rem1 and c * k <= rem2:
            rec(i + 1, rem0 - a * k, rem1 - b * k, rem2 - c * k, cur + [s] * k)
            k += 1
            if a == 0 and b == 0 and c == 0:
                break
    rec(0, m0, m1, m2, [])
    return out
def bf_bounds(n, m0, m1, m2):
    best = {1: (10 ** 9, -1), 2: (10 ** 9, -1), 3: (10 ** 9, -1)}
    ub1 = ub2 = ub3 = 0; lb1 = 10 ** 9
    for D in enum_decomps(m0, m1, m2):
        s1 = s2 = s3 = 0; l1 = 0
        for s in D:
            rk = rankof(s)
            hasW = "W" in s
            s1 += rk - 1                                   # (b5)
            if hasW:
                l1 += 1                                    # (b4)
                s2 += sum(1 for x in s if x in ("T", "S"))  # (b2)
                if rk == 4:
                    s3 += 1                                # (b6)
        ub1 = max(ub1, s1); ub2 = max(ub2, s2); ub3 = max(ub3, s3)
        lb1 = min(lb1, l1)
    return ub1, ub2, ub3, lb1
def closed(n, m0, m1, m2):
    return (n - m1 - max(max(m0 - m1, 0), max(m2 - m1, 0)),
            min(m0, m1) + min(m2, m1), min(m0, m1, m2), m1)
say("  chi  deg  (m0,m1,m2)   closed formulas      brute force        agree")
BND = {}
for r in range(nc):
    mu = [x[0] for x in helpvec(*vals[r], 2)]
    m0, m1, m2 = int(mu[0]), int(mu[1]), int(mu[2])
    cf = closed(DEGS[r], m0, m1, m2)
    bf = bf_bounds(DEGS[r], m0, m1, m2)
    BND[r] = cf
    say("  chi%-2d %3d  (%d,%d,%d)      UB1=%2d UB2=%d UB3=%d LB1=%d   UB1=%2d UB2=%d UB3=%d LB1=%d   %s"
        % (r + 1, DEGS[r], m0, m1, m2, cf[0], cf[1], cf[2], cf[3],
           bf[0], bf[1], bf[2], bf[3], "YES" if cf == bf else "NO"))
    assert cf == bf
say("  all %d bounds agree with the closed formulas." % (4 * nc))

say("")
say("FEASIBILITY, recomputed: unknowns r_j(S) for S in {1,4a,4b} inside the ONE block")
say("that can obstruct, constrained by sum_S d_chi,S r_j(S) <= UB_j(chi).")
COMP = {r: DEC[r] for r in prin}
for j in (1, 2, 3):
    sols = [v for v in product(range(1), range(4), range(4))
            if all(sum(COMP[r][i] * v[i] for i in range(3)) <= BND[r][[0, 1, 2][j - 1]]
                   for r in prin)]
    say("  j = %d : %d solutions, all-zero admissible = %s" % (j, len(sols), (0, 0, 0) in sols))
    assert (0, 0, 0) in sols
say("  ==> FEASIBLE.  Independent confirmation that the p=2 lattice method does not")
say("      settle A_6 either.")

# ---------------------------------------------------------------- V8
hdr("V8  the A_6 GLOBAL killer, rebuilt MODULE-FREE")
say("The 4-dimensional F_3-section of the 6-point permutation module has Brauer")
say("character pi_6 - 2 on 3-regular classes; its EXTERIOR SQUARE has Brauer character")
say("chi(g)^2 - chi(g^2))/2, valid because Brauer characters are sums of lifted")
say("eigenvalues and Lambda^2 has the pairwise products.")
i1a = 0
sq = {i1a: i1a, i2a: i1a, i4a: i2a}
ch = {k: pi6[k] - 2 for k in (i1a, i2a, i4a)}
L2 = {k: (ch[k] * ch[k] - ch[sq[k]]) // 2 for k in (i1a, i2a, i4a)}
say("  chi_M   on (1a,2a,4a) = %s" % [ch[k] for k in (i1a, i2a, i4a)])
say("  Lambda^2 on (1a,2a,4a) = %s   (no matrices built)" % [L2[k] for k in (i1a, i2a, i4a)])
assert [L2[k] for k in (i1a, i2a, i4a)] == [6, -2, 2]
for t in (0, 2):
    mu = [x[0] for x in helpvec(L2[i1a], L2[i2a], L2[i4a], t)]
    say("  t = %d : mu = %s  %s" % (t, [str(x) for x in mu],
        "KILLED" if any(x < 0 for x in mu) else "passes  <-- POSITIVE CONTROL"))
say("  ==> confirmed: (2,-1) dies GLOBALLY for A_6 and survives 2-LOCALLY.")

# ---------------------------------------------------------------- V9
hdr("V9  the A_6 -> A_7 fusion, opposite convention")
def sgn7(p):
    s = 0; seen = [0] * 7
    for i in range(7):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]:
                seen[j] = 1; j = p[j]; L += 1
            s += L - 1
    return (-1) ** s
for nm, i in (("2a", i2a), ("4a", i4a)):
    g7 = tuple(list(reps[i]) + [6])
    wit = None
    for q in permutations(range(7)):
        if mul(q, g7) == mul(g7, q) and sgn7(q) == -1:
            wit = q; break
    say("  A_6 %s -> A_7 cycle type %s ; odd centralising element %s exists ==> the S_7"
        " class does NOT split, so A_7 has ONE class of this type" % (nm, ctype(g7), wit))
    assert wit is not None
say("  ==> the fusion is one-to-one; the transfer lemma is confirmed.")
say("  DIRECTION: the lemma is the inclusion Z_2A_6 subset Z_2A_7.  Witnesses push")
say("  forward; non-existence does NOT pull back.  ONE-DIRECTIONAL.")

hdr("VERIFICATION COMPLETE -- every assertion above passed")
import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_r5_run.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
