# w61 S3 — Theorem GFANν (ν ≤ 6) re-round on rebuilt enumeration text — Qwen3.8-Max harvest

Source conversation: https://chat.qwen.ai/c/e2abc2f6-5f8d-47f8-8831-971342d9e760
Dispatched: qwen-driver-r13, 2026-08-22 00:38 CDT. Harvested verbatim: qwen-driver-r14, 2026-08-22 01:3x CDT.
Brief: `prompts/w61_S3_GFANNU_qwen.md` (31 KB, queue row Q30). This is the re-round after Q25's
J-GFANNU GAP was diagnosed as a briefing defect (the ν=3…6 enumeration was cited by filename
and never pasted) — repair Z2 puts the complete finite case list in the text.

Completion verified per notes/web_model_ops.md protocol: action-icon row (Copy/Good
Response/Bad Response/Share/Regenerate) present under the final assistant message and static
across two polls ≥10s apart. No CAPTCHA encountered.

**VERDICT (model's own words):**

> VERDICT: GAP — I found no MATHEMATICS defect in the joints I could actually verify, but I
> could not independently regenerate the full ν = 4,5,6 finite check, especially the complete
> E ≥ 1 survivor roster, so the decisive completeness obligation remains unresolved for me. I
> also list several BOOKKEEPING defects/ambiguities.

---

## Verbatim harvest (via get_page_text)

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

*(the standing setting / GFan configuration definitions / four imports, as pasted — see
`prompts/w61_S3_GFANNU_qwen.md` for the exact source text; identical text, not repeated
here since this section is the unmodified input the model was given)*

---

## Model's response (verbatim)

Thinking completed

VERDICT: GAP — I found no MATHEMATICS defect in the joints I could actually verify, but I could not
independently regenerate the full ν = 4,5,6 finite check, especially the complete E ≥ 1 survivor
roster, so the decisive completeness obligation remains unresolved for me. I also list several
BOOKKEEPING defects/ambiguities.

### Joint table

| joint | verdict | short reason |
|---|---|---|
| J-FIN | CLEAN | The split E=0/L≥λ₁, E=0/ν+1≤L<λ₁, E≥1 is disjoint and exhaustive under the imported bounds. λ₁≤2ν is justified for E=0. E≤ν−1 follows for E≥1 from MB1 + FAN-8′ and is used consistently. |
| J-SPEC | CLEAN (with one wording caveat) | The five conventions pin down the positive multiset being tested. Zero padding is inert for "clears in exactly L steps". No graphicality filter is needed for a superset argument. The only caveat is a wording ambiguity about zero entries, listed below. |
| J-E0 | GAP | I verified the partition counts and hand-checked all of ν≤3 and many ν=4,5,6 entries, but I did not independently recompute all 159 s₀(λ) values. The printed column is plausible, but I cannot certify it fully. |
| J-BND | CLEAN | Pair counts 0,1,3,7,14,26 are correct. I checked the listed boundary survivors directly and verified the natural pattern [L+k,1^{k−1}]; I found no missing boundary survivor in the cases I tested. |
| J-COUNT | CLEAN | The closed form S(ν)=Σ_{E=1}^{ν−1}(ν−E)p(E)p(2ν−E) follows from the parameter ranges, and it evaluates to 0,3,24,110,397,1211. The "all p(E) occur" step is valid because L+1≥ν+2>E. |
| J-SURV | GAP | I could not independently regenerate the full E≥1 list of 1211 shapes for ν=6 (or the corresponding ν=4,5 lists) and confirm that exactly the printed 72 rows survive. This is the main unresolved computer-assisted step. |
| J-KILL | CLEAN | Every printed certificate (w,2nd) has a unique maximum and satisfies 2nd ≤ w−2. The boundary cases (w,1) at w=3 and (w,2) at w=4 are allowed by the lemma. |
| J-FAN6P | PARTIAL | The proof is valid for the form used. However, the zero-entry convention is worded ambiguously; see BOOKKEEPING defect D3. This does not affect any certificate actually used, all of which have w≥2 and in practice w≥3 except [2] at ν=1. |
| J-IMPORT | CLEAN | The hypotheses supplied to MB1, FAN-4′, FAN-8′, and TAIL match the hypotheses those lemmas state, and the conclusions used are the conclusions proved. |
| J-HC | CLEAN | The arithmetic ν≥7 ⇒ L≥ν+1≥8 is correct. The corollary uses only ν≤L−1 from Theorem RIG and Theorem GFANν. |

### Defect list

**D1 — BOOKKEEPING: unqualified "only residue clearing in exactly L steps is [2ν]"**

In the proof of Theorem GFANν the text says: "At E = 0 the only residue clearing in exactly L
steps is the single part [2ν], for every ν ≤ 6 …" Read literally, this is contradicted by
Appendix B-3, which prints additional E=0 boundary survivors, e.g. (L,λ)=(5,[7,1]), (7,[9,1]),
(7,[10,1,1]), etc. The intended statement is clearly the TAIL-range statement: among partitions
with s₀(λ)=λ₁, the only one is [2ν]. The missing qualifier "for L≥λ₁" or "with s₀(λ)=λ₁" should
be restored. This does not appear to affect the proof, because B-3 checks and kills the boundary
survivors separately.

**D2 — BOOKKEEPING: theorem statement should say 1 ≤ ν ≤ 6**

The theorem says "every ν ≤ 6", but the enumeration, TAIL's hypothesis λ non-empty, and MB1's
ν≥1 all implicitly assume ν≥1. If ν=0 were intended, E=0 would give an empty λ, and TAIL as
stated would not apply. The standing setting likely excludes ν=0, but the theorem statement
should make ν≥1 explicit.

**D3 — BOOKKEEPING / ambiguity: zero-entry convention in Lemma FAN-6′**

Lemma FAN-6′ says: "the A′ value multiset carries its zero entries — every a∈A′ contributes its
current value, zero included — so the 'second-largest entry' of a residue with a single positive
part is 0, not −∞." If the actual A′ multiset has exactly one positive entry and no zero-valued
A′ vertices, then there is literally no second-largest carried entry. The convention therefore
behaves like a sentinel zero, not merely a statement that actual zeros are present. This is
harmless for the certificates actually used: all printed (w,0) certificates have w≥2, and the
proof's "no entry w−1" form kills a singleton [w] for w≥2 regardless of whether a real zero is
present. But the wording should distinguish "actual zero entries" from "a conventional
second-largest value 0 for a singleton partition".

**D4 — BOOKKEEPING: padding control scope narrower than the full enumeration**

B-1(2) cites a padding-inertness control over lists [L]^{L+1}∪λ with ν≤4. The full enumeration
includes ν≤6 and E≥1 lists. The general argument given is sound, but the cited control run does
not literally cover the whole enumerated class. This is not a mathematical defect, because the
reason given is general, but the control description could be strengthened.

### Refutation log: what I tried and what it produced

**1. Havel–Hakimi implementation used for checking**

I used the following positive-entry version of Havel–Hakimi. For "clears in exactly L steps",
zeros may be ignored because they are inert unless a step would have to subtract from them, in
which case the run aborts.

```python
def clears_in_L_steps(seq, L):
    # seq is a multiset of nonnegative integers
    pos = sorted([x for x in seq if x > 0], reverse=True)

    for step in range(L):
        if not pos:
            return False        # already all zeros before L steps
        d = pos[0]
        if d <= 0:
            return False
        if d > len(pos) - 1:
            return False        # head exceeds remaining entries

        pos = pos[1:]
        # subtract from d largest remaining entries
        if d > len(pos):
            return False
        for i in range(d):
            if pos[i] == 0:
                return False    # would drive a zero negative
            pos[i] -= 1
        ...
```

I did not execute a full machine enumeration in this environment. The checks below are hand
simulations using exactly this rule, plus closed-form counting. I am reporting this honestly
rather than presenting printed output I did not produce.

**2. Calibration, before checking any enumerated numbers**

I calibrated the rule on the two requested families.

`residue(K₂) = 1`: K₂ has degree multiset [1,1]. Step 1: delete 1, subtract from the other 1,
leaving [0]. One zero remains, so residue = 1.

`residue(Cₙ) = ceil(n/3)` for n=3,…,9: Cₙ has degree multiset [2]^n. Hand simulation gives:

| n | HH residue of [2]^n | ceil(n/3) |
|---|---|---|
| 3 | 1 | 1 |
| 4 | 2 | 2 |
| 5 | 2 | 2 |
| 6 | 2 | 2 |
| 7 | 3 | 3 |
| 8 | 3 | 3 |
| 9 | 3 | 3 |

For example: [2,2,2,2] → [2,1,1] → [0,0], residue 2. [2]^7 → [2,2,2,2,1,1] → [2,1,1,1,1] →
[1,1,0,0] → [0,0,0], residue 3. This matches the claimed calibration.

**3. Small-case recomputation / refutation attempts**

I tried to find an admissible shape that clears in exactly L steps but is not killed by FAN-6′.

*ν = 1*: E=0, partitions of 2. [2]: s₀([2]) = 2, survivor, killed by FAN-6′ as (2,0). [1,1]:
s₀([1,1]) = 2 ≠ 1, not a survivor. No boundary rows. No E≥1 rows because E≤ν−1=0. No
counterexample.

*ν = 2*: E=0, partitions of 4. I hand-checked: [4]: s₀=4, survivor, killed. [3,1]: s₀=4≠3.
[2,2]: s₀=3≠2. [2,1,1]: s₀=3≠2. [1,1,1,1]: s₀=3≠1. Boundary ν+1≤L<λ₁ has one pair:
(L,λ)=(3,[4]). Direct simulation: [4,3,3,3,3] → [2,2,2,2] → [2,1,1] → zeros in 3 steps.
Survivor, killed by (4,0). E=1: only L=3, e=1, and λ⊢3. λ=[3]: list [4,3,3,3,3], clears in 3
steps, killed (3,0). λ=[2,1]: list [4,3,3,3,2,1], does not clear in 3 steps. λ=[1,1,1]: list
[4,3,3,3,1,1,1], does not clear in 3 steps. No unkilled survivor.

*ν = 3*: I recomputed all 11 s₀(λ) values for partitions of 6 by hand and obtained the same
survivor criterion: only [6] has s₀=λ₁. I also checked the single boundary survivor (5,[6]) and
the four printed E≥1 survivors. I found no missing unkilled row in the cases I tested. For
example, the printed E≥1 row L4 E1 e=1 λ=5 gives list [5,5,4,4,4,4], which clears in 4 steps and
has certificate (5,0). The non-killed partition shapes such as λ=[3,2,1] or λ=[1^5] do not clear
in the required number of steps in my simulations.

*ν = 4 and higher*: I hand-checked many individual rows, especially all printed survivors for
ν=4, and the boundary survivors for all ν. I did not exhaustively hand-simulate all 110, 397,
and 1211 shapes. This is the source of the GAP verdict on J-SURV.

**4. Boundary-row count check**

For E=0, boundary pairs satisfy ν+1 ≤ L < λ₁. For a partition λ⊢2ν with maximum m=λ₁, the
number of boundary L values is max(0, m−ν−1). Summing over partitions of 2ν gives: ν=1: 0; ν=2:
[4] contributes 1; ν=3: [6] contributes 2, [5,1] contributes 1, total 3; ν=4: [8] contributes 3,
[7,1] contributes 2, two 6-max partitions contribute 1 each, total 7; ν=5: total 14; ν=6: total
26. These agree with the printed counts.

The printed boundary survivors also follow the pattern λ = [L+k, 1^{k−1}], with L + 2k − 1 = 2ν
and L ≥ ν+1. For ν=6, this gives k=1,2,3, hence: k=1: L=11, λ=[12]; k=2: L=9, λ=[11,1]; k=3:
L=7, λ=[10,1,1] — exactly as printed.

**5. Closed-form count check**

For E≥1: MB1 gives L≥ν+1. FAN-8′ gives L≤2ν−E. Hence E≤ν−1. For fixed E, the number of allowed
L values is ν−E. The escape multiset e is a partition of E; because L+1≥ν+2>E, every partition
of E fits into at most L+1 parts. λ is an arbitrary partition of 2ν−E. Therefore
S(ν)=Σ_{E=1}^{ν−1}(ν−E)p(E)p(2ν−E).

Evaluating: ν=1: empty sum = 0. ν=2: 1·p(1)p(3)=1·1·3=3. ν=3: 2·1·p(5)+1·2·p(4)=2·7+2·5=24.
ν=4: 3·1·p(7)+2·2·p(6)+1·3·p(5)=45+44+21=110. ν=5: 4·1·p(9)+3·2·p(8)+2·3·p(7)+1·5·p(6)
=120+132+90+55=397. ν=6: 5·1·p(11)+4·2·p(10)+3·3·p(9)+2·5·p(8)+1·7·p(7)=280+336+270+220+105=1211.
These match the printed values.

### Mandatory control section

**1. Counterfactual availability: hypotheses are load-bearing**

I constructed explicit shape-like multisets that violate individual lemma hypotheses.

*Violating FAN-4′ mass condition*: Take ν=2, E=0, L=3, but let the A′ part be λ=[3], whose sum
is 3, not 2ν−E=4. The full multiset is [3,3,3,3,3]. This has the superficial shape of an E=0
row, but FAN-4′ is unavailable because the A′ total is not 2ν−E. TAIL is also unavailable as
stated, because TAIL assumes λ is the A′ residue of total 2ν.

*Violating FAN-8′ escape bound*: Take ν=2, E=1, L=4. Let the escape multiset be e=[1], so the
C-part is [5,4,4,4,4]. Let λ=[3], whose sum is 2ν−E=3. This satisfies the FAN-4′ mass shape, but
violates FAN-8′'s conclusion because L = 4 > 3 = 2ν−E. Thus FAN-8′ cannot be invoked. This shows
that the bound E≥1 ⟹ L≤2ν−E is load-bearing for finiteness: without it, L would not be bounded
for E≥1.

*Violating TAIL's range hypothesis*: Take ν=2, E=0, L=3, λ=[4]. Then λ₁=4, so L<λ₁. TAIL is
unavailable. The list is [4,3,3,3,3], and it clears in exactly 3 steps: [4,3,3,3,3] →
[2,2,2,2] → [2,1,1] → zeros. This shows why the boundary class ν+1≤L<λ₁ must be checked
separately.

**2. Calibration output** — repeated here for convenience, before any enumeration-derived
claim: residue(K2) = 1; C3 residue = 1; C4 residue = 2; C5 residue = 2; C6 residue = 2; C7
residue = 3; C8 residue = 3; C9 residue = 3. These agree with ceil(n/3).

**3. What I could NOT check** (mandatory)

- Full independent regeneration of the E≥1 survivor roster. I did not execute a complete
  enumeration of the 110, 397, and 1211 shapes for ν=4,5,6. Therefore I cannot independently
  certify that the printed 72 E≥1 survivors are complete and that no unprinted survivor exists.
  This is the central unresolved computer-assisted obligation, J-SURV.
- Full independent recomputation of all 159 s₀(λ) values. I hand-checked all partitions for
  ν≤3, many for ν=4, and spot-checked several for ν=5,6, including likely dangerous
  small-maximum cases. But I did not recompute every entry in B-2. Thus J-E0 is only partially
  verified by me.
- Author's control runs. I did not reproduce: the 1817-pair TAIL cross-check; the 480-list
  padding-inertness control; the two independent enumeration passes; the instrumented per-E
  split for ν=6.
- Proofs of the imported lemmas. Per the instructions, I did not referee the proofs of FAN-4′,
  FAN-8′, MB1, or TAIL. I only checked that their hypotheses and conclusions match the way
  Theorem GFANν uses them.
- Theorem RIG. Theorem RIG is not included in the supplied text. For Corollary GFANν-HC I only
  checked that, if RIG supplies ν≤L−1, then the arithmetic conclusion ν≥7 and L≥8 follows using
  Theorem GFANν.

### Final assessment (model's own words)

The finiteness argument is sound, the closed-form count is correct, the boundary-row counts and
printed boundary survivors check out, and all printed FAN-6′ certificates are valid. Lemma
FAN-6′ is correctly proved for the way it is used, modulo a minor wording ambiguity about zero
entries. However, the decisive computer-assisted completeness claim — that the printed 72 E≥1
survivors are the entire survivor set inside the 1745 enumerated shapes — is not something I
could independently verify from the text alone without executing the enumeration. Therefore the
correct verdict for this review is GAP, not CLEAN.

---

*(Note: get_page_text's plain-text extraction reordered some KaTeX-rendered inline math and
collapsed several `text`/`python` code blocks to placeholder labels followed by their content on
separate lines — see notes/web_model_ops.md's KaTeX-extraction-order caveat. The transcription
above preserves the model's content and structure faithfully but reflows some of that
extraction; no wording was altered or invented.)*

**UNVERIFIED by owner-w61** — this is a verbatim capture, not an owner adjudication.
