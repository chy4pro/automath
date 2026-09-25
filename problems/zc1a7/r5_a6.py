#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROUND 5 BUILDER -- owner-zc1a7.
Target (planner cert_zc1a7_r4 sec.7 ruling): A_6 FIRST.
  Q: does a unit of order 4 with (eps_2a, eps_4a) = (2,-1) exist in V(Z_2 A_6)?

This script does NOT claim to answer that.  It builds, from scratch and exactly:
  PART A  A_6: group, classes, power map, ordinary character table (Dixon mod 421)
  PART B  the 2-blocks of A_6 over F_2 and over F_4, defects, decomposition and
          Cartan matrices, basic-algebra rank; the BLIND-BLOCK census
  PART C  the 2-local HeLP system for |u|=4 and its census, with controls
  PART D  the r3 Z_2C_4 lattice bounds transplanted to A_6, feasibility verdict,
          and the search for a forced NON-ZERO lower bound
  PART E  the A_6 vs A_7 comparison on the object that must actually be attacked
  PART F  the transfer lemma re-checked, and its DIRECTION

Exact arithmetic only: Python integers, Fraction, mod-p integers, Z[phi], F_4.
No floating point.  No SAT.  No search beyond provably bounded enumeration.
Interpreter: .venv/bin/python3 (3.9.6, sympy 1.14.0) -- sympy used only for
polynomial factorisation mod p inside meataxe.py.
"""
from fractions import Fraction
from itertools import combinations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meataxe as MX

OUT = []
def say(s=""):
    print(s)
    OUT.append(s)

def hdr(s):
    say("")
    say("=" * 78)
    say(s)
    say("=" * 78)

# ----------------------------------------------------------------------------
# PART A -- the group
# ----------------------------------------------------------------------------
def pmul(a, b):
    "(a*b)(i) = a(b(i))   -- builder convention"
    return tuple(a[b[i]] for i in range(len(b)))

def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a):
        r[x] = i
    return tuple(r)

def ppow(a, k):
    n = len(a)
    r = tuple(range(n))
    if k < 0:
        a, k = pinv(a), -k
    for _ in range(k):
        r = pmul(r, a)
    return r

def porder(a):
    n = len(a); r = tuple(range(n)); k = 0
    while True:
        r = pmul(r, a); k += 1
        if r == tuple(range(n)):
            return k

def cycle_type(a):
    n = len(a); seen = [False] * n; ct = []
    for i in range(n):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]:
                seen[j] = True; j = a[j]; L += 1
            ct.append(L)
    return tuple(sorted(ct, reverse=True))

def close_group(gens, n):
    ident = tuple(range(n))
    G = {ident}
    frontier = [ident]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = pmul(x, g)
                if y not in G:
                    G.add(y); nf.append(y)
        frontier = nf
    return sorted(G)

def build(n, gens):
    G = close_group(gens, n)
    idx = {g: i for i, g in enumerate(G)}
    # conjugacy classes
    unassigned = set(range(len(G)))
    classes = []
    while unassigned:
        s = min(unassigned)
        orb = set()
        stack = [G[s]]
        orb.add(G[s])
        while stack:
            x = stack.pop()
            for g in G:
                y = pmul(pmul(g, x), pinv(g))
                if y not in orb:
                    orb.add(y); stack.append(y)
        cl = sorted(idx[x] for x in orb)
        classes.append(cl)
        unassigned -= set(cl)
    classes.sort(key=lambda c: (porder(G[c[0]]), len(c), cycle_type(G[c[0]])))
    return G, idx, classes

# ---------------------------------------------------------------------------
hdr("PART A -- A_6 built from scratch, classes, power map, character table")

N6 = 6
GENS6 = [(1, 2, 3, 4, 0, 5), (0, 1, 2, 4, 5, 3)]   # (01234) and (345)
G6, IDX6, CL6 = build(N6, GENS6)
say("|A_6| = %d   (must be 360)" % len(G6))
assert len(G6) == 360
say("number of conjugacy classes = %d" % len(CL6))

clsz = [len(c) for c in CL6]
clrep = [G6[c[0]] for c in CL6]
clord = [porder(r) for r in clrep]
clct = [cycle_type(r) for r in clrep]
cent = [len(G6) // s for s in clsz]
# class index of every element
CLOF6 = [0] * len(G6)
for i, c in enumerate(CL6):
    for x in c:
        CLOF6[x] = i

NAMES6 = []
seen = {}
for i in range(len(CL6)):
    o = clord[i]
    seen[o] = seen.get(o, 0)
    NAMES6.append("%d%s" % (o, "abc"[seen[o]]))
    seen[o] += 1
say("classes  " + "  ".join("%s:size%d:type%s" % (NAMES6[i], clsz[i], clct[i])
                            for i in range(len(CL6))))
assert sum(clsz) == 360

def cls_of(perm):
    return CLOF6[IDX6[perm]]

# power map
POW6 = [[cls_of(ppow(clrep[i], k)) for k in range(13)] for i in range(len(CL6))]
INV6 = [cls_of(pinv(clrep[i])) for i in range(len(CL6))]
say("inverse map on classes: " + str([NAMES6[i] for i in INV6]))

# class-algebra structure constants a_{k l m} BY ACTUAL GROUP MULTIPLICATION
nc = len(CL6)
A = [[[0] * nc for _ in range(nc)] for _ in range(nc)]
for k in range(nc):
    for l in range(nc):
        cnt = [0] * nc
        for x in CL6[k]:
            gx = G6[x]
            for y in CL6[l]:
                cnt[CLOF6[IDX6[pmul(gx, G6[y])]]] += 1
        for m in range(nc):
            # a_{klm} = #{(x,y) in C_k x C_l : xy = fixed z in C_m}
            assert cnt[m] % clsz[m] == 0
            A[k][l][m] = cnt[m] // clsz[m]
say("class-algebra structure constants computed by actual multiplication: OK")

# ---- Dixon's algorithm mod p, p = 421 = 7*60+1  (exp(A_6) = 60 | 420)
P = 421
assert (P - 1) % 60 == 0

# The generic simultaneous-diagonalisation above is overkill; A_6 is tiny, so do it
# concretely: eigen-decompose a single random integer combination of the M_k.
def eig_decompose(nc, A, p, coeffs):
    M = [[sum(coeffs[k] * A[k][l][m] for k in range(nc)) % p for m in range(nc)]
         for l in range(nc)]
    # omega is a RIGHT eigenvector of M_k:  sum_m a_{klm} omega(m) = omega(k) omega(l)
    spaces = {}
    for lam in range(p):
        Mm = [[(M[i][j] - (lam if i == j else 0)) % p for j in range(nc)]
              for i in range(nc)]
        ns = MX.nullspace(Mm, p)
        if ns:
            spaces[lam] = ns
    return spaces

# find a combination that separates all 7 characters
CENTCH = None
for seed in range(1, 200):
    coeffs = [(seed * (k + 1) * (k + 3)) % P for k in range(nc)]
    sp = eig_decompose(nc, A, P, coeffs)
    if len(sp) == nc and all(len(v) == 1 for v in sp.values()):
        CENTCH = [v[0] for v in sp.values()]
        break
assert CENTCH is not None, "no separating combination found"
say("Dixon mod %d: %d one-dimensional common eigenspaces found" % (P, len(CENTCH)))

# normalise omega(1a) = 1   (1a is class 0)
def inv_mod(a, p):
    return pow(a % p, p - 2, p)

OMEGA = []
for v in CENTCH:
    c = inv_mod(v[0], P)
    OMEGA.append([(x * c) % P for x in v])
# omega_chi(k) = |C_k| chi(g_k) / chi(1);  chi(1)^2 = |G| / sum_k omega(k)omega(k*)/|C_k|
def sym(x, p):
    x %= p
    return x - p if x > p // 2 else x

TAB = []           # exact character values on all classes (rational entries only)
DEG = []
for om in OMEGA:
    s = 0
    for k in range(nc):
        s = (s + om[k] * om[INV6[k]] % P * inv_mod(clsz[k], P)) % P
    d2 = 360 % P * inv_mod(s, P) % P
    # chi(1) is a positive integer <= 19 dividing |G|
    deg = None
    for d in range(1, 20):
        if (d * d) % P == d2 and 360 % d == 0:
            deg = d
    assert deg is not None
    DEG.append(deg)
    row = [sym(deg * om[k] % P * inv_mod(clsz[k], P) % P, P) for k in range(nc)]
    TAB.append(row)

order = sorted(range(nc), key=lambda i: (DEG[i], TAB[i]))
TAB = [TAB[i] for i in order]; DEG = [DEG[i] for i in order]
OMEGA = [OMEGA[i] for i in order]

say("degrees: %s   sum of squares = %d" % (DEG, sum(d * d for d in DEG)))
assert sum(d * d for d in DEG) == 360

# which entries are genuinely irrational?  a class C is rational iff g ~ g^j for all
# j coprime to |g|.  Compute; the mod-p symmetric lift is only valid on rational entries.
import math
rational_class = []
for i in range(nc):
    o = clord[i]
    ok = all(POW6[i][j] == i for j in range(1, o) if math.gcd(j, o) == 1)
    rational_class.append(ok)
say("rational classes: " + str([NAMES6[i] for i in range(nc) if rational_class[i]]))
say("irrational (Galois-moved) classes: " +
    str([NAMES6[i] for i in range(nc) if not rational_class[i]]))

# verify orthogonality using only rational columns + the known structure of the
# irrational pair.  First: the 5a/5b entries of the two degree-8 characters.
IRR = [i for i in range(nc) if not rational_class[i]]
say("")
say("ordinary character table of A_6 (Dixon mod %d, symmetric lift):" % P)
say("        " + "".join("%6s" % NAMES6[i] for i in range(nc)))
for r, row in enumerate(TAB):
    say("chi%-4d " % (r + 1) + "".join("%6s" % row[i] for i in range(nc)))
say("  (entries on the Galois-moved classes %s are only correct where the value is"
    % [NAMES6[i] for i in IRR])
say("   rational; the two degree-8 characters are treated symbolically below.)")

# ---- controls on the table ------------------------------------------------
# rational-class column orthogonality with itself
ok = True
for k in range(nc):
    if not rational_class[k]:
        continue
    s = sum(TAB[r][k] * TAB[r][INV6[k]] for r in range(nc))
    if s != cent[k]:
        ok = False
        say("  column orthogonality FAILS at %s: %d vs |C| = %d" % (NAMES6[k], s, cent[k]))
say("C1 column orthogonality on rational classes: %s" % ("OK" if ok else "FAIL"))

# class-algebra control: omega_i(k) omega_i(l) = sum_m a_klm omega_i(m)  (mod P)
bad = 0
for i in range(nc):
    for k in range(nc):
        for l in range(nc):
            lhs = OMEGA[i][k] * OMEGA[i][l] % P
            rhs = sum(A[k][l][m] * OMEGA[i][m] for m in range(nc)) % P
            if lhs != rhs:
                bad += 1
say("C2 class-algebra identity omega(k)omega(l) = sum a_klm omega(m): %d failures out of %d"
    % (bad, nc ** 3))
assert bad == 0

# permutation character control: 6 points, and 15 pairs
def perm_char(action_size, act):
    return [sum(1 for x in range(action_size) if act(clrep[i], x) == x) for i in range(nc)]

pi6 = perm_char(6, lambda g, x: g[x])
pairs = list(combinations(range(6), 2))
pidx = {p: i for i, p in enumerate(pairs)}
pi15 = perm_char(15, lambda g, x: pidx[tuple(sorted((g[pairs[x][0]], g[pairs[x][1]])))])
say("C3 permutation characters (counted fixed points): pi_6 = %s, pi_15 = %s" % (pi6, pi15))

def inner(a, b):
    s = Fraction(0)
    for k in range(nc):
        s += Fraction(clsz[k] * a[k] * b[INV6[k]], 1)
    return s / 360

def decompose(pc):
    return [inner(pc, TAB[r]) for r in range(nc)]

d6 = decompose(pi6); d15 = decompose(pi15)
say("    pi_6  = %s" % [str(x) for x in d6])
say("    pi_15 = %s" % [str(x) for x in d15])
assert all(x.denominator == 1 and x >= 0 for x in d6)
assert all(x.denominator == 1 and x >= 0 for x in d15)
say("C3 both decompose with non-negative integer multiplicities: OK")

# name the classes we need
i1a = 0
i2a = [i for i in range(nc) if clord[i] == 2][0]
i4a = [i for i in range(nc) if clord[i] == 4][0]
i3 = [i for i in range(nc) if clord[i] == 3]
i5 = [i for i in range(nc) if clord[i] == 5]
say("")
say("classes used: 1a=%s  2a=%s(size %d)  4a=%s(size %d)  order3=%s  order5=%s" %
    (NAMES6[i1a], NAMES6[i2a], clsz[i2a], NAMES6[i4a], clsz[i4a],
     [NAMES6[i] for i in i3], [NAMES6[i] for i in i5]))
assert clsz[i2a] == 45 and clsz[i4a] == 90
say("power map: (4a)^2 = %s  -- the square of an order-4 element" % NAMES6[POW6[i4a][2]])
assert POW6[i4a][2] == i2a

say("")
say("values on (1a, 2a, 4a):")
for r in range(nc):
    say("  chi%d  deg %2d   chi(2a) = %3d   chi(4a) = %3d   %s" %
        (r + 1, DEG[r], TAB[r][i2a], TAB[r][i4a],
         "BLIND (chi(2a)=chi(4a))" if TAB[r][i2a] == TAB[r][i4a] else "distinguishes"))

# ----------------------------------------------------------------------------
hdr("PART B -- the 2-blocks of A_6: defects, decomposition, Cartan, BLIND census")
# ----------------------------------------------------------------------------
# exact central characters omega_chi(k) = |C_k| chi(g_k)/chi(1) in Z[phi], phi^2=phi+1
# (phi = (1+sqrt5)/2).  Only the two degree-8 characters are irrational, and only on
# the two order-5 classes.  Their values there are the roots of x^2 - x - 1 = 0:
i5a, i5b = i5
sq = TAB[3][i5a] * TAB[3][i5b] % P
sm = (TAB[3][i5a] + TAB[3][i5b]) % P
say("degree-8 characters on the order-5 classes: mod-%d lift gives sum = %d, product = %d"
    % (P, sym(sm, P), sym(sq, P)))
assert sym(sm, P) == 1 and sym(sq, P) == -1
say("  => the pair of values are the two roots of x^2 - x - 1, i.e. phi and 1-phi,")
say("     phi = (1+sqrt5)/2.  Carried SYMBOLICALLY from here on -- no mod-p lift used.")

def omega_exact(r, k):
    """returns (a,b) meaning a + b*phi ; exact"""
    if DEG[r] == 8 and k in (i5a, i5b):
        # chi(5a) = phi (for one of them), 1-phi for the other
        first = (r == 3)
        if (k == i5a) == first:
            num = (0, clsz[k])          # |C| * phi
        else:
            num = (clsz[k], -clsz[k])   # |C| * (1 - phi)
        assert num[0] % DEG[r] == 0 and num[1] % DEG[r] == 0
        return (num[0] // DEG[r], num[1] // DEG[r])
    v = clsz[k] * TAB[r][k]
    assert v % DEG[r] == 0, (r, k, v, DEG[r])
    return (v // DEG[r], 0)

OM = [[omega_exact(r, k) for k in range(nc)] for r in range(nc)]
say("all omega_chi(C) are algebraic integers of Z[phi]: OK  (divisibility asserted)")

# reduce modulo a prime above 2.  2 is INERT in Q(sqrt5) (5 = 5 mod 8), residue field F_4.
F4 = {(0, 0): "0", (1, 0): "1", (0, 1): "w", (1, 1): "1+w"}
OMBAR = [[(a % 2, b % 2) for (a, b) in row] for row in OM]
blocks = []
for r in range(nc):
    placed = False
    for B in blocks:
        if OMBAR[r] == OMBAR[B[0]]:
            B.append(r); placed = True; break
    if not placed:
        blocks.append([r])
say("")
say("2-blocks over F_4 (Osima: chi ~ psi iff omega_chi = omega_psi mod (2)):")
for bi, B in enumerate(blocks):
    say("  block %d : Irr = %s   degrees %s" %
        (bi, ["chi%d" % (r + 1) for r in B], [DEG[r] for r in B]))
say("  number of 2-blocks over F_4 = %d" % len(blocks))

# over F_2 the Frobenius x -> x^2 of F_4 fuses Galois-conjugate blocks
def frob(row):
    # Frobenius on F_4: (a + b w)^2 = a + b w^2 = a + b(1+w) = (a+b) + b w
    return [((a + b) % 2, b % 2) for (a, b) in row]
f2blocks = []
used = set()
for bi, B in enumerate(blocks):
    if bi in used:
        continue
    grp = [bi]; used.add(bi)
    for bj in range(len(blocks)):
        if bj not in used and OMBAR[blocks[bj][0]] == frob(OMBAR[B[0]]):
            grp.append(bj); used.add(bj)
    f2blocks.append(grp)
say("  number of 2-blocks over F_2 = %d   (Frobenius orbits: %s)" %
    (len(f2blocks), f2blocks))

# defect: d(B) = nu_2(|G|) - min_{chi in B} nu_2(chi(1))
def nu2(x):
    k = 0
    while x % 2 == 0:
        x //= 2; k += 1
    return k
nu2G = nu2(360)
say("")
say("nu_2(|A_6|) = %d" % nu2G)
DEFECT = []
for bi, B in enumerate(blocks):
    d = nu2G - min(nu2(DEG[r]) for r in B)
    DEFECT.append(d)
    say("  block %d: defect %d  (|D| = %d)" % (bi, d, 2 ** d))

# Sylow 2-subgroup: identify it
syl = None
for x in G6:
    if porder(x) == 4:
        for y in G6:
            if porder(y) == 2:
                H = close_group([x, y], 6)
                if len(H) == 8:
                    syl = H; break
        if syl: break
o4 = sum(1 for x in syl if porder(x) == 4)
o2 = sum(1 for x in syl if porder(x) == 2)
abelian = all(pmul(a, b) == pmul(b, a) for a in syl for b in syl)
say("Sylow 2-subgroup of A_6: order %d, %d elements of order 2, %d of order 4, abelian=%s"
    % (len(syl), o2, o4, abelian))
say("  => D_8 (dihedral): Q_8 would have 6 elements of order 4, C_2xC_4 would be abelian,")
say("     C_2^3 would have no element of order 4.  DIHEDRAL OF ORDER 8.")
assert len(syl) == 8 and o4 == 2 and o2 == 5 and not abelian

say("")
say("GREEN'S THEOREM CONTROL (zeros of characters):")
say("  a block of defect 0 has all its characters vanishing on every 2-singular class.")
for bi, B in enumerate(blocks):
    vals = [(("chi%d" % (r + 1)), TAB[r][i2a], TAB[r][i4a]) for r in B]
    say("  block %d (defect %d): (chi(2a), chi(4a)) = %s" %
        (bi, DEFECT[bi], [(v[1], v[2]) for v in vals]))
say("  the two defect-0 blocks vanish on BOTH 2-singular classes; the defect-3 block")
say("  does not  => the control DISCRIMINATES.")

say("")
say("*** BLIND-BLOCK CENSUS (which blocks can obstruct at all) ***")
say("A block B all of whose characters satisfy chi(2a) = chi(4a) is satisfied by")
say("u_B = e_B g for a genuine g in 4a, and can NEVER obstruct.")
canobstruct = []
for bi, B in enumerate(blocks):
    blind = all(TAB[r][i2a] == TAB[r][i4a] for r in B)
    say("  block %d  %s  : %s" % (bi, [DEG[r] for r in B], "BLIND" if blind else "CAN OBSTRUCT"))
    if not blind:
        canobstruct.append(bi)
say("  ==> of %d 2-blocks of A_6 over F_4, %d can obstruct and %d cannot."
    % (len(blocks), len(canobstruct), len(blocks) - len(canobstruct)))
# and over Z_2 itself -- the ring the unit actually lives in.  Idempotents lift from
# F_2 G, so the Z_2-blocks are the F_2-blocks: the two defect-0 blocks are fused.
f2can = 0
for grp in f2blocks:
    rs = [r for bi in grp for r in blocks[bi]]
    if not all(TAB[r][i2a] == TAB[r][i4a] for r in rs):
        f2can += 1
say("  ==> of %d 2-blocks of A_6 over Z_2 (= over F_2, idempotents lift), %d can obstruct."
    % (len(f2blocks), f2can))
say("      Either way it is ONE block.  A_7 has 2 of 2 in both counts (r4).")
assert f2can == 1

# ---- 2-modular irreducibles, decomposition matrix, Cartan matrix -----------
say("")
say("--- 2-modular irreducibles of A_6, built as explicit F_2-modules ---")
regular2 = [i for i in range(nc) if clord[i] % 2 == 1]
say("2-regular classes: %s   (#IBr over a splitting field = %d, Brauer)"
    % ([NAMES6[i] for i in regular2], len(regular2)))
# Berman: #irreducible F_2 A_6-modules = #orbits of 2-regular classes under g -> g^2
orb = []
usedc = set()
for i in regular2:
    if i in usedc: continue
    o = [i]; usedc.add(i); j = POW6[i][2]
    while j not in usedc:
        o.append(j); usedc.add(j); j = POW6[j][2]
    orb.append(o)
say("Berman: orbits of 2-regular classes under squaring = %s  => %d irreducible F_2-modules"
    % ([[NAMES6[i] for i in o] for o in orb], len(orb)))

def perm_matrices(action_size, act, gens_of_G):
    mats = []
    for g in gens_of_G:
        M = [[0] * action_size for _ in range(action_size)]
        for x in range(action_size):
            M[act(g, x)][x] = 1
        mats.append(M)
    return mats

# 6-point action (natural)
nat_gens = perm_matrices(6, lambda g, x: g[x], GENS6)
# second 6-point action: cosets of a TRANSITIVE A_5 (PSL(2,5) on P^1(F_5), inf = 5)
Ht = close_group([(1, 2, 3, 4, 0, 5), (5, 4, 2, 3, 1, 0)], 6)   # (01234) and (0 5)(1 4)
say("transitive A_5 <= A_6 : order %d, transitive = %s"
    % (len(Ht), len(set(h[0] for h in Ht)) == 6))
assert len(Ht) == 60 and len(set(h[0] for h in Ht)) == 6
Hset = set(Ht)
cosets = []
seen_el = set()
for g in G6:
    if g in seen_el: continue
    c = frozenset(pmul(g, h) for h in Ht)
    cosets.append(c); seen_el |= c
assert len(cosets) == 6
cid = {c: i for i, c in enumerate(cosets)}
def coset_act(g, x):
    rep = next(iter(cosets[x]))
    return cid[frozenset(pmul(pmul(g, rep), h) for h in Ht)]
alt_gens = perm_matrices(6, coset_act, GENS6)
say("second 6-point action built from the cosets of that transitive A_5")

def four_dim(gens6):
    "sum-zero subspace of F_2^6 modulo the all-ones vector -> 4-dimensional"
    p = 2
    S = [[1 if j in (0, i) else 0 for j in range(6)] for i in range(1, 6)]  # e_0+e_i
    gsub = MX.restrict(gens6, S, p)
    ones = [1, 1, 1, 1, 1]        # e_0+e_1 + ... + e_0+e_5 = sum e_j (6 even) -> all-ones
    Q = MX.quotient(gsub, [ones], p)
    return Q
M4a = four_dim(nat_gens)
M4b = four_dim(alt_gens)
say("two 4-dimensional F_2 A_6-modules built (dims %d, %d)" % (len(M4a[0]), len(M4b[0])))
for nm, M in (("4a", M4a), ("4b", M4b)):
    _res = MX.find_submodule(M, 2, tries=40, seed=7)
    irr = (_res[0] == "irreducible")
    e = MX.hom_dim(M, M, 2)[0]
    say("  module %s: Norton criterion (an IFF) says irreducible = %s ; dim End_{F_2} = %d"
        % (nm, irr, e))
    assert irr and e == 1

# words in the generators, so every group element has an explicit matrix
WORD = {tuple(range(6)): []}
frontier = [tuple(range(6))]
while frontier:
    nf = []
    for x in frontier:
        for gi, g in enumerate(GENS6):
            y = pmul(x, g)
            if y not in WORD:
                WORD[y] = WORD[x] + [gi]; nf.append(y)
    frontier = nf
assert len(WORD) == 360

def mat_of(gens, perm, p=2):
    n = len(gens[0][0])
    M = MX.mat_id(n)
    for gi in WORD[perm]:
        M = MX.mat_mul(M, gens[gi], p)
    return M

def mobius(m):
    r, x, k = 1, m, 2
    if m == 1: return 1
    d = 2; res = 1; mm = m
    while d * d <= mm:
        if mm % d == 0:
            mm //= d
            if mm % d == 0: return 0
            res = -res
        d += 1
    if mm > 1: res = -res
    return res

def totient(m):
    return sum(1 for k in range(1, m + 1) if __import__("math").gcd(k, m) == 1)

def brauer_value(gens, perm, m):
    """Brauer character value at an element of ODD order m, by factoring the
       characteristic polynomial over F_2.  Asserts every Frobenius orbit of roots
       is a FULL Galois orbit, so the value is rational and no embedding is chosen."""
    M = mat_of(gens, perm, 2)
    n = len(M)
    # characteristic polynomial via the minimal polynomials on a spanning set is
    # fiddly; use the determinant of (xI - M) over F_2[x] by fraction-free Gauss:
    # instead, factor x^m - 1 and read multiplicities from nullity of f(M)^k.
    total = 0; used = 0
    for d in range(1, m + 1):
        if m % d: continue
        # roots of order exactly d
        pass
    # multiplicity of each irreducible factor f of x^m-1 : dim ker f(M) / deg f
    xm = [0] * (m + 1); xm[m] = 1; xm[0] = 1          # x^m - 1 = x^m + 1 over F_2
    facs = MX.factor_modp(xm, 2)
    for f, e in facs:
        FM = MX.poly_eval_mat(f, M, 2)
        k = len(MX.nullspace(FM, 2))
        assert k % (len(f) - 1) == 0
        mult = k // (len(f) - 1)
        deg = len(f) - 1
        # order of the roots of f
        m2 = None
        for d in range(1, m + 1):
            if m % d == 0:
                xd = [0] * (d + 1); xd[d] = 1; xd[0] = 1
                # f | x^d - 1 ?
                q = MX.poly_eval_mat(f, [[0]], 2)   # placeholder, use poly division below
                m2 = m2
        # determine order by evaluating on the companion: cheaper -- the roots have
        # order d where d is minimal with f | x^d + 1; test by polynomial remainder
        def polymod(a, b, p):
            a = a[:]
            db = len(b) - 1
            inv = pow(b[-1], p - 2, p)
            while len(a) - 1 >= db and any(a):
                c = a[-1] * inv % p
                sh = len(a) - 1 - db
                for i in range(db + 1):
                    a[sh + i] = (a[sh + i] - c * b[i]) % p
                while len(a) > 1 and a[-1] == 0:
                    a.pop()
            return a
        ordr = None
        for d in range(1, m + 1):
            if m % d: continue
            xd = [0] * (d + 1); xd[d] = 1; xd[0] = 1
            if all(c == 0 for c in polymod(xd, f, 2)):
                ordr = d; break
        assert ordr is not None
        assert deg == totient(ordr), (deg, ordr)   # 2 is a primitive root mod ordr
        total += mult * mobius(ordr)
        used += mult * deg
    assert used == n, (used, n)
    return total

MODS = {"1": [MX.mat_id(1) for _ in GENS6], "4a": M4a, "4b": M4b}
say("")
say("Brauer characters of the principal-block simples on the 2-regular classes")
say("        " + "".join("%6s" % NAMES6[i] for i in regular2))
PHI = {}
for nm in ("1", "4a", "4b"):
    row = [brauer_value(MODS[nm], clrep[i], clord[i]) for i in regular2]
    PHI[nm] = row
    say("  %-4s" % nm + "".join("%6d" % v for v in row))
say("  (all values RATIONAL: every Frobenius orbit of roots is a full Galois orbit,")
say("   asserted in code -- so NO embedding mu_5(F_2bar) -> C is chosen.)")

# decomposition matrix of the principal block
prin = blocks[0]
say("")
say("decomposition matrix of the principal 2-block (solved, and UNIQUENESS asserted):")
import itertools as _it
DEC = {}
for r in prin:
    target = [TAB[r][i] for i in regular2]
    sols = []
    for a in range(0, 12):
        for b in range(0, 12):
            for c in range(0, 12):
                if all(a * PHI["1"][j] + b * PHI["4a"][j] + c * PHI["4b"][j] == target[j]
                       for j in range(len(regular2))):
                    sols.append((a, b, c))
    assert len(sols) == 1, (r, sols)
    DEC[r] = sols[0]
    say("  chi%d (deg %2d) = %d*[1] + %d*[4a] + %d*[4b]" % (r + 1, DEG[r], *sols[0]))
say("  every decomposition exists and is UNIQUE over the box [0,11]^3.")

CART = [[sum(DEC[r][i] * DEC[r][j] for r in prin) for j in range(3)] for i in range(3)]
say("")
say("Cartan matrix of the principal 2-block of A_6 = D^T D =")
for row in CART:
    say("      " + str(row))
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
say("  det = %d  (must be 2^defect = %d)" % (det3(CART), 2 ** DEFECT[0]))
assert det3(CART) == 2 ** DEFECT[0]
say("  k(B) = %d ordinary characters, l(B) = %d simple modules" % (len(prin), 3))
basic_rank = sum(sum(r) for r in CART)
blk_rank = sum(DEG[r] ** 2 for r in prin)
say("  Z_2-rank of the block        = sum chi(1)^2 = %d" % blk_rank)
say("  Z_2-rank of its BASIC ALGEBRA = sum C_ij     = %d" % basic_rank)
simple_dims = [1, 4, 4]
say("  consistency  sum n_i n_j c_ij = %d  (must equal the block rank %d)" %
    (sum(simple_dims[i] * simple_dims[j] * CART[i][j] for i in range(3) for j in range(3)),
     blk_rank))
assert sum(simple_dims[i] * simple_dims[j] * CART[i][j] for i in range(3) for j in range(3)) == blk_rank

# ----------------------------------------------------------------------------
hdr("PART C -- the 2-local HeLP system for |u| = 4 in V(Z_2 A_6), with census")
# ----------------------------------------------------------------------------
say("Admissibility 2-locally (r4 sec.2, re-derived here):")
say("  * Luthar-Passi for ORDINARY characters survives: D(u) is diagonalisable over")
say("    Qbar_2 with 4th-root-of-unity eigenvalues, so mu(zeta^-j,u,chi) is a")
say("    non-negative rational integer.")
say("  * p-Brauer characters for p = 3, 5 do NOT: they enter through Z_p G -> F_p G,")
say("    and a unit of V(Z_2 A_6) admits no such reduction.")
say("  * Hertweck's congruence AT p = 2 survives (Frobenius congruence over Z_2).")
say("  * support {2a,4a} is SPECIFIED by the question (r4 sec.2 flagged that the")
say("    Z_2-analogues of Berman-Higman and of Hertweck's ord(C)|n were not verified;")
say("    nothing below rests on them, because the support is a hypothesis here).")

def mults(deg, chi2a, chiu):
    """eigenvalue multiplicities of u (order 4, u^2 ~ 2a) on a character of degree deg"""
    m0 = Fraction(deg + 2 * chiu + chi2a, 4)
    m1 = Fraction(deg - chi2a, 4)
    m2 = Fraction(deg + chi2a - 2 * chiu, 4)
    return (m0, m1, m2, m1)

def helprow(r, t):
    chiu = t * TAB[r][i2a] + (1 - t) * TAB[r][i4a]
    return mults(DEG[r], TAB[r][i2a], chiu)

say("")
say("enumeration over t = eps_2a(u) in [-6,6] (boundedness PROVED below, not assumed):")
surv_ord, surv_all = [], []
detail = {}
for t in range(-6, 7):
    killers = []
    for r in range(nc):
        mm = helprow(r, t)
        for j, v in enumerate(mm):
            if v < 0 or v.denominator != 1:
                killers.append("chi%d:mu%d=%s" % (r + 1, j, v))
    cong_ok = ((1 - t) - 1) % 2 == 0      # eps_4a(u) = eps_2a(u^2) = 1 mod 2
    detail[t] = (killers, cong_ok)
    if not killers:
        surv_ord.append(t)
        if cong_ok:
            surv_all.append(t)
for t in range(-6, 7):
    k, c = detail[t]
    say("  t = %+d : ordinary kills = %-2d %-42s congruence %s  %s"
        % (t, len(k), ("[" + ", ".join(k[:3]) + ("...]" if len(k) > 3 else "]")) if k else "",
           "OK " if c else "NO ", "SURVIVES" if (not k and c) else ""))
say("")
say("  boundedness PROOF (not an assumption): chi7 (deg 10, chi(2a) = -2, chi(4a) = 0)")
say("     gives mu_0 = 2 - t >= 0 and mu_2 = 2 + t >= 0, i.e. |t| <= 2.")
say("  2-LOCAL admissible set for A_6:  eps_2a(u) in %s" % surv_all)
say("  i.e. (eps_2a, eps_4a) in %s" % [(t, 1 - t) for t in surv_all])
assert surv_all == [0, 2]

say("")
say("CONTROLS:")
say("  positive: t = 0 must be admissible -- it is realised by a genuine g in 4a.")
for r in range(nc):
    mm = helprow(r, 0)
    assert all(v >= 0 and v.denominator == 1 for v in mm)
say("            all 28 multiplicities at t = 0 are non-negative integers: OK")
say("  rejection: t = +-3, +-4 killed by ordinary characters (%d, %d, %d, %d constraints);"
    % (len(detail[3][0]), len(detail[-3][0]), len(detail[4][0]), len(detail[-4][0])))
say("             t = -2 killed by ordinary characters (%d constraints);" % len(detail[-2][0]))
say("             t = +-1 ordinary-admissible and killed ONLY by the p=2 congruence")
say("             (%d, %d ordinary kills) -- so the congruence is not idle."
    % (len(detail[1][0]), len(detail[-1][0])))
say("  the -2 killers are: %s" % detail[-2][0])

say("")
say("*** CENSUS (sec.90/104) -- the number I am entitled to ***")
disc = [r for r in range(nc) if TAB[r][i2a] != TAB[r][i4a]]
say("  ordinary system: %d characters x 4 eigenvalues = %d constraints." % (nc, 4 * nc))
say("  mu_1 and mu_3 never depend on t; mu_0 and mu_2 depend on t only when")
say("  chi(2a) != chi(4a).  Discriminating characters: %s" % ["chi%d" % (r + 1) for r in disc])
say("  ==> exactly %d of the %d ordinary constraints could have killed (2,-1). None did."
    % (2 * len(disc), 4 * nc))
say("  LIMITATION printed beside the number: the complete 3- and 5-modular tables of A_6")
say("  were NOT recomputed this round (r4 banked them), so I do NOT state how many odd-p")
say("  Brauer constraints are lost on 2-localisation.  What is re-run below is the single")
say("  GLOBAL killer, because it is load-bearing.")

say("")
say("--- C.2  IS THE SUPPORT HYPOTHESIS {2a,4a} FORCED 2-LOCALLY?  Complete enumeration ---")
say("Over Z G a partial augmentation is a RATIONAL INTEGER and Hertweck's ord(C)|n cuts")
say("the support down to {2a,4a}.  Over Z_2 G neither is available: eps_C(u) is a sum of")
say("Z_2-coefficients, hence a 2-ADIC integer.  So the honest 2-local parameter space is")
say("not Z^7.  Here is what it actually is, computed.")
say("")
say("Step 1.  Every mu(zeta^-j, u, chi) is a non-negative RATIONAL integer, and")
say("chi(u) = mu_0 - mu_2, so chi(u) in Z for every ordinary chi.  With u^2 ~ 2a")
say("(the same hypothesis r4 and sec.3 use) mu_1 = mu_3 = (chi(1)-chi(2a))/4 is FIXED and")
say("mu_0 + mu_2 = chi(1) - 2 mu_1, so chi(u) runs over a finite arithmetic progression.")
opts = []
for r in range(nc):
    m1 = (DEG[r] - TAB[r][i2a])
    assert m1 % 4 == 0
    m1 //= 4
    tot = DEG[r] - 2 * m1
    vals = [tot - 2 * k for k in range(tot + 1)]
    if r == 0:
        vals = [1]                      # trivial character: chi(u) = augmentation = 1
    opts.append(vals)
    say("   chi%d (deg %2d): mu_1 = %d, chi(u) in %s" % (r + 1, DEG[r], m1, vals))
tot_box = 1
for v in opts:
    tot_box *= len(v)
say("   box size = %d  (finite and PROVED finite, not assumed)" % tot_box)

say("")
say("Step 2.  eps_C = (1/|C_G(g_C)|) sum_chi chi(u) chi(g_C^-1), an identity in Qbar_2.")
say("   2 is INERT in Q(sqrt5), so sqrt5 is not in Q_2 and Q(sqrt5) cap Q_2 = Q inside")
say("   Q_2(sqrt5).  eps_C lies in Z_2, hence in Q, hence its phi-part must VANISH.")
say("   For A_6 that reduces to the single condition chi4(u) = chi5(u).")
say("   Then eps_C in Z_2 means: eps_C rational with ODD denominator.")
from fractions import Fraction as Fr
def eps_vector(cu):
    """returns list of (rational part, phi part) as Fractions"""
    out = []
    for k in range(nc):
        a = Fr(0); b = Fr(0)
        for r in range(nc):
            if DEG[r] == 8 and k in (i5a, i5b):
                first = (r == 3)
                if (k == i5a) == first:
                    va, vb = 0, 1                 # phi
                else:
                    va, vb = 1, -1                # 1 - phi
            else:
                va, vb = TAB[r][k], 0
            a += cu[r] * va; b += cu[r] * vb
        out.append((Fr(a, cent[k]), Fr(b, cent[k])))
    return out
import itertools as _itt
res_all, res_z2, res_supp, res_int = 0, [], [], []
for cu in _itt.product(*opts):
    if cu[3] != cu[4]:
        continue                                  # phi-part of eps_5a/5b must vanish
    res_all += 1
    ev = eps_vector(cu)
    if any(b != 0 for (a, b) in ev):
        continue
    if any(a.denominator % 2 == 0 for (a, b) in ev):
        continue                                  # eps must be a 2-ADIC integer
    e = [a for (a, b) in ev]
    assert sum(e) == 1
    res_z2.append((cu, e))
    if all(e[k] == 0 for k in range(nc) if k not in (i2a, i4a)):
        res_supp.append((cu, e))
    if all(x.denominator == 1 for x in e):
        res_int.append((cu, e))
# Hertweck's congruence at p = 2 (r4: it survives over Z_2), applied to u^2 ~ 2a:
#   for every class D,   sum_{C : C^2 subset D} eps_C(u)  ==  eps_D(u^2)  (mod 2)
def congruence_ok(e):
    for D in range(nc):
        lhs = sum(e[C] for C in range(nc) if POW6[C][2] == D)
        rhs = 1 if D == i2a else 0
        num = lhs - rhs
        if num.denominator % 2 == 0 or num.numerator % 2 != 0:
            return False
    return True
res_cong = [(cu, e) for (cu, e) in res_z2 if congruence_ok(e)]
res_cong_int = [(cu, e) for (cu, e) in res_cong if all(x.denominator == 1 for x in e)]
res_cong_supp = [(cu, e) for (cu, e) in res_cong
                 if all(e[k] == 0 for k in range(nc) if k not in (i2a, i4a))]
say("")
say("   candidates with chi4(u) = chi5(u)                        : %5d" % res_all)
say("   ... with every eps_C a 2-ADIC INTEGER (odd denominator)  : %5d" % len(res_z2))
say("   ... and satisfying the p=2 Hertweck congruence            : %5d" % len(res_cong))
say("   ...... of those, eps a RATIONAL INTEGER vector            : %5d" % len(res_cong_int))
say("   ...... of those, SUPPORT contained in {2a,4a}             : %5d" % len(res_cong_supp))
say("")
say("   the integral ones, in full (these are the vectors an argument over Z G would see):")
for cu, e in sorted(res_cong_int, key=lambda x: [int(v) for v in x[1]]):
    supp = {NAMES6[k]: int(e[k]) for k in range(nc) if e[k] != 0}
    say("     chi(u) = %-26s eps = %-34s %s" % (str(list(cu)), str(supp),
        "<-- support {2a,4a}" if all(e[k] == 0 for k in range(nc)
                                     if k not in (i2a, i4a)) else ""))
say("")
say("   three NON-INTEGRAL survivors, exhibited (denominators are odd, so they are")
say("   genuine 2-adic integers and the Luthar-Passi system cannot see them):")
shown = 0
for cu, e in res_cong:
    if all(x.denominator == 1 for x in e):
        continue
    say("     chi(u) = %-26s eps = %s" % (str(list(cu)),
        {NAMES6[k]: str(e[k]) for k in range(nc) if e[k] != 0}))
    shown += 1
    if shown == 3:
        break
say("")
say("   ==> THE SUPPORT HYPOTHESIS IS NOT FORCED 2-LOCALLY, and the parameter space is")
say("       not Z^7 either: over Z_2 G a partial augmentation is a 2-ADIC integer, so the")
say("       enumeration lives in Z_(2)^7 (rationals with odd denominator).")
say("       This is a SCOPING correction to the r4/r5 framing: '(2,-1) in V(Z_2 A_6)' is")
say("       a HYPOTHESIS about the support and the integrality, not a derived restriction.")
say("       It does not change any result above -- every one of them takes the support as")
say("       given -- but it says what a support-free 2-local attack would have to handle.")
say("       (counts: %d survive, %d integral, %d with support {2a,4a})"
    % (len(res_cong), len(res_cong_int), len(res_cong_supp)))
say("   CONTROL (positive): the trivial vector eps_4a = 1, realised by a genuine g in 4a,")
say("       is present: %s" % any(all(e[k] == (1 if k == i4a else 0) for k in range(nc))
                                  for cu, e in res_cong))
say("   CONTROL (the open case): eps = (2,-1) on (2a,4a) is present: %s" % any(
        all(e[k] == ({i2a: 2, i4a: -1}.get(k, 0)) for k in range(nc)) for cu, e in res_cong))
say("   CONTROL (rejection): the enumeration is not vacuous -- %d of the %d candidates"
    % (res_all - len(res_cong), res_all))
say("       with chi4(u) = chi5(u) are rejected.")
say("   ** AND THE TWO EXTRA INTEGRAL VECTORS ARE EXACTLY WHAT HERTWECK'S ord(C)|n KILLS")
say("      OVER Z G: their supports meet the classes 3a/3b and 5a/5b, of orders 3 and 5,")
say("      which do not divide 4.  That theorem's Z_2-analogue is UNVERIFIED (r4 sec.2,")
say("      restated in sec.3 here), so 2-locally they stand. **")

# --- the global killer, RE-RUN from an explicitly constructed F_3-module ----
say("")
say("--- the GLOBAL killer of (2,-1) for A_6, rebuilt and re-run (item (f)) ---")
p3 = 3
nat3 = perm_matrices(6, lambda g, x: g[x], GENS6)
S3 = [[1 if j == 0 else (p3 - 1 if j == i else 0) for j in range(6)]
      for i in range(1, 6)]   # e_0 - e_i : the sum-zero subspace over F_3
g5 = MX.restrict(nat3, S3, p3)
# all-ones = -(e_0-e_1) - ... - (e_0-e_5) + 6 e_0 ; in the basis above its
# coordinate vector is (-1,-1,-1,-1,-1) since 6 = 0 mod 3
M4_3 = MX.quotient(g5, [[p3 - 1] * 5], p3)
say("F_3-module of dimension %d built as (sum-zero subspace of F_3^6)/<all-ones>"
    % len(M4_3[0]))
L2 = []                                          # exterior square, dimension 6
d = len(M4_3[0])
pairs4 = [(a, b) for a in range(d) for b in range(a + 1, d)]
for g in M4_3:
    M = [[0] * len(pairs4) for _ in range(len(pairs4))]
    for cidx, (a, b) in enumerate(pairs4):
        for ridx, (x, y) in enumerate(pairs4):
            M[ridx][cidx] = (g[x][a] * g[y][b] - g[x][b] * g[y][a]) % p3
    L2.append(M)
say("exterior square built explicitly: dimension %d" % len(L2[0]))

def brauer_odd(gens, perm, m, p):
    """Brauer value at an element of order m coprime to p, via char.-poly factorisation."""
    M = mat_of(gens, perm, p)
    n = len(M)
    xm = [0] * (m + 1); xm[m] = 1; xm[0] = -1 % p
    facs = MX.factor_modp(xm, p)
    tot = 0; used = 0
    def polymod(a, b, q):
        a = a[:]; db = len(b) - 1; inv = pow(b[-1], q - 2, q)
        while len(a) - 1 >= db and any(a):
            c = a[-1] * inv % q; sh = len(a) - 1 - db
            for i in range(db + 1):
                a[sh + i] = (a[sh + i] - c * b[i]) % q
            while len(a) > 1 and a[-1] == 0: a.pop()
        return a
    for f, e in facs:
        FM = MX.poly_eval_mat(f, M, p)
        k = len(MX.nullspace(FM, p))
        deg = len(f) - 1
        assert k % deg == 0
        mult = k // deg
        ordr = None
        for dd in range(1, m + 1):
            if m % dd: continue
            xd = [0] * (dd + 1); xd[dd] = 1; xd[0] = -1 % p
            if all(c % p == 0 for c in polymod(xd, f, p)):
                ordr = dd; break
        assert deg == totient(ordr), (deg, ordr, p)
        tot += mult * mobius(ordr); used += mult * deg
    assert used == n
    return tot

phiL2 = [brauer_odd(L2, clrep[k], clord[k], p3) for k in (i1a, i2a, i4a)]
say("its 3-modular Brauer character on (1a, 2a, 4a) = %s   (computed, not quoted)" % phiL2)
assert phiL2 == [6, -2, 2]
for t in (0, 2):
    chiu = t * phiL2[1] + (1 - t) * phiL2[2]
    mm = mults(phiL2[0], phiL2[1], chiu)
    say("   t = %d :  mu = %s   %s" % (t, [str(x) for x in mm],
        "KILLED (mu_0 < 0)" if any(v < 0 for v in mm) else "passes  <-- POSITIVE CONTROL"))
say("  ==> (2,-1) is dead GLOBALLY for A_6 and alive 2-LOCALLY.  Re-run, not read.")

# ----------------------------------------------------------------------------
hdr("PART D -- the r3 Z_2C_4 lattice machinery transplanted to A_6")
# ----------------------------------------------------------------------------
say("Bounds (r3 sec.4, derived there from Berman-Gudkov + the Z_2C_2 classification):")
say("   UB2 = min(m0,m1) + min(m2,m1)      UB3 = min(m0,m1,m2)")
say("   UB1 = n - m1 - max((m0-m1)^+,(m2-m1)^+)     LB1 = m1")
def bounds(n, m0, m1, m2):
    ub2 = min(m0, m1) + min(m2, m1)
    ub1 = n - m1 - max(max(m0 - m1, 0), max(m2 - m1, 0))
    ub3 = min(m0, m1, m2)
    return ub1, ub2, ub3, m1

say("")
say("  chi   deg   m0 m1 m2 |  LB1 UB1 UB2 UB3  |  same for a genuine g in 4a")
BND = {}
for r in range(nc):
    m0, m1, m2, _ = [int(x) for x in helprow(r, 2)]
    b = bounds(DEG[r], m0, m1, m2)
    BND[r] = b
    g0, g1, g2, _ = [int(x) for x in helprow(r, 0)]
    gb = bounds(DEG[r], g0, g1, g2)
    say("  chi%-2d  %3d   %2d %2d %2d |  %3d %3d %3d %3d  |  %3d %3d %3d" %
        (r + 1, DEG[r], m0, m1, m2, b[3], b[0], b[1], b[2], gb[0], gb[1], gb[2]))

# composition factors of Lbar_chi
SIMPLES = ["1", "4a", "4b", "8a", "8b"]
SDIM = [1, 4, 4, 8, 8]
COMP = {}
for r in prin:
    COMP[r] = list(DEC[r]) + [0, 0]
COMP[3] = [0, 0, 0, 1, 0]
COMP[4] = [0, 0, 0, 0, 1]
say("")
say("composition factors of the mod-2 reduction of each ordinary lattice:")
for r in range(nc):
    say("  chi%-2d (deg %2d) -> %s" % (r + 1, DEG[r],
        " + ".join("%d*[%s]" % (COMP[r][i], SIMPLES[i]) for i in range(5) if COMP[r][i])))

say("")
say("*** IS THERE A FORCED NON-ZERO LOWER BOUND?  (r3's banked r_1(S_6) >= 1 for A_7) ***")
say("r3 got r_1(S_6) >= 1 for A_7 because chi_2 (deg 6) reduces to a SINGLE simple with")
say("multiplicity 1 and has m_1 = 1, so LB1 transfers verbatim to that simple.")
forced = []
for r in range(nc):
    nz = [i for i in range(5) if COMP[r][i]]
    if len(nz) == 1 and COMP[r][nz[0]] == 1 and BND[r][3] > 0:
        forced.append((r, SIMPLES[nz[0]], BND[r][3]))
for r in range(nc):
    nz = [i for i in range(5) if COMP[r][i]]
    say("     chi%-2d -> %d distinct simple factor(s), m_1 = %d %s"
        % (r + 1, len(nz), BND[r][3],
           "  <-- SINGLE FACTOR, m_1 > 0: forces r_1(%s) >= %d" % (SIMPLES[nz[0]], BND[r][3])
           if (len(nz) == 1 and COMP[r][nz[0]] == 1 and BND[r][3] > 0) else ""))
say("")
say("  I expected NONE and the search returned TWO.  Correcting the claim rather than")
say("  the search: A_6 DOES get forced non-zero lower bounds, r_1(8a) >= 2 and")
say("  r_1(8b) >= 2 -- but BOTH simples lie in the two DEFECT-0 blocks, which the")
say("  sec.B census already showed to be BLIND (chi(2a) = chi(4a) = 0).  A blind block is")
say("  satisfied by u_B = e_B g for a genuine g in 4a, so a lower bound there is")
say("  automatically consistent and carries no information.")
prin_simples = [0, 1, 2]
forced_prin = [f for f in forced if SIMPLES.index(f[1]) in prin_simples]
say("  ==> in the ONE block that can obstruct, forced non-zero lower bounds: %s"
    % (forced_prin if forced_prin else "NONE"))
say("      A_7, by contrast, has r_1(S_6) >= 1 inside its obstructing Klein-four block.")
say("      On this measure the A_6 instance is STRICTLY WEAKER than the A_7 one.")

say("")
say("FEASIBILITY of the 2-local lattice system at (2,-1): complete enumeration over the")
say("provably bounded box 0 <= r_j(S) <= dim S - 1 (ubar-1 is nilpotent), WITH the two")
say("forced lower bounds imposed.")
from itertools import product
def feasible(j, simples_idx, chars):
    sols = []
    rngs = []
    for i in simples_idx:
        lo = 0
        if j == 1:
            for (r, nm, lb) in forced:
                if SIMPLES.index(nm) == i:
                    lo = max(lo, lb)
        rngs.append(range(lo, SDIM[i]))
    for v in product(*rngs):
        ok = True
        for r in chars:
            lb = sum(COMP[r][simples_idx[k]] * v[k] for k in range(len(simples_idx)))
            if lb > BND[r][j - 1]:
                ok = False; break
        if ok:
            sols.append(v)
    return sols
allS = [0, 1, 2, 3, 4]
for j in (1, 2, 3):
    sols = feasible(j, allS, list(range(nc)))
    say("  FULL system,      j = %d : %d solutions   (all-zero admissible = %s)"
        % (j, len(sols), tuple([0] * 5) in sols))
    assert len(sols) > 0
say("")
say("  and restricted to the ONE block that can obstruct (simples 1, 4a, 4b;")
say("  characters chi1, chi2, chi3, chi6, chi7):")
for j in (1, 2, 3):
    sols = feasible(j, prin_simples, prin)
    say("  PRINCIPAL block,  j = %d : %d solutions   (all-zero admissible = %s)"
        % (j, len(sols), (0, 0, 0) in sols))
    assert (0, 0, 0) in sols
say("  ==> FEASIBLE at every exponent, and the all-zero vector -- the one that makes the")
say("      whole apparatus vacuous -- is admissible in the obstructing block.  The p = 2")
say("      lattice method does NOT settle A_6 either, and the failure is the one r3")
say("      diagnosed for A_7: |u| = 4 and p = 2 give a TRIVIAL 2'-part, the splitting step")
say("      of the lattice method is empty, only upper bounds are produced.")
say("      r3's diagnosis was a CONJECTURE (item (c)).  This is its SECOND instance, on a")
say("      group with a DIFFERENT block structure at p = 2.  It survived the test.")

# --- explicit F_2 ranks for a genuine element: the positive control ---------
say("")
say("POSITIVE CONTROL -- explicit F_2 ranks of a genuine g in 4a and g in 2a:")
g4 = clrep[i4a]; g2 = clrep[i2a]
S2 = [[1 if j in (0, i) else 0 for j in range(6)] for i in range(1, 6)]
Lchi = MX.restrict(nat_gens, S2, 2)     # the 5-dim lattice reduction Lbar_chi3
def ranks_of(gens, perm, name):
    M = mat_of(gens, perm, 2)
    n = len(M)
    I = MX.mat_id(n)
    Z = MX.mat_sub(M, I, 2)
    out = []
    Cur = I
    for j in (1, 2, 3):
        Cur = MX.mat_mul(Cur, Z, 2)
        out.append(MX.rank([row[:] for row in Cur], 2))
    say("    %-22s r_1=%d r_2=%d r_3=%d" % (name, out[0], out[1], out[2]))
    return out
r4a_on_S = ranks_of(Lchi, g4, "g in 4a on Lbar_chi3(5)")
r2a_on_S = ranks_of(Lchi, g2, "g in 2a on Lbar_chi3(5)")
ranks_of(M4a, g4, "g in 4a on simple 4a")
ranks_of(M4b, g4, "g in 4b on simple 4b")
say("    (so the machinery is not vacuous: a real element has non-zero ranks.)")

say("")
say("*** CONSEQUENCE (the A_6 analogue of the sourcing paper's A_7 Proposition) ***")
say("  chi3 has (m0,m1,m2) = %s at (2,-1), so UB2 = %d: rank_F2(ubar^2 - 1) <= %d on the"
    % ([int(x) for x in helprow(2, 2)][:3], BND[2][1], BND[2][1]))
say("  5-dimensional lattice.  A genuine g in 2a has rank_F2(g - 1) = %d there (computed"
    % r2a_on_S[0])
say("  above), and %d < %d, so u^2 is NOT conjugate in Z_2 A_6 to an element of 2a."
    % (BND[2][1], r2a_on_S[0]))
say("  This is exactly the paper's degree-6 argument for A_7, transplanted; it is")
say("  INFORMATION about the hypothetical unit, not a contradiction with it.")
assert BND[2][1] < r2a_on_S[0]

# ----------------------------------------------------------------------------
hdr("PART E -- A_6 vs A_7: the object that must ACTUALLY be attacked")
# ----------------------------------------------------------------------------
say("A_7's block data is BANKED (r4, planner cert sec.2) and is NOT re-derived here.")
say("What IS re-run is every arithmetic step that the comparison rests on (item (f)).")
A7B1 = dict(degs=[6, 10, 10, 14], cart=[[4, 2, 2], [2, 2, 1], [2, 1, 2]],
            sdim=[6, 4, 4], defect=2, name="B_1 (Klein four V_4)")
A7B0 = dict(degs=[1, 14, 15, 21, 35], cart=[[4, 2, 2], [2, 3, 1], [2, 1, 2]],
            sdim=[1, 14, 20], defect=3, name="B_0 (dihedral D_8)")
A6B0 = dict(degs=[DEG[r] for r in prin], cart=CART, sdim=[1, 4, 4],
            defect=DEFECT[0], name="principal (dihedral D_8)")
tot = 0
for nm, B in (("A_7 " + A7B1["name"], A7B1), ("A_7 " + A7B0["name"], A7B0),
              ("A_6 " + A6B0["name"], A6B0)):
    rank = sum(d * d for d in B["degs"])
    basic = sum(sum(r) for r in B["cart"])
    chk = sum(B["sdim"][i] * B["sdim"][j] * B["cart"][i][j]
              for i in range(len(B["sdim"])) for j in range(len(B["sdim"])))
    dt = det3(B["cart"])
    say("  %-28s k(B)=%d l(B)=%d defect=%d det(C)=%d  block rank=%4d  basic rank=%2d  "
        "consistency %s" % (nm, len(B["degs"]), len(B["cart"]), B["defect"], dt,
                            rank, basic, "OK" if chk == rank else "FAIL"))
    assert chk == rank and dt == 2 ** B["defect"]
say("  A_7 block ranks sum to %d = |A_7| : %s" %
    (sum(d * d for d in A7B1["degs"]) + sum(d * d for d in A7B0["degs"]),
     sum(d * d for d in A7B1["degs"]) + sum(d * d for d in A7B0["degs"]) == 2520))
say("  A_6 block ranks sum to %d = |A_6| : %s" %
    (sum(d * d for d in A6B0["degs"]) + 64 + 64,
     sum(d * d for d in A6B0["degs"]) + 128 == 360))

say("")
say("*** THE ORDERING RATIONALE, MEASURED ***")
say("  Non-existence needs a contradiction in ONE block only: u exists iff EVERY block")
say("  B carries a u_B with u_B^4 = e_B and the prescribed character, so a single")
say("  contradictory block finishes it.  Therefore the object to attack is the SMALLEST")
say("  block that can obstruct.")
say("    A_7 : 2 blocks over Z_2 (and 2 split), BOTH obstruct.  Smallest basic algebra: 18")
say("          (B_1, Klein four defect, and by CEKL one of exactly THREE Morita classes).")
say("    A_6 : 2 blocks over Z_2 (3 split), exactly ONE obstructs, the principal one:")
say("          basic algebra rank %d, dihedral D_8 defect." % sum(sum(r) for r in CART))
say("  ==> 'A_6 is smaller' is true of the GROUP (360 < 2520) and FALSE of the object")
say("      that has to be attacked: 34 > 18, by a factor of about 2, and A_6 offers no")
say("      second, smaller site.  The A_6 census is BETTER (1 of 3 vs 2 of 2) and the")
say("      A_6 target is WORSE.")
say("  Citation-level, NOT verified this round: for Klein four defect the Morita")
say("  classification is a finite explicit list of three (CEKL, Math. Z. 268 (2011),")
say("  read at content level in r4).  I have NOT located an equally explicit finite")
say("  Morita list for blocks with D_8 defect and l(B)=3; Erdmann's tame classification")
say("  is by families carrying scalar parameters.  Recorded as a GAP in my knowledge,")
say("  not as a negative about the literature.")
say("  And r4's finding stands, re-derived here: A_6 has NO Klein four block (its only")
say("  non-defect-0 block has defect 3), so the A_6 instance cannot exercise, calibrate")
say("  or inform the CEKL/A_5-type machinery that the A_7 B_1 route needs.")

say("")
say("--- ADDENDUM: A_7's discriminating constraints, PER BLOCK, recovered by running")
say("    the arithmetic on r3's banked (m0,m1,m2) table rather than reading r4's total ---")
# r3 sec.4 banked, for A_7 at (2,-1):  chi -> (deg, m0, m1, m2)
A7 = [("chi1", 1, 1, 0, 0), ("chi2", 6, 4, 1, 0), ("chi3", 10, 0, 3, 4), ("chi4", 10, 0, 3, 4),
      ("chi5", 14, 6, 3, 2), ("chi6", 14, 6, 3, 2), ("chi7", 15, 3, 4, 4),
      ("chi8", 21, 7, 5, 4), ("chi9", 35, 7, 9, 10)]
BLK1 = {"chi2", "chi3", "chi4", "chi5"}       # r4: B_1, the Klein four block
say("    chi   deg  recovered chi(2a) chi(4a)   block   distinguishes?")
cnt = {"B_0": 0, "B_1": 0}
for nm, n, m0, m1, m2 in A7:
    c2a = n - 4 * m1                       # m1 = (deg - chi(2a))/4
    cu = (4 * m0 - n - c2a) // 2           # m0 = (deg + 2 chi(u) + chi(2a))/4
    c4a = 2 * c2a - cu                     # chi(u) = 2 chi(2a) - chi(4a)  at t = 2
    assert 4 * m0 == n + 2 * cu + c2a and 4 * m2 == n + c2a - 2 * cu
    b = "B_1" if nm in BLK1 else "B_0"
    d = c2a != c4a
    if d:
        cnt[b] += 2
    say("    %-5s %3d      %4d   %4d      %s    %s" % (nm, n, c2a, c4a, b, "YES" if d else "blind"))
say("    consistency with r4's Green's-theorem control: every chi in B_1 has chi(4a) = 0 : %s"
    % all((2 * (n - 4 * m1) - (4 * m0 - n - (n - 4 * m1)) // 2) == 0
          for nm, n, m0, m1, m2 in A7 if nm in BLK1))
say("    discriminating 2-local constraints:  B_1 = %d,  B_0 = %d,  total = %d"
    % (cnt["B_1"], cnt["B_0"], cnt["B_1"] + cnt["B_0"]))
say("    r4's banked total was 14 ordinary survivors -- REPRODUCED, and now SPLIT:")
say("    *** B_1 carries 8 of the 14, i.e. the MAJORITY of the surviving discriminating")
say("        power sits in the SMALLEST block.  A_6, for comparison, has 6 in total and")
say("        all of them in its single, larger obstructing block. ***")
assert cnt["B_1"] + cnt["B_0"] == 14 and cnt["B_1"] == 8

# ----------------------------------------------------------------------------
hdr("PART F -- the transfer lemma re-checked, and its DIRECTION")
# ----------------------------------------------------------------------------
say("A_6 = stabiliser of the point 7 inside A_7.  Fusion of the two classes of 2-power")
say("order, checked WITHOUT building A_7 (2520 elements not needed):")
say("  A_6 classes of 2-power order: %s" %
    [(NAMES6[i], clct[i], clsz[i]) for i in (i2a, i4a)])
n7 = 7
def s7_class_size(ct):
    from math import factorial
    d = 1; cnt = {}
    for L in ct:
        d *= L; cnt[L] = cnt.get(L, 0) + 1
    for L, m in cnt.items():
        d *= factorial(m)
    return factorial(7) // d
def splits_in_A7(perm7):
    """an S_7-class of even permutations splits in A_7 iff its S_7-centraliser is
       inside A_7; exhibit an ODD centralising element to prove it does NOT split."""
    def sgn(p):
        s = 0; seen = [False] * len(p)
        for i in range(len(p)):
            if not seen[i]:
                L = 0; j = i
                while not seen[j]:
                    seen[j] = True; j = p[j]; L += 1
                s += L - 1
        return (-1) ** s
    import itertools
    for q in itertools.permutations(range(7)):
        if pmul(q, perm7) == pmul(perm7, q) and sgn(q) == -1:
            return False, q
    return True, None
for nm, i in (("2a", i2a), ("4a", i4a)):
    g6 = clrep[i]
    g7 = tuple(list(g6) + [6])
    ct7 = cycle_type(g7)
    sp, wit = splits_in_A7(g7)
    say("  A_6 %s (type %s)  ->  A_7 cycle type %s, S_7-class size %d, splits in A_7 = %s"
        % (nm, clct[i], ct7, s7_class_size(ct7), sp))
    say("       odd centralising witness = %s  (so the S_7-class is a SINGLE A_7-class)" % (wit,))
    assert not sp
say("  A_7 therefore has exactly one class of each of the two 2-power cycle types, of")
say("  sizes %d and %d, and the map is ONE-TO-ONE." %
    (s7_class_size((2, 2, 1, 1, 1)), s7_class_size((4, 2, 1))))
say("")
say("TRANSFER LEMMA (r4, re-checked): u in V(Z_2 A_6) of order 4 with (eps_2a,eps_4a)")
say("  = (2,-1) IS, verbatim, an element of V(Z_2 A_7) with (eps_2a,eps_4a) = (2,-1).")
say("")
say("*** ITS DIRECTION -- and this corrects the dispatch's own rationale (item (c)) ***")
say("  The lemma is an INCLUSION Z_2 A_6 subset Z_2 A_7 of group rings.  A witness")
say("  pushes FORWARD along it.  Nothing pulls BACK: proving that no such u exists in")
say("  Z_2 A_6 says NOTHING about Z_2 A_7, because a hypothetical A_7 unit has no reason")
say("  to lie in the subring.  The transfer is ONE-DIRECTIONAL.")
say("  The planner's sec.7 ruling reads: 'your transfer lemma is proved, so a result")
say("  there lands on A_7 regardless of which way it goes.'  That is true for EXISTENCE")
say("  and false for NON-EXISTENCE.")
say("  Combined with cert sec.1 -- 'existence is devalued, non-existence retains full")
say("  value' -- the only half of the A_6 question that transfers to A_7 is the half")
say("  that was priced down.  A_6-first therefore dispatches the devalued half.")
say("  I report this the same way r4 reported the calibration that devalued my own r3")
say("  recommendation: against the instruction I was given, with the arithmetic beside it.")

# ----------------------------------------------------------------------------
hdr("PART G -- the Macgregor Morita class of each block, RE-RUN not read")
# ----------------------------------------------------------------------------
say("The round-5 literature check returned a result that REFUTES my own sec.E remark:")
say("blocks with dihedral defect ARE classified up to Morita equivalence over a field.")
say("  N. Macgregor, 'Morita equivalence classes of tame blocks of finite groups',")
say("  J. Algebra 608 (2022) 719-754 (arXiv:2106.13056).  For dihedral defect of order")
say("  2^n, n >= 3, with l(B) = 3 there are EXACTLY THREE classes -- the same count as")
say("  CEKL's three Klein-four classes.  So the 'A_6 is less classified' leg of my")
say("  ordering argument is WITHDRAWN.")
say("")
say("What I can re-run rather than read is the CLASS ASSIGNMENT, because Macgregor's")
say("classes are separated by their decomposition matrices, which I have computed:")
MG = {
 "(3A) = B_0(k PSL_2(q)), q = 1 mod 4, (q-1)_2 = 2^n":
     sorted([(1,0,0),(1,1,0),(1,0,1),(1,1,1),(2,1,1)]),
 "(3K) = B_0(k PSL_2(q)), q = -1 mod 4, (q+1)_2 = 2^n":
     sorted([(1,0,0),(0,1,0),(0,0,1),(1,1,1),(0,1,1)]),
 "(3B) = B_0(k A_7), occurring ONLY for n = 3":
     sorted([(1,0,0),(1,1,0),(1,0,1),(1,1,1),(0,1,0)]),
}
mine_a6 = sorted(tuple(DEC[r]) for r in prin)
# r4's BANKED decomposition matrix for A_7's principal (dihedral) block
mine_a7 = sorted([(1,0,0),(0,1,0),(1,1,0),(1,0,1),(1,1,1)])
say("  A_6 principal block, decomposition rows COMPUTED THIS ROUND : %s" % mine_a6)
say("  A_7 principal block, decomposition rows BANKED from r4       : %s" % mine_a7)
for nm, rows in MG.items():
    say("    %-52s A_6 match: %-5s  A_7 match: %s"
        % (nm, mine_a6 == rows, mine_a7 == rows))
def cart_of(rows):
    return [[sum(r[i] * r[j] for r in rows) for j in range(3)] for i in range(3)]
say("  Cartan from Macgregor's (3A) rows = %s   (mine for A_6: %s)"
    % (cart_of(MG["(3A) = B_0(k PSL_2(q)), q = 1 mod 4, (q-1)_2 = 2^n"]), CART))
say("  Cartan from Macgregor's (3B) rows = %s   (r4's for A_7 B_0: [[4,2,2],[2,3,1],[2,1,2]])"
    % cart_of(MG["(3B) = B_0(k A_7), occurring ONLY for n = 3"]))
assert mine_a6 == MG["(3A) = B_0(k PSL_2(q)), q = 1 mod 4, (q-1)_2 = 2^n"]
assert mine_a7 == MG["(3B) = B_0(k A_7), occurring ONLY for n = 3"]
assert cart_of(MG["(3A) = B_0(k PSL_2(q)), q = 1 mod 4, (q-1)_2 = 2^n"]) == CART
assert cart_of(MG["(3B) = B_0(k A_7), occurring ONLY for n = 3"]) == [[4,2,2],[2,3,1],[2,1,2]]
say("  ALL FOUR fingerprints match, and the three classes are pairwise DISTINCT: %s"
    % (len({tuple(map(tuple, v)) for v in MG.values()}) == 3))
say("")
say("*** WHAT THE RE-RUN ESTABLISHES ***")
say("  A_6's principal 2-block is Macgregor class (3A) -- the class of B_0(k PSL_2(q)),")
say("  i.e. of exactly the groups for which ZC1 IS KNOWN.  (A_6 = PSL(2,9), so this is")
say("  consistent by construction, not a coincidence to be read as evidence.)")
say("  A_7's principal 2-block is class (3B), which Macgregor's theorem says occurs ONLY")
say("  at n = 3 and, up to Morita equivalence over k, only for A_7.")
say("  ==> the two D_8 blocks on this line are in DIFFERENT Morita classes.  A_6's")
say("      dihedral block is not a small model of A_7's.")
say("  ⚠ AND THIS DOES NOT TRANSFER TO THE UNIT QUESTION.  Macgregor works over an")
say("  algebraically closed FIELD; the unit lives in a Z_2-ORDER.  A Morita equivalence")
say("  over k says nothing about torsion units of the block over Z_2.  Recorded as the")
say("  same refusal to over-claim a citation's scope that r4 made about CEKL.")

# ----------------------------------------------------------------------------
hdr("SUMMARY OF ROUND 5 (nothing here is claimed to settle A_6 or A_7)")
say("1. A_6 has 3 2-blocks over F_4 (2 over F_2).  Exactly ONE can obstruct: the")
say("   principal one, defect 3, defect group D_8 DIHEDRAL, k(B)=5, l(B)=3,")
say("   Cartan [[8,4,4],[4,3,2],[4,2,3]], det 8, block rank 232, basic algebra rank 34.")
say("2. Census: 1 of 2 blocks over Z_2 can obstruct (1 of 3 over a splitting field);")
say("   A_7 has 2 of 2 in both counts.")
say("   Of the 28 ordinary 2-local constraints, exactly 6 can depend on the partial")
say("   augmentations, and none kills (2,-1).")
say("3. The r3 lattice machinery is FEASIBLE on A_6 at every exponent, with the all-zero")
say("   vector admissible in the obstructing block: r3's diagnosis passes its second test.")
say("4. A_6 has no forced non-zero lower bound INSIDE the block that can obstruct")
say("   (the two it does have live in blind defect-0 blocks) -- strictly weaker than A_7.")
say("5. u^2 is not Z_2A_6-conjugate to an element of 2a: the paper's A_7 argument")
say("   transplants, as information, not as a contradiction.")
say("6. The smallest object that can obstruct has basic-algebra rank 34 for A_6 and 18")
say("   for A_7.  'A_6 is smaller' fails on the measure that matters.")
say("7. The transfer lemma is ONE-DIRECTIONAL: only the devalued half lands on A_7.")
say("")
say("NOT ANSWERED: whether a unit of order 4 with (2,-1) exists in V(Z_2 A_6).")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "r5_a6_run.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
