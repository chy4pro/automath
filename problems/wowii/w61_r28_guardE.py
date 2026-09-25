#!/usr/bin/env python3
"""
owner-w61 round 28, task item 2 -- GUARD E: DOES THE BRIEF'S TRANSCRIPTION MATCH
THE SOURCE?

THE GAP THIS CLOSES, stated by me in SS7.41 (g) before a judge said it:

    "GUARD B proves that a STATEMENT BLOCK EXISTS for each covered name.  It does
     not prove the statement is CORRECT, or that it matches the draft, or that it
     is the version the proof actually uses.  Seven statements were transcribed
     into A.1 by hand and no guard checks them against SS7.5 / SS7.6 / SS7.2."

    "The brief no longer lies about what it contains"  is NOT
    "the brief's imports are right."

GUARD E is the second half.  It is MECHANICAL: it never reads for meaning, it
matches math atoms between the shipped brief and the draft that is their source.

TWO DIRECTIONS, and the second one is the dangerous one:
  * FORWARD  (brief -> source): every math atom the brief prints under a name must
    occur in that name's source block.  Catches an ALTERED or INVENTED clause.
  * REVERSE  (source -> brief): every math atom the SOURCE block prints must occur
    in the brief's transcription.  Catches a DROPPED HYPOTHESIS -- which is the
    AB2/AE1 species, i.e. the one that has actually cost this line rounds.
A one-directional check would pass a transcription that silently drops "tau >= 2".

NORMALISATION IS DECLARED, NOT HIDDEN.  The draft is Unicode (and SS7.2 is in
Chinese); the brief is ASCII.  A transform table is REQUIRED to compare them at
all.  Every entry of it is printed below before any grading.  A transform is not
a narrowing: it maps both sides through the same function.  What is FORBIDDEN
here, under RULING CE, is adding a transform in order to silence a specific
mismatch -- so the table is fixed before the run, printed, and every surviving
mismatch is adjudicated by NAME with a REASON, never by widening the table.

RULING AS: the POPULATION is printed before the verdict.
RULING CD: this guard's liveness is DEMONSTRATED against deliberately corrupted
transcriptions, not asserted.  A printed 'PASS' from a guard nobody has seen fail
is the same evidence as a printed Output: block.

ONE PRODUCT: w61_r28_guardE.out.
"""

import re
import sys

BRIEF = "prompts/w61_S3_GFAN_r28.md"
DRAFT = "notes/proofs/wowii61_draft.md"

# ===================================================== THE DECLARED TRANSFORM TABLE
# Fixed before the run.  Printed.  Applied to BOTH sides.
TRANSFORMS = [
    ("τ", "tau"), ("α", "alpha"), ("ν", "nu"), ("Δ", "Delta"),
    ("Σ", "sum"), ("∑", "sum"), ("δ", "delta"), ("λ", "lambda"),
    ("≤", "<="), ("≥", ">="), ("≠", "!="), ("−", "-"),
    ("≡", "=="), ("∈", " in "), ("∉", " notin "),
    ("∪", " u "), ("∩", " cap "), ("∅", "empty"),
    ("⁺", "+"), ("⁰", "^0"), ("¹", "^1"), ("²", "^2"),
    ("₀", "_0"), ("₁", "_1"), ("₂", "_2"), ("₃", "_3"),
    ("m̄", "mbar"), ("¯", "bar"),
    ("′", "'"), ("’", "'"), ("‘", "'"), ("—", "-"), ("–", "-"),
    (" ", " "), (" ", " "),
    ("\\", ""), ("`", ""), ("*", ""), ("$", ""),
]
# 'deg v' and 'deg(v)' are the SAME atom in this document; likewise 'C(tau,2)' spacing.
SPACE_INSENSITIVE = True


def norm(s):
    for a, b in TRANSFORMS:
        s = s.replace(a, b)
    s = s.replace("̄", "bar")
    return s


def key(s):
    """comparison key: normalised, space-stripped, case-folded."""
    return re.sub(r"\s+", "", norm(s)).lower()


REL = ("<=", ">=", "!=", "=", "|-")
WORDY = re.compile(r"^[A-Za-z][A-Za-z ]*$")


PROSE_TOKENS = 3   # the CLASS rule, not a word list


def is_prose(t):
    """DEFECT E-3 root fix.  A math run that carries three or more whitespace-
    delimited PURELY-ALPHABETIC tokens is prose, not an atom.  This is a CLASS
    test (RULING S): it names no word.  Without it the extractor admitted the
    whole line '> Theorem K. Assume residue(G) = alpha(G) (so s = tau) and that
    every has' as an 'atom' -- the checker generating its own false alarms."""
    return sum(1 for w in t.split() if w.isalpha()) >= PROSE_TOKENS


def atoms(block, excluded=None):
    """math atoms of a block: every backticked span, every BOLD span carrying a
    relational operator (the draft bolds its displays instead of quoting them),
    plus every maximal math run that carries a relational operator and is not
    prose by the class rule above."""
    out = []
    for m in re.finditer(r"`([^`]+)`", block):
        out.append(m.group(1).strip())
    for m in re.finditer(r"\*\*([^*]+)\*\*", block):
        t = m.group(1).strip()
        if any(r in norm(t) for r in REL):
            out.append(t)
    stripped = re.sub(r"`[^`]*`", " ", block)
    stripped = re.sub(r"\*\*[^*]+\*\*", " ", stripped)
    stripped = norm(stripped)
    for m in re.finditer(r"[A-Za-z0-9_^{}()\[\]|+\-*/=<>,.:!'̄ ]{4,}", stripped):
        t = m.group(0).strip()
        if any(r in t for r in REL) and not WORDY.match(t):
            if is_prose(t):
                if excluded is not None:
                    excluded.append(t)
                continue
            out.append(t)
    # DEFECT E-4, caught on the second run: a BOLD span that wraps a backticked
    # display plus its sentence period ('**`...− 1`.**') was captured WITH the
    # period, so the same inequality read as both MATCHED and DROPPED.  Sentence
    # punctuation is not part of a math atom.  Class rule, printed, no word list.
    out = [a.strip().rstrip(".,;:").strip() for a in out]
    seen, uniq = set(), []
    for a in out:
        k = key(a)
        if len(k) >= 3 and k not in seen:
            seen.add(k)
            uniq.append(a)
    return uniq


# ============================================= THE SEVEN, AND THEIR SOURCE ANCHORS
# The seven names SS7.41 records as hand-transcribed into A.1 this round.  Each
# source is located by ANCHOR TEXT, not by line number, and the located line is
# printed so the location itself is reviewable.
SEVEN = [
    ("Lemma S", "> **Lemma S (survivor degree bound).**",
     "> **Lemma S（生存者度界）.**", "SS7.2 B"),
    ("Lemma Z+", "> **Lemma Z+ (block occupancy).**",
     "> **Lemma Z⁺ (block occupancy, sharpened", "SS7.5"),
    ("Lemma F3'", "> **Lemma F3' (survivor decay, general",
     "> **Lemma F3′ (survivor decay, general", "SS7.5 Repair R2"),
    ("Theorem K", "> **Theorem K.** Assume `residue(G)",
     "> **Theorem K.** Assume residue(G)", "SS7.5"),
    ("Theorem MB", "> **Theorem MB (master budget).** **In the hard core**",
     "> **Theorem MB (master budget).** In the hard core", "SS7.6"),
    ("Theorem SL", "> **Theorem SL (slack positivity).** Assume `residue(G)",
     "> **Theorem SL (slack positivity).** Assume the reductio hypothesis", "SS7.6 F"),
    ("Favaron-Maheo-Sacle", "> **Favaron-Maheo-Sacle.**",
     "**Fact 2 (Favaron–Mahéo–Saclé 1991", "SS7.1 Fact 2"),
]

# DEFECT E-2, caught on the first run: the block terminator treated a BLANK QUOTE
# line ('>' alone) as the end of the statement.  Theorem SL's statement has two of
# them between its displayed formulas, so the block was cut to two lines and all
# three of SL's displays were reported as 'matched elsewhere'.  Direction of error:
# AGAINST ourselves (false alarm), like SS7.40's comma-stripping defect.  Root fix:
# a block ends at the PROOF marker or at the first line that leaves the quote, and
# a blank quote line is inside it.
STOP = re.compile(r"^\s*>?\s*\*?\*?Proof|^\s*>?\s*\*?\*?证|^\s*>?\s*\[证|^\s*$")
def in_quote(ln):
    return ln.lstrip().startswith(">")


def block_at(text, anchor, maxlines=14):
    i = text.find(anchor)
    if i < 0:
        return None, None
    line_no = text[:i].count("\n") + 1
    lines = text[i:].split("\n")
    out = [lines[0]]
    for ln in lines[1:maxlines]:
        if STOP.match(ln) or (out[0].lstrip().startswith(">") and not in_quote(ln)):
            break
        out.append(ln)
    return "\n".join(out), line_no


def where(draft_text, k):
    """the draft line at which a normalised atom first occurs -- so that every
    'matched elsewhere' adjudication names a place a reviewer can open."""
    lines = draft_text.split("\n")
    acc = 0
    for i, ln in enumerate(lines, 1):
        acc2 = acc + len(re.sub(r"\s+", "", norm(ln)).lower())
        if k in re.sub(r"\s+", "", norm("\n".join(lines[max(0, i - 3):i + 2]))).lower():
            return i
        acc = acc2
    return -1


def run(brief_text, draft_text, label, verbose=True):
    P = []
    def emit(s=""):
        P.append(s)

    emit("=" * 78)
    emit("GUARD E RUN: %s" % label)
    emit("=" * 78)
    emit("-- declared transform table (%d entries), applied to BOTH sides --" % len(TRANSFORMS))
    emit("   " + "  ".join("%r->%r" % (a, b) for a, b in TRANSFORMS[:10]))
    emit("   " + "  ".join("%r->%r" % (a, b) for a, b in TRANSFORMS[10:22]))
    emit("   " + "  ".join("%r->%r" % (a, b) for a, b in TRANSFORMS[22:]))
    emit("   plus: whitespace-insensitive comparison, case-folded.")
    emit("")

    draft_key = key(draft_text)
    findings = {"NO-MATCH": [], "ELSEWHERE": [], "MATCH": []}
    rows = []

    for name, banchor, danchor, sec in SEVEN:
        bblk, bln = block_at(brief_text, banchor)
        dblk, dln = block_at(draft_text, danchor)
        emit("-" * 78)
        if bblk is None:
            emit("[%s] BRIEF BLOCK NOT FOUND at anchor -- GUARD E cannot grade it" % name)
            findings["NO-MATCH"].append((name, "<brief block missing>", "anchor not found"))
            continue
        if dblk is None:
            emit("[%s] SOURCE BLOCK NOT FOUND in %s -- GUARD E cannot grade it" % (name, sec))
            findings["NO-MATCH"].append((name, "<source block missing>", "anchor not found"))
            continue
        emit("[%s]  brief line %d   <-->   source %s, draft line %d" % (name, bln, sec, dln))
        dkey = key(dblk)
        bkey = key(bblk)

        exb, exd = [], []
        ba, da = atoms(bblk, exb), atoms(dblk, exd)
        emit("   POPULATION: %d brief atoms, %d source atoms  (printed in full before the verdict)"
             % (len(ba), len(da)))
        for t in exb + exd:
            emit("     ---  EXCLUDED AS PROSE by the class rule (>=%d alphabetic tokens): %s"
                 % (PROSE_TOKENS, t[:96]))
        for a in ba:
            k = key(a)
            if k in dkey:
                st = "MATCH-IN-BLOCK"
                findings["MATCH"].append((name, a))
            elif k in draft_key:
                st = "MATCH-ELSEWHERE-IN-DRAFT (draft line %d)" % where(draft_text, k)
                findings["ELSEWHERE"].append((name, a, where(draft_text, k)))
            else:
                st = "*** NO MATCH ***"
                findings["NO-MATCH"].append((name, a, "brief->source"))
            emit("     FWD  %-24s %s" % (st, a))
            rows.append((name, "FWD", st, a))
        for a in da:
            k = key(a)
            if k in bkey:
                st = "MATCH-IN-BRIEF"
                findings["MATCH"].append((name, a))
            else:
                st = "*** DROPPED FROM BRIEF ***"
                findings["NO-MATCH"].append((name, a, "source->brief"))
            emit("     REV  %-24s %s" % (st, a))
            rows.append((name, "REV", st, a))

    emit("-" * 78)
    emit("VERDICT for %s" % label)
    emit("   atoms matched in block : %d" % len(findings["MATCH"]))
    emit("   atoms matched ELSEWHERE in the draft (adjudication list, below) : %d"
         % len(findings["ELSEWHERE"]))
    emit("   atoms with NO MATCH ANYWHERE : %d   <== these are DEFECTS" % len(findings["NO-MATCH"]))
    for f in findings["NO-MATCH"]:
        emit("      DEFECT  [%s]  %s   (%s)" % (f[0], f[1], f[2] if len(f) > 2 else ""))
    emit("")
    return "\n".join(P), findings, rows


def main():
    brief = open(BRIEF).read()
    draft = open(DRAFT).read()
    log = []

    rep, findings, rows = run(brief, draft, "REBUILT BRIEF %s (NOT YET SENT -- the bench is empty)" % BRIEF)
    log.append(rep)

    # ---------------------------------------------- LIVENESS: corrupt on purpose
    # Three corruptions, one per failure species.  The guard is shown FAILING;
    # a guard nobody has seen fail is an assertion, not evidence (RULING CD).
    corruptions = [
        ("C1 ALTERED CONSTANT (the AZ species)",
         "`|B_lo+| + c + mbar <= L + nu(B_lo) - 1`",
         "`|B_lo+| + c + mbar <= L + nu(B_lo) + 1`"),
        ("C2 DROPPED HYPOTHESIS (the AB2/AE1 species -- the dangerous direction)",
         "> **and** `tau >= 2`. If `L >= 1` then",
         "> If `L >= 1` then"),
        ("C3 WEAKENED RIDER (a plausible-looking edit)",
         "> `b in B` **has** `deg(b) >= tau + 1`.",
         "> `b in B` **has** `deg(b) >= tau`."),
    ]
    live = []
    for tag, old, new in corruptions:
        assert brief.count(old) == 1, (tag, brief.count(old))
        bad = brief.replace(old, new)
        rep2, f2, _ = run(bad, draft, "DELIBERATELY CORRUPTED -- %s" % tag)
        fired = len(f2["NO-MATCH"]) > len(findings["NO-MATCH"])
        live.append((tag, fired, len(f2["NO-MATCH"]), [x[1] for x in f2["NO-MATCH"]]))
        log.append(rep2)

    L = []
    L.append("")
    L.append("#" * 78)
    L.append("# GUARD E LIVENESS -- the guard shown FAILING on purpose")
    L.append("#" * 78)
    L.append("baseline (shipped brief) NO-MATCH count = %d" % len(findings["NO-MATCH"]))
    allfired = True
    for tag, fired, n, atomlist in live:
        allfired = allfired and fired
        L.append("  %-64s  %s  (NO-MATCH %d)" % (tag, "FIRES" if fired else "*** SILENT ***", n))
        new_atoms = [a for a in atomlist if a not in [x[1] for x in findings["NO-MATCH"]]]
        for a in new_atoms:
            L.append("        newly-unmatched atom: %s" % a)
    L.append("  ALL THREE CORRUPTIONS DETECTED = %s" % allfired)
    L.append("")
    L.append("#" * 78)
    L.append("# ADJUDICATION LIST -- RULING CE: a false positive is named in the open,")
    L.append("# with its reason, and is NEVER regexed away.  Narrowing the class to")
    L.append("# silence one is how BK1 was born.")
    L.append("#" * 78)
    for f in findings["ELSEWHERE"]:
        L.append("  [%-20s] draft line %-5s  %s" % (f[0], f[2], f[1]))
    L.append("  (count %d -- each one is content that IS in the draft but NOT inside the"
             % len(findings["ELSEWHERE"]))
    L.append("   statement block the brief attributes it to.  That is a PROVENANCE finding,")
    L.append("   not a correctness finding, and it is reported as such.)")
    L.append("")
    L.append("#" * 78)
    L.append("# WHAT GUARD E DOES NOT DO -- stated here, not left for a judge")
    L.append("#" * 78)
    L.append("  * It matches ATOMS, not MEANING.  Two clauses can share every atom and")
    L.append("    still say different things (quantifier order, scope of a 'for every').")
    L.append("  * It cannot see a hypothesis that the SOURCE itself leaves standing")
    L.append("    outside its statement block (SS7.2's standing reductio is a paragraph")
    L.append("    above Lemma S, not inside it).  Those show up as MATCH-ELSEWHERE.")
    L.append("  * It says nothing about whether the SOURCE is right.  GUARD B said the")
    L.append("    brief no longer lies about what it contains; GUARD E says the brief's")
    L.append("    transcription matches the draft.  Neither says the mathematics is true.")
    log.append("\n".join(L))

    # ============================================================ RULING CI
    # FALSE-POSITIVE PROBES.  A checker that MANUFACTURES a defect is worse than
    # one that misses a defect: a miss costs a round, a manufactured defect costs
    # a correct result.  Liveness alone only proves the guard can say NO.  These
    # two inputs are ADMISSIBLE BY CONSTRUCTION -- each differs from the shipped
    # brief only in a way the declared transform table is defined to absorb -- and
    # the guard must say YES to both.
    fp = [
        ("FP1 WHITESPACE REFLOW inside a statement block (semantics identical)",
         "> `slack := L(tau+1) - ( sum_{b in B_lo} deg(b) + nu ) >= 1`, i.e.\n"
         "> `sum_{b in B_lo} deg(b) + nu <= L(tau+1) - 1`. Equivalently",
         "> `slack := L(tau+1) - ( sum_{b in B_lo} deg(b) + nu ) >= 1`,\n"
         "> i.e. `sum_{b in B_lo} deg(b) + nu <= L(tau+1) - 1`.\n> Equivalently"),
        ("FP2 UNICODE tau FOR ASCII tau in Theorem K (a pure transform difference)",
         "> `b in B` **has** `deg(b) >= tau + 1`.",
         "> `b in B` **has** `deg(b) >= \u03c4 + 1`."),
    ]
    F = []
    F.append("")
    F.append("#" * 78)
    F.append("# GUARD E FALSE-POSITIVE PROBES (RULING CI) -- the guard must stay SILENT")
    F.append("#" * 78)
    F.append("baseline (shipped brief) NO-MATCH count = %d" % len(findings["NO-MATCH"]))
    nofp = True
    for tag, old_s, new_s in fp:
        n = brief.count(old_s)
        if n != 1:
            F.append("  %-64s  ANCHOR NOT FOUND (%d) -- probe INVALID, not a pass" % (tag, n))
            nofp = False
            continue
        good = brief.replace(old_s, new_s)
        _r, f3, _ = run(good, draft, "FALSE-POSITIVE PROBE -- %s" % tag, verbose=False)
        clean = len(f3["NO-MATCH"]) <= len(findings["NO-MATCH"])
        nofp = nofp and clean
        F.append("  %-64s  %s  (NO-MATCH %d)" % (
            tag, "SILENT (correct)" if clean else "*** MANUFACTURED A DEFECT ***",
            len(f3["NO-MATCH"])))
        for a in [x[1] for x in f3["NO-MATCH"]]:
            if a not in [x[1] for x in findings["NO-MATCH"]]:
                F.append("        FALSELY unmatched atom: %s" % a)
    F.append("  NO FALSE POSITIVE ON EITHER PROBE = %s" % nofp)
    F.append("  (Liveness says the guard can say NO.  This says it does not say NO to")
    F.append("   text it has no business objecting to.  Both are required from here on.)")
    log.append("\n".join(F))

    out = "\n".join(log)
    open("problems/wowii/w61_r28_guardE.out", "w").write(out + "\n")
    print(out)
    return 0 if (len(findings["NO-MATCH"]) == 0 and allfired and nofp) else 1


if __name__ == "__main__":
    sys.exit(main())
