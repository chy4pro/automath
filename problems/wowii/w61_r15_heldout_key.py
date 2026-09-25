#!/usr/bin/env python3
"""Compute the FRESH held-out answer key for the round-15 (Q35) GFAN brief.

Why fresh: the round-14 key (`w61_r15_heldout_key.txt`'s predecessor
`w61_r14_heldout_key.txt`) is BURNED — the campaign ledger now prints H3 = 45 and
H4 = 3340 term by term, and the H1 step counts were recomputed in the open.  A held-out
that has been published is no longer held out.

All five new quantities sit at `nu = 8` or on explicit lists that appear nowhere in any
brief, and every one is determined by Appendix A.0 + Appendix C.1 of the brief alone.

Primitives are written here from the A.0 specification, not imported from any earlier
harness or from any engine's checker.  Self-calibration runs first: the routines are
made to reproduce data the draft already prints (residues of K2/Cn, the s0 survivor
column for nu <= 6, the boundary-pair counts 0,1,3,7,14,26, and S(nu) = 0,3,24,110,
397,1211) BEFORE any held-out value is computed.  A calibration failure aborts.

ONE product: `problems/wowii/w61_r15_heldout_key.txt`.
"""
import pathlib
import sys

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")

# --------------------------------------------------------------- primitives (A.0)


def hh_steps(multiset):
    """Havel-Hakimi run, A.0 semantics.

    Returns (steps, residue) where the run reached all-zeros, or (None, reason) if the
    run is 'not a step sequence' (head exceeds the entries left, or the block would
    drive an entry negative).
    """
    lst = sorted((int(x) for x in multiset), reverse=True)
    s = 0
    while True:
        lst = sorted(lst, reverse=True)
        if not lst or lst[0] == 0:
            return s, len(lst)
        head, rest = lst[0], lst[1:]
        if head > len(rest):
            return None, "head exceeds remaining entries"
        if any(v == 0 for v in rest[:head]):
            return None, "block would go negative"
        lst = [v - 1 for v in rest[:head]] + rest[head:]
        s += 1


def steps_or_abort(multiset):
    s, _ = hh_steps(multiset)
    return s


def s0(lam):
    """s0(lam) := steps([lam1]^{lam1+1} + lam), Appendix C.1 (C-2)."""
    w = max(lam)
    return steps_or_abort([w] * (w + 1) + list(lam))


def clears_in(L, lam):
    """Step count of the E = 0 row ([L]^{L+1} + lam); None if not a step sequence."""
    return steps_or_abort([L] * (L + 1) + list(lam))


def partitions(n, cap=None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def p(n):
    return sum(1 for _ in partitions(n))


def cycle_degrees(n):
    return [2] * n


# ------------------------------------------------------- calibration, runs FIRST
fail = []

# (i) residues the draft prints for K2 and C3..C9: 1,1,2,2,2,3,3,3
res_expect = {"K2": 1, "C3": 1, "C4": 2, "C5": 2, "C6": 2, "C7": 3, "C8": 3, "C9": 3}
res_got = {"K2": hh_steps([1, 1])[1]}
for n in range(3, 10):
    res_got[f"C{n}"] = hh_steps(cycle_degrees(n))[1]
if res_got != res_expect:
    fail.append(f"residue calibration {res_got} != {res_expect}")

# (ii) for nu <= 6 the ONLY partition of 2nu with s0(lam) = lam1 is the single part
for nu in range(1, 7):
    surv = [lam for lam in partitions(2 * nu) if s0(lam) == max(lam)]
    if surv != [(2 * nu,)]:
        fail.append(f"s0 survivor calibration nu={nu}: {surv}")
    if sum(1 for _ in partitions(2 * nu)) != p(2 * nu):
        fail.append(f"partition count nu={nu}")

# (iii) E = 0 boundary-pair counts 0,1,3,7,14,26 for nu = 1..6
bp = [sum(max(0, max(lam) - nu - 1) for lam in partitions(2 * nu)) for nu in range(1, 7)]
if bp != [0, 1, 3, 7, 14, 26]:
    fail.append(f"boundary-pair calibration {bp}")

# (iv) S(nu) = sum_{E=1}^{nu-1} (nu-E) p(E) p(2nu-E)  ->  0,3,24,110,397,1211
S = [sum((nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu)) for nu in range(1, 7)]
if S != [0, 3, 24, 110, 397, 1211]:
    fail.append(f"S(nu) calibration {S}")

# (v) the E = 0 boundary survivors the draft prints, recomputed
bs_expect = {2: [(3, (4,))], 3: [(5, (6,))], 4: [(5, (7, 1)), (7, (8,))],
             5: [(7, (9, 1)), (9, (10,))],
             6: [(7, (10, 1, 1)), (9, (11, 1)), (11, (12,))]}
for nu, expect in bs_expect.items():
    got = sorted((L, lam) for lam in partitions(2 * nu)
                 for L in range(nu + 1, max(lam)) if clears_in(L, lam) == L)
    if got != sorted(expect):
        fail.append(f"boundary survivors nu={nu}: {got} != {expect}")

if fail:
    print("CALIBRATION FAILED — no key written:")
    for f in fail:
        print("   ", f)
    sys.exit(1)

# ------------------------------------------------------------------ the held-outs
NU = 8

G1_LISTS = {
    "La = [3,3,2,2,2]": [3, 3, 2, 2, 2],
    "Lb = [4,4,3,3,2,2]": [4, 4, 3, 3, 2, 2],
    "Lc = [5,5,4,4,3,3,2,2]": [5, 5, 4, 4, 3, 3, 2, 2],
    "Ld = [6,6,6,6,6,6,6]": [6] * 7,
}
G1 = {}
for name, lst in G1_LISTS.items():
    s, r = hh_steps(lst)
    G1[name] = (s, r) if s is not None else ("ABORT", r)

G2_lam = (9, 5, 2)
G2 = s0(G2_lam)

G3 = sum(max(0, max(lam) - NU - 1) for lam in partitions(2 * NU))

G4 = sum((NU - E) * p(E) * p(2 * NU - E) for E in range(1, NU))

G5_L, G5_lam = 10, (12, 4)
G5 = clears_in(G5_L, G5_lam)

key = f"""Q35 HELD-OUT ANSWER KEY — owner-w61 round 15, 2026-08-22
Computed by problems/wowii/w61_r15_heldout_key.py, own primitives written from the
Appendix A.0 specification. Calibrated against printed draft data BEFORE computing any
held-out (residues K2/C3..C9; the s0 survivor column for nu<=6; boundary-pair counts
0,1,3,7,14,26; S(nu)=0,3,24,110,397,1211; every printed E=0 boundary survivor) — all
five calibrations PASSED.
This file is NOT part of any brief and must never be pasted into one.
The round-14 key is BURNED (the ledger prints H3=45 and H4=3340); none of its values
is reused here.

G1  step counts (head-deletions to all-zeros) and residue, for four explicit lists
    that appear in NO brief and in NO table:
"""
for name, (s, r) in G1.items():
    key += f"      {name:24s} -> steps = {s}, residue = {r}\n"
key += f"""    (the brief prints residues for K2/Cn only, and no step count for anything)

G2  s0({list(G2_lam)}) = {G2}          [lam |- {sum(G2_lam)} = 2*{sum(G2_lam)//2}, two nu beyond every printed table]

G3  E=0 boundary pairs at nu={NU} = {G3}      [continues 0,1,3,7,14,26,...; nu={NU}, not nu=7]

G4  S({NU}) = {G4}                          [continues 0,3,24,110,397,1211,...]

G5  (L,lam) = ({G5_L},{list(G5_lam)}) at nu={NU}: clears in {G5} steps, target L = {G5_L}
    -> answer {"YES" if G5 == G5_L else "NO"}, count {G5}

Grading: G1 is the discriminator — echo-proof (nothing to echo), trivially
hand-computable, four independent values so a lucky guess is negligible.
G3/G4 are hand-derivations of the kind Qwen-class judges have demonstrated.
G2/G5 require actually running the process on a list the brief never shows.
"""

out = ROOT / "problems/wowii/w61_r15_heldout_key.txt"
out.write_text(key)
print(f"wrote {out} ({len(key)} bytes) — 5 calibrations passed, 5 held-outs computed")
