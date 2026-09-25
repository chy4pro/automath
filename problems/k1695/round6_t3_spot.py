#!/usr/bin/env python3
"""ROUND 6-K: independent spot re-run of K6-T3 unit-ideal certificates from the printed ideal files
(own parser, sympy groebner, grevlex).  Cells: Case A support-1 over GF(2) and GF(3), support-2 over GF(2)."""
import sys, time, re
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
def load(path):
    lines = open(path).read().split("\n")
    names = lines[0].strip().split(","); p = int(lines[1].strip())
    body = "\n".join(lines[2:])
    syms = sp.symbols(names); loc = dict(zip(names, syms))
    gens = [sp.sympify(s.strip().replace("^", "**"), locals=loc) for s in re.split(r",\s*\n|,\s*$", body) if s.strip()]
    return syms, p, gens
for cell in ["caseA_kappa1_p2", "caseA_kappa1_p3", "caseA_kappa2_p2"]:
    syms, p, gens = load("engine/harvest/k1695_r6_T3/ideals/%s.ms" % cell)
    t0 = time.time()
    G = sp.groebner(gens, *syms, order="grevlex", modulus=p) if p else sp.groebner(gens, *syms, order="grevlex", domain=sp.QQ)
    basis = [str(sp.expand(g.as_expr())) for g in G.polys]
    print("%s: vars=%d gens=%d char=%d basis=%s  [%.1fs]" % (cell, len(syms), len(gens), p, basis if len(basis) < 3 else "size %d" % len(basis), time.time()-t0))
# negative control: drop the Rabinowitsch generator -> must NOT be [1]
syms, p, gens = load("engine/harvest/k1695_r6_T3/ideals/caseA_kappa1_p2.ms")
G = sp.groebner(gens[:-1], *syms, order="grevlex", modulus=p)
print("control (Rabinowitsch generator dropped): basis size=%d is_unit=%s" % (len(G.polys), [str(g.as_expr()) for g in G.polys] == ['1']))
