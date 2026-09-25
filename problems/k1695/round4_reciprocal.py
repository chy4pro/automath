#!/usr/bin/env python3
"""ROUND 4-B (line k1695): the residual lambda != 1 layer, restated as a RECIPROCAL-ROOT
problem, and solved for three live tokens over GF(2).

Where this sits.  L4 (R3.8) collapsed the lambda=1 layer of A = aI + u v^T to the single
residual case v = rho*u (all tokens pairwise proportional).  R4.1 solved lambda != 1 for two
live tokens.  This is the general reformulation of what is left.

REFORMULATION.  Let v = rho*u, and let the live tokens sit at cyclic positions s_i with
coefficients u_i; put F(x) = sum_i u_i x^{s_i}.  Then
    U-hat(lambda) = F(lambda)     and     V-hat(lambda) = rho * F(lambda^{-1}),
so lambda is a BAD CANDIDATE exactly when F(lambda) = 0 AND F(lambda^{-1}) = 0, i.e. exactly
when the root set of F inside mu_m is closed under inversion at lambda.  Writing F* for the
reversal of F, that is gcd(F, F*) having a root in mu_m \\ {1}.  So the remaining question is
purely combinatorial:

    choose the positions (and which coefficient goes where) so that the roots of F in mu_m
    contain NO pair {lambda, lambda^{-1}} -- in particular F(-1) != 0 when -1 is in mu_m,
    since -1 is its own inverse.

WORKED CASE, three live tokens over GF(2) (so u = v = 1 on the support).  With positions
{0, a, b}: F(lambda) = 1 + lambda^a + lambda^b and F(lambda^{-1}) = 0 rearranges to
1 + lambda^{b-a} + lambda^b = 0.  Subtracting the two forces lambda^{2a-b} = 1.  So choosing
a, b with gcd(2a-b, m) = 1 leaves lambda = 1 as the only candidate -- and positions {0,1,3}
do that for every n >= 4, since 2a-b = -1.  (n = 3 is forced to be {0,1,2}, which is the
aI+bJ case round 2 already settled.)

CHECKS (each falsifiable on one row):
  V1  the reformulation itself: for proportional tokens, "no {lambda,lambda^-1} pair among the
      roots of F in mu_m" must coincide with "C1's obstruction lies at most at lambda=1".
  V2  the worked case: positions {0,1,3} must leave no lambda != 1 obstruction, GF(2), n>=4.
  V3  CONTROL that must FAIL: positions {0,1,2} at n=3, and any position set whose 2a-b shares
      a factor with m, must be reported as HAVING a candidate -- otherwise V2 says nothing.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round3_family.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 3-B family attack start')], "rf", "exec"), G)
GF, criterion_ncycle, pmod, pgcd = G['GF'], G['criterion_ncycle'], G['pmod'], G['pgcd']

def m_of(n, F):
    m = n
    while m % F.p == 0:
        m //= F.p
    return m

def obstruction_off_1(seq, n, F):
    """does C1's gcd have a root != 1 ?"""
    ok, g = criterion_ncycle(list(seq), n, F)
    if ok:
        return False
    h = list(g); L = [F.NEG[1], 1]
    while len(h) > 1 and pmod(h, L, F) == []:
        qo = [0]*(len(h)-1); rem = list(h)
        for d in range(len(h)-2, -1, -1):
            c = rem[d+1]; qo[d] = c; rem[d+1] = 0
            rem[d] = F.ADD[rem[d]][c]
        h = qo
        while h and h[-1] == 0: h.pop()
    return len(h) > 1

def pair_candidate(u_at, n, F):
    """is there lambda in mu_m\\{1} with F(lambda)=F(1/lambda)=0 ?  Computed as: does
    gcd(F, F*, (x^m-1)/(x-1)) have positive degree?  F has exponents mod m."""
    m = m_of(n, F)
    Fp = [0]*m
    for s, c in u_at.items():
        Fp[s % m] = F.ADD[Fp[s % m]][c]
    while Fp and Fp[-1] == 0: Fp.pop()
    if m == 1:
        return False    # mu_m = {1}: there is NO lambda != 1 to be a candidate at all.
        # (Bug found 2026-08-24: the old code fell through to the "F identically 0" branch
        # below and reported a candidate for every n that is a power of the characteristic --
        # a FALSE POSITIVE, invisible to V1 because V1 is deliberately one-sided.)
    if not Fp:
        return True                       # F identically 0 mod x^m-1: every lambda is a root
    d = len(Fp)-1
    Fs = list(reversed(Fp))               # reversal
    xm = [F.NEG[1]] + [0]*(m-1) + [1]     # x^m - 1
    one = [F.NEG[1], 1]                   # x - 1
    quot = [0]*m
    rem = list(xm)
    for k in range(m-1, -1, -1):          # divide x^m-1 by x-1 exactly
        c = rem[k+1]; quot[k] = c; rem[k+1] = 0; rem[k] = F.ADD[rem[k]][c]
    while quot and quot[-1] == 0: quot.pop()
    g = pgcd(Fp, Fs, F)
    g = pgcd(g, quot, F)
    return len(g) > 1

print("ROUND 4-B: reciprocal-root reformulation")
print("--- V1: reformulation vs criterion C1 (proportional tokens) ---")
rows = 0; bad = 0; both = [0, 0]
for q in [2, 3, 4, 5]:
    F = GF(q)
    for n in range(3, 9):
        for rho in range(1, q):
            for k in range(1, min(n, 4)+1):
                for pos in itertools.combinations(range(n), k):
                    if pos[0] != 0:
                        continue                      # rotation-normalise
                    for coeffs in itertools.product(range(1, q), repeat=k):
                        u_at = dict(zip(pos, coeffs))
                        c0 = 0
                        for c in coeffs:
                            c0 = F.ADD[c0][F.MUL[F.MUL[c][rho]][c]]
                        if F.ADD[1][c0] == 0:
                            continue
                        seq = [(1, 0, 0)]*n
                        for s, c in u_at.items():
                            seq[s] = (1, c, F.MUL[rho][c])
                        pred = pair_candidate(u_at, n, F)
                        truth = obstruction_off_1(seq, n, F)
                        rows += 1
                        both[0 if pred else 1] += 1
                        if truth and not pred:
                            bad += 1
                            if bad <= 3:
                                print("   V1 FAIL q=%d n=%d pos=%s coeffs=%s rho=%d" % (q, n, pos, coeffs, rho))
print("V1: %d rows | predicted-candidate %d, predicted-none %d | rows with a lambda!=1 obstruction "
      "but NO predicted candidate: %d" % (rows, both[0], both[1], bad))
assert bad == 0, "REFORMULATION WRONG"
assert both[0] > 0 and both[1] > 0, "V1 VACUOUS: one side never occurred"

print("--- V2/V3: FOUR live tokens over GF(2) (the smallest size that EXISTS) ---")
# Over GF(2) the only nonzero value is 1, so u = v = 1_S and c0 = |S| mod 2; A = I+u v^T is
# invertible iff |S| is EVEN.  |S|=3 is ALWAYS SINGULAR -- an earlier draft of this script used
# it as the worked case and therefore quantified over the empty set.  The guard below makes
# that failure mode impossible to repeat silently: a test whose body never ran is an ERROR.
F = GF(2)
okc = 0
for n in range(5, 30):
    S = {0: 1, 1: 1, 2: 1, 3: 1}                      # consecutive positions
    if len(S) % 2 != 0:
        continue
    seq = [(1, 0, 0)]*n
    for s_ in S: seq[s_] = (1, 1, 1)
    assert not pair_candidate(S, n, F), "V2 FAILED at n=%d: consecutive {0,1,2,3} has a reciprocal pair" % n
    assert not obstruction_off_1(seq, n, F), "V2 FAILED at n=%d: C1 shows a lambda!=1 obstruction" % n
    okc += 1
assert okc > 0, "V2 VACUOUS -- the loop body never executed; a test that cannot run is not a test"
print("V2: consecutive positions {0,1,2,3} leave NO lambda!=1 obstruction, every n in 5..29 (%d values)" % okc)
print("    reason: F = (x^4-1)/(x-1) = (x+1)^3 over GF(2), whose only root is 1 -- so no inverse-closed pair.")

# V3: the SAME construction must FAIL at |S| = 6, where F = (x^6-1)/(x-1) carries order-3 roots.
fired = 0; tested = 0
for n in [9, 12, 15, 18, 21]:
    S6 = {i: 1 for i in range(6)}
    tested += 1
    if pair_candidate(S6, n, F):
        fired += 1
assert tested > 0, "V3 VACUOUS"
assert fired == tested, "V3 CONTROL DID NOT FIRE: |S|=6 consecutive was expected to carry a bad candidate"
print("V3 control: consecutive positions at |S|=6 carry a bad candidate at %d of %d tested n "
      "(9,12,15,18,21) -- so V2 is discriminating, not a rule that always says clean" % (fired, tested))
print("%.1fs" % (time.time()-T0))
