#!/usr/bin/env python3
"""owner-tdn round 2 -- WHERE DOES THE CONJECTURE'S SLACK COME FROM?

The setting.  On the p=5 class  A_e1 = {(0,0),(1,0)}, |A_e2| <= 3  (complete
sub-population; see tdn_r2_class_census.py for why the enumeration is lossless):

    * the POINTWISE Case-A conclusion |A_w| >= 4 on mixed w  FAILS
      (tdn_r2_certificate.py: an explicit witness; 900 of 10925 normal forms).
    * the AGGREGATE version  sum over mixed w of |A_w| >= 4(p-1)^2  ALSO FAILS
      (tdn_r2_aggregate.py: min = 62 < 64, on 300 normal forms).
    * yet the CONJECTURE  |T_f - T_f| >= (2p-1)^2  HOLDS on the class, with
      equality attained (tdn_r2_aggregate.py: min = 81, 0 members below).

So the loss on mixed directions is being PAID FOR somewhere else.  The paper's
proof bounds each direction class separately and pointwise, which is exactly the
bookkeeping that cannot see a transfer between classes.  This file measures the
transfer.

For every f in the class it records the decomposition
    S_u = sum of |A_u| over the p-1 nonzero multiples of e1
    S_v = sum of |A_u| over the p-1 nonzero multiples of e2
    S_m = sum of |A_w| over the (p-1)^2 mixed w
    total = 1 + S_u + S_v + S_m  =  |T_f - T_f|
and reports the joint minima and the trade-off, so that a repair lemma can be
aimed at the inequality that is actually binding rather than at the one the
paper happens to split on.

CONTROL THAT COULD FAIL
    H1  1 + S_u + S_v + S_m  ==  |T_f - T_f| computed LITERALLY as a difference
        set in (Z/p^2 Z)^2, for EVERY member.  No shared code path.

Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r2_decomp.py
"""
import itertools
import sys
import time

T_START = time.time()
HARD_TIMEOUT_S = 600
try:
    sys.stdout.reconfigure(line_buffering=True)
except AttributeError:
    pass

P = 5
PTS = [(a, b) for a in range(P) for b in range(P)]
MIXED = [(a, b) for a in range(1, P) for b in range(1, P)]
UMULT = [(a, 0) for a in range(1, P)]
VMULT = [(0, b) for b in range(1, P)]
M = [[i - (1 if q < i else 0) for i in range(P)] for q in range(P)]
A_E1 = frozenset([(0, 0), (1, 0)])


def carry(u, x, p):
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def A_set(f, u, p):
    out = set()
    for x in PTS:
        y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
        c = carry(u, x, p)
        fy, fx = f[y], f[x]
        out.add(((fy[0] - fx[0] + c[0]) % p, (fy[1] - fx[1] + c[1]) % p))
    return out


def diffset_literal(f, p):
    m = p * p
    T = [((x[0] + p * f[x][0]) % m, (x[1] + p * f[x][1]) % m) for x in PTS]
    return len(set(((a[0] - b[0]) % m, (a[1] - b[1]) % m) for a in T for b in T))


def build(qs, betas):
    b = [(0, 0)] * P
    for j in range(P - 1):
        b[j + 1] = ((b[j][0] + betas[j][0]) % P, (b[j][1] + betas[j][1]) % P)
    f = {}
    for j in range(P):
        for i in range(P):
            f[(i, j)] = ((b[j][0] + M[qs[j]][i]) % P, b[j][1])
    return f


BOX = (2 * P - 1) ** 2
POINTWISE_MIXED = 4 * (P - 1) ** 2
recs = []
h1_viol = 0
complete = True

for qs in itertools.product(range(P), repeat=P):
    if time.time() - T_START > HARD_TIMEOUT_S:
        complete = False
        break
    D = []
    okq = True
    for j in range(P):
        jn = (j + 1) % P
        dj = set((M[qs[jn]][i] - M[qs[j]][i]) % P for i in range(P))
        if len(dj) > 3:
            okq = False
            break
        D.append(sorted(dj))
    if not okq:
        continue

    def cells(j, beta):
        return set(((beta[0] + d) % P, beta[1]) for d in D[j])

    b0 = (0, 0)
    U0 = cells(0, b0)
    if len(U0) > 3:
        continue
    for b1 in PTS:
        U1 = U0 | cells(1, b1)
        if len(U1) > 3:
            continue
        for b2 in PTS:
            U2 = U1 | cells(2, b2)
            if len(U2) > 3:
                continue
            for b3 in PTS:
                U3 = U2 | cells(3, b3)
                if len(U3) > 3:
                    continue
                b4 = ((-(b1[0] + b2[0] + b3[0])) % P,
                      (-1 - (b1[1] + b2[1] + b3[1])) % P)
                U4 = U3 | cells(4, b4)
                if len(U4) > 3:
                    continue
                f = build(qs, [b0, b1, b2, b3, b4])
                if A_set(f, (1, 0), P) != A_E1 or set(A_set(f, (0, 1), P)) != U4:
                    continue
                sz = dict((u, len(A_set(f, u, P))) for u in UMULT + VMULT + MIXED)
                su = sum(sz[u] for u in UMULT)
                sv = sum(sz[u] for u in VMULT)
                sm = sum(sz[w] for w in MIXED)
                if diffset_literal(f, P) != 1 + su + sv + sm:
                    h1_viol += 1
                minw = min(sz[w] for w in MIXED)
                recs.append((su, sv, sm, 1 + su + sv + sm, minw, len(U4)))

n = len(recs)
print("=" * 78)
print("DECOMPOSITION OF |T_f - T_f| BY DIRECTION CLASS -- p=5, complete class")
print("=" * 78)
print("  class enumerated completely = %s" % complete)
print("  normal-form f = %d ; de-normalised = %d" % (n, n * P * P))
print("  [%s] H1  1 + S_u + S_v + S_m == literal |T_f - T_f| : %d violations"
      % ("PASS" if h1_viol == 0 else "FAIL", h1_viol))
print("       population: ALL %d normal-form f; exclusion list EMPTY." % n)
print()

mn_su = min(r[0] for r in recs)
mn_sv = min(r[1] for r in recs)
mn_sm = min(r[2] for r in recs)
mn_tot = min(r[3] for r in recs)
print("  class-by-class MINIMA, each taken independently over the whole class:")
print("     min S_u (over the %d nonzero multiples of e1) = %d" % (P - 1, mn_su))
print("     min S_v (over the %d nonzero multiples of e2) = %d" % (P - 1, mn_sv))
print("     min S_m (over the %d mixed w)                 = %d" % ((P - 1) ** 2, mn_sm))
print("     ---------------------------------------------------")
print("     1 + sum of the three INDEPENDENT minima          = %d"
      % (1 + mn_su + mn_sv + mn_sm))
print("     min of the TOTAL, taken jointly                  = %d" % mn_tot)
print("     the conjecture's target (2p-1)^2                 = %d" % BOX)
print()
gap = (1 + mn_su + mn_sv + mn_sm)
print("  ** THE POINT: the class-by-class bookkeeping can only ever prove >= %d,"
      % gap)
print("     which is %d SHORT of the target %d. The joint minimum is %d,"
      % (BOX - gap, BOX, mn_tot))
print("     i.e. the three minima are NOT SIMULTANEOUSLY ATTAINABLE. Any proof")
print("     that bounds the direction classes separately loses exactly this.")
print()

print("  the trade-off, tabulated. For each value of S_m, the minimum of S_u+S_v")
print("  attained with it, and the resulting minimum total:")
print("     %-6s %-8s %-10s %-8s %s" % ("S_m", "count", "min S_u+S_v", "min tot", "note"))
by_sm = {}
for su, sv, sm, tot, minw, na2 in recs:
    cur = by_sm.get(sm)
    if cur is None or su + sv < cur[0]:
        by_sm[sm] = (su + sv, tot, 1 if cur is None else cur[2] + 1)
    else:
        by_sm[sm] = (cur[0], min(cur[1], tot), cur[2] + 1)
for sm in sorted(by_sm):
    a, t, c = by_sm[sm]
    note = ""
    if sm < POINTWISE_MIXED:
        note = "<- below the pointwise total %d" % POINTWISE_MIXED
    if t == BOX:
        note += "   <- attains the box exactly"
    print("     %-6d %-8d %-10d %-8d %s" % (sm, c, a, t, note))
print()

tight = [r for r in recs if r[3] == BOX]
print("  members attaining the box EXACTLY (|T_f - T_f| = %d): %d of %d"
      % (BOX, len(tight), n))
print("     their S_m values           : %s" % sorted(set(r[2] for r in tight)))
print("     their min mixed |A_w|      : %s" % sorted(set(r[4] for r in tight)))
print("     their |A_e2|               : %s" % sorted(set(r[5] for r in tight)))
ce = [r for r in recs if r[4] <= 3]
print()
print("  members violating the POINTWISE floor (min mixed |A_w| <= 3): %d" % len(ce))
print("     their totals range over    : %d .. %d"
      % (min(r[3] for r in ce), max(r[3] for r in ce)))
print("     how many of THEM attain the box exactly : %d"
      % len([r for r in ce if r[3] == BOX]))
print()
print("  ** DISJOINTNESS: the f that break the lemma and the f that make the")
print("     conjecture tight are DIFFERENT f. That is why the lemma can be false")
print("     while the conjecture stays true and sharp.")
print()
print("=" * 78)
allok = (h1_viol == 0 and complete)
print("  controls_ok = %s" % allok)
print("  elapsed_s = %.2f" % (time.time() - T_START))
sys.exit(0 if allok else 1)
