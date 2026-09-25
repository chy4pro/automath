"""iso_check.py -- ROUND 2 control: the F_p-irreducibles found are PAIRWISE
NON-ISOMORPHIC, certified by an isomorphism invariant computed here and nowhere
else: the characteristic polynomial of a fixed element of order 7 (and of the
other class representatives).  This closes the one way the Berman completeness
count could be satisfied by a duplicate: if two modules of equal dimension were
in fact isomorphic, the count would still come out right but one irreducible
would be missing."""
import json
from sympy import Matrix, Poly, symbols
x = symbols('x')

GENS = [(1, 2, 0, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6, 0)]


def compose(f, g):
    return tuple(f[g[i]] for i in range(7))


def ctype(p):
    seen, t = [False] * 7, []
    for i in range(7):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j, L = p[j], L + 1
            t.append(L)
    return tuple(sorted(t, reverse=True))


def words():
    seen, frontier = {tuple(range(7)): []}, [tuple(range(7))]
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


def mm(A, B, p):
    k = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % p for j in range(len(B[0]))]
            for i in range(len(A))]


def wm(w, gens, p):
    d = len(gens[0])
    M = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for gi in w:
        M = mm(M, gens[gi], p)
    return M


W = words()
btab = json.load(open('brauer_tables.json'))
probe = {}
for ct in [(7,), (5, 1, 1), (3, 3, 1), (4, 2, 1), (3, 1, 1, 1, 1)]:
    for g, w in W.items():
        if ctype(g) == ct:
            probe[ct] = w
            break

print("isomorphism-invariant fingerprints (char. polys mod p of fixed elements)")
for ps in sorted(btab, key=int):
    p = int(ps)
    seen = {}
    for r in btab[ps]['rows']:
        fp = []
        for ct, w in sorted(probe.items()):
            cp = Poly(Matrix(wm(w, r['gens'], p)).charpoly(x).as_expr(), x, modulus=p)
            fp.append(tuple(int(c) % p for c in cp.all_coeffs()))
        fp = tuple(fp)
        assert fp not in seen, ("p=%d: two modules of dimensions %d and %d share every "
                               "fingerprint -- possible duplicate!"
                               % (p, seen.get(fp), r['dim_fp']))
        seen[fp] = r['dim_fp']
    print("   p=%d: %d modules, %d DISTINCT fingerprints -> pairwise non-isomorphic  [OK]"
          % (p, len(btab[ps]['rows']), len(seen)))
    if p == 2:
        four = [r for r in btab[ps]['rows'] if r['dim_fp'] == 4]
        cps = []
        for r in four:
            cp = Poly(Matrix(wm(probe[(7,)], r['gens'], p)).charpoly(x).as_expr(),
                      x, modulus=p)
            cps.append(cp.factor_list()[1])
        print("      the two 4-dimensional F_2-modules, on an element of order 7:")
        for i, f in enumerate(cps):
            print("         module %d: char poly factors %s"
                  % (i + 1, [(str(a.as_expr()), b) for a, b in f]))
        assert cps[0] != cps[1], "the two 4-dim F_2-modules are NOT distinguished!"
        print("      -> DIFFERENT, so genuinely non-isomorphic (they are the Galois pair "
              "whose Brauer characters differ only on 7a / 7b)")
