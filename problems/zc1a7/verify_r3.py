"""
verify_r3.py -- ROUND 3 INDEPENDENT RE-VERIFICATION (Sec.105).   owner-zc1a7.

Imports NOTHING from r3_2local.py.  Rebuilds every object it needs by a different
route and re-chooses coordinates (Sec.97):

  V1  The double-action Lemma of Margolis-del Rio (arXiv:1706.02483,
      'CharacterAsIntegralPermutation'):   chi_alpha = sum_{g^G} eps_g(u) ind_{[g]}^{UxG}(1).
      Reduced here to a statement about partial augmentations only, and TESTED.  We show
      it HOLDS for a genuine group element and FAILS for A_7's open case -- so the
      nilpotency hypothesis in that paper is essential, not cosmetic.

  V2  The collapse identity  <chi_alpha, lambda_j (x) theta> = mu(zeta^{-j}, u, theta),
      re-derived by summing over the 10080 elements of C_4 x A_7 ONE BY ONE (no class
      algebra, no |C_G(h)| shortcut) using an explicitly constructed A_7.

  V3  The Z_2 C_4 bounds UB1/UB2/UB3, re-derived by BRUTE-FORCE enumeration over all
      admissible multisets of indecomposable-lattice supports, instead of by the closed
      formulas used in r3_2local.py.

  V4  The F_2 ranks on the degree-6 lattice, recomputed in the OTHER model of that
      lattice (the sum-zero SUBLATTICE of Z^7, not the quotient Z^7/<all-ones>) and with
      a bit-vector rank routine sharing no code with the first one.

Exact integer arithmetic only.  Interpreter: .venv/bin/python3.
"""
import json
import itertools
from fractions import Fraction

REPO = "$HOME/workspace/claudecode/automath/problems/zc1a7"
CL = ['1a', '2a', '3a', '3b', '4a', '5a', '6a', '7a', '7b']
SZ = [1, 105, 70, 280, 630, 504, 210, 360, 360]
OD = [1, 2, 3, 3, 4, 5, 6, 7, 7]
NG = 2520


def hr(t=''):
    print('=' * 92)
    if t:
        print(t)
        print('=' * 92)


# ------------------------------------------------------------------ build A_7 by hand
def perms_of_A7():
    """all 2520 even permutations of {0..6}, as tuples."""
    out = []
    for p in itertools.permutations(range(7)):
        # parity
        seen = [False] * 7
        par = 0
        for s in range(7):
            if not seen[s]:
                L = 0
                t = s
                while not seen[t]:
                    seen[t] = True
                    t = p[t]
                    L += 1
                par += L - 1
        if par % 2 == 0:
            out.append(p)
    return out


A7 = perms_of_A7()
assert len(A7) == 2520
IDX = {p: i for i, p in enumerate(A7)}


def cyc_type(p):
    seen = [False] * 7
    t = []
    for s in range(7):
        if not seen[s]:
            L = 0
            x = s
            while not seen[x]:
                seen[x] = True
                x = p[x]
                L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))


def order_of(p):
    from math import gcd
    o = 1
    for L in cyc_type(p):
        o = o * L // gcd(o, L)
    return o


def mul(p, q):
    """(p*q)(x) = p(q(x))"""
    return tuple(p[q[x]] for x in range(7))


def power(p, k):
    r = tuple(range(7))
    for _ in range(k):
        r = mul(p, r)
    return r


# conjugacy classes: cycle type, except (7) which splits, and we must match the
# published labels 3a=(3,1^4), 3b=(3,3,1), 4a=(4,2,1), 6a=(6,1)? -- determine by SIZE.
from collections import defaultdict
bycyc = defaultdict(list)
for p in A7:
    bycyc[cyc_type(p)].append(p)
print("cycle types of A_7 and their sizes:", {k: len(v) for k, v in sorted(bycyc.items())})

# split the 7-cycles into two classes by conjugation orbit
sev = bycyc[(7,)]
sevset = set(sev)
seed = sev[0]
orb = set()
for g in A7:                                   # conjugate by EVERY element of A_7
    gi = power(g, order_of(g) - 1)
    orb.add(mul(mul(g, seed), gi))
assert len(orb) == 360, len(orb)

CLASSOF = {}
for p in A7:
    ct = cyc_type(p)
    if ct == (7,):
        CLASSOF[p] = '7a' if p in orb else '7b'
    elif ct == (1,) * 7:
        CLASSOF[p] = '1a'
    elif ct == (2, 2, 1, 1, 1):
        CLASSOF[p] = '2a'
    elif ct == (3, 1, 1, 1, 1):
        CLASSOF[p] = '3a'
    elif ct == (3, 3, 1):
        CLASSOF[p] = '3b'
    elif ct == (4, 2, 1):
        CLASSOF[p] = '4a'
    elif ct == (5, 1, 1):
        CLASSOF[p] = '5a'
    elif ct == (6, 2) or ct == (3, 2, 2):
        CLASSOF[p] = '6a'
    else:
        raise AssertionError(ct)
cnt = defaultdict(int)
for p in A7:
    cnt[CLASSOF[p]] += 1
print("class sizes recomputed from the explicit group:", [cnt[c] for c in CL])
assert [cnt[c] for c in CL] == SZ

# power map, computed by ACTUAL EXPONENTIATION of group elements
PW = {}
for c in CL:
    rep = next(p for p in A7 if CLASSOF[p] == c)
    for k in range(1, 8):
        PW[(c, k)] = CLASSOF[power(rep, k)]
print("power map (class, k) -> class, recomputed by exponentiating real elements: OK")

# ------------------------------------------------------------------ V1
hr("V1  The Margolis-del Rio double-action Lemma, reduced and TESTED")
print("""  ind_{[g]}^{UxG}(1)(u^i,h) = #{ (a,x)[g] : (a,x)^{-1}(u^i,h)(a,x) in [g] }.
  Since U is abelian this is  |C_G(h)| if h ~_G g^i, and 0 otherwise.  And
  chi_alpha(u^i,h) = |C_G(h)| eps_h(u^i).  So the Lemma
      chi_alpha = sum_{g^G} eps_g(u) ind_{[g]}^{UxG}(1)
  is EQUIVALENT to the purely combinatorial identity
      eps_h(u^i) = sum_{ g^G : g^i in h^G } eps_g(u)      for all i and all classes h.""")

EPS = {0: {'1a': 1}, 1: {'2a': 2, '4a': -1}, 2: {'2a': 1}, 3: {'2a': 2, '4a': -1}}
EPSG = {0: {'1a': 1}, 1: {'4a': 1}, 2: {'2a': 1}, 3: {'4a': 1}}


def test_lemma(eps, tag):
    bad = []
    for i in range(4):
        for h in CL:
            lhs = eps[i].get(h, 0)
            rhs = sum(v for g, v in eps[1].items() if PW[(g, i)] == h) if i else \
                sum(v for g, v in eps[1].items() if '1a' == h)
            if i == 0:
                rhs = sum(v for g, v in eps[1].items()) if h == '1a' else 0
            if lhs != rhs:
                bad.append((i, h, lhs, rhs))
    print("  %-28s : %d of 36 (i,h) pairs VIOLATE the identity" % (tag, len(bad)))
    for b in bad:
        print("        i=%d  h=%-3s  eps_h(u^i)=%3d  but  sum_{g^i in h} eps_g(u) = %3d"
              % b)
    return bad


bad_g = test_lemma(EPSG, "u = genuine g in 4a")
bad_u = test_lemma(EPS, "u = the OPEN case (2,-1)")
assert not bad_g, bad_g
assert bad_u, "expected the Lemma to fail for the open case"
print("""  ==> The Lemma HOLDS for a group element (as it must: chi_alpha is then literally the
      permutation module on (UxG)/[g]) and FAILS for the open case.  So the nilpotency
      hypothesis of arXiv:1706.02483 is ESSENTIAL, not cosmetic: without it the character
      of the double action module is NOT the integral combination of permutation
      characters on which the Cliff-Weiss inequalities are built.""")

# ------------------------------------------------------------------ V2
hr("V2  <chi_alpha, lambda_j (x) theta> = mu(zeta^{-j}, u, theta), by SUMMING OVER ALL")
print("     10080 elements of C_4 x A_7 one at a time (no class algebra).")
raw = json.load(open(REPO + '/a7_table.json'))
from sympy import sympify, simplify, Rational, I
TAB = [[sympify(x) for x in row] for row in raw['table']]
DEG = [int(r[0]) for r in TAB]
CI = {c: k for k, c in enumerate(CL)}

# chi_alpha(u^i, h) = |C_G(h)| eps_h(u^i);  |C_G(h)| = |G|/|h^G|
def chialpha(i, h):
    return Rational(NG, SZ[CI[h]]) * Rational(EPS[i].get(h, 0))


def mu_direct(l, k):
    """mu(i^l, u, chi_k) = (1/4) sum_j i^{-l j} chi_k(u^j)."""
    s = 0
    for j in range(4):
        cv = sum(Rational(v) * TAB[k][CI[c]] for c, v in EPS[j].items())
        s += (I ** ((-l * j) % 4)) * cv
    return simplify(s / 4)


ok = 0
tot = 0
for k in range(9):
    for jj in range(4):
        acc = 0
        for i in range(4):
            zc = (I ** ((jj * i) % 4)).conjugate()
            for p in A7:                                   # ALL 2520 elements
                h = CLASSOF[p]
                acc += chialpha(i, h) * zc * TAB[k][CI[h]].conjugate()
        val = simplify(acc / (4 * NG))
        tgt = mu_direct((-jj) % 4, k)
        tot += 1
        if simplify(val - tgt) == 0:
            ok += 1
        else:
            print("   MISMATCH k=%d j=%d  %s vs %s" % (k, jj, val, tgt))
print("  %d / %d inner products match the HeLP multiplicity exactly." % (ok, tot))
assert ok == tot
print("""  ==> CONFIRMED by a route that touches every group element: for ANY finite group and
      ANY torsion unit, the 'global' double-action inequalities <chi_alpha, psi> >= 0 for
      psi irreducible are EXACTLY the HeLP inequalities.  The extra strength of the
      Cliff-Weiss inequalities lives entirely in the restriction to U x N with N a proper
      nilpotent normal subgroup, which A_7 does not have.""")

# ------------------------------------------------------------------ V3
hr("V3  UB1 / UB2 / UB3 re-derived by BRUTE-FORCE enumeration of summand supports")
print("""  An indecomposable Z_2 C_4-lattice has support S a non-empty subset of {T,Sg,W}
  (each simple at most once, [BG64] Thm 4.1).  rank = |S cap {T}| + |S cap {Sg}| + 2|S cap {W}|.
  Per-summand maxima, PROVED in the state file:
      r_1 <= rank - 1                       (a reduction has >= 1 Jordan block)
      r_1 >= 1  if W in S                   ((i-1)/2 is not an algebraic integer)
      r_2 <= |S cap {T}| + |S cap {Sg}|  if W in S, else 0
      r_3 <= 1  if S = {T,Sg,W}, else 0     (a J_4 needs rank >= 4)
  Enumerate ALL multisets of supports with the right (m0,m1,m2) and maximise.""")
SUPPORTS = [s for s in itertools.chain.from_iterable(
    itertools.combinations(['T', 'Sg', 'W'], r) for r in (1, 2, 3))]


def brute(n, m0, m1, m2, cap=200000):
    """max r_1, max r_2, max r_3, min #summands over all admissible decompositions."""
    best = [-1, -1, -1]
    minsum = 10 ** 9
    # counts per support type
    types = SUPPORTS
    ranges = []
    for S in types:
        hi = min([m0 if 'T' in S else 10 ** 9,
                  m2 if 'Sg' in S else 10 ** 9,
                  m1 if 'W' in S else 10 ** 9])
        ranges.append(range(0, min(hi, n) + 1))
    for c in itertools.product(*ranges):
        t0 = sum(c[a] for a, S in enumerate(types) if 'T' in S)
        t2 = sum(c[a] for a, S in enumerate(types) if 'Sg' in S)
        t1 = sum(c[a] for a, S in enumerate(types) if 'W' in S)
        if (t0, t1, t2) != (m0, m1, m2):
            continue
        ns = sum(c)
        minsum = min(minsum, ns)
        r1 = r2 = r3 = 0
        for a, S in enumerate(types):
            rk = ('T' in S) + ('Sg' in S) + 2 * ('W' in S)
            r1 += c[a] * (rk - 1)
            if 'W' in S:
                r2 += c[a] * (('T' in S) + ('Sg' in S))
            if len(S) == 3:
                r3 += c[a]
        best = [max(best[0], r1), max(best[1], r2), max(best[2], r3)]
    return best, minsum


MU = {0: [1, 0, 0, 0], 1: [4, 1, 0, 1], 2: [0, 3, 4, 3], 3: [0, 3, 4, 3],
      4: [6, 3, 2, 3], 5: [6, 3, 2, 3], 6: [3, 4, 4, 4], 7: [7, 5, 4, 5], 8: [7, 9, 10, 9]}


def UB1c(n, m0, m1, m2):
    return n - m1 - max(max(m0 - m1, 0), max(m2 - m1, 0))


print("\n  chi deg | brute(UB1,UB2,UB3) | closed-form(UB1,UB2,UB3) | agree")
allok = True
for k in range(9):
    m0, m1, m2 = MU[k][0], MU[k][1], MU[k][2]
    n = DEG[k]
    b, ms = brute(n, m0, m1, m2)
    cf = (UB1c(n, m0, m1, m2), min(m0, m1) + min(m2, m1), min(m0, m1, m2))
    agree = (tuple(b) == cf)
    allok = allok and agree
    print("  %-3d %3d | %-18s | %-24s | %s" % (k + 1, n, tuple(b), cf, agree))
print("  ALL NINE closed-form bounds reproduced by brute-force enumeration:", allok)
assert allok

# ------------------------------------------------------------------ V4
hr("V4  F_2 ranks on the degree-6 lattice, in the OTHER model, with a different routine")
print("""  r3_2local.py used  L = Z^7/<all-ones>  with basis e_1..e_6 (the paper's own model).
  Here we use  L' = the SUM-ZERO SUBLATTICE of Z^7,  basis f_a = e_a - e_{a+1}, a=1..6,
  and a bit-vector rank routine over F_2 sharing no code with the first.""")


def bitrank(rows, ncols):
    rows = [r for r in rows]
    r = 0
    for c in range(ncols):
        piv = None
        for t in range(r, len(rows)):
            if (rows[t] >> c) & 1:
                piv = t
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for t in range(len(rows)):
            if t != r and ((rows[t] >> c) & 1):
                rows[t] ^= rows[r]
        r += 1
    return r


def act_on_sumzero(p):
    """matrix of p acting on the basis f_a = e_a - e_{a+1}, a=0..5, as integers."""
    # e_a -> e_{p(a)}.  f_a = e_a - e_{a+1} -> e_{p(a)} - e_{p(a+1)}.
    # express e_x - e_y in the f-basis: e_x - e_y = sum_{t=min}^{max-1} +-f_t
    def ev(x, y):
        v = [0] * 6
        if x == y:
            return v
        if x < y:
            for t in range(x, y):
                v[t] += 1
        else:
            for t in range(y, x):
                v[t] -= 1
        return v
    cols = []
    for a in range(6):
        cols.append(ev(p[a], p[a + 1]))
    M = [[cols[b][a] for b in range(6)] for a in range(6)]
    return M


def to_rows_mod2(M):
    return [sum(((M[a][b] % 2) << b) for b in range(6)) for a in range(6)]


def matmulZ(A, B):
    return [[sum(A[a][t] * B[t][b] for t in range(6)) for b in range(6)] for a in range(6)]


def sub_id(M):
    return [[M[a][b] - (1 if a == b else 0) for b in range(6)] for a in range(6)]


g2 = tuple([1, 0, 3, 2, 4, 5, 6])          # (1 2)(3 4)
g4 = tuple([1, 2, 3, 0, 5, 4, 6])          # (1 2 3 4)(5 6)
assert CLASSOF[g2] == '2a' and CLASSOF[g4] == '4a'
M2 = act_on_sumzero(g2)
M4 = act_on_sumzero(g4)
r_g2 = bitrank(to_rows_mod2(sub_id(M2)), 6)
M4sq = matmulZ(M4, M4)
X = sub_id(M4)
r1_g4 = bitrank(to_rows_mod2(X), 6)
r2_g4 = bitrank(to_rows_mod2(sub_id(M4sq)), 6)
X3 = matmulZ(matmulZ(X, X), X)
r3_g4 = bitrank(to_rows_mod2(X3), 6)
print("  rank_F2(g-1) for g in 2a on L' : %d   (r3_2local.py got 2 on the quotient model)"
      % r_g2)
print("  (r_1,r_2,r_3) for g in 4a on L' : (%d,%d,%d)   (r3_2local.py got (4,2,1))"
      % (r1_g4, r2_g4, r3_g4))
assert r_g2 == 2 and (r1_g4, r2_g4, r3_g4) == (4, 2, 1)
print("  => coordinates re-chosen (Sec.97), same numbers.")
print("  and our UB2 for the open case on chi2 is 1 < 2, the paper's contradiction, intact.")

hr("VERIFY_R3: ALL CHECKS PASSED")
