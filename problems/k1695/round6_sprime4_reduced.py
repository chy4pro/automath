#!/usr/bin/env python3
"""ROUND 6-S2: the REDUCED (S')_4 ideal (registry R6.54).  By left-permutation symmetry
P_pi A P_sigma = P_pi (A P_{sigma pi}) P_pi^{-1}, (S') for every index i is equivalent to (S'_0): for
every invertible A some sigma makes e_0 Krylov-cyclic for A P_sigma.  Cyclicity is invariant under
A -> lambda A and the family {A P_sigma} under right permutations, so a_00 = 1 without loss of
generality.  Ideal: the 24 determinants K_{0,sigma}(A)|_{a00=1} in the 15 remaining entries, plus
1 - t*det(A)|_{a00=1}.  Unit over GF(p) <=> (S')_4 <=> Kourovka 16.95 at n = 4 in characteristic p.
Writes engine/harvest/k1695_r6_sprime4/sprime4r_p{p}.ms for the given primes (no solver run here).
Usage: round6_sprime4_reduced.py p [p ...]"""
import sys, os, time
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()
OUT = "$HOME/workspace/claudecode/automath/engine/harvest/k1695_r6_sprime4"
n = 4
syms = sp.symbols(" ".join("a%d%d" % (i, j) for i in range(n) for j in range(n)))
A = sp.Matrix(n, n, syms)
t = sp.Symbol("t")
loc = dict(zip([str(s) for s in syms], syms))
gens = [sp.sympify(l, locals=loc) for l in open(OUT + "/gens_Z.txt") if l.strip()]
assert len(gens) == 96
# generator index = 4*k + i (k = permutation index, i = start vector); keep i = 0
gens0 = [gens[k] for k in range(0, 96, 4)]
a00 = syms[0]
sub = {a00: 1}
gens0 = [sp.expand(g.subs(sub)) for g in gens0]
detA = sp.expand(A.det().subs(sub))
rab = sp.expand(1 - t*detA)
VARS = [s for s in syms if s != a00] + [t]
print("reduced generators: %d (nonzero %d), variables %d, degrees %s  [%.0fs]" % (
    len(gens0), sum(1 for g in gens0 if g != 0), len(VARS),
    sorted({sp.Poly(g, *VARS).total_degree() for g in gens0 if g != 0}), time.time()-T0))
def reduce_mod(expr, p):
    P = sp.Poly(expr, *VARS)
    terms = {m: (int(c) % p) for m, c in P.terms() if int(c) % p}
    return sp.Poly(terms, *VARS).as_expr() if terms else sp.Integer(0)
for p in map(int, sys.argv[1:]):
    body = []
    for g in gens0 + [rab]:
        r = reduce_mod(g, p)
        if r != 0: body.append(str(r).replace("**", "^"))
    path = OUT + "/sprime4r_p%d.ms" % p
    open(path, "w").write(",".join(str(v) for v in VARS) + "\n" + str(p) + "\n" + ",\n".join(body) + "\n")
    print("wrote %s: %d generators, %d bytes  [%.0fs]" % (path, len(body), os.path.getsize(path), time.time()-T0))
print("done %.0fs" % (time.time()-T0))
