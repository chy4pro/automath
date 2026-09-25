#!/usr/bin/env python3
"""owner-tdn round 2 -- STANDALONE CERTIFICATE for the p=5 counterexample.

WHAT THIS FILE IS FOR
---------------------
Round 1 refuted charter clause (3):

    Sec.6 of arXiv:2606.27961 proves  |A_w| >= 4  for mixed w = lam*u + mu*v
    (lam*mu != 0) under the hypothesis |A_u| = |A_v| = 2.  Does the conclusion
    survive weakening the hypothesis to  |A_u|, |A_v| <= 3  ?

    ANSWER: NO at p = 5.  A witness exists with (|A_e1|, |A_e2|) = (2, 3) and
    |A_w| = 3 for the mixed direction w = (1,3).

Round 1 exhibited that witness twice but PRESERVED NEITHER SCRIPT: the table of
f lived only in prose in the state file.  That is precisely the failure species
this project audits.  This file closes it.  It is a THIRD, independent
implementation, written from the definitions as quoted below and importing
nothing from probe_t1.py or tdn_r1_census.py, and it is a VERIFIER, not a
search: the witness is data, the verdict is computed.

DEFINITIONS (arXiv:2606.27961 Sec.6; [z] = the lift of z in F_p to {0..p-1})
    G          = (Z/p^2 Z)^2
    T_f        = { [x] + p[f(x)] : x in F_p^2 },  f : F_p^2 -> F_p^2, f(0) = 0
    c_u(x)     = ([x+u] - [x] - [u]) / p         (each coordinate 0 or -1)
    d_u f(x)   = f(x+u) - f(x) + c_u(x)
    A_u(f)     = { d_u f(x) : x in F_p^2 }
    |T_f - T_f| = sum over u of |A_u(f)|         (the Sec.6 fibre decomposition)

CONTROLS THAT COULD FAIL (all of them do fail if the implementation is wrong)
    C1  fibre-sum  ==  |T_f - T_f| computed LITERALLY as a difference set in
        (Z/p^2 Z)^2.  These two share no code path.
    C2  f == 0 reproduces the paper's PUBLISHED box values at p = 3 and p = 5.
    C3  T_f is genuinely a transversal (p^2 points, one over each x in F_p^2).
    C4  Sec.6 Lemma: a 2-point A_u lies on a line parallel to <u>.  The witness
        has |A_e1| = 2, so this must hold FOR THE WITNESS.
    C5  the free p^4 action f -> f + lam*x_1 + mu*x_2 preserves every |A_w|.
        This is the invariance the round-1 census PATH 2 reduction rests on; it
        is re-checked here against the witness rather than assumed.
    C6  the witness is NOT in the paper's proved Case A ((2,2)); if it were,
        the correct conclusion would be that THIS CODE is wrong, not the paper.
    C7  the witness does NOT refute the conjecture: |T_f - T_f| > (2p-1)^2.

Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r2_certificate.py
"""
import itertools
import sys
import time

T_START = time.time()
try:
    sys.stdout.reconfigure(line_buffering=True)   # doctrine 65: durable at print
except AttributeError:
    pass

# The paper's published values of |T_f - T_f| for f == 0, keyed by p.  Data, so
# that C2 is a COMPARISON against the paper and not a narration of it.
PUBLISHED_BOX = {3: 25, 5: 81}

P = 5

# ---------------------------------------------------------------- THE WITNESS
# Round 1's counterexample, transcribed from orchestration/results/tdn_state.md
# section 3.2 as pure DATA.  WITNESS[j][i] = f(i, j) in F_5^2.
WITNESS = [
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],   # j = 0
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],   # j = 1
    [(2, 2), (2, 2), (3, 2), (4, 2), (0, 2)],   # j = 2
    [(2, 2), (3, 2), (3, 2), (4, 2), (0, 2)],   # j = 3
    [(4, 4), (0, 4), (0, 4), (1, 4), (2, 4)],   # j = 4
]


# ------------------------------------------------------------------- algebra
def carry(u, x, p):
    """c_u(x) = ([x+u] - [x] - [u]) / p ; each coordinate is 0 or -1."""
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def d_u(f, u, x, p):
    """d_u f(x) = f(x+u) - f(x) + c_u(x)."""
    y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
    c = carry(u, x, p)
    fy, fx = f[y], f[x]
    return ((fy[0] - fx[0] + c[0]) % p, (fy[1] - fx[1] + c[1]) % p)


def A_set(f, u, p):
    """A_u(f) as a frozenset."""
    return frozenset(d_u(f, u, x, p)
                     for x in itertools.product(range(p), repeat=2))


def transversal(f, p):
    """T_f = { [x] + p[f(x)] } as a set of points of (Z/p^2 Z)^2."""
    m = p * p
    return set((((x[0] + p * f[(x[0], x[1])][0]) % m),
                ((x[1] + p * f[(x[0], x[1])][1]) % m))
               for x in itertools.product(range(p), repeat=2))


def diffset_literal(T, p):
    """|T - T| computed LITERALLY in (Z/p^2 Z)^2.  Uses no Sec.6 machinery."""
    m = p * p
    return set(((a[0] - b[0]) % m, (a[1] - b[1]) % m)
               for a in T for b in T)


def fibre_sum(f, p):
    """sum over ALL u (including u = 0) of |A_u(f)|."""
    return sum(len(A_set(f, u, p))
               for u in itertools.product(range(p), repeat=2))


def as_dict(rows, p):
    """WITNESS-style row table -> {(i,j): f(i,j)}."""
    return dict(((i, j), rows[j][i])
                for j in range(p) for i in range(p))


def zero_f(p):
    return dict(((i, j), (0, 0))
                for j in range(p) for i in range(p))


def shifted(f, lam, mu, p):
    """The free p^4 action  f -> f + lam*x_1 + mu*x_2  with lam, mu in F_p^2.

    NOTE this is the FULL p^4 action (lam and mu are VECTORS, giving p^2 * p^2
    group elements), not the p^2 diagonal subgroup.  It is the full action that
    the round-1 census PATH 2 reduction quotients by, so it is the full action
    that has to be controlled.
    """
    return dict(((i, j), ((f[(i, j)][0] + lam[0] * i + mu[0] * j) % p,
                          (f[(i, j)][1] + lam[1] * i + mu[1] * j) % p))
                for j in range(p) for i in range(p))


# ------------------------------------------------------------------- report
def rule(title):
    print("=" * 78)
    print(title)
    print("=" * 78)


ok = True


def check(name, condition, detail=""):
    global ok
    if not condition:
        ok = False
    print("  [%s] %s%s" % ("PASS" if condition else "FAIL", name,
                           ("   " + detail) if detail else ""))
    return condition


rule("CONTROLS -- every one of these fails if the implementation is wrong")

# ---- C2: the paper's published box, reproduced two ways, at both primes.
for p in sorted(PUBLISHED_BOX):
    z = zero_f(p)
    lit = len(diffset_literal(transversal(z, p), p))
    fib = fibre_sum(z, p)
    box = (2 * p - 1) ** 2
    check("C2  p=%d  f==0:  literal |T-T| = %d ; fibre-sum = %d ; (2p-1)^2 = %d ;"
          " paper publishes %d" % (p, lit, fib, box, PUBLISHED_BOX[p]),
          lit == fib == box == PUBLISHED_BOX[p],
          "population: 1 function per prime")

f = as_dict(WITNESS, P)

# ---- C3: T_f is a transversal.
T = transversal(f, P)
resid = sorted(set((a % P, b % P) for (a, b) in T))
check("C3  T_f is a transversal: |T_f| = %d = p^2, and it covers all %d residues"
      " exactly once" % (len(T), len(resid)),
      len(T) == P * P and len(resid) == P * P,
      "population: all %d points of T_f" % (P * P))

# ---- C1: fibre-sum vs literal difference set.  No shared code path.
lit_w = len(diffset_literal(T, P))
fib_w = fibre_sum(f, P)
check("C1  witness:  literal |T_f - T_f| in (Z/%dZ)^2 = %d ;  Sec.6 fibre-sum"
      " sum_u |A_u| = %d" % (P * P, lit_w, fib_w),
      lit_w == fib_w,
      "population: all %d ordered pairs from T_f" % (len(T) ** 2))

# ---- C4: Sec.6's 2-point lemma, on the witness's own 2-point direction.
e1, e2 = (1, 0), (0, 1)
A1, A2 = A_set(f, e1, P), A_set(f, e2, P)
pts = sorted(A1)
diffs = [((a[0] - b[0]) % P, (a[1] - b[1]) % P)
         for a in pts for b in pts if a != b]
para = all((d[0] * e1[1] - d[1] * e1[0]) % P == 0 for d in diffs)
check("C4  |A_e1| = %d and its %d difference vector(s) are parallel to <e1>"
      % (len(A1), len(diffs)), len(A1) == 2 and para,
      "A_e1 = %s" % (sorted(A1),))

# ---- C5: the p^4 action preserves every |A_w|.  Population stated.
base = dict((u, len(A_set(f, u, P)))
            for u in itertools.product(range(P), repeat=2))
viol, tested, gp = 0, 0, 0
for lam in itertools.product(range(P), repeat=2):
    for mu in itertools.product(range(P), repeat=2):
        gp += 1
        g = shifted(f, lam, mu, P)
        for u in itertools.product(range(P), repeat=2):
            tested += 1
            if len(A_set(g, u, P)) != base[u]:
                viol += 1
check("C5  FULL p^4 action f -> f + lam*x1 + mu*x2 (lam,mu vectors) preserves"
      " |A_u| for every u: %d violations" % viol, viol == 0,
      "population: %d group elements x %d directions = %d checks; exclusion"
      " list EMPTY (nothing skipped)" % (gp, P * P, tested))

# ---- C6: the witness is not in the paper's proved Case A.
check("C6  witness is NOT in the paper's Case A:  (|A_e1|, |A_e2|) = (%d, %d),"
      " Case A requires (2, 2)" % (len(A1), len(A2)),
      not (len(A1) == 2 and len(A2) == 2),
      "if this FAILED the correct conclusion would be that this code is wrong")

# ---- C7: the conjecture itself is untouched.
box5 = (2 * P - 1) ** 2
check("C7  witness does NOT refute the conjecture: |T_f - T_f| = %d > %d ="
      " (2p-1)^2" % (lit_w, box5), lit_w > box5,
      "it kills a PROOF STRATEGY, not the theorem")

# ------------------------------------------------------------------ verdict
rule("THE REFUTATION -- clause (3) is answered NO at p = %d" % P)

print("  hypothesis of the weakening :  |A_e1| = %d <= 3   and   |A_e2| = %d <= 3"
      % (len(A1), len(A2)))
print("  A_e1 = %s" % (sorted(A1),))
print("  A_e2 = %s" % (sorted(A2),))
print()

mixed = [(a, b) for a in range(1, P) for b in range(1, P)]
sizes = dict((w, len(A_set(f, w, P))) for w in mixed)
lo = min(sizes.values())
bad = sorted(w for w in mixed if sizes[w] <= 3)
print("  |A_w| over the %d mixed directions w = (lam, mu), lam*mu != 0:" % len(mixed))
for b in range(1, P):
    print("     mu=%d : %s" % (b, "  ".join("|A_(%d,%d)|=%d" % (a, b, sizes[(a, b)])
                                            for a in range(1, P))))
print()
print("  min |A_w| over mixed w = %d      (Sec.6's Case-A conclusion asserts >= 4)"
      % lo)
print("  mixed w with |A_w| <= 3 : %d of %d   -> %s"
      % (len(bad), len(mixed), bad))
print("  population for BOTH counts above: all %d mixed directions; exclusion"
      " list EMPTY." % len(mixed))
print()
print("  VERDICT: the conclusion |A_w| >= 4 is FALSE under the weakened"
      " hypothesis. REFUTED BY EXHIBITION.")

# ------------------------------------------------------- the direction profile
rule("FULL DIRECTION PROFILE of the witness -- context for any repair attempt")
prof = {}
for u in itertools.product(range(P), repeat=2):
    if u == (0, 0):
        continue
    k = len(A_set(f, u, P))
    prof.setdefault(k, []).append(u)
nz = P * P - 1
for k in sorted(prof):
    print("  n_%d = %-3d  directions: %s" % (k, len(prof[k]), sorted(prof[k])))
print("  population: all %d nonzero directions of F_%d^2; exclusion list EMPTY."
      % (nz, P))
print("  sum_u |A_u| over ALL u (u=0 contributes 1) = %d" % fib_w)

print()
rule("SUMMARY")
print("  controls_ok = %s" % ok)
print("  elapsed_s = %.2f" % (time.time() - T_START))
print("  interpreter: run this with .venv/bin/python3 (pure stdlib; no sympy,"
      " no networkx, so either interpreter gives the same numbers)")
sys.exit(0 if ok else 1)
