# Decompose the slack a_n - 2 beta(n-1) = holes + 2*(nonboundary Y in window) + 2*(Harper slack on Y)
import numpy as np
from windows import all_pm_sums, inner_boundary, lattice_count_open, beta, conway_guy_set, is_dss
sets = {
 'opt5': [3,6,11,12,13], 'opt6': [11,17,20,22,23,24], 'opt7': [20,31,37,40,42,43,44],
 'opt8a': [20,40,71,77,80,82,83,84], 'opt8b': [39,59,70,77,78,79,81,84],
 'CG12': conway_guy_set(12), 'CG16': conway_guy_set(16), 'CG20': conway_guy_set(20), 'CG22': conway_guy_set(22),
 '2^n-2^i,12': sorted(2**12-2**i for i in range(12)), 'pow2,12': [2**i for i in range(12)],
}
print(f"{'set':>12} {'n':>3} {'a_n':>8} {'slack':>8} | {'holes':>7} {'2*nonbd':>8} {'2*HarperSlack':>13}  (fractions of a_n)")
for name, a in sets.items():
    a = sorted(a); n = len(a); an = a[-1]
    assert is_dss(a)
    X = all_pm_sums(a); Y = all_pm_sums(a[:-1]); s = sum(a) % 2
    lat = lattice_count_open(-an, an, s)
    occ = int(np.count_nonzero((X > -an) & (X < an)))
    yc = int(np.count_nonzero((Y > -2*an) & (Y < 0)))
    dBp = inner_boundary(Y, a[:-1])
    holes = lat - occ
    nonbd = yc - dBp
    hs = dBp - beta(n-1)
    slack = an - 2*beta(n-1)
    # identity: an = (an - lat) + holes + 2*nonbd + 2*hs + 2*beta(n-1)
    assert an == (an - lat) + holes + 2*nonbd + 2*hs + 2*beta(n-1)
    print(f"{name:>12} {n:3d} {an:8d} {slack/an:8.3f} | {holes/an:7.3f} {2*nonbd/an:8.3f} {2*hs/an:13.3f}   parity-loss={an-lat}")
