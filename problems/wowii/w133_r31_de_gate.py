#!/usr/bin/env python3
"""
w133 round 31 -- ITEM 2: RULING DE AS A PRE-DISPATCH GATE.

    RULING DA asks whether the held-out ANSWER was reachable from the bytes we shipped.
    RULING DE asks whether the VERDICT was.  They are different failure modes and until
    r30 only one of them was gated.

    DE, operationally: before dispatch, assert that the brief does not supply BOTH
      (L) the LOCATION of the finding it is most likely to receive -- a site named AND
          declared unverifiable, which is what makes it the likely site -- and
      (M) the METHOD -- a check prescribed for that site.
    Where a guard that cannot travel HAS to be declared, L alone is permitted; the
    resulting finding is then recorded as UN-INDEPENDENT and does not count as engagement.

POSITIVE CONTROL, per RULING CZ: the real historical instance.  This line has a perfect
one -- its own r29 "A GUARD THAT CANNOT MOVE" paragraph, which shipped L and M together
and duly received back a GAP at exactly that location, found by exactly that method.
The dispatched bytes are on disk and are read here, not paraphrased from memory.

RULING CZ' -- THE GATE MUST FIRE ON THE FEATURE, NOT ON THE INSTANCE STRING.  Two things
are done about that, and neither is an assertion:
  * a DELIBERATELY-WRONG comparator (exact-substring against the historical paragraph) is
    run beside the real gate on every probe.  Where the naive one misses and the real one
    fires, the real one demonstrably read the feature;
  * the gate's coverage on PARAPHRASES is MEASURED AND PRINTED AS A FRACTION, not claimed.
    r30's DA-coverage lesson: an instrument reported as "clean" without a denominator is
    worth an unknown amount.  This one reports its denominator.

NEGATIVE CONTROLS, hardest form: the same paragraph with ONLY the prescribed-check clause
removed must come back LOCATION-ONLY, not DETERMINED -- otherwise the gate is firing on
"the brief admits an enumeration exists" rather than on the method.

No SAT.  Wall-clock self-limit 120 s, exit(2) on overrun -- never a silent `return`.
"""
import os, re, sys, time, unicodedata

T0 = time.time()
LIMIT = 120.0
def tick(tag):
    if time.time() - T0 > LIMIT:
        print("OVERRUN at %s" % tag)
        sys.exit(2)

FAIL = []
NCHECK = 0
def check(name, ok, detail=""):
    global NCHECK
    NCHECK += 1
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)

SANDBOX = os.path.expanduser("~/workspace/claudecode/automath-sandbox/briefs")
SHIPPED = os.path.join(SANDBOX, "w133_r29_q41.md")     # the DISPATCHED bytes, md5 8195c12d...
REBUILT = os.path.join(SANDBOX, "w133_r31_q41.md")     # this round's rebuild


# ============================================================================
# THE THREE FEATURE PREDICATES
# ============================================================================
def norm(t):
    """NFKC + casefold + unify the dash/quote/space zoo, so that an encoding difference
    is not mistaken for a content difference (RULING CG's blind spot, made explicit)."""
    t = unicodedata.normalize("NFKC", t).casefold()
    for a, b in [("—", "-"), ("–", "-"), ("‘", "'"), ("’", "'"),
                 ("“", '"'), ("”", '"'), (" ", " "), ("→", "->")]:
        t = t.replace(a, b)
    t = re.sub(r"[`*_>]+", " ", t)
    return re.sub(r"\s+", " ", t)


# (L1) the site is declared UNVERIFIABLE -- this is what makes it the LIKELY finding site
UNVERIFIABLE = [
    r"\b(cannot|can not|can't|could not|couldn't|unable to|no way to|impossible to)\s+"
    r"(\w+\s+){0,3}(re-?run|re-?generate|reproduce|reconstruct|repeat|re-?derive|re-?execute)",
    r"\bun(-?re-?runnable|reproducible|verifiable|checkable)\b",
    r"\bnot\s+(\w+\s+){0,2}(reproducible|re-?runnable|verifiable|checkable|re-?derivable)\b",
    r"\bdoes not pretend you can\b",
    r"\bbeyond (your|the reviewer'?s) reach\b",
    r"\btake (them|these|it) on trust\b",
]
# (L2) a SITE is named -- an address, a named object, or a printed population
SITE = [
    r"\(z\s?\d\)", r"\(s\s?\d\)", r"\(b'?\)", r"\bsection\s?\d", r"§\s?\d",
    r"\bframe tables?\b", r"\btables?\b", r"\bsweeps?\b", r"\benumerations?\b",
    r"\blink \d\b", r"\b\d[\d ,]{1,9}\s+(frames|regions|configurations)\b",
]
# (M) a CHECK is PRESCRIBED for it
METHOD = [
    r"\b(check|verify|confirm|test|audit)\b\s+(\w+\s+){0,3}\b(that|whether|them|these|it|for)\b",
    r"\bso that you (can|could|may)\b",
    r"\byou can at least\b",
    r"\be\.?g\.?\s+that\b",
    r"\bfor instance that\b",
    r"\bmake sure that\b",
    r"\bsatisf(y|ies)\s+\w*\s*the\s+\w*\s*(check|test|identity|relation)\b",
]

def _any(pats, t):
    return [p for p in pats if re.search(p, t)]

def de_features(block):
    t = norm(block)
    return {"unverifiable": _any(UNVERIFIABLE, t),
            "site": _any(SITE, t),
            "method": _any(METHOD, t)}

def de_verdict(block):
    f = de_features(block)
    L = bool(f["unverifiable"]) and bool(f["site"])
    M = bool(f["method"])
    if L and M:
        return "DETERMINED", f
    if L:
        return "LOCATION-ONLY", f
    if M:
        return "METHOD-ONLY", f
    return "CLEAN", f


def blocks_of(text):
    """A block = a paragraph together with any block-quote lines that follow it, since a
    withdrawal or a prescription written as a quoted aside belongs to the paragraph above."""
    out, cur = [], []
    for line in text.split("\n"):
        if line.strip() == "":
            if cur:
                out.append("\n".join(cur))
                cur = []
        else:
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    merged, i = [], 0
    while i < len(out):
        b = out[i]
        while i + 1 < len(out) and out[i + 1].lstrip().startswith(">"):
            b += "\n" + out[i + 1]
            i += 1
        merged.append(b)
        i += 1
    return merged


def gate_brief(path):
    text = open(path, encoding="utf-8").read()
    worst, hits = "CLEAN", []
    order = {"CLEAN": 0, "METHOD-ONLY": 1, "LOCATION-ONLY": 2, "DETERMINED": 3}
    for b in blocks_of(text):
        v, f = de_verdict(b)
        if order[v] >= 2:
            hits.append((v, b, f))
        if order[v] > order[worst]:
            worst = v
    return worst, hits


# the DELIBERATELY-WRONG comparator that runs beside the gate (RULING CZ')
HISTORICAL = None
def naive_comparator(block):
    """A whole-text comparator: 'is this the paragraph we already know about?'  It is WRONG
    on purpose.  Its job is to be run on the same probes so that the cases where it misses
    and the real gate fires are visible, which is what shows the gate reads the FEATURE."""
    return "DETERMINED" if norm(HISTORICAL)[:400] in norm(block) else "CLEAN"


# ============================================================================
def part0():
    print("\n=== PART 0 -- EVERY PREDICATE SHIPS AN INPUT ON WHICH IT MUST RETURN TRUE ===")
    check("MUST-FIRE unverifiable: 'You cannot re-run those'",
          bool(_any(UNVERIFIABLE, norm("You cannot re-run those."))))
    check("MUST-FIRE unverifiable: 'these counts are not reproducible here'",
          bool(_any(UNVERIFIABLE, norm("These counts are not reproducible here."))))
    check("specificity: a plain sentence with no unverifiability marker does NOT fire",
          not _any(UNVERIFIABLE, norm("The three links are supported by machine enumerations.")))
    check("MUST-FIRE site: 'frame tables of 32 to 872 frames'",
          bool(_any(SITE, norm("frame tables of 32 to 872 frames"))))
    check("MUST-FIRE site: an address '(Z3)'", bool(_any(SITE, norm("step (Z3) is where"))))
    check("specificity: a sentence naming no site does NOT fire",
          not _any(SITE, norm("Please answer in the format given below.")))
    check("MUST-FIRE method: 'check them for internal consistency'",
          bool(_any(METHOD, norm("check them for internal consistency"))))
    check("MUST-FIRE method: 'e.g. that a table's N frames is the product of the free bits'",
          bool(_any(METHOD, norm("e.g. that a table's `N frames` is the product of the free bits"))))
    check("specificity: 'say so - that is a legitimate finding' prescribes NO check",
          not _any(METHOD, norm("Where a conclusion rests only on a count you cannot "
                                "reproduce, say so - that is a legitimate finding.")))
    check("MUST-FIRE verdict: L and M together give DETERMINED",
          de_verdict("You cannot re-run the frame tables; check them for internal "
                     "consistency.")[0] == "DETERMINED")
    check("MUST-FIRE verdict: L alone gives LOCATION-ONLY",
          de_verdict("You cannot re-run the frame tables.")[0] == "LOCATION-ONLY")
    check("MUST-FIRE verdict: neither gives CLEAN",
          de_verdict("The hexagon Z is induced and C4-freeness is inherited.")[0] == "CLEAN")
    tick("part0")


def part1():
    print("\n=== PART 1 -- POSITIVE CONTROL ON THE REAL HISTORICAL INSTANCE (RULING CZ) ===")
    print("  The DISPATCHED bytes, read off disk: %s" % SHIPPED)
    global HISTORICAL
    text = open(SHIPPED, encoding="utf-8").read()
    guard = [b for b in blocks_of(text) if "GUARD THAT CANNOT MOVE" in b]
    check("the historical guard paragraph is present in the dispatched bytes, exactly once",
          len(guard) == 1, "%d blocks" % len(guard))
    HISTORICAL = guard[0]
    v, f = de_verdict(HISTORICAL)
    print("      verdict on the r29 guard paragraph: %s" % v)
    print("        unverifiable markers hit: %r" % f["unverifiable"])
    print("        site markers hit        : %r" % f["site"])
    print("        method markers hit      : %r" % f["method"])
    check("*** POSITIVE CONTROL: the gate returns DETERMINED on the real r29 guard "
          "paragraph -- the instance that actually determined a verdict", v == "DETERMINED")
    worst, hits = gate_brief(SHIPPED)
    print("      whole-brief verdict for the DISPATCHED r29 brief: %s (%d flagged blocks)"
          % (worst, len(hits)))
    check("and the whole dispatched brief is flagged DETERMINED, so the gate would have "
          "REFUSED that dispatch", worst == "DETERMINED")
    tick("part1")
    return HISTORICAL


def part2(hist):
    print("\n=== PART 2 -- RULING CZ': DOES IT READ THE FEATURE OR THE STRING? ===")
    print("  Five paraphrases, increasingly far from the original wording.  The naive")
    print("  whole-text comparator is run on each, beside the gate.  MEASURED, not claimed.")
    paraphrases = [
        # 1 -- synonym swap only
        "A guard that cannot travel, stated rather than concealed. The three links lean on "
        "machine enumerations - frame tables of 32 to 872 frames, and two sweeps. You cannot "
        "re-run those and this brief does not pretend you can. Their populations appear in "
        "the text below so that you can at least check them for internal consistency.",
        # 2 -- restructured, different verbs
        "Steps (Z3) and (Z5) rest on counts we are unable to reproduce for you here. We print "
        "the sizes anyway, so that you may verify that each size is the product of the binary "
        "choices described beside it.",
        # 3 -- passive, no imperative
        "The frame tables below are not reproducible from this document. Their populations are "
        "printed so that a reader can confirm that a table's size equals the product of its "
        "free bits.",
        # 4 -- the prescription hidden in an aside
        "Two sweeps and several enumerations underpin Link 3; it is impossible to re-run them "
        "from what is here. The counts are given (e.g. that 832 should factor as a power of "
        "two) purely for internal consistency.",
        # 5 -- no shared content word with the original except the addresses
        "Section 37's populations are beyond your reach: nothing here lets you re-derive them. "
        "They are listed so you can audit whether each equals the product of its binary "
        "degrees of freedom.",
    ]
    fired = naive_fired = 0
    for i, p in enumerate(paraphrases, 1):
        v, f = de_verdict(p)
        nv = naive_comparator(p)
        shared = max_ngram_overlap(hist, p, 6)
        print("      paraphrase %d: gate=%-14s naive=%-10s longest shared 6-gram: %s"
              % (i, v, nv, "yes" if shared else "NONE"))
        if v == "DETERMINED":
            fired += 1
        if nv == "DETERMINED":
            naive_fired += 1
    print("      COVERAGE, as a fraction and not as a pass: gate %d/5, naive comparator %d/5"
          % (fired, naive_fired))
    check("the gate fires on a MAJORITY of paraphrases (a number, not a pass): %d/5" % fired,
          fired >= 3, "%d/5" % fired)
    check("*** CZ' DISCHARGED BY CONSTRUCTION: the naive whole-text comparator fires on "
          "ZERO of them, so wherever the gate fired it read the FEATURE and not the "
          "instance string", naive_fired == 0, "naive %d/5" % naive_fired)
    print()
    print("  HARDEST-FORM NEGATIVE CONTROL: the SAME historical paragraph with ONLY the")
    print("  prescribed-check clause deleted -- everything else byte-identical.")
    stripped = hist.replace(
        ", deliberately, so that you can at least check them for internal\nconsistency "
        "(e.g. that a table's \"N frames\" is the product of the free bits it describes)", "")
    check("the deletion actually landed (the stripped block is shorter)",
          len(stripped) < len(hist), "%d -> %d chars" % (len(hist), len(stripped)))
    v2, f2 = de_verdict(stripped)
    print("      verdict with the method clause removed: %s (method markers %r)"
          % (v2, f2["method"]))
    check("*** NEGATIVE CONTROL: removing ONLY the method clause drops the verdict from "
          "DETERMINED to LOCATION-ONLY, so the gate is not firing on 'the brief admits "
          "an enumeration exists'", v2 == "LOCATION-ONLY")
    # and the converse: the site removed, the prescription kept
    v3, _ = de_verdict("You cannot reproduce these. Check that each figure is the product "
                       "of the choices described.")
    print("      verdict with a prescription but NO named site: %s" % v3)
    tick("part2")


def max_ngram_overlap(a, b, n):
    ta, tb = norm(a).split(), norm(b).split()
    A = {tuple(ta[i:i + n]) for i in range(len(ta) - n + 1)}
    B = {tuple(tb[i:i + n]) for i in range(len(tb) - n + 1)}
    return A & B


def part3():
    print("\n=== PART 3 -- THE GATE RUN ON THIS ROUND'S REBUILT BRIEF ===")
    if not os.path.exists(REBUILT):
        check("the rebuilt brief exists to be gated", False, REBUILT)
        return
    worst, hits = gate_brief(REBUILT)
    print("      whole-brief verdict for the r31 rebuild: %s (%d flagged blocks)"
          % (worst, len(hits)))
    for v, b, f in hits:
        first = b.strip().split("\n")[0][:96]
        print("        %-14s %s" % (v, first))
        print("          site=%d unverifiable=%d method=%d"
              % (len(f["site"]), len(f["unverifiable"]), len(f["method"])))
    check("*** the rebuilt brief is NOT DETERMINED: the withdrawal removed the METHOD "
          "while the declaration (which cannot travel, so must be declared) remains",
          worst != "DETERMINED", "verdict %s" % worst)
    print()
    print("  ENGAGEMENT LEDGER, the second half of RULING DE.  The guard is still")
    print("  LOCATION-ONLY, because a guard that cannot travel HAS to be declared.")
    print("  Consequence, recorded before dispatch rather than argued after it:")
    print("      * a returned finding LOCATED AT an enumeration is UN-INDEPENDENT and")
    print("        DOES NOT COUNT AS ENGAGEMENT;")
    print("      * a returned finding that names the METHOD as well DOES count, because")
    print("        no method is supplied by these bytes;")
    print("      * a finding anywhere else is scored normally.")
    tick("part3")


def part4():
    print("\n=== PART 4 -- WHAT THE GATE WOULD HAVE SAID ABOUT r30'S ACTUAL VERDICT ===")
    print("  The returned GAPs were: (Z3)'s frame counts 832/858/872, and (Z5)'s 32/384.")
    print("  Both sites were named in the guard; both were reached by the guard's own")
    print("  prescribed check.  Under DE both are UN-INDEPENDENT and neither counts as")
    print("  engagement.  What is NOT determined, and therefore still counts:")
    print("      * WHICH tables the reviewer declined and WHY -- the guard says nothing")
    print("        about that, and 49 = 7x7 / 686 = 7x7x7x2 are printed nowhere;")
    print("      * (P2)'s six-step re-derivation of (Z1), volunteered and not requested.")
    print("  And one thing the gate CANNOT decide, stated rather than assumed away:")
    print("      the (Z5) row's population in the shipped bytes was ITSELF WRONG (384 for")
    print("      768).  A reviewer reporting that row unreconstructible was reporting a")
    print("      true thing about a false number.  Determinedness and correctness are")
    print("      independent, and this gate measures only the first.")
    tick("part4")


HARVEST = os.path.expanduser(
    "~/workspace/claudecode/automath-sandbox/logs/w133_r30/q41_harvest.txt")

def part5():
    print("\n=== PART 5 -- THE (Z3)/(Z5) GAP, RE-GRADED ===")
    print("  The planner asked whether the returned GAP survives on its own merits once")
    print("  the unsatisfiable check is withdrawn.  It splits, and the two halves grade")
    print("  DIFFERENTLY.  The discriminator is not rhetoric, it is arithmetic:")
    print()
    print("      A reviewer executing ONLY the guard's prescribed check would have")
    print("      flagged exactly the populations that are NOT powers of two.")
    print("      %-22s %6s %-14s %-12s" % ("table", "N", "power of 2?", "prescribed check"))
    verdicts = {}
    for label, N in [("(Z3)/(Z4) 832", 832), ("(Z4) 858", 858), ("(Z4) 872", 872),
                     ("(Z5) one slot 32", 32), ("(Z5) two slots 384*", 384)]:
        pw = (N & (N - 1)) == 0
        verdicts[label] = pw
        print("      %-22s %6d %-14s %-12s"
              % (label, N, "yes" if pw else "NO", "PASSES" if pw else "flags it"))
    print("      * 384 is the number the SHIPPED bytes carried; the true population is 768")
    print("        (PART 4).  Either way it is not a power of two, so the prescribed check")
    print("        would have flagged it -- the independent content of the (Z5) bullet is")
    print("        specifically the 32 flag, not the 384 flag.")
    check("the prescribed check FLAGS 832/858/872 -- so the (Z3) half of the returned GAP "
          "is exactly what the shipped method produces",
          not any(verdicts[k] for k in ("(Z3)/(Z4) 832", "(Z4) 858", "(Z4) 872")))
    check("*** and the prescribed check PASSES (Z5)'s 32 (= 2^5) -- so the (Z5) half of "
          "the returned GAP CANNOT have come from the shipped method",
          verdicts["(Z5) one slot 32"] is True)
    print()
    print("  RIVAL EXPLANATION, tested rather than dismissed (OPS-15: a right answer from")
    print("  a constant looks the same in a log as a right answer from a measurement).")
    print("  Rival: 'the reviewer flagged everything in Link 3, so 32 tells us nothing.'")
    if not os.path.exists(HARVEST):
        check("the harvest text is on disk to test the rival explanation against", False, HARVEST)
        return
    h = open(HARVEST, encoding="utf-8").read()
    p3 = h.split("(P3)")[1].split("GAPS:")[0] if "(P3)" in h and "GAPS:" in h else ""
    gaps = h.split("GAPS:")[1] if "GAPS:" in h else ""
    passed_in_link3 = [tok for tok in ("802 853", "8 feasible") if tok in norm(p3) or tok in p3]
    print("      populations the reviewer PASSED inside Link 3: %r" % passed_in_link3)
    print("      populations the reviewer FLAGGED             : %s"
          % ", ".join(t for t in ("832", "858", "872", "32", "384") if t in gaps))
    check("the rival is FALSIFIED: the reviewer passed populations inside the SAME link "
          "it flagged, so the flag is per-table and not a blanket over Link 3",
          len(passed_in_link3) >= 1, "passed in Link 3: %r" % passed_in_link3)
    check("and 32 is flagged in the GAPS section although it passes the prescribed check",
          "32" in gaps and "(Z5)" in gaps)
    print()
    print("  RE-GRADE, stated as two separate verdicts:")
    print("    (Z3) HALF -- DETERMINED, and it does NOT survive as engagement.")
    print("        Location supplied (the guard names the frame tables and declares them")
    print("        un-re-runnable) AND method supplied (the prescribed product check).")
    print("        Its CLAIM is nonetheless TRUE: reconstructing 872 needs an 18-branch")
    print("        list with f_b in {1,2,4,6,9}, printed nowhere in the brief")
    print("        (w133_r31_frames.py).  True, un-independent, not engagement.")
    print("        Against the MATHEMATICS it is worth nothing: a second implementation")
    print("        reproduces 832/832/858/872/858/832 and survivors 0/0/0/2/0/0, so (Z3)")
    print("        and (Z4) stand as stated.")
    print("    (Z5) HALF -- SURVIVES, as a PARTIALLY INDEPENDENT finding.")
    print("        Location supplied (the guard's '32 to 872 frames' names the range);")
    print("        METHOD NOT SUPPLIED -- the prescribed check passes 32, so flagging it")
    print("        required a per-table reconstruction test the reviewer brought itself.")
    print("        Under DE's ledger a finding whose METHOD is not supplied counts.")
    print("        And it is worth more than the reviewer could know: the brief's 384 was")
    print("        WRONG (768).  The reviewer reported a true thing about a false number.")
    print("    NET: r30's verdict buys LESS than one independent finding and MORE than")
    print("    zero.  The honest ledger entry is ONE HALF-FINDING, at (Z5), and that is")
    print("    an upgrade on r30's accounting, which priced 32/384 as a WEAK decline.")
    tick("part5")


def main():
    print(__doc__)
    part0()
    hist = part1()
    part2(hist)
    part3()
    part4()
    part5()
    print("\n=== SUMMARY ===")
    print("  checks run: %d, failures: %d %s" % (NCHECK, len(FAIL), FAIL if FAIL else ""))
    print("  wall clock: %.2f s (self-limit %.0f s)" % (time.time() - T0, LIMIT))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
