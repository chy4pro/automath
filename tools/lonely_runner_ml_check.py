from fractions import Fraction
from math import gcd
from itertools import combinations
import sys

def ML(v):
    """Exact max_t min_i ||t*v_i||.  Candidate optimal t are rationals m/d with
       d in {2v_i} U {|v_i +- v_j|}: breakpoints of each ||t v_i|| and crossings."""
    dens=set()
    for x in v: dens.add(2*x)
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            for d in (v[i]+v[j], abs(v[i]-v[j])):
                if d>0: dens.add(d)
    best_n, best_d = 0, 1          # best = best_n/best_d
    for d in dens:
        for m in range(0, d+1):
            # min_i ||m*v_i/d|| = (min_i min(r, d-r))/d
            mn = d
            for x in v:
                r = (m*x) % d
                r = r if r < d-r else d-r
                if r < mn:
                    mn = r
                    if mn == 0: break
            if mn*best_d > best_n*d:
                best_n, best_d = mn, d
    return Fraction(best_n, best_d)

# ---- POSITIVE CONTROL: known values -----------------------------------------
print("CONTROL  ML(1,2,3)      =", ML([1,2,3]),      " LRC bound 1/4 =", Fraction(1,4))
print("CONTROL  ML(1,2,3,4)    =", ML([1,2,3,4]),    " LRC bound 1/5 =", Fraction(1,5))
print("CONTROL  ML(1,3,4,7)    =", ML([1,3,4,7]),    " (Goddyn-Wong sporadic tight set, expect 1/5)")
print("CONTROL  ML(1,3,4,5,9)  =", ML([1,3,4,5,9]),  " (sporadic tight set, expect 1/6)")
print("CONTROL  ML(1,2,3,4,5)  =", ML([1,2,3,4,5]),  " expect 1/6")
print()

# ---- Fan-Sun regime: n=4 speeds. Spectrum Conjecture (Kravitz 2021):
#      ML = s/(4s+1) for some s in N, OR ML >= 1/4.
#      LRC (target) for 4 speeds: ML >= 1/5.
LIM = 26
spec_viol = []
lrc_viol  = []
tight     = 0
tot       = 0
for v in combinations(range(1,LIM+1), 4):
    g = 0
    for x in v: g = gcd(g,x)
    if g != 1: continue          # scale-invariant; keep primitive tuples only
    tot += 1
    m = ML(list(v))
    if m == Fraction(1,5): tight += 1
    if m < Fraction(1,5): lrc_viol.append((v,m))          # would be an LRC counterexample
    if m < Fraction(1,4):
        # spectrum branch: is m == s/(4s+1) for some positive integer s?
        # m = s/(4s+1)  <=>  s = m/(1-4m)
        ok=False
        if 1-4*m != 0:
            s = m/(1-4*m)
            ok = (s.denominator==1 and s.numerator>=1)
        if not ok: spec_viol.append((v,m))
print("primitive 4-tuples, speeds <= %d : %d"%(LIM,tot))
print("tight (ML exactly 1/5)          :", tight)
print("LRC counterexamples (ML < 1/5)  :", len(lrc_viol))
print("SPECTRUM-conjecture counterexamples (ML<1/4 and ML != s/(4s+1)):", len(spec_viol))
print()
if spec_viol:
    mn = min(x[1] for x in spec_viol)
    print("  smallest ML among spectrum counterexamples:", mn, "=", float(mn))
    print("  LRC bound 1/5 =", float(Fraction(1,5)), " -> all satisfy LRC?", all(x[1]>=Fraction(1,5) for x in spec_viol))
    print("  first 12 spectrum counterexamples (tuple, ML):")
    for v,m in spec_viol[:12]:
        print("   ", v, m, "  ML-1/5 =", m-Fraction(1,5))
