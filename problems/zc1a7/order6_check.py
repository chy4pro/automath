#!/usr/bin/env python3
"""
zc1a7 ROUND 1, step 4: FALSIFICATION TEST of the HeLP engine against a published,
explicitly listed HeLP output.

arXiv:2006.09031, Section 4, prints the complete HeLP output for units of ORDER 6
in V(Z A_7) (the output of HeLP_ZC(CharacterTable("A7")) in GAP, i.e. computed with
the FULL ordinary and Brauer character tables):

  u^2 ~ 3a :  (eps_2a, eps_3a, eps_3b, eps_6a) in { (-2,1,2,0), (2,0,0,-1) }
  u^2 ~ 3b :                                     { (-2,2,1,0), (0,1,-1,1), (2,-1,1,-1) }

My constraint set is WEAKER than GAP's (I have the full ordinary table but only the
Brauer characters I can construct from permutation modules), so my solution set must
be a SUPERSET of those.  The test that can fail:
   *** if any of the five published vectors is MISSING from my solution set, then
       either my engine is wrong or the published list is wrong. ***
That is the falsification.  Nothing here is used for the order-4 kill condition.
"""

import json, os, itertools
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "a7_table.json")))
NAMES = D["names"]; ORDERS = D["orders"]; POW = D["powermap"]
NC = len(NAMES)
IDX = {NAMES[k]: k for k in range(NC)}
TAB = [[sp.sympify(s) for s in row] for row in D["table"]]
DEG = D["degrees"]

# Brauer characters: rebuilt exactly as in helpr1.py (pi - 2 / pi - 1 of permutation modules)
PI = {   # permutation characters, recomputed there and pasted as data with their source
    "7 points":  {"1a": 7, "2a": 3, "3a": 4, "3b": 1, "4a": 1, "5a": 2, "6a": 0, "7a": 0, "7b": 0},
    "21 pairs":  {"1a": 21, "2a": 5, "3a": 6, "3b": 0, "4a": 1, "5a": 1, "6a": 2, "7a": 0, "7b": 0},
    "35 triples": {"1a": 35, "2a": 7, "3a": 5, "3b": 2, "4a": 1, "5a": 0, "6a": 1, "7a": 0, "7b": 0},
    "15 cosets": {"1a": 15, "2a": 3, "3a": 0, "3b": 3, "4a": 1, "5a": 0, "6a": 0, "7a": 1, "7b": 1},
}
CHARS = []
for i in range(NC):
    CHARS.append(("ordinary deg %d" % DEG[i], [TAB[i][k] for k in range(NC)], None))
for lab, pi in PI.items():
    m = pi["1a"]
    for p in (5, 7):
        sub = 2 if m % p == 0 else 1
        CHARS.append(("p=%d %s dim %d" % (p, lab, m - sub),
                      [sp.Integer(pi[NAMES[k]] - sub) for k in range(NC)], p))

n = 6
a, b, c = sp.symbols("e3a e3b e6a", integer=True)
eps2a = 1 - a - b - c
FREE = (a, b, c)

def zeta(k):
    return sp.exp(2*sp.pi*sp.I*sp.Rational(k, n))

results = {}
for sq in ("3a", "3b"):
    eps_u = {IDX["2a"]: eps2a, IDX["3a"]: a, IDX["3b"]: b, IDX["6a"]: c}
    eps_u2 = {IDX[sq]: sp.Integer(1)}
    eps_u3 = {IDX["2a"]: sp.Integer(1)}
    ebd = {1: eps_u, 2: eps_u2, 3: eps_u3}

    def mult(vals, ell):
        tot = vals[IDX["1a"]]
        for k in range(1, n):
            d = int(sp.gcd(k, n)); j = k // d
            val = sum(e*vals[POW[cl][j]] for cl, e in ebd[d].items())
            tot += val*zeta(-k*ell)
        return sp.expand(sp.simplify(sp.expand_complex(sp.expand(tot/n))))

    ineqs = []
    Lints = []          # (coeff vector of chi(u) in FREE, const, [lo,hi])
    for name, vals, p in CHARS:
        if p is not None and n % p == 0:
            continue
        L = sp.expand(sum(e*vals[cl] for cl, e in eps_u.items()))
        mus = [sp.nsimplify(mult(vals, ell)) for ell in range(n)]
        assert sp.simplify(sum(mus) - vals[IDX["1a"]]) == 0, "multiplicities do not sum to the degree"
        for ell, mu in enumerate(mus):
            ineqs.append((name, ell, sp.expand(mu)))
        # bounds on the linear functional L from mu_ell >= 0
        lo, hi = -sp.oo, sp.oo
        for ell, mu in enumerate(mus):
            pol = sp.Poly(mu, *FREE)
            # mu = A + B*L  with B = 2cos(pi*ell/3)/6 ; recover B from the a-coefficient ratio
            polL = sp.Poly(sp.expand(mu), *FREE)
            # write mu as function of L: solve linearly
            Lsym = sp.Symbol("L")
            # express: mu is affine in (a,b,c); L is affine in (a,b,c); if the linear parts
            # are proportional we can substitute.
            lin_mu = sp.Matrix([sp.diff(mu, v) for v in FREE])
            lin_L = sp.Matrix([sp.diff(L, v) for v in FREE])
            if lin_L.norm() == 0:
                continue
            # find scalar s with lin_mu = s * lin_L
            s = None
            for i in range(3):
                if lin_L[i] != 0:
                    s = sp.simplify(lin_mu[i]/lin_L[i]); break
            if s is None or sp.simplify((lin_mu - s*lin_L).norm()) != 0:
                continue
            const = sp.simplify(mu - s*L)
            if s > 0:
                lo = max(lo, sp.nsimplify(-const/s))
            elif s < 0:
                hi = min(hi, sp.nsimplify(-const/s))
        if lo != -sp.oo or hi != sp.oo:
            Lints.append((sp.Matrix([sp.diff(L, v) for v in FREE]),
                          sp.simplify(L - sum(sp.diff(L, v)*v for v in FREE)), lo, hi, name))

    # bounding box: choose 3 functionals with an invertible coefficient matrix
    box = None
    for trip in itertools.combinations(range(len(Lints)), 3):
        M = sp.Matrix.hstack(*[Lints[i][0] for i in trip]).T
        if M.det() == 0:
            continue
        if any(Lints[i][2] == -sp.oo or Lints[i][3] == sp.oo for i in trip):
            continue
        Minv = M.inv()
        cst = sp.Matrix([Lints[i][1] for i in trip])
        loV = sp.Matrix([Lints[i][2] for i in trip]) - cst
        hiV = sp.Matrix([Lints[i][3] for i in trip]) - cst
        bb = []
        for i in range(3):
            lo_i = hi_i = 0
            for j in range(3):
                m = Minv[i, j]
                if m >= 0:
                    lo_i += m*loV[j]; hi_i += m*hiV[j]
                else:
                    lo_i += m*hiV[j]; hi_i += m*loV[j]
            bb.append((sp.ceiling(lo_i), sp.floor(hi_i)))
        vol = 1
        for l, h in bb:
            vol *= max(0, int(h) - int(l) + 1)
        if vol > 0 and (box is None or vol < box[0]):
            box = (vol, bb, [Lints[i][4] for i in trip])
    assert box is not None, "no bounding box found"
    print("u^2 ~ %s : proven bounding box %s  (from %s), %d integer points"
          % (sq, box[1], box[2], box[0]))

    # congruences (Prop. partial augmentations (iii))
    def cong_ok(av, bv, cv):
        e = {IDX["2a"]: 1 - av - bv - cv, IDX["3a"]: av, IDX["3b"]: bv, IDX["6a"]: cv}
        for p, m in ((2, 2), (3, 3)):
            for Dcl in range(NC):
                lhs = sum(v for cl, v in e.items() if POW[cl][m] == Dcl)
                if m == 2:
                    rhs = 1 if Dcl == IDX[sq] else 0
                else:
                    rhs = 1 if Dcl == IDX["2a"] else 0
                if (lhs - rhs) % p != 0:
                    return False
        return True

    sols = []
    (la, ha), (lb, hb), (lc, hc) = box[1]
    for av in range(int(la), int(ha)+1):
        for bv in range(int(lb), int(hb)+1):
            for cv in range(int(lc), int(hc)+1):
                if not cong_ok(av, bv, cv):
                    continue
                ok = True
                for name, ell, mu in ineqs:
                    val = sp.nsimplify(mu.subs({a: av, b: bv, c: cv}))
                    if val < 0 or not val.is_integer:
                        ok = False; break
                if ok:
                    sols.append((1-av-bv-cv, av, bv, cv))
    results[sq] = sols
    print("   my solution set (eps_2a, eps_3a, eps_3b, eps_6a) : %s" % sols)

PAPER = {"3a": [(-2, 1, 2, 0), (2, 0, 0, -1)],
         "3b": [(-2, 2, 1, 0), (0, 1, -1, 1), (2, -1, 1, -1)]}

print()
print("=== FALSIFICATION TEST ===")
allok = True
for sq in ("3a", "3b"):
    mine = set(results[sq])
    trivial = set(v for v in mine if all(x >= 0 for x in v))
    nontriv = mine - trivial
    missing = [v for v in PAPER[sq] if v not in mine]
    extra = sorted(nontriv - set(PAPER[sq]))
    print("u^2 ~ %s : published non-trivial vectors present? %s"
          % (sq, "ALL PRESENT" if not missing else "MISSING %s  <<< FALSIFIED" % missing))
    print("          my extra non-trivial vectors (expected: weaker character set) : %s" % extra)
    print("          my trivial (all >= 0) vectors : %s" % sorted(trivial))
    if missing:
        allok = False
print()
print("VERDICT:", "engine consistent with the published HeLP output" if allok
      else "INCONSISTENT WITH THE PUBLISHED OUTPUT")
