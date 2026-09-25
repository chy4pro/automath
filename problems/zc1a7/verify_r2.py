"""
verify_r2.py -- ROUND 2, line zc1a7:  INDEPENDENT re-verification (doctrine s105).

Imports NOTHING from meataxe.py / modular_a7.py / help_full.py.  It reads only
the two data files (the round-1 ordinary table, and the round-2 module matrices)
and re-derives every claim-carrying number by a DIFFERENT algorithm:

  * eigenvalue multiplicities from the CHARACTERISTIC POLYNOMIAL factored over
    F_p (modular_a7.py used nullities of cyclotomic-polynomial evaluations);
  * the group re-built with sympy's Permutation machinery, class membership
    re-established from cycle type;
  * a homomorphism test on random pairs (the modules must really be modules);
  * two MODULE-FREE tests that use only the resulting value tables:
      (D0) defect-zero blocks:  |G|_p | chi(1)  =>  chi restricted to p-regular
           classes must itself be an irreducible Brauer character;
      (DEC) every ordinary chi restricted to the p-regular classes must be a
           NON-NEGATIVE INTEGER combination of the computed Brauer characters;
  * the eigenvalue multiplicities of the hypothetical order-4 unit recomputed by
    solving the 4x4 Vandermonde system over Q(i) (help_full.py used Ramanujan
    sums).

Interpreter: .venv/bin/python3.  Exact arithmetic only.
"""
import json
import random
from sympy import Poly, symbols, Matrix, I, Rational, sympify, eye

x = symbols('x')

P_ORDER = {2: 8, 3: 9, 5: 5, 7: 7}          # |A_7|_p ,  |A_7| = 2520 = 2^3*3^2*5*7
CLASS_CYCLE = {'1a': (1,) * 7, '2a': (2, 2, 1, 1, 1), '3a': (3, 1, 1, 1, 1),
               '3b': (3, 3, 1), '4a': (4, 2, 1), '5a': (5, 1, 1), '6a': (3, 2, 2)}
CLASS_ORDER = {'1a': 1, '2a': 2, '3a': 3, '3b': 3, '4a': 4, '5a': 5, '6a': 6}


# ------------------------------------------------------------------ group, again

def compose(f, g):
    """(f o g)(i) = f(g(i))."""
    return tuple(f[g[i]] for i in range(7))


GA = (1, 2, 0, 3, 4, 5, 6)          # (1 2 3)
GB = (1, 2, 3, 4, 5, 6, 0)          # (1 2 3 4 5 6 7)
GENS = [GA, GB]
IDP = tuple(range(7))


def ctype(perm):
    seen, t = [False] * 7, []
    for i in range(7):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j, L = perm[j], L + 1
            t.append(L)
    return tuple(sorted(t, reverse=True))


def perm_of_word(w):
    r = IDP
    for gi in w:
        r = compose(r, GENS[gi])
    return r


def enumerate_group():
    """BFS with the OPPOSITE multiplication convention to the builder's."""
    seen = {IDP: []}
    frontier = [IDP]
    while frontier:
        nxt = []
        for g in frontier:
            for gi, s in enumerate(GENS):
                h = compose(g, s)
                if h not in seen:
                    seen[h] = seen[g] + [gi]
                    nxt.append(h)
        frontier = nxt
    return seen


# ------------------------------------------------------------------ matrices, again

def mm(A, B, p):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % p for j in range(m)]
            for i in range(n)]


def word_mat(w, gens, p):
    d = len(gens[0])
    M = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for gi in w:
        M = mm(M, gens[gi], p)
    return M


def eig_mults(M, p, m):
    """Multiplicities of the m-th roots of unity as eigenvalues of M over Fbar_p,
    via the CHARACTERISTIC POLYNOMIAL (a different algorithm from nullities).
    Returns {d: multiplicity of each primitive d-th root}, d | m."""
    cp = Matrix(M).charpoly(x)
    pol = Poly(cp.as_expr(), x, modulus=p)
    facs = {}
    for f, e in pol.factor_list()[1]:
        facs[tuple(int(c) % p for c in f.all_coeffs())] = e
    out = {}
    from sympy import divisors, cyclotomic_poly
    total = 0
    for d in divisors(m):
        Phi = Poly(cyclotomic_poly(d, x), x, modulus=p)
        mults = []
        for f, _ in Phi.factor_list()[1]:
            key = tuple(int(c) % p for c in f.all_coeffs())
            e = facs.get(key, 0)
            mults.append((e, len(key) - 1))
        assert len(set(a for a, _ in mults)) == 1, \
            "class not rational: primitive %d-th roots occur with multiplicities %s" \
            % (d, mults)
        out[d] = mults[0][0]
        total += mults[0][0] * sum(b for _, b in mults)
    assert total == len(M), "multiplicities %s do not sum to dim %d" % (out, len(M))
    return out


def brauer_from_mults(mults):
    from sympy import mobius
    return sum(v * int(mobius(d)) for d, v in mults.items())


# ------------------------------------------------------------------ main

def main():
    rnd = random.Random(20260823)
    words = enumerate_group()
    assert len(words) == 2520
    print("independent group build (opposite multiplication convention): |A_7| = %d"
          % len(words))

    # class representatives, identified by cycle type only
    reps = {}
    for c, ct in CLASS_CYCLE.items():
        for g, w in words.items():
            if ctype(g) == ct:
                reps[c] = (g, w)
                break
    print("class reps re-found by cycle type: %s"
          % ", ".join("%s=%s" % (c, CLASS_CYCLE[c]) for c in sorted(reps)))

    # extra words for the same classes, for the class-function control
    extra = {c: [] for c in reps}
    for g, w in words.items():
        for c, ct in CLASS_CYCLE.items():
            if ctype(g) == ct and len(extra[c]) < 4 and w != reps[c][1]:
                extra[c].append(w)

    btab = json.load(open('brauer_tables.json'))
    ord_d = json.load(open('a7_table.json'))
    names, degrees = ord_d['names'], ord_d['degrees']
    otab = [[sympify(v) for v in row] for row in ord_d['table']]

    print()
    print("=" * 78)
    print("(1) MODULES ARE MODULES, AND THE VALUES ARE CLASS FUNCTIONS")
    for p_s in sorted(btab, key=int):
        p = int(p_s)
        for r in btab[p_s]['rows']:
            g1, g2 = r['gens']
            d = len(g1)
            # generator relations
            A3 = mm(mm(g1, g1, p), g1, p)
            B = g2
            B7 = g2
            for _ in range(6):
                B7 = mm(B7, B, p)
            assert A3 == [[1 if i == j else 0 for j in range(d)] for i in range(d)], \
                "M(a)^3 != I  (p=%d, dim %d)" % (p, d)
            assert B7 == [[1 if i == j else 0 for j in range(d)] for i in range(d)], \
                "M(b)^7 != I  (p=%d, dim %d)" % (p, d)
            # homomorphism test on random pairs
            for _ in range(12):
                g = rnd.choice(list(words))
                h = rnd.choice(list(words))
                lhs = mm(word_mat(words[g], r['gens'], p),
                         word_mat(words[h], r['gens'], p), p)
                rhs = word_mat(words[compose(g, h)], r['gens'], p)
                assert lhs == rhs, "not a representation (p=%d, dim %d)" % (p, d)
        print("   p=%d: all %d modules satisfy M(a)^3 = M(b)^7 = I and "
              "M(g)M(h) = M(gh) on 12 random pairs each" % (p, len(btab[p_s]['rows'])))

    print()
    print("=" * 78)
    print("(2) BRAUER VALUES RECOMPUTED FROM CHARACTERISTIC POLYNOMIALS")
    recomputed = {}
    for p_s in sorted(btab, key=int):
        p = int(p_s)
        rows = []
        for r in btab[p_s]['rows']:
            vals = {}
            for c in btab[p_s]['classes']:
                M = word_mat(reps[c][1], r['gens'], p)
                v = brauer_from_mults(eig_mults(M, p, CLASS_ORDER[c]))
                # class-function control: other elements of the same class
                for w2 in extra[c]:
                    M2 = word_mat(w2, r['gens'], p)
                    v2 = brauer_from_mults(eig_mults(M2, p, CLASS_ORDER[c]))
                    assert v2 == v, ("value on class %s depends on the element "
                                     "(%s vs %s)" % (c, v, v2))
                assert v % r['k'] == 0
                vals[c] = v // r['k']
            assert vals == r['vals'], ("MISMATCH p=%d deg %d: %s vs %s"
                                       % (p, r['deg'], vals, r['vals']))
            rows.append((r['deg'], vals))
        recomputed[p] = (btab[p_s]['classes'], rows)
        print("   p=%d: all %d Brauer characters reproduced EXACTLY by the "
              "charpoly route, and every value survives a 5-element "
              "class-function check" % (p, len(rows)))

    print()
    print("=" * 78)
    print("(3) MODULE-FREE TEST D0 -- defect-zero blocks")
    n_d0 = 0
    for p, (cls, rows) in recomputed.items():
        for i, deg in enumerate(degrees):
            if deg % P_ORDER[p] == 0:
                want = {c: int(otab[i][names.index(c)]) for c in cls}
                hit = [d for d, v in rows if d == deg and v == want]
                assert hit, ("chi%d (deg %d) lies in a p=%d block of defect 0 but its "
                             "restriction %s is NOT in the computed Brauer table"
                             % (i + 1, deg, p, want))
                n_d0 += 1
                print("   p=%d  chi%-2d (deg %-2d): |G|_p = %d divides the degree => defect 0 "
                      "=> chi restricted must BE an irreducible Brauer character.  FOUND."
                      % (p, i + 1, deg, P_ORDER[p]))
    print("   %d defect-zero checks, all passed.  (This test uses only the ordinary "
          "table and block theory -- no module, no MeatAxe.)" % n_d0)

    print()
    print("=" * 78)
    print("(4) MODULE-FREE TEST DEC -- decomposition matrices")
    for p, (cls, rows) in sorted(recomputed.items()):
        # distinct value-vectors (Galois conjugates coincide on rational classes)
        cols = []
        for deg, v in rows:
            key = (deg, tuple(v[c] for c in cls))
            if key not in cols:
                cols.append(key)
        print("   p=%d, basic columns (degree; %s):" % (p, ",".join(cls)))
        for deg, v in cols:
            print("        deg %-3d %s" % (deg, list(v)))
        for i, deg in enumerate(degrees):
            target = [int(otab[i][names.index(c)]) for c in cls]
            sols = []

            def rec(j, rem, coeff):
                if j == len(cols):
                    if all(v == 0 for v in rem):
                        sols.append(tuple(coeff))
                    return
                d0, v0 = cols[j]
                m = min(rem[0] // d0, 40) if d0 else 0
                for a in range(m + 1):
                    nrem = [r - a * b for r, b in zip(rem, v0)]
                    if nrem[0] < 0:
                        break
                    rec(j + 1, nrem, coeff + [a])
            rec(0, target, [])
            assert sols, ("chi%d (deg %d) does NOT decompose into the computed %d-modular "
                          "Brauer characters with non-negative integer multiplicities"
                          % (i + 1, deg, p))
            tag = "unique" if len(sols) == 1 else "%d solutions" % len(sols)
            print("      chi%-2d (deg %-2d) = %s   [%s]"
                  % (i + 1, deg,
                     " + ".join("%d*(deg %d)" % (a, cols[j][0])
                                for j, a in enumerate(sols[0]) if a) or "0",
                     tag))
        print("   p=%d: ALL 9 ordinary characters decompose with non-negative integer "
              "multiplicities.  A missing or wrong irreducible would break this." % p)

    print()
    print("=" * 78)
    print("(5) THE ORDER-4 MULTIPLICITIES, RECOMPUTED OVER Q(i) BY LINEAR ALGEBRA")
    # eigenvalues of D(u): 1, i, -1, -i with multiplicities m0..m3, and
    #   sum_k m_k * i^{jk} = chi(u^j),  j = 0,1,2,3
    V = Matrix(4, 4, lambda j, k: I ** (j * k))
    Vinv = V.inv()
    chars = []
    for i2, deg in enumerate(degrees):
        chars.append(('ord chi%d(deg %d)' % (i2 + 1, deg),
                      {c: int(otab[i2][names.index(c)]) for c in ('1a', '2a', '4a')}))
    for p, (cls, rows) in sorted(recomputed.items()):
        if 4 % p == 0:
            continue
        for deg, v in rows:
            chars.append(('%d-mod phi(deg %d)' % (p, deg),
                          {c: v[c] for c in ('1a', '2a', '4a')}))
    bad = []
    tight = 0
    for label, v in chars:
        d, c2, c4 = v['1a'], v['2a'], v['4a']
        cu = 2 * c2 - c4                     # chi(u)  for (eps_2a,eps_4a) = (2,-1)
        rhs = Matrix(4, 1, [d, cu, c2, cu])  # chi(u^0), chi(u), chi(u^2), chi(u^3)
        m = Vinv * rhs
        m = [Rational(t) for t in m]
        if any(t < 0 or t.q != 1 for t in m):
            bad.append((label, m))
        if any(t == 0 for t in (m[0], m[2])):
            tight += 1
    print("   %d characters (ordinary + 3-,5-,7-modular).  Multiplicity vectors with a "
          "negative or non-integral entry: %d" % (len(chars), len(bad)))
    assert not bad, bad
    print("   => (eps_2a, eps_4a) = (2,-1) SURVIVES the complete system.  "
          "CONFIRMED INDEPENDENTLY.")
    print("   tight characters (mu_0 = 0 or mu_2 = 0): %d" % tight)

    # the load-bearing step, re-isolated
    kill = []
    for label, v in chars:
        d, c2, c4 = v['1a'], v['2a'], v['4a']
        cu = -2 * c2 + 3 * c4                # chi(u) for (eps_2a,eps_4a) = (-2,3)
        m = Vinv * Matrix(4, 1, [d, cu, c2, cu])
        if any(Rational(t) < 0 or Rational(t).q != 1 for t in m):
            kill.append(label)
    print("   characters that reject (eps_2a,eps_4a) = (-2,3), i.e. t = -2: %s" % kill)
    assert kill == ['7-mod phi(deg 5)'], kill
    print("   => the SINGLE load-bearing inequality of round 1 is still the single "
          "load-bearing inequality of the COMPLETE system.")


if __name__ == '__main__':
    main()
