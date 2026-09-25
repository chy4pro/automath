#!/usr/bin/env python3
"""owner-w61 round 25 -- land the RULING BK bounded weakenings and append SS7.40.

RULING BK: "a bounded weakening goes on the record against the specific joints affected ...
Write it into the ledger beside those promotions so a reader meets it there rather than
deducing it here."  Not a re-run, not a retraction.

RULING AS: the address space is printed before anything is written.
Every insertion is anchored and asserted; every record claim is checked after the write.
"""
import hashlib, pathlib, sys
sys.path.insert(0, "$HOME/workspace/claudecode/automath/problems/wowii")
from w61_mint import spent, next_free

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
D = ROOT / "notes/proofs/wowii61_draft.md"

print("=== ADDRESS SPACE, PRINTED BEFORE ANY WRITE (RULING AS / BB) ===")
s = spent("R")
print(f"  R-family addresses spent : {sorted(s)}")
print(f"  lowest free              : {next_free('R')}")
print("  minted this round        : NONE (no promotion, no registry move)")

src = D.read_text(); pre = hashlib.md5(src.encode()).hexdigest()
out = src

W_2021 = """〔**BOUNDED WEAKENING recorded 2026-08-23 (§7.40 (e)/(f), planner RULING BK) — rows R-20 and
R-21.** Family 1 (**Q25**, `w61_S3_GFAN_qwen.md`) and family 2 (**Q33**, `w61_S3_GFAN_sol.md`)
were **both** scored on briefs that had already told the judge the imports were settled. Q25
carries per-statement status labels (*"Theorem K — certified by four independent judges across
two model families"*, *"Certified; context."*), an explicit *"What is NOT under review"*
exclusion list, and a **gate-status disclosure** naming which statements were one clean round
short. Q33 carries the **global** form — *"Everything else in the project has been through two
independent families and is certified"* — plus *"all separately certified"* and *"the certified
toolkit"*, and it **names the reward**: *"Your round is the second of the two independent
families this document requires."* Under RULING AZ each of those answers **J-IMPORT** before the
judge reads. Q25 additionally carries a REQUIRED control phrased *"name at least one lemma the
text treats as available but which never executes"* — unconditional, i.e. a control that **pays
for a manufactured finding** (§7.40 BK7). **What is weakened:** the evidential weight of the
**import-legitimacy** verdicts (J-CAP's and J-RIG's import clauses) on both families. **What is
NOT weakened:** the mathematics. Both bounds of Lemma CAP were re-derived independently by Q33,
Theorem RIG's five conclusions were re-verified here in `w61_r13_adjudicate.py` against an
independently constructed frame witness, and Repairs AB2/AB3 are unaffected. **Status stands at
PROVED-S3. This is a stated weakening, not a re-run and not a retraction.**〕

"""

W_22 = """〔**BOUNDED WEAKENING recorded 2026-08-23 (§7.40 (e)/(f), planner RULING BK) — row R-22.**
All three families were scored on briefs asserting the imports' status. **Q34**
(`w61_S3_GFAN_r14.md`) and **Q34b** (`w61_S3_GFAN_r14b.md`) each carry *"Do not referee the
imports' own proofs — **they are separately certified**"* inside **J-IMPORT itself**, *"**Each of
these is separately certified.** Your job with them is import matching only"* in the Appendix A.1
preamble, and *"**The certified toolkit**"* attached to the eight-name import list; **Q25**'s
weakening is recorded at rows R-20/R-21 above. Under RULING AZ an import is an interface, and
telling the judge the interior is settled **answers J-IMPORT before the judge reads anything**.
RULING Q's pass, run retroactively over `r14b`, additionally found that **held-out row H1's
cross-reference is false** (*"Appendix A.0 gives the residues for these"* — A.0 contains no
residues) and that **H5 forces a binary the brief's own convention makes ternary**, so that row
did not determine a unique admissible answer; Q34b answered `5/5` and the flaw never bit, but an
**untested** calibration row is not a passed one. **What is weakened:** the import-legitimacy
verdicts (J-IMPORT, J-RIG1's import clause) across all three families, and the *precision* — not
the outcome — of Q34b's held-out gate. **What is NOT weakened:** the seven Part-1 statements'
own mathematics, which is hand-checkable, was re-derived by three families, and took zero
mathematics defects. **Status stands at PROVED-S3.**〕

"""

W_23 = """〔**BOUNDED WEAKENING recorded 2026-08-23 (§7.40 (e)/(f), planner RULING BK) — row R-23, and
this one has TWO parts, the second heavier than the first.**
**(1) Import legitimacy.** Family 1 (**Q35**, `w61_S3_GFAN_r15.md`) and family 2 (**Q37**,
`w61_S3_GFAN_r20.md`) both carry *"they are separately certified"* inside J-IMPORT, *"Each of
these is separately certified"* in the Appendix A.1 preamble, and *"**The certified toolkit**"*
on the import list — J-IMPORT answered before the judge read (RULING AZ / BK).
**(2) The withdrawn obligation was fenced on BOTH briefs, and RULING Q's retroactive pass found
it unprompted on each.** On `r20` it is ranked HIGH and labelled **verdict-pushing**: the brief
*"names the single unverifiable step of the target proof, forbids that step from grounding the
verdict the tags would otherwise demand, and offers two allowed verdicts without a tie-break."*
On `r15` the same defect appears in a different shape, also HIGH: the designed-out obligation
*"lives inside J-DATA, a **TARGET** joint"* while the four verdict tags give a hand-deriving
reviewer nowhere to record it, so *"the brief simultaneously forbids and forces a downgrade."*
**This is heavier than the r14 sentence: that one shaped an import verdict; this shapes the
verdict on the target statement itself.**
**A third weakening, from the judge rather than the audit** (§7.40 (d)): the evidence column
below describes the second implementation as *"written from the §7.22 (c-1) spec alone and
forbidden to read any repo file"*. **That is an authorship claim, and what is on disk proves
output agreement in both directions (`791` rows, `0` and `0`), not authorship independence** —
Q38 raised exactly this and it is upheld. **Read the column as: two implementations agreeing at
roster level in both directions.**
**What is NOT weakened:** the computational half does not rest on the withdrawal at all —
Q37 **ran code** and returned `H3 = 791` with its full ten-entry per-`E` split and `H4 = 131`
exact, Q38 has now **independently reproduced both** from its own checker, and two
implementations of ours agree at roster level in both directions. The `ν ≤ 10` elimination is
the most-recomputed object on this line. **Status stands at PROVED-S3. Stated weakening, not a
re-run and not a retraction.**〕

"""

INSERTS = [
 (W_2021, "**The do-not-overreach constraints, honoured.** (i) **Lemmas FAN-4′/FAN-8′/FAN-6′,"),
 (W_22,   "**The do-not-overreach constraints, honoured.** (i) **Theorem GFANν and Corollary"),
 (W_23,   "〔**Numbering note, caught by the closing grep and recorded rather than quietly fixed.**"),
]
for note, anchor in INSERTS:
    assert out.count(anchor) == 1, f"anchor not unique ({out.count(anchor)}): {anchor[:60]}"
    out = out.replace(anchor, note + anchor)

body = pathlib.Path("/private/tmp/claude-501/-Users-user-workspace-claudecode-automath/"
                    "d1405342-fe87-49aa-8c1d-75c2ca4b3b2b/scratchpad/w61_r25_sec740.md").read_text()
assert out.endswith("\n")
out = out + "\n" + body
D.write_text(out)
post = hashlib.md5(out.encode()).hexdigest()
print(f"\ndraft md5 {pre} -> {post}   ({len(src)} -> {len(out)} chars)")

t = D.read_text()
checks = [
 ("SS7.40 present exactly once", t.count("## §7.40 owner-w61 round 25:"), 1),
 ("SS7.40 is the LAST section", t.rfind("## §7.4") == t.rfind("## §7.40 owner-w61 round 25:"), True),
 ("three bounded-weakening notes landed", t.count("**BOUNDED WEAKENING recorded 2026-08-23"), 3),
 ("all four weakened rows named (R-20/R-21, R-22, R-23)",
  (t.count("rows R-20 and\nR-21.**"), t.count("\u2014 row R-22.**"), t.count("\u2014 row R-23, and")), (1,1,1)),
 ("void gate PASS recorded, not asserted", t.count("**VOID GATE: PASS, `5/5`"), 1),
 ("no family 2 stated plainly", t.count("Corollary GFANν-HC does NOT take family 2"), 1),
 ("withdrawal outcome recorded as (1)-weak, never as a pass",
  t.count("**Recorded as (1)-weak. Not as a pass, and not as (1).**"), 1),
 ("the live leak is named as live", t.count("**BK1 — THE LEAK IS STILL THERE"), 1),
 ("my own checker failure recorded", t.count("The checker failure, reported rather than only the pass"), 1),
 ("no address minted this round", t.count("no address was minted this round"), 1),
 ("sweep limits ride the citation", t.count("numeric/non-emptiness guards only"), 1),
 ("audit limits ride the citation", t.count("What the audit is worth, and the bound on it."), 1),
 ("no stale count: SEVEN findings, not SIX", t.count("audit found SEVEN things"), 1),
]
ok = True
for n, g, w in checks:
    f = "OK " if g == w else "FAIL"
    ok = ok and (g == w)
    print(f"  [{f}] {n}: {g} (want {w})")
print("ALL RECORD ASSERTIONS PASS" if ok else "RECORD ASSERTIONS FAILED")
sys.exit(0 if ok else 1)
