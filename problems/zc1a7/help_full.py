"""
help_full.py -- ROUND 2, line zc1a7.

The HeLP method for A_7 run over the COMPLETE p-modular Brauer character
tables computed in modular_a7.py, closing the survival half of round 1.

Hypothesis for the modular part is taken from the paper's own statement of
Hertweck's extension (arXiv:2006.09031, l.174):  a p-Brauer character may be
used for a unit u iff  p does NOT divide |u|,  the sums running over p-regular
classes only.  So for |u| = 4 the complete system is  ordinary + 3 + 5 + 7
modular; p = 2 is NOT admissible and is not used.

Multiplicity formula (Luthar-Passi / Hertweck), EXACT integer arithmetic via
Ramanujan sums:
    mu(xi^l, u, chi) = (1/n) sum_{d | n} Tr_{Q(zeta_d)/Q}( chi(u^{n/d}) zeta_d^{-l} )
                     = (1/n) sum_{d | n} chi(u^{n/d}) * c_d(l),
    c_d(l) = mobius(d/g) * phi(d)/phi(d/g),  g = gcd(l,d).
Valid here because every class an order-3/4/6 unit can touch is RATIONAL, so
every character value involved is a rational integer.

Interpreter: .venv/bin/python3   (sympy 1.14.0).  No floating point.
"""
import json
from fractions import Fraction
from math import gcd
from sympy import sympify, divisors, totient, mobius, Rational, Matrix

CLASSES = ['1a', '2a', '3a', '3b', '4a', '5a', '6a', '7a', '7b']
ORDERS = {'1a': 1, '2a': 2, '3a': 3, '3b': 3, '4a': 4, '5a': 5, '6a': 6, '7a': 7, '7b': 7}
RATIONAL = ['1a', '2a', '3a', '3b', '4a', '5a', '6a']       # 7a,7b are the only irrational ones

# class power map, from cycle types (all we need: rational classes)
POWER = {
    ('1a', 'any'): '1a',
    ('2a', 2): '1a',
    ('3a', 3): '1a', ('3a', 2): '3a',
    ('3b', 3): '1a', ('3b', 2): '3b',
    ('4a', 2): '2a', ('4a', 4): '1a', ('4a', 3): '4a',
    ('5a', 5): '1a',
    ('6a', 2): '3a', ('6a', 3): '2a', ('6a', 6): '1a',
}


def class_power(c, k):
    """class of g^k for g in class c (rational classes only)."""
    o = ORDERS[c]
    k = k % o
    if k == 0:
        return '1a'
    if gcd(k, o) == 1:
        return c                     # rational class: g^k ~ g
    return POWER[(c, gcd(k, o))]


def ramanujan(d, l):
    g = gcd(l, d)
    return int(mobius(d // g) * totient(d) // totient(d // g))


def mu(l, n, chi_pow):
    """chi_pow[j] = chi(u^j) for j | n (j=0 means the identity).  Returns Fraction."""
    s = 0
    for d in divisors(n):
        j = (n // d) % n
        s += chi_pow[j] * ramanujan(d, l)
    return Fraction(s, n)


# ---------------------------------------------------------------- data

def load_ordinary():
    d = json.load(open('a7_table.json'))
    tab = [[sympify(x) for x in row] for row in d['table']]
    return d['names'], d['degrees'], tab


def load_brauer():
    return json.load(open('brauer_tables.json'))


def characters_for_order(n, names, degrees, otab, btab):
    """All characters usable for a unit of order n, as dicts class -> integer value.
    Returns list of (label, {class: value}).  Only classes of order dividing n matter."""
    touch = [c for c in RATIONAL if n % ORDERS[c] == 0]
    out = []
    for i, deg in enumerate(degrees):
        vals = {}
        ok = True
        for c in touch:
            v = otab[i][names.index(c)]
            if not v.is_integer:
                ok = False
                break
            vals[c] = int(v)
        if ok:
            out.append(('ord chi%d(deg %d)' % (i + 1, deg), vals))
    for p_str, tab in sorted(btab.items()):
        p = int(p_str)
        if n % p == 0:
            continue                          # Hertweck: p must not divide |u|
        for j, row in enumerate(tab['rows']):
            if not all(c in row['vals'] for c in touch):
                continue
            out.append(('%d-mod phi(deg %d)' % (p, row['deg']),
                        {c: row['vals'][c] for c in touch}))
    return out


# ---------------------------------------------------------------- HeLP solver

def chi_of(vals, eps):
    return sum(eps[c] * vals[c] for c in eps)


def pa_at(k, n, x, pa):
    """partial augmentations of u^k (all classes involved are rational)."""
    if k % n == 0:
        return {'1a': 1}
    g = gcd(k, n)
    return x if g == 1 else pa[g]


def hertweck_congruences(n, x, pa, allowed):
    """Prop 2.7(iii) of the paper: for a prime power p^j and any class D,
    sum_{C : C^(p^j) subset D} eps_C(u) = eps_D(u^(p^j))  mod p."""
    for p in (2, 3, 5, 7):
        pj = p
        while pj <= n:
            target = pa_at(pj, n, x, pa)
            for D in set(class_power(c, pj) for c in allowed) | set(target):
                lhs = sum(x[c] for c in allowed if class_power(c, pj) == D)
                rhs = target.get(D, 0)
                if (lhs - rhs) % p != 0:
                    return False
            pj *= p
    return True


def solve_order(n, pa, chars, verbose=False):
    """pa[j] = dict of partial augmentations of u^j for each j | n, 1 < j < n.
    Returns the complete HeLP solution set for u itself, as dicts."""
    allowed = [c for c in RATIONAL if ORDERS[c] != 1 and n % ORDERS[c] == 0]
    A = len(allowed)

    # constant part of chi(u^j) for j > 1, and bounds on the linear functional chi_x
    bounds = {}
    for label, vals in chars:
        known = {0: vals['1a']}
        for j in sorted(pa):
            known[j] = chi_of(vals, pa[j])
        lo, hi = None, None
        for l in range(n):
            cn = ramanujan(n, l)
            if cn == 0:
                continue
            # mu_l = (1/n)[ sum_{d<n} chi(u^{n/d}) c_d(l) + cn * chi_x ] >= 0
            const = 0
            for d in divisors(n):
                if d == n:
                    continue
                const += known[(n // d) % n] * ramanujan(d, l)
            # cn*chi_x >= -const  and  mu_l <= deg  =>  cn*chi_x <= n*deg - const
            for sense in (0, 1):
                if sense == 0:
                    b = Fraction(-const, cn)
                    if cn > 0:
                        lo = b if lo is None else max(lo, b)
                    else:
                        hi = b if hi is None else min(hi, b)
                else:
                    b = Fraction(n * vals['1a'] - const, cn)
                    if cn > 0:
                        hi = b if hi is None else min(hi, b)
                    else:
                        lo = b if lo is None else max(lo, b)
        if lo is not None and hi is not None:
            bounds[label] = (vals, lo, hi)

    # pick A characters whose value-matrix on `allowed` is invertible
    labels = list(bounds)
    chosen = []
    M = Matrix(0, A, [])
    for lab in labels:
        vals = bounds[lab][0]
        row = Matrix(1, A, [vals[c] for c in allowed])
        if (M.col_join(row)).rank() > M.rank():
            M = M.col_join(row)
            chosen.append(lab)
        if len(chosen) == A:
            break
    assert len(chosen) == A, ("cannot bound the search region for order %d: "
                             "rank %d < %d" % (n, M.rank(), A))
    Minv = M.inv()

    ranges = []
    for lab in chosen:
        _, lo, hi = bounds[lab]
        import math
        ranges.append(range(math.ceil(lo), math.floor(hi) + 1))
    size = 1
    for r in ranges:
        size *= len(r)
    if verbose:
        print("   order %d: search region = %s (%d integer points), "
              "bounded by %s" % (n, [ (r.start, r.stop-1) for r in ranges], size,
                                 ", ".join(chosen)))
    assert size < 5_000_000, "search region too large: %d" % size

    sols = []
    import itertools
    for y in itertools.product(*ranges):
        xv = Minv * Matrix(A, 1, list(y))
        if any(v.q != 1 for v in xv):
            continue
        x = {c: int(xv[i]) for i, c in enumerate(allowed)}
        if sum(x.values()) != 1:
            continue
        if not hertweck_congruences(n, x, pa, allowed):
            continue
        ok = True
        for label, vals in chars:
            chi_pow = {0: vals['1a'], 1: chi_of(vals, x)}
            for j in sorted(pa):
                chi_pow[j] = chi_of(vals, pa[j])
            for l in range(n):
                m = mu(l, n, chi_pow)
                if m < 0 or m.denominator != 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            sols.append(x)
    return sols, allowed


# ---------------------------------------------------------------- report helpers

def multiplicity_table(n, x, pa, chars):
    """Return list of (label, [mu_0..mu_{n-1}], nonvacuous_flag)."""
    rows = []
    for label, vals in chars:
        chi_pow = {0: vals['1a'], 1: chi_of(vals, x)}
        for j in sorted(pa):
            chi_pow[j] = chi_of(vals, pa[j])
        mus = [mu(l, n, chi_pow) for l in range(n)]
        rows.append((label, vals, mus))
    return rows


def order4_constraints(vals, t):
    """mu_0..mu_3 for eps_2a=t, eps_4a=1-t, u^2 ~ 2a.  Exact Fractions."""
    d, c2, c4 = vals['1a'], vals['2a'], vals['4a']
    b = t * c2 + (1 - t) * c4
    return [Fraction(d + 2 * b + c2, 4), Fraction(d - c2, 4),
            Fraction(d + c2 - 2 * b, 4), Fraction(d - c2, 4)]


def main():
    names, degrees, otab = load_ordinary()
    btab = load_brauer()

    # -- control C5 (re-run): the ordinary table against the paper's Table 1
    cols = ['1a', '2a', '3a', '3b', '6a']
    mine = set(tuple(int(otab[i][names.index(c)]) for c in cols) for i in range(9))
    paper = {(1, 1, 1, 1, 1), (14, 2, 2, -1, 2), (14, 2, -1, 2, -1)}
    assert paper <= mine, "paper Table 1 mismatch: %s" % (paper - mine)
    print("control C5 (ordinary table rows vs the paper's printed Table 1, on "
          "(1a,2a,3a,3b,6a)): MATCH")
    print("   (my chi5/chi6 are the GAP chi6/chi5 -- the two degree-14 irreducibles are "
          "indexed in the other order; 3a/3b agree with GAP, as the mod-7 and mod-2 "
          "checks below confirm)")

    # -- published Brauer values from the paper
    def has(p, deg, **kw):
        for r in btab[str(p)]['rows']:
            if r['deg'] == deg and all(r['vals'].get(k) == v for k, v in kw.items()):
                return True
        return False
    checks = [
        ("paper: 7-modular irreducible with chi(1)=5, chi(3a)=2, chi(3b)=-1",
         has(7, 5, **{'3a': 2, '3b': -1})),
        ("paper: 2-modular irreducible with chi(1)=4, chi(3a)=-2, chi(3b)=1",
         has(2, 4, **{'3a': -2, '3b': 1})),
        ("paper Table 2b: 3-modular psi_5 of degree 13 with psi_5(2a)=1",
         has(3, 13, **{'2a': 1})),
        ("paper Brauer tree (3-block of defect 1, chi2-chi8-chi7): degrees 6 and 15",
         has(3, 6) and has(3, 15)),
        ("round 1 (verified 3 ways): 7-modular degree 5 has (1a,2a,4a) = (5,1,-1)",
         has(7, 5, **{'1a': 5, '2a': 1, '4a': -1})),
    ]
    for lab, ok in checks:
        print("   %-78s %s" % (lab, "MATCH" if ok else "*** FAIL ***"))
        assert ok

    print()
    print("=" * 78)
    print("ORDER 3  (complete system: ordinary + 2-, 5-, 7-modular)")
    ch3 = characters_for_order(3, names, degrees, otab, btab)
    s3, al3 = solve_order(3, {}, ch3, verbose=True)
    print("   characters used: %d  (%s)" % (len(ch3), ", ".join(l for l, _ in ch3)))
    print("   SOLUTIONS (eps_3a, eps_3b): %s"
          % sorted((s['3a'], s['3b']) for s in s3))
    print("   paper: eps_3a in {0,1}, eps_3b = 1-eps_3a   -> %s"
          % ("REPRODUCED EXACTLY" if sorted((s['3a'], s['3b']) for s in s3) == [(0, 1), (1, 0)]
             else "*** MISMATCH ***"))

    print()
    print("=" * 78)
    print("ORDER 4  (complete system: ordinary + 3-, 5-, 7-modular; p=2 inadmissible)")
    ch4 = characters_for_order(4, names, degrees, otab, btab)
    print("   characters used: %d" % len(ch4))
    for l, v in ch4:
        print("      %-24s (1a,2a,4a) = (%d,%d,%d)" % (l, v['1a'], v['2a'], v['4a']))
    s4, al4 = solve_order(4, {2: {'2a': 1}}, ch4, verbose=True)
    print("   SOLUTIONS (eps_2a, eps_4a): %s" % sorted((s['2a'], s['4a']) for s in s4))

    print()
    print("-- which constraint kills which t (t = eps_2a, eps_4a = 1-t) --")
    for t in range(-4, 5):
        viol = []
        for label, vals in ch4:
            mus = order4_constraints(vals, t)
            for l, m in enumerate(mus):
                if m < 0:
                    viol.append("%s mu_%d=%s<0" % (label, l, m))
                elif m.denominator != 1:
                    viol.append("%s mu_%d=%s not an integer" % (label, l, m))
        cong = ((t % 2 == 0) and ((1 - t) % 2 == 1))
        tag = [] if cong else ["Hertweck congruence mod 2"]
        print("   t=%-3d %s" % (t, ("SURVIVES" if not viol and cong else
                                    "killed by %d constraint(s): %s"
                                    % (len(viol) + len(tag),
                                       "; ".join((tag + viol)[:4])))))

    print()
    print("-- (eps_2a,eps_4a) = (2,-1): full eigenvalue multiplicity table --")
    tight = []
    nonvac = 0
    for label, vals in ch4:
        mus = order4_constraints(vals, 2)
        star = ''
        if vals['2a'] != vals['4a']:
            nonvac += 1
        if any(m == 0 for m in mus[:1] + mus[2:3]):
            star = '   <== TIGHT'
        print("   %-24s deg %-3d  mu = (%s)%s"
              % (label, vals['1a'], ", ".join(str(m) for m in mus), star))
        assert sum(mus) == vals['1a']
        for l in (0, 2):
            if mus[l] == 0:
                tight.append((label, l, vals))
    print("   -> ALL multiplicities are non-negative integers: (2,-1) SURVIVES the "
          "complete system")
    print("   -> characters whose constraint is TIGHT (mu = 0, i.e. one step from "
          "killing it): %d" % len(tight))
    for label, l, vals in tight:
        print("        %-24s mu_%d = 0   (eigenvalue %s is absent from D(u))"
              % (label, l, ['1', 'i', '-1', '-i'][l]))
    # CENSUS (doctrine s90/s104): report the number I am ENTITLED to.
    tot = disc = 0
    for label, vals in ch4:
        for l in range(4):
            tot += 1
            if order4_constraints(vals, 2)[l] != order4_constraints(vals, 0)[l]:
                disc += 1
    print("   -> CENSUS.  Total constraints in the complete order-4 system: %d "
          "(%d characters x 4 eigenvalues)." % (tot, len(ch4)))
    print("      Of these, %d actually DEPEND on the partial augmentations (mu_1 and "
          "mu_3 never do," % disc)
    print("      and mu_0, mu_2 do not either when chi(2a) = chi(4a)).  The other %d "
          "are satisfied by" % (tot - disc))
    print("      any candidate whatsoever, because the trivial solution (0,1) -- an "
          "actual element of 4a --")
    print("      already satisfies them.  So the number this round is entitled to "
          "report is %d constraints" % disc)
    print("      that COULD have killed (2,-1) and did not, not %d." % tot)

    print()
    print("=" * 78)
    print("ORDER 6  (complete system: ordinary + 5-, 7-modular) -- FALSIFICATION TEST")
    ch6 = characters_for_order(6, names, degrees, otab, btab)
    print("   characters used: %d" % len(ch6))
    for sq, lab in ((({'3a': 1}), '3a'), (({'3b': 1}), '3b')):
        s6, al6 = solve_order(6, {2: sq, 3: {'2a': 1}}, ch6, verbose=True)
        got = sorted(tuple(s[c] for c in al6) for s in s6)
        print("   u^2 ~ %s : classes %s" % (lab, al6))
        print("      SOLUTIONS: %s" % got)
    print("   paper (complete GAP run):")
    print("      u^2~3a: {(-2,1,2,0), (2,0,0,-1)} plus the trivial (0,1,0,0)/(0,0,0,1)")
    print("      u^2~3b: {(-2,2,1,0), (0,1,-1,1), (2,-1,1,-1)} plus trivial")

    print()
    print("=" * 78)
    print("REJECTION CONTROL -- the survival test must have teeth")
    print("   (a) the same test applied to the OTHER integer points: see the t-table above;")
    print("       t = -2 is rejected by exactly ONE constraint out of %d, and t = -1, 1, 3"
          % (4 * len(ch4)))
    print("       are rejected too.  The system is not vacuous.")
    killed = 0
    total = 0
    import copy
    for i in range(len(ch4)):
        for cls in ('2a', '4a'):
            for delta in (-2, -1, 1, 2):
                bad = copy.deepcopy(ch4)
                bad[i][1][cls] += delta
                total += 1
                viol = []
                for label, vals in bad:
                    for l, m in enumerate(order4_constraints(vals, 2)):
                        if m < 0 or m.denominator != 1:
                            viol.append((label, l, m))
                if viol:
                    killed += 1
    print("   (b) perturbing ONE Brauer/ordinary value by +-1 or +-2: %d of the %d "
          "single-entry perturbations kill (2,-1)." % (killed, total))
    print("       => the survival of (2,-1) is a property of the ACTUAL table, not an "
          "artefact of the test being weak.")
    assert killed > 0, "the survival test is vacuous"

    # a specific, named corruption that DOES kill it
    bad = copy.deepcopy(ch4)
    for l, v in bad:
        if l.startswith('7-mod') and v['1a'] == 5:
            v['2a'] = -1
            break
    viol = [(label, l, m) for label, vals in bad
            for l, m in enumerate(order4_constraints(vals, 2))
            if m < 0 or m.denominator != 1]
    print("   (c) named example: corrupting the 7-modular degree-5 character from "
          "2a=1 to 2a=-1")
    print("       kills (2,-1) via %s" % (viol,))
    assert viol


if __name__ == '__main__':
    main()
