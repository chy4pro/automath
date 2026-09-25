#!/usr/bin/env python3
"""
w61_r26_build_q39.py  --  build prompts/w61_S3_GFAN_r26.md from the r24 brief.

ROUND 26, RULING BQ step 1: FIX THE BRIEF.  Three defects, three different species,
each with a builder guard that is a CLASS test rather than a string test.

  (1) THE GAP's SOLE GROUND (sec 7.40 b).  Appendix A.1 has claimed to state "in full,
      every fact the proofs below reach outside themselves for", naming Theorem K --
      and has never printed K's statement, in any brief r14..r24.  Repair AD1 then made
      "at L = 0 Theorem K makes B a clique" the TARGET's first step, so a nine-round
      dormant briefing defect became load-bearing and Q38 returned GAP on it.
      FIX: print Theorem K, Theorem MB, Theorem SL, Lemma S, Lemma Z+, Lemma F3',
      Theorem FAN and Favaron-Maheo-Sacle as STATEMENT BLOCKS, verbatim in scope from
      the draft -- MB in particular keeps its "in the hard core" filing, because
      restating it under weaker hypotheses to make a gloss come out true would be the
      AB2/AE1 unlicensed-weakening defect committed by the briefer.
      GUARD B: for every name in the coverage sentence, a STATEMENT BLOCK must exist.
      Occurrence of the name is not evidence of a statement -- that is the
      silent-and-favourable check sec 7.40 (h)2 names.

  (2) BK1, still live in the dispatched r24 brief.  "The certified toolkit." answers
      J-IMPORT for eight named statements three lines above the place the judge cannot
      check them.  r24's assert missed it because its word list was FOUR LITERAL STRINGS
      (PROVED-S3 / separately certified / two independent families / already certified)
      and that phrase contains none of them.  RULING S: a perfectly live assert pointed
      at the wrong strings.
      GUARD A: a CLASS test -- any status predicate from a vocabulary, on any line that
      also names an imported statement.  Anti-leak sentences (which necessarily contain
      status words, negated) are carried on a NAMED allow-list that is printed, not
      hidden in the regex.

  (3) BK7.  A required control must be satisfiable by "none", or it is a bounty for a
      manufactured finding.
      GUARD D: a CLASS test for the control shape "<verb> ... at least one ..." and for
      unconditional demands.

  (4) RULING AZ, first field test (sec 7.40 c): the on-site bracket committed to THREE
      imports and there are FOUR.  The bracket is rewritten to four, K's guard is
      supplied clause by clause, and GUARD C asserts the bracket's committed count
      equals the number of distinct imports the target proof actually cites.

RULING AS throughout: every guard PRINTS ITS POPULATION before it grades.
"""
import re, sys, hashlib
from pathlib import Path

ROOT = Path("$HOME/workspace/claudecode/automath")
BASE = ROOT / "prompts/w61_S3_GFAN_r24.md"
OUT  = ROOT / "prompts/w61_S3_GFAN_r26.md"

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

# ===================================================================== IMPORT NAMES
# The names A.1 claims to cover.  This list IS the coverage sentence; Guard B checks
# the brief against it, and the brief prints the same list as a table the judge can
# check back against us.
COVERED = [
    "Lemma FAN-1", "Lemma DICH", "Proposition L2", "Corollary L1-short",
    "Corollary MB1", "Lemma TAIL", "Lemma 4", "Observation R1", "Lemma C*",
    "(F-b)", "Lemma S", "Lemma Z+", "Lemma F3'", "Theorem K", "Theorem MB",
    "Theorem SL", "Theorem FAN", "Favaron-Maheo-Sacle",
]

# ============================================================ 1. THE TOOLKIT BLOCK
# Kills BK1 at its root (the status sentence is deleted, not softened) and prints the
# five statements that were names only.  Scopes are the draft's, unaltered.
OLD_TOOLKIT = """**Lemma S, Lemma Z+, Lemma F3', Theorem K, Theorem MB, Theorem SL, Theorem FAN,
Favaron-Maheo-Sacle (`residue <= alpha`).** The certified toolkit. Theorem FAN says
the whole `Fan(tau, L >= 2)` family is eliminated from the hard core. Theorem MB reads
`|B_lo+| + c + mbar <= (L - 1) + nu(B_lo)` where `c = |B_lo ∩ (T_1 ∪ T_2)|`; Theorem
SL's (LOW3) form reads `sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1`."""

NEW_TOOLKIT = """**Lemma S, Lemma Z+, Lemma F3', Theorem K, Theorem MB, Theorem SL, Theorem FAN,
Favaron-Maheo-Sacle.** These eight were named here in every previous brief of this line
and **five of them were never stated**. They are stated now. Their hypotheses are
reproduced **exactly as the source states them** — where a statement is filed under more
than its own proof needs, that is left standing and is yours to report under J-SCOPE.

> **Lemma S (survivor degree bound).** Under the reductio `residue(G) = alpha(G)`
> (so `s = tau`): every survivor of the Havel-Hakimi run has degree `<= tau`;
> equivalently every vertex with `deg(v) >= tau+1` is a **head**, so
> `#{v : deg(v) >= tau+1} <= tau`.

> **Lemma Z+ (block occupancy).** At the start of step `j`, every later head whose
> current value exceeds `s - j + 1` lies in `block_j`, and is therefore decremented
> at step `j`.

> **Lemma F3' (survivor decay, general `s` — no reductio).** Let `s` be the number of
> Havel-Hakimi steps. At the start of step `j` (`1 <= j <= s`), every survivor has
> value `<= s - j + 1`.

> **Theorem K.** Assume `residue(G) = alpha(G)` (so `s = tau`) **and that every**
> `b in B` **has** `deg(b) >= tau + 1`. Then `K = B` and **`e_B = C(tau,2)`**, i.e.
> **`B` is a clique**.
> *(`K` is the set of heads of the run; `e_B` is the number of edges inside `G[B]`.
> The two displayed hypotheses are the whole of what Theorem K assumes: `diam = 4`,
> `f = alpha+1` and `tau >= 4` are **not** among them.)*

> **Theorem MB (master budget).** **In the hard core**, for `L >= 1`:
> `|B_lo+| + c + mbar <= L + nu(B_lo) - 1`, where `c = |B_lo ∩ (T_1 ∪ T_2)|`.
> *(Filed under the hard core, which by Appendix A's vocabulary includes `tau >= 4`.
> This is the statement as its source states it; whether its own proof consumes that
> rider is a J-SCOPE question and it is deliberately not answered for you here.)*

> **Theorem SL (slack positivity).** Assume `residue(G) = alpha(G)` (so `s = tau`)
> **and** `tau >= 2`. If `L >= 1` then
> `slack := L(tau+1) - ( sum_{b in B_lo} deg(b) + nu ) >= 1`, i.e.
> `sum_{b in B_lo} deg(b) + nu <= L(tau+1) - 1`. Its **(LOW3)** form, which is the
> form cited below, reads
> `sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1`.

> **Theorem FAN.** For every `tau` and every `L >= 2` there is **no** graph carrying the
> `Fan(tau,L)` configuration with `residue(G) = alpha(G)`. Consequently every
> `Fan(tau, L >= 2)` graph has `residue <= alpha - 1`.

> **Favaron-Maheo-Sacle.** `residue(G) <= alpha(G)`, for every graph `G`."""

rep(OLD_TOOLKIT, NEW_TOOLKIT, 1, "K-STATED/BK1-ROOT")

# ============================================================ 2. THE COVERAGE CLAIM
# The old sentence asserted coverage.  The new one hands the judge the list and invites
# it to falsify the claim -- and Guard B makes the claim true before it ships.
OLD_COVER = """now states, in full, every fact the proofs below reach outside themselves for:
Lemma FAN-1, Lemma DICH (all three clauses), Proposition L2, Corollary L1-short,
Corollary MB1, Lemma TAIL, Lemma 4, Observation R1, Lemma C*, (F-b), Theorem MB,
Theorem SL, Theorem FAN, Theorem K, Favaron-Maheo-Sacle. Appendix A.0 states the
Havel-Hakimi run vocabulary they are written in.

So **"I could not check this import" is no longer an available answer.**"""

NEW_COVER = """claims to state, in full, every fact the proofs below reach outside
themselves for. **That claim was FALSE in the five previous briefs of this line and a
judge caught it**: A.1 named Theorem K in a list, asserted it had been stated in full,
and never printed its statement — while a repair had meanwhile made "at `L = 0` Theorem K
makes `B` a clique" the **first step of the target proof**. The verdict that came back was
a GAP on precisely that, and it was right.

**So the claim is now printed as a list you can grade us on, not as an assurance:**
Lemma FAN-1, Lemma DICH (all three clauses), Proposition L2, Corollary L1-short,
Corollary MB1, Lemma TAIL, Lemma 4, Observation R1, Lemma C*, (F-b), Lemma S,
Lemma Z+, Lemma F3', Theorem K, Theorem MB, Theorem SL, Theorem FAN,
Favaron-Maheo-Sacle. **Eighteen names; this brief must contain eighteen statement blocks** —
seventeen in Appendix A.1 and **Lemma TAIL** in Appendix C, where it is used. Appendix A.0 states the Havel-Hakimi run vocabulary they are written in.
**If any name on that list has no statement under it, that is a defect of this brief and
we want it reported as one** — and if a proof below reaches for a fact that is on
neither list, that is a defect too.

So **"I could not check this import" is no longer an available answer.**"""

rep(OLD_COVER, NEW_COVER, 1, "COVERAGE-CHECKED")

# ============================================================ 3. THE AZ BRACKET -> FOUR
OLD_BRACKET = """> 〔**The guards this proof's three imports need, supplied here rather than three sections
> away.** (i) *Theorem RIG* additionally needs the hard-core **frame**; the corollary is
> stated *in the hard core*, which is the frame plus the reductio plus `τ ≥ 4` (Appendix A's
> vocabulary), so the frame is present a fortiori, and `B_lo ≠ ∅` is the step above.
> (ii) *Observation R1* needs `diam = 4`, which is part of the frame, hence present.
> (iii) *Theorem GFANν* is stated for a `GFan(τ,L,ν)` configuration with `1 ≤ ν ≤ 10` and
> `L ≥ ν+1`; the configuration comes from RIG, the range is the case being eliminated, and
> `L ≥ ν+1` is the line above. **`τ ≥ 4` is available but is NOT consumed by this proof** —
> stated so that an over-hypothesis reading of the corollary is visible rather than
> inferred. Check every clause of this bracket: it is an affirmative claim about what the
> imports need, and if one of these guards is not in fact required, or is required and not
> in fact supplied, that is a defect of this corollary.〕"""

NEW_BRACKET = """> 〔**The guards this proof's FOUR imports need, supplied here rather than four sections
> away.** The imports are **Theorem K**, **Theorem RIG**, **Observation R1** and
> **Theorem GFANν**. *(The previous version of this bracket said **three** and omitted
> Theorem K; a judge scored the three clause by clause and found the fourth missing. The
> count is part of the claim: if you can find a fifth import, or show one of these four is
> unused, that is a defect of this bracket and we want it as a finding.)*
> (i) *Theorem K* (Appendix A.1) needs exactly two things. **(K-a)** `residue(G) = α(G)`:
> that is the reductio, part of *the hard core*, hence present. **(K-b) every** `b ∈ B` has
> `deg(b) ≥ τ+1`: supplied by the case assumption `L = 0` **itself**, since `B_lo` is by
> definition (Appendix A) the set of `b ∈ B` with `deg(b) ≤ τ`, so `L = |B_lo| = 0` says
> exactly that every `b ∈ B` is high. **(K-b) is NOT supplied by "every low vertex is
> B-universal"**, which is vacuous at `B_lo = ∅` — that is the whole reason this step is
> written out. The conclusion used is exactly "`B` is a clique"; `e_B = C(τ,2)` and `K = B`
> are not used.
> (ii) *Theorem RIG* additionally needs the hard-core **frame**; the corollary is
> stated *in the hard core*, which is the frame plus the reductio plus `τ ≥ 4` (Appendix A's
> vocabulary), so the frame is present a fortiori, and `B_lo ≠ ∅` is the step above.
> (iii) *Observation R1* needs `diam = 4`, which is part of the frame, hence present.
> (iv) *Theorem GFANν* is stated for a `GFan(τ,L,ν)` configuration with `1 ≤ ν ≤ 10` and
> `L ≥ ν+1`; the configuration comes from RIG, the range is the case being eliminated, and
> `L ≥ ν+1` is the line above. **`τ ≥ 4` is available but is NOT consumed by this proof** —
> stated so that an over-hypothesis reading of the corollary is visible rather than
> inferred. **That negative claim now has to be checked against four imports, K included**,
> and K's two hypotheses are printed in A.1 so that it can be. Check every clause of this
> bracket: it is an affirmative claim about what the
> imports need, and if one of these guards is not in fact required, or is required and not
> in fact supplied, that is a defect of this corollary.〕"""

rep(OLD_BRACKET, NEW_BRACKET, 1, "AZ-BRACKET-FOUR")

# ============================================================ 4. VERSION STAMP
out = out.replace("w61_S3_GFAN_r24", "w61_S3_GFAN_r26")

# ===================================================================== GUARD A (BK1)
# CLASS test.  Not four strings: a status-predicate vocabulary x an import-name context.
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

# The class stays NOISY (RULING BB: err noisy).  Every line it flags and we do NOT
# treat as a leak is adjudicated HERE, BY NAME, WITH A REASON, and printed -- an
# off-site exclusion is invisible, a printed one is reviewable (RULING AZ's principle
# applied to our own checker).
ADJUDICATED = [
    ("You are not",
     "anti-leak sentence: tells the judge it is NOT told the imports' status"),
    ("a status word here would",
     "anti-leak sentence: explains why status is withheld"),
    ("none of them carries a status word",
     "anti-leak sentence: our own promise, stated to the judge"),
    ("was proved under",
     "J-SCOPE instruction: 'holds under less than it was proved under' compares "
     "HYPOTHESES, it does not grant any import a status"),
    ("five of them were never stated",
     "our own confession of the r14-r24 defect, printed to the judge"),
    ("That claim was FALSE",
     "our own confession of the r14-r24 defect, printed to the judge"),
]
ALLOW = [a for a, _ in ADJUDICATED]

def guard_a(text):
    hits = []
    for i, ln in enumerate(text.splitlines(), 1):
        if STATUS_PRED.search(ln) and IMPORT_CTX.search(ln):
            hits.append((i, ln.strip()))
    kept = [(i, l) for i, l in hits if not any(a.lower() in l.lower() for a in ALLOW)]
    return hits, kept

# ===================================================================== GUARD B (coverage)
POINTER = re.compile(r"\bis (stated|printed|given|found|proved) in\b|\bsee Appendix\b", re.I)

def statement_block_exists(text, name):
    """A NAME is not a STATEMENT, and a POINTER is not a STATEMENT either.

    Three ways this test was silent-and-favourable on its first run and is not now:
      * `\b` after `+`, `*`, `'` never matches (both sides non-word), so `Lemma Z+`,
        `Lemma F3'` and `Lemma C*` read as MISSING even when stated.  Use a
        not-followed-by-word-char lookahead instead.
      * the brief writes `Lemma C\*` (escaped); match either form.
      * `**Lemma TAIL** is stated in Appendix C` is a CROSS-REFERENCE.  It was accepted
        as a statement block on the first run.  Pointers are now rejected, and TAIL's
        real block in Appendix C is what has to be found.
    """
    esc = re.escape(name).replace(r"\*", r"\\?\*")
    pats = [rf"^>?\s*\*\*{esc}(?![A-Za-z0-9])[^*]*\*\*",
            rf"^>?\s*\*\*{esc}\\?\*(?![A-Za-z0-9])[^*]*\*\*"]
    # a joint lead-in such as "**Lemma C\*, (F-b).**" states both names at once
    for ln in text.splitlines():
        t = ln.strip()
        if POINTER.search(t):
            continue
        for p in pats:
            if re.match(p, t):
                return True, t[:90]
        # the lead-in itself may contain an escaped asterisk (`Lemma C\*`), so a plain
        # [^*]+ stops short of the comma and the second name is never seen
        m = re.match(r"^>?\s*\*\*((?:[^*]|\\\*)+?)\.?\*\*", t)
        if m:
            lead = m.group(1).replace("\\", "")
            parts = [x.strip().rstrip(".") for x in lead.split(",")]
            if name in parts:
                return True, t[:90]
    return False, ""

# ===================================================================== GUARD C (AZ count)
NUMWORD = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8}
def guard_c(text):
    m = re.search(r"guards this proof's\s+(\w+)\s+imports", text, re.I)
    committed = NUMWORD.get(m.group(1).lower()) if m else None
    # the target proof body: from the Corollary GFANnu-HC statement to the bracket
    i = text.index("**Corollary GFANν-HC.** In the hard core")
    j = text.index("〔**The guards this proof's", i)
    body = text[i:j]
    cited = sorted({n for n in
                    ["Theorem K", "Theorem RIG", "Observation R1", "Theorem GFANν",
                     "Theorem MB", "Theorem SL", "Theorem FAN", "Corollary L1-short",
                     "Lemma TAIL", "Lemma 4", "Proposition L2", "Corollary MB1"]
                    if n in body})
    return committed, cited, body

# ===================================================================== GUARD D (BK7)
BOUNTY = re.compile(
    r"\b(name|give|list|identify|find|produce|report)\b[^.\n]{0,60}\bat least one\b"
    r"|\bat least one\b[^.\n]{0,60}\b(must|required)\b"
    r"|\byou must (name|give|find|identify|produce)\b", re.I)

# ===================================================================== RUN THE GUARDS
print(f"\npatches : {patches}")
print("\n" + "="*70 + "\nGUARD A  (BK1: status-predicate CLASS x import context)\n" + "="*70)
hits, kept = guard_a(out)
print(f"population: {len(hits)} line(s) matched the class; ALLOW-listed anti-leak: {len(hits)-len(kept)}")
for i, l in hits:
    tag = "ALLOW" if (i, l) not in kept else "LEAK "
    print(f"  [{tag}] L{i}: {l[:150]}")
# and the same class run on the BASE, so the guard is shown to be able to fire
bh, bk = guard_a(src)
print(f"\n  LIVENESS: same class on the r24 BASE -> {len(bk)} leak(s) (must be > 0):")
for i, l in bk:
    print(f"    L{i}: {l[:150]}")

print("\n" + "="*70 + "\nGUARD B  (coverage: a NAME is not a STATEMENT)\n" + "="*70)
covrows = []
for n in COVERED:
    ok, ln = statement_block_exists(out, n)
    covrows.append((n, ok, ln))
    print(f"  [{'OK ' if ok else 'MISS'}] {n:24s} {ln}")
print("\n  LIVENESS: same test on the r24 BASE:")
for n in COVERED:
    ok, _ = statement_block_exists(src, n)
    if not ok:
        print(f"    [MISS on base] {n}")

print("\n" + "="*70 + "\nGUARD C  (AZ bracket: committed import count vs cited)\n" + "="*70)
committed, cited, body = guard_c(out)
print(f"  bracket commits to : {committed}")
print(f"  proof body cites   : {len(cited)}  {cited}")
cb, cc, _ = guard_c(src)
print(f"  LIVENESS on r24 base: commits {cb} vs cites {len(cc)} {cc}")

print("\n" + "="*70 + "\nGUARD D  (BK7: a required control must be satisfiable by \"none\")\n" + "="*70)
dhits = [(i, ln.strip()) for i, ln in enumerate(out.splitlines(), 1) if BOUNTY.search(ln)]
print(f"  population: {len(dhits)} bounty-shaped control(s)")
for i, l in dhits:
    print(f"    L{i}: {l[:150]}")
print("  LIVENESS: the shape the audit found in Q25's brief, run through this guard:")
probe = 'Name at least one lemma the text treats as available but which never actually executes, with the reason'
print(f"    probe matches = {bool(BOUNTY.search(probe))}  (must be True)")

# ===================================================================== VERDICT
checks = [
    ("GUARD A: no status-predicate leak on an import line", len(kept), 0),
    ("GUARD A liveness: the class fires on the r24 base", 1 if len(bk) > 0 else 0, 1),
    ("GUARD B: every covered name has a statement block", sum(1 for _, ok, _ in covrows if not ok), 0),
    ("GUARD B liveness: base is missing at least one", 1 if any(not statement_block_exists(src, n)[0] for n in COVERED) else 0, 1),
    ("GUARD C: bracket count == cited imports", 1 if committed == len(cited) else 0, 1),
    ("GUARD C liveness: base count != base cited", 1 if cb != len(cc) else 0, 1),
    ("GUARD D: zero bounty-shaped controls", len(dhits), 0),
    ("GUARD D liveness: the Q25 shape is caught", 1 if BOUNTY.search(probe) else 0, 1),
    ("Theorem K statement present", out.count("Then `K = B` and **`e_B = C(tau,2)`**"), 1),
    ("no r24 stamp survives", out.count("w61_S3_GFAN_r24"), 0),
    ("r26 stamp present", out.count("w61_S3_GFAN_r26"), 4),
    ("AZ bracket says FOUR", out.count("this proof's FOUR imports"), 1),
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
print(f"delta vs r24: {len(out)-len(src):+d} chars")
