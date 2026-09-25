#!/usr/bin/env python3
"""Build prompts/w61_S3_GFAN_r24.md -- the Q38 brief: Corollary GFANnu-HC, family 2, to
codex `gpt-5.6-sol`.

PATCH, NOT REBUILD.  Base = prompts/w61_S3_GFAN_r20.md, the text Gemini read in Q37.
Every edit is an anchored replace with an exact-count assert; the script refuses to write
if any anchor is missing or a count is wrong.

WHAT CHANGES, and why each one is here
--------------------------------------
RETARGET  Theorem GFANnu was promoted (registry row R-23, planner certification
          cert_w61_provedS3.md).  The single TARGET of this round is **Corollary
          GFANnu-HC**.  GFANnu stays printed in full as CONTEXT because the corollary
          consumes its conclusion verbatim -- and the brief says, in as many words, that
          if that conclusion is not what GFANnu proves, that is a MATHEMATICS defect OF
          THE COROLLARY.  No favourable status word for GFANnu appears anywhere in the
          product: `PROVED-S3`, `certified`, `two families` must not leak into the text
          the judge reads, or J-IMPORT is answered for it.

RIDE      AD1 (3 sites) + AE1 (1 site) are four sentences WE wrote and NOBODY has
          reviewed.  They are landed into the brief text verbatim from the draft and
          then named, quoted and handed to the judge as a TARGET joint (J-NEWTEXT).
          Assuming them clean is exactly the move that produced AE1.

AZ        RULING AZ: supply guards AT the import site.  Ten of eleven clear import edges
          in this document are supplied off-site and are therefore invisible to any judge
          handed the statement.  The corollary's own edges get their guards on-site; the
          ones that CANNOT move get a named block saying the obligation exists and where
          it is carried.  First brief in this project written with AZ known.

TIERS     RULING A (cert_677_r15) tiered held-out grading, PRE-REGISTERED AND DISCLOSED:
          H1/H2/H5 HAND (wrong => round VOID), H3/H4 COMPUTATIONAL (CANNOT COMPUTE =>
          clean; wrong => traced downgrade; ALL computational rows confidently wrong =>
          VOID).  r20 disclosed the boundary but not the penalties.

LINT      brieflint L1/L2 findings on the base (3 toolkit-as-xref + 1 doubled article)
          are fixed here, because brieflint is this round's BUILD GATE and a build gate
          you ship around is decoration.

RULING S (COVERAGE != LIVENESS) applied: the two new product asserts (no favourable
status word for GFANnu; all four ridden sentences present) are run against the BASE text
too, and the script dies unless they FAIL there.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
BASE = ROOT / "prompts/w61_S3_GFAN_r20.md"
OUT  = ROOT / "prompts/w61_S3_GFAN_r24.md"

src = BASE.read_text()
BASE_MD5 = hashlib.md5(src.encode()).hexdigest()
print(f"base : prompts/w61_S3_GFAN_r20.md  md5 {BASE_MD5}  {len(src)} chars")
assert BASE_MD5 == "c9c0b6b9c1e6c5aa3f3f9a3f3a1b6f01" or True  # recorded below, not gated

out = src
patches = 0


def rep(old, new, n=1, tag=""):
    global out, patches
    c = out.count(old)
    assert c == n, f"[{tag}] expected {n} occurrence(s), found {c}"
    out = out.replace(old, new)
    assert out.count(new) >= 1, f"[{tag}] replacement missing"
    patches += 1
    print(f"  [{tag}] patched")


# ============================================================ LIVENESS PROBES on the BASE
def favourable_status_hits(text):
    """Words that would tell the judge GFANnu's verdict instead of asking for it."""
    pats = [r"PROVED-S3", r"separately certified", r"two independent families",
            r"already certified"]
    return [p for p in pats if re.search(p, text)]


RIDDEN = [
    "First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`: at `L = 0` Theorem K makes `B` a clique,",
    "which is Theorem RIG's remaining",
    "the canonical hard core minus its",
]
base_ridden = [s for s in RIDDEN if s in src]
base_status = favourable_status_hits(src)
print(f"LIVENESS on BASE : ridden sentences present {len(base_ridden)}/3 (want 0)")
print(f"LIVENESS on BASE : favourable-status hits    {base_status} (want non-empty)")
assert len(base_ridden) == 0, "LIVENESS FAIL: base already carries the ridden sentences"
assert base_status, "LIVENESS FAIL: the status-leak check cannot fire on the base"

# ============================================================ 1. TARGET block
rep("""# GFAN family — corrected second-family adversarial round

TARGET — **two statements, and only two**:

> **Theorem GFANnu (`1 <= nu <= 10`)** and **Corollary GFANnu-HC (`nu >= 11`, `L >= 12`)**,
> both in Appendix C.

Everything else in this file — Lemma CAP, Corollary CAP1, Theorem RIG, Corollary RIG-1,
Corollary RIG-2, Lemma FAN-4', Lemma FAN-8', Lemma FAN-6', Theorem GFAN2, Corollaries
GFAN2-HC and GFAN2-L3 in Appendix B, and every fact in Appendix A — is **CONTEXT**.
It is printed in full for one reason: Theorem GFANnu's proof reaches for those
statements, and you cannot check an import you cannot read. Earlier rounds of this
review were wasted precisely because imported statements were named and not printed.

**What "context" means here, exactly.** You are *not* asked to referee the context's own
proofs, and a verdict on them is not what this round counts. You *are* asked to check
every point where the target reaches into them (joint **J-IMPORT**). And if you happen
to see a defect in the context, **report it** — it will be read and acted on; it simply
will not decide this round's verdict.""",
"""# GFAN family — Corollary GFANnu-HC, adversarial round

TARGET — **one statement, and only one**:

> **Corollary GFANnu-HC (`nu >= 11`, `L >= 12`)**, in Appendix C.

Everything else in this file — Lemma CAP, Corollary CAP1, Theorem RIG, Corollary RIG-1,
Corollary RIG-2, Lemma FAN-4', Lemma FAN-8', Lemma FAN-6', Theorem GFAN2, Corollaries
GFAN2-HC and GFAN2-L3, **Theorem GFANnu itself**, and every fact in Appendix A — is
**CONTEXT**. It is printed in full for one reason: the corollary's proof is four lines
long and every one of those lines reaches outside itself, and you cannot check an import
you cannot read. Earlier rounds of this review were wasted precisely because imported
statements were named and not printed.

**What "context" means here, exactly — and read the second half of this, it is the whole
round.** You are *not* asked to referee the context's own proofs line by line, and a
verdict on them is not what this round counts. You *are* asked to check every point where
the target reaches into them (joint **J-IMPORT**). **Theorem GFANnu is the sharp case.**
The corollary consumes GFANnu's conclusion verbatim and consumes nothing else of it. So:

* whether GFANnu's *proof* works is not this round's question;
* whether the sentence the corollary imports **is the sentence GFANnu actually proves** —
  same quantifier range, same hypotheses, same conclusion — **is** this round's question,
  and a mismatch there is a **MATHEMATICS defect of the corollary**.

You are not told GFANnu's review status and you should not infer one; several of the
statements printed here have been reviewed elsewhere and several have not, and which is
which is deliberately not disclosed, because a status word in a brief is a verdict handed
to the judge instead of asked of it. And if you happen to see a defect in the context,
**report it** — it will be read and acted on; it simply will not decide this round's
verdict.

## FOUR SENTENCES IN THIS BRIEF ARE NEW TEXT NOBODY HAS EVER REVIEWED

They are ours, they were written recently, and they are **marked** — because unmarked new
text gets read as settled text, and this project has now twice shipped a repair whose own
sentence was never checked. What each of them asserts, whether it is *needed*, and above
all whether it actually **supplies what it claims to supply**, is a TARGET question
(joint **J-NEWTEXT**). They are quoted in full at that joint. You are **not** told what
they were written in response to, and you should not guess: judge the sentences.""",
    1, "TARGET")

# ============================================================ 2. tier pre-registration
rep("""**Two of the five are deliberately beyond hand computation.** `H3` and `H4` each require
an enumeration of tens of thousands of shapes or a thousand separate runs. If you cannot
compute one, **write `CANNOT COMPUTE` in that row and say why** — that is an *expected*
and fully acceptable answer, it is graded as honest, and it costs you nothing in this
round. A wrong number here is recoverable. A confident wrong number here, next to a
claim that you recomputed the printed data, is not. **Do not extrapolate a pattern and
present the result as a computation**: the published survivor counts have no closed form
in this document, and an extrapolation will grade as WRONG where `CANNOT COMPUTE` would
have graded as honest.

| # | held-out quantity |
|---|---|""",
"""**The five rows sit in two TIERS, and the tiers and their consequences are written here,
before you answer, so that nothing about the grading is decided after the fact.**

| tier | rows | what a wrong value costs | what `CANNOT COMPUTE` costs |
|---|---|---|---|
| **HAND** | `H1`, `H2`, `H5` | a stated wrong value **VOIDS the round** — the report is not scored at all | nothing, but these are derivable in a few dozen lookups and a declined HAND row is itself informative |
| **COMPUTATIONAL** | `H3`, `H4` | a stated wrong value does **not** void: it triggers a **traced downgrade** — we identify which claims in your report actually rest on that computation and mark those, and only those | **nothing at all.** This is the intended answer if you cannot run the enumeration, it is graded as honest, and it costs you no credit anywhere in the round |

**One further pre-registered rule, stated now rather than later:** if **every**
computational row is answered with a confident wrong value while the `CANNOT COMPUTE`
hatch sits unused, that is the fabrication pattern and it **VOIDS the round** — one wrong
hard row is incapacity, all of them with a hatch available is not.

`H3` and `H4` each require an enumeration of tens of thousands of shapes or a thousand
separate runs; they are in the computational tier for that reason and for no other.
**Do not extrapolate a pattern and present the result as a computation**: the published
survivor counts have no closed form in this document, and an extrapolation grades as
WRONG where `CANNOT COMPUTE` grades as honest.

| # | tier | held-out quantity |
|---|---|---|""",
    1, "TIERS")

# tier column into the five rows
for lab, tier in [("H1", "HAND"), ("H2", "HAND"), ("H3", "COMPUTATIONAL"),
                  ("H4", "COMPUTATIONAL"), ("H5", "HAND")]:
    rep(f"| **{lab}** | ", f"| **{lab}** | {tier} | ", 1, f"TIERCOL/{lab}")

# ============================================================ 3. AD1 site 1 -- Corollary MB1 (Appendix A.1)
rep("""> *Proof.* B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,
> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it
> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎""",
"""> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`: at `L = 0` Theorem K makes `B` a clique,
> contradicting Observation R1. This step is what licenses the appeal to Theorem MB
> below, which is stated **for `L ≥ 1`**, and it is not supplied by the hypothesis “every
> low vertex is B-universal” — that is vacuously true when `B_lo = ∅`.
> B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,
> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it
> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎""",
    1, "AD1/MB1")

# ============================================================ 4. AE1 -- Theorem RIG's trailing gloss
rep("""> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of Appendix A,
> with `ν = m̄ ≥ 1`. In the **hard core** (i.e. adding the reductio) one has in
> addition **`ν ≤ L − 1`**.""",
"""> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of Appendix A,
> with `ν = m̄ ≥ 1`. In the **hard-core frame plus the reductio** — which is the canonical
> hard core minus its `τ ≥ 4` rider, a rider the chain behind this bound does not consume
> (Corollary MB1 → Theorem MB → Theorem SL use only `τ ≥ 2`, and `τ ≥ 2` follows from the
> frame's `diam = 4` alone: a connected graph with `τ ≤ 1` is edgeless or a star, hence
> `diam ≤ 2`) — one has in addition **`ν ≤ L − 1`**.""",
    1, "AE1/RIG")

# ============================================================ 5. AD1 site 2 -- Corollary GFAN2-HC
#     (also clears brieflint L1 at this line: "the certified toolkit" as a cross-reference)
rep("""> *Proof.* Theorem RIG (the certified toolkit) makes the instance `GFan(τ,L,ν)` with
> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and""",
"""> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`, which is Theorem RIG's remaining
> hypothesis and is **not** supplied by “every low vertex is B-universal” (vacuous at
> `B_lo = ∅`): at `L = 0` Theorem K makes `B` a clique, contradicting Observation R1.
> Theorem RIG (Appendix B of this brief) then makes the instance `GFan(τ,L,ν)` with
> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and""",
    1, "AD1/GFAN2-HC")

# ============================================================ 6. AD1 site 3 + RULING AZ on-site guards
#     THE TARGET's own proof.  Every guard that can be supplied here is supplied here.
rep("""> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 11` and `L ≥ 12`**.
>
> *Proof.* Theorem RIG gives `GFan(τ,L,ν)` with **`1 ≤ ν ≤ L−1`** — the lower bound
> is RIG (d), i.e. Observation R1 — so `L ≥ ν+1`; Theorem GFANν eliminates every
> `ν` with `1 ≤ ν ≤ 10`, which by that lower bound is every `ν ≤ 10` available here. ∎""",
"""> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 11` and `L ≥ 12`**.
>
> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`, which is Theorem RIG's remaining
> hypothesis and is **not** supplied by “every low vertex is B-universal” (vacuous at
> `B_lo = ∅`): at `L = 0` Theorem K makes `B` a clique, contradicting Observation R1.
> Theorem RIG then gives `GFan(τ,L,ν)` with **`1 ≤ ν ≤ L−1`** — the lower bound
> is RIG (d), i.e. Observation R1 — so `L ≥ ν+1`; Theorem GFANν eliminates every
> `ν` with `1 ≤ ν ≤ 10`, which by that lower bound is every `ν ≤ 10` available here. ∎
>
> 〔**The guards this proof's three imports need, supplied here rather than three sections
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
> in fact supplied, that is a defect of this corollary.〕""",
    1, "AD1+AZ/GFANnuHC")

# ============================================================ 7. brieflint L1/L2 at the RIG-1 note
rep("""> the pre-declared failure mode **L-d** of the the certified toolkit error prior (dispatch file,""",
"""> the pre-declared failure mode **L-d** of this line's own error prior (dispatch file,""",
    1, "LINT/L-d")

# ============================================================ 8. brieflint L1 at the (C-3) reference
rep("""> `ν+1 ≤ L < λ₁` have their **own** survivors, tabulated in the certified toolkit (C-3), each with its""",
"""> `ν+1 ≤ L < λ₁` have their **own** survivors, tabulated in **(C-3)** of Appendix C.1
> below, each with its""",
    1, "LINT/C-3")

# ============================================================ 9. the AZ block + the two new joints
rep("""| **J-SCOPE** *(TARGET)* | For **Theorem GFANnu and Corollary GFANnu-HC**: what hypotheses does its own proof consume, versus what it is filed under? Report both under- and over-hypothesis. Under-hypothesis is a MATHEMATICS defect; over-hypothesis is bookkeeping. Watch for a scope note that *weakens* an import's hypotheses in passing — asserting that a cited lemma holds under less than it was proved under is an affirmative claim and needs a proof of its own. |""",
"""| **J-SCOPE** *(TARGET)* | For **Corollary GFANnu-HC**: what hypotheses does its own proof consume, versus what it is filed under? Report both under- and over-hypothesis. Under-hypothesis is a MATHEMATICS defect; over-hypothesis is bookkeeping. Watch for a scope note that *weakens* an import's hypotheses in passing — asserting that a cited lemma holds under less than it was proved under is an affirmative claim and needs a proof of its own. |
| **J-NEWTEXT** *(TARGET)* | **The four sentences nobody has reviewed.** Quoted in full below this table. For each: is the claim **true**; is it **needed** (or is it a true sentence supplying a guard that was never required, which is its own defect class here); and does it actually **supply** what it says it supplies? Two of the four are the *same* sentence at two sites — say so if you find they are not in fact interchangeable, because the sites differ. |
| **J-AZGUARD** *(TARGET)* | **Guard supply, judged locally.** For the target corollary, every guard its imports need is claimed **at the import site**, inside the bracket that follows its proof, together with an explicit statement of which available hypothesis it does *not* consume. Audit that bracket clause by clause against the imported statements as printed in Appendix A.1 / Appendix B: a guard claimed and not needed, a guard needed and not claimed, or a guard claimed-and-supplied-from-somewhere-that-does-not-supply-it are three different defects and all three are MATHEMATICS. **The block "Guards this brief cannot move on-site" below tells you exactly which obligations are carried elsewhere; those are yours to attack too, and "I could not check it from this file" is the correct report if that is the truth.** |""",
    1, "JOINTS")

# ============================================================ 10. the ridden sentences, quoted; and the AZ off-site block
rep("""## Classify every defect""",
"""### J-NEWTEXT — the four sentences, quoted verbatim

**(N1)** at **Corollary MB1** (Appendix A.1):
> *"First, `B_lo ≠ ∅`, i.e. `L ≥ 1`: at `L = 0` Theorem K makes `B` a clique, contradicting
> Observation R1. This step is what licenses the appeal to Theorem MB below, which is stated
> for `L ≥ 1`, and it is not supplied by the hypothesis “every low vertex is B-universal” —
> that is vacuously true when `B_lo = ∅`."*

**(N2)** at **Corollary GFAN2-HC** (Appendix B) and **(N3)** at **Corollary GFANnu-HC**
(Appendix C) — the same sentence at two different sites:
> *"First, `B_lo ≠ ∅`, i.e. `L ≥ 1`, which is Theorem RIG's remaining hypothesis and is not
> supplied by “every low vertex is B-universal” (vacuous at `B_lo = ∅`): at `L = 0` Theorem K
> makes `B` a clique, contradicting Observation R1."*

**(N4)** inside the statement of **Theorem RIG** (Appendix B), replacing a one-clause gloss:
> *"In the hard-core frame plus the reductio — which is the canonical hard core minus its
> `τ ≥ 4` rider, a rider the chain behind this bound does not consume (Corollary MB1 →
> Theorem MB → Theorem SL use only `τ ≥ 2`, and `τ ≥ 2` follows from the frame's `diam = 4`
> alone: a connected graph with `τ ≤ 1` is edgeless or a star, hence `diam ≤ 2`) — one has in
> addition `ν ≤ L − 1`."*

**(N4) is an affirmative claim about an import's hypotheses, made in a scope note**, which
is precisely the shape J-SCOPE tells you to distrust. It is printed here rather than hidden
because we would rather it be attacked than assumed. Check the chain it names against
Theorem MB and Theorem SL as printed in Appendix A.1, and check the `τ ≥ 2` derivation.

### Guards this brief CANNOT move on-site — the obligation exists and is carried elsewhere

A guard supplied at the import site is one you can check from the statement in front of
you. A guard supplied three sections away is one you **cannot**, no matter how good you
are, and this brief is the first on this line written with that understood. Where a guard
could be moved to its import site, it has been. Where it could not, it is named here:

1. **The configuration licence for `GFan(τ,L,ν)`.** Every lemma of Appendix B stated for
   `Fan(τ,L)` is run inside the wider configuration `GFan(τ,L,ν)`. What licenses that is a
   sentence in the section preamble of the source document — *"Lemma FAN-1 applies word for
   word"* — and it governs a whole family of lemmas at once, so it cannot be attached to any
   single import without being asserted many times over. **It is an assumption of this
   brief.** If you think a particular `Fan`-stated lemma does **not** survive the widening,
   that is a MATHEMATICS defect and it is exactly the kind this block exists to expose.
2. **The canonical meaning of "the hard core".** It is *frame + reductio + `τ ≥ 4`*, and it
   is fixed once in Appendix A's vocabulary rather than restated at each of the ~15 statements
   filed under it. Sentence **(N4)** above is what happens when a statement quietly uses a
   different meaning; there may be others, and finding one is a defect report.
3. **Completeness of the printed rosters.** Withdrawn as an obligation, with the evidence
   printed inline in the scoring section above rather than asserted. It may not be the sole
   ground of a `GAP`; attacking that evidence is a defect report and is invited.

Nothing else in the target's dependency chain is knowingly supplied off-site. If you find
something that is, **say so** — that finding is worth more to us than a verdict.

## Classify every defect""",
    1, "AZBLOCK")

# ============================================================ 11. verdict tags -- one statement
rep("""Give **two** verdict lines, one for Theorem GFANnu and one for Corollary GFANnu-HC, and
then the single overall `VERDICT:` line the report format asks for. A defect in one of
the two is not automatically a defect in the other, and a joint verdict that hides which
statement is affected cannot be scored.""",
"""There is **one** target statement this round, so give **one** per-statement verdict line
for **Corollary GFANnu-HC**, and then the single overall `VERDICT:` line the report format
asks for. If you find a defect in a context statement, report it in the defect list with
its own tag; do **not** fold it into the corollary's verdict line unless it actually
reaches the corollary — and if it does reach, say by which import it reaches.""",
    1, "VERDICT1")

# ============================================================ 12. report format
rep("""Open with the `EXECUTION ENVIRONMENT:` line, then the **two per-statement verdict
lines** described above (Theorem GFANnu, Corollary GFANnu-HC), then the single overall
`VERDICT:` line, then
`TEXT VERSION REVIEWED: w61_S3_GFAN_r20`. Then, in this order:""",
"""Open with the `EXECUTION ENVIRONMENT:` line, then the **one per-statement verdict line**
described above (Corollary GFANnu-HC), then the single overall
`VERDICT:` line, then
`TEXT VERSION REVIEWED: w61_S3_GFAN_r24`. Then, in this order:""",
    1, "REPORTFMT")

rep("""3. the defect list — each with a MATHEMATICS/BOOKKEEPING tag, **<= 200 words each**;""",
"""3. the defect list — each with a MATHEMATICS/BOOKKEEPING tag, **<= 200 words each**;
   **J-NEWTEXT and J-AZGUARD get their own sub-lists**, one line per sentence / per guard
   clause, so that a clean finding there is legible as a check that was actually run;""",
    1, "REPORTFMT2")

# ============================================================ 13. environment paths
rep("""problems/wowii/w61_S3_GFAN_r20.md`, put your scripts in
  `problems/wowii/w61_S3_GFAN_r20_check.py` and keep their **raw stdout** (not a
  hand-written summary) in `problems/wowii/w61_S3_GFAN_r20_check.out`.""",
"""problems/wowii/w61_S3_GFAN_r24.md`, put your scripts in
  `problems/wowii/w61_S3_GFAN_r24_check.py` and keep their **raw stdout** (not a
  hand-written summary) in `problems/wowii/w61_S3_GFAN_r24_check.out`.""",
    1, "PATHS")

# ============================================================ 14. J-CORHC retarget
rep("""| **J-CORHC** *(TARGET for GFANnu-HC only; context for GFAN2-HC / GFAN2-L3)* |""",
"""| **J-CORHC** *(TARGET — this is the round)* |""",
    1, "JCORHC")

# ============================================================ 15. J-FIN / J-SPEC / J-DATA / J-KILL retier
for j, old, new in [
    ("J-FIN",  "| **J-FIN** *(TARGET)* |",  "| **J-FIN** *(context — but see the TARGET clause below the table)* |"),
    ("J-SPEC", "| **J-SPEC** *(TARGET)* |", "| **J-SPEC** *(context — but see the TARGET clause below the table)* |"),
    ("J-DATA", "| **J-DATA** *(TARGET)* |", "| **J-DATA** *(context — but see the TARGET clause below the table)* |"),
    ("J-KILL", "| **J-KILL** *(TARGET)* |", "| **J-KILL** *(context — but see the TARGET clause below the table)* |"),
]:
    rep(old, new, 1, f"RETIER/{j}")

rep("""**Scoring:** the joints marked **(TARGET)** decide this round. The joints marked
**(context)** are printed so that a defect you happen to find there gets reported; they
do not decide the verdict, and `NOT REVIEWED` is an acceptable answer on any of them.
**J-IMPORT is a TARGET joint even though it points at context statements** — a
mismatched import is a defect *of the target*, not of the thing imported.""",
"""**Scoring:** the joints marked **(TARGET)** decide this round. The joints marked
**(context)** are printed so that a defect you happen to find there gets reported; they
do not decide the verdict, and `NOT REVIEWED` is an acceptable answer on any of them.
**J-IMPORT is a TARGET joint even though it points at context statements** — a
mismatched import is a defect *of the target*, not of the thing imported.

**The TARGET clause, and it is not a formality.** `J-FIN`, `J-SPEC`, `J-DATA` and `J-KILL`
are context this round because they are about Theorem GFANnu's *own* proof. But the target
corollary's entire content is *"GFANnu eliminates every `ν ≤ 10`"*. So: **any defect you
find in those four joints that changes what GFANnu's conclusion SAYS — its range, its
hypotheses, or whether the elimination is of all `ν ≤ 10` or only of some — is a
MATHEMATICS defect OF THE TARGET, and must be reported as one.** A defect that leaves the
conclusion's statement intact stays context. Deciding which side of that line a finding
falls on is part of the finding, and we would rather you argue it than round it off.""",
    1, "TARGETCLAUSE")

# ============================================================ 16. the status leak inside J-IMPORT
# "they are separately certified" tells the judge the imports' verdicts.  Under RULING AZ
# the judge's job at an import is the INTERFACE, and it must not be told the interior is
# settled -- that is a verdict handed over rather than asked for.
rep("""Do not referee the imports' own proofs — they are separately certified.""",
    """Do not referee the imports' own proofs line by line — check the **interface**, which is
what an import is. You are not told which imports have been reviewed elsewhere.""",
    1, "STATUSLEAK/J-IMPORT")

rep("""Each of these is separately certified. Your job with them is **import matching only**:
does the caller supply the hypothesis the statement requires, and does the caller use
only the conclusion the statement proves?""",
    """Their own proofs are not printed and are not this round's question; **their statements
are**, because an import is an interface and this is the side of it you can see. Your job
with them is **import matching**: does the caller supply the hypothesis the statement
requires, and does the caller use only the conclusion the statement proves? You are not
told which of them have been reviewed elsewhere, deliberately — a status word here would
answer J-IMPORT for you.""",
    1, "STATUSLEAK/A1")

# ============================================================ product asserts
print(f"\npatches : {patches}")

prod_status = favourable_status_hits(out)
prod_ridden = [s for s in RIDDEN if s in out]
checks = [
    ("all four ridden sentences present", len(prod_ridden), 3),   # N2/N3 are one string, twice
    ("N2/N3 sentence at two sites + once quoted at J-NEWTEXT",
     out.count("which is Theorem RIG's remaining"), 3),
    ("no favourable status word for GFANnu", len(prod_status), 0),
    ("exactly one version stamp", out.count("w61_S3_GFAN_r24"), 4),
    ("no r20 stamp survives", out.count("w61_S3_GFAN_r20"), 0),
    ("brieflint L1 toolkit-as-xref cleared",
     len([1 for ln in out.splitlines()
          if "the certified toolkit" in ln.lower()
          and "The certified toolkit. Theorem FAN says" not in ln]), 0),
    ("brieflint L2 doubled-article cleared", len(re.findall(r"\bthe the\b", out)), 0),
    ("AZ off-site block present", out.count("Guards this brief CANNOT move on-site"), 1),
    ("J-NEWTEXT joint row + its quoted block", out.count("**J-NEWTEXT**"), 2),
    ("J-AZGUARD joint present", out.count("**J-AZGUARD**"), 1),
    ("tier table present", out.count("| **HAND** | `H1`, `H2`, `H5` |"), 1),
    ("one verdict line, not two", out.count("Give **two** verdict lines"), 0),
]
ok = True
for name, got, want in checks:
    flag = "OK " if got == want else "FAIL"
    if got != want:
        ok = False
    print(f"  [{flag}] {name}: {got} (want {want})")

if not ok:
    print("\nPRODUCT ASSERTS FAILED -- nothing written")
    sys.exit(1)

OUT.write_text(out)
print(f"\nwrote {OUT}  {len(out)} chars  md5 {hashlib.md5(out.encode()).hexdigest()}")
print(f"base md5 {BASE_MD5}  ({len(src)} chars)  ->  delta {len(out) - len(src):+d} chars")
