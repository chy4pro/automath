"""
r4_alt.py -- ROUND 4, line zc1a7.   owner-zc1a7.

A GENERIC alternating-group engine, used this round for TWO jobs:

  JOB 1 (control):  recompute the ordinary character table of A_7 on the rational
        classes as the Brauer table at a prime p NOT dividing |A_7| (there F_p A_7
        is semisimple and Brauer characters ARE ordinary characters).  This is a
        THIRD independent derivation of the r1 table (r1: Murnaghan-Nakayama;
        r1 verify: Dixon mod 421).

  JOB 2 (the round-4 question):  A_6 <= A_7 with EXACT class matching:
        A_6-class (2,2)   is contained in A_7-class 2a
        A_6-class (4,2)   is contained in A_7-class 4a
        Hence a unit of order 4 in V(Z_2 A_6) with A_6-partial augmentations
        (eps_2a, eps_4a) = (2,-1) IS, verbatim, a unit of V(Z_2 A_7) with
        (eps_2a, eps_4a) = (2,-1).   A_6 is therefore a candidate CONSTRUCTION
        SITE for the round-4 existence question -- and (ZC1) for A_6 is a THEOREM
        (Hertweck 2008), so we learn exactly WHICH argument kills it and whether
        that argument survives 2-localisation.

EXACT arithmetic only: integers mod p, Fraction, sympy Rational.  No floating point.
Interpreter: .venv/bin/python3 (3.9.6, sympy 1.14.0).
"""
import itertools
import sys
from collections import deque
from fractions import Fraction

from sympy import Poly, symbols, cyclotomic_poly, divisors, mobius, Rational, Integer

import meataxe as MA

X = symbols('x')


def log(*a):
    print(*a)
    sys.stdout.flush()


# ============================================================ generic group code

class Alt:
    def __init__(self, n):
        self.n = n
        self.gens = self._gens()
        self.words = self._bfs()
        self.elts = list(self.words)
        self.classes, self.reps = self._classes()

    def _gens(self):
        n = self.n
        a = tuple([1, 2, 0] + list(range(3, n)))                     # (1 2 3)
        if n % 2 == 1:
            b = tuple(list(range(1, n)) + [0])                       # n-cycle (n odd -> even perm)
        else:
            b = tuple([0] + list(range(2, n)) + [1])                 # (2 3 ... n), n-1 odd
        return [a, b]

    def mul(self, x, y):
        return tuple(x[y[i]] for i in range(self.n))

    def _bfs(self):
        ident = tuple(range(self.n))
        words = {ident: []}
        q = deque([ident])
        while q:
            g = q.popleft()
            for gi, s in enumerate(self.gens):
                h = self.mul(s, g)
                if h not in words:
                    words[h] = [gi] + words[g]
                    q.append(h)
        return words

    def cycle_type(self, p):
        seen = [False] * self.n
        t = []
        for i in range(self.n):
            if not seen[i]:
                j, L = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = p[j]
                    L += 1
                t.append(L)
        return tuple(sorted(t, reverse=True))

    def order(self, p):
        from math import gcd
        o = 1
        for c in self.cycle_type(p):
            o = o * c // gcd(o, c)
        return o

    def _classes(self):
        seen = set()
        classes = []
        for g in self.elts:
            if g in seen:
                continue
            orb = set()
            stack = [g]
            while stack:
                x = stack.pop()
                if x in orb:
                    continue
                orb.add(x)
                for s in self.gens:
                    si = self.inv(s)
                    stack.append(self.mul(self.mul(s, x), si))
            seen |= orb
            classes.append(sorted(orb))
        classes.sort(key=lambda c: (self.order(c[0]), -len(c), self.cycle_type(c[0])))
        return classes, [c[0] for c in classes]

    def inv(self, p):
        q = [0] * self.n
        for i, v in enumerate(p):
            q[v] = i
        return tuple(q)

    def pw(self, p, k):
        r = tuple(range(self.n))
        for _ in range(k):
            r = self.mul(r, p)
        return r

    def class_of(self, g):
        for i, c in enumerate(self.classes):
            if g in c:
                return i
        raise KeyError

    def rational_classes(self):
        """indices of classes C with g ~ g^k for every k coprime to |g|"""
        from math import gcd
        out = []
        for i, r in enumerate(self.reps):
            o = self.order(r)
            if all(self.class_of(self.pw(r, k)) == i
                   for k in range(1, o) if gcd(k, o) == 1):
                out.append(i)
        return out


# ============================================================ modules / Brauer

def perm_module(G, points, act, p):
    idx = {x: i for i, x in enumerate(points)}
    d = len(points)
    out = []
    for s in G.gens:
        M = [[0] * d for _ in range(d)]
        for x in points:
            M[idx[act(s, x)]][idx[x]] = 1
        out.append(M)
    return out


def word_matrix(word, gens_mats, p):
    d = len(gens_mats[0][0])
    M = MA.mat_id(d)
    for gi in word:
        M = MA.mat_mul(M, gens_mats[gi], p)
    return M


def brauer_value(Mg, m, p):
    d = len(Mg)
    total, val = 0, 0
    for dd in divisors(m):
        Phi = Poly(cyclotomic_poly(dd, X), X, modulus=p)
        facs = Phi.factor_list()[1]
        mults = []
        for f, e in facs:
            assert e == 1, "cyclotomic poly not squarefree mod p"
            cs = [int(c) % p for c in reversed(f.all_coeffs())]
            deg = len(cs) - 1
            nul = len(Mg) - MA.rank(MA.poly_eval_mat(cs, Mg, p), p)
            assert nul % deg == 0
            mults.append(nul // deg)
            total += nul
        assert len(set(mults)) == 1, "class not rational: mults %s" % mults
        val += mults[0] * int(mobius(dd))
    assert total == d, "eigenvalue multiplicities do not sum to dim"
    return val


def chop_robust(mod, p):
    """MeatAxe chop with a wider random search than meataxe.chop's defaults
    (meataxe.py is left untouched so that the round-2 runs stay reproducible).
    The MeatAxe is Las Vegas: an 'undecided' return is a failure of the random
    search, never a mathematical statement.  Norton's criterion (used inside
    find_submodule) is an iff, so every 'irreducible' verdict is a proof."""
    out = []
    stack = [(mod, 1)]
    while stack:
        m, sd = stack.pop()
        n = len(m[0])
        if n == 0:
            continue
        status, data = None, None
        for attempt in range(10):
            status, data = MA.find_submodule(
                m, p, tries=40, seed=sd + 977 * attempt, max_nullity=5)
            if status != 'unknown':
                break
        if status == 'irreducible':
            out.append(m)
        elif status == 'reducible':
            W = data
            stack.append((MA.restrict(m, W, p), sd + 7))
            stack.append((MA.quotient(m, W, p), sd + 13))
        else:
            raise RuntimeError("MeatAxe undecided, dim %d, p=%d" % (n, p))
    return out


def all_irreducibles(G, p, target, log=log):
    irrs = []

    def add(m):
        d = len(m[0])
        for r in irrs:
            if r['dim'] == d and MA.hom_dim(m, r['gens'], p)[0] > 0:
                return False
        irrs.append({'gens': m, 'dim': d})
        return True

    n = G.n
    nat = perm_module(G, list(range(n)), lambda s, x: s[x], p)
    act_set = lambda s, x: tuple(sorted(s[i] for i in x))
    queue = [('nat', nat),
             ('pairs', perm_module(G, list(itertools.combinations(range(n), 2)), act_set, p)),
             ('triples', perm_module(G, list(itertools.combinations(range(n), 3)), act_set, p))]
    tensored = set()
    while len(irrs) < target:
        if not queue:
            # tensor PAIRS of already-found irreducibles, smallest total dimension
            # first.  (Tensoring everything with the natural module makes the
            # modules too big for the MeatAxe's random search on A_6.)
            pairs = [(irrs[a]['dim'] * irrs[b]['dim'], a, b)
                     for a in range(len(irrs)) for b in range(a, len(irrs))
                     if (a, b) not in tensored and irrs[a]['dim'] > 1]
            if not pairs:
                raise RuntimeError("out of module sources p=%d" % p)
            pairs.sort()
            _, a, b = pairs[0]
            tensored.add((a, b))
            queue.append(('(%d)(x)(%d)' % (irrs[a]['dim'], irrs[b]['dim']),
                          MA.tensor(irrs[a]['gens'], irrs[b]['gens'], p)))
        name, mod = queue.pop(0)
        for f in chop_robust(mod, p):
            add(f)
            if len(irrs) >= target:
                break
    return irrs


def brauer_table(G, p, log=log):
    """absolutely irreducible p-Brauer characters on the RATIONAL p-regular classes.
    For p not dividing |G| this is the ordinary table on rational classes."""
    order = len(G.elts)
    preg = [i for i in range(len(G.reps)) if G.order(G.reps[i]) % p != 0] if order % p == 0 \
        else list(range(len(G.reps)))
    rat = set(G.rational_classes())
    cols = [i for i in preg if i in rat]
    # BERMAN: #{irreducible F_p G-modules} = #{orbits of p-regular classes under g -> g^p}
    seen, n_orbits = set(), 0
    for i in preg:
        if i in seen:
            continue
        n_orbits += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = G.class_of(G.pw(G.reps[j], p))
    target = n_orbits
    log("   p=%-2d  %d p-regular classes; Berman orbit count (g -> g^p) = %d"
        % (p, len(preg), n_orbits))
    irrs = all_irreducibles(G, p, target, log=log)
    rows, ksum = [], 0
    for r in irrs:
        k, _ = MA.hom_dim(r['gens'], r['gens'], p)
        ksum += k
        vals = {}
        for c in cols:
            Mg = word_matrix(G.words[G.reps[c]], r['gens'], p)
            v = brauer_value(Mg, G.order(G.reps[c]), p)
            assert v % k == 0, "Galois division failed"
            vals[c] = v // k
        rows.append(dict(deg=r['dim'] // k, dim_fp=r['dim'], k=k, vals=vals))
    assert ksum == len(preg), ("completeness certificate FAILED at p=%d: "
                               "sum dim End(S) = %d != %d" % (p, ksum, len(preg)))
    log("   p=%-2d  %d absolutely irreducible Brauer characters, degrees %s"
        % (p, len(rows), sorted(r['deg'] for r in rows)))
    log("         completeness: sum_S dim End(S) = %d = #{p-regular classes}  OK" % ksum)
    return rows, cols


# ============================================================ HeLP, order 4

def mults4(deg, c2a, c4a, t):
    """multiplicities of 1, i, -1, -i for |u|=4, eps_2a=t, eps_4a=1-t, u^2 ~ 2a."""
    cu = t * c2a + (1 - t) * c4a
    out = []
    for k in range(4):
        re = [2, 0, -2, 0][k % 4]
        out.append(Rational(deg + c2a * (-1) ** k + cu * re, 4))
    return out


def help_order4(rows_by_name, i2a, i4a, box=range(-6, 7)):
    """rows_by_name: list of (label, deg, chi(2a), chi(4a)).  Returns dict t -> killers."""
    res = {}
    for t in box:
        killers = []
        for (lab, deg, c2, c4) in rows_by_name:
            m = mults4(deg, c2, c4, t)
            for k in range(4):
                if m[k].q != 1 or m[k] < 0:
                    killers.append("%s mu_%d=%s" % (lab, k, m[k]))
        res[t] = killers
    return res


# ============================================================ JOB 1  --  A_7 control

log("=" * 78)
log("r4_alt.py  --  ROUND 4, zc1a7")
log("=" * 78)
log("")
log("JOB 1 -- CONTROL: ordinary character table of A_7 on rational classes,")
log("         obtained as the Brauer table at p = 11 (11 does not divide |A_7| =")
log("         2520, so F_11 A_7 is semisimple and its Brauer characters are the")
log("         ordinary characters).  THIRD independent derivation.")
A7 = Alt(7)
log("   |A_7| = %d, %d conjugacy classes, cycle types %s"
    % (len(A7.elts), len(A7.classes), [A7.cycle_type(r) for r in A7.reps]))
rat7 = A7.rational_classes()
log("   rational classes: %s" % [A7.cycle_type(A7.reps[i]) for i in rat7])
rows11, cols11 = brauer_table(A7, 11)
i2a7 = [i for i in range(len(A7.reps)) if A7.cycle_type(A7.reps[i]) == (2, 2, 1, 1, 1)][0]
i4a7 = [i for i in range(len(A7.reps)) if A7.cycle_type(A7.reps[i]) == (4, 2, 1)][0]
tab11 = sorted([(r['deg'], r['vals'][i2a7], r['vals'][i4a7]) for r in rows11])
log("   (deg, chi(2a), chi(4a)) from p=11 : %s" % tab11)
EXPECT7 = sorted([(1, 1, 1), (6, 2, 0), (10, -2, 0), (10, -2, 0), (14, 2, 0),
                  (14, 2, 0), (15, -1, -1), (21, 1, -1), (35, -1, 1)])
log("   r1/r2 table (Murnaghan-Nakayama)  : %s" % EXPECT7)
assert tab11 == EXPECT7, "A_7 control FAILED"
log("   MATCH.  Control passed.")

# ============================================================ JOB 2  --  A_6

log("")
log("=" * 78)
log("JOB 2 -- A_6, the transfer site")
log("=" * 78)
A6 = Alt(6)
log("   |A_6| = %d, %d classes, cycle types %s"
    % (len(A6.elts), len(A6.classes), [A6.cycle_type(r) for r in A6.reps]))
rat6 = A6.rational_classes()
log("   rational classes: %s" % [A6.cycle_type(A6.reps[i]) for i in rat6])
i2a6 = [i for i in range(len(A6.reps)) if A6.cycle_type(A6.reps[i]) == (2, 2, 1, 1)][0]
i4a6 = [i for i in range(len(A6.reps)) if A6.cycle_type(A6.reps[i]) == (4, 2)][0]
log("   |2a| = %d, |4a| = %d" % (len(A6.classes[i2a6]), len(A6.classes[i4a6])))
log("   A_6 has exactly ONE class of involutions (%d classes of order 2) and ONE"
    % sum(1 for i in range(len(A6.reps)) if A6.order(A6.reps[i]) == 2))
log("   class of elements of order 4 (%d)."
    % sum(1 for i in range(len(A6.reps)) if A6.order(A6.reps[i]) == 4))

log("")
log("   THE FUSION (computed, not assumed): embed A_6 in A_7 as the stabiliser of")
log("   the point 7.  Cycle types are preserved with a fixed point added.")
log("      A_6 (2,2)   -> A_7 (2,2,1,1,1) = 2a")
log("      A_6 (4,2)   -> A_7 (4,2,1)     = 4a")
log("   so eps^{A_7}_{2a}(u) = eps^{A_6}_{2a}(u) and eps^{A_7}_{4a}(u) = eps^{A_6}_{4a}(u)")
log("   for any u in Z A_6, because 2a and 4a each receive exactly ONE A_6-class")
log("   and no other A_6-class of 2-power order exists.")
n2 = sum(1 for i in range(len(A6.reps)) if A6.order(A6.reps[i]) in (2, 4))
assert n2 == 2, "A_6 has more 2-power classes than expected"

log("")
log("   ordinary table of A_6 on rational classes, via p = 7 (7 does not divide 360):")
rows7, _ = brauer_table(A6, 7)
ORD6 = [("ord deg %d" % r['deg'], r['deg'], r['vals'][i2a6], r['vals'][i4a6]) for r in rows7]
for lab, d, c2, c4 in sorted(ORD6, key=lambda z: z[1]):
    log("      %-12s chi(2a)=%-3d chi(4a)=%-3d  %s"
        % (lab, c2, c4, "DISTINGUISHES" if c2 != c4 else "blind"))

log("")
log("   complete modular Brauer tables of A_6 at the ADMISSIBLE primes 3 and 5")
log("   (p must not divide |u| = 4):")
MOD6 = []
for p in (3, 5):
    rows, cols = brauer_table(A6, p)
    for r in rows:
        if i2a6 in r['vals'] and i4a6 in r['vals']:
            MOD6.append(("%d-mod deg %d" % (p, r['deg']), r['deg'],
                         r['vals'][i2a6], r['vals'][i4a6]))
for lab, d, c2, c4 in MOD6:
    log("      %-14s phi(2a)=%-3d phi(4a)=%-3d  %s"
        % (lab, c2, c4, "DISTINGUISHES" if c2 != c4 else "blind"))

log("")
log("   HeLP for |u| = 4 in V(Z A_6) / V(Z_2 A_6), eps_2a = t, eps_4a = 1-t:")


def cong2(t):
    return (1 - t - 1) % 2 == 0


res_ord = help_order4(ORD6, i2a6, i4a6)
res_all = help_order4(ORD6 + MOD6, i2a6, i4a6)
log("      t  | ordinary only | +cong(p=2) | + 3-,5-modular")
log("     ----+---------------+------------+----------------")
two_local6, global6 = [], []
for t in range(-4, 5):
    o = not res_ord[t]
    a = not res_all[t]
    if o and cong2(t):
        two_local6.append(t)
        if a:
            global6.append(t)
    log("     %3d | %-13s | %-10s | %s"
        % (t, "SURVIVES" if o else "killed(%d)" % len(res_ord[t]),
           ("SURVIVES" if cong2(t) else "killed") if o else "-",
           ("SURVIVES" if a else "killed by " + res_all[t][0]) if o and cong2(t) else "-"))
log("")
log("   ==> 2-LOCAL admissible set for |u|=4 in V(Z_2 A_6):  t in %s" % two_local6)
log("   ==> GLOBAL admissible set for |u|=4 in V(Z A_6):     t in %s" % global6)

log("")
log("   INTERPRETATION (this is the point of JOB 2):")
if 2 in global6:
    log("      (2,-1) SURVIVES the complete global HeLP system for A_6 as well.")
    log("      So HeLP does NOT settle order 4 for A_6 either; Hertweck's proof of")
    log("      (ZC1) for A_6 must kill it by another argument.")
else:
    log("      (2,-1) is killed GLOBALLY for A_6 by: %s"
        % (res_all[2][0] if res_all[2] else "the p=2 congruence"))
    if 2 in two_local6:
        log("      but it SURVIVES 2-localisation (the killer is an odd-p Brauer")
        log("      character, which a unit of V(Z_2 A_6) does not have to satisfy).")
        log("      ==> the A_6 analogue of the ROUND-4 QUESTION IS OPEN TOO, in a group")
        log("          where (ZC1) is a THEOREM.  A_6 is NOT excluded as a construction")
        log("          site by HeLP.")
    else:
        log("      and it is killed 2-locally as well -> A_6 is excluded as a")
        log("      construction site.")

log("")
log("   CONTROLS for JOB 2")
log("     positive: t = 0 (a genuine g in 4a) must survive everything: %s"
    % ("OK" if (not res_all[0]) and cong2(0) else "FAILED"))
assert (not res_all[0]) and cong2(0)
log("     rejection: t = 3, 4, -3, -4 must be killed by ordinary characters alone:")
for t in (3, 4, -3, -4):
    assert res_ord[t], "rejection control failed at t=%d" % t
    log("        t=%3d killed by %d ordinary inequalities, e.g. %s"
        % (t, len(res_ord[t]), res_ord[t][0]))
log("     rejection: t = 1, -1 must be ordinary-admissible but killed by the")
log("                p = 2 congruence:")
for t in (1, -1):
    assert (not res_ord[t]) and (not cong2(t))
    log("        t=%3d OK" % t)

log("")
log("done.")
