#!/usr/bin/env python3
"""owner-w61 round 12 — make Theorem GFANnu's enumeration reproducible FROM THE TEXT.

Q25 defect D2: the nu=3..6 enumeration was referenced (script + .out) but not
embedded, so the judge could not reproduce the decisive "rows FAN-6' misses = none"
table.  This script re-runs the same finite check with FULL instrumentation and
prints exactly the data that has to sit in the draft:

  (A) E = 0, per nu: every partition lam of 2nu, with lam_1, s0(lam), survive?,
      and the FAN-6' certificate for each survivor.
  (B) E = 0 boundary rows nu+1 <= L < lam_1: every (L, lam) pair, survivors only.
  (C) E >= 1, per nu: shapes tested, and EVERY survivor (L, E, escape vector,
      lam) with its FAN-6' certificate.
  (D) zero-padding inertness check (the "zero-entry convention" the judge asked
      about) and the labelled/unlabelled statement.

Own code; the two primitives hh_steps/partitions are transcribed from
w61_r5_gfan2.py so the numbers are the SAME check, re-instrumented.
"""
from itertools import combinations_with_replacement


def hh_steps(mult):
    s = sorted([x for x in mult], reverse=True)
    steps = 0
    while s and s[0] > 0:
        d = s[0]
        rest = s[1:]
        if d > len(rest):
            return None
        head, tail = rest[:d], rest[d:]
        if any(x <= 0 for x in head):
            return None
        head = [x - 1 for x in head]
        s = sorted(head + tail, reverse=True)
        steps += 1
    return steps


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield []
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest


def escape_multisets(E, slots):
    out = set()
    for comb in combinations_with_replacement(range(E + 1), slots):
        if sum(comb) == E:
            out.add(tuple(sorted(comb, reverse=True)))
    return sorted(out)


def fan6prime(lam):
    """Lemma FAN-6': unique maximum w >= 1 with second-largest <= w-2."""
    if not lam:
        return False
    s = sorted(lam, reverse=True)
    w, sec = s[0], (s[1] if len(s) > 1 else 0)
    return w >= 1 and s.count(w) == 1 and sec <= w - 2


def cert(lam):
    s = sorted(lam, reverse=True)
    w = s[0]
    sec = s[1] if len(s) > 1 else 0
    return f"w={w}, 2nd={sec}, mult(w)={s.count(w)}, FAN-6'={'YES' if fan6prime(lam) else 'no'}"


NUMAX = 6
PAD = 3

print("=" * 78)
print("(D) ZERO-PADDING INERTNESS  — pad p in {0,1,2,3,4,8}, all shapes of nu<=4")
print("=" * 78)
bad = 0
tested = 0
for nu in range(1, 5):
    for lam in partitions(2 * nu):
        for L in range(1, 13):
            base = [L] * (L + 1) + lam
            vals = set()
            for p in (0, 1, 2, 3, 4, 8):
                vals.add(hh_steps(base + [0] * p))
            tested += 1
            if len(vals) != 1:
                bad += 1
                print("   PAD MISMATCH", nu, lam, L, vals)
print(f"   {tested} lists x 6 paddings: padding-dependent step counts = {bad}")
print("   => zero entries are INERT for hh_steps; the draft's [0,0,0] padding is")
print("      a convenience, not a modelling choice.")
print()

print("=" * 78)
print("(A) E = 0 : the L-independent criterion  s0(lam) = lam_1   (Lemma TAIL)")
print("    columns: lam | lam_1 | s0(lam) | verdict | FAN-6' certificate")
print("=" * 78)
e0_surv = {}
for nu in range(1, NUMAX + 1):
    print(f"--- nu = {nu} :  partitions of 2nu = {2 * nu}  "
          f"(p({2*nu}) = {len(list(partitions(2*nu)))})")
    surv = []
    for lam in partitions(2 * nu):
        l1 = lam[0]
        s0 = hh_steps([l1] * (l1 + 1) + lam + [0] * PAD)
        ok = (s0 == l1)
        if ok:
            surv.append(tuple(lam))
        print(f"    lam={str(tuple(lam)):<22} lam1={l1:<3} s0={str(s0):<5} "
              f"{'SURVIVES' if ok else 'dies    '}  {cert(lam) if ok else ''}")
    e0_surv[nu] = surv
    print(f"    => E=0 survivors for nu={nu}: {surv}")
    miss = [l for l in surv if not fan6prime(list(l))]
    print(f"    => survivors NOT killed by FAN-6': {miss or 'NONE'}")
print()

print("=" * 78)
print("(B) E = 0 boundary rows  nu+1 <= L < lam_1  (outside Lemma TAIL's range)")
print("=" * 78)
for nu in range(1, NUMAX + 1):
    rows = 0
    surv = []
    for L in range(nu + 1, 2 * nu + 1):
        for lam in partitions(2 * nu):
            if L >= lam[0]:
                continue
            rows += 1
            if hh_steps([L] * (L + 1) + lam + [0] * PAD) == L:
                surv.append((L, tuple(lam)))
    miss = [r for r in surv if not fan6prime(list(r[1]))]
    print(f"  nu={nu}: boundary pairs (L,lam) checked = {rows:<4} "
          f"survivors = {surv or 'NONE'}   not killed by FAN-6' = {miss or 'NONE'}")
print()

print("=" * 78)
print("(C) E >= 1 : finite by FAN-8' (L <= 2nu-E) and MB1 (L >= nu+1)")
print("    every survivor listed with its FAN-6' certificate")
print("=" * 78)
for nu in range(1, NUMAX + 1):
    tested = 0
    surv = []
    per_E = {}
    for E in range(1, 2 * nu + 1):
        for L in range(nu + 1, 2 * nu - E + 1):
            for ev in escape_multisets(E, L + 1):
                C = [L + e for e in ev]
                for lam in partitions(2 * nu - E):
                    tested += 1
                    per_E[E] = per_E.get(E, 0) + 1
                    if hh_steps(C + lam + [0] * PAD) == L:
                        surv.append((L, E, tuple(ev), tuple(lam)))
    miss = [r for r in surv if not fan6prime(list(r[3]))]
    print(f"--- nu = {nu}: shapes tested = {tested}   per-E split = "
          f"{ {k: v for k, v in sorted(per_E.items())} }")
    print(f"    survivors (clear in exactly L steps) = {len(surv)}")
    for r in surv:
        L, E, ev, lam = r
        C = tuple(L + e for e in ev)
        print(f"      L={L} E={E} e=({','.join(map(str, ev))}) C={C} "
              f"lam={lam}   {cert(lam)}")
    print(f"    survivors NOT killed by FAN-6' = {miss or 'NONE'}")
print()

print("=" * 78)
print("(E) SUMMARY TABLE (the one the draft prints)")
print("=" * 78)
print(" nu | E=0 surv | E=0 misses | E>=1 tested | E>=1 surv | E>=1 misses | verdict")
for nu in range(1, NUMAX + 1):
    s0l = e0_surv[nu]
    m0 = [l for l in s0l if not fan6prime(list(l))]
    tested = 0
    surv = []
    for E in range(1, 2 * nu + 1):
        for L in range(nu + 1, 2 * nu - E + 1):
            for ev in escape_multisets(E, L + 1):
                C = [L + e for e in ev]
                for lam in partitions(2 * nu - E):
                    tested += 1
                    if hh_steps(C + lam + [0] * PAD) == L:
                        surv.append((L, E, tuple(ev), tuple(lam)))
    m1 = [r for r in surv if not fan6prime(list(r[3]))]
    print(f" {nu:>2} | {str(s0l):<10} | {str(m0 or 'none'):<10} | {tested:>11} | "
          f"{len(surv):>9} | {str(m1 or 'none'):<11} | "
          f"{'ELIMINATED' if not m0 and not m1 else 'OPEN'}")
print()

print("=" * 78)
print("(F) E>=1 shape-count closed form check:  S(nu) = sum_{E=1}^{?} N(E,nu)")
print("=" * 78)


def p(n, cache={}):
    if n < 0:
        return 0
    if n in (0, 1):
        return 1
    if n in cache:
        return cache[n]
    cache[n] = len(list(partitions(n)))
    return cache[n]


for nu in range(1, NUMAX + 1):
    tot = 0
    for E in range(1, 2 * nu + 1):
        for L in range(nu + 1, 2 * nu - E + 1):
            tot += len(escape_multisets(E, L + 1)) * len(list(partitions(2 * nu - E)))
    print(f"  nu={nu}: S(nu) = {tot}")
print("done")
