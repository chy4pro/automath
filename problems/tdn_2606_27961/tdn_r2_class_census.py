#!/usr/bin/env python3
"""owner-tdn round 2 -- COMPLETE CENSUS of the p=5 class that contains the
counterexample, and an independent RE-DERIVATION of it by search.

WHY THIS EXISTS
---------------
Round 1 found the counterexample twice, but preserved no search script: the
witness survived only as a table in prose.  tdn_r2_certificate.py restores the
VERIFICATION side (witness as data, verdict computed).  This file restores the
PRODUCTION side -- it FINDS witnesses, from nothing but the definitions, and it
enumerates its class to completion so that every count below carries a
population and every zero carries an exclusion list.

It also replaces round 1's weakest sentence.  The p=5 census recorded
"counterexamples: 5" with a recorder that CAPPED at 5 -- a censored count, which
is not a count.  This file reports the exact number in a fully specified
sub-population.

THE SUB-POPULATION, stated exactly
----------------------------------
    { f : F_5^2 -> F_5^2 ,  f(0) = 0 ,  A_e1(f) = {(0,0),(1,0)}  exactly ,
                                        |A_e2(f)| <= 3 }
This is ONE A-class of the round-1 census.  It is a complete sub-population, so
a completed enumeration of it is a rigorous statement about IT and about
nothing else.  It is NOT all of p=5 and is never reported as such.

WHY THE ENUMERATION IS SMALL, AND WHY IT IS LOSSLESS (no exhaustion of F_5^2's
function space, which is 5^48 and barred)
-----------------------------------------
1. ROWS.  f <-> (base b_j = f(0,j), word w_j) with w_j[i] = d_e1 f(i,j).  The
   cycle identity says sum_i w_j[i] = -e1, so the parametrisation ABSORBS it.
   With alphabet {(0,0),(1,0)}, a word of length 5 summing to (-1,0) needs
   exactly four (1,0)s and one (0,0)  ->  exactly 5 words per row, indexed by
   the position q_j of the (0,0) letter.  Every row therefore uses BOTH letters,
   so A_e1 = {(0,0),(1,0)} exactly, automatically.
2. COLUMNS.  With f(i,j) = b_j + (m_j(i), 0), the vertical derivative is
   d_e2 f(i,j) = beta_j + (delta_j(i), 0),  beta_j = b_{j+1} - b_j - (0,[j=4]),
   delta_j(i) = m_{j+1}(i) - m_j(i).  Since delta_j(0) = 0, beta_j is itself in
   A_e2 -- so |A_e2| <= 3 prunes the beta-search hard.
3. CLOSURE.  sum_j beta_j = (0,-1) identically, so beta_4 is DETERMINED by
   beta_0..beta_3.  No search over it.
4. NORMALISATION.  The free p^4 action f -> f + lam*x_1 + mu*x_2 shifts A_e1 by
   lam and A_e2 by mu.  Fixing A_e1 = {(0,0),(1,0)} forces lam = 0 (that set is
   not translation-invariant); mu stays free and shifts every beta_j by mu.  So
   WLOG beta_0 = (0,0), and the de-normalisation factor is exactly p^2 = 25.
   The action preserves every |A_w| -- verified as control C5 of
   tdn_r2_certificate.py over all 625 group elements -- so this reduction is
   LOSSLESS for the rigidity question.

CONTROLS THAT COULD FAIL
------------------------
    K1  Every f produced satisfies A_e1 = {(0,0),(1,0)} exactly and
        |A_e2| <= 3, re-checked from the DEFINITIONS (not from the
        parametrisation that built it).  A parametrisation bug shows up here.
    K2  THE PAPER'S OWN THEOREM AS A CONTROL.  Among enumerated f with
        |A_e2| = 2, both e1 and e2 are 2-point independent directions, i.e.
        the paper's PROVED Case A -- so the count of those with any mixed
        |A_w| <= 3 MUST be 0.  If it is not, this code is wrong, not the paper.
    K3  The round-1 witness must be re-found by this search, which shares no
        code with the round-1 census DFS.

Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r2_class_census.py
"""
import itertools
import sys
import time

T_START = time.time()
HARD_TIMEOUT_S = 600          # self-limit, PROTOCOL hard constraint 3
try:
    sys.stdout.reconfigure(line_buffering=True)
except AttributeError:
    pass

P = 5
PTS = [(a, b) for a in range(P) for b in range(P)]
MIXED = [(a, b) for a in range(1, P) for b in range(1, P)]

# Round 1's witness, transcribed as DATA, used only by control K3.
WITNESS_ROWS = [
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],
    [(2, 2), (2, 2), (3, 2), (4, 2), (0, 2)],
    [(2, 2), (3, 2), (3, 2), (4, 2), (0, 2)],
    [(4, 4), (0, 4), (0, 4), (1, 4), (2, 4)],
]


# ---------------------------------------------------- definitions, from scratch
def carry(u, x, p):
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def A_set(f, u, p):
    """A_u(f) = { f(x+u) - f(x) + c_u(x) }, straight from the definition."""
    out = set()
    for x in PTS:
        y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
        c = carry(u, x, p)
        fy, fx = f[y], f[x]
        out.add(((fy[0] - fx[0] + c[0]) % p, (fy[1] - fx[1] + c[1]) % p))
    return frozenset(out)


# ------------------------------------------------------------ parametrisation
# m[q][i] = number of (1,0) letters among the first i letters of the word whose
# (0,0) letter sits at position q.
M = [[i - (1 if q < i else 0) for i in range(P)] for q in range(P)]

A_E1 = frozenset([(0, 0), (1, 0)])


def build(qs, betas):
    """(word positions q_0..q_4, betas beta_0..beta_4) -> f as {(i,j): value}."""
    b = [(0, 0)] * P
    for j in range(P - 1):
        b[j + 1] = ((b[j][0] + betas[j][0]) % P, (b[j][1] + betas[j][1]) % P)
    f = {}
    for j in range(P):
        for i in range(P):
            f[(i, j)] = ((b[j][0] + M[qs[j]][i]) % P, b[j][1])
    return f


def a_e2_union(qs, betas):
    """A_e2 predicted by the parametrisation (used for pruning only)."""
    u = set()
    for j in range(P):
        jn = (j + 1) % P
        for i in range(P):
            d = (M[qs[jn]][i] - M[qs[j]][i]) % P
            u.add(((betas[j][0] + d) % P, betas[j][1]))
    return u


# ---------------------------------------------------------------------- search
print("=" * 78)
print("COMPLETE CENSUS -- p=5 class  A_e1 = {(0,0),(1,0)},  |A_e2| <= 3")
print("=" * 78)

n_norm = 0                    # normal-form f found (beta_0 = (0,0))
n_ce = 0                      # of those, ones with some mixed |A_w| <= 3
n_caseA = 0                   # of those, ones with |A_e2| = 2 (paper's Case A)
n_caseA_ce = 0                # K2: MUST be 0
k1_viol = 0                   # K1 violations
minw_hist = {}                # min mixed |A_w| -> count
ce_examples = []              # every counterexample, uncapped
found_witness = False
complete = True

witness = dict(((i, j), WITNESS_ROWS[j][i]) for j in range(P) for i in range(P))

for qs in itertools.product(range(P), repeat=P):
    if time.time() - T_START > HARD_TIMEOUT_S:
        complete = False
        break
    # delta sets per j; if any exceeds 3 points this word-tuple is impossible
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

    # DFS over beta_1..beta_3 (beta_0 = (0,0) by normalisation, beta_4 forced)
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
                # sum_j beta_j = (0,-1)  =>  beta_4 is determined
                b4 = ((-(b0[0] + b1[0] + b2[0] + b3[0])) % P,
                      (-1 - (b0[1] + b1[1] + b2[1] + b3[1])) % P)
                U4 = U3 | cells(4, b4)
                if len(U4) > 3:
                    continue

                betas = [b0, b1, b2, b3, b4]
                f = build(qs, betas)

                # ---- K1: re-check from the DEFINITIONS, not the parametrisation
                a1 = A_set(f, (1, 0), P)
                a2 = A_set(f, (0, 1), P)
                if a1 != A_E1 or len(a2) > 3 or set(a2) != U4:
                    k1_viol += 1
                    continue

                n_norm += 1
                sizes = [len(A_set(f, w, P)) for w in MIXED]
                lo = min(sizes)
                minw_hist[lo] = minw_hist.get(lo, 0) + 1
                is_ce = lo <= 3
                if len(a2) == 2:
                    n_caseA += 1
                    if is_ce:
                        n_caseA_ce += 1
                if is_ce:
                    n_ce += 1
                    ce_examples.append(
                        (tuple(qs), tuple(betas), sorted(a2),
                         [MIXED[t] for t in range(len(MIXED)) if sizes[t] <= 3]))
                if f == witness:
                    found_witness = True

print("  enumeration complete = %s   elapsed_s = %.1f"
      % (complete, time.time() - T_START))
print()
print("  normal-form f in the class (beta_0 = (0,0))        : %d" % n_norm)
print("  de-normalised class size (x p^2 = %d, action free) : %d"
      % (P * P, n_norm * P * P))
print("  population searched: all %d word-tuples x all beta-tuples surviving"
      " the |A_e2| <= 3 prune; beta_4 forced by the cycle identity."
      % (P ** P))
print()

print("=" * 78)
print("CONTROLS")
print("=" * 78)
print("  [%s] K1  every f re-checked from the definitions (A_e1 exact, A_e2"
      " matches): %d violations"
      % ("PASS" if k1_viol == 0 else "FAIL", k1_viol))
print("  [%s] K2  PAPER'S THEOREM AS CONTROL: of the %d normal-form f with"
      " |A_e2| = 2 (the paper's PROVED Case A), the number with any mixed"
      " |A_w| <= 3 is %d"
      % ("PASS" if n_caseA_ce == 0 else "FAIL", n_caseA, n_caseA_ce))
print("       exclusion list for that zero: NONE -- all %d Case-A members of"
      " this class were tested on all %d mixed directions."
      % (n_caseA, len(MIXED)))
print("  [%s] K3  round-1 witness re-found by this independent search: %s"
      % ("PASS" if found_witness else "FAIL", found_witness))
print()

print("=" * 78)
print("RESULT -- the counterexamples, UNCAPPED, with their population")
print("=" * 78)
print("  normal-form f with min mixed |A_w| <= 3   : %d" % n_ce)
print("  de-normalised                             : %d" % (n_ce * P * P))
print("  population for both                       : the %d normal-form f"
      " (%d de-normalised) of this class; exclusion list EMPTY."
      % (n_norm, n_norm * P * P))
print()
print("  distribution of  min over mixed w of |A_w|  across the class:")
for k in sorted(minw_hist):
    print("     min |A_w| = %d :  %6d normal-form f  (%.4f of class)"
          % (k, minw_hist[k], float(minw_hist[k]) / max(n_norm, 1)))
print()
print("  how many of the %d mixed directions fail, per counterexample:" % len(MIXED))
fh = {}
for _, _, _, bad in ce_examples:
    fh[len(bad)] = fh.get(len(bad), 0) + 1
for k in sorted(fh):
    print("     %d failing mixed direction(s) : %d normal-form f" % (k, fh[k]))
print()
print("  |A_e2| of the counterexamples:")
sh = {}
for _, _, a2, _ in ce_examples:
    sh[len(a2)] = sh.get(len(a2), 0) + 1
for k in sorted(sh):
    print("     |A_e2| = %d : %d normal-form f" % (k, sh[k]))
print()
print("  first counterexamples found (q-tuple, betas, A_e2, failing mixed w):")
for rec in ce_examples[:8]:
    print("     q=%s  beta=%s  A_e2=%s  bad_w=%s" % rec)

print()
print("=" * 78)
allok = (k1_viol == 0 and n_caseA_ce == 0 and found_witness and complete)
print("  controls_ok = %s" % allok)
print("  elapsed_s = %.2f" % (time.time() - T_START))
sys.exit(0 if allok else 1)
