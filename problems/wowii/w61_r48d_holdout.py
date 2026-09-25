#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r48d -- HELD-OUT CONFIRMATION, on code that shares nothing with r48/r48b/r48c.

The theorems of this round (THEOREM DOWN-SET, THEOREM CHAIN-STEP, (CHAIN), THEOREM R-CLOSED,
(DOM-MAJ)) were all developed and censused on populations built with `stepA` lifted from
w61_r29_c1audit.py.  This file re-tests their CONCLUSIONS on a LARGER population with an
implementation written from the definitions and sharing no line with any of them:

  * `hh` is a multiplicity-counter step (a Counter of part sizes; it never sorts a list and
    never indexes a partition);
  * `graphic` is Erdos-Gallai, not Havel-Hakimi;
  * `dom` compares conjugate prefix sums (c_m), not partial sums of the parts;
  * `mu` is read off the counter walk.

Nothing here is lifted, imported or exec'd from another file.  If the round's theorems are
right, every count below is 0 on a population strictly larger than the one they were built on.

sec 90: every block states the population it could have failed on, and each is paired with a
control that fires on the same population.  Interpreter .venv/bin/python3 (pure Python).
"""
import sys
import time
from collections import Counter

T0 = time.time()
LIMIT = 540.0
NMAX = 26
PARTIAL = False
FAIL = []
CTRL = []


def over():
    global PARTIAL
    if time.time() - T0 > LIMIT:
        PARTIAL = True
        return True
    return False


def bad(tag, detail):
    FAIL.append("%s  %s" % (tag, detail))
    print("   ** DEFECT %s  %s" % (tag, detail))


def ctrl(name, hits, must_fire=True):
    ok = (hits > 0) if must_fire else (hits == 0)
    CTRL.append((name, hits, ok))
    print("    [%s] %-80s hits=%d" % ("ok" if ok else "DEAD", name, hits))
    if not ok:
        bad("CONTROL-DEAD", name)


# ------------------------------------------------------------------ partitions as counters
def enumerate_parts(n):
    """partitions of n as tuples, largest part first."""
    def rec(rem, cap):
        if rem == 0:
            yield ()
            return
        top = cap if cap < rem else rem
        while top >= 1:
            for tail in rec(rem - top, top):
                yield (top,) + tail
            top -= 1
    return rec(n, n)


def hh(cnt):
    """ONE Havel-Hakimi step on a Counter {part size: multiplicity}.
    Returns a Counter, or the string 'STOP' when the step is not available."""
    live = [v for v in cnt if v > 0 and cnt[v] > 0]
    if not live:
        return Counter()
    d = max(live)
    c = Counter(cnt)
    c[d] -= 1
    if c[d] == 0:
        del c[d]
    avail = 0
    for v in c:
        if v > 0:
            avail += c[v]
    if avail < d:
        return "STOP"
    need = d
    out = Counter()
    for v in sorted([v for v in c if v > 0], reverse=True):
        take = c[v] if c[v] < need else need
        if take:
            out[v - 1] += take
            need -= take
        if c[v] - take:
            out[v] += c[v] - take
        if need == 0:
            for w in sorted([w for w in c if w > 0], reverse=True):
                if w < v:
                    out[w] += c[w]
            break
    for v in list(out):
        if v <= 0 or out[v] == 0:
            del out[v]
    return out


def walk(cnt):
    """the list of heads removed, or None if the walk stops early."""
    c = Counter(cnt)
    heads = []
    for _ in range(4 * NMAX + 8):
        live = [v for v in c if v > 0 and c[v] > 0]
        if not live:
            return heads
        heads.append(max(live))
        c = hh(c)
        if c == "STOP":
            return None
    return None


def graphic(t):
    """Erdos-Gallai.  No Havel-Hakimi anywhere in this function."""
    L = list(t)
    if sum(L) % 2:
        return False
    n = len(L)
    for k in range(1, n + 1):
        left = 0
        for i in range(k):
            left += L[i]
        right = k * (k - 1)
        for i in range(k, n):
            right += L[i] if L[i] < k else k
        if left > right:
            return False
    return True


def cvec(t, M):
    """c_m(X) = sum_i min(X_i, m), m = 0..M."""
    return tuple(sum((v if v < m else m) for v in t) for m in range(M + 1))


def dom(a, b, M):
    """a >= b in dominance, tested through the CONJUGATE (c_m(a) <= c_m(b)), for equal sums."""
    ca, cb = cvec(a, M), cvec(b, M)
    return all(x <= y for x, y in zip(ca, cb))


def tup(c):
    out = []
    for v in sorted([v for v in c if v > 0], reverse=True):
        out.extend([v] * c[v])
    return tuple(out)


print("=" * 100)
print("w61 r48d -- HELD-OUT re-test of the round's theorems on independent code, N <= %d."
      % NMAX)
print("=" * 100)

M = NMAX + 2
GR = {}
nall = 0
for N in range(1, NMAX + 1):
    if over():
        break
    for p in enumerate_parts(N):
        nall += 1
        if graphic(p):
            GR[p] = Counter(p)
print("\n[0] population: %d partitions of N <= %d ; GRAPHIC (Erdos-Gallai) : %d"
      % (nall, NMAX, len(GR)))
ctrl("CONTROL: the population contains non-graphic partitions", nall - len(GR))

# every graphic partition's HH walk must complete -- HH and Erdos-Gallai agree
MU = {}
disagree = 0
for p in GR:
    w = walk(GR[p])
    if w is None:
        disagree += 1
    else:
        MU[p] = tuple(w)
print("    graphic partitions whose HH walk does NOT complete : %d   (must be 0)" % disagree)
if disagree:
    bad("EG-HH", "%d" % disagree)
ng = 0
for N in range(1, NMAX + 1):
    if over():
        break
    for p in enumerate_parts(N):
        if p not in GR and walk(Counter(p)) is not None:
            ng += 1
print("    NON-graphic partitions whose HH walk DOES complete  : %d   (must be 0)" % ng)
if ng:
    bad("HH-EG", "%d" % ng)
ctrl("CONTROL: mu was computed for a non-empty set", len(MU))

# --------------------------------------------------------------- [1] THEOREM DOWN-SET again
print("\n[1] THEOREM DOWN-SET, re-tested: lam graphic, one unit moved DOWN => graphic.")
ds_t = ds_v = 0
for lam in GR:
    if over():
        break
    L = list(lam) + [0]
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] - 1 < L[j] + 1:
                continue
            mu = tuple(sorted([L[t] - (t == i) + (t == j) for t in range(len(L))],
                              reverse=True))
            mu = tuple(v for v in mu if v > 0)
            ds_t += 1
            if not graphic(mu):
                ds_v += 1
print("    instances %d ; NOT graphic %d" % (ds_t, ds_v))
if ds_v:
    bad("DOWN-SET", "%d" % ds_v)
ctrl("CONTROL: the down-set census is non-vacuous", ds_t)

# ------------------------------------------------ [2] (CHAIN) and (DOM-MAJ) on every pair
print("\n[2] (CHAIN) and (DOM-MAJ), re-tested on every equal-sum dominance pair of graphic")
print("    partitions.  The chain is rebuilt from scratch by the i*/j** rule.")


def chain_step(lam, mu):
    L = max(len(lam), len(mu)) + 1
    A = list(lam) + [0] * (L - len(lam))
    B = list(mu) + [0] * (L - len(mu))
    i = 0
    while A[i] == B[i]:
        i += 1
    istar = i
    while istar + 1 < L and A[istar + 1] == A[i]:
        istar += 1
    j = istar + 1
    while A[j] >= B[j]:
        j += 1
    jss = istar + 1
    while A[jss] != A[j]:
        jss += 1
    A[istar] -= 1
    A[jss] += 1
    return tuple(v for v in A if v > 0)


byN = {}
for p in GR:
    byN.setdefault(sum(p), []).append(p)
dm_t = dm_v = ch_t = ch_v = 0
ch_len = 0
dm_ex = ch_ex = None
for N in sorted(byN):
    if over():
        break
    lst = byN[N]
    for a in lst:
        for b in lst:
            if a == b or not dom(a, b, M):
                continue
            dm_t += 1
            if not dom(MU[a], MU[b], M):
                dm_v += 1
                if dm_ex is None:
                    dm_ex = (a, b, MU[a], MU[b])
            cur = a
            k = 0
            while cur != b and k <= N * N + 8:
                cur = chain_step(cur, b)
                k += 1
                ch_t += 1
                if cur not in GR:
                    ch_v += 1
                    if ch_ex is None:
                        ch_ex = (a, b, cur)
            if cur != b:
                ch_v += 1
                if ch_ex is None:
                    ch_ex = ("NOREACH", a, b)
            if k > ch_len:
                ch_len = k
print("    equal-sum dominance pairs of graphic partitions : %d" % dm_t)
print("    (DOM-MAJ)  mu(A) >= mu(B) FAILURES              : %d   e.g. %s" % (dm_v, dm_ex))
print("    (CHAIN)    chain elements built %d , longest chain %d edges, elements OUTSIDE the"
      " graphic set or chains that do not reach B : %d   e.g. %s" % (ch_t, ch_len, ch_v, ch_ex))
if dm_v:
    bad("DOM-MAJ", "%d %s" % (dm_v, dm_ex))
if ch_v:
    bad("CHAIN", "%d %s" % (ch_v, ch_ex))
ctrl("CONTROL: (DOM-MAJ) was tested on a non-empty population", dm_t)
ctrl("CONTROL: chains longer than one edge occur", 1 if ch_len > 1 else 0)
# ------------------------------------------------------- [2c] the corrupt control, run properly
cc_t = cc_v = 0
for N in sorted(byN):
    if over():
        break
    lst = byN[N]
    for a in lst:
        for b in lst:
            if a == b or dom(a, b, M) or dom(b, a, M):
                continue
            cc_t += 1
            if not dom(MU[a], MU[b], M) and not dom(MU[b], MU[a], M):
                cc_v += 1
print("    [2c] INCOMPARABLE equal-sum pairs of graphic partitions : %d ; of them whose mu's"
      " are also incomparable : %d" % (cc_t, cc_v))
ctrl("CORRUPT CONTROL: mu-dominance is a real conclusion -- incomparable inputs give "
     "incomparable mu's, so [2] is not measuring a tautology", cc_v)

# ------------------------------------------------------------- [3] THEOREM R-CLOSED again
print("\n[3] THEOREM R-CLOSED, re-tested.  R is rebuilt here from the c_m profile alone.")


def shape(a, b):
    ca, cb = cvec(a, M), cvec(b, M)
    p = [y - x for x, y in zip(ca, cb)]
    g = sum(b) - sum(a)
    if p[0] != 0:
        return None
    if g == 0:
        if a == b:
            return ("EQ",)
        one = [m for m in range(M + 1) if p[m] == 1]
        if set(p) <= {0, 1} and one and one[-1] - one[0] + 1 == len(one) and p[M] == 0:
            return ("T",)
        return None
    if g == 2 and set(p) <= {0, 1, 2} and p[M] == 2 and \
            all(p[m] <= p[m + 1] for m in range(M)):
        v1 = min(m for m in range(M + 1) if p[m] >= 1) - 1
        v2 = min(m for m in range(M + 1) if p[m] == 2) - 1
        return ("U", v1, v2)
    return None


def inR(a, b):
    s = shape(a, b)
    if s is None:
        return False
    if s[0] in ("EQ", "T"):
        return True
    d = a[0] if a else 0
    adp1 = a[d + 1] if d + 1 < len(a) else 0
    return s[2] <= d and s[1] <= adp1


NX = {}
for p in GR:
    n = hh(GR[p])
    NX[p] = tup(n) if n != "STOP" else None
NX[()] = ()
r_t = r_v = 0
r_ex = None
by2 = {}
for p in GR:
    by2.setdefault(sum(p), []).append(p)
for N in sorted(by2):
    if over():
        break
    for a in by2[N]:
        for b in by2.get(N, []) + by2.get(N + 2, []):
            if not inR(a, b):
                continue
            r_t += 1
            na, nb = NX[a], NX[b]
            if na is None or nb is None:
                bad("HELDOUT-ILLEGAL", "%s %s" % (a, b))
                continue
            if not inR(na, nb):
                r_v += 1
                if r_ex is None:
                    r_ex = (a, b, shape(a, b), na, nb, shape(na, nb))
print("    pairs in R : %d ; CLOSURE VIOLATIONS : %d   e.g. %s" % (r_t, r_v, r_ex))
if r_v:
    bad("R-CLOSED", "%d %s" % (r_v, r_ex))
ctrl("CONTROL: R is non-empty on the held-out population", r_t)

# ------------------------------------------------------------------------------- SUMMARY
print("\n" + "=" * 100)
ok = sum(1 for _, _, o in CTRL if o)
print("ELAPSED %.2f s / %.0f s internal limit ; PARTIAL=%s" % (time.time() - T0, LIMIT, PARTIAL))
print("CONTROLS %d/%d firing ; DEFECTS %d" % (ok, len(CTRL), len(FAIL)))
for f in FAIL:
    print("   DEFECT: %s" % f)
print("=" * 100)
sys.exit(1 if FAIL or PARTIAL else 0)
