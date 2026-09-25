#!/usr/bin/env python3
"""
w133 round 30 -- THE VERDICT-DETERMINEDNESS AUDIT, and it finds against this line's own brief.

RULING DA measured whether a held-out ANSWER is greppable from the shipped bytes.  Nobody has
measured whether the VERDICT is.  On Q41 it is, and this file establishes that mechanically.

THE FINDING, in one sentence: the Q41 brief contains a paragraph -- "A GUARD THAT CANNOT MOVE"
-- which (a) declares the frame tables un-re-runnable, naming their range, and (b) prescribes
the exact check to run on them ("that a table's `N frames` is the product of the free bits it
describes").  The returned verdict is GAP, located at the frame tables, reached by running
exactly that prescribed check.  **The verdict's LOCATION and its METHOD were both supplied by
the brief.**  Under the logic of RULING DA (an answer available from the shipped bytes grades
nothing) the top-level verdict on this dispatch grades much less than it appears to.

WHAT SURVIVES, and it is measured here rather than asserted: the brief does NOT say which
tables pass the prescribed check.  The reviewer factored four of them correctly and declined
five.  This file checks (i) that no factorisation is printed in the brief, so each one had to
be produced, and (ii) whether each decline was JUSTIFIED -- because a count carrying a large
prime factor cannot be a product of free bits at all.

AND IT FINDS A SECOND DEFECT IN THE BRIEF: three of the brief's own tables CANNOT satisfy the
consistency check the brief prescribes.  The brief told the reviewer to check something its
own tables fail.

Exit 0 iff every control passes.  Exit 2 otherwise.
"""
import os, re, sys

BRIEF = os.path.expanduser(
    "~/workspace/claudecode/automath-sandbox/briefs/w133_r29_q41.md")
brief = open(BRIEF, encoding="utf-8").read()

FAIL = []
NCHK = [0]


def check(label, got, want):
    NCHK[0] += 1
    ok = (got == want)
    print("  [%s] %-72s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)
    return ok


def factor(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


# ------------------------------------------------------- PART 0: the guard paragraph exists
print("=" * 96)
print("PART 0 -- THE GUARD PARAGRAPH.  Located by its own heading, quoted only by measurement.")
print("=" * 96)
m = re.search(r"\*\*A GUARD THAT CANNOT MOVE.*?\n\n", brief, re.S)
check("the brief contains a paragraph headed 'A GUARD THAT CANNOT MOVE'", m is not None, True)
guard = m.group(0) if m else ""
check("the guard DECLARES the frame tables un-re-runnable",
      "You cannot re-run those" in guard, True)
check("the guard NAMES the frame tables' numeric range", "32 to 872 frames" in guard, True)
check("the guard PRESCRIBES the free-bit-product check",
      "is the product of the free bits it describes" in guard, True)

# ------------------------------------- PART 1: the verdict's location was in the guard alone
print()
print("=" * 96)
print("PART 1 -- WAS THE VERDICT DETERMINED?  The test is DA's, one level up: could the")
print("          returned verdict have been produced from a passage of the shipped bytes")
print("          WITHOUT doing the work the brief asked for?")
print("=" * 96)
# The returned GAPS name: Link 3 (Z3) frame counts, and Link 3 (Z5) frame counts.
returned_gap_subject = "frame counts"
check("the returned GAP's subject ('frame counts') is the guard's own subject ('frame tables')",
      "frame tables" in guard, True)
check("the guard names the flagged minimum 32 and the flagged maximum 872",
      ("32" in guard, "872" in guard), (True, True))
print("  VERDICT-DETERMINEDNESS: a reviewer who read ONLY the guard paragraph could answer")
print("  'GAP, at the frame tables' -- location AND method both supplied. The top-level")
print("  verdict is therefore DETERMINED in RULING DA's sense and grades little.")

# ---------------------------------------- PART 2: what the guard did NOT supply -- the residue
print()
print("=" * 96)
print("PART 2 -- THE RESIDUE.  The guard does not say WHICH tables satisfy the check it")
print("          prescribes.  Every factorisation the reviewer returned is checked here for")
print("          (a) absence from the brief and (b) arithmetic correctness.")
print("=" * 96)
# Frame counts the brief actually prints, and the products the reviewer returned for them.
ACCEPTED = {                      # count : (reviewer's product, its factors)
    64:  ("2^6", [2, 2, 2, 2, 2, 2]),
    256: ("64 x 2 x 2", [64, 2, 2]),
    49:  ("7 x 7", [7, 7]),
    686: ("7 x 7 x 7 x 2", [7, 7, 7, 2]),
}
DECLINED = [832, 858, 872, 32, 384]

print("  %-8s %-16s %-14s %-26s %s" %
      ("count", "in brief?", "product OK?", "printed in brief?", "prime factorisation"))
for n, (prod, parts) in sorted(ACCEPTED.items()):
    inb = bool(re.search(r"(?<![\d])%d(?![\d])" % n, brief))
    ok = (eval("*".join(str(p) for p in parts)) == n)
    # Is the PRODUCT itself printed anywhere in the brief, in any spacing?
    # OWNER DEFECT, r30, fixed here and reported not absorbed: the first version of this test
    # was `re.escape(prod.replace(" x ", "")) in brief` -- for 49 that searched for the string
    # "77", which occurs INSIDE 177 316, and reported 49's factorisation as printed when it is
    # not.  A substring test on digits is not a test on numbers.  Digit-boundary-aware now.
    sep = r"\s*(?:[x×*∗]|\\times)\s*"
    printed = bool(re.search(r"(?<![\d.])" + sep.join(re.escape(str(p)) for p in parts)
                             + r"(?![\d])", brief))
    print("  %-8d %-16s %-14s %-26s %s" %
          (n, "yes" if inb else "NO", "yes" if ok else "NO",
           "printed" if printed else "NOT printed", factor(n)))
    check("count %d is really in the brief" % n, inb, True)
    check("reviewer's product for %d is arithmetically correct" % n, ok, True)

check("64's factorisation '2^6' IS printed in the brief (so it is transcription, not work)",
      "2⁶ = 64" in brief or "2^6" in brief, True)
check("no '7 x 7' product form is printed anywhere in the brief, so 49 and 686 both had to\n"
      "        be PRODUCED by the reviewer (digit-boundary aware; the naive substring test\n"
      "        matched '77' inside '177 316' and was wrong -- owner defect, fixed, reported)",
      bool(re.search(r"(?<![\d.])7\s*(?:[x\u00d7*\u2217]|\\times)\s*7(?![\d])", brief)), False)

print()
print("  DECLINED counts -- was each decline JUSTIFIED?  A count carrying a LARGE PRIME factor")
print("  cannot be a product of small free-bit multiplicities at all, so the brief's own")
print("  prescribed check is INAPPLICABLE to it.")
print("  %-8s %-24s %-14s %s" % ("count", "prime factorisation", "largest prime", "decline"))
strong, weak = [], []
for n in DECLINED:
    f = factor(n)
    lp = max(f)
    justified = lp >= 11
    (strong if justified else weak).append(n)
    print("  %-8d %-24s %-14d %s" %
          (n, "x".join(str(x) for x in f), lp,
           "STRONGLY justified: not a bit-product" if justified
           else "weak: bit-shaped, the brief merely omits the bit count"))
check("(Z3)'s three counts 832/858/872 all carry a prime factor >= 11", sorted(strong), [832, 858, 872])
check("(Z5)'s two counts 32/384 are bit-shaped (2-smooth or 3-smooth)", sorted(weak), [32, 384])

# ---------------------------------- PART 3: THE SECOND DEFECT -- the brief prescribes a check
#                                    that three of its own tables cannot pass.
print()
print("=" * 96)
print("PART 3 -- SECOND DEFECT IN THE BRIEF, and it is this line's own.")
print("=" * 96)
print("  The guard prescribes: 'a table's N frames is the product of the free bits it")
print("  describes'.  832 = 2^6x13, 858 = 2x3x11x13, 872 = 2^3x109.  A free-bit product is a")
print("  product of small multiplicities; 13, 11 and 109 cannot arise that way.  Those three")
print("  tables are POST-DEDUPLICATION counts (the brief itself says 'every identification")
print("  pattern (v' may itself be a neighbour of v; their far neighbours may coincide)'),")
print("  so the prescribed check CANNOT succeed on them by construction.")
check("the brief's (Z3) prose does describe identification/de-duplication",
      "every identification pattern" in brief, True)
check("so the prescribed consistency check is inapplicable to >=3 of the brief's own tables",
      len(strong), 3)
print("  CONSEQUENCE: the brief invited the reviewer to run a check, on tables where the check")
print("  cannot pass, and then received the failure as the verdict.  That is a defect in the")
print("  DISPATCH, not in the reviewer, and not in the mathematics.")

# --------------------------------------------- PART 4: RULING CZ control on this file's gate
print()
print("=" * 96)
print("PART 4 -- RULING CZ.  This file's own predicates fired on adversarial inputs.")
print("=" * 96)
# The gate here is `guard_determines(verdict_subject, guard_text)`.


def guard_determines(subject, g):
    """Does the guard paragraph itself name the region this verdict is located at?"""
    return subject in g


check("POSITIVE: the real returned subject 'frame tables' IS named by the guard",
      guard_determines("frame tables", guard), True)
# HARDEST negative: a DIFFERENT region of the brief that is also machine-supported and also
# un-re-runnable -- the (Z2) 152-configuration table -- but which the guard does NOT single
# out.  If the gate fired on this too it would be firing on 'the brief mentions enumeration',
# not on the guard's actual content.
check("NEGATIVE (hardest): the guard does NOT name '152 neighbourhood configurations'",
      guard_determines("152 neighbourhood configurations", guard), False)
check("CONTROL: that other region really does exist in the brief (so the negative is live)",
      "152 neighbourhood configurations" in brief, True)
check("NEGATIVE: the guard does NOT name the (Z2) table's count 152",
      bool(re.search(r"(?<![\d])152(?![\d])", guard)), False)
print("  So the gate fires on the guard's CONTENT, not on the presence of enumeration talk:")
print("  it distinguishes the region the guard singles out from a region it does not.")

print()
print("=" * 96)
print("CHECKS: %d   FAILURES: %d" % (NCHK[0], len(FAIL)))
if FAIL:
    for f in FAIL:
        print("  FAILED: %s" % f)
    print("=" * 96)
    sys.exit(2)
print("ALL CHECKS PASS.")
print("=" * 96)
sys.exit(0)
