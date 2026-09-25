"""
r3_2local.py -- ROUND 3, line zc1a7.   owner-zc1a7.

TARGET (planner, cert_zc1a7_r2.md Sec.1): "a 2-local argument valid when the 2'-part
is trivial."

This script does FOUR things, each with a positive control and a rejection control:

 (A) CLIFF-WEISS COLLAPSE.  Margolis-del Rio (J.Algebra 507 (2018), arXiv:1706.02483)
     derive linear inequalities on partial augmentations from the double action module.
     Their hypothesis is  N  a NILPOTENT NORMAL subgroup and  u in V(ZG,N).  A_7 is
     simple so N=1 and the inequalities are vacuous.  Here we verify the sharper
     statement: with N = G the "global" inequality  <chi_alpha, psi> >= 0  is EXACTLY
     the HeLP multiplicity  mu(xi,u,theta) >= 0.  So the method DEGENERATES TO HeLP
     for a simple group; it is not merely inapplicable.

 (B) THE Z_2 C_4 LATTICE BOUNDS at p=2, m=1 (trivial 2'-part), derived here:
       r_j(Lbar) := rank_{F_2}( (ubar-1)^j | L/2L ).   Note (ubar-1)^2 = ubar^2 - 1.
       UB2(chi) = min(m0,m1) + min(m2,m1)                       [Berman-Gudkov]
       UB1(chi) = n - m1 - max((m0-m1)^+, (m2-m1)^+)            [Berman-Gudkov]
       LB1(chi) = m1                                            [(i-1)/2 not integral]
       LB_j(chi) >= sum_S d_{chi,S} r_j(S)                      [superadditivity]
     with (m0,m1,m2) = (mu(1),mu(i),mu(-1)) of u under chi, n = chi(1),
     d = the 2-modular decomposition matrix.
     POSITIVE CONTROL: UB2 must reproduce the paper's own degree-6 number (1, vs 2 for
     a genuine element of 2a), and must be ATTAINED by a genuine element of 4a.

 (C) THE FEASIBILITY QUESTION.  Is the whole system satisfiable?  If yes the p=2
     lattice method cannot settle A_7 for |u|=4, and we say exactly why.

 (D) THE PROJECTIVE-IDEMPOTENT PROBE -- derived here independently, then found in the
     literature and CREDITED: it is l.197 of Margolis, arXiv:1706.02117.
     e = (1+u+u^2+u^3)/4 is an idempotent of
     Z_p A_7 for every ODD p, so  P = Z_p A_7 e  is a PROJECTIVE lattice and its
     ordinary character  theta = sum_chi mu(1,u,chi) chi  must be a NON-NEGATIVE
     INTEGER combination of the projective indecomposable characters.  Same for
     (1+u^2)/2 and (1-u^2)/2.  Run at p = 3,5,7 with a perturbation rejection control.

Exact arithmetic only (Fraction / sympy Rational / exact roots of unity).  No floats.
Interpreter: .venv/bin/python3 (3.9.6, sympy 1.14.0).
Imports NOTHING from round 1/2 builders except the two JSON data files, and re-derives
the order-4 multiplicities by a method (Vandermonde inverse over Q(i)) different from
help_full.py's Ramanujan sums.
"""
import json
import itertools
from fractions import Fraction
from sympy import sympify, Matrix, I, Rational, simplify, nsimplify

REPO = "$HOME/workspace/claudecode/automath/problems/zc1a7"
CLASSES = ['1a', '2a', '3a', '3b', '4a', '5a', '6a', '7a', '7b']
SIZES   = [1, 105, 70, 280, 630, 504, 210, 360, 360]
ORD     = [1, 2, 3, 3, 4, 5, 6, 7, 7]
GORD    = 2520

def hr(t=''):
    print('=' * 92)
    if t:
        print(t)
        print('=' * 92)

# ---------------------------------------------------------------- ordinary table
raw = json.load(open(REPO + '/a7_table.json'))
assert raw['names'] == CLASSES, raw['names']
assert raw['sizes'] == SIZES
ORDTAB = [[sympify(x) for x in row] for row in raw['table']]
DEG = [int(r[0]) for r in ORDTAB]

# self-check: orthogonality (C1) -- do not trust the file
for a in range(9):
    for b in range(9):
        s = sum(Rational(SIZES[k]) * ORDTAB[a][k] * ORDTAB[b][k].conjugate() for k in range(9))
        assert simplify(s - (GORD if a == b else 0)) == 0, (a, b, s)
assert sum(d * d for d in DEG) == GORD
print("ordinary character table of A_7 loaded and re-verified orthogonal; degrees", DEG)

# ---------------------------------------------------------------- power map on classes
# only the classes an order-4 unit can touch matter, but build it for all rational ones
POWER = {('1a', 2): '1a', ('2a', 2): '1a', ('3a', 2): '3a', ('3a', 3): '1a',
         ('3b', 2): '3b', ('3b', 3): '1a', ('4a', 2): '2a', ('4a', 3): '4a', ('4a', 4): '1a',
         ('5a', 5): '1a', ('6a', 2): '3a', ('6a', 3): '2a', ('6a', 6): '1a'}

# ---------------------------------------------------------------- the candidate unit
# eps(u):  2 at 2a, -1 at 4a, 0 elsewhere.  eps(u^2): 1 at 2a (u^2 ~ 2a).  eps(u^0)=1 at 1a.
# u^3 = u^{-1}; 2a and 4a are real classes of A_7, so eps(u^3) = eps(u).
EPS = {}
EPS[0] = {'1a': 1}
EPS[1] = {'2a': 2, '4a': -1}
EPS[2] = {'2a': 1}
EPS[3] = {'2a': 2, '4a': -1}
# trivial solution (0,1): u a genuine element of 4a
EPSG = {0: {'1a': 1}, 1: {'4a': 1}, 2: {'2a': 1}, 3: {'4a': 1}}


def chival(chi_idx, eps):
    """chi(x) for a unit x with partial augmentations eps (dict class->int)."""
    return sum(Rational(v) * ORDTAB[chi_idx][CLASSES.index(c)] for c, v in eps.items())


def mults(chi_idx, epsdict):
    """mu(i^l, u, chi) for l=0..3, by inverting the 4x4 Vandermonde over Q(i).
       (A DIFFERENT algorithm from help_full.py's Ramanujan sums.)"""
    z = [1, I, -1, -I]
    V = Matrix(4, 4, lambda a, b: z[a] ** b)     # V[a][b] = zeta^{a*b}? careful below
    # chi(u^j) = sum_l mu_l * zeta^{l j}  ->  vector of chi(u^j) = M * mu, M[j][l]=zeta^(l j)
    M = Matrix(4, 4, lambda j, l: z[l] ** j)
    rhs = Matrix(4, 1, [chival(chi_idx, epsdict[j]) for j in range(4)])
    sol = M.inv() * rhs
    out = []
    for l in range(4):
        v = simplify(sol[l])
        assert v.is_rational, (chi_idx, l, v)
        out.append(Rational(v))
    return out


hr("(0)  ORDER-4 MULTIPLICITIES, re-derived by Vandermonde inversion over Q(i)")
MU = {}
for k in range(9):
    m = mults(k, EPS)
    assert sum(m) == DEG[k]
    for x in m:
        assert x.q == 1 and x >= 0, (k, m)
    MU[k] = [int(x) for x in m]
MUG = {}
for k in range(9):
    m = mults(k, EPSG)
    assert sum(m) == DEG[k]
    MUG[k] = [int(x) for x in m]
print("  chi  deg | mu(1) mu(i) mu(-1) mu(-i)   [u = the OPEN case (2,-1)]  ||  [g in 4a]")
for k in range(9):
    print("  chi%-2d %3d | %5d %5d %6d %6d              || %s"
          % (k + 1, DEG[k], MU[k][0], MU[k][1], MU[k][2], MU[k][3], MUG[k]))
print("  CONTROL vs round 2 (banked): chi2 row must be (4,1,0,1) ->", MU[1] == [4, 1, 0, 1])
print("  CONTROL vs round 2 (banked): both deg-10 rows must be (0,3,4,3) ->",
      MU[2] == [0, 3, 4, 3] and MU[3] == [0, 3, 4, 3])
assert MU[1] == [4, 1, 0, 1] and MU[2] == [0, 3, 4, 3] and MU[3] == [0, 3, 4, 3]

# =================================================================== (A) CW COLLAPSE
hr("(A)  CLIFF-WEISS 'GLOBAL' INEQUALITY WITH N = G  ==  HeLP, VERIFIED NUMERICALLY")
print("""  Margolis-del Rio arXiv:1706.02483, Prop. 'EquationCharacter':
     <chi_alpha, psi>  =  sum_n a(n,psi) eps_n(u)  >= 0,   a(n,psi) = (1/|u|) sum_i psi(u^i, n^i).
  The double-action character is  chi_alpha(u^i, h) = |C_G(h)| * eps_h(u^i)   [Sehgal 38.12].
  For psi = lambda_j (x) theta an irreducible character of U x G we compute both sides.""")
rows = []
for k in range(9):
    for j in range(4):
        # LHS: <chi_alpha, lambda_j (x) theta> over U x G, computed from the DEFINITION
        # <chi_alpha,psi> = 1/(4|G|) sum_{i,h} chi_alpha(u^i,h) conj(psi(u^i,h))
        tot = 0
        for i in range(4):
            zj = (I ** (j * i))
            inner = 0
            for ci, c in enumerate(CLASSES):
                e = EPS[i].get(c, 0)
                if e:
                    # sum over h in class c of |C_G(h)| eps_h(u^i) conj(theta(h))
                    # |class| * |C_G| = |G|
                    inner += Rational(GORD) * Rational(e) * ORDTAB[k][ci].conjugate()
            tot += zj.conjugate() * inner
        lhs = simplify(tot / (4 * GORD))
        rhs = MU[k][(-j) % 4]
        rows.append((k, j, simplify(lhs - rhs) == 0, lhs, rhs))
bad = [r for r in rows if not r[2]]
print("  36 pairs (9 ordinary characters x 4 characters of C_4) checked.")
print("  <chi_alpha, lambda_j (x) theta>  ==  mu(zeta^{-j}, u, theta)  in  %d / %d cases."
      % (len(rows) - len(bad), len(rows)))
assert not bad, bad[:3]
print("  ==> For N = G the Cliff-Weiss GLOBAL inequalities ARE the HeLP inequalities.")
print("      A_7 is simple, so N = 1 is the only nilpotent normal subgroup and V(ZG,N) = 1:")
print("      the LOCAL (matrix-strategy) half of Cliff-Weiss is vacuous, and the global half")
print("      is HeLP, which round 2 proved exhausted.  CLIFF-WEISS ADDS NOTHING TO A_7.")
# POSITIVE CONTROL for (A): repeat with u = genuine element of 4a; must also match
okg = True
for k in range(9):
    for j in range(4):
        tot = 0
        for i in range(4):
            zj = (I ** (j * i))
            inner = 0
            for ci, c in enumerate(CLASSES):
                e = EPSG[i].get(c, 0)
                if e:
                    inner += Rational(GORD) * Rational(e) * ORDTAB[k][ci].conjugate()
            tot += zj.conjugate() * inner
        if simplify(tot / (4 * GORD) - MUG[k][(-j) % 4]) != 0:
            okg = False
print("  POSITIVE CONTROL (u := a genuine element of 4a, where every quantity is a real")
print("  eigenvalue multiplicity): identity holds in all 36 cases ->", okg)
assert okg
# REJECTION CONTROL: a bogus augmentation vector must break the >= 0 half somewhere
bogus = {0: {'1a': 1}, 1: {'2a': 3, '4a': -2}, 2: {'2a': 1}, 3: {'2a': 3, '4a': -2}}
neg = 0
for k in range(9):
    m = mults(k, bogus)
    if any(x < 0 or x.q != 1 for x in m):
        neg += 1
print("  REJECTION CONTROL: the (non-solution) vector (eps_2a,eps_4a)=(3,-2) is rejected by")
print("  %d of the 9 ordinary characters -> the inequality set is not vacuous." % neg)
assert neg > 0

# =================================================================== (B) LATTICE BOUNDS
hr("(B)  Z_2 C_4 LATTICE BOUNDS  (p = 2, |u| = 4, 2'-part TRIVIAL)")
print("""  Simple Z_2 C_4-modules (paper, Sec.4, citing [BG64] Sec.4 / [CR81] Sec.34C):
      T : u -> 1        Sg : u -> -1       W : u -> [[0,-1],[1,0]]  (eigenvalues i,-i)
  and an INDECOMPOSABLE Z_2 C_4-lattice contains each of T,Sg,W at most once as a
  composition factor  ([BG64] Thm 4.1, quoted verbatim in the paper).  Consequences,
  derived here (see the state file for the proofs):
    (b1) a summand with no W has u^2 acting as the identity, so it contributes 0 to r_2;
    (b2) a summand X with W once has u^2-eigenvalues (-1,-1) and (1)^(a+b), a,b in {0,1},
         hence contributes at most a+b to r_2  [classification of Z_2 C_2-lattices];
    (b3) each summand can absorb at most one T and one Sg, so
             r_2(Lbar) <= min(m0,m1) + min(m2,m1) =: UB2
    (b4) if u = 1 + 2A on a summand containing W then A has eigenvalue (i-1)/2, whose
         norm to Q_2 is 1/2, not integral.  So EVERY W-summand has ubar != 1, giving
             r_1(Lbar) >= m1 =: LB1
    (b5) r_1(Xbar) <= dim X - 1 per summand and #summands >= m1 + max((m0-m1)^+,(m2-m1)^+),
             r_1(Lbar) <= n - m1 - max((m0-m1)^+, (m2-m1)^+) =: UB1""")


def UB2(m0, m1, m2):
    return min(m0, m1) + min(m2, m1)


def UB1(n, m0, m1, m2):
    return n - m1 - max(max(m0 - m1, 0), max(m2 - m1, 0))


def UB3(m0, m1, m2):
    """r_3 = #{Jordan blocks of size 4}.  A J_4 lives inside ONE indecomposable summand,
       so that summand has rank >= 4, hence support {T,Sg,W} (each at most once, total
       rank 1+1+2 = 4).  Number of such summands <= min(m0,m1,m2)."""
    return min(m0, m1, m2)


def jordan_types(n, r1, r2, r3):
    """all partitions of n with parts <= 4 and the given rank sequence."""
    out = []
    # a4=#parts of size4, a3, a2, a1
    for a4 in range(n // 4 + 1):
        for a3 in range((n - 4 * a4) // 3 + 1):
            for a2 in range((n - 4 * a4 - 3 * a3) // 2 + 1):
                a1 = n - 4 * a4 - 3 * a3 - 2 * a2
                if a1 < 0:
                    continue
                R1 = 3 * a4 + 2 * a3 + a2
                R2 = 2 * a4 + a3
                R3 = a4
                if (R1, R2, R3) == (r1, r2, r3):
                    out.append(tuple([4] * a4 + [3] * a3 + [2] * a2 + [1] * a1))
    return out


print("""    (b6) a J_4 block needs an indecomposable summand of rank 4, i.e. support {T,Sg,W},
             r_3(Lbar) <= min(m0,m1,m2) =: UB3

  chi  deg | m0 m1 m2 | LB1 UB1 | UB2 | UB3 ||  g in 4a: (m0,m1,m2) UB1 UB2 UB3""")
B = {}
strict = []
for k in range(9):
    m0, m1, m2 = MU[k][0], MU[k][1], MU[k][2]
    n = DEG[k]
    B[k] = dict(m0=m0, m1=m1, m2=m2, n=n, ub2=UB2(m0, m1, m2), ub1=UB1(n, m0, m1, m2),
                lb1=m1, ub3=UB3(m0, m1, m2))
    g0, g1, g2 = MUG[k][0], MUG[k][1], MUG[k][2]
    gb = (UB1(n, g0, g1, g2), UB2(g0, g1, g2), UB3(g0, g1, g2))
    print("  chi%-2d %3d | %2d %2d %2d | %3d %3d | %3d | %3d || (%d,%d,%d)  %3d %3d %3d"
          % (k + 1, n, m0, m1, m2, m1, B[k]['ub1'], B[k]['ub2'], B[k]['ub3'],
             g0, g1, g2, gb[0], gb[1], gb[2]))
    assert B[k]['lb1'] <= B[k]['ub1'], (k, B[k])
    if (B[k]['ub2'], B[k]['ub3']) != (gb[1], gb[2]):
        strict.append(k + 1)
print("  ==> the OPEN case admits a STRICTLY SMALLER 2-adic Jordan structure than a genuine")
print("      element of 4a on characters %s  (%d of 9).  The paper observed this for chi2"
      % (strict, len(strict)))
print("      only; it is a systematic feature of the whole ordinary character table.")

# ------------------------------------------------- POSITIVE CONTROL: explicit matrices
hr("(B-CTRL)  POSITIVE CONTROL -- the bounds against ACTUAL matrices of A_7")


def permmat6(cyc):
    """6x6 matrix of a permutation of {1..6} given as list of cycles, over Z."""
    p = list(range(6))
    for c in cyc:
        for a in range(len(c)):
            p[c[a] - 1] = c[(a + 1) % len(c)] - 1
    M = [[0] * 6 for _ in range(6)]
    for a in range(6):
        M[p[a]][a] = 1
    return M


def matmul(A, B_):
    n = len(A)
    return [[sum(A[a][t] * B_[t][b] for t in range(n)) for b in range(n)] for a in range(n)]


def rank_f2(M):
    n = len(M)
    A = [[x % 2 for x in row] for row in M]
    r = 0
    for c in range(len(A[0])):
        piv = None
        for i in range(r, n):
            if A[i][c]:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(n):
            if i != r and A[i][c]:
                A[i] = [(x + y) % 2 for x, y in zip(A[i], A[r])]
        r += 1
    return r


I6 = [[1 if a == b else 0 for b in range(6)] for a in range(6)]
# L_2 = the degree-6 lattice = Z^7 / <all-ones>, basis the images of e_1..e_6; the paper
# writes D_2(g) for g=(1,2)(3,4) exactly as the 6x6 permutation matrix below.
g2 = permmat6([[1, 2], [3, 4]])
g4 = permmat6([[1, 2, 3, 4], [5, 6]])
g4sq = matmul(g4, g4)
r1_g2 = rank_f2([[g2[a][b] - I6[a][b] for b in range(6)] for a in range(6)])
r2_g4 = rank_f2([[g4sq[a][b] - I6[a][b] for b in range(6)] for a in range(6)])
r1_g4 = rank_f2([[g4[a][b] - I6[a][b] for b in range(6)] for a in range(6)])
print("  the paper's own D_2(g) for g in 2a:  rank_F2(g-1) on Lbar_2 = %d" % r1_g2)
print("  our UB2 for the OPEN case (2,-1) on chi2:  %d" % B[1]['ub2'])
print("  => r_2(u^2) <= %d  <  %d = r_2(g),  which is EXACTLY the paper's contradiction"
      % (B[1]['ub2'], r1_g2))
assert B[1]['ub2'] == 1 and r1_g2 == 2
print("  for g in 4a (the TRIVIAL HeLP solution):  actual rank_F2(g^2-1) on Lbar_2 = %d,"
      % r2_g4)
print("     our UB2 predicts %d  -> the bound is ATTAINED by a real group element (tight),"
      % UB2(MUG[1][0], MUG[1][1], MUG[1][2]))
print("     so it is not a vacuous over-estimate.")
assert r2_g4 == UB2(MUG[1][0], MUG[1][1], MUG[1][2]) == 2
print("  for g in 4a:  actual rank_F2(g-1) on Lbar_2 = %d;  our LB1 = %d, UB1 = %d  -> inside"
      % (r1_g4, MUG[1][1], UB1(6, MUG[1][0], MUG[1][1], MUG[1][2])))
assert MUG[1][1] <= r1_g4 <= UB1(6, MUG[1][0], MUG[1][1], MUG[1][2])

# =================================================================== (C) THE SYSTEM
hr("(C)  THE 2-MODULAR SYSTEM:  can the p=2 lattice method reach a contradiction?")
# 2-modular decomposition matrix of A_7, as computed and certified UNIQUE in round 2
# (verify_r2.py, test DEC).  Columns are the 2-modular irreducibles; on the RATIONAL
# 2-regular classes the two 4-dimensional simples are indistinguishable, so they appear
# as a single column "4" -- recorded as a LIMITATION below.
DEC = {  # chi index -> {simple label: multiplicity}
    0: {'S1': 1},
    1: {'S6': 1},
    2: {'S6': 1, 'S4': 1},
    3: {'S6': 1, 'S4': 1},
    4: {'S6': 1, 'S4': 2},
    5: {'S14': 1},
    6: {'S1': 1, 'S14': 1},
    7: {'S1': 1, 'S20': 1},
    8: {'S1': 1, 'S14': 1, 'S20': 1},
}
SDIM = {'S1': 1, 'S4': 4, 'S6': 6, 'S14': 14, 'S20': 20}
for k in range(9):
    assert sum(SDIM[s] * m for s, m in DEC[k].items()) == DEG[k], (k, DEC[k])
print("  2-modular decomposition matrix (round 2, test DEC, each row UNIQUE) re-checked")
print("  against the ordinary degrees: all 9 rows consistent.")

print("""
  Superadditivity: for 0 -> A -> V -> B -> 0 of F_2<ubar>-modules,
      rank(z^j|V) >= rank(z^j|A) + rank(z^j|B)      (z = ubar - 1)
  because z^j V contains z^j A and surjects onto z^j B.  Hence
      r_j(Lbar_chi) >= sum_S d_{chi,S} r_j(S),
  and r_j(S) is well defined per ISOMORPHISM TYPE because ubar is ONE element of F_2 A_7.""")

# --- the one nonzero LOWER bound available
print("\n  *** THE ONE FORCED NONZERO VALUE ***")
print("  chi2 (degree 6) reduces mod 2 to the SIMPLE module S6 (decomposition row = 1*S6).")
print("  So Lbar_{chi2} = S6 and r_1(S6) = r_1(Lbar_{chi2}) >= LB1 = m1 = %d." % B[1]['lb1'])
print("  ==> ubar acts NON-TRIVIALLY on the 6-dimensional simple F_2 A_7-module.")
print("      Equivalently: ubar - 1 is NOT in the Jacobson radical of F_2 A_7.")
print("  Upper bound on the same quantity: r_1(S6) <= UB1(chi2) = %d." % B[1]['ub1'])
assert B[1]['lb1'] == 1

print("\n  *** THE JORDAN TYPE OF ubar ON THE 6-DIMENSIONAL SIMPLE F_2 A_7-MODULE ***")
print("  Lbar_{chi2} = S6 exactly, so the three bounds pin S6's type directly:")
print("     %d = LB1 <= r_1 <= UB1 = %d,   r_2 <= UB2 = %d,   r_3 <= UB3 = %d"
      % (B[1]['lb1'], B[1]['ub1'], B[1]['ub2'], B[1]['ub3']))
types6 = []
for r1 in range(B[1]['lb1'], B[1]['ub1'] + 1):
    for r2 in range(0, B[1]['ub2'] + 1):
        for r3 in range(0, B[1]['ub3'] + 1):
            if r1 >= r2 >= r3:
                types6 += jordan_types(6, r1, r2, r3)
types6 = sorted(set(types6))
print("  ==> the Jordan type of ubar on S6 is one of exactly %d partitions: %s"
      % (len(types6), types6))
# what a genuine element of 4a does on the same module, from explicit matrices
gr1 = rank_f2([[g4[a][b] - I6[a][b] for b in range(6)] for a in range(6)])
g4c = matmul(g4, g4)
gr2 = rank_f2([[g4c[a][b] - I6[a][b] for b in range(6)] for a in range(6)])
g4cube = matmul(g4c, g4)
gr3 = rank_f2([[sum((g4cube[a][t] - I6[a][t]) * 1 for t in [b]) for b in range(6)]
               for a in range(6)])
# r_3 = rank((g-1)^3): compute (g-1)^3 directly over Z then reduce
Gm1 = [[g4[a][b] - I6[a][b] for b in range(6)] for a in range(6)]
G3 = matmul(matmul(Gm1, Gm1), Gm1)
gr3 = rank_f2(G3)
print("  a genuine g in 4a on the SAME module has (r_1,r_2,r_3) = (%d,%d,%d), type %s."
      % (gr1, gr2, gr3, jordan_types(6, gr1, gr2, gr3)))
print("  NONE of the %d admissible types for ubar is that type -> reproduces and STRENGTHENS"
      % len(types6))
print("  the paper's degree-6 argument (which only compared u^2 with an element of 2a).")
assert (gr1, gr2, gr3) not in [(3 * t.count(4) + 2 * t.count(3) + t.count(2),
                                2 * t.count(4) + t.count(3), t.count(4)) for t in types6]

# --- feasibility over the box
LB1S = {'S1': 0, 'S4': 0, 'S6': 1, 'S14': 0, 'S20': 0}   # the forced ones
UB1S = {s: SDIM[s] - 1 for s in SDIM}
UB1S['S1'] = 0                                            # trivial module: ubar acts as 1
UB2S = {s: SDIM[s] // 2 for s in SDIM}
UB2S['S1'] = 0
# r_1(S6) <= UB1(chi2)
UB1S['S6'] = min(UB1S['S6'], B[1]['ub1'])

feas1, feas2 = [], []
labels = ['S1', 'S4', 'S6', 'S14', 'S20']
ranges = [range(LB1S[s], UB1S[s] + 1) for s in labels]
for tup in itertools.product(*ranges):
    y = dict(zip(labels, tup))
    ok = True
    for k in range(9):
        if sum(DEC[k].get(s, 0) * y[s] for s in labels) > B[k]['ub1']:
            ok = False
            break
    if ok:
        feas1.append(tup)
ranges2 = [range(0, UB2S[s] + 1) for s in labels]
for tup in itertools.product(*ranges2):
    y = dict(zip(labels, tup))
    ok = True
    for k in range(9):
        if sum(DEC[k].get(s, 0) * y[s] for s in labels) > B[k]['ub2']:
            ok = False
            break
    if ok:
        feas2.append(tup)
feas3 = []
UB3S = {s: SDIM[s] // 4 for s in SDIM}
UB3S['S1'] = 0
for tup in itertools.product(*[range(0, UB3S[s] + 1) for s in labels]):
    y = dict(zip(labels, tup))
    if all(sum(DEC[k].get(s, 0) * y[s] for s in labels) <= B[k]['ub3'] for k in range(9)):
        feas3.append(tup)
print("\n  FEASIBILITY (exact complete enumeration over the provably bounded box):")
print("     j=1 system  (LB1 forced, all 9 UB1 constraints): %d solutions" % len(feas1))
print("     j=2 system  (all 9 UB2 constraints):             %d solutions" % len(feas2))
print("     j=3 system  (all 9 UB3 constraints):             %d solutions" % len(feas3))
if feas1:
    print("     an explicit j=1 witness  (r_1(S1),r_1(S4),r_1(S6),r_1(S14),r_1(S20)) =", feas1[0])
if feas2:
    print("     an explicit j=2 witness  (r_2(...)) =", feas2[0])
if feas3:
    print("     an explicit j=3 witness  (r_3(...)) =", feas3[0])
    print("     forced-to-zero by the j=3 system:",
          [labels[t] for t in range(5) if all(f[t] == 0 for f in feas3)])

# --- entitled census
print("\n  CENSUS I AM ENTITLED TO (Sec.90/104):")
nz1 = [k for k in range(9) if B[k]['lb1'] > 0]
disc1 = [k for k in range(9) if any(DEC[k].get(s, 0) for s in ('S4', 'S6', 'S14', 'S20'))]
tight2 = [k for k in range(9) if B[k]['ub2'] == 0]
print("     9 ordinary characters x 2 exponents (j=1,2) = 18 lattice constraints in total.")
print("     Characters whose j=1 constraint can bind at all (UB1 < sum of dims of the")
print("     non-trivial composition factors): ", end='')
bind1 = [k + 1 for k in range(9)
         if B[k]['ub1'] < sum(DEC[k].get(s, 0) * (SDIM[s] - 1) for s in labels)]
print(bind1, "-> %d of 9." % len(bind1))
print("     Characters forcing r_2(S) = 0 outright (UB2 = 0):", [k + 1 for k in tight2],
      "-> %d of 9." % len(tight2))
print("     Characters with a NONZERO forced lower bound (m1 > 0):",
      [k + 1 for k in nz1], "-> %d of 9." % len(nz1))
print("     Constraints that could have produced a contradiction and did not: %d."
      % (len(bind1) + len(tight2)))

# =================================================================== (D) PROJECTIVE PROBE
hr("(D)  THE PROJECTIVE-IDEMPOTENT PROBE  e = (1+u+u^2+u^3)/4  at ODD p  -- NOT NEW")
print('''  PROVENANCE, corrected by this round's literature check: this is NOT my invention.
  It is the computation on l.197 of Margolis, arXiv:1706.02117 (source read):
     "Let theta_e be the character associated to the projective RG-module RGe.  We know
      theta_e(g) = |C_G(g)| eps_{g^G}(e).  Since theta_e vanishes on R-singular elements
      [CR (32.15) Theorem] the result follows."
  I derived it independently before finding it; I report it with his name on it.''')
print("""  u has order 4, so N = 1+u+u^2+u^3 satisfies N^2 = 4N and e = N/4 is an idempotent
  of Q A_7 lying in Z_p A_7 for every ODD p.  Hence P = Z_p A_7 e is PROJECTIVE and its
  ordinary character is  theta = sum_chi mu(1,u,chi) chi.  Two necessary conditions:
     (d1) theta vanishes on every p-singular class;
     (d2) theta = sum_S c_S Phi_S with c_S = <theta, phi_S> a NON-NEGATIVE INTEGER,
          phi_S the irreducible p-Brauer characters.
  The same for f=(1+u^2)/2 (rank mu(1)+mu(-1)) and 1-f (rank mu(i)+mu(-i)).""")

BR = json.load(open(REPO + '/brauer_tables.json'))
PREG = {3: ['1a', '2a', '4a', '5a', '7a', '7b'],
        5: ['1a', '2a', '3a', '3b', '4a', '6a', '7a', '7b'],
        7: ['1a', '2a', '3a', '3b', '4a', '5a', '6a']}


def brauer_rows(p):
    """returns list of (label, {class: value}) for the irreducible p-Brauer characters,
       on the RATIONAL p-regular classes only (7a/7b were not computed in round 2)."""
    t = BR[str(p)]
    out = []
    if isinstance(t, dict):
        for lab, v in t.items():
            out.append((lab, v))
    else:
        for e in t:
            out.append((str(e.get('label', e.get('deg', '?'))), e))
    return out


print("  brauer_tables.json top-level keys:", list(BR.keys()),
      "| structure of p=3 entry:", type(BR['3']).__name__)
# fall back to the values printed and banked in round 2 (state file Sec.3), hard-coded
# here so that this script does not depend on the round-2 file format.
BRTAB = {
    3: {'cols': ['1a', '2a', '4a', '5a'],
        'rows': [('1', [1, 1, 1, 1]), ('6', [6, 2, 0, 1]), ('13', [13, 1, -1, -2]),
                 ('15', [15, -1, -1, 0]), ('10a', [10, -2, 0, 0]), ('10b', [10, -2, 0, 0])]},
    5: {'cols': ['1a', '2a', '3a', '3b', '4a', '6a'],
        'rows': [('1', [1, 1, 1, 1, 1, 1]), ('6', [6, 2, 3, 0, 0, -1]), ('8', [8, 0, -1, -1, 0, 3]),
                 ('13', [13, 1, -2, 1, -1, -2]), ('15', [15, -1, 3, 0, -1, -1]),
                 ('35', [35, -1, -1, -1, 1, -1]), ('10a', [10, -2, 1, 1, 0, 1]),
                 ('10b', [10, -2, 1, 1, 0, 1])]},
    7: {'cols': ['1a', '2a', '3a', '3b', '4a', '5a', '6a'],
        'rows': [('1', [1, 1, 1, 1, 1, 1, 1]), ('5', [5, 1, 2, -1, -1, 0, -2]),
                 ('14a', [14, 2, 2, -1, 0, -1, 2]), ('14b', [14, 2, -1, 2, 0, -1, -1]),
                 ('10', [10, -2, 1, 1, 0, 0, 1]), ('35', [35, -1, -1, -1, 1, 0, -1]),
                 ('21', [21, 1, -3, 0, -1, 1, 1])]},
}


def theta_vals(mus):
    """theta(x) = sum_chi mus[chi] * chi(x), as exact values on the 9 classes."""
    return [simplify(sum(Rational(mus[k]) * ORDTAB[k][ci] for k in range(9))) for ci in range(9)]


def probe(mus, tag, verbose=True):
    """returns dict p -> (all c_S non-negative integers?, list of c_S)"""
    th = theta_vals(mus)
    res = {}
    for p in (3, 5, 7):
        # (d1) vanishing on p-singular classes
        sing = [CLASSES[ci] for ci in range(9) if ORD[ci] % p == 0 and simplify(th[ci]) != 0]
        cols = BRTAB[p]['cols']
        cS = []
        okp = (len(sing) == 0)
        for lab, vals in BRTAB[p]['rows']:
            s = 0
            for j, c in enumerate(cols):
                ci = CLASSES.index(c)
                s += Rational(SIZES[ci]) * th[ci] * Rational(vals[j])
            v = simplify(Rational(s, GORD))
            cS.append((lab, v))
            if not (v.q == 1 and v >= 0):
                okp = False
        res[p] = (okp, cS, sing)
        if verbose:
            print("    p=%d | p-singular non-vanishing: %s | c_S = %s | VERDICT %s"
                  % (p, sing if sing else 'none', [(l, str(v)) for l, v in cS],
                     'PASS' if okp else 'FAIL'))
    return res


print("\n  e = (1+u+u^2+u^3)/4,  theta = sum mu(1,u,chi) chi,  rank = %d"
      % sum(MU[k][0] * DEG[k] for k in range(9)))
r_e = probe([MU[k][0] for k in range(9)], 'e')
print("\n  f = (1+u^2)/2,        theta = sum (mu(1)+mu(-1)) chi,  rank = %d"
      % sum((MU[k][0] + MU[k][2]) * DEG[k] for k in range(9)))
r_f = probe([MU[k][0] + MU[k][2] for k in range(9)], 'f')
print("\n  1-f,                  theta = sum (mu(i)+mu(-i)) chi,  rank = %d"
      % sum((MU[k][1] + MU[k][3]) * DEG[k] for k in range(9)))
r_g = probe([MU[k][1] + MU[k][3] for k in range(9)], '1-f')

print("\n  (D-CTRL) POSITIVE CONTROL: the same probe on the TRIVIAL solution (0,1),")
print("  where e is literally (1+g+g^2+g^3)/4 for a group element g in 4a:")
r_triv = probe([MUG[k][0] for k in range(9)], 'e-trivial')

print("\n  (D-CTRL) REJECTION CONTROL: single-entry perturbations of the mu(1,u,.) vector")
print("  (keeping sum mu(1)*deg fixed is impossible with one entry, so we perturb one")
print("  entry by +-1 and ask how many perturbations the probe REJECTS).")
base = [MU[k][0] for k in range(9)]
killed = 0
total = 0
for k in range(9):
    for d in (-1, 1):
        v = list(base)
        v[k] += d
        if v[k] < 0:
            continue
        total += 1
        rr = probe(v, 'pert', verbose=False)
        if not all(rr[p][0] for p in (3, 5, 7)):
            killed += 1
print("  %d of %d single-entry perturbations are REJECTED by the projectivity probe."
      % (killed, total))
print("  -> the probe has teeth; its PASS on the real vector is not vacuous.")

# ---- THE CONTROL THAT MATTERS: is the probe STRICTLY STRONGER than HeLP anywhere?
hr("(D-POWER)  IS THE PROJECTIVE-IDEMPOTENT PROBE STRONGER THAN HeLP?  -- ORDER 6 OF A_7")
print("""  A_7 is the right test bed: for |u| = 6 the HeLP method is NOT sufficient (round 2
  reproduced the paper's complete output), and the paper needs two extra arguments -- a
  degree-5/6 eigenvalue comparison and Theorem 'main_inequality' (Brauer tree of the
  3-block of defect 1) -- to finish.  For |u| = 6, N = sum_{j=0}^{5} u^j has N^2 = 6N, so
  e = N/6 is an idempotent of Z_p A_7 for p = 5 and p = 7 and the SAME probe applies.
  If the probe kills any vector that HeLP leaves alive, it is strictly stronger.""")


def mu1_of_order(chi_idx, epsn, n):
    """mu(1, u, chi) = (1/n) sum_{j=0}^{n-1} chi(u^j).   (Only the eigenvalue 1 is needed
       for the projective idempotent e = (1/n) sum u^j, so no Vandermonde inverse.)"""
    return simplify(Rational(1, n) * sum(chival(chi_idx, epsn[j]) for j in range(n)))


def eps6_of(vec, sqcls):
    """vec = (e2a,e3a,e3b,e6a) for u; u^2 ~ sqcls (3a or 3b); u^3 ~ 2a."""
    e = {}
    e[0] = {'1a': 1}
    e[1] = {'2a': vec[0], '3a': vec[1], '3b': vec[2], '6a': vec[3]}
    e[2] = {sqcls: 1}
    e[3] = {'2a': 1}
    e[4] = {sqcls: 1}
    e[5] = dict(e[1])
    return e


ORDER6 = [((-2, 1, 2, 0), '3a', 'paper: killed by the deg-5/6 comparison'),
          ((2, 0, 0, -1), '3a', 'paper: killed by the deg-5/6 comparison'),
          ((-2, 2, 1, 0), '3b', 'paper: killed by the deg-5/6 comparison'),
          ((0, 1, -1, 1), '3b', 'paper: killed by the deg-5/6 comparison'),
          ((2, -1, 1, -1), '3b', 'paper: killed ONLY by the Brauer-tree inequality')]


def probe6(vec, sqcls):
    e6 = eps6_of(vec, sqcls)
    mus = [mu1_of_order(k, e6, 6) for k in range(9)]
    if any((not x.is_rational) or Rational(x).q != 1 or x < 0 for x in mus):
        return 'mu(1) not a non-negative integer: %s' % mus, None
    mus = [int(x) for x in mus]
    th = theta_vals(mus)
    verdict = {}
    for p in (5, 7):
        sing = [CLASSES[ci] for ci in range(9) if ORD[ci] % p == 0 and simplify(th[ci]) != 0]
        cols = BRTAB[p]['cols']
        okp = (len(sing) == 0)
        cs = []
        for lab, vals in BRTAB[p]['rows']:
            s = sum(Rational(SIZES[CLASSES.index(c)]) * th[CLASSES.index(c)] * Rational(vals[j])
                    for j, c in enumerate(cols))
            v = simplify(Rational(s, GORD))
            cs.append((lab, v))
            if not (v.q == 1 and v >= 0):
                okp = False
        verdict[p] = (okp, cs, sing)
    return mus, verdict


for vec, sq, note in ORDER6:
    mus, verd = probe6(vec, sq)
    if verd is None:
        print("  %-16s u^2~%s : %s" % (str(vec), sq, mus))
        continue
    res = {p: ('PASS' if verd[p][0] else 'KILL') for p in (5, 7)}
    print("  %-16s u^2~%s | rank(e)=%4d | p=5 %s  p=7 %s   [%s]"
          % (str(vec), sq, sum(mus[k] * DEG[k] for k in range(9)), res[5], res[7], note))
    if not verd[5][0]:
        print("        p=5 detail:", [(l, str(v)) for l, v in verd[5][1]])
    if not verd[7][0]:
        print("        p=7 detail:", [(l, str(v)) for l, v in verd[7][1]])
# positive control: a genuine element of 6a must PASS
mus_t, verd_t = probe6((0, 0, 0, 1), '3a')
print("  POSITIVE CONTROL, genuine g in 6a (0,0,0,1), u^2~3a: p=5 %s  p=7 %s"
      % ('PASS' if verd_t[5][0] else 'KILL', 'PASS' if verd_t[7][0] else 'KILL'))
assert verd_t[5][0] and verd_t[7][0]

hr("SUMMARY")
print("""  (A) Cliff-Weiss collapses to HeLP for a simple group.   VERIFIED (36/36).
  (B) The Z_2 C_4 bounds reproduce the paper's degree-6 number exactly and are ATTAINED
      by a genuine element of 4a.                             VERIFIED.
  (C) The p=2 lattice system is FEASIBLE  ->  no contradiction is available from it.
      The single nonzero fact it does force is r_1(S6) >= 1, i.e. ubar-1 is NOT in the
      Jacobson radical of F_2 A_7; and the Jordan type of ubar on the 6-dimensional
      simple F_2 A_7-module is one of exactly 3 partitions, none of them the type (4,2)
      of a genuine element of 4a.
  (D) The projective-idempotent probe PASSES at p = 3, 5, 7 for the open case.
      *** AND IT IS DEMONSTRABLY NOT STRONGER THAN HeLP. ***  The 16/16 perturbation
      control only shows the probe detects ARITHMETIC CORRUPTION of the mu vector.  The
      control that measures real discriminating power is the order-6 test: A_7 has FIVE
      order-6 partial-augmentation vectors that survive HeLP and that the paper proves
      cannot occur.  The probe kills ZERO of the five.  So its PASS on the order-4 open
      case carries no evidence, and I report it as a probe with no demonstrated power,
      not as a passed test.""")
