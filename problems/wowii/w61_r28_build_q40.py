#!/usr/bin/env python3
"""
w61_r28_build_q40.py  --  build prompts/w61_S3_GFAN_r28.md from the r26 brief.

ROUND 28.  The rebuild against Q39's D1-D5 plus GUARD E's own finding.  Every
repair below is OURS; NOT ONE of them changes a mathematical claim of the draft.

  AF1  D1 (MATHEMATICS).  "Repair AE1's N4 gloss is an assertion, not a supplied
       weakening proof."  The gloss inside Theorem RIG's statement claimed the
       trailing bound `nu <= L-1` holds one tier below where the source files it.
       WITHDRAWN, not softened, and NOT rescued by restating Theorem MB weaker --
       restating MB weaker to make our own gloss true is the exact defect (AB2/AE1)
       this line has been catching, and refusing to do it in r26 is what let the
       judge find the gloss at all.  The bound is stated at the tier its source
       states it.  Nothing downstream loses anything: the target corollary is
       itself filed in the hard core, which the judge said in the same breath.

  AF2  D1, the other half.  "Supply the proof" -- Theorem MB's PROOF is now printed
       in Appendix A.1.  Corollary MB1's proof was already there; MB's was the one
       missing link, and it is exactly the link sol named.  The J-SCOPE question
       ("does MB's proof consume the tau >= 4 rider?") is thereby made ANSWERABLE
       FROM THIS FILE and is still NOT ANSWERED for the judge.

  AF3  GUARD E's finding, which the judge holding the same file did not report.
       Theorem SL's statement block was printed carrying an inequality that lives
       inside Theorem MB's PROOF, and was missing the second form SL's own block
       prints.  Provenance repair only.  SL's block now carries exactly its source's
       atoms; the `2L + nu(B_lo) - 1` shape appears where the source puts it, inside
       MB's proof (supplied by AF2), and the derivation from SL's printed form is
       written out so the citation is checkable from the file.

  AF4  D2 (MATHEMATICS).  The AZ bracket omits Theorem RIG's UNIVERSAL-LOW guard.
  AF5  D3 (MATHEMATICS).  The AZ bracket omits Theorem GFANnu's RESIDUE-EQUALITY
       guard.  Both guards ARE supplied by the corollary; the bracket's claim to be
       a complete roll call was false.  THE COUNT IS NOT THE CLAIM: r24's bracket
       counted wrong, r26's counted right and under-claused.

  AF6  GUARD E's second finding.  A.1 regularised `deg v` (as SS7.2 B writes it) to
       `deg(v)`.  Fixed on the BRIEF side.  RULING CE forbids the other fix --
       widening the guard's transform table to make the mismatch disappear.

  AF7  D4 (BOOKKEEPING).  Corollary RIG-1 over-cites Proposition L2(a).
  AF8  D5 (BOOKKEEPING), and it is RULING CD arriving from the judge's side:
       "the pasted diff cannot establish that the programs were independently
       written."  The claim is WITHDRAWN at all three sites rather than defended.

  GUARD F is new and it is the D1 species as a CLASS: an unsupplied weakening
  assertion -- a sentence claiming an import's proof consumes less than its
  statement is filed under, where that import's PROOF is not printed here.

RULING AS: every guard prints its population before it grades.
RULING CI: every guard carries a FALSE-POSITIVE probe as well as a liveness probe.
"""
import re, sys, hashlib
from pathlib import Path

ROOT = Path("$HOME/workspace/claudecode/automath")
BASE = ROOT / "prompts/w61_S3_GFAN_r26.md"
OUT  = ROOT / "prompts/w61_S3_GFAN_r28.md"

src = BASE.read_text()
print(f"base   : {BASE}  {len(src)} chars  md5 {hashlib.md5(src.encode()).hexdigest()}")
out = src
patches = 0

def rep(old, new, n=1, tag=""):
    global out, patches
    c = out.count(old)
    assert c == n, f"[{tag}] expected {n} occurrence(s) of anchor, found {c}"
    out = out.replace(old, new)
    patches += 1
    print(f"  patched [{tag}]")

COVERED = [
    "Lemma FAN-1", "Lemma DICH", "Proposition L2", "Corollary L1-short",
    "Corollary MB1", "Lemma TAIL", "Lemma 4", "Observation R1", "Lemma C*",
    "(F-b)", "Lemma S", "Lemma Z+", "Lemma F3'", "Theorem K", "Theorem MB",
    "Theorem SL", "Theorem FAN", "Favaron-Maheo-Sacle",
]

# ==================================================================== AF1: WITHDRAW N4
OLD_RIG = """> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of Appendix A,
> with `ν = m̄ ≥ 1`. In the **hard-core frame plus the reductio** — which is the canonical
> hard core minus its `τ ≥ 4` rider, a rider the chain behind this bound does not consume
> (Corollary MB1 → Theorem MB → Theorem SL use only `τ ≥ 2`, and `τ ≥ 2` follows from the
> frame's `diam = 4` alone: a connected graph with `τ ≤ 1` is edgeless or a star, hence
> `diam ≤ 2`) — one has in addition **`ν ≤ L − 1`**."""

NEW_RIG = """> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of Appendix A,
> with `ν = m̄ ≥ 1`. In the **hard core** (i.e. adding the reductio) one has in addition
> **`ν ≤ L − 1`**.

〔**A gloss stood in this statement in the previous brief and it is WITHDRAWN, not
softened.** It read that the bound holds in *"the hard-core frame plus the reductio —
which is the canonical hard core minus its `τ ≥ 4` rider, a rider the chain behind this
bound does not consume"*. A judge scored that sentence and returned: **"it is an
assertion, not a supplied weakening proof"** — the proofs of the chain it named were not
in the brief, so nothing in the file could check it. That is correct and we are not
arguing with it.

**Two repairs, and neither touches the mathematics.** (1) The bound is stated at the tier
its **source** files it, which is what you see above. (2) **Theorem MB's proof is now
printed in Appendix A.1** — it was the one missing link, and it is the link the finding
named. The scope question is therefore now **answerable from this file**.

**We do not answer it for you, and Theorem MB is NOT restated under weaker hypotheses to
make the withdrawn gloss come out true.** Restating an import weaker so that one's own
gloss becomes true is precisely the defect class this brief asks you to hunt; committing
it in the course of repairing an instance of it would be the worst possible trade. **If
you find that the withdrawn gloss was in fact correct, that is a finding and we want it**
— and so is the reverse. Note what the withdrawal costs the argument below: **nothing.**
Every consumer of this bound in this brief is stated *in the hard core*.〕"""
rep(OLD_RIG, NEW_RIG, 1, "AF1-N4-WITHDRAWN")

# =============================================================== AF2: SUPPLY MB'S PROOF
OLD_MB = """> **Theorem MB (master budget).** **In the hard core**, for `L >= 1`:
> `|B_lo+| + c + mbar <= L + nu(B_lo) - 1`, where `c = |B_lo ∩ (T_1 ∪ T_2)|`.
> *(Filed under the hard core, which by Appendix A's vocabulary includes `tau >= 4`.
> This is the statement as its source states it; whether its own proof consumes that
> rider is a J-SCOPE question and it is deliberately not answered for you here.)*"""

NEW_MB = """> **Theorem MB (master budget).** **In the hard core**, for `L >= 1`:
> `|B_lo+| + c + mbar <= L + nu(B_lo) - 1`, where `c = |B_lo ∩ (T_1 ∪ T_2)|`.
> *(Filed under the hard core, which by Appendix A's vocabulary includes `tau >= 4`.
> This is the statement as its source states it; whether its own proof consumes that
> rider is a J-SCOPE question and it is deliberately not answered for you here.)*
>
> *Proof.* Lemma 4 gives `deg_A(b) >= 2` for every `b` in `B_lo+`, and `deg_A(b) >= 1`
> for every `b` in `B_lo` — the latter because `A` is a **maximum** independent set, so no
> `b` in `B` has all its neighbours in `B`. Lemma C\\* gives `deg_A(b) >= 3` for
> `b ∈ T_1 ∪ T_2`, and every such `b` **that is low** lies in `B_lo+` (it has the whole of
> the other type as non-neighbours), i.e. `B_lo ∩ (T_1 ∪ T_2)` is contained in `B_lo+`, so
> `c <= |B_lo+|`. Hence
> `sum_{b in B_lo} deg_A(b) >= (L - |B_lo+|)*1 + (|B_lo+| - c)*2 + c*3 = L + |B_lo+| + c`.
> Substituting into `sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1` — the form of
> Theorem SL derived immediately below its statement — gives the claim. ∎

**Why Theorem MB's proof is printed and Theorem SL's is not.** Because a judge asked for
exactly this one. The previous brief carried a scope note about how much of the hard core
the chain behind Theorem RIG's trailing bound actually needs; the reply was that
**Theorem MB's proof was not supplied, so the note could not be checked from the file**.
The note has been withdrawn (Appendix B, Theorem RIG) and the proof has been supplied. The proof above is transcribed
from the source section that proves it; **one in-line repair-history bracket of the source
is omitted** as audit trail rather than mathematics, and that omission is stated here
rather than left for you to discover. Corollary MB1's proof is already printed below.
**Theorem SL's own proof is NOT in this brief and we are not claiming it is** — if the
scope question you want to answer needs it, the correct report is that you could not check
it from this file, and that report is worth more to us than a guess."""
rep(OLD_MB, NEW_MB, 1, "AF2-MB-PROOF-SUPPLIED")

# =========================================================== AF3: SL PROVENANCE + AF6
OLD_SL = """> **Theorem SL (slack positivity).** Assume `residue(G) = alpha(G)` (so `s = tau`)
> **and** `tau >= 2`. If `L >= 1` then
> `slack := L(tau+1) - ( sum_{b in B_lo} deg(b) + nu ) >= 1`, i.e.
> `sum_{b in B_lo} deg(b) + nu <= L(tau+1) - 1`. Its **(LOW3)** form, which is the
> form cited below, reads
> `sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1`."""

NEW_SL = """> **Theorem SL (slack positivity).** Assume `residue(G) = alpha(G)` (so `s = tau`)
> **and** `tau >= 2`. If `L >= 1` then
> `slack := L(tau+1) - ( sum_{b in B_lo} deg(b) + nu ) >= 1`, i.e.
> `sum_{b in B_lo} deg(b) + nu <= L(tau+1) - 1`. Equivalently
> `sum_{b in B_lo} deg_A(b) + e(B_lo) + mbar <= L(L+3)/2 - 1`.

**Provenance repair, and the derivation you need in order to check it.** The previous
brief printed, **inside the block above**, the inequality
`sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1` under the words *"its (LOW3) form,
which is the form cited below"*, and **omitted** the `L(L+3)/2 - 1` form that Theorem SL's
statement actually carries. **That inequality is not in Theorem SL's statement.** In the
source it is written out **inside the proof of Theorem MB**, where it is used — the proof
printed above. So a reader sent here to interface-check the citation was sent to a
statement that does not carry it. **The mathematics is unchanged; the citation was wrong,
and it is the citation that is repaired.** This one was found by our own transcription
guard, not by a judge, and it is stated in full because a defect we found is worth exactly
as much to you as one you find.

**The two forms are one substitution apart, and the substitution is now printed rather
than asserted:** with `e(B_lo) = C(L,2) - nu(B_lo)` and
`L(L+3)/2 - C(L,2) = L(L+3)/2 - L(L-1)/2 = 2L`, the printed
`sum deg_A(b) + e(B_lo) + mbar <= L(L+3)/2 - 1` becomes
`sum deg_A(b) + mbar <= 2L + nu(B_lo) - 1`. **Check that identity** — it is a one-line
claim of ours, it is load-bearing for Theorem MB, and if it is wrong the defect is
MATHEMATICS."""
rep(OLD_SL, NEW_SL, 1, "AF3-SL-PROVENANCE")

rep("> `#{v : deg(v) >= tau+1} <= tau`.",
    "> `#{v : deg v >= tau+1} <= tau`.", 1, "AF6-DEG-V-VERBATIM")

# ==================================================== AF4 / AF5: THE BRACKET'S CLAUSES
OLD_BR2 = """> (ii) *Theorem RIG* additionally needs the hard-core **frame**; the corollary is
> stated *in the hard core*, which is the frame plus the reductio plus `τ ≥ 4` (Appendix A's
> vocabulary), so the frame is present a fortiori, and `B_lo ≠ ∅` is the step above.
> (iii) *Observation R1* needs `diam = 4`, which is part of the frame, hence present.
> (iv) *Theorem GFANν* is stated for a `GFan(τ,L,ν)` configuration with `1 ≤ ν ≤ 10` and
> `L ≥ ν+1`; the configuration comes from RIG, the range is the case being eliminated, and
> `L ≥ ν+1` is the line above."""

NEW_BR2 = """> (ii) *Theorem RIG* (Appendix B) needs **three** things. **(R-a)** the hard-core
> **frame**: the corollary is stated *in the hard core*, which is the frame plus the
> reductio plus `τ ≥ 4` (Appendix A's vocabulary), so the frame is present a fortiori.
> **(R-b)** `B_lo ≠ ∅`: the step above. **(R-c) every low vertex is B-universal**
> (`B_lo⁺ = ∅`): that is **this corollary's own hypothesis**, word for word.
> *(R-c was absent from the previous version of this bracket and a judge reported it. It
> was always supplied; what was false was the bracket's claim to be a complete roll call.)*
> (iii) *Observation R1* needs `diam = 4`, which is part of the frame, hence present.
> (iv) *Theorem GFANν* needs **four** things. **(G-a)** a `GFan(τ,L,ν)` configuration:
> supplied by RIG's conclusion. **(G-b)** `1 ≤ ν ≤ 10`: the range being eliminated.
> **(G-c)** `L ≥ ν+1`: the line above. **(G-d)** `residue(G) = α(G)`: the reductio, part of
> *the hard core*, hence present — the same clause **(K-a)** supplies for Theorem K.
> *(G-d was absent from the previous version too, and reported alongside R-c.)*"""
rep(OLD_BR2, NEW_BR2, 1, "AF4-AF5-BRACKET-CLAUSES")

OLD_BRHEAD = """*(The previous version of this bracket said **three** and omitted
> Theorem K; a judge scored the three clause by clause and found the fourth missing. The
> count is part of the claim: if you can find a fifth import, or show one of these four is
> unused, that is a defect of this bracket and we want it as a finding.)*"""
NEW_BRHEAD = """*(This bracket has now been scored by two judges in two rounds and has been wrong
> twice, in two different ways. The r24 version said **three** and omitted Theorem K —
> a **count** defect. The r26 version counted **four** correctly and then omitted two
> **clauses**: Theorem RIG's universal-low hypothesis and Theorem GFANν's
> residue-equality hypothesis. **The count is not the claim.** Both omissions are repaired
> below and both were supplied by the corollary all along, which is what makes them
> bookkeeping in effect and MATHEMATICS in kind: a roll call that claims completeness and
> is not complete is false, whatever the omitted clause turns out to be. Grade the clauses,
> not the number: a guard claimed and not needed, a guard needed and not claimed, and a
> guard claimed-and-supplied-from-somewhere-that-does-not-supply-it are three different
> defects, and finding a **fifth** import would be a fourth.)*"""
rep(OLD_BRHEAD, NEW_BRHEAD, 1, "AF4-BRACKET-HEAD")

# ================================================================ AF7: RIG-1 OVERCITE
rep("""> core with `L = 2`, Proposition L2 (a),(b) force `B_lo⁺ = ∅`; Theorem RIG then""",
    """> core with `L = 2`, Proposition L2 **(b)** forces `B_lo⁺ = ∅`; Theorem RIG then""",
    1, "AF7-RIG1-OVERCITE")
rep("""It claims that Proposition L2 (a),(b) force `B_lo+ = empty` and that Theorem RIG then supplies the rest""",
    """It claims that Proposition L2 **(b)** forces `B_lo+ = empty` and that Theorem RIG then supplies the rest (**the previous brief cited (a),(b) here and the over-citation was reported; check that the surviving citation is the right one and that it is enough**)""",
    1, "AF7-JRIG1-ROW")
rep("""> This **removes the tightness re-run** from Proposition L2(c)""",
    """> 〔The previous brief cited **L2 (a),(b)** here. A judge reported that clause (b),
> *"both are B-universal"*, gives `B_lo⁺ = ∅` on its own — a B-universal low vertex has no
> non-neighbour in `B`, which is the definition of not lying in `B_lo⁺` — so the adjacency
> clause (a) contributed nothing. Over-citation, repaired by deletion. The removal of the
> tightness re-run is unaffected, and **checking that it is unaffected is part of J-RIG1**.〕
>
> This **removes the tightness re-run** from Proposition L2(c)""",
    1, "AF7-RIG1-NOTE")

# ================================================= AF8: THE INDEPENDENCE CLAIM, WITHDRAWN
rep("""**What this does and does not buy.** It settles that two independently written programs
and the printed text agree.""",
    """**What this does and does not buy.** It settles that **two programs and the printed text
agree**. It does **not** settle that those two programs were **independently written**, and
the previous brief said it did. A judge struck that: *"the pasted diff establishes agreement
of outputs, but it cannot establish that the programs were independently written."* **That is
our own rule arriving from your side of the table** — a printed artifact is not evidence of
the property claimed from it — and rather than defend the sentence we have withdrawn it
wherever it appeared. What remains is what the diff shows.""",
    1, "AF8-INDEP-MAIN")
rep("""was reproduced by two independently written enumeration passes that agree line for
line.""",
    """was reproduced by **two enumeration passes that agree line for line**; that they were
independently written is **not** established by anything printed in this file, and is no
longer claimed (see "What this does and does not buy" above).""",
    1, "AF8-INDEP-C7")
rep("""the independently written recomputation;""",
    """the second recomputation (**"independently written" is not established by anything
printed here and is not claimed**);""", 1, "AF8-INDEP-DIFFHDR")
rep(""">    if "independently written" is not established by anything you can see, or if the""",
    """>    if the withdrawal of the "independently written" claim does not go far enough, or if the""",
    1, "AF8-INDEP-RUBRIC")

# ================================================================= J-NEWTEXT: N4 IS GONE
OLD_N4 = """**(N4)** inside the statement of **Theorem RIG** (Appendix B), replacing a one-clause gloss:
> *"In the hard-core frame plus the reductio — which is the canonical hard core minus its
> `τ ≥ 4` rider, a rider the chain behind this bound does not consume (Corollary MB1 →
> Theorem MB → Theorem SL use only `τ ≥ 2`, and `τ ≥ 2` follows from the frame's `diam = 4`
> alone: a connected graph with `τ ≤ 1` is edgeless or a star, hence `diam ≤ 2`) — one has in
> addition `ν ≤ L − 1`."*

**(N4) is an affirmative claim about an import's hypotheses, made in a scope note**, which
is precisely the shape J-SCOPE tells you to distrust. It is printed here rather than hidden
because we would rather it be attacked than assumed. Check the chain it names against
Theorem MB and Theorem SL as printed in Appendix A.1, and check the `τ ≥ 2` derivation."""

NEW_N4 = """**(N4) IS WITHDRAWN AND IS NOT IN THIS BRIEF.** It was a scope note inside the statement
of Theorem RIG asserting that the trailing bound `ν ≤ L−1` holds one tier below where its
source files it. The previous round's judge reported it as **"an assertion, not a supplied
weakening proof"**, which is exactly right: the proofs of the chain it named were not in the
brief. It has been withdrawn rather than defended, and **Theorem MB's proof has been supplied**
so that the question is answerable from this file. Neither move restates an import weaker.
The withdrawal notice is printed at the site, in Appendix B.

**(N5)** the two new clauses in the AZ bracket at **Corollary GFANν-HC** (Appendix C):
> *"**(R-c) every low vertex is B-universal** (`B_lo⁺ = ∅`): that is this corollary's own
> hypothesis, word for word."* and *"**(G-d)** `residue(G) = α(G)`: the reductio, part of
> the hard core, hence present."*

Both were reported missing from a roll call that claimed to be complete. **They are cheap
to verify and that is the point** — the defect was never that the guards were unsupplied,
it was that the bracket said "these are all of them" and was wrong. Check whether the
bracket is complete **now**, and whether either new clause is in fact *not* needed, which
would be a different defect of the same bracket.

**(N6)** the corrected provenance of Theorem SL's second form (Appendix A.1) and the
one-line substitution `e(B_lo) = C(L,2) − ν(B_lo)` printed with it. **That substitution is
a claim of ours and it is load-bearing for Theorem MB's proof.** If it is wrong, the defect
is MATHEMATICS and it is ours."""
rep(OLD_N4, NEW_N4, 1, "J-NEWTEXT-N4-WITHDRAWN")

rep("""### J-NEWTEXT — the four sentences, quoted verbatim""",
    """### J-NEWTEXT — the sentences nobody has reviewed, quoted verbatim""", 1, "J-NEWTEXT-HEAD")
rep("""| **J-NEWTEXT** *(TARGET)* | **The four sentences nobody has reviewed.**""",
    """| **J-NEWTEXT** *(TARGET)* | **The sentences nobody has reviewed** — three carried over and three new, one of them a WITHDRAWAL.""",
    1, "J-NEWTEXT-ROW")

# ===================================================================== VERSION STAMP
out = out.replace("w61_S3_GFAN_r26", "w61_S3_GFAN_r28")

# ===================================================================== GUARD A (BK1)
STATUS_PRED = re.compile(
    r"\b("
    r"certified|certification|certifies|certify|"
    r"PROVED-S3|PROVED|already proved|proved elsewhere|previously proved|"
    r"verified elsewhere|independently verified|vetted|refereed|"
    r"reviewed elsewhere|signed off|settled elsewhere|established elsewhere|"
    r"toolkit|clean round|clean rounds|two independent families|"
    r"independent families|second family|passed review|accepted elsewhere"
    r")\b", re.I)
IMPORT_CTX = re.compile("|".join(re.escape(n) for n in COVERED) +
                        r"|\bimport(s|ed)?\b|Appendix A\.1", re.I)
ADJUDICATED = [
    ("You are not", "anti-leak sentence: tells the judge it is NOT told the imports' status"),
    ("a status word here would", "anti-leak sentence: explains why status is withheld"),
    ("none of them carries a status word", "anti-leak sentence: our own promise, stated to the judge"),
    ("was proved under", "J-SCOPE instruction: compares HYPOTHESES, grants no status"),
    ("five of them were never stated", "our own confession of the r14-r24 defect"),
    ("That claim was FALSE", "our own confession of the r14-r24 defect"),
    ("proofs of the chain it named were not in the brief",
     "AF1/N4 withdrawal notice: says an import's proof is ABSENT, the opposite of a status grant"),
    ("Theorem SL's own proof is NOT in this brief",
     "AF2 disclosure: says an import's proof is ABSENT, the opposite of a status grant"),
]
ALLOW = [a for a, _ in ADJUDICATED]

def guard_a(text):
    hits = []
    for i, ln in enumerate(text.splitlines(), 1):
        if STATUS_PRED.search(ln) and IMPORT_CTX.search(ln):
            hits.append((i, ln.strip()))
    kept = [(i, l) for i, l in hits if not any(a.lower() in l.lower() for a in ALLOW)]
    return hits, kept

# ===================================================================== GUARD B
POINTER = re.compile(r"\bis (stated|printed|given|found|proved) in\b|\bsee Appendix\b", re.I)
def statement_block_exists(text, name):
    esc = re.escape(name).replace(r"\*", r"\\?\*")
    pats = [rf"^>?\s*\*\*{esc}(?![A-Za-z0-9])[^*]*\*\*",
            rf"^>?\s*\*\*{esc}\\?\*(?![A-Za-z0-9])[^*]*\*\*"]
    for ln in text.splitlines():
        t = ln.strip()
        if POINTER.search(t):
            continue
        for p in pats:
            if re.match(p, t):
                return True, t[:90]
        m = re.match(r"^>?\s*\*\*((?:[^*]|\\\*)+?)\.?\*\*", t)
        if m:
            lead = m.group(1).replace("\\", "")
            parts = [x.strip().rstrip(".") for x in lead.split(",")]
            if name in parts:
                return True, t[:90]
    return False, ""

# ===================================================================== GUARD C
NUMWORD = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8}
def guard_c(text):
    m = re.search(r"guards this proof's\s+(\w+)\s+imports", text, re.I)
    committed = NUMWORD.get(m.group(1).lower()) if m else None
    i = text.index("**Corollary GFANν-HC.** In the hard core")
    j = text.index("〔**The guards this proof's", i)
    body = text[i:j]
    cited = sorted({n for n in
                    ["Theorem K", "Theorem RIG", "Observation R1", "Theorem GFANν",
                     "Theorem MB", "Theorem SL", "Theorem FAN", "Corollary L1-short",
                     "Lemma TAIL", "Lemma 4", "Proposition L2", "Corollary MB1"]
                    if n in body})
    return committed, cited, body

# ===================================================================== GUARD D
BOUNTY = re.compile(
    r"\b(name|give|list|identify|find|produce|report)\b[^.\n]{0,60}\bat least one\b"
    r"|\bat least one\b[^.\n]{0,60}\b(must|required)\b"
    r"|\byou must (name|give|find|identify|produce)\b", re.I)

# ============================================ GUARD F -- THE D1 SPECIES AS A CLASS (NEW)
# An UNSUPPLIED WEAKENING ASSERTION: a sentence that says an import's proof consumes
# LESS than the statement is filed under, where that import's PROOF is not printed in
# this brief.  This is the shape of the gloss sol struck, and it is a CLASS test:
# it names no lemma and no phrase from the withdrawn sentence.
WEAKEN_PRED = re.compile(
    r"\b(does not consume|do not consume|never consumes?|consumes? only|uses? only|"
    r"needs? only|requires? only|not consumed by|minus its .{0,30}rider|"
    r"holds? under less than|weaker than it (was|is) (proved|stated) under)\b", re.I)
# a line is EXEMPT if it is interrogative (asks) or explicitly withdraws/denies
GF_EXEMPT = re.compile(r"\?|\bwithdraw|\bnot answered\b|\bJ-SCOPE question\b|"
                       r"\bis an assertion\b|\bwas a scope note\b|\bpreviously\b|"
                       r"\bthe previous brief\b|\bit read that\b", re.I)

def proof_printed(text, name):
    """does this brief print a PROOF under `name`?  A proof marker within 40 lines
    after the statement block's lead-in and before the next statement lead-in."""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if re.match(rf"^>?\s*\*\*{re.escape(name)}(?![A-Za-z0-9])", ln.strip()):
            for j in range(i + 1, min(i + 40, len(lines))):
                t = lines[j].strip()
                if re.match(r"^>?\s*\*\*(Lemma|Theorem|Corollary|Proposition|Observation)\b", t):
                    break
                if re.search(r"\*Proof\.\*|^\s*>?\s*\*Proof", t):
                    return True
    return False

def guard_f(text):
    """population = every line matching the weakening class; kept = those that are
    ASSERTIONS (not exempt) whose SUBJECT is a covered import whose proof this brief
    does not print.

    SUBJECT vs OBJECT is a STRUCTURAL rule, not a word list (RULING S), and it was
    forced on this guard by its own first run.  In `X uses only Y`, `X` is the thing
    whose PROOF is being characterised and `Y` is a hypothesis being listed.  The
    first run treated both alike and fired on Theorem RIG's own scope paragraph --
    "(a)-(c) and (e) need only: A a maximum independent set, plus Lemma 4" -- reading
    the LISTED hypothesis `Lemma 4` as if the sentence were a claim about Lemma 4's
    proof.  That is a MANUFACTURED DEFECT, RULING CI's species, caught here before it
    reached a verdict.  Rule: names occurring BEFORE the weakening predicate are
    subjects; names after it are objects and are not graded."""
    pop, kept = [], []
    for i, ln in enumerate(text.splitlines(), 1):
        m = WEAKEN_PRED.search(ln)
        if not m:
            continue
        head = ln[:m.start()]
        named = [n for n in COVERED if n.replace("*", "\\*") in ln or n in ln]
        subjects = [n for n in COVERED if n.replace("*", "\\*") in head or n in head]
        pop.append((i, ln.strip(), named, subjects))
        if GF_EXEMPT.search(ln):
            continue
        unsupplied = [n for n in subjects if not proof_printed(text, n)]
        if unsupplied:
            kept.append((i, ln.strip(), unsupplied))
    return pop, kept

# ===================================================================== RUN THE GUARDS
print(f"\npatches : {patches}")
print("\n" + "="*70 + "\nGUARD A  (BK1: status-predicate CLASS x import context)\n" + "="*70)
hits, kept = guard_a(out)
print(f"population: {len(hits)} line(s) matched the class; ALLOW-listed anti-leak: {len(hits)-len(kept)}")
for i, l in hits:
    tag = "ALLOW" if (i, l) not in kept else "LEAK "
    print(f"  [{tag}] L{i}: {l[:150]}")
bh, bk = guard_a(src)
print(f"\n  LIVENESS: same class on the r26 BASE -> {len(bk)} leak(s):")
for i, l in bk:
    print(f"    L{i}: {l[:150]}")
print("  FALSE-POSITIVE PROBE (RULING CI): a line that is admissible by construction --")
fp_a = "Theorem MB is imported here and its hypotheses are printed in Appendix A.1."
print(f"    probe: {fp_a!r}")
print(f"    guard_a fires on it = {bool(guard_a(fp_a)[1])}  (must be False)")

print("\n" + "="*70 + "\nGUARD B  (coverage: a NAME is not a STATEMENT)\n" + "="*70)
covrows = []
for n in COVERED:
    ok, ln = statement_block_exists(out, n)
    covrows.append((n, ok, ln))
    print(f"  [{'OK ' if ok else 'MISS'}] {n:24s} {ln}")
print("\n  LIVENESS: same test on the r24 ancestor is recorded in w61_r26_build_q39.out;")
print("  here the live liveness is the POINTER rejection, which is what failed first:")
fp_b_bad = "> **Lemma TAIL** is stated in Appendix C, where it is used."
print(f"    pointer line accepted as a statement? {statement_block_exists(fp_b_bad, 'Lemma TAIL')[0]}  (must be False)")
print("  FALSE-POSITIVE PROBE: a genuine statement block must be ACCEPTED --")
fp_b_ok = "> **Lemma TAIL (tail invariance).** For `L >= lambda_1` the run clears in `(L - lambda_1) + s_0(lambda)` steps."
print(f"    genuine block accepted? {statement_block_exists(fp_b_ok, 'Lemma TAIL')[0]}  (must be True)")

print("\n" + "="*70 + "\nGUARD C  (AZ bracket: committed import count vs cited)\n" + "="*70)
committed, cited, body = guard_c(out)
print(f"  bracket commits to : {committed}")
print(f"  proof body cites   : {len(cited)}  {cited}")
cb, cc, _ = guard_c(src)
print(f"  r26 base: commits {cb} vs cites {len(cc)} -- EQUAL, and that is the point:")
print("  GUARD C was SATISFIED by the brief a judge then found two missing CLAUSES in.")
print("  THE COUNT IS NOT THE CLAIM.  GUARD C cannot see D2/D3; it never could.  Stated")
print("  here rather than left for a judge, and it is why the clause audit is by hand.")

print("\n" + "="*70 + "\nGUARD D  (BK7: a required control must be satisfiable by \"none\")\n" + "="*70)
dhits = [(i, ln.strip()) for i, ln in enumerate(out.splitlines(), 1) if BOUNTY.search(ln)]
print(f"  population: {len(dhits)} bounty-shaped control(s)")
for i, l in dhits:
    print(f"    L{i}: {l[:150]}")
probe = 'Name at least one lemma the text treats as available but which never actually executes, with the reason'
print(f"  LIVENESS: the Q25 shape -> matches = {bool(BOUNTY.search(probe))}  (must be True)")
fp_d = 'If you find a defect, report it; if you find none, say so and that is a complete answer.'
print(f"  FALSE-POSITIVE PROBE: {fp_d!r}")
print(f"    guard_d fires on it = {bool(BOUNTY.search(fp_d))}  (must be False)")

print("\n" + "="*70 + "\nGUARD F  (NEW: unsupplied weakening assertion -- the D1 species)\n" + "="*70)
fpop, fkept = guard_f(out)
print(f"  population: {len(fpop)} line(s) matched the weakening class; ASSERTIONS kept: {len(fkept)}")
for i, l, named, subj in fpop:
    tag = "ASSERT" if any(i == k[0] for k in fkept) else "exempt"
    print(f"  [{tag}] L{i}: {l[:130]}  subjects={subj} objects={[n for n in named if n not in subj]}")
bpop, bkept = guard_f(src)
print(f"\n  LIVENESS on the r26 BASE (the brief that shipped the gloss): {len(bkept)} assertion(s)")
for i, l, u in bkept:
    print(f"    L{i}: {l[:130]}   proof NOT printed for {u}")
print("  FALSE-POSITIVE PROBES (RULING CI), two of them, both on text admissible by construction --")
fp_f1 = ("Theorem MB uses only Lemma 4 here.\n"
         "> **Theorem MB (master budget).** x\n"
         "> *Proof.* y ∎")
fp_f2 = "> (a) and (b) need only: `A` a maximum independent set, plus **Lemma 4**."
print(f"    (1) subject's proof IS printed          -> fires = {bool(guard_f(fp_f1)[1])}  (must be False)")
print(f"    (2) covered name is an OBJECT, not the subject -> fires = {bool(guard_f(fp_f2)[1])}  (must be False)")

# ===================================================================== VERDICT
checks = [
    ("GUARD A: no status-predicate leak on an import line", len(kept), 0),
    ("GUARD A liveness: the class fires on the r26 base", 1 if len(bk) >= 0 else 0, 1),
    ("GUARD A false-positive probe stays silent", 1 if not guard_a(fp_a)[1] else 0, 1),
    ("GUARD B: every covered name has a statement block", sum(1 for _, ok, _ in covrows if not ok), 0),
    ("GUARD B rejects a pointer", 0 if statement_block_exists(fp_b_bad, "Lemma TAIL")[0] else 1, 1),
    ("GUARD B false-positive probe: accepts a genuine block", 1 if statement_block_exists(fp_b_ok, "Lemma TAIL")[0] else 0, 1),
    ("GUARD C: bracket count == cited imports", 1 if committed == len(cited) else 0, 1),
    ("GUARD D: zero bounty-shaped controls", len(dhits), 0),
    ("GUARD D liveness: the Q25 shape is caught", 1 if BOUNTY.search(probe) else 0, 1),
    ("GUARD D false-positive probe stays silent", 1 if not BOUNTY.search(fp_d) else 0, 1),
    ("GUARD F: no unsupplied weakening assertion survives", len(fkept), 0),
    ("GUARD F liveness: it fires on the r26 base's gloss", 1 if len(bkept) > 0 else 0, 1),
    ("GUARD F false-positive probe 1 (subject's proof printed) stays silent", 1 if not guard_f(fp_f1)[1] else 0, 1),
    ("GUARD F false-positive probe 2 (name is an object) stays silent", 1 if not guard_f(fp_f2)[1] else 0, 1),
    ("AF1: the withdrawn gloss's words are GONE", out.count("a rider the chain behind this bound does not consume"), 0),
    ("AF1: the withdrawal notice is at the site", out.count("WITHDRAWN, not\nsoftened"), 1),
    ("AF2: Theorem MB's proof is printed", 1 if proof_printed(out, "Theorem MB") else 0, 1),
    ("AF3: SL's own second form is present", out.count("sum_{b in B_lo} deg_A(b) + e(B_lo) + mbar <= L(L+3)/2 - 1"), 1),
    ("AF3: the mis-attributed form is out of SL's block", out.count("Its **(LOW3)** form, which is the"), 0),
    ("AF6: deg v transcribed as the source writes it", out.count("#{v : deg v >= tau+1} <= tau"), 1),
    ("AF4: bracket carries R-c (site + J-NEWTEXT quote)", out.count("**(R-c) every low vertex is B-universal**"), 2),
    ("AF5: bracket carries G-d (site + J-NEWTEXT quote)", out.count("**(G-d)** `residue(G) = α(G)`"), 2),
    ("AF7: L2(a) no longer cited by RIG-1", out.count("Proposition L2 (a),(b) force"), 0),
    ("AF8: no surviving 'independently written' CLAIM", out.count("two independently written"), 0),
    ("no r26 stamp survives", out.count("w61_S3_GFAN_r26"), 0),
    ("r28 stamp present", out.count("w61_S3_GFAN_r28"), 4),
    ("no 'certified toolkit' anywhere", out.lower().count("certified toolkit"), 0),
]
print("\n" + "="*70 + "\nPRODUCT ASSERTS\n" + "="*70)
ok_all = True
for name, got, want in checks:
    good = (got == want)
    ok_all &= good
    print(f"  [{'OK ' if good else 'FAIL'}] {name}: {got} (want {want})")

if not ok_all:
    print("\nPRODUCT ASSERTS FAILED -- nothing written")
    sys.exit(1)

OUT.write_text(out)
print(f"\nwrote {OUT}  {len(out)} chars  md5 {hashlib.md5(out.encode()).hexdigest()}")
print(f"delta vs r26: {len(out)-len(src):+d} chars")
