#!/usr/bin/env python3
"""Assemble prompts/w61_S3_GFANNU_qwen.md — the DIFF-SCOPED J-GFANNU re-round brief.

Round 12.  Q25's J-GFANNU came back GAP for a briefing reason: the nu=3..6 enumeration
was cited by filename and never pasted, so the judge could not reproduce the decisive
column.  Repair Z2 (draft section 7.22 (c)) puts the whole finite case list in the text.
This brief is the re-round on that new text.

Construction, same discipline as w61_r10_build_spark_brief.py:
  * protocol block reused from the Q25 GFAN brief (refute-first, read restriction,
    T12 control, report format),
  * the text under review pulled LIVE from the draft, with every repair-provenance
    annotation stripped and every reference to a previous judge removed, so this judge
    reads corrected mathematics in the author's voice and is not told what the last
    judge found,
  * diff-scoped: only Theorem GFANnu's finiteness + enumeration, its four imports
    (stated, not refereed) and Lemma FAN-6' (whose bracket changed).
"""
import re
import pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
draft = (ROOT / "notes/proofs/wowii61_draft.md").read_text().splitlines(keepends=True)


def slice_between(start_pred, end_pred, lines=None):
    lines = lines if lines is not None else draft
    i = next(k for k, l in enumerate(lines) if start_pred(l))
    j = next(k for k, l in enumerate(lines) if k > i and end_pred(l))
    return "".join(lines[i:j])


def strip_annotations(text):
    """Remove repair-provenance brackets and any pointer to the review record."""
    # nested-bracket-safe removal of 〔**Repair X 已落地** ... 〕 blocks
    out = []
    i = 0
    while i < len(text):
        if text.startswith("〔**Repair", i) or text.startswith("〔**Repair", i):
            depth = 0
            j = i
            while j < len(text):
                if text[j] == "〔":
                    depth += 1
                elif text[j] == "〕":
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            i = j
            continue
        out.append(text[i])
        i += 1
    text = "".join(out)
    # tidy the debris the removals leave behind
    text = re.sub(r"[ \t]*\n(>\s*\n)+(?=>\s*\n)", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r">\s*\n>\s*$", "", text)
    return text


# ---------------------------------------------------------------- draft slices
fan4p = slice_between(lambda l: l.startswith("> **Lemma FAN-4′ (residue mass)"),
                      lambda l: l.startswith("> **Lemma FAN-8′"))
fan8p = slice_between(lambda l: l.startswith("> **Lemma FAN-8′ (escape bound)"),
                      lambda l: l.startswith("> **Lemma FAN-6′"))
fan6p = slice_between(lambda l: l.startswith("> **Lemma FAN-6′ (backward induction"),
                      lambda l: l.startswith("### B. Theorem GFAN2"))
mb1 = slice_between(lambda l: l.startswith("> **Corollary MB1 (a floor on L)"),
                    lambda l: l.strip() == "")
secD = slice_between(lambda l: l.startswith("### D. **Lemma TAIL, and the elimination"),
                     lambda l: l.startswith("## §7.14 owner-w61 round 5"))
embed = slice_between(lambda l: l.startswith("### (c) Repair Z2 in full"),
                      lambda l: l.startswith("### (d) Registry row R-14"))

fan6p = strip_annotations(fan6p)
# dangling cross-references: rewrite self-containedly
fan6p = fan6p.replace(
    "Repair F4 already\n> corrected the parenthetical that misdiagnosed why `1+1` escapes: the reason is\n"
    "> that its maximum is not unique.",
    "The reason `1+1` escapes is that its\n> maximum is not unique — not that a `0` entry is present.")
secD = strip_annotations(secD)
embed = strip_annotations(embed)

# secD: drop the trailing status line (it names the review record) and the GFAN2 pointer
secD = re.sub(r"\*Status 〔\*\*updated.*?\*\n", "", secD, flags=re.S)
# rewrite the Z2 pointer inside secD into the author's own voice
secD = secD.replace(
    "**§7.22 (c) now\n> carries", "**Appendix B below now\n> carries")
secD = re.sub(r"§7\.22 \(c\)", "Appendix B", secD)
secD = re.sub(r"\s*〔\*\*Repair Z2 已落地\*\*.*?〕\s*", "\n>\n", secD, flags=re.S)
secD = secD.replace("— which with §7.12 D\nwould reduce", "— which\nwould reduce")

# embed: strip the adjudication framing; it is data, not a reply to anyone
embed = re.sub(r"^### \(c\) Repair Z2 in full.*$",
               "## Appendix B — the `ν ≤ 6` enumeration, in full",
               embed, count=1, flags=re.M)
embed = re.sub(r"the specification the\s*\njudge asked for",
               "the specification a reader needs", embed)
embed = re.sub(r"\bjudge\b", "reader", embed)
embed = re.sub(r"\*\(Q25's (judge|reader) derived this identity.*?\)\*", "", embed,
               flags=re.S)
embed = re.sub(r"§7\.13 D", "Appendix A", embed)
embed = re.sub(r"§7\.22 \(c\)", "this appendix", embed)
embed = re.sub(r"§7\.8 A firewall, Repair V3,", "no-simulation-substitutes-for-proof firewall", embed)
embed = re.sub(r"the judge (asked for|had to guess and now does not)", r"a reader needs", embed)
embed = embed.replace("Five conventions, each of which\na reader needs:",
                      "Five conventions, all of which a reader needs and none of which\n"
                      "should have to be guessed:")
embed = re.sub(r"\*\*\(c-6\) The honest-demarcation note, upgraded\.\*\*.*?(?=\*\*\(c-7\))",
               "", embed, flags=re.S)
embed = re.sub(r"\(c-(\d)\)", r"(B-\1)", embed)
embed = embed.replace("§7.13 D's bracket is replaced by:", "")

HEADER = r"""# Theorem GFANν (`ν ≤ 6`) — adversarial round on the ENUMERATION (Qwen3.8-Max)

**Driver note (do NOT act on this box; it is addressed to the operator, not to you).**
Queue row **Q30**. **Diff-scoped and deliberately small** (~40 KB, versus the 138 KB
GFAN-family brief that drew the slider CAPTCHA twice) — paste it as ONE message, slow
pacing per `notes/web_model_ops.md`. Confirm the model badge reads Qwen3.8-Max before
sending. Family note for the ledger: this round is **family 1** for Theorem GFANν
(whose text is new this round) and does **not** supply the second family for Theorem
RIG / Theorem GFAN2 / the CAP and primed-FAN lemmas — those need a non-Qwen family.

TARGET: **THEOREM GFANν (`ν ≤ 6`)** and **COROLLARY GFANν-HC** — specifically the
finiteness argument and the enumeration that decides `ν = 3…6`.

## Who you are

You are an INDEPENDENT adversarial reviewer. You are not the author and have no stake
in the result. Your job is to find defects. A CLEAN verdict that misses a real defect
is the worst outcome; a false alarm you retract after computing is fine. Everything
below is under review, including every line labelled PROVED.

## Read restriction — a hard constraint, not a preference

Everything you need is in this file. Treat it as the complete, authoritative text.
Do **not** search the web, and do not ask for files: if you believe a joint cannot be
settled from what is written here, **say so and mark that joint UNRESOLVED** — that is
a useful finding, not a failure. Do not guess a convention; report the ambiguity.

## Why this target, and what turns on it

Theorem GFANν is the statement that empties an entire structural layer of the problem
for every `ν ≤ 6`. It is a **computer-assisted** proof: four hand-proved bounds make
the case list finite, and a finite check inside that list finishes it. A previous
version of this write-up cited the finite check by filename instead of printing it,
which made the decisive column impossible to verify without the author's files. That
is fixed: **Appendix B prints the whole finite case list**, together with the
specification that generates it. Your round is a round on *that* text.

So the question this round has to answer is not "did the author's script run" — it is:

* is the case list **finite for the reason claimed**, and is the case split
  **disjoint and exhaustive**?
* is the **specification** in Appendix B (B-1) precise enough that two people
  implementing it independently would enumerate the *same* set of shapes?
* do the **printed data** actually say what the theorem claims they say — recompute
  them?
* and does **Lemma FAN-6′** really kill every printed survivor?

## REFUTE FIRST — the required order of work

1. **Try to refute Theorem GFANν by computation.** Implement Havel–Hakimi yourself
   from the specification in Appendix B (B-1). **Calibrate your implementation before
   you use it** — e.g. against `residue(K₂) = 1` and `residue(Cₙ) = ⌈n/3⌉` for
   `n = 3…9` — and say in the report what you calibrated on. Then regenerate the
   finite list for at least `ν = 1, 2, 3, 4` (and `ν = 5, 6` if you can) and check
   whether ANY admissible shape clears in exactly `L` steps and is **not** killed by
   Lemma FAN-6′. **One such shape refutes the theorem.** Reuse none of the printed
   numbers while doing this; compare only afterwards.
2. **Then try to refute the finiteness argument on paper**: find a `(ν, L, E, λ)`
   with `L ≥ ν+1` that the three-way case split does not cover, or that two branches
   both claim, or a value of `λ₁` outside the range the argument assumes.
3. **Then, and only then**, review the joints below line by line.
4. Report what you could NOT check. That section is mandatory.

## Named joints — give each an explicit verdict

| joint | what to check |
|---|---|
| **J-FIN** | The finiteness argument. The case list is claimed finite for each `ν` because of four imports: FAN-4′ (residue total `2ν−E`, `C`-part `{L+e_c}`), FAN-8′ (`E ≥ 1 ⟹ L ≤ 2ν−E`), MB1 (`L ≥ ν+1`) and TAIL (`E = 0`, `L ≥ λ₁` ⟹ criterion on `λ` alone). Is the resulting split into `E=0/L≥λ₁`, `E=0/ν+1≤L<λ₁`, `E≥1` **disjoint** and **exhaustive**? Is `λ₁ ≤ 2ν` justified? Does anything force `E ≤ ν−1`, and is that used consistently? |
| **J-SPEC** | Appendix B (B-1). Are the five conventions sufficient to pin the enumerated set exactly? In particular: is the unlabelled/multiset reduction legitimate; is the zero-inertness claim true (test it); is the "no graphicality filter needed" argument valid, and does its monotonicity run in the direction the conclusion needs; is "clears in exactly `L` steps" unambiguous including the abort cases? |
| **J-E0** | Appendix B (B-2). Recompute `s₀(λ)` for the partitions of `2ν`, `ν ≤ 6`, yourself. Does the printed column match? Is `[2ν]` really the **only** survivor at every `ν ≤ 6`? Does the claim depend on `L` anywhere it should not? |
| **J-BND** | Appendix B (B-3). The boundary rows `ν+1 ≤ L < λ₁`. Are the pair counts `0,1,3,7,14,26` right? Is the survivor list complete? |
| **J-COUNT** | Appendix B (B-4). The closed form `S(ν) = Σ_{E=1}^{ν−1}(ν−E)·p(E)·p(2ν−E)`. Derive it yourself from the parameter ranges. Does the "`L+1 > E`, so all `p(E)` escape partitions occur" step hold at the extremes? Do you get `0,3,24,110,397,1211`? |
| **J-SURV** | Appendix B (B-4). The roster of `72` surviving `E ≥ 1` rows. Regenerate it. Is it complete — does your run produce any survivor that is not printed? Is any printed row **not** actually a survivor? |
| **J-KILL** | Lemma FAN-6′ against the printed survivors. For each of the `9` `E=0`/boundary survivors and the `72` `E≥1` survivors, does the certificate `(w, 2nd)` satisfy the lemma's hypothesis (unique maximum `w ≥ 1`, second-largest `≤ w−2`)? Watch the boundary cases `(w,2)` with `w = 4` and `(w,1)` with `w = 3`. |
| **J-FAN6P** | Lemma FAN-6′ itself (Appendix A). Its proof, and the bracket listing which residues it kills — is the list right, including at its smallest cases? Is the treatment of zero entries stated and used consistently between the lemma and FAN-4′? |
| **J-IMPORT** | The four imports are stated in Appendix A **for reference and are NOT your target** (FAN-4′, FAN-8′ and MB1 are separately certified; TAIL is separately certified in two families). Do **not** referee their proofs. Do check that each **import matches**: the hypothesis the theorem supplies is the hypothesis the lemma requires, and the conclusion used is the conclusion proved. A mismatched import is in scope and is a MATHEMATICS defect. |
| **J-HC** | Corollary GFANν-HC (`ν ≥ 7` and `L ≥ 8` in the hard core). Its arithmetic, and whether it uses anything beyond Theorem RIG's `ν ≤ L−1` and Theorem GFANν. |

## Classify every defect

Tag each finding **MATHEMATICS** (a claim is false, a proof does not prove its
statement, an import does not match, an enumeration is incomplete or wrong) or
**BOOKKEEPING** (label, cross-reference, wording, a true statement stated imprecisely,
a missing convention that a reader can supply uniquely). State plainly in your verdict
line **whether any MATHEMATICS defect was found**.

## Mandatory control section (do this; a verdict without it does not count)

1. **Counterfactual availability.** Construct a concrete degree multiset that has the
   *shape* of an admissible row (a `C`-part of `L+1` near-equal entries plus a residue
   partition) but **violates** one of the standing hypotheses — e.g. residue total
   `≠ 2ν−E`, or `E ≥ 1` with `L > 2ν−E`. Confirm that the named lemmas are
   **unavailable** on it, i.e. that the hypotheses are load-bearing rather than
   decorative. Report the instance explicitly.
2. **Calibration.** State what you calibrated your Havel–Hakimi code against, and show
   the calibration output, **before** any number you report from the enumeration.
3. **What I could NOT check.** Mandatory. List every joint or sub-claim you did not
   settle, and why.

## Verdict tags — use exactly one

`CLEAN` (no defect of either class) · `PARTIAL` (bookkeeping defects only, no
mathematics defect) · `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) · `REFUTED` (an explicit counterexample, printed in full).

## Report format

Open with a single `VERDICT:` line. Then the joint table with one verdict per named
joint, then the defect list with the MATHEMATICS/BOOKKEEPING tag on each, then the
refutation log (what you tried and what it produced, including code output), then the
mandatory control section, then "What I could NOT check".

---

## Appendix A — the statements, and the text under review

**Standing setting.** `G` is a finite simple graph; `A` is a maximum independent set;
`B = V ∖ A`; `τ = |B|`; `α = |A|`; `residue` is the Havel–Hakimi residue (repeatedly
delete the largest entry `d` and subtract 1 from the next `d` entries; the residue is
the number of zeros left). The **reductio** is the hypothesis `residue(G) = α`, which
the whole line is trying to contradict. `B_lo` / `B_hi` are the low/high vertices of
`B`, `L = |B_lo|`, `p = |B_hi|`, `τ = p + L`. `A′ = A ∖ {a₀}`, and `C` is the set
consisting of `a₀` together with the `L` low vertices — the `C`-part below is its
value multiset at the start of step `p+1`. `ν` is the number of non-edges of `G[B]`.

**The configuration `GFan(τ, L, ν)`.** `B_lo` is non-empty, all of its vertices are
B-universal with `deg_A = 1`, sharing one common A-neighbour `a₀` which is adjacent to
all of `B`; all `ν` non-edges of `B` lie inside `B_hi`; all of `B_hi` is high; and no
`a ∈ A ∖ {a₀}` has a neighbour in `B_lo`. `Fan(τ,L)` is the case `ν = 1`.

### A.1 The four imports (stated for reference — do NOT referee their proofs)

{MB1}

{FAN4P}
{FAN8P}

### A.2 Lemma FAN-6′ — this one IS under review

{FAN6P}

### A.3 The text under review

{SECD}

---

{EMBED}
"""

def polish(t):
    """Remove annotation-strip debris and every repository filename."""
    # debris: an orphaned "." or "," left where a bracket used to sit
    t = re.sub(r"`\n(>\s*)?([.,])", r"`\2", t)
    t = re.sub(r"([`\w])\s+([.,])\s", r"\1\2 ", t)
    t = re.sub(r"\n>\s*\n>\s*\n", "\n>\n", t)
    # filenames: the read restriction forbids opening them, so do not name them
    t = t.replace("The enumeration is\n> `problems/wowii/w61_r5_gfan2.py` functions "
                  "`tail_check` / `escape_check` /\n> `complete_check`, output "
                  "`w61_r5_gfan2_complete.out`:",
                  "The enumeration gives:")
    t = t.replace("**Cross-check of Lemma TAIL** (`w61_r5_gfan2_complete.out`, first line): the",
                  "**Cross-check of Lemma TAIL.** The")
    t = t.replace("it is not mechanically regenerable — the `E = 0` step-count column and the complete\n"
                  "roster of surviving `E ≥ 1` rows. Instrumented re-run:\n"
                  "`problems/wowii/w61_r12_gfannu_embed.py`, output `w61_r12_gfannu_embed.out` (both new\n"
                  "this round; the two primitives are transcribed from `w61_r5_gfan2.py`, so the numbers\n"
                  "below are the **same** check, re-instrumented, and the older script's summary line is\n"
                  "reproduced verbatim as a control).",
                  "it is not mechanically regenerable — the `E = 0` step-count column and the complete\n"
                  "roster of surviving `E ≥ 1` rows.")
    t = t.replace("**(B-7) Controls run before any of the above was written.** (i) The older script's\n"
                  "summary line `nu=1..6 … NONE / ELIMINATED` is reproduced byte-compatibly by the new\n"
                  "run, so this is the same check, not a new one that happens to agree. (ii)",
                  "**(B-6) Controls run before any of the above was written.** (i) The summary column\n"
                  "was reproduced by two independently written enumeration passes that agree line for\n"
                  "line. (ii)")
    t = t.replace("`problems/wowii/w61_r12_gfannu_embed.py`", "the author's instrumented run")
    t = t.replace("### D. **Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 6`** (15:0x CDT)",
                  "**Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 6`.**")
    t = t.replace("the shape-generation specification the\nreader asked for",
                  "the shape-generation specification")
    t = t.replace("of Appendix A's table", "of the table in Appendix A.3")
    t = re.sub(r"\n---\n+---\n", "\n---\n", t)
    t = re.sub(r"([.,]) >\n", r"\1\n>\n", t)
    t = t.replace("(`w61_r12_gfannu_embed.out` block (D))", "(control run, block (D))")
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t


out = (HEADER
       .replace("{MB1}", mb1.rstrip())
       .replace("{FAN4P}", fan4p.rstrip())
       .replace("{FAN8P}", fan8p.rstrip())
       .replace("{FAN6P}", fan6p.rstrip())
       .replace("{SECD}", secD.rstrip())
       .replace("{EMBED}", embed.rstrip()))
out = polish(out)

# final sweep: no pointer to the review record may survive
leaks = [w for w in ("Q25", "Q24", "Q27", "Q23", "Q18", "Q14", "judge", "Repair Z",
                     "Repair Y", "Repair W", "Repair V", "w61_S3_", "wowii61_draft",
                     "PROVED-S3", "§7.22", "s3_dispatch")
         if w in out]
if leaks:
    print("  LEAK CHECK FAILED — these must not appear in the brief:", leaks)
else:
    print("  leak check: clean")

path = ROOT / "prompts/w61_S3_GFANNU_qwen.md"
path.write_text(out)
print(f"  wrote {path} ({len(out.encode()) / 1024:.1f} KB)")
