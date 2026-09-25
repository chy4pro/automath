#!/usr/bin/env python3
"""
zc1a7 ROUND 1, step 2: the HeLP method for A_7, run from the character table
derived in step 1 (a7_table.py / a7_table.json).

KILL-CONDITION TARGET (charter s2):  re-derive that HeLP singles out exactly
(eps_2a, eps_4a) = (2,-1) for a torsion unit of order 4 in Z A_7, all other
partial augmentations zero.

Exact arithmetic throughout (sympy).  Interpreter: .venv/bin/python3.

Ingredients, each stated where it is used:
 (P1) Berman-Higman:            eps_{1a}(u) = 0 for u != 1
 (P2) Hertweck:                 eps_C(u) != 0  ==>  |C| divides |u|
 (P3) congruences:              sum_{C : C^{p^j} = D} eps_C(u) = eps_D(u^{p^j}) mod p
 (LP) Luthar-Passi/Hertweck:    mu(z,u,chi) = (1/n) sum_k chi(u^k) z^{-k} in Z_{>=0}
                                for every ordinary chi, and every p-Brauer chi with p
                                not dividing the order of u.
 (MRSW) u is conjugate in QG to a trivial unit  <=>  eps_C(u^d) >= 0 for all C, d|n.

Brauer characters used here are NOT taken from any table: they are the Brauer
characters of EXPLICIT F_p A_7-modules built from permutation modules
  F_p[Omega] > S > <1>,  S = sum-zero subspace,
  Brauer char of S/<1>  = pi_Omega - 2   (when p divides |Omega|)
  Brauer char of S      = pi_Omega - 1   (when p does not divide |Omega|)
which is legitimate for any module, irreducible or not (Brauer characters are
additive on filtrations; a permutation matrix has the same eigenvalues in char p,
p-regular, as over C).
"""

import json, os, itertools
from collections import defaultdict
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
N = 7

# ---------------------------------------------------------------- group (rebuilt)

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    r = [0]*N
    for i, pi in enumerate(p):
        r[pi] = i
    return tuple(r)

def cycle_type(p):
    seen = [False]*N; ct = []
    for i in range(N):
        if not seen[i]:
            l = 0; j = i
            while not seen[j]:
                seen[j] = True; j = p[j]; l += 1
            ct.append(l)
    return tuple(sorted(ct, reverse=True))

def parity(p):
    return (N - len(cycle_type(p))) % 2

A7 = [p for p in itertools.permutations(range(N)) if parity(p) == 0]
ID = tuple(range(N))

D = json.load(open(os.path.join(HERE, "a7_table.json")))
NAMES = D["names"]; ORDERS = D["orders"]; SIZES = D["sizes"]; POW = D["powermap"]
CT = [tuple(c) for c in D["cycle_types"]]
NC = len(NAMES)
IDXOF = {NAMES[k]: k for k in range(NC)}
TAB = [[sp.sympify(sp.srepr and s) for s in row] for row in D["table"]]
TAB = [[sp.sympify(s) for s in row] for row in D["table"]]
DEG = D["degrees"]

# class of each element (needed for permutation characters we compute by hand below)
def class_of_rep(p):
    """index of the A_7 class of p, using cycle type + the 7a/7b split."""
    ct = cycle_type(p)
    cand = [k for k in range(NC) if CT[k] == ct]
    if len(cand) == 1:
        return cand[0]
    return None    # only the two classes of 7-cycles are ambiguous by cycle type

# ---------------------------------------------------------------- exact roots of unity

def zeta(n, k=1):
    return sp.exp(2*sp.pi*sp.I*sp.Rational(k, n))

def ex(x):
    return sp.simplify(sp.expand(sp.expand_complex(sp.expand(x))))

# ---------------------------------------------------------------- HeLP engine

def allowed_classes(n):
    """classes C != 1a whose element order divides n  (P1)+(P2)"""
    return [k for k in range(NC) if ORDERS[k] != 1 and n % ORDERS[k] == 0]

def chi_on(vals, eps):
    """chi(u) = sum_C eps_C chi(C) ; eps a dict class-index -> value"""
    return sum(eps[k]*vals[k] for k in eps)

def multiplicity(vals, n, ell, eps_by_div):
    """
    mu(zeta_n^ell, u, chi) = (1/n) sum_{k=0}^{n-1} chi(u^k) zeta_n^{-k ell}
    chi(u^k) for gcd(k,n)=d is sigma_{k/d}( chi(u^d) ) = sum_C eps_C(u^d) chi(C^{k/d}).
    eps_by_div : dict d -> {class index: value}  for each proper divisor d of n (d<n).
    """
    tot = vals[IDXOF["1a"]]                          # k = 0 term, chi(u^0)=chi(1)
    for k in range(1, n):
        d = sp.gcd(k, n)
        j = k // d
        eps = eps_by_div[int(d)]
        val = 0
        for c, e in eps.items():
            val += e*vals[POW[c][j % ORDERS[c] if ORDERS[c] > 1 else 1]] if False else e*vals[POW[c][j]]
        tot += val*zeta(n, -k*ell)
    return sp.expand(tot/n)

def congruence_conditions(n, eps_by_div, primes=(2, 3, 5, 7)):
    """(P3). returns list of (description, expression, modulus) required = 0 mod p"""
    out = []
    for p in primes:
        j = 1
        while p**j <= n:
            m = p**j
            if n % m == 0:
                # u^m has order n/m ; its partial augmentations are eps_by_div[m]
                for Dcl in range(NC):
                    lhs = 0
                    for c, e in eps_by_div[1].items():
                        if POW[c][m] == Dcl:
                            lhs += e
                    rhs = eps_by_div[m].get(Dcl, 0) if m < n else (1 if ORDERS[Dcl] == 1 else 0)
                    if lhs != 0 or rhs != 0:
                        out.append(("p=%d, p^j=%d, D=%s" % (p, m, NAMES[Dcl]), sp.expand(lhs - rhs), p))
            j += 1
    return out

# ---------------------------------------------------------------- Brauer characters

def perm_character(points, act):
    """pi(C) for a permutation action; returns list over classes (uses class reps)."""
    pi = [0]*NC
    reps = {}
    # find a representative of each class by scanning A7 (cheap, 2520 elements)
    seen = {}
    for g in A7:
        k = class_of_rep(g)
        if k is not None and k not in seen:
            seen[k] = g
    # the two 7-classes: distinguish by matching character values of chi3 is overkill;
    # instead: 7a and 7b are swapped by conjugation with an odd permutation, and every
    # permutation action defined S_7-equivariantly has EQUAL fixed-point counts on them.
    for k, g in seen.items():
        pi[k] = sum(1 for x in points if act(g, x) == x)
    amb = [k for k in range(NC) if CT[k] == (7,)]
    if len(amb) == 2:
        # compute for one actual 7-cycle and copy (S_7-stable actions), else compute both
        g7 = None
        for g in A7:
            if cycle_type(g) == (7,):
                g7 = g; break
        v = sum(1 for x in points if act(g7, x) == x)
        for k in amb:
            pi[k] = v
    return pi

def subsets_action(k):
    pts = [frozenset(s) for s in itertools.combinations(range(N), k)]
    def act(g, s):
        return frozenset(g[i] for i in s)
    return pts, act

def fano_cosets_action():
    lines = [frozenset(l) for l in
             [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]]
    L = set(lines)
    H = [g for g in A7 if {frozenset(g[i] for i in l) for l in lines} == L]
    assert len(H) == 168, "Fano automorphism group inside A_7 has order %d" % len(H)
    Hs = set(H)
    cosets = []
    seen = set()
    for g in A7:
        if g in seen:
            continue
        c = frozenset(compose(g, h) for h in H)
        cosets.append(c)
        seen |= c
    assert len(cosets) == 15
    idx = {}
    for i, c in enumerate(cosets):
        for x in c:
            idx[x] = i
    def act(g, i):
        rep = next(iter(cosets[i]))
        return idx[compose(g, rep)]
    return list(range(15)), act, len(H)

# ---------------------------------------------------------------- assemble characters

ORD_CHARS = [("chi%d(deg %d)" % (i+1, DEG[i]), TAB[i], None) for i in range(NC)]

BRAUER = []
actions = []
for k in (1, 2, 3):
    pts, act = subsets_action(k)
    actions.append(("%d-subsets (deg %d)" % (k, len(pts)), pts, act))
pts15, act15, ordH = fano_cosets_action()
actions.append(("cosets of Fano group |H|=%d (deg 15)" % ordH, pts15, act15))

for label, pts, act in actions:
    pi = perm_character(pts, act)
    m = len(pts)
    for p in (2, 3, 5, 7):
        if m % p == 0:
            vals = [sp.Integer(pi[k] - 2) for k in range(NC)]
            dim = m - 2
            tag = "pi(%s)-2" % label
        else:
            vals = [sp.Integer(pi[k] - 1) for k in range(NC)]
            dim = m - 1
            tag = "pi(%s)-1" % label
        BRAUER.append(("p=%d %s dim %d" % (p, tag, dim), vals, p))

print("=== permutation characters used to build Brauer characters ===")
for label, pts, act in actions:
    pi = perm_character(pts, act)
    print("  %-45s pi = %s" % (label, dict(zip(NAMES, pi))))
print()

# ---------------------------------------------------------------- ORDER 4 : the target

print("="*88)
print("ORDER 4 UNITS IN V(Z A_7)   -- the charter's kill condition")
print("="*88)

n = 4
allow = allowed_classes(n)
print("(P1)+(P2): classes with eps_C(u) possibly nonzero for |u|=4 :",
      [NAMES[k] for k in allow])
allow2 = allowed_classes(2)
print("(P1)+(P2): classes with eps_C(u^2) possibly nonzero (|u^2|=2) :",
      [NAMES[k] for k in allow2])
assert allow2 == [IDXOF["2a"]]
print("  => eps_2a(u^2) = 1 (normalised), so u^2 is rationally conjugate to 2a by MRSW.")

t = sp.Symbol("t", integer=True)
eps1 = {IDXOF["2a"]: t, IDXOF["4a"]: 1 - t}
eps_by_div = {1: eps1, 2: {IDXOF["2a"]: sp.Integer(1)}}
print("  variables: eps_2a(u) = t, eps_4a(u) = 1 - t")
print()

# --- congruences
print("--- (P3) congruences")
lo, hi = None, None
cong = congruence_conditions(4, eps_by_div)
mods = []
for desc, e, p in cong:
    if e.free_symbols:
        print("   %-28s  %s = 0 (mod %d)" % (desc, sp.sstr(e), p))
        mods.append((e, p))
print()

# --- HeLP inequalities
def collect(chars, tag):
    rows = []
    for name, vals, p in chars:
        for ell in range(n):
            mu = ex(multiplicity(vals, n, ell, eps_by_div))
            mu = sp.expand(mu)
            rows.append((name, ell, sp.nsimplify(mu)))
    return rows

rows = collect(ORD_CHARS, "ordinary")
rows_b = collect([b for b in BRAUER if 4 % b[2] != 0], "brauer")

def bounds_from(rows):
    lo, hi = -sp.oo, sp.oo
    detail = []
    for name, ell, mu in rows:
        poly = sp.Poly(mu, t)
        assert poly.degree() <= 1
        b = poly.coeff_monomial(t)
        a = poly.coeff_monomial(1)
        if b > 0:
            nb = sp.ceiling(-a/b)
            if nb > lo:
                lo = nb; detail.append(("t >= %s" % nb, name, ell, mu))
        elif b < 0:
            nb = sp.floor(-a/b)
            if nb < hi:
                hi = nb; detail.append(("t <= %s" % nb, name, ell, mu))
    return lo, hi, detail

lo_o, hi_o, det_o = bounds_from(rows)
print("--- HeLP with ORDINARY characters only")
for d in det_o:
    print("   %-12s from %-22s ell=%d  mu = %s" % (d[0], d[1], d[2], sp.sstr(d[3])))
print("   => %s <= t <= %s" % (lo_o, hi_o))
print()

lo_b, hi_b, det_b = bounds_from(rows + rows_b)
print("--- HeLP with ordinary + the explicitly-constructed Brauer characters")
for d in det_b:
    print("   %-12s from %-46s ell=%d  mu = %s" % (d[0], d[1], d[2], sp.sstr(d[3])))
print("   => %s <= t <= %s" % (lo_b, hi_b))
print()

cands = [int(v) for v in range(int(lo_b), int(hi_b)+1)]
print("--- candidate integers in the proven interval:", cands)
surv = []
for v in cands:
    okc = all(sp.Integer(e.subs(t, v)) % p == 0 for e, p in mods)
    oki = True
    okp = True
    for name, ell, mu in rows + rows_b:
        val = sp.nsimplify(mu.subs(t, v))
        if val < 0:
            okp = False
        if not sp.Integer(val*1) == val or not val.is_integer:
            oki = False
    print("   t = %2d : congruences %-5s  all mu integral %-5s  all mu >= 0 %-5s"
          % (v, okc, oki, okp))
    if okc and oki and okp:
        surv.append(v)
print()
print("SURVIVING partial augmentation vectors (eps_2a, eps_4a) for |u| = 4:")
for v in surv:
    trivial = (v >= 0 and 1 - v >= 0)
    print("   (%d, %d)   %s" % (v, 1-v,
          "TRIVIAL distribution (MRSW: u rationally conjugate to a trivial unit)"
          if trivial else "NON-TRIVIAL  <<<"))
print()

# --- print the full multiplicity table for the surviving non-trivial vector
for v in surv:
    if v == 0:
        continue
    print("--- eigenvalue multiplicities of D(u) for (eps_2a,eps_4a) = (%d,%d)" % (v, 1-v))
    print("    %-46s %-6s %-6s %-6s %-6s" % ("character", "mu(1)", "mu(i)", "mu(-1)", "mu(-i)"))
    for name, vals, p in ORD_CHARS + [b for b in BRAUER if 4 % b[2] != 0]:
        ms = [sp.nsimplify(ex(multiplicity(vals, 4, ell, eps_by_div)).subs(t, v))
              for ell in range(4)]
        tot = sum(ms)
        print("    %-46s %-6s %-6s %-6s %-6s   sum=%s deg=%s"
              % (name, ms[0], ms[1], ms[2], ms[3], tot, vals[IDXOF["1a"]]))
    print()

# ---------------------------------------------------------------- other orders (context)

print("="*88)
print("CONTEXT: other orders, same machinery (NOT the kill condition)")
print("="*88)

def run_prime_order(n):
    allow = allowed_classes(n)
    syms = sp.symbols("e0:%d" % len(allow), integer=True)
    eps1 = {allow[i]: syms[i] for i in range(len(allow))}
    # normalisation
    subsmap = {syms[-1]: 1 - sum(syms[:-1])}
    eps1 = {k: sp.expand(v.subs(subsmap)) for k, v in eps1.items()}
    ebd = {1: eps1}
    chars = ORD_CHARS + [b for b in BRAUER if n % b[2] != 0]
    ineqs = []
    for name, vals, p in chars:
        for ell in range(n):
            mu = sp.nsimplify(ex(multiplicity(vals, n, ell, ebd)))
            ineqs.append((name, ell, sp.expand(mu)))
    return allow, syms[:-1], ineqs

for n in (2, 3, 5, 7):
    allow, freesyms, ineqs = run_prime_order(n)
    print("\n|u| = %d : classes %s, free variables %s"
          % (n, [NAMES[k] for k in allow], list(freesyms)))
    if len(freesyms) == 0:
        print("   only one class possible => eps = 1 there => trivial by MRSW.")
        continue
    if len(freesyms) == 1:
        x = freesyms[0]
        lo, hi = -sp.oo, sp.oo
        for name, ell, mu in ineqs:
            poly = sp.Poly(mu, x)
            assert poly.degree() <= 1
            b = poly.coeff_monomial(x)
            a = poly.coeff_monomial(1)
            if b == 0:
                continue
            if b > 0:
                lo = max(lo, sp.ceiling(-a/b))
            elif b < 0:
                hi = min(hi, sp.floor(-a/b))
        print("   HeLP interval: %s <= %s <= %s" % (lo, x, hi))
        vals_ok = []
        for v in range(int(lo), int(hi)+1):
            if all(sp.nsimplify(mu.subs(x, v)) >= 0 and sp.nsimplify(mu.subs(x, v)).is_integer
                   for _, _, mu in ineqs):
                vals_ok.append(v)
        print("   surviving %s = %s  -> vectors %s"
              % (x, vals_ok, [(v, 1-v) for v in vals_ok]))
        print("   all non-negative (=> trivial by MRSW)? %s"
              % all(v >= 0 and 1-v >= 0 for v in vals_ok))
    else:
        print("   (multi-variable; not solved here)")
