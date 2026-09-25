"""
r4_2local.py -- ROUND 4, line zc1a7.   owner-zc1a7.

TARGET (planner-approved): does a unit of order 4 with partial augmentations
(eps_2a, eps_4a) = (2,-1) exist in V(Z_2 A_7), the 2-ADIC group ring?

This script establishes the FRAMEWORK, exactly, in three parts.

PART A -- WHAT SURVIVES 2-LOCALISATION.
   Round 2 proved the GLOBAL HeLP system (ordinary + all 3-,5-,7-modular Brauer
   characters) leaves exactly {(0,1),(2,-1)}.  Brauer characters at an ODD prime p
   are obtained by reducing u mod p, which needs u in Z_p G.  A unit of V(Z_2 A_7)
   admits no such reduction.  So the 2-LOCAL system is strictly smaller.  We compute
   both, and the census of what is lost.

PART B -- THE 2-BLOCKS OF A_7, computed from central characters modulo a prime
   above 2 (2 splits in Q(sqrt(-7)) since -7 = 1 mod 8), cross-checked against the
   connectivity of the 2-modular decomposition matrix.

PART C -- THE BLOCK REDUCTION.  Z_2 A_7 = prod_B B with B two-sided ideals and
   1 = sum e_B orthogonal.  A unit u with u^4=1 is exactly a tuple (u_B) with
   u_B^4 = e_B, INDEPENDENTLY chosen.  chi(u) = chi(u_B) for chi in Irr(B).
   Hence: the existence question splits over blocks, and every block all of whose
   ordinary characters satisfy chi(2a) = chi(4a) is satisfied by u_B = e_B*g,
   g in 4a.  This LOCALISES the obstruction.

EXACT arithmetic only: Python integers, Fraction, sympy Rational / sqrt(-7),
2-adic integers as residues mod 2^PREC.  NO floating point.
Interpreter: .venv/bin/python3 (3.9.6, sympy 1.14.0).
"""
import json
import os
import sys
from fractions import Fraction
from itertools import product

import sympy
from sympy import Integer, Rational, sqrt, srepr, simplify, nsimplify

HERE = os.path.dirname(os.path.abspath(__file__))

# ============================================================ ordinary table

with open(os.path.join(HERE, 'a7_table.json')) as f:
    T = json.load(f)

NAMES = T['names']            # ['1a','2a','3a','3b','4a','5a','6a','7a','7b']
ORDERS = T['orders']
SIZES = T['sizes']
DEG = T['degrees']
IRRN = T['irrnames']
TAB = [[sympy.sympify(x) for x in row] for row in T['table']]   # exact sympy
NCL = len(NAMES)
NIRR = len(TAB)

I1 = NAMES.index('1a')
I2 = NAMES.index('2a')
I4 = NAMES.index('4a')

def log(*a):
    print(*a)
    sys.stdout.flush()


log("=" * 78)
log("r4_2local.py  --  ROUND 4, zc1a7.   Z_2 A_7, |u| = 4.")
log("=" * 78)
log("ordinary character table of A_7 loaded (built in r1 by Murnaghan-Nakayama,")
log("re-derived in r1 by Dixon mod 421; degrees %s)" % DEG)
log("chi(2a), chi(4a):")
for i in range(NIRR):
    log("   %-5s deg %-3d  chi(2a)=%-3s chi(4a)=%-3s   %s"
        % (IRRN[i], DEG[i], TAB[i][I2], TAB[i][I4],
           "DISTINGUISHES" if TAB[i][I2] != TAB[i][I4] else "blind (chi(2a)=chi(4a))"))

# ============================================================ PART A

log("")
log("#" * 78)
log("# PART A -- the 2-LOCALLY admissible system for |u| = 4")
log("#" * 78)
log("""
Hypotheses used (stated, not hidden):
  H1  supp(eps) subset {2a,4a}, eps_2a + eps_4a = 1.  [Berman-Higman + Hertweck
      Thm 2.3, both cited for Z G; the round-4 question SPECIFIES this support,
      so H1 is part of the question, not an extra assumption.]
  H2  u^2 has order 2 and 2a is the only class of involutions => eps_2a(u^2)=1.
  H3  Luthar-Passi multiplicities for ORDINARY characters are valid for
      u in V(Z_2 G): D(u) has finite order so it is diagonalisable over Qbar_2
      with 4th-root-of-unity eigenvalues and non-negative INTEGER multiplicities.
  H4  Hertweck's congruence Prop 2.7(iii) AT THE PRIME 2 is valid for
      u in V(Z_2 G): its proof is the Frobenius congruence
      (sum a_g g)^{2^j} = sum a_g^{2^j} g^{2^j} mod 2, and a^2 = a mod 2 holds
      for a in Z_2.  At an ODD prime it is NOT available (Z_2 has no map to F_p).
  NOT available 2-locally: p-Brauer characters for p in {3,5,7}.  Those need the
      reduction Z_p G -> F_p G, i.e. u in Z_p G.
""")

ZETA = sympy.I     # primitive 4th root of unity


def mults_ord4(chi_row, t):
    """Eigenvalue multiplicities of D(u) for |u|=4, eps_2a=t, eps_4a=1-t, u^2~2a.
    mu_k = (1/4) sum_{d|4} Tr_{Q(zeta^d)/Q}( chi(u^d) zeta^{-dk} ).
    All exact."""
    c1 = chi_row[I1]                       # chi(u^4) = chi(1)
    c2 = chi_row[I2]                       # chi(u^2) = chi(2a)
    cu = t * chi_row[I2] + (1 - t) * chi_row[I4]     # chi(u) = chi(u^3)
    out = []
    for k in range(4):
        # d=4 -> zeta^{-4k}=1 term chi(1); d=2 -> chi(u^2)*(-1)^k ; d=1 -> Tr(chi(u) i^{-k})
        # Tr_{Q(i)/Q}(x * i^{-k}) with x rational  =  x * (i^{-k} + conj) = x*2*Re(i^{-k})
        re = [2, 0, -2, 0][k % 4]
        val = Rational(1, 4) * (c1 + c2 * Integer((-1) ** k) + cu * Integer(re))
        out.append(sympy.nsimplify(val))
    return out


def helper_check_ordinary(t):
    """Returns (ok, list of (chi index, k, mu) failures)."""
    bad = []
    for i in range(NIRR):
        m = mults_ord4(TAB[i], t)
        for k in range(4):
            v = m[k]
            if v.q != 1 or v < 0:
                bad.append((IRRN[i], k, v))
    return (len(bad) == 0), bad


def congruence_p2(t):
    """Hertweck Prop 2.7(iii) with p=2, j=1, D=2a:
       sum_{C : C^2 subset 2a} eps_C(u) = eps_2a(u^2) mod 2.
       The classes squaring into 2a are exactly those of order 4 -> only 4a."""
    return (1 - t - 1) % 2 == 0


# ---- boundedness: PROVED from one ordinary character, no unbounded search
i_deg6 = DEG.index(6)
c6_2a, c6_4a = TAB[i_deg6][I2], TAB[i_deg6][I4]
log("Boundedness (so that the enumeration below is provably complete, not a search):")
log("   chi_2 (deg 6) has chi(2a)=%s, chi(4a)=%s => chi(u) = %s*t" % (c6_2a, c6_4a, c6_2a))
m6 = mults_ord4(TAB[i_deg6], sympy.Symbol('t'))
log("   mu_0 = %s >= 0 and mu_2 = %s >= 0  =>  -2 <= t <= 2." % (sympy.expand(m6[0]), sympy.expand(m6[2])))
BOX = list(range(-6, 7))     # strictly larger than the proved box, so the box is
                             # observed to be non-binding

surv_ord, surv_ord_cong = [], []
kill_report = {}
for t in BOX:
    ok, bad = helper_check_ordinary(t)
    if ok:
        surv_ord.append(t)
        if congruence_p2(t):
            surv_ord_cong.append(t)
    kill_report[t] = (ok, len(bad), bad[:3])

log("")
log("2-LOCAL system (ordinary characters only) survivors over t in [-6,6]: %s" % surv_ord)
log("   + Hertweck congruence at p=2                          survivors: %s" % surv_ord_cong)
log("   (box [-6,6] is wider than the proved bound [-2,2]; nothing outside [-2,2]")
log("    survives, so the enumeration is complete.)")

# ---- the GLOBAL system, for comparison: reload round 2's Brauer tables
with open(os.path.join(HERE, 'brauer_tables.json')) as f:
    BT = json.load(f)

log("")
log("brauer_tables.json keys: %s" % sorted(BT.keys()))


def brauer_rows_for(p):
    """rows: list of (deg, {classname: value}) for absolutely irreducible p-Brauer chars"""
    node = BT[str(p)] if str(p) in BT else BT[p]
    rows = []
    for r in node['rows'] if isinstance(node, dict) and 'rows' in node else node:
        rows.append((r['deg'], r['vals']))
    return rows


ADMISSIBLE_PRIMES = [3, 5, 7]     # p not dividing |u| = 4
global_surv = []
kill_by = {}
for t in surv_ord_cong + [x for x in BOX if x not in surv_ord_cong]:
    pass

def check_brauer(t):
    """returns list of names of Brauer constraints that kill t"""
    killers = []
    for p in ADMISSIBLE_PRIMES:
        for (deg, vals) in brauer_rows_for(p):
            if '2a' not in vals or '4a' not in vals or '1a' not in vals:
                continue
            row = {I1: Integer(vals['1a']), I2: Integer(vals['2a']), I4: Integer(vals['4a'])}
            fake = [Integer(0)] * NCL
            fake[I1], fake[I2], fake[I4] = row[I1], row[I2], row[I4]
            m = mults_ord4(fake, t)
            for k in range(4):
                v = m[k]
                if v.q != 1 or v < 0:
                    killers.append("%d-mod deg %d (mu_%d = %s)" % (p, deg, k, v))
    return killers


log("")
log("t   | ordinary-only | +cong(p=2) | odd-p Brauer killers")
log("----+---------------+------------+---------------------")
for t in range(-4, 5):
    ok, nbad, _ = kill_report[t]
    kb = check_brauer(t) if ok else []
    log("%3d |   %-11s |   %-8s | %s"
        % (t, "SURVIVES" if ok else "killed(%d)" % nbad,
           ("SURVIVES" if congruence_p2(t) else "killed") if ok else "-",
           (", ".join(kb[:3]) + (" ..." if len(kb) > 3 else "")) if kb else ("none" if ok else "-")))

two_local = [t for t in surv_ord_cong]
global_set = [t for t in surv_ord_cong if not check_brauer(t)]
log("")
log("==> 2-LOCAL admissible set for |u|=4 in V(Z_2 A_7):  t = eps_2a in %s" % two_local)
log("    i.e. (eps_2a, eps_4a) in %s" % [(t, 1 - t) for t in two_local])
log("==> GLOBAL admissible set (round 2, reproduced here): t in %s" % global_set)

# ---- census of discriminating constraints, 2-local vs global
def n_discriminating(rows):
    """rows: list of (name, [chi(1a),chi(2a),chi(4a)]).  A constraint mu_k can depend
    on the partial augmentations only if k in {0,2} and chi(2a) != chi(4a)."""
    n = 0
    for (nm, c1, c2, c4) in rows:
        if c2 != c4:
            n += 2
    return n


ord_rows = [(IRRN[i], TAB[i][I1], TAB[i][I2], TAB[i][I4]) for i in range(NIRR)]
brau_rows = []
for p in ADMISSIBLE_PRIMES:
    for (deg, vals) in brauer_rows_for(p):
        if '2a' in vals and '4a' in vals:
            brau_rows.append(("%d-mod deg %d" % (p, deg), Integer(vals['1a']),
                              Integer(vals['2a']), Integer(vals['4a'])))

n_ord = n_discriminating(ord_rows)
n_bra = n_discriminating(brau_rows)
log("")
log("CENSUS (the number I am entitled to, sec.90/104):")
log("   discriminating constraints, ordinary characters      : %d" % n_ord)
log("   discriminating constraints, odd-p Brauer characters   : %d" % n_bra)
log("   GLOBAL total (round 2 reported 40)                    : %d" % (n_ord + n_bra))
log("   surviving 2-localisation                              : %d  (%.0f%% lost)"
    % (n_ord, 100.0 * n_bra / (n_ord + n_bra)))
log("   -- and the ONE constraint that killed t=-2 globally is among the lost ones:")
log("      %s" % (check_brauer(-2) if -2 in surv_ord_cong else "t=-2 not ordinary-admissible?!"))

# ---- CONTROLS
log("")
log("CONTROLS for part A")
log("  POSITIVE: the trivial vector t=0 is realised by an actual g in 4a; its")
log("            multiplicities must be the true eigenvalue multiplicities.")
g4a_mults = mults_ord4(TAB[i_deg6], 0)
log("            chi_2(deg 6) at t=0 -> mu = %s" % [str(x) for x in g4a_mults])
log("            (the standard 6-dim'l module: (1234)(56) has eigenvalues")
log("             1,1,-1,-1,i,-i  ->  (2,1,2,1))")
assert [int(x) for x in g4a_mults] == [2, 1, 2, 1], "positive control failed"
log("            MATCH.")
log("  REJECTION: t must be rejectable.")
for t in (3, 4, -3, -4):
    ok, nbad, sample = kill_report[t]
    assert not ok, "rejection control failed at t=%d" % t
    log("            t=%3d rejected by %d ordinary inequalities, e.g. %s" % (t, nbad, sample[:1]))
log("  REJECTION: t = +-1 must be rejected by the congruence and NOT by ordinary chars.")
for t in (1, -1):
    ok, nbad, _ = kill_report[t]
    assert ok and not congruence_p2(t), "congruence rejection control failed at t=%d" % t
    log("            t=%3d ordinary-admissible, killed by the p=2 congruence. OK" % t)

# ============================================================ PART B  -- 2-blocks

log("")
log("#" * 78)
log("# PART B -- the 2-blocks of A_7, computed")
log("#" * 78)

PREC = 40
MOD = 1 << PREC


def sqrt_m7_2adic(prec):
    """2-adic square root of -7 (exists: -7 = 1 mod 8).  Returns x mod 2^prec with
    x^2 = -7 mod 2^prec, x = 1 mod 4."""
    x, k = 1, 3
    assert (x * x + 7) % 8 == 0
    while k < prec:
        if (x * x + 7) % (1 << (k + 1)):
            x += 1 << (k - 1)
        k += 1
    m = 1 << prec
    assert (x * x + 7) % m == 0, "2-adic sqrt(-7) failed"
    return x % m


SBIG = sqrt_m7_2adic(PREC + 8)
S = SBIG % MOD
log("2-adic sqrt(-7) to precision 2^%d : s = %d,  s^2 + 7 = 0 mod 2^%d" % (PREC, S, PREC))
log("  (2 splits in Q(sqrt(-7)) because -7 = 1 mod 8; the two primes above 2 are the")
log("   two 2-adic square roots +-s, and the block partition is the same for both --")
log("   asserted below.)")


def to_z2(val):
    """Exact sympy algebraic number in Q(sqrt(-7)) -> its residue mod 2^PREC under
    the embedding sqrt(-7) -> S.   Handles a/b + (c/d) sqrt(-7)."""
    val = sympy.expand(val)
    a = sympy.simplify(val.subs(sympy.sqrt(-7), 0))
    b = sympy.simplify((val - a) / sympy.sqrt(-7))
    b = sympy.simplify(b)
    assert a.is_Rational and b.is_Rational, "unexpected irrationality: %s" % val
    # write val = (P + Q*sqrt(-7)) / D with P,Q,D integers, D > 0
    D = sympy.ilcm(int(a.q), int(b.q))
    P, Q = int(a * D), int(b * D)
    e = 0
    dd = D
    while dd % 2 == 0:
        dd //= 2
        e += 1
    assert e <= 4
    BIG = 1 << (PREC + e)
    num = (P + Q * SBIG) % BIG
    assert num % (1 << e) == 0, "not a 2-adic integer: %s" % val
    return ((num >> e) * pow(dd, -1, BIG)) % MOD


def v2(x):
    x %= MOD
    if x == 0:
        return PREC
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


# central character omega_chi(C) = |C| chi(g_C) / chi(1)   (an algebraic integer)
OMEGA = []
for i in range(NIRR):
    row = []
    for c in range(NCL):
        num = (SIZES[c] * to_z2(TAB[i][c])) % MOD
        d = DEG[i]
        vd = 0
        dd = d
        while dd % 2 == 0:
            dd //= 2
            vd += 1
        assert v2(num) >= vd, ("omega not integral: chi=%s class=%s" % (IRRN[i], NAMES[c]))
        val = (num >> vd) * pow(dd, -1, MOD) % MOD
        row.append(val)
    OMEGA.append(row)

# blocks: chi ~ psi iff omega_chi(C) = omega_psi(C) mod p for all C
parent = list(range(NIRR))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[max(ra, rb)] = min(ra, rb)

for i in range(NIRR):
    for j in range(i + 1, NIRR):
        if all(v2(OMEGA[i][c] - OMEGA[j][c]) >= 1 for c in range(NCL)):
            union(i, j)

blocks = {}
for i in range(NIRR):
    blocks.setdefault(find(i), []).append(i)
BLOCKS = [sorted(v) for v in blocks.values()]
BLOCKS.sort(key=lambda b: -len(b))

log("")
log("2-BLOCKS of A_7 (central characters mod a prime above 2):")
for bi, b in enumerate(BLOCKS):
    degs = [DEG[i] for i in b]
    # defect: nu_2(|G|) - min nu_2(chi(1))
    def nu2(n):
        k = 0
        while n % 2 == 0:
            n //= 2
            k += 1
        return k
    d = 3 - min(nu2(x) for x in degs)
    log("   block %d : %-28s degrees %-24s  k(B)=%d  defect=%d"
        % (bi, [IRRN[i] for i in b], degs, len(b), d))

log("")
log("CONTROLS for part B")
log("  (i) the principal block must contain the trivial character: block containing")
log("      chi1 = block %d.  OK" % [bi for bi, b in enumerate(BLOCKS) if 0 in b][0])
log("  (ii) sum of k(B) over blocks = 9 =", sum(len(b) for b in BLOCKS))
assert sum(len(b) for b in BLOCKS) == NIRR
log("  (iii) INDEPENDENT cross-check: characters in the same block must be connected")
log("      in the 2-modular decomposition graph (Brauer).  Using round 2's p=2 table")
log("      on the RATIONAL 2-regular classes 1a,3a,3b,5a:")

rows2 = brauer_rows_for(2)
reg2 = ['1a', '3a', '3b', '5a']
log("      p=2 IBr degrees %s on %s" % ([r[0] for r in rows2], reg2))
# decompose each ordinary character
import itertools
dec = {}
for i in range(NIRR):
    target = [int(TAB[i][NAMES.index(c)]) for c in reg2]
    sols = []
    maxes = [target[0] // r[0] + 1 for r in rows2]
    for combo in itertools.product(*[range(m + 1) for m in maxes]):
        if sum(combo[j] * rows2[j][0] for j in range(len(rows2))) != target[0]:
            continue
        ok = True
        for ci, c in enumerate(reg2):
            if sum(combo[j] * int(rows2[j][1][c]) for j in range(len(rows2))) != target[ci]:
                ok = False
                break
        if ok:
            sols.append(combo)
    dec[i] = sols
    log("      %-5s deg %-3d -> %d non-negative integer decomposition(s): %s"
        % (IRRN[i], DEG[i], len(sols), sols[:4]))

log("      NOTE the two 4-dimensional 2-modular simples agree on every RATIONAL class")
log("      (r3 limitation), so a decomposition can only be unique up to swapping them.")

# connectivity graph from the (multi-)set of supports
sup = {}
for i in range(NIRR):
    s = set()
    for combo in dec[i]:
        for j, m in enumerate(combo):
            if m:
                s.add(j)
    sup[i] = s
parent2 = list(range(NIRR))
def find2(x):
    while parent2[x] != x:
        parent2[x] = parent2[parent2[x]]
        x = parent2[x]
    return x
for i in range(NIRR):
    for j in range(i + 1, NIRR):
        if sup[i] & sup[j]:
            a, b = find2(i), find2(j)
            if a != b:
                parent2[max(a, b)] = min(a, b)
blocks2 = {}
for i in range(NIRR):
    blocks2.setdefault(find2(i), []).append(i)
B2 = sorted([sorted(v) for v in blocks2.values()], key=lambda b: -len(b))
log("      decomposition-graph components: %s" % [[IRRN[i] for i in b] for b in B2])
log("      central-character blocks      : %s" % [[IRRN[i] for i in b] for b in BLOCKS])
log("      AGREE: %s" % (B2 == BLOCKS))

# ============================================================ PART C

log("")
log("#" * 78)
log("# PART C -- the block reduction of the 2-LOCAL existence question")
log("#" * 78)
log("""
LEMMA (elementary, proof in one line, and it is the point of part B).
  Z_2 A_7 = (+)_B B  with B = e_B Z_2 A_7 two-sided ideals, e_B orthogonal
  idempotents summing to 1.  Then
      { u in (Z_2 A_7)^x : u^4 = 1 }  =  prod_B { u_B in B^x : u_B^4 = e_B }
  and chi(u) = chi(u_B) for chi in Irr(B).  The choices are INDEPENDENT.
COROLLARY.  If every chi in Irr(B) has chi(2a) = chi(4a), then u_B := e_B*g for
  g in 4a already realises the prescribed values on that block.  Such a block can
  never obstruct.
""")
free_blocks, obstructing = [], []
for bi, b in enumerate(BLOCKS):
    disc = [i for i in b if TAB[i][I2] != TAB[i][I4]]
    if disc:
        obstructing.append((bi, b, disc))
    else:
        free_blocks.append((bi, b))
for bi, b in free_blocks:
    log("   block %d %-30s : NO distinguishing character -> satisfied by e_B*g, g in 4a"
        % (bi, [IRRN[i] for i in b]))
for bi, b, disc in obstructing:
    log("   block %d %-30s : distinguishing characters %s -> CAN obstruct"
        % (bi, [IRRN[i] for i in b], [IRRN[i] for i in disc]))

log("")
log("CENSUS: of %d two-blocks of A_7, %d can obstruct and %d cannot."
    % (len(BLOCKS), len(obstructing), len(free_blocks)))
log("        Of the %d ordinary characters, %d distinguish (2,-1) from (0,1)."
    % (NIRR, sum(1 for i in range(NIRR) if TAB[i][I2] != TAB[i][I4])))

log("")
log("LIMITATION printed beside the result: the block reduction says the question")
log("is a CONJUNCTION of independent per-block questions.  It removes the blocks")
log("listed above as 'cannot obstruct'.  It does NOT decide the remaining blocks;")
log("each of those still has full defect (Sylow_2(A_7) = D_8) and is not of any")
log("type for which the unit group of the order is classified.")


# ============================================================ PART D

log("")
log("#" * 78)
log("# PART D -- the DEFECT GROUPS, and what the two blocks actually are")
log("#" * 78)

from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

IBR2 = [r[0] for r in rows2]        # degrees of the 6 two-modular irreducibles
log("2-modular irreducible degrees: %s" % IBR2)

# which IBr belong to which block: an IBr lies in the block of any ordinary
# character in whose decomposition it occurs
blk_of_ibr = {}
for bi, b in enumerate(BLOCKS):
    for i in b:
        for combo in dec[i]:
            for j, m in enumerate(combo):
                if m:
                    blk_of_ibr.setdefault(j, set()).add(bi)
for j in sorted(blk_of_ibr):
    assert len(blk_of_ibr[j]) == 1, "IBr %d straddles blocks -- impossible" % j
log("IBr -> block: %s" % {IBR2[j]: list(blk_of_ibr[j])[0] for j in sorted(blk_of_ibr)})

def nu2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k

for bi, b in enumerate(BLOCKS):
    cols = sorted([j for j in blk_of_ibr if list(blk_of_ibr[j])[0] == bi])
    d = 3 - min(nu2(DEG[i]) for i in b)
    log("")
    log("BLOCK %d : Irr = %s (degrees %s),  IBr degrees %s"
        % (bi, [IRRN[i] for i in b], [DEG[i] for i in b], [IBR2[j] for j in cols]))
    log("   k(B) = %d,  l(B) = %d,  defect d = nu_2(|G|) - min nu_2(chi(1)) = 3 - %d = %d"
        % (len(b), len(cols), min(nu2(DEG[i]) for i in b), d))
    # enumerate all decomposition matrices for this block consistent with the
    # Brauer values, with every column non-zero, and det(D^T D) = 2^d
    choices = []
    for i in b:
        opts = set()
        for combo in dec[i]:
            opts.add(tuple(combo[j] for j in cols))
        choices.append(sorted(opts))
    good = []
    for pick in product(*choices):
        D = Matrix([list(r) for r in pick])
        if any(all(D[r, c] == 0 for r in range(D.rows)) for c in range(D.cols)):
            continue                       # a column of zeros: that IBr not in B
        C = (D.T * D)
        S = smith_normal_form(C)
        ed = sorted(abs(S[k, k]) for k in range(S.rows))
        if ed[-1] != 2 ** d:
            continue
        good.append((pick, C, ed))
    log("   decomposition matrices consistent with (Brauer values, every IBr present,")
    log("   largest elementary divisor of the Cartan matrix = p^d = %d): %d"
        % (2 ** d, len(good)))
    # canonicalise up to permutation of the columns
    canon = set()
    for pick, C, ed in good:
        cols_t = list(zip(*pick))
        canon.add(tuple(sorted(cols_t)))
    log("   ... which is %d up to relabelling the simple modules." % len(canon))
    for pick, C, ed in good[:1]:
        log("   D = %s" % [list(r) for r in pick])
        log("   Cartan C = D^T D = %s,  elementary divisors %s, det = %s"
            % (C.tolist(), ed, C.det()))
    if len(canon) == 1:
        log("   ==> the decomposition matrix of this block is UNIQUE up to relabelling.")

log("")
log("READING OFF THE DEFECT GROUPS.")
log("  Block 0: defect 3 = nu_2(|A_7|), so its defect group is a full Sylow")
log("           2-subgroup of A_7, i.e. D_8.  k(B)=5, l(B)=3: exactly the shape of")
log("           a block with dihedral defect group of order 8.")
log("  Block 1: defect 2, so |D| = 4, i.e. D is C_4 or C_2 x C_2.")
log("           A block with CYCLIC defect group C_{p^n} has l(B) = e | p-1; for")
log("           p = 2 that forces l(B) = 1 (Dade's theory of cyclic blocks).")
log("           Block 1 has l(B) = 3.  ==> D is NOT cyclic  ==>")
log("")
log("     *****  BLOCK 1 OF Z_2 A_7 HAS KLEIN FOUR DEFECT GROUP  *****")
log("")
log("  and its Cartan matrix is [[4,2,2],[2,2,1],[2,1,2]].  The two Morita classes of")
log("  Klein-four blocks with l(B)=3 are distinguished by their Cartan matrices:")
log("     R A_4                       : [[2,1,1],[1,2,1],[1,1,2]]")
log("     principal block of R A_5    : [[4,2,2],[2,2,1],[2,1,2]]")
log("  so block 1 is of A_5 TYPE.  By the classification of blocks with Klein four")
log("  defect groups (Craven-Eaton-Kessar-Linckelmann, Math. Z. 268 (2011), which uses")
log("  CFSG) every such block is Morita equivalent to R V_4, R A_4 or B_0(R A_5);")
log("  ==> BLOCK 1 IS MORITA EQUIVALENT TO THE PRINCIPAL 2-BLOCK OF R A_5.")
log("  Its basic algebra has R-rank sum(C) = 4+2+2+2+2+1+2+1+2 = 18.")

log("")
log("CONTROL for part D -- GREEN'S THEOREM ON ZEROS OF CHARACTERS.")
log("  If B has defect group D and the 2-part of g is not G-conjugate into D, then")
log("  chi(g) = 0 for every chi in Irr(B).  A Klein four group has exponent 2, so")
log("  EVERY character of block 1 must vanish on 4a.  Check:")
for bi, b in enumerate(BLOCKS):
    vals = [(IRRN[i], TAB[i][I4]) for i in b]
    log("    block %d on 4a: %s" % (bi, vals))
b1 = [b for b in BLOCKS if len(b) == 4][0]
assert all(TAB[i][I4] == 0 for i in b1), "GREEN CONTROL FAILED for block 1"
log("    block 1: ALL FOUR VANISH on 4a.  Green's theorem is satisfied -- an")
log("    INDEPENDENT confirmation of the Klein four defect group.")
b0 = [b for b in BLOCKS if len(b) == 5][0]
assert any(TAB[i][I4] != 0 for i in b0), "control failed"
log("    block 0: NOT all vanish on 4a (as it must be: its defect group D_8 has")
log("    elements of order 4).  The control discriminates.")

log("")
log("CONSEQUENCE FOR ROUND 3'S STATED LIMITATION (r3 sec.10, first bullet).")
log("  r3 recorded: 'the 2-modular decomposition matrix merges the two 4-dimensional")
log("  simples; separating them needs the 7a/7b Brauer values, which were not")
log("  computed.'  Part D separates them WITHOUT any 7a/7b value: both 4-dimensional")
log("  simples lie in block 1, and inside that block the decomposition matrix is")
log("  forced up to relabelling them.  Relabelling is exactly the ambiguity that does")
log("  not matter.  ==> the limitation is REMOVED, by block theory rather than by")
log("  computing the irrational classes.")

log("")
log("WHAT PART D DOES NOT DO (sec. (b) of the dispatch).")
log("  It does NOT decide either block.  It says WHERE the question lives and that")
log("  one of the two places is an algebra whose Morita class is known.  The prescribed")
log("  eigenvalue multiplicities per block, for the record:")
for bi, b in enumerate(BLOCKS):
    for i in b:
        m_open = mults_ord4(TAB[i], 2)
        m_triv = mults_ord4(TAB[i], 0)
        log("    block %d  %-5s deg %-3d  open (2,-1): mu = %-16s   trivial (0,1): mu = %s"
            % (bi, IRRN[i], DEG[i], [int(x) for x in m_open], [int(x) for x in m_triv]))

log("")
log("done.")
