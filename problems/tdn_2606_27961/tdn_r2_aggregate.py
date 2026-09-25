#!/usr/bin/env python3
"""owner-tdn round 2 -- does the AGGREGATE survive what the POINTWISE floor lost?

THE QUESTION THIS ASKS, AND WHY IT IS NOT THE ONE ALREADY ANSWERED
------------------------------------------------------------------
Clause (3) asked whether Sec.6's POINTWISE conclusion

        |A_w| >= 4   for EVERY mixed w

survives weakening |A_u| = |A_v| = 2 to <= 3.  Round 2's certificate answers NO.
But the conjecture never needed the pointwise statement.  What the conjecture
needs is only

        sum over u != 0 of |A_u|  >=  (2p-1)^2 - 1,

and the pointwise floor was merely the route the paper had to it.  The census
(tdn_r2_class_census.py) reported that EVERY counterexample in the class fails
on exactly 2 of the 16 mixed directions -- w and -w, one direction up to sign.
That is a very small pointwise loss, and it costs the SUM at most 2.

So the sharp question is whether the AGGREGATE form of the Case-A conclusion
survives the same weakening that killed the pointwise form:

    Q1  is  sum over mixed w of |A_w|  >=  4(p-1)^2   still true?
        (4(p-1)^2 is exactly the total the pointwise floor would have delivered)
    Q2  is  |T_f - T_f| >= (2p-1)^2  -- THE CONJECTURE ITSELF -- true on the
        whole class?

Both are answered here by a COMPLETE census of the same sub-population, so both
answers carry a population and any zero carries an exclusion list.

SUB-POPULATION (identical to tdn_r2_class_census.py; see that file for why the
enumeration is lossless and why it is a census rather than a barred search):
    { f : f(0) = 0 , A_e1(f) = {(0,0),(1,0)} exactly , |A_e2(f)| <= 3 }

CONTROL THAT COULD FAIL
    G1  for EVERY f enumerated, the Sec.6 fibre sum  sum_u |A_u|  is compared
        against |T_f - T_f| computed LITERALLY as a difference set in
        (Z/p^2 Z)^2.  No shared code path.  Population = the entire class.

Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r2_aggregate.py
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
NONZERO = [u for u in PTS if u != (0, 0)]
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
    """|T_f - T_f| computed literally in (Z/p^2 Z)^2. Uses no Sec.6 machinery."""
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


# ------------------------------------------------------------------- the run
BOX = (2 * P - 1) ** 2                      # the conjecture's target
PAPER_UNCOND = 3 * P * P - P - 1            # the paper's proved bound
POINTWISE_TOTAL = 4 * (P - 1) ** 2          # what the pointwise floor would give

print("=" * 78)
print("AGGREGATE vs POINTWISE on the p=5 class  A_e1={(0,0),(1,0)}, |A_e2|<=3")
print("=" * 78)
print("  reference values, computed not narrated:")
print("     (2p-1)^2                      = %d   <- the conjecture's target" % BOX)
print("     3p^2 - p - 1                  = %d   <- the paper's PROVED bound"
      % PAPER_UNCOND)
print("     4(p-1)^2                      = %d   <- total the POINTWISE floor"
      " would deliver on mixed w" % POINTWISE_TOTAL)
print()

n = 0
g1_viol = 0
below_box = []            # f with |T-T| < BOX  -> would refute the CONJECTURE
below_pointwise = []      # f with mixed sum < POINTWISE_TOTAL
min_mixed_sum = None
min_total = None
ce_count = 0
ce_min_mixed_sum = None
ce_min_total = None
mixed_sum_hist = {}
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
                betas = [b0, b1, b2, b3, b4]
                f = build(qs, betas)
                if A_set(f, (1, 0), P) != A_E1 or set(A_set(f, (0, 1), P)) != U4:
                    continue
                n += 1

                sizes = dict((u, len(A_set(f, u, P))) for u in NONZERO)
                mixed_sum = sum(sizes[w] for w in MIXED)
                total = sum(sizes.values()) + 1          # u = 0 contributes 1

                # ---- G1: control that could fail, on EVERY member
                if diffset_literal(f, P) != total:
                    g1_viol += 1

                mixed_sum_hist[mixed_sum] = mixed_sum_hist.get(mixed_sum, 0) + 1
                if min_mixed_sum is None or mixed_sum < min_mixed_sum:
                    min_mixed_sum = mixed_sum
                if min_total is None or total < min_total:
                    min_total = total
                if total < BOX:
                    below_box.append((tuple(qs), tuple(betas), total))
                if mixed_sum < POINTWISE_TOTAL:
                    below_pointwise.append((tuple(qs), tuple(betas), mixed_sum))
                if min(sizes[w] for w in MIXED) <= 3:
                    ce_count += 1
                    if ce_min_mixed_sum is None or mixed_sum < ce_min_mixed_sum:
                        ce_min_mixed_sum = mixed_sum
                    if ce_min_total is None or total < ce_min_total:
                        ce_min_total = total

print("  class enumerated completely = %s ; normal-form f = %d ; de-normalised"
      " = %d" % (complete, n, n * P * P))
print("  elapsed_s so far = %.1f" % (time.time() - T_START))
print()
print("=" * 78)
print("CONTROL")
print("=" * 78)
print("  [%s] G1  Sec.6 fibre sum  ==  literal |T_f - T_f| in (Z/%dZ)^2 :"
      " %d violations" % ("PASS" if g1_viol == 0 else "FAIL", P * P, g1_viol))
print("       population: ALL %d normal-form f of the class; exclusion list"
      " EMPTY (no sampling)." % n)
print()
print("=" * 78)
print("Q1 -- does the AGGREGATE mixed-direction bound survive?")
print("=" * 78)
print("  min over the class of  sum over mixed w of |A_w|   = %d" % min_mixed_sum)
print("  the pointwise floor would deliver                   = %d"
      % POINTWISE_TOTAL)
print("  members BELOW the pointwise total                   = %d"
      % len(below_pointwise))
print("  population: all %d normal-form f (%d de-normalised); exclusion list"
      " EMPTY." % (n, n * P * P))
print()
print("  distribution of sum over mixed w of |A_w|:")
for k in sorted(mixed_sum_hist):
    print("     %3d : %6d normal-form f" % (k, mixed_sum_hist[k]))
print()
print("=" * 78)
print("Q2 -- is the CONJECTURE true on this class?")
print("=" * 78)
print("  min over the class of |T_f - T_f|      = %d" % min_total)
print("  the conjecture's target (2p-1)^2       = %d" % BOX)
print("  the paper's proved bound 3p^2-p-1      = %d" % PAPER_UNCOND)
print("  members with |T_f - T_f| < (2p-1)^2    = %d" % len(below_box))
print("  population: all %d normal-form f (%d de-normalised); exclusion list"
      " EMPTY -- every member tested, none skipped, none sampled."
      % (n, n * P * P))
print()
print("=" * 78)
print("THE COUNTEREXAMPLES SPECIFICALLY (pointwise floor fails on these)")
print("=" * 78)
print("  count                                   = %d" % ce_count)
print("  min over THEM of sum over mixed |A_w|   = %d  (pointwise total = %d)"
      % (ce_min_mixed_sum, POINTWISE_TOTAL))
print("  min over THEM of |T_f - T_f|            = %d  (target = %d)"
      % (ce_min_total, BOX))
print()
print("=" * 78)
allok = (g1_viol == 0 and complete)
print("  controls_ok = %s" % allok)
print("  elapsed_s = %.2f" % (time.time() - T_START))
sys.exit(0 if allok else 1)
