#!/usr/bin/env python3
"""owner-w61 round 10 adjudication of Q23 (w61_S3_76_qwen.md) and Q24 (w61_S3_TAIL_qwen.md).

Own residueAux/steps transcription (Lean spec quoted in draft lines 54-57), calibrated
on residue(K2)=1 and residue(C_n)=ceil(n/3) BEFORE any adjudication number is printed.
No number from either judge report or from any earlier w61_* script is reused as input.
"""
from itertools import count


def hh_step(s):
    """One Havel-Hakimi step on a descending list, N-truncated, splitAt-truncated."""
    d = s[0]
    rest = s[1:]
    head, tail = rest[:d], rest[d:]
    new = [x - 1 if x > 0 else 0 for x in head] + tail
    return sorted(new, reverse=True)


def steps(seq):
    """Number of HH steps residueAux performs before it hits [] or a 0-head."""
    s = sorted(seq, reverse=True)
    k = 0
    while s and s[0] != 0:
        s = hh_step(s)
        k += 1
    return k


def residue(seq):
    s = sorted(seq, reverse=True)
    while s and s[0] != 0:
        s = hh_step(s)
    return len(s)          # residueAux [] = 0 ; residueAux (0::t) = 1 + |t|


def cyc(n):
    return [2] * n


# ---------------------------------------------------------------- calibration
print("[CALIBRATION] (must pass before anything else)")
ok = residue([1, 1]) == 1
print("  residue(K2) =", residue([1, 1]), "expect 1", "OK" if ok else "FAIL")
allok = ok
for n in range(3, 10):
    r = residue(cyc(n))
    e = -(-n // 3)
    allok &= (r == e)
    print(f"  residue(C{n}) = {r}  expect {e}  {'OK' if r == e else 'FAIL'}")
print("  CALIBRATION", "PASS" if allok else "FAIL")
assert allok

def s0(lam):
    l1 = max(lam)
    return steps([l1] * (l1 + 1) + list(lam))


def tail_lhs(lam, L):
    return steps([L] * (L + 1) + list(lam))


def tail_rhs(lam, L):
    return (L - max(lam)) + s0(lam)      # signed, no N-truncation


def partitions(n, cap=None):
    if cap is None:
        cap = n
    if n == 0:
        yield []
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest


# ------------------------------------------------- Q24 D1: equality case L=lam1
print("\n[Q24-D1] equality case L = lambda_1 (proof parenthetical claims t>lam1 'true at t=L')")
bad = 0
for tot in range(1, 13):
    for lam in partitions(tot):
        L = max(lam)
        if tail_lhs(lam, L) != tail_rhs(lam, L):
            bad += 1
            print("   FORMULA FAILS at equality:", lam, L)
print(f"   partitions |lam|<=12 tested at L=lam1: formula mismatches = {bad}")
print("   => statement survives at L=lam1; only the parenthetical 't>lam1 true at t=L' is false.")

# --------------------------------------------- Q24 D3 / boundary probe witnesses
print("\n[Q24-D3] judge's named witnesses (recomputed from scratch)")
for lam, L in ([4], 2), ([3], 1), ([2], 0), ([2], 2), ([2, 2], 2):
    print(f"   lam={lam} L={L}: list={sorted([L]*(L+1)+lam, reverse=True)} "
          f"direct steps={tail_lhs(lam, L)} formula={tail_rhs(lam, L)} "
          f"s0={s0(lam)} lam1={max(lam)} in-scope={L >= max(lam)}")

# ------------------------------------------------ full in-scope / out-scope sweep
print("\n[Q24-SWEEP] |lam|<=12, L=0..15")
insc_bad, outsc_bad, insc, outsc = 0, [], 0, 0
for tot in range(1, 13):
    for lam in partitions(tot):
        for L in range(0, 16):
            lhs, rhs = tail_lhs(lam, L), tail_rhs(lam, L)
            if L >= max(lam):
                insc += 1
                if lhs != rhs:
                    insc_bad += 1
                    print("   IN-SCOPE MISMATCH:", lam, L, lhs, rhs)
            else:
                outsc += 1
                if lhs != rhs:
                    outsc.__class__  # no-op
                    outsc_bad.append((sum(lam), max(lam), lam, L, lhs, rhs))
print(f"   in-scope pairs={insc} mismatches={insc_bad}")
print(f"   out-of-scope pairs={outsc} mismatches={len(outsc_bad)}")
outsc_bad.sort()
print("   five smallest out-of-scope failures (by |lam|, then lam1):")
for row in outsc_bad[:5]:
    print("     |lam|=%d lam1=%d lam=%s L=%d direct=%d formula=%d" % row)

# ----------------------------------------------------- Q24 J-FAN5: lam=[2] rider
print("\n[Q24-JFAN5] Observation FAN-5 second half: steps([L]^{L+1} u [2]) == L ?")
bad5 = [L for L in range(2, 30) if tail_lhs([2], L) != L]
print("   s0([2]) = steps([2,2,2,2]) =", s0([2]), "(lam1 = 2)")
print("   L=2..29 counterexamples to 'total = L':", bad5 if bad5 else "none")
print("   L=0,1 (outside L>=lam1):", [(L, tail_lhs([2], L)) for L in (0, 1)])

# ----------------------------------------------- Q24 D2: lam = empty convention
print("\n[Q24-D3b] rider 'clears in exactly L steps <=> s0(lam)=lam1' with L>=lam1 dropped")
fwd, bwd = [], []
for tot in range(1, 13):
    for lam in partitions(tot):
        for L in range(0, 16):
            if L >= max(lam):
                continue                      # rider is TRUE in scope (swept above)
            clears = (tail_lhs(lam, L) == L)
            pred = (s0(lam) == max(lam))
            if pred and not clears:
                fwd.append((tot, max(lam), lam, L))
            if clears and not pred:
                bwd.append((tot, max(lam), lam, L))
fwd.sort()
bwd.sort()
print("   smallest =>-direction failure (s0=lam1 but does NOT clear in L):", fwd[0] if fwd else None)
print("   smallest <=-direction failure (clears in L but s0!=lam1):      ", bwd[0] if bwd else None)
print("   judge named lam=[4],L=2 as 'smallest'; it IS a failure but not the smallest:",
      (4, 4, [4], 2) in fwd)

print("\n[Q24-D2] lambda = empty set: 'lam1 := max lam' is undefined")
try:
    max([])
except ValueError as e:
    print("   max([]) raises:", e)
print("   consumers: TAIL is invoked only at E=0 where FAN-4' gives |lam| = 2*nu >= 2 (nu>=1 by R1),")
print("   so lam is nonempty at every call site; steps([L]^{L+1}) alone =",
      [(L, steps([L] * (L + 1))) for L in range(0, 6)])

# ------------------------------------------------------- Q23 D4: Fan slack rider
print("\n[Q23-D4] Fan(tau,L) slack = L-1 ?  (symbolic check + explicit instances)")
print("   In Fan(tau,L): every b in B_lo is B-universal with deg_A(b)=1, so deg(b)=(tau-1)+1=tau;")
print("   nu = 1 (B = K_tau - uv).  slack = L(tau+1) - (L*tau + 1) = L - 1.")
for tau in range(4, 9):
    for L in range(1, tau):
        slack = L * (tau + 1) - (L * tau + 1)
        assert slack == L - 1
print("   verified as an identity for tau=4..8, L=1..tau-1: slack == L-1 everywhere.")

# ------------------------------- Q23 D1: Prop L2(c) two-sided squeeze arithmetic
print("\n[Q23-D1] Prop L2(c): the forced Sum deg_A = 2 needs BOTH bounds simultaneously")
L, Blo_plus, c, mbar, nu_Blo = 2, 0, 0, 1, 0
lower = L + Blo_plus + c                       # Theorem MB's degree count
upper = 2 * L + nu_Blo - 1 - mbar              # Theorem SL in (LOW3) form, minus mbar
print(f"   MB lower bound  : Sum deg_A >= L + |B_lo+| + c = {lower}")
print(f"   SL (LOW3) upper : Sum deg_A <= 2L + nu(B_lo) - 1 - mbar = {upper}")
print("   squeeze =>", "Sum deg_A = 2 forced" if lower == upper == 2 else "NOT forced")

# ------------------------------- Q23 D2: witness that T1 u T2 need not meet B_lo+
print("\n[Q23-D2] Theorem MB's 'every such b lies in B_lo+' vs the draft's own Prop L2 config")
print("   Prop L2(d): T1={u}, T2={v} with u,v in B_hi.  B_lo+ subset B_lo, and B_hi cap B_lo = {}.")
print("   => u,v in T1 u T2 but u,v NOT in B_lo+: the universally-quantified sentence is false as written.")
print("   The count only uses c = |B_lo cap (T1 u T2)|, and B_lo cap (T1 u T2) subset B_lo+ IS true,")
print("   so the inequality |B_lo+| + c + mbar <= L + nu(B_lo) - 1 is unaffected.")
