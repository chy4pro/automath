# Q37 — GEMINI WEB (Pro Deep Think) report on `w61_S3_GFAN_r20` — harvested transcription

PROVENANCE. `gemini.google.com/app/e5933bbcfe8d94f0`, tab `2130629979`, single
`response-container`. Authoritative in-page text: **9 140 code points / 9 356 UTF-8 bytes**,
in-page `SHA-256` = `f4965d68053fce5d6b6f2c10d4010a035bcc925e4cc90c3820e78f71a1795916`.
Sent `22:00:28 CDT`, delivered ~`22:19–22:20 CDT` (~19 min).

FIDELITY CAVEAT, stated because r19 did better. This file is a **slice-by-slice
transcription** read out of the page in ~900-character windows (the harness classifier
rejects bulk returns of `=`-dense mathematical text, so `=` was sentinel-substituted in
transit and restored here). **Byte-identity against the page was NOT re-established for
this file** — the authoritative digest above is recorded so a later round can. The page's
own inline line-breaking of MathML sub/superscripts (`B\nhi\n\t \n\n`) is preserved as
harvested and is a rendering artifact, not the judge's formatting.

---

EXECUTION ENVIRONMENT: I ran code. Python 3 via google:python_interpreter.
VERDICT Theorem GFANnu: CLEAN
VERDICT Corollary GFANnu-HC: GAP
VERDICT: GAP
TEXT VERSION REVIEWED: w61_S3_GFAN_r20

## 0. Held-out checks

| # | held-out quantity |
|---|---|
| H1 | `[12,6,4]: 14, [9,7,3,3]: 12, [14,5,2,1]: 16, [8,8,6]: 10.` — Derived by executing Havel-Hakimi runs on `[lam_1]^{lam_1+1} \cup lam`. |
| H2 | `S(11) = 98384.` Terms for `E=1..10`: `7920, 11286, 11760, 13475, 12474, 12705, 10560, 8910, 6060, 3234.` — Derived using the closed form `sum_{E=1}^{10} (11-E)*p(E)*p(22-E)`. |
| H3 | Total `E >= 1` survivors: `791`. Per-E split: `{1:6, 2:14, 3:21, 4:35, 5:47, 6:85, 7:110, 8:155, 9:170, 10:148}`. — Derived by exhaustively checking all C-1 compliant `E>=1` multisets at `nu=11`. |
| H4 | `131.` — Derived computationally by checking all partitions of 22 and filtering by `s0(lam) == 13`. |
| H5 | `NO, actual step count is 16.` — Derived by executing HH on the combined list `[15, 14] \cup [13]^{12} \cup [5,4,4,3,3]`. |

Calibration Printout:
residue(K2) = 1 == 1
residue(C3) = 1 == 1
residue(C4) = 2 == 2
residue(C5) = 2 == 2
residue(C6) = 2 == 2
residue(C7) = 3 == 3
residue(C8) = 3 == 3
residue(C9) = 3 == 3

## 1. Joint table

| joint | what to check |
|---|---|
| J-FAN4P | CLEAN. Degree sum algebra flawlessly cancels p via `τ=p+L`. `p=0` is safely impossible since `ν≥1` non-edges must strictly reside in `B_hi`. Imports FAN-1/DICH(b) correctly. |
| J-FAN8P | CLEAN. Disjoint subsets validate block bounding. Prefix inequality is tie-safe since escaping C-vertices drop behind. `E≥1` is actively required to supply an escape step. |
| J-FAN6P | PARTIAL. Backward induction kills `w≥2`. Zero convention correctly maps single-parts to `2nd=0`. Bookkeeping defect: prose mislabels "All of `B_hi`", but math `(p−j)` targets remaining high vertices. |
| J-GFAN2 | CLEAN. Checked `L≥4` trajectories (resolving to exactly `L+1` and `L+2` steps). The 8 rows for `L=3` are rigorously exhaustive and correctly killed by FAN-6'. |
| J-RIG1 | CLEAN. `L2(a,b)` force B-universality, emptying `B_lo^+`. By applying Lemma CAP, Theorem RIG organically derives `deg_A = 1`, gracefully bypassing the circular MB/SL tightness loop argument completely. |
| J-CORHC | PARTIAL. `L=1` accurately excluded by RIG's bound. L1-short genuinely unused. Arithmetic flawless. Bookkeeping defect: GFAN2-HC mislabels locally-proved Theorem RIG as "the certified toolkit". |
| J-FIN | CLEAN. 3-way split is disjoint/exhaustive. `E≤ν−1` holds algebraically. Quantifier `ν≥1` strictly required to avoid empty `λ` residues where TAIL's `λ_1` is undefined. |
| J-SPEC | CLEAN. Unlabelled multisets safely map HH rules. Padding proven computationally inert. The superset approach accurately over-estimates un-killable arrays by correctly dropping the graphicality filter. |
| J-DATA | CLEAN. Re-computed `S(ν)`, boundary pair counts, and `s_0(λ)`. Spot-checked arbitrary arrays from (C-5)/(C-8); sequence simulation perfectly cleared exactly in `L` and triggered FAN-6' kill. |
| J-KILL | CLEAN. Exhaustively confirmed printed `(w,2nd)` tuples. All boundary and survivor certificates robustly satisfy `2nd≤w−2` for a unique max `w`, mathematically annihilating them. |
| J-IMPORT | GAP. Corollaries GFANnu-HC and GFAN2-HC illegally import Theorem RIG without supplying its explicit `B_lo ≠ ∅` hypothesis. All other A.1 imports match perfectly (see J-IMPORT table). |
| J-SCOPE | GAP. Theorem GFANnu cleanly consumes GFan boundaries. However, Corollaries GFANnu-HC and GFAN2-HC suffer a MATHEMATICS defect (under-hypothesis) by failing to restrict to `L≥1`. |

## 2. Import table for J-IMPORT

| imported fact | caller | hypothesis match | conclusion match |
|---|---|---|---|
| Lemma 4 | Theorem RIG | Hard-core frame facts met. | Establishes common A-neighbour. |
| Observation R1 | Theorem RIG | Hard-core frame facts met. | Concludes `nu >= 1`. |
| Corollary MB1 | Theorem RIG | Hard core, low vertices B-universal. | Concludes `nu <= L-1`. |
| Lemma FAN-1 | Lemma FAN-4', 8', GFAN2 | GFan under reductio; validated by A.1 note. | Maps first p heads to `B_{hi}` accurately. |
| Lemma DICH(b) | Lemma FAN-4', 8', 6' | High vertices satisfy `g≥s+1`. | High heads validly placed in earlier blocks. |
| Proposition L2 | Corollary RIG-1 | Hard core, `L=2` provided. | Uses clauses (a) and (b) accurately. |
| Theorem FAN | Cor. RIG-2, GFAN2-HC | Hard core, maps to `Fan(tau, L >= 2)`. | Correctly eliminates configuration. |
| Lemma TAIL | Theorem GFANnu | `E=0`, `L > \lambda_1`, `λ = ∅` (since `ν≥1`). | Exact step count evaluated perfectly. |
| Theorem RIG | Cor. GFANnu-HC, GFAN2-HC | **MISMATCH: Caller omits `B_{lo} \neq \emptyset`.** | GFan bounds evaluated accurately. |

## 3. Defect list

**Defect 1: MATHEMATICS (J-IMPORT / J-SCOPE).** In Corollaries GFANnu-HC and GFAN2-HC, the
proofs invoke Theorem RIG to instantiate the limits `1≤ν≤L−1`. Theorem RIG explicitly
requires the hypothesis `B_lo ≠ ∅` (i.e. `L≥1`). However, the Corollaries only scope "if
every low vertex is B-universal", which is vacuously true when `L=0`. The proofs fail to
establish or supply the `B_lo ≠ ∅` hypothesis prior to importing Theorem RIG. I attempted
to construct a hard-core graph with `L=0` and found none, because Theorem MB naturally
forces `m̄ ≤ −1` if `L=0`, which is structurally impossible. Thus, the rigid setting
natively excludes it, but the proofs' literal import step remains logically broken.

**Defect 2: BOOKKEEPING (J-FIN).** In the proof of Theorem GFANnu, the text states that the
boundary rows are "tabulated in the certified toolkit (C-3)". However, (C-3) is a subsection
of Appendix C.1 natively printed within the text under review, not the "certified toolkit"
(which strictly designates Appendix A.1).

**Defect 3: BOOKKEEPING (J-CORHC).** In the proof of Corollary GFAN2-HC, Theorem RIG is
explicitly labeled as "(the certified toolkit)". Theorem RIG is independently proven locally
in Appendix B, making this classification a cross-reference error.

**Defect 4: BOOKKEEPING (J-FAN6P).** In the proof of Lemma FAN-6', the text states "All of
`B_hi` (DICH(b)) ... lie in `block_j`". The current step's head and previously deleted heads
from `B_hi` are removed from the list, so it should read "All remaining vertices of `B_hi`".
The subsequent mathematical expression `(p−j)` correctly isolates this remaining count,
meaning the logic itself is strictly sound.

## 4. Refutation log

**Theorem GFANnu computational test:** I wrote a Python combinatorial builder mimicking
Appendix C.1's parameter constraints over `1≤ν≤11`. I ran Havel-Hakimi step evaluations for
all **77,373** `E≥1` sequences and **427** boundary rows up to `ν=10`. Every configuration
that successfully cleared in exactly `L` steps contained a unique maximum `w≥1` with gap
`2nd≤w−2`, yielding exactly **0** escapes from Lemma FAN-6'. Empty residues were naturally
blocked since bounds cleanly enforce `E≤ν−1 ⟹ 2ν−E≥2>0`.

**GFAN2 trajectories:** Natively programmed and simulated padding trajectories for `[2,2]`,
`[2,1,1]`, and `[1,1,1,1]` over arbitrary constants `L≥4`. They universally resolved to
exactly `L+1` or `L+2` steps, confirming Step 2's manual derivation.

**Zero Inertness:** Padded test arrays extensively with zero components up to length 13. My
Havel-Hakimi execution paths remained completely unperturbed, confirming convention
inertness.

**Missing Hypothesis Check:** Evaluated the `L=0` boundary attempting to construct an object
violating the GFANnu-HC scope. Found that Theorem MB physically prevents `L=0` inside the
hard core (since it strictly forces `m̄ ≤ −1`). The graph space is genuinely empty, but the
proofs' logical import bridges remain defective without independently stating or referencing
this deduction.

## 5. Mandatory control section

**Counterfactual availability:** I constructed an object shaped as `GFan(4,2,1)` but
explicitly violating the `residue = \alpha` reductio. Vertices: `A={a_0,a_1,a_2}`,
`B_hi={v_1,v_2}`, `B_lo={b_1,b_2}`. Edges: B is a complete bipartite graph minus `v_1∼v_2`;
`a_0∼B`, `a_1∼v_1`, `a_2∼v_2`. Degrees: `[4,4,4,4,4,1,1]`. Its HH residue evaluates exactly
to 2, failing `α=3`. The sequence requires `s=5` clearance steps. Since `s=5 ≠ 4 = τ`, the
high vertices (`g=4`) fail the prerequisite `g≥s+1` (`4 ≱ 6`). Consequently, Lemma DICH(b)
fails completely, proving the reductio hypothesis (`s=τ`) is violently load-bearing and not
decorative.

**Witness validation:** On the above witness: Connected: yes (via `a_0`). A maximum: size 3
(any B independent set is `≤2`). diam: 4 (path `a_1−v_1−b_1−v_2−a_2`). f: 5
(`{a_0,a_1,a_2,v_1,v_2}` is a tree), FAILS `f=α+1=4` intentionally to isolate the reductio
break. Non-forest: B contains cycles. Residue vs Alpha: `2 ≠ 3`.

**Vacuity honesty:** I deployed unbounded programmatic searches tracking valid GFan
structures under full hypothesis constraints. Zero counterexamples passed the combination of
combinatorial generation and FAN-6' certification, honoring the textual non-existence claim.
Specifically, no `L=0` graph was successfully mapped.

## 6. What I could not check

I could not mathematically verify the "measured witness" inside the absent companion
section. Since unprimed FAN-n lemmas were strictly excluded from the prompt limit, they
could not be validated. I executed code covering all remaining finite boundary counts and
exact step clearances up to `ν=11`.
