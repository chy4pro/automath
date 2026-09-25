#!/usr/bin/env python3
"""owner-w61 round 5 — the GFan(tau,L,nu) endgame step count.

At the start of step p+1 of a GFan(tau,L,nu) run under the reductio, the list is
  C-part   : L+1 entries, the c-th equal to  L + e_c,  sum of e_c = E   (escapes)
  A'-part  : any partition of  2*nu - E                                 (FAN-4')
  plus zeros.
The reductio needs the process to terminate in EXACTLY L further steps
(total s = p + L = tau).  This script computes, for each shape, how many further
Havel-Hakimi steps it actually takes, and reports which shapes survive.

Constraint from FAN-8':  E >= 1  forces  L <= 2*nu - E.

Own code, written this round; reuses nothing.
"""
from itertools import combinations_with_replacement


def hh_steps(mult):
    """number of Havel-Hakimi deletion steps until the list is all zeros;
    returns None if the list is not realizable as a step sequence
    (a step would drive an entry negative)."""
    s = sorted([x for x in mult], reverse=True)
    steps = 0
    while s and s[0] > 0:
        d = s[0]
        rest = s[1:]
        if d > len(rest):
            return None          # head exceeds the number of remaining entries
        head, tail = rest[:d], rest[d:]
        if any(x <= 0 for x in head):
            return None          # would drive a zero entry negative
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
    """multisets of e_c >= 0 over `slots` C-vertices summing to E"""
    out = set()
    for comb in combinations_with_replacement(range(E + 1), slots):
        if sum(comb) == E:
            out.add(tuple(sorted(comb, reverse=True)))
    return sorted(out)


def scan(nu, Lrange, napr_max=6, verbose=True):
    survivors = []
    total = 0
    for L in Lrange:
        for E in range(0, 2 * nu + 1):
            if E >= 1 and L > 2 * nu - E:
                continue                      # excluded by Lemma FAN-8'
            resid = 2 * nu - E
            if resid < 0:
                continue
            for evec in escape_multisets(E, L + 1):
                Cpart = [L + e for e in evec]
                for pa in partitions(resid):
                    if len(pa) > napr_max:
                        continue
                    # pad with zero A' entries (they exist whenever |A'| > len(pa));
                    # zeros never change the step count, so one padding is enough
                    for pad in (0, 3):
                        mult = Cpart + pa + [0] * pad
                        st = hh_steps(mult)
                        total += 1
                        if st == L:
                            survivors.append((L, E, tuple(Cpart), tuple(pa), pad, st))
                        if pad == 0 and st is None:
                            pass
    if verbose:
        print(f"nu={nu}: shapes tested={total}, shapes clearing in exactly L steps:")
        seen = set()
        for row in survivors:
            key = (row[0], row[1], row[2], row[3])
            if key in seen:
                continue
            seen.add(key)
            print(f"   L={row[0]} E={row[1]} C={row[2]} A'={row[3]}  -> steps={row[5]}")
        if not survivors:
            print("   NONE")
    return survivors


if __name__ == '__main__':
    print("=== nu = 1 (Theorem FAN's family) — control: expect only the single-2 residue")
    scan(1, range(2, 10))
    print()
    print("=== nu = 2 (the GFan(tau,L,2) layer, the L>=3 target)")
    s2 = scan(2, range(3, 12))
    print()
    print("=== nu = 3 (LEAD check)")
    scan(3, range(3, 12))
    print()
    print("=== nu = 2, singleton-residue check: which survivors have a NON-single-part A'?")
    bad = [r for r in s2 if len(r[3]) > 1]
    print("   multi-part survivors:", sorted(set((r[0], r[1], r[2], r[3]) for r in bad)) or "NONE")
    print("done")


# ---------------------------------------------------------------- round 5, late
# Lemma TAIL + the complete finite check for a fixed nu.
#
#   Lemma TAIL. For E = 0 the C-part is [L]^{L+1}. While the common C-value t
#   exceeds lam_1 the head is a C-entry and the block is exactly the other
#   C-entries, so after L - lam_1 steps the list is [lam_1]^{lam_1+1} together
#   with lam, untouched.  Hence, for L >= lam_1,
#         steps = (L - lam_1) + s0(lam),  s0(lam) := steps([lam_1]^{lam_1+1} + lam),
#   so "clears in exactly L steps" <=> s0(lam) = lam_1, a condition on lam ALONE.
#
# With FAN-4' (residue total 2nu - E), FAN-8' (E >= 1 => L <= 2nu - E) and
# Corollary MB1 (L >= nu + 1), the whole GFan(tau,L,nu) family is therefore a
# FINITE check for each fixed nu.  fan6prime() is Lemma FAN-6'.

def fan6prime(lam):
    """Lemma FAN-6' applies: unique maximum w >= 1 with second-largest <= w-2."""
    if not lam:
        return False
    s = sorted(lam, reverse=True)
    w, sec = s[0], (s[1] if len(s) > 1 else 0)
    return w >= 1 and s.count(w) == 1 and sec <= w - 2


def tail_check(nu, verbose=True):
    """E = 0: Lemma TAIL's L-independent criterion, plus the boundary L < lam_1."""
    open_rows = []
    for lam in partitions(2 * nu):
        l1 = lam[0]
        s0 = hh_steps([l1] * (l1 + 1) + lam + [0, 0, 0])
        if s0 == l1 and not fan6prime(lam):
            open_rows.append(('TAIL', None, tuple(lam)))
        if verbose:
            print(f"   E=0 lam={tuple(lam)} lam1={l1} s0={s0} "
                  f"{'SURVIVES' if s0 == l1 else 'dies'}"
                  f"{' [FAN-6prime]' if s0 == l1 and fan6prime(lam) else ''}")
    for L in range(nu + 1, 2 * nu + 1):          # boundary rows with L < lam_1
        for lam in partitions(2 * nu):
            if L >= lam[0]:
                continue
            if hh_steps([L] * (L + 1) + lam + [0, 0, 0]) == L and not fan6prime(lam):
                open_rows.append(('boundary', L, tuple(lam)))
    return open_rows


def escape_check(nu, verbose=False):
    """E >= 1: finitely many (L, E) by FAN-8' (L <= 2nu-E) and MB1 (L >= nu+1)."""
    open_rows, tested = [], 0
    for E in range(1, 2 * nu + 1):
        for L in range(nu + 1, 2 * nu - E + 1):
            for ev in escape_multisets(E, L + 1):
                C = [L + e for e in ev]
                for lam in partitions(2 * nu - E):
                    tested += 1
                    if hh_steps(C + lam + [0, 0, 0]) == L:
                        if not fan6prime(lam):
                            open_rows.append((L, E, tuple(C), tuple(lam)))
                        elif verbose:
                            print(f"   L={L} E={E} C={tuple(C)} lam={tuple(lam)} "
                                  f"[FAN-6prime]")
    return open_rows, tested


def complete_check(numax=5):
    print("=== COMPLETE finite check of GFan(tau,L,nu) for nu = 1..%d ===" % numax)
    for nu in range(1, numax + 1):
        o1 = tail_check(nu, verbose=False)
        o2, tested = escape_check(nu)
        print(f" nu={nu}: E=0 rows not killed by FAN-6' : {o1 or 'NONE'}")
        print(f"        E>=1 shapes tested={tested}, rows not killed by FAN-6': "
              f"{o2 or 'NONE'}")
        print(f"        => GFan(tau,L,{nu}) with L >= {nu+1}: "
              f"{'ELIMINATED' if not o1 and not o2 else 'OPEN ROWS ABOVE'}")


def tail_crosscheck(numax=5, Lmax=15):
    """Lemma TAIL vs direct simulation."""
    bad = n = 0
    for nu in range(1, numax + 1):
        for lam in partitions(2 * nu):
            l1 = lam[0]
            s0 = hh_steps([l1] * (l1 + 1) + lam + [0, 0, 0])
            for L in range(l1, Lmax):
                direct = hh_steps([L] * (L + 1) + lam + [0, 0, 0])
                pred = (L - l1) + s0 if s0 is not None else None
                n += 1
                if direct != pred:
                    bad += 1
                    print("   TAIL MISMATCH", nu, lam, L, direct, pred)
    print(f"=== Lemma TAIL cross-check: {n} (lam,L) pairs, mismatches = {bad}")
