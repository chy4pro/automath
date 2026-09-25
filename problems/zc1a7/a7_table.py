#!/usr/bin/env python3
"""
zc1a7 ROUND 1, step 1: build A_7 from scratch and derive its ORDINARY CHARACTER TABLE.

Everything exact (integers / sympy algebraic numbers).  No floating point.
Interpreter: .venv/bin/python3 (sympy 1.14.0).

Method (two independent ingredients, so that step 3 can cross-check):
  (A) the GROUP: A_7 built as permutations of {0..6}; conjugacy classes, class sizes,
      element orders and power maps computed by actual group multiplication.
  (B) the COMBINATORICS: the ordinary character table of S_7 via the Murnaghan-Nakayama
      rule on beta-sets; restriction to A_7; the one self-conjugate partition (4,1,1,1)
      splits, with the classical (x +- sqrt(eps*prod h_i))/2 formula.

Self-checks run at the end (POSITIVE CONTROLS):
  C1 row orthogonality      sum_k |C_k| chi_i(k) conj(chi_j(k)) = |G| delta_ij
  C2 column orthogonality
  C3 sum of squares of degrees = |G|, number of irreducibles = number of classes
  C4 class-algebra structure constants computed BY MULTIPLYING GROUP ELEMENTS:
        omega_i(k) omega_i(l) = sum_m a_{klm} omega_i(m),  omega_i(k)=|C_k|chi_i(k)/chi_i(1)
     (this ties the combinatorial table (B) back to the actual group (A))
  C5 comparison against the values PRINTED in arXiv:2006.09031 Table 1
     (chi_1, chi_5, chi_6 on 1a,2a,3a,3b,6a) and against the 7-modular Brauer character
     values the paper states (deg 5 with 3a->2, 3b->-1).
"""

from itertools import permutations, combinations
from functools import lru_cache
import sympy as sp

# ----------------------------------------------------------------- (A) the group

N = 7

def compose(p, q):
    """(p*q)(i) = p(q(i))"""
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    r = [0]*N
    for i, pi in enumerate(p):
        r[pi] = i
    return tuple(r)

def cycle_type(p):
    seen = [False]*N
    ct = []
    for i in range(N):
        if not seen[i]:
            l = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                l += 1
            ct.append(l)
    return tuple(sorted(ct, reverse=True))

def parity(p):
    ct = cycle_type(p)
    return (N - len(ct)) % 2          # 0 = even

def order_of(p):
    ct = cycle_type(p)
    o = 1
    for c in ct:
        o = o*c//sp.gcd(o, c)
    return int(o)

A7 = [p for p in permutations(range(N)) if parity(p) == 0]
assert len(A7) == 2520
IDX = {p: i for i, p in enumerate(A7)}
ID = tuple(range(N))

# generators of A_7 (3-cycles generate A_n; use two that generate everything)
GENS = [(1, 2, 0, 3, 4, 5, 6),                        # (0 1 2)
        (0, 1, 2, 3, 4, 5, 6)]
GENS[1] = (1, 2, 3, 4, 5, 6, 0) if N % 2 == 1 else GENS[1]   # 7-cycle, even for N=7
# sanity: both generators even, and they generate A_7
for g in GENS:
    assert parity(g) == 0

def closure(gens):
    seen = {ID}
    frontier = [ID]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = compose(g, x)
                if y not in seen:
                    seen.add(y)
                    nf.append(y)
        frontier = nf
    return seen

assert len(closure(GENS)) == 2520, "generators do not generate A_7"

# conjugacy classes: orbits under conjugation by the generators
def conj_classes():
    unassigned = set(A7)
    classes = []
    while unassigned:
        x0 = min(unassigned)
        orb = {x0}
        frontier = [x0]
        while frontier:
            nf = []
            for x in frontier:
                for g in GENS:
                    y = compose(compose(g, x), inverse(g))
                    if y not in orb:
                        orb.add(y)
                        nf.append(y)
            frontier = nf
        classes.append(orb)
        unassigned -= orb
    return classes

CLASSES = conj_classes()
assert sum(len(c) for c in CLASSES) == 2520

# canonical ordering / GAP-style names: by element order, then by class size
info = []
for c in CLASSES:
    rep = min(c)
    info.append((order_of(rep), len(c), cycle_type(rep), rep, c))
info.sort(key=lambda t: (t[0], t[1]))

NAMES = []
from collections import defaultdict
cnt = defaultdict(int)
for o, sz, ct, rep, c in info:
    cnt[o] += 1
    NAMES.append("%d%s" % (o, "abcdefg"[cnt[o]-1]))

CLASS_ORDER = [t[0] for t in info]
CLASS_SIZE = [t[1] for t in info]
CLASS_CT = [t[2] for t in info]
CLASS_REP = [t[3] for t in info]
CLASS_SET = [t[4] for t in info]
NC = len(info)
CLASS_OF = {}
for k, c in enumerate(CLASS_SET):
    for x in c:
        CLASS_OF[x] = k

def power(p, k):
    r = ID
    for _ in range(k):
        r = compose(r, p)
    return r

# power map: POW[k][j] = class of (rep of class k)^j
POW = [[CLASS_OF[power(CLASS_REP[k], j)] for j in range(13)] for k in range(NC)]

print("=== A_7 : %d elements, %d conjugacy classes ===" % (len(A7), NC))
print("%-5s %-6s %-8s %-14s" % ("name", "order", "size", "cycle type"))
for k in range(NC):
    print("%-5s %-6d %-8d %-14s" % (NAMES[k], CLASS_ORDER[k], CLASS_SIZE[k], str(CLASS_CT[k])))
print()

# ------------------------------------------------- (B) S_7 table by Murnaghan-Nakayama

def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

PARTS = list(partitions(N))
assert len(PARTS) == 15

def conjugate_partition(lam):
    if not lam:
        return ()
    m = lam[0]
    return tuple(sum(1 for x in lam if x >= j) for j in range(1, m+1))

def beta_set(lam):
    k = len(lam)
    return frozenset(lam[i] + (k - 1 - i) for i in range(k))

@lru_cache(maxsize=None)
def mn(beta, rho):
    """Murnaghan-Nakayama on beta-sets. rho a tuple (cycle type, any order)."""
    if not rho:
        return 1
    r = rho[0]
    rest = rho[1:]
    tot = 0
    for b in beta:
        nb = b - r
        if nb >= 0 and nb not in beta:
            ht = sum(1 for x in beta if nb < x < b)
            tot += (-1)**ht * mn(frozenset((beta - {b}) | {nb}), rest)
    return tot

def chiS7(lam, rho):
    return mn(beta_set(lam), tuple(rho))

# dimension check
for lam in PARTS:
    d = chiS7(lam, (1,)*N)
    assert d > 0
assert sum(chiS7(lam, (1,)*N)**2 for lam in PARTS) == 5040, "S_7 degrees wrong"

# ------------------------------------------------- restriction to A_7

# even cycle types = the A_7 classes' S_7 cycle types
even_types = sorted({CLASS_CT[k] for k in range(NC)})
split_types = [ct for ct in even_types
               if len(set(ct)) == len(ct) and all(x % 2 == 1 for x in ct)]
print("S_7 cycle types meeting A_7 :", even_types)
print("types that SPLIT in A_7     :", split_types)
assert split_types == [(7,)]

selfconj = [lam for lam in PARTS if conjugate_partition(lam) == lam]
print("self-conjugate partitions of 7 :", selfconj)
assert selfconj == [(4, 1, 1, 1)]

# pair up conjugate partitions
pairs = []
used = set()
for lam in PARTS:
    if lam in used:
        continue
    mu = conjugate_partition(lam)
    used.add(lam); used.add(mu)
    if lam != mu:
        pairs.append(lam)

irr = []      # each entry: (label, dict class-index -> exact value)
for lam in pairs:
    vals = {k: sp.Integer(chiS7(lam, CLASS_CT[k])) for k in range(NC)}
    irr.append(("S7:%s" % (lam,), vals))

# the split pair
lam = selfconj[0]
# principal hooks of a self-conjugate partition
def principal_hooks(l):
    hooks = []
    lc = conjugate_partition(l)
    i = 0
    while i < len(l) and l[i] - i > 0:
        hooks.append(l[i] + lc[i] - 2*i - 1)
        i += 1
    return hooks

H = principal_hooks(lam)
print("principal hooks of %s : %s" % (str(lam), H))
assert sorted(H, reverse=True) == list(reversed(sorted(H))) # trivial
d = len(H)
eps = (-1)**((N - d)//2)
prod = 1
for h in H:
    prod *= h
disc = sp.sqrt(sp.Integer(eps*prod))
print("splitting discriminant sqrt(%d * %d) = %s" % (eps, prod, disc))

split_ct = tuple(sorted(H, reverse=True))
assert split_ct in split_types
x_on_split = sp.Integer(chiS7(lam, split_ct))
plus = {}
minus = {}
first_split = True
for k in range(NC):
    if CLASS_CT[k] == split_ct:
        if first_split:
            plus[k] = (x_on_split + disc)/2
            minus[k] = (x_on_split - disc)/2
            first_split = False
        else:
            plus[k] = (x_on_split - disc)/2
            minus[k] = (x_on_split + disc)/2
    else:
        v = sp.Integer(chiS7(lam, CLASS_CT[k]))
        assert v % 2 == 0, "restriction of self-conjugate character not divisible by 2"
        plus[k] = v/2
        minus[k] = v/2
irr.append(("S7:%s+" % (lam,), plus))
irr.append(("S7:%s-" % (lam,), minus))

# order irreducibles by degree
one = [k for k in range(NC) if CLASS_ORDER[k] == 1][0]
irr.sort(key=lambda t: (sp.nsimplify(t[1][one]), str(t[0])))
IRRNAME = ["chi%d" % (i+1) for i in range(len(irr))]
TAB = [irr[i][1] for i in range(len(irr))]
DEG = [TAB[i][one] for i in range(len(irr))]

print()
print("=== ORDINARY CHARACTER TABLE OF A_7 (derived) ===")
hdr = "%-7s" % "" + "".join("%-14s" % NAMES[k] for k in range(NC))
print(hdr)
for i in range(len(irr)):
    print("%-7s" % IRRNAME[i] + "".join("%-14s" % sp.sstr(sp.simplify(TAB[i][k])) for k in range(NC)))
print()

# ------------------------------------------------- checks

def conj(x):
    return sp.conjugate(x)

# C3
assert len(irr) == NC, "wrong number of irreducibles"
assert sum(sp.Integer(DEG[i])**2 for i in range(NC)) == 2520
print("C3  #irr = #classes = %d, sum of squares of degrees = 2520 : OK" % NC)

# C1
ok = True
for i in range(NC):
    for j in range(NC):
        s = sum(sp.Integer(CLASS_SIZE[k])*TAB[i][k]*conj(TAB[j][k]) for k in range(NC))
        s = sp.simplify(sp.expand(s))
        want = 2520 if i == j else 0
        if s != want:
            ok = False
            print("C1 FAIL", i, j, s)
print("C1  row orthogonality : %s" % ("OK" if ok else "FAIL"))

# C2
ok = True
for k in range(NC):
    for l in range(NC):
        s = sum(TAB[i][k]*conj(TAB[i][l]) for i in range(NC))
        s = sp.simplify(sp.expand(s))
        want = sp.Rational(2520, CLASS_SIZE[k]) if k == l else 0
        if s != want:
            ok = False
            print("C2 FAIL", k, l, s, want)
print("C2  column orthogonality : %s" % ("OK" if ok else "FAIL"))

# C4 : class-algebra structure constants, computed from the GROUP
def struct_const(k, l, m):
    """#{ (x,y) : x in C_k, y in C_l, xy = z } for a fixed z in C_m"""
    z = CLASS_REP[m]
    Cl = CLASS_SET[l]
    c = 0
    for x in CLASS_SET[k]:
        if compose(inverse(x), z) in Cl:      # y = x^{-1} z
            c += 1
    return c

A = [[[struct_const(k, l, m) for m in range(NC)] for l in range(NC)] for k in range(NC)]
ok = True
for i in range(NC):
    w = [sp.Integer(CLASS_SIZE[k])*TAB[i][k]/DEG[i] for k in range(NC)]
    for k in range(NC):
        for l in range(NC):
            lhs = sp.expand(w[k]*w[l])
            rhs = sp.expand(sum(A[k][l][m]*w[m] for m in range(NC)))
            if sp.simplify(lhs - rhs) != 0:
                ok = False
                print("C4 FAIL", i, k, l, lhs, rhs)
print("C4  class-algebra constants (computed by multiplying group elements) : %s"
      % ("OK" if ok else "FAIL"))

# C5 : the values PRINTED in arXiv:2006.09031, Table 1
idx = {NAMES[k]: k for k in range(NC)}
paper_rows = {  # degree -> (2a,3a,3b,6a)  as printed for chi_1, chi_5, chi_6
    1:  (1, 1, 1, 1),
    14: [(2, 2, -1, 2), (2, -1, 2, -1)],
}
got14 = sorted([tuple(int(TAB[i][idx[c]]) for c in ("2a", "3a", "3b", "6a"))
                for i in range(NC) if DEG[i] == 14])
want14 = sorted(paper_rows[14])
print("C5a chi of degree 14 on (2a,3a,3b,6a): derived %s  paper %s : %s"
      % (got14, want14, "MATCH" if got14 == want14 else "MISMATCH"))
i1 = [i for i in range(NC) if DEG[i] == 1][0]
got1 = tuple(int(TAB[i1][idx[c]]) for c in ("2a", "3a", "3b", "6a"))
print("C5b trivial character on (2a,3a,3b,6a): %s : %s"
      % (str(got1), "MATCH" if got1 == paper_rows[1] else "MISMATCH"))

# the natural degree-6 character = permutation character on 7 points minus 1
i6 = [i for i in range(NC) if DEG[i] == 6][0]
permchar = [sum(1 for j in range(N) if CLASS_REP[k][j] == j) for k in range(NC)]
ok = all(TAB[i6][k] == permchar[k] - 1 for k in range(NC))
print("C5c degree-6 character equals (fixed points - 1) on every class : %s" % ("OK" if ok else "FAIL"))
print("    fixed-point counts:", dict(zip(NAMES, permchar)))
print("    7-modular Brauer character phi5 := chi_6dim - 1 on (3a,3b) = (%s,%s); paper states (2,-1) : %s"
      % (TAB[i6][idx["3a"]]-1, TAB[i6][idx["3b"]]-1,
         "MATCH" if (TAB[i6][idx["3a"]]-1, TAB[i6][idx["3b"]]-1) == (2, -1) else "MISMATCH"))

# ------------------------------------------------- dump for later steps
import json
out = {
    "names": NAMES,
    "orders": CLASS_ORDER,
    "sizes": CLASS_SIZE,
    "cycle_types": [list(c) for c in CLASS_CT],
    "powermap": POW,
    "degrees": [int(DEG[i]) for i in range(NC)],
    "table": [[sp.srepr(sp.simplify(TAB[i][k])) for k in range(NC)] for i in range(NC)],
    "irrnames": IRRNAME,
}
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "a7_table.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nwrote a7_table.json")
