#!/usr/bin/env python3
"""Assemble prompts/w61_S3_GFAN_sol.md — the WIDENED second-family brief (codex `sol`).

Round 12, planner-approved 00:5x.  One brief covering BOTH open GFAN debts:
  * S3-D3a — the 11-statement group at 1 clean round (Q25, Qwen): Lemma CAP,
    Corollary CAP1, Theorem RIG, Corollaries RIG-1/RIG-2, Lemmas FAN-4'/FAN-8'/FAN-6',
    Theorem GFAN2, Corollaries GFAN2-HC/GFAN2-L3.  This round is their NON-QWEN
    second family, on the REPAIRED text (Z1/Z3/Z4 landed), and therefore doubles as
    the repair-confirmation pass.
  * S3-D3b — Theorem GFANnu and Corollary GFANnu-HC, at 0 rounds, on the rebuilt
    text-complete enumeration (Z2).  Runs in parallel with Q30 (Qwen) so GFANnu gets
    two families in one cycle; the two judges never see each other.

Same construction discipline as w61_r10_build_sol_brief.py and
w61_r12_build_gfannu_brief.py: text pulled LIVE from the draft, every repair-provenance
annotation stripped, every pointer to the review record removed by a leak check.
"""
import re
import pathlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
draft = (ROOT / "notes/proofs/wowii61_draft.md").read_text().splitlines(keepends=True)
gfannu = (ROOT / "prompts/w61_S3_GFANNU_qwen.md").read_text()


def slice_between(start_pred, end_pred):
    i = next(k for k, l in enumerate(draft) if start_pred(l))
    j = next(k for k, l in enumerate(draft) if k > i and end_pred(l))
    return "".join(draft[i:j])


def strip_annotations(text):
    out, i = [], 0
    while i < len(text):
        if text.startswith("〔**Repair", i) or text.startswith("〔**Repairs", i):
            depth, j = 0, i
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
    text = re.sub(r"[ \t]*\n(>\s*\n)+(?=>\s*\n)", "\n", text)
    text = re.sub(r"([`\w])\s+([.,])\s", r"\1\2 ", text)
    text = re.sub(r"([.,]) >\n", r"\1\n>\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


# ---- draft slices: the whole of 7.12 A-C and 7.13 A-C, plus 7.8 G's configuration
cap = slice_between(lambda l: l.startswith("### A. The degree cap"),
                    lambda l: l.startswith("### B. Theorem RIG"))
rig = slice_between(lambda l: l.startswith("### B. Theorem RIG"),
                    lambda l: l.startswith("### D. The other layer"))
lemmas = slice_between(lambda l: l.startswith("### A. The three generalized lemmas"),
                       lambda l: l.startswith("### C. Numerical backing"))
for s in ("cap", "rig", "lemmas"):
    pass
cap, rig, lemmas = (strip_annotations(x) for x in (cap, rig, lemmas))
lemmas = lemmas.replace(
    "Repair F4 already\n> corrected the parenthetical that misdiagnosed why `1+1` escapes: the reason is\n"
    "> that its maximum is not unique.",
    "The reason `1+1` escapes is that its\n> maximum is not unique -- not that a `0` entry is present.")
lemmas = re.sub(r"`w61_r5_gfan2[^`]*`", "the author's archived run", lemmas)
rig = re.sub(r"`w61_r5[^`]*`", "the author's archived run", rig)
cap = re.sub(r"`w61_r5[^`]*`", "the author's archived run", cap)

# drop the status paragraphs (they name the review record)
rig = re.sub(r"\*Status 〔\*\*updated.*?\*\n", "", rig, flags=re.S)
rig = re.sub(r"\n---\n", "\n", rig)

# the GFANnu half is EXACTLY the Qwen brief's Appendix A.3 + Appendix B, reused verbatim
i = gfannu.index("### A.3 The text under review")
gfannu_part = gfannu[i:].replace("### A.3 The text under review",
                                 "## Appendix C — Theorem GFANnu and its enumeration")
gfannu_part = gfannu_part.replace("## Appendix B — the `ν ≤ 6` enumeration, in full",
                                  "### C.1 The enumeration, in full")
gfannu_part = gfannu_part.replace("Appendix B", "Appendix C.1")
gfannu_part = gfannu_part.replace("the table in Appendix A.3", "the table in Appendix C")

HEADER = r"""# GFAN family — SECOND-FAMILY round (S3-D3a) **and** first round on Theorem GFANnu (S3-D3b) — codex `gpt-5.6-sol`

**Driver note (do NOT act on this box; it is addressed to the operator, not to you).**
Queue row **Q33**. Dispatch method: codex TUI in screen session `codex`, `/model` ->
`gpt-5.6-sol` high, then send ONE line -- `Read prompts/w61_S3_GFAN_sol.md and execute
the task in it.` -- and confirm "Working" appears on a `hardcopy`. Do not paste the
brief into the TUI. If the approval box appears, answer `a`. A Qwen round on the
GFANnu half runs in parallel; the two judges are independent and neither is shown the
other's brief or output.

TARGET, in two parts:
* **Part 1 (the group):** Lemma CAP, Corollary CAP1, Theorem RIG, Corollaries RIG-1
  and RIG-2, Lemmas FAN-4', FAN-8', FAN-6', Theorem GFAN2, Corollaries GFAN2-HC and
  GFAN2-L3.
* **Part 2 (the computer-assisted one):** Theorem GFANnu (`nu <= 6`) and Corollary
  GFANnu-HC.

## Who you are

You are an INDEPENDENT adversarial reviewer. You are not the author and have no stake
in the result. Your job is to find defects. A CLEAN verdict that misses a real defect
is the worst outcome; a false alarm you retract after computing is fine. Everything
below is under review, including every line labelled PROVED.

Part 1 has had **one** adversarial round, from a different model family. **You are not
being shown that report and you must not go looking for it** -- see the read
restriction. Your round is the second of the two independent families this document
requires, and two families agreeing is the whole point: a round that reproduces another
judge's reading because it read that judge is worth nothing here. Several passages have
been **edited since that round**. They are not marked, deliberately: find them the way
you would find anything else, by checking every line.

## Read restriction -- a hard constraint, not a preference

You are running with filesystem access inside a repository that contains the full
working record of this project, including other judges' reports and the author's notes
on what he expects you to find. Reading any of it destroys the independence this round
exists to provide.

* **Everything you need is in this file.** Treat it as the complete, authoritative text.
* **Do NOT open, grep, or otherwise read**: `notes/proofs/wowii61_draft.md`, anything
  under `notes/reviews/`, anything matching `problems/wowii/w61_*`, anything matching
  `prompts/w61_*` other than this file, anything under `orchestration/`, or any file
  whose name contains `dispatch`, `adjudicate`, `harvest`, `gfan`, `embed`, or `qwen`.
  In particular **do not run the author's archived enumeration scripts** -- reproduce
  anything you need from the specification, in your own code.
* You **may** write and run your own scratch code, and read files you created yourself.
* If a joint cannot be settled without a restricted file, **say so and mark that joint
  UNRESOLVED**. Do not read it. Do not search the web.

**Write your report to `problems/wowii/w61_S3_GFAN_sol.md`** (create it; do not read
any other file in that directory). Put your scripts in
`problems/wowii/w61_S3_GFAN_sol_check.py` and **keep their raw stdout** in
`problems/wowii/w61_S3_GFAN_sol_check.out` -- raw output, not a hand-written summary.
Print the verdict line to the terminal as well.

## Why this target, and what turns on it

The line's remaining uncertified surface is exactly what is in this file. Everything
else in the project has been through two independent families and is certified. So a
defect here is load-bearing in a way that a defect elsewhere no longer is.

Part 1 is a rigidity result and a case analysis: Theorem RIG says that a whole
structural layer, if non-empty, is forced into one named configuration `GFan(tau,L,nu)`;
Theorem GFAN2 then kills the `nu = 2` slice of it. Part 2 is a **computer-assisted**
theorem: four hand-proved bounds make a case list finite for each `nu`, and a finite
check inside that list finishes it. The finite check is printed in full in Appendix C.1
-- specification and data both -- so it is checkable without the author's files.

## REFUTE FIRST -- the required order of work

1. **Build your own tools and calibrate them before use.** Implement Havel-Hakimi from
   the specification below; calibrate against `residue(K2) = 1` and
   `residue(Cn) = ceil(n/3)` for `n = 3..9`, and print the calibration. **A number you
   report before your calibration is printed does not count.**
2. **Try to refute Theorem GFANnu by computation** (Part 2): regenerate the finite case
   list from the specification in Appendix C.1 for at least `nu = 1,2,3,4`, and find a
   shape that clears in exactly `L` steps and is **not** killed by Lemma FAN-6'. One
   such shape refutes the theorem. Reuse none of the printed numbers while doing this;
   compare only afterwards.
3. **Try to refute Theorem GFAN2** the same way, and Theorem RIG by construction: build
   a graph in the hard-core frame with `B_lo` non-empty and every low vertex
   B-universal, and check whether all five conclusions (a)-(e) actually hold.
4. **Then, and only then**, review the joints line by line.
5. Report what you could NOT check. That section is mandatory.

## Named joints -- give each an explicit verdict

| joint | what to check |
|---|---|
| **J-CAP** | Lemma CAP and Corollary CAP1: the degree cap and the `deg_A(b) = 1` it buys. Does the lower bound need `A` **maximum** or only maximal? Is the upper-bound arithmetic right at both boundaries (`n_b = 0` and `n_b = tau-1`)? Is any frame or reductio hypothesis used silently? |
| **J-RIG** | Theorem RIG (a)-(e) clause by clause. Where exactly does `diam = 4` enter? Is Lemma 4 used in the form it is stated? Is the trailing `nu <= L-1` correctly attributed? |
| **J-RIG-EQ** | Theorem RIG's word **"exactly"**: the proof matches each `GFan` clause to one of (a)-(e) and then asserts the converse. Is the converse actually definitional, or is something being smuggled? |
| **J-RIG12** | Corollaries RIG-1 and RIG-2. RIG-1 claims to remove a tightness argument from an earlier proposition -- does it? RIG-2's chain (`nu = 1` killed by Theorem FAN, `L = 2` empty, `L = 3` a single configuration) -- is each link earned? |
| **J-FAN4P** | Lemma FAN-4': the residue mass `2nu - E` and the `C`-entries `L + e_c`. Re-derive the degree-sum bookkeeping yourself; the `p`-terms are supposed to cancel via `tau = p + L`. |
| **J-FAN8P** | Lemma FAN-8': the escape bound `L <= 2nu - E`. Are the two subtracted sets disjoint and genuinely inside the block? Is the prefix inequality tie-safe? What does the lemma say at `E = 0`? |
| **J-FAN6P** | Lemma FAN-6' and its proof. Also the bracket listing which residues it kills: is that list right at its smallest cases? Is the treatment of zero entries stated, and used consistently between FAN-6' and FAN-4'? |
| **J-GFAN2** | Theorem GFAN2: Step 1's escape budget, Step 2's three `L >= 4` trajectories, and all eight `L = 3` rows. Simulate them yourself. Is the row list **complete** -- is anything excluded that should not be? |
| **J-CORHC** | Corollaries GFAN2-HC, GFAN2-L3, GFANnu-HC. Arithmetic and dependency only. |
| **J-FIN** | (Part 2) Theorem GFANnu's finiteness argument. The split into `E=0/L>=lam_1`, `E=0/nu+1<=L<lam_1`, `E>=1` -- disjoint? exhaustive? Is `lam_1 <= 2nu` justified? Does anything force `E <= nu-1`, and is it used consistently? Do the four imports match their statements? |
| **J-SPEC** | (Part 2) Appendix C.1's five conventions. Are they sufficient to pin the enumerated set exactly? Is the unlabelled/multiset reduction legitimate? Is the zero-inertness claim true -- test it. Is "no graphicality filter is needed" valid, and does its monotonicity run in the direction the conclusion needs? |
| **J-DATA** | (Part 2) The printed data. Recompute `s0(lam)` for the partitions of `2nu`, `nu <= 6`; check the boundary pair counts `0,1,3,7,14,26`; derive the closed form `S(nu)` yourself and check `0,3,24,110,397,1211`; regenerate the roster of `72` surviving `E >= 1` rows and ask whether it is **complete** -- does your run produce a survivor that is not printed? Is any printed row not actually a survivor? |
| **J-KILL** | (Part 2) Lemma FAN-6' against every printed survivor. Watch the boundary certificates `(w, 2nd) = (4, 2)` and `(3, 1)`. |
| **J-SCOPE** | Every statement in this file: what hypotheses does its own proof consume, versus what it is filed under? Report both under- and over-hypothesis. Under-hypothesis is a MATHEMATICS defect; over-hypothesis is bookkeeping. |

## Classify every defect

Tag each finding **MATHEMATICS** (a claim is false, a proof does not prove its
statement, an import does not match, an enumeration is incomplete or wrong, a statement
is used outside the hypotheses it was proved under) or **BOOKKEEPING** (label,
cross-reference, wording, a true statement stated imprecisely, a missing convention a
reader can supply uniquely). **State plainly in your verdict line whether any
MATHEMATICS defect was found.**

## Mandatory control section (a verdict without it does not count)

1. **Counterfactual availability.** Build a concrete instance that has the *shape* of
   an admissible configuration but **violates** one standing hypothesis -- e.g. a
   `Fan`/`GFan`-shaped degree sequence failing the reductio, or a residue total not
   equal to `2nu - E`. Confirm the named lemmas are **unavailable** on it, so the
   hypotheses are load-bearing rather than decorative. Print the instance.
2. **Witness validation in class-definition order.** For any graph you name as a
   witness, verify the class predicates in the order the class defines them
   (connected, then `A` **maximum** by exhaustive enumeration, then `diam`, then `f`,
   then non-forest, then `residue` vs `alpha`) and print each.
3. **Vacuity honesty.** If your search box contains no instance satisfying the full
   hypotheses of a composite statement, **say so explicitly** and do not present the
   absence of a counterexample as positive evidence. Attack the ingredients separately
   instead, and label that as what it is.
4. **What I could NOT check.** Mandatory. Every joint or sub-claim you did not settle,
   and why.

## Verdict tags -- use exactly one

`CLEAN` (no defect of either class) - `PARTIAL` (bookkeeping defects only, no
mathematics defect) - `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) - `REFUTED` (an explicit counterexample, printed in full).

## Report format

Open with a single `VERDICT:` line, then `TEXT VERSION REVIEWED: w61_S3_GFAN_sol
(Q33)`. Then the joint table with one verdict per named joint, then the defect list
with a MATHEMATICS/BOOKKEEPING tag on each, then the refutation log (what you tried and
what it produced, with code output), then the mandatory control section, then "What I
could not check".

---

## Appendix A -- the standing setting

`G` is a finite simple graph; `A` is a **maximum** independent set; `B = V \ A`;
`tau = |B|`; `alpha = |A|`; `f` is the forest number (largest vertex set inducing a
forest); `residue` is the Havel-Hakimi residue (repeatedly delete the largest entry `d`
and subtract 1 from the next `d` entries; the residue is the number of zeros left).

* **hard-core frame** := `G` connected, non-forest, `diam(G) = 4`, `f = alpha+1`
  (no reductio).
* **hard core** := the hard-core frame **plus** `residue = alpha` (the reductio), plus
  `tau >= 4`.

`B_lo` / `B_hi` are the low (`deg <= tau`) / high (`deg >= tau+1`) vertices of `B`;
`L = |B_lo|`, `p = |B_hi|`, `tau = p + L`. `nu` is the number of non-edges of `G[B]`;
`mbar` is the number of non-edges lying inside `B_hi`. `B_lo^+` is the set of low
vertices having a non-neighbour in `B`. `A' = A \ {a0}`. `C` is `a0` together with the
`L` low vertices; the `C`-part below is its value multiset at the start of step `p+1`.

**The configuration `GFan(tau, L, nu)`.** `B_lo` is non-empty, all of its vertices are
B-universal with `deg_A = 1`, sharing one common A-neighbour `a0` adjacent to all of
`B`; all `nu` non-edges of `B` lie inside `B_hi`; all of `B_hi` is high; and no
`a` in `A \ {a0}` has a neighbour in `B_lo`. `Fan(tau,L)` is the case `nu = 1`.

**Facts you may assume without refereeing them** (all separately certified; check only
that each *import* matches -- hypothesis supplied = hypothesis required, conclusion
used = conclusion proved; a mismatched import IS in scope and IS a MATHEMATICS defect):

* **Lemma 4**: in the frame, any two adjacent vertices of `B` have a common
  A-neighbour.
* **Observation R1**: in the frame, `diam = 4` implies `B` is not a clique, so
  `nu >= 1`.
* **Lemma C\***, **(F-b)**: the frame facts about occurring types.
* **Lemma S**, **Lemma DICH**, **Lemma Z+**, **Lemma F3'**, **Theorem K**: the
  certified toolkit.
* **Theorem MB**, **Corollary MB1** (`nu = mbar <= L-1`, so `L >= nu+1 >= 2`, when
  every low vertex is B-universal), **Theorem SL**, **Proposition L2**.
* **Theorem FAN**: the whole `Fan(tau, L>=2)` family is eliminated from the hard core.
* **Lemma TAIL**: stated in Appendix C where it is used.
* **Favaron-Maheo-Sacle**: `residue <= alpha`.

---

## Appendix B -- Part 1, the text under review

{CAP}
{RIG}
{LEMMAS}

---

{GFANNU}
"""

out = (HEADER
       .replace("{CAP}", cap.rstrip())
       .replace("{RIG}", rig.rstrip())
       .replace("{LEMMAS}", lemmas.rstrip())
       .replace("{GFANNU}", gfannu_part.rstrip()))

# strip any surviving section pointers and review-record names
out = re.sub(r"§7\.8 G", "Appendix A", out)
out = re.sub(r"§7\.12 D", "the companion section (not supplied)", out)
out = re.sub(r"§7\.13 D", "Appendix C", out)
out = re.sub(r"§7\.(\d+)( [A-G])?", "the certified toolkit", out)
out = re.sub(r"\n{3,}", "\n\n", out)

probe = out.replace("`notes/proofs/wowii61_draft.md`", "")
leaks = [w for w in ("Q23", "Q24", "Q25", "Q26", "Q27", "Q30", "judge's report",
                     "Repair ", "LANDED", "w61_S3_GFAN_qwen", "w61_r5_gfan2",
                     "w61_r12_gfannu", "wowii61_draft", "PROVED-S3", "§7.")
         if w in probe]
print("  leak check:", "clean" if not leaks else f"FAILED {leaks}")
path = ROOT / "prompts/w61_S3_GFAN_sol.md"
path.write_text(out)
print(f"  wrote {path} ({len(out.encode()) / 1024:.1f} KB)")
