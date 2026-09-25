#!/usr/bin/env python3
"""ROUND 6-O: independent check of K6-N4k's rank-1 ideals.
(1) Regenerate the fixed-row family R = [x, e1+y1 x, e2+y2 x, e3+y3 x] and its 18 determinants
    D_{0,j,tau} = det[c_j, M c_j, M^2 c_j] (M = other three columns in order tau) with sympy over Z,
    and compare the set of nonzero ones with the generators in ideals/r1_S_a_p0.ms (modulo sign).
(2) Run sympy groebner (grevlex) on the S/a system over GF(2) and over Q as a second engine,
    with a wall cap; print [1] or not."""
import sys, time, re, itertools, signal
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()
a, b, c, y1, y2, y3, z, t, r = sp.symbols('a b c y1 y2 y3 z t r')
x = sp.Matrix([a, b, c]); ys = [y1, y2, y3]
cols = [x] + [sp.Matrix([1 if k == j else 0 for k in range(3)]) + ys[j]*x for j in range(3)]
dets = {}
for j in (1, 2, 3):
    others = [k for k in range(4) if k != j]
    for tau in itertools.permutations(others):
        M = sp.Matrix.hstack(*[cols[k] for k in tau]); bj = cols[j]
        D = sp.expand(sp.Matrix.hstack(bj, M*bj, M*M*bj).det())
        dets[(j, tau)] = D
nonzero = [D for D in dets.values() if D != 0]
print("regenerated: %d determinants, %d nonzero" % (len(dets), len(nonzero)))
# parse the ideal file (msolve format: line1 vars, line2 char, then generators separated by ',')
def load(path):
    lines = open(path).read().split("\n")
    names = lines[0].strip().split(","); p = int(lines[1].strip())
    body = "\n".join(lines[2:])
    syms = sp.symbols(names); loc = dict(zip(names, syms))
    gens = [sp.expand(sp.sympify(s.strip().replace("^", "**"), locals=loc)) for s in re.split(r",\s*\n|,\s*$", body) if s.strip()]
    return syms, p, gens
syms, p, gens = load("engine/harvest/k1695_r6_n4k/ideals/r1_S_a_p0.ms")
print("file r1_S_a_p0: vars=%s char=%d generators=%d" % (syms, p, len(gens)))
S = a + b + c
file_set = set(str(g) for g in gens) | set(str(-g) for g in gens)
matched = sum(1 for D in nonzero if str(sp.expand(D)) in file_set or str(sp.expand(-D)) in file_set)
print("of my %d nonzero determinants, %d appear (up to sign) among the file's generators" % (len(nonzero), matched))
extra = [g for g in gens if str(g) not in set(str(D) for D in nonzero) | set(str(-D) for D in nonzero)]
print("generators in the file that are not determinants: %s" % [str(g)[:60] for g in extra])
# (2) sympy groebner, capped
def run(gens, syms, modulus, cap):
    def handler(signum, frame): raise TimeoutError()
    signal.signal(signal.SIGALRM, handler); signal.alarm(cap)
    t0 = time.time()
    try:
        G = sp.groebner(gens, *syms, order='grevlex', modulus=modulus) if modulus else sp.groebner(gens, *syms, order='grevlex', domain=sp.QQ)
        signal.alarm(0)
        return [str(g.as_expr()) for g in G.polys], time.time()-t0
    except TimeoutError:
        return None, cap
for (path, mod) in [("engine/harvest/k1695_r6_n4k/ideals/r1_S_a_p2.ms", 2), ("engine/harvest/k1695_r6_n4k/ideals/r1_S_a_p0.ms", 0)]:
    syms, p, gens = load(path)
    basis, dt = run(gens, syms, mod, 900)
    print("sympy on %s (char %d): %s  [%.0fs]" % (path.split('/')[-1], p, ("basis=" + str(basis)) if basis is not None else "TIMEOUT(900s)", dt))
print("done %.1fs" % (time.time()-T0))
