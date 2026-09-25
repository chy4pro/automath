#!/usr/bin/env python3
"""owner-tdn round 4 -- THE COLUMN BOUND.  Target: prove sum|A_w| off the 2-carrying
line is >= the residual that round 3 could only MEASURE (the 62 at p=5).

STATUS OF THE MATHEMATICS THIS FILE TESTS
-----------------------------------------
This file does NOT search for a proof.  A proof is written out in the round-4 state
file section 16 and is reproduced in outline below; this file exists to give every one
of its steps a control that COULD FAIL, on populations that are stated, and to print
the numbers the proof predicts so that a prediction and a measurement can disagree.

INPUTS ALREADY IN HAND (round 3, PROVISIONAL, re-verified here from scratch)
    (I)  d_{u+v} f(x) = d_u f(x) + d_v f(x+u) + eps(u,v),  eps(u,v)_c = floor((u_c+v_c)/p)
    (II) d_{ku} f(x) = sum_{i<k} d_u f(x+iu) + gam(u,k),   gam(u,k)_c = floor(k u_c / p)
    definitions: c_u(x) = ([x+u]-[x]-[u])/p ;  d_u f(x) = f(x+u)-f(x)+c_u(x) ;
                 A_u(f) = { d_u f(x) } ;  |T_f - T_f| = 1 + sum_{u != 0} |A_u(f)|.

THE NEW STEP, AND IT IS ONE LINE: THE CURL IS IDENTICALLY ZERO.
    eps(u,v)_c = floor((u_c+v_c)/p) is SYMMETRIC in u and v.  Apply (I) twice, once as
    u+v and once as v+u:
        d_u f(x) + d_v f(x+u) + eps(u,v) = d_v f(x) + d_u f(x+v) + eps(v,u)
    and the eps terms cancel, leaving
        (VI)   d_v f(x+u) - d_v f(x)  =  d_u f(x+v) - d_u f(x)      for ALL u,v,x.
    E36 named "the curl cross-term K_{u,v}(x)" as its obstruction and E40 named the
    missing A_u <-> A_{ku} relation as its break point.  K is zero.  The whole of the
    round-4 argument is what (VI) does when one of the two directions carries only two
    values.

THE ARGUMENT (proved; this file is its instrument panel)
    Let u != 0 with |A_u| = 2, and let v be any direction NOT in <u>.
 1. |A_w| >= 2 for every w != 0.   [cycle identity sum_i d_w f(x+iw) = -w != 0 kills 1]
 2. A_u = {a, a+s}.  The cycle identity gives p*a + t(x)*s = -u with t(x) = number of
    1s of the labelling L on the u-orbit of x; p*a = 0, so t*s = -u.  Hence
    s = c*u with c = -t^{-1}, and t is the SAME for every orbit, 1 <= t <= p-1.
 3. Put beta = d_v f.  By (VI),  beta(x+u) - beta(x) = (L(x+v) - L(x)) * s  in <u>.
    So pi o beta is CONSTANT on each u-coset, where pi = quotient by <u>.
    Write h(n) = pi(beta) on the u-coset n.
 4. Cycle identity along v: sum_n beta(nv) = -v, so sum_n h(n) = pi(-v) != 0.  A
    constant h would sum to p*h = 0.  Therefore h is NON-CONSTANT and g := |im h| >= 2.
 5. By (I)+(II), for every k,  A_{ku+v} = K_k + { n~(y,k)*s + beta(y) : y },
    n~(y,k) = sum_{j=1..k} L(y - ju).  Since s is in <u>, pi(A_{ku+v}) = pi(K_k) + im h,
    so |A_{ku+v}| = sum over gamma in im h of |C_k(gamma)| >= g,  where C_k(gamma) is
    the set of <u>-coordinates of the part of the image lying over gamma.
 6. Fix gamma and pick ONE u-coset n0 with h(n0) = gamma.  On it, with W_n(i) the
    labelling word of coset n (base points z_n = n v, so z_{n+1} = z_n + v):
        phi_k(i) = c*n~_{n0}(i,k) + delta_{n0}(i)   satisfies
        phi_k(i+1) - phi_k(i) = c * ( W_{n0+1}(i) - W_{n0}(i-k) ).
    So |C_k(gamma)| >= |phi_k(F_p)| >= 2 UNLESS every step vanishes, i.e. unless
    W_{n0+1} = W_{n0} shifted by k.
 7. W_{n0} has length p (p prime) and weight t with 1 <= t <= p-1, so it is APERIODIC:
    its p rotations are distinct.  Hence AT MOST ONE k in F_p can be exceptional.
        ==>  sum_{k in F_p} |C_k(gamma)| >= 2p - 1.
 8. Summing over gamma:  S^(v) := sum_{k in F_p} |A_{ku+v}| >= g*(2p-1) >= 4p - 2.
 9. The p(p-1) directions off <u> partition into the p-1 columns {ku+mv : k in F_p},
    m = 1..p-1, so  S_off >= (p-1)(4p-2).
10. S_<u> = sum_{k!=0} |A_{ku}| >= 2(p-1) by step 1.
11. |T_f-T_f| = 1 + S_<u> + S_off >= 1 + 2(p-1) + (p-1)(4p-2) = 1 + 4p(p-1) = (2p-1)^2. []

    *** THEOREM (this round): if ANY direction u has |A_u| = 2 then the conjecture
        holds for f.  Every inequality above is tight simultaneously, which is why the
        chain lands on (2p-1)^2 EXACTLY and not above it. ***
    *** NOT PROVED, and stated so it cannot be misread: the branch |A_w| >= 3 for
        EVERY w.  There step 1 gives only 1 + 3(p^2-1) = 3p^2-2, which is short of
        (2p-1)^2 for every p >= 3.  Round 3's (V) split is 0/1/2 two-carrying lines;
        this round closes the 1 and 2 branches and leaves the 0 branch open. ***

CONTROLS THAT COULD FAIL (each one kills a specific step if the step is wrong)
    Q1  the curl (VI) at carry level, exhaustive over the whole carry space, 4 primes.
    Q2  the curl (VI) on real f, all x, all (u,v).
    Q3  |A_w| >= 2, and the cycle identity sum_i d_w f(x+iw) = -w.
    Q4  step 2: s = c*u, t constant over orbits, t*c = -1, 1 <= t <= p-1.
    Q5  step 3: beta(x+u)-beta(x) = (L(x+v)-L(x))*s exactly (a SET-free pointwise test).
    Q6  step 4: h well defined, sum_n h(n) = pi(-v), h non-constant, g >= 2 -- g spectrum
        REPORTED, not assumed.
    Q7  step 5: the PREDICTED SET A_{ku+v} = K_k + {n~ s + beta}, compared as sets.
    Q8  step 6/7: per (gamma, n0), sum_k |C_k| >= 2p-1, and #exceptional k <= 1, and the
        exceptional k is EXACTLY the shift with W_{n0+1} = shift_k W_{n0}.
    Q9  step 8: the column bound S^(v) >= 4p-2, min over the population REPORTED.
    Q10 step 11: |T_f-T_f| >= (2p-1)^2, min over the population REPORTED.
    Q11 aperiodicity: binary words of length p and weight 1..p-1 have p distinct
        rotations -- exhaustive at p = 3,5,7,11.
    Q12 an INDEPENDENT check of |T_f-T_f| computed literally in (Z/p^2 Z)^2 (stated
        subsample), sharing no code path with the A_w machinery.

POPULATIONS (all stated; nothing is sampled unless the word "subsample" appears)
    POP-A  the complete round-2/3 class at p=5:  A_e1 = {(0,0),(1,0)}, |A_e2| <= 3,
           re-enumerated here from scratch.  This is the population round 3's
           MEASURED 62 came from, so the theorem must reproduce its frontier.
    POP-B  f constructed to have |A_u| = 2 for a prescribed direction u, at
           p = 3,5,7,11 and for several u including non-axis u.  This population is
           NOT confined to one A-class and NOT confined to p=5; it is the answer to
           round 3's stated limit 2 ("verified at p=5 only, on ONE A-class").
    Neither population is claimed to be all f.  The THEOREM is claimed; the runs are
    controls on it.

Interpreter: .venv/bin/python3 (pure stdlib -- no sympy, no networkx).
Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r4_column.py
"""
import itertools
import sys
import time

T_START = time.time()
HARD_TIMEOUT_S = 900          # self-limit, PROTOCOL hard constraint 3
try:
    sys.stdout.reconfigure(line_buffering=True)
except AttributeError:
    pass

controls = {}


def record(name, ok, detail):
    controls[name] = bool(ok)
    print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", name, detail))


# ------------------------------------------------------------------ definitions
def carry(u, x, p):
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def add(a, b, p):
    return ((a[0] + b[0]) % p, (a[1] + b[1]) % p)


def sub(a, b, p):
    return ((a[0] - b[0]) % p, (a[1] - b[1]) % p)


def smul(k, a, p):
    return ((k * a[0]) % p, (k * a[1]) % p)


def d_u_pt(f, u, x, p):
    y = add(x, u, p)
    c = carry(u, x, p)
    return ((f[y][0] - f[x][0] + c[0]) % p, (f[y][1] - f[x][1] + c[1]) % p)


def A_set(f, u, p, pts):
    return frozenset(d_u_pt(f, u, x, p) for x in pts)


def eps_claim(u, v, p):
    return (((u[0] + v[0]) // p) % p, ((u[1] + v[1]) // p) % p)


def gam_claim(u, k, p):
    return (((k * u[0]) // p) % p, ((k * u[1]) // p) % p)


def inv(a, p):
    return pow(a, p - 2, p)


print("=" * 78)
print("TDN r4 -- THE COLUMN BOUND;  the curl is zero and it closes the 2-branch")
print("=" * 78)

# =============================================================== Q1
print("\n[1] Q1 -- the CURL is identically zero, at carry level, exhaustively.")
print("    Claim: c_v(x+u) - c_v(x) = c_u(x+v) - c_u(x)  for ALL u,v,x.")
print("    (this is (VI) with the f-terms cancelled; if it fails, (VI) fails)")
q1_viol = 0
q1_pop = 0
q1_primes = []
for p in (3, 5, 7, 11):
    q1_primes.append(p)
    pts = [(i, j) for i in range(p) for j in range(p)]
    for u in pts:
        for v in pts:
            for x in pts:
                lhs = sub(carry(v, add(x, u, p), p), carry(v, x, p), p)
                rhs = sub(carry(u, add(x, v, p), p), carry(u, x, p), p)
                q1_pop += 1
                if lhs != rhs:
                    q1_viol += 1
record("Q1", q1_viol == 0,
       "curl at carry level: %d violations / %d (x,u,v) triples, EXHAUSTIVE at primes %s; "
       "exclusion list EMPTY" % (q1_viol, q1_pop, q1_primes))

# also: eps symmetry, which is the entire reason the curl vanishes
q1b_viol = 0
q1b_pop = 0
for p in (3, 5, 7, 11):
    pts = [(i, j) for i in range(p) for j in range(p)]
    for u in pts:
        for v in pts:
            q1b_pop += 1
            if eps_claim(u, v, p) != eps_claim(v, u, p):
                q1b_viol += 1
record("Q1b", q1b_viol == 0,
       "eps(u,v) == eps(v,u): %d violations / %d (u,v) pairs, EXHAUSTIVE at primes %s"
       % (q1b_viol, q1b_pop, q1_primes))

# =============================================================== Q11
print("\n[2] Q11 -- aperiodicity: a binary word of prime length p and weight not 0 or p")
print("    has p DISTINCT rotations.  Step 7 of the argument is exactly this.")
q11_viol = 0
q11_pop = 0
for p in (3, 5, 7, 11):
    for bits in itertools.product((0, 1), repeat=p):
        w = sum(bits)
        if w == 0 or w == p:
            continue
        rots = set(tuple(bits[(i + r) % p] for i in range(p)) for r in range(p))
        q11_pop += 1
        if len(rots) != p:
            q11_viol += 1
record("Q11", q11_viol == 0,
       "%d words with non-trivial rotation stabiliser / %d binary words of length "
       "p in {3,5,7,11} with weight in 1..p-1; EXHAUSTIVE, exclusion list EMPTY"
       % (q11_viol, q11_pop))


# ------------------------------------------------- the analyser (the whole round)
class Fail(Exception):
    pass


def analyse(f, u, p, pts, stats, full_cycle=False):
    """Full round-4 analysis of one f at one 2-direction u.  Mutates `stats`.

    Every step of the printed argument is CHECKED here, not assumed.  Raises Fail
    only on an internal impossibility (|A_u| != 2), which the caller filters out.
    `full_cycle` sweeps every base point in the cycle identity (used on POP-B, whose
    size allows it); on POP-A one base point per (f,w) is used and the population is
    reported that way.
    """
    Au = sorted(A_set(f, u, p, pts))
    if len(Au) != 2:
        raise Fail("|A_u| != 2")
    a, b = Au[0], Au[1]
    s = sub(b, a, p)

    # ---- Q4: s = c*u, t constant across orbits, t*c = -1, 1 <= t <= p-1
    c = None
    if u[0] % p:
        c = (s[0] * inv(u[0], p)) % p
    else:
        c = (s[1] * inv(u[1], p)) % p
    if smul(c, u, p) != s:
        stats['q4_viol'] += 1
    L = {}
    for x in pts:
        L[x] = 0 if d_u_pt(f, u, x, p) == a else 1
    # orbit weights
    seen = set()
    orbits = []
    for x in pts:
        if x in seen:
            continue
        orb = []
        y = x
        for _ in range(p):
            orb.append(y)
            seen.add(y)
            y = add(y, u, p)
        orbits.append(orb)
    ts = set(sum(L[y] for y in orb) for orb in orbits)
    stats['q4_pop'] += 1
    if len(ts) != 1:
        stats['q4_viol'] += 1
        t = None
    else:
        t = ts.pop()
        if not (1 <= t <= p - 1) or (t * c) % p != (p - 1):
            stats['q4_viol'] += 1
    stats['t_hist'][t] = stats['t_hist'].get(t, 0) + 1

    # ---- Q3: cycle identity and |A_w| >= 2 over ALL nonzero w
    sizes = {}
    bases = pts if full_cycle else pts[:1]
    for w in pts:
        if w == (0, 0):
            continue
        sizes[w] = len(A_set(f, w, p, pts))
        stats['q3_pop'] += 1
        if sizes[w] < 2:
            stats['q3_viol'] += 1
        for x in bases:
            acc = (0, 0)
            y = x
            for _ in range(p):
                acc = add(acc, d_u_pt(f, w, y, p), p)
                y = add(y, w, p)
            if acc != smul(p - 1, w, p):
                stats['q3_viol'] += 1

    # window sums n~(y,k) = sum_{j=1..k} L(y - ju): they depend on the LABELLING only,
    # not on the column v, so they are computed ONCE per f.
    NT = {}
    for y in pts:
        row = [0] * p
        acc = 0
        z = y
        for k in range(1, p):
            z = sub(z, u, p)
            acc += L[z]
            row[k] = acc
        NT[y] = row

    # ---- lambda = the linear functional whose kernel is <u>
    def lam(z):
        return (u[1] * z[0] - u[0] * z[1]) % p
    # e with lam(e) = 1
    e_rep = None
    for z in pts:
        if lam(z) == 1:
            e_rep = z
            break

    # a direction v not in <u>; use all p-1 columns v = m * v0
    v0 = None
    for z in pts:
        if z != (0, 0) and lam(z) != 0:
            v0 = z
            break

    total = 1 + sum(sizes.values())
    S_line_u = sum(sizes[smul(k, u, p)] for k in range(1, p))
    stats['q10_pop'] += 1
    if total < (2 * p - 1) ** 2:
        stats['q10_viol'] += 1
    if stats['min_total'] is None or total < stats['min_total']:
        stats['min_total'] = total
    stats['SLu_hist'][S_line_u] = stats['SLu_hist'].get(S_line_u, 0) + 1

    S_off = 0
    for m in range(1, p):
        v = smul(m, v0, p)
        # ---- Q5: beta(x+u) - beta(x) = (L(x+v)-L(x)) * s
        beta = dict((x, d_u_pt(f, v, x, p)) for x in pts)
        for x in pts:
            stats['q5_pop'] += 1
            lhs = sub(beta[add(x, u, p)], beta[x], p)
            rhs = smul((L[add(x, v, p)] - L[x]) % p, s, p)
            if lhs != rhs:
                stats['q5_viol'] += 1

        # ---- Q6: h well defined on u-cosets, sum h = lam(-v), h non-constant
        # index cosets by n with base point z_n = n*v  (so z_{n+1} = z_n + v)
        zbase = [smul(n, v, p) for n in range(p)]
        if len(set(lam(z) for z in zbase)) != p:
            stats['q6_viol'] += 1          # v must meet every u-coset exactly once
        h = []
        for n in range(p):
            vals = set(lam(beta[add(zbase[n], smul(i, u, p), p)]) for i in range(p))
            stats['q6_pop'] += 1
            if len(vals) != 1:
                stats['q6_viol'] += 1
                h.append(None)
            else:
                h.append(vals.pop())
        if None not in h:
            if sum(h) % p != lam(smul(p - 1, v, p)):
                stats['q6_viol'] += 1
            if len(set(h)) < 2:
                stats['q6_viol'] += 1
        g = len(set(h))
        stats['g_hist'][g] = stats['g_hist'].get(g, 0) + 1

        # the point grid, words W_n(i) = L(z_n + i u), and delta
        pg = [[add(zbase[n], smul(i, u, p), p) for i in range(p)] for n in range(p)]
        W = [tuple(L[pg[n][i]] for i in range(p)) for n in range(p)]
        # delta_n(i): beta(z_n + i u) = h(n)*e_rep + delta * u
        delta = []
        for n in range(p):
            row = []
            for i in range(p):
                z = beta[pg[n][i]]
                d = sub(z, smul(h[n], e_rep, p), p)
                if u[0] % p:
                    th = (d[0] * inv(u[0], p)) % p
                else:
                    th = (d[1] * inv(u[1], p)) % p
                if smul(th, u, p) != d:
                    stats['q6_viol'] += 1
                row.append(th)
            delta.append(row)

        # ---- Q7 / Q8 / Q9: the columns
        S_col = 0
        # C_k(gamma) collected as sets of <u>-coordinates, and the predicted A set
        for k in range(p):
            w = add(smul(k, u, p), v, p)
            # predicted set
            Kk = add(add(smul(k, a, p), gam_claim(u, k, p), p),
                     eps_claim(smul(k, u, p), v, p), p)
            pred = set()
            per_gamma = {}
            for n in range(p):
                for i in range(p):
                    y = pg[n][i]
                    nt = NT[y][k]
                    val = add(add(smul(nt % p, s, p), beta[y], p), Kk, p)
                    pred.add(val)
                    per_gamma.setdefault(h[n], set()).add((c * nt + delta[n][i]) % p)
            got = set(A_set(f, w, p, pts))
            stats['q7_pop'] += 1
            if pred != got:
                stats['q7_viol'] += 1
            if sum(len(x) for x in per_gamma.values()) != len(got):
                stats['q7_viol'] += 1
            S_col += sizes[w]

        # per-coset budget (step 6/7), checked on EVERY n0, not just one
        for n0 in range(p):
            tot = 0
            exc = []
            for k in range(p):
                cs = set()
                for i in range(p):
                    cs.add((c * NT[pg[n0][i]][k] + delta[n0][i]) % p)
                tot += len(cs)
                if len(cs) == 1:
                    exc.append(k)
                # the predicted equivalence: |C_k| == 1 iff W_{n0+1} = shift_k W_{n0}
                shifted = tuple(W[n0][(i - k) % p] for i in range(p))
                is_shift = (W[(n0 + 1) % p] == shifted)
                stats['q8_pop'] += 1
                if (len(cs) == 1) != is_shift:
                    stats['q8_viol'] += 1
            if len(exc) > 1:
                stats['q8_viol'] += 1
            if tot < 2 * p - 1:
                stats['q8_viol'] += 1
            stats['percoset_min'] = tot if stats['percoset_min'] is None \
                else min(stats['percoset_min'], tot)

        stats['q9_pop'] += 1
        if S_col < 4 * p - 2:
            stats['q9_viol'] += 1
        stats['col_hist'][S_col] = stats['col_hist'].get(S_col, 0) + 1
        if stats['min_col'] is None or S_col < stats['min_col']:
            stats['min_col'] = S_col
        S_off += S_col

    stats['Soff_hist'][S_off] = stats['Soff_hist'].get(S_off, 0) + 1
    if stats['min_Soff'] is None or S_off < stats['min_Soff']:
        stats['min_Soff'] = S_off
    if S_off + S_line_u + 1 != total:
        stats['q9_viol'] += 1          # the partition into <u> + columns must be exact
    return total, S_line_u, S_off, sizes


def new_stats():
    return dict(q3_viol=0, q3_pop=0, q4_viol=0, q4_pop=0, q5_viol=0, q5_pop=0,
                q6_viol=0, q6_pop=0, q7_viol=0, q7_pop=0, q8_viol=0, q8_pop=0,
                q9_viol=0, q9_pop=0, q10_viol=0, q10_pop=0,
                t_hist={}, g_hist={}, col_hist={}, Soff_hist={}, SLu_hist={},
                min_total=None, min_col=None, min_Soff=None,
                percoset_min=None)


def merge_report(tag, st, p):
    print("    -- %s --" % tag)
    print("       t (orbit weight) spectrum      : %s" % dict(sorted(st['t_hist'].items())))
    print("       g = |im h| spectrum            : %s" % dict(sorted(st['g_hist'].items())))
    print("       S_<u> spectrum                 : %s" % dict(sorted(st['SLu_hist'].items())))
    print("       column sum S^(v) spectrum      : %s" % dict(sorted(st['col_hist'].items())))
    print("       min column sum                 : %s   (bound 4p-2 = %d)"
          % (st['min_col'], 4 * p - 2))
    print("       min per-coset budget sum_k|C_k|: %s   (bound 2p-1 = %d)"
          % (st['percoset_min'], 2 * p - 1))
    print("       min S_off                      : %s   (bound (p-1)(4p-2) = %d)"
          % (st['min_Soff'], (p - 1) * (4 * p - 2)))
    print("       min |T_f - T_f|                : %s   (box (2p-1)^2 = %d)"
          % (st['min_total'], (2 * p - 1) ** 2))


# =============================================================== POP-B
print("\n[3] POP-B -- f CONSTRUCTED to carry a 2-direction, at four primes and at")
print("    non-axis directions too.  Construction: choose the labelling L with every")
print("    u-orbit of weight t, set d_u f = a + L*s with s = -t^{-1} u, and integrate")
print("    along the orbit (consistent because sum_i c_u = -u).  This realises EXACTLY")
print("    the hypothesis |A_u| = 2 and nothing else, so it is a population of the")
print("    theorem's hypothesis rather than of one A-class.")


def make_2dir_f(p, u, t, a, seed):
    pts = [(i, j) for i in range(p) for j in range(p)]
    seen = set()
    orbits = []
    for x in pts:
        if x in seen:
            continue
        orb = []
        y = x
        for _ in range(p):
            orb.append(y)
            seen.add(y)
            y = add(y, u, p)
        orbits.append(orb)
    st = seed
    def rnd(n):
        nonlocal st
        st = (st * 1103515245 + 12345) % (2 ** 31)
        return st % n
    s = smul((-inv(t, p)) % p, u, p)
    L = {}
    for orb in orbits:
        pos = list(range(p))
        ones = set()
        while len(ones) < t:
            ones.add(pos[rnd(p)])
        for idx, y in enumerate(orb):
            L[y] = 1 if idx in ones else 0
    f = {}
    for orb in orbits:
        f[orb[0]] = (rnd(p), rnd(p))
        for idx in range(p - 1):
            y = orb[idx]
            f[orb[idx + 1]] = add(sub(add(f[y], add(a, smul(L[y], s, p), p), p),
                                      carry(u, y, p), p), (0, 0), p)
        # closure check
        yl = orb[p - 1]
        clos = sub(add(f[yl], add(a, smul(L[yl], s, p), p), p), carry(u, yl, p), p)
        if clos != f[orb[0]]:
            return None
    return f


PRIMES_B = (3, 5, 7, 11)
DIRS_B = {3: [(1, 0), (1, 1)],
          5: [(1, 0), (1, 1), (2, 1), (0, 1)],
          7: [(1, 0), (1, 1), (3, 2)],
          11: [(1, 0), (1, 3)]}
N_PER = {3: 40, 5: 20, 7: 4, 11: 1}

popB_stats = {}
popB_counts = {}
popB_closure_fail = 0
for p in PRIMES_B:
    st = new_stats()
    pts = [(i, j) for i in range(p) for j in range(p)]
    n_f = 0
    for u in DIRS_B[p]:
        for t in range(1, p):
            for rep in range(N_PER[p]):
                if time.time() - T_START > HARD_TIMEOUT_S:
                    break
                seed = 1000000 * p + 1000 * (u[0] * p + u[1]) + 10 * t + rep
                a = ((seed // 7) % p, (seed // 13) % p)
                f = make_2dir_f(p, u, t, a, seed)
                if f is None:
                    popB_closure_fail += 1
                    continue
                try:
                    analyse(f, u, p, pts, st, full_cycle=(p <= 7))
                    n_f += 1
                except Fail:
                    st['q4_viol'] += 1
    popB_stats[p] = st
    popB_counts[p] = n_f
    print("\n  p = %d : %d constructed f analysed, directions u = %s, all t in 1..%d"
          % (p, n_f, DIRS_B[p], p - 1))
    merge_report("POP-B p=%d" % p, st, p)

record("Q3", all(popB_stats[p]['q3_viol'] == 0 for p in PRIMES_B),
       "|A_w| >= 2 and cycle identity sum_i d_w f(x+iw) = -w : %d violations / %d "
       "(f,w) checks over POP-B; exclusion list EMPTY"
       % (sum(popB_stats[p]['q3_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q3_pop'] for p in PRIMES_B)))
record("Q4", all(popB_stats[p]['q4_viol'] == 0 for p in PRIMES_B),
       "s = c*u with t*c = -1 and t constant over u-orbits, 1 <= t <= p-1 : %d "
       "violations / %d f over POP-B"
       % (sum(popB_stats[p]['q4_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q4_pop'] for p in PRIMES_B)))
record("Q5", all(popB_stats[p]['q5_viol'] == 0 for p in PRIMES_B),
       "beta(x+u)-beta(x) = (L(x+v)-L(x))*s : %d violations / %d (f,v,x) pointwise "
       "checks over POP-B; ALL x, ALL p-1 columns, no sampling"
       % (sum(popB_stats[p]['q5_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q5_pop'] for p in PRIMES_B)))
record("Q6", all(popB_stats[p]['q6_viol'] == 0 for p in PRIMES_B),
       "h constant on u-cosets, sum_n h(n) = lam(-v), h non-constant (g >= 2) : %d "
       "violations / %d (f,v,coset) checks over POP-B"
       % (sum(popB_stats[p]['q6_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q6_pop'] for p in PRIMES_B)))
record("Q7", all(popB_stats[p]['q7_viol'] == 0 for p in PRIMES_B),
       "PREDICTED SET A_{ku+v} = K_k + {n~(y,k)s + beta(y)} compared AS SETS, and the "
       "coset split sums to |A_{ku+v}| : %d violations / %d (f,v,k) checks over POP-B"
       % (sum(popB_stats[p]['q7_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q7_pop'] for p in PRIMES_B)))
record("Q8", all(popB_stats[p]['q8_viol'] == 0 for p in PRIMES_B),
       "per-coset budget sum_k |C_k| >= 2p-1, at most ONE exceptional k, and "
       "|C_k| = 1 <=> W_{n0+1} = shift_k W_{n0} : %d violations / %d (f,v,n0,k) checks "
       "over POP-B; EVERY coset n0 checked, not one" %
       (sum(popB_stats[p]['q8_viol'] for p in PRIMES_B),
        sum(popB_stats[p]['q8_pop'] for p in PRIMES_B)))
record("Q9", all(popB_stats[p]['q9_viol'] == 0 for p in PRIMES_B),
       "column bound S^(v) >= 4p-2, and the partition 1 + S_<u> + S_off = |T_f-T_f| : "
       "%d violations / %d (f,column) checks over POP-B"
       % (sum(popB_stats[p]['q9_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q9_pop'] for p in PRIMES_B)))
record("Q10", all(popB_stats[p]['q10_viol'] == 0 for p in PRIMES_B),
       "|T_f-T_f| >= (2p-1)^2 whenever some |A_u| = 2 : %d violations / %d f over "
       "POP-B at p = 3,5,7,11; exclusion list EMPTY"
       % (sum(popB_stats[p]['q10_viol'] for p in PRIMES_B),
          sum(popB_stats[p]['q10_pop'] for p in PRIMES_B)))
print("\n  constructions rejected by their own closure check: %d" % popB_closure_fail)

# =============================================================== Q2 curl on real f
print("\n[4] Q2 -- the curl (VI) on REAL f, all x, all (u,v), p = 5 and 7.")
q2_viol = 0
q2_pop = 0
for p in (5, 7):
    pts = [(i, j) for i in range(p) for j in range(p)]
    fam = []
    stt = 7
    for _ in range(6):
        f = {}
        for x in pts:
            stt = (stt * 1103515245 + 12345) % (2 ** 31)
            aa = stt % p
            stt = (stt * 1103515245 + 12345) % (2 ** 31)
            bb = stt % p
            f[x] = (aa, bb)
        fam.append(f)
    for f in fam:
        for u in pts:
            if u == (0, 0):
                continue
            for v in pts:
                if v == (0, 0):
                    continue
                for x in pts:
                    q2_pop += 1
                    lhs = sub(d_u_pt(f, v, add(x, u, p), p), d_u_pt(f, v, x, p), p)
                    rhs = sub(d_u_pt(f, u, add(x, v, p), p), d_u_pt(f, u, x, p), p)
                    if lhs != rhs:
                        q2_viol += 1
record("Q2", q2_viol == 0,
       "d_v f(x+u)-d_v f(x) = d_u f(x+v)-d_u f(x) on real f : %d violations / %d "
       "(f,u,v,x) checks, 6 seeded f at each of p=5,7, ALL x, ALL nonzero u,v"
       % (q2_viol, q2_pop))

# =============================================================== POP-A
print("\n[5] POP-A -- the complete round-2/3 class at p=5, re-enumerated from scratch:")
print("    A_e1 = {(0,0),(1,0)}, |A_e2| <= 3.  Round 3 MEASURED a floor for S_m on this")
print("    class and could NOT prove it; the theorem now predicts that floor.  Every")
print("    bound below is computed from p by this run, never transcribed from round 3.")

P = 5
print("    predicted:  min S_off = (p-1)(4p-2) = %d ;  min column = 4p-2 = %d ;"
      % ((P - 1) * (4 * P - 2), 4 * P - 2))
print("                min per-coset budget = 2p-1 = %d ;  box (2p-1)^2 = %d"
      % (2 * P - 1, (2 * P - 1) ** 2))
PTS = [(i, j) for i in range(P) for j in range(P)]
NZ = [w for w in PTS if w != (0, 0)]
M = [[i - (1 if q < i else 0) for i in range(P)] for q in range(P)]
A_E1 = frozenset([(0, 0), (1, 0)])
E1, E2 = (1, 0), (0, 1)


def build(qs, betas):
    b = [(0, 0)] * P
    for j in range(P - 1):
        b[j + 1] = ((b[j][0] + betas[j][0]) % P, (b[j][1] + betas[j][1]) % P)
    f = {}
    for j in range(P):
        for i in range(P):
            f[(i, j)] = ((b[j][0] + M[qs[j]][i]) % P, b[j][1])
    return f


def literal_diffset(f, p, pts):
    n = p * p
    T = [((x[0] + p * f[x][0]) % n, (x[1] + p * f[x][1]) % n) for x in pts]
    return len(set((((aa[0] - bb[0]) % n), ((aa[1] - bb[1]) % n)) for aa in T for bb in T))


stA = new_stats()
n_norm = 0
k1_viol = 0
q12_viol = 0
q12_pop = 0
completeA = True
Sm_min = None
Se2_min = None
frontier = {}
fcount = {}

for qs in itertools.product(range(P), repeat=P):
    if time.time() - T_START > HARD_TIMEOUT_S:
        completeA = False
        break
    D, okq = [], True
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
                b4 = ((-(b0[0] + b1[0] + b2[0] + b3[0])) % P,
                      (-1 - (b0[1] + b1[1] + b2[1] + b3[1])) % P)
                U4 = U3 | cells(4, b4)
                if len(U4) > 3:
                    continue
                f = build(qs, [b0, b1, b2, b3, b4])
                a1 = A_set(f, E1, P, PTS)
                a2 = A_set(f, E2, P, PTS)
                if a1 != A_E1 or len(a2) > 3 or set(a2) != U4:
                    k1_viol += 1
                    continue
                n_norm += 1
                total, SLu, Soff, sizes = analyse(f, E1, P, PTS, stA)
                S_e2 = sum(sizes[smul(k, E2, P)] for k in range(1, P))
                S_m = Soff - S_e2
                if Sm_min is None or S_m < Sm_min:
                    Sm_min = S_m
                if Se2_min is None or S_e2 < Se2_min:
                    Se2_min = S_e2
                # NOTE: the count and the minimum are kept in SEPARATE accumulators.
                # The first draft of this block reset the counter every time a new
                # minimum arrived, which makes it "members seen since the last
                # improvement" -- a resetting recorder, not a population.  It
                # disagreed with section 12's histogram by 920, and section 12 was right.
                key = S_e2
                if key not in frontier or S_m < frontier[key]:
                    frontier[key] = S_m
                fcount[key] = fcount.get(key, 0) + 1
                if n_norm % 250 == 1:
                    q12_pop += 1
                    if literal_diffset(f, P, PTS) != total:
                        q12_viol += 1

print("\n    normal forms enumerated : %d      complete = %s" % (n_norm, completeA))
print("    K1 (rejected candidates, i.e. the filter's own exclusion list) : %d" % k1_viol)
merge_report("POP-A complete class p=5", stA, P)
print("       min S_m over the %d mixed directions      : %s" % ((P - 1) ** 2, Sm_min))
print("       min S_e2                                  : %s" % Se2_min)
print("       frontier  S_e2 -> min S_m                 : %s"
      % dict(sorted(frontier.items())))
print("       S_e2 bucket POPULATION (separate counter)  : %s   sum = %d"
      % (dict(sorted(fcount.items())), sum(fcount.values())))
record("Q12", q12_viol == 0,
       "|T_f-T_f| from the fibre sum vs computed LITERALLY in (Z/25Z)^2 (no shared "
       "code path) : %d violations / %d f -- SUBSAMPLE (every 250th normal form), "
       "stated as a subsample, not a census" % (q12_viol, q12_pop))
record("Q9A", stA['q9_viol'] == 0,
       "column bound S^(v) >= 4p-2 = 18 on POP-A : %d violations / %d (f,column) "
       "checks; min column = %s" % (stA['q9_viol'], stA['q9_pop'], stA['min_col']))
record("Q8A", stA['q8_viol'] == 0,
       "per-coset budget >= 2p-1 = 9 on POP-A : %d violations / %d (f,v,n0,k) checks; "
       "min per-coset budget = %s" % (stA['q8_viol'], stA['q8_pop'], stA['percoset_min']))
record("Q10A", stA['q10_viol'] == 0,
       "|T_f-T_f| >= 81 on POP-A : %d violations / %d normal forms; min total = %s"
       % (stA['q10_viol'], stA['q10_pop'], stA['min_total']))
record("Q7A", stA['q7_viol'] == 0,
       "PREDICTED SET equality on POP-A : %d violations / %d (f,v,k) checks"
       % (stA['q7_viol'], stA['q7_pop']))

# =============================================================== the open branch
print("\n[6] THE BRANCH THIS ROUND DOES **NOT** CLOSE, measured so it is not hidden.")
print("    If NO direction has |A_u| = 2 then step 1 alone gives only 1 + 3(p^2-1):")
for p in (3, 5, 7, 11):
    print("      p = %2d : all-|A_w|>=3 floor = %5d   box (2p-1)^2 = %5d   short by %4d"
          % (p, 1 + 3 * (p * p - 1), (2 * p - 1) ** 2,
             (2 * p - 1) ** 2 - (1 + 3 * (p * p - 1))))
print("    That branch is OPEN.  Nothing in this file addresses it.")

# =============================================================== verdict
elapsed = time.time() - T_START
print("\n" + "=" * 78)
ok = all(controls.values())
print("controls : %d  |  all PASS = %s" % (len(controls), ok))
print("failing  : %s" % [k for k, vv in controls.items() if not vv])
print("complete (POP-A enumeration) = %s" % completeA)
print("elapsed_s = %.2f" % elapsed)
print("=" * 78)
