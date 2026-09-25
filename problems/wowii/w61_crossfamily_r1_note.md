> Verified by OpenAI GPT-5/Codex, 2026-08-23. 57 citations opened, 44 load-bearing numbers re-derived.

# Findings

## 1. CLAIM EXCEEDS EVIDENCE — Fact F-b contains a false extra conclusion

Exact passage (Fact `fact:Fb`):

> “In the hard-core frame there exist occurring types $T_1,T_2$ that are disjoint and have no $G[B]$-edge between them. **In particular a singleton type occurs.**”

The proof establishes the first sentence and does not establish the bold sentence. The latter is false. An exhaustive scan using the permitted primitives in `w61_cstar.py` found the following eight-vertex hard-core-frame instance:

```text
E = {01,05,06,12,14,23,25,34,45,70,71,75,76}
A = {1,3,5,6},  B = {0,2,4,7},  alpha = 4,  f = 5,  diam = 4.
occurring types (with multiplicity) = {0,2,4,7}, {0,2,4,7}, {0,7}, {2,4}.
```

There are disjoint witness types `{0,7}` and `{2,4}`, with no edge between them, but no occurring singleton type. Thus the displayed proof supports the diameter-witness clause but not “In particular a singleton type occurs.” The attached `certified` marker also exceeds the mathematical text in this clause. I did not find a downstream argument in the paper that actually consumes the singleton add-on; downstream uses consume nonempty disjoint types.

## 2. UNEXECUTED VERIFICATION CLAIM — several `certified` markers are not supported by the paper's own ledger

The marker definition says `certified` means two clean rounds from distinct model families and says Appendix A reproduces the evidence for every such statement. The following instances do not meet that description in the supplied paper:

- Lemma `lem:S` and Lemma `lem:T` cite rows R-11/R-12. The ledger records only “verification pass (Qwen3.8-Max), joint V-M1”; it records no second model family.
- Lemma `lem:pair`, Observation `obs:R1`, Fact `fact:Fb`, and Lemma `lem:Cstar` cite a “root-reduction block,” but no root-reduction row appears in the ledger at all.
- Theorem `thm:tau2` cites a “closeout block”; the ledger's R-13 entry names only Theorem `thm:T3`, not `thm:tau2`.
- More generally, the actual review reports are not among the Appendix's permitted evidence files. The Python checkers can re-evaluate mathematics, but cannot establish that two named review rounds occurred, belonged to distinct families, or reviewed final repaired text.

This directly contradicts the abstract's/process section's assertion that Sections 4–9 contain only statements that survived two distinct-family rounds. It is a status defect independent of whether the displayed mathematics is correct.

## 3. CLAIM EXCEEDS EVIDENCE — “we settle $\tau\le3$ completely” relies on an omitted proof

Exact abstract passage:

> “we settle $\tau\le3$ completely”

Theorem `thm:T3` is the load-bearing $\tau=3$ result, but the paper supplies only a proof skeleton and explicitly says the certified branch-by-branch proof is in a source report. That report is not named in Appendix B and the task's read restriction forbids opening the likely source-report location. The permitted computations reproduce the bounded boxes and structural subclaims, not the universal case analysis. I therefore could not independently verify “settle” from the paper as written. This is also the sole numbered statement whose mathematical proof could not be checked end-to-end.

## 4. UNSOURCED NUMBER — the C* marker says 340 graphs; the named script says 332

Exact passage (Remark `rem:obstacle-tau`):

> “restricted to the hard-core frame: $340$ graphs, $399$ pairs …”

Observed output of `python3 problems/wowii/w61_cstar.py`:

```text
[C* +n=8 cover] hard-core graphs=332 (F-b) pairs=399 C* failures=0
[C*] hard-core tau histogram: {2: 14, 3: 200, 4: 118}
```

The paper prints the same histogram, and `14+200+118=332`. The claimed 340 is a transcription/count error. The 399-pair and zero-failure claims match.

## 5. UNSOURCED NUMBER — the paper counts ten one-round statements, but contains seven

Exact passages:

> “Exactly ten statements sit at one round”

and

> “Ten statements are one round short”

Section `sec:oneround` contains seven numbered assertions: `lem:FAN4p`, `lem:FAN8p`, `lem:FAN6p`, `thm:GFAN2`, `cor:RIG1`, `cor:GFAN2HC`, and `cor:GFAN2L3`. The summary table and certification ledger list those same seven. The count ten is wrong.

## 6. UNSOURCED NUMBER — the Theorem SL corpus description treats a cumulative count as an additional count

Exact marker (Remark `rem:SLsharp`):

> “$2,740$ trajectories on the exhaustive atlas $n\le7$ **and $19,710$ on** $9,000$ random graphs … plus $4,000$ near-split graphs”

`w61_r4_thmSL.py` prints 2,740 after the atlas, then 19,710 after adding the random and near-split corpora. Its counter is cumulative; the non-atlas increment is 16,970, not 19,710. The proof-check outcomes (1,925 stronger-claim counterexamples, 2,300 equality heads, and histogram `{2:2300}`) match. If “19,710” was intended as the final cumulative total, the word “on” is misleading; read literally as written, the scope is overstated by 2,740.

## 7. UNSOURCED NUMBER — the base Fan-box counts are not produced by the cited script's documented execution

Appendix B.4 attributes 63,239 strict and 99,619 superset sequences to `w61_r4_fanL.py`, but supplies no parameter invocation for those figures. Executing the current script with its own defaults (`tau_max=9`, `R_max=20`, `K_max=16`) gives 736,630 strict and 1,101,234 superset sequences. The separately displayed enlarged box is reproducible exactly with `w61_r4_fanL.py 10 20 14` (1,098,141 strict and 1,700,094 superset, all gap one), so this is a provenance/count defect in the smaller Appendix inventory item, not a failure of the displayed enlarged experiment.

## 8. MISATTRIBUTED CITATION — `w61_r13_adjudicate.py` does not diff against the published paper

Appendix B.5 says the later adjudication scripts parse “this paper” and diff its printed data against an independent recomputation. The source of `w61_r13_adjudicate.py` instead hard-codes:

```python
DRAFT = "$HOME/workspace/claudecode/automath/notes/proofs/wowii61_draft.md"
draft = open(DRAFT, encoding="utf-8").read()
```

That is a different artifact, and it is explicitly forbidden by this task. I therefore did not run the script. The published Appendix C data do independently match `w61_r12_gfannu_embed.py`, but the specific “diffed against this text as parsed from the file” claim attached to the 282 values is unsupported by the cited script.

## 9. CLAIM EXCEEDS EVIDENCE — the script inventory's universal calibration claim is false

Exact Appendix B passage:

> “Each begins by recomputing the two calibration values $\res(K_2)=1$ and $\res(C_n)=\lceil n/3\rceil$ for $n=3,\dots,9$ …”

Only eight of the 49 directly named `problems/wowii/w61_*.py` files even contain both calibration blocks: `w61_S3_76_sol_check.py`, `w61_S3_GFAN_sol_check.py`, `w61_S3_TAIL_spark_check.py`, `w61_r10_adjudicate.py`, `w61_r11_adjudicate.py`, `w61_r12_adjudicate.py`, `w61_r13_adjudicate.py`, and `w61_r6_q14check.py`. The remaining 41 do not begin with—indeed do not contain—the claimed pair of calibrations:

`w61_S3B_K_avail.py`, `w61_S3B_K_exh.py`, `w61_S3B_K_hh.py`, `w61_S3B_K_probe.py`, `w61_S3B_T3_probe.py`, `w61_adjudicate.py`, `w61_adjudicate_r4.py`, `w61_blockocc.py`, `w61_cstar.py`, `w61_famgen.py`, `w61_lemH.py`, `w61_r10_build_sol_brief.py`, `w61_r10_build_spark_brief.py`, `w61_r12_build_gfannu_brief.py`, `w61_r12_build_sol_gfan_brief.py`, `w61_r12_c1_probe.py`, `w61_r12_c1k2.py`, `w61_r12_gfannu_embed.py`, `w61_r12_gfannu_ext.py`, `w61_r13_padding_ext.py`, `w61_r3_repair.py`, `w61_r4_a2check.py`, `w61_r4_fan.py`, `w61_r4_fanE.py`, `w61_r4_fanL.py`, `w61_r4_fanmech.py`, `w61_r4_fanres.py`, `w61_r4_low.py`, `w61_r4_mb.py`, `w61_r4_slack.py`, `w61_r4_thmSL.py`, `w61_r5_a2check.py`, `w61_r5_bcheck.py`, `w61_r5_generalS.py`, `w61_r5_gfan2.py`, `w61_r5_jcheck.py`, `w61_r5_rig.py`, `w61_r5_t3check.py`, `w61_tau3.py`, `w61_tau3_struct.py`, `w61_thmK_check.py`.

## 10. CLAIM EXCEEDS EVIDENCE — not every listed script is stand-alone

Exact Appendix B passage:

> “Every script below is a stand-alone Python program in the campaign repository.”

Counterinstances:

- `w61_S3B_T3_probe.py` ends in `if __name__ == '__main__': pass`; executing it performs no check and emits no result.
- The four brief builders require the forbidden draft and additional unlisted prompt files: `w61_r10_build_spark_brief.py`, `w61_r10_build_sol_brief.py`, `w61_r12_build_gfannu_brief.py`, and `w61_r12_build_sol_gfan_brief.py`.
- `w61_r6_q14check.py` and `w61_r13_adjudicate.py` read the forbidden draft at runtime.
- The primary verifier is named as `notes/proofs/wowii61_verify.py`, outside the only directory the hard read restriction authorizes for evidence files.

## 11. MISATTRIBUTED CITATION — one bibliography entry is unused

The `funsearch` bibliography entry resolves and its metadata are accurate, but no `\cite{funsearch}` or prose attribution to it occurs anywhere in the paper. It is an over-cited/unused bibliography entry.

## 12. Wording/implication audit

I found no instance where the paper silently upgrades “A and B would imply C” to C itself. In particular, the abstract separates the tiers; Section `sec:open` says “granting Theorem GFANnu at its current tier”; and the limitations explicitly say `cor:GFANnuHC` should not be quoted as established. Apart from the $\tau\le3$ “settle” wording and the status-marker defects above, the verbs “implies,” “reduces,” “eliminates,” and “forces” track the displayed proofs.

# Could not verify

- `notes/proofs/wowii61_verify.py` (the source of stages A–E, coverage rates, witnesses W1–W7, the 150,905-run execution, and the 30,995-run stage E) could not be opened or run: the task permits only evidence files directly under `problems/wowii/`.
- The complete branch proof behind Theorem `thm:T3` could not be opened: it is not in the paper and the source report is outside the permitted set.
- The actual review reports behind every `Scert`/`Sone` process assertion are not named in Appendix B. Python checkers do not verify reviewer identity, model family, report contents, or whether final repaired text was read.
- `w61_r6_q14check.py` and `w61_r13_adjudicate.py` could not be executed without causing a forbidden read of `notes/proofs/wowii61_draft.md`.
- The four brief builders could not be executed without reading the forbidden draft and unlisted prompt files.
- The large round-B claims (89.8M tuples to $n\le37$, 77.9M tuples to $n\le73$, 7.7M huge-multiplicity instances, $2^{21}$ brute force, 5,842,009 trajectories over 28,163 graphs) were not rerun. `w61_S3B_T3_probe.py` has no executable main, and reconstructing the undocumented invocations would exceed the paper's stated seconds/100-second script scope.
- The three 2026 H. Chen companion works (`batch1`, `fernandespaper`, `etp677`) could not be located by exact-title web and Zenodo searches; no URL, DOI, venue, or repository path is supplied.
- Havel's original Czech text and the full paywalled papers of Hakimi/Favaron–Mahéo–Saclé/Griggs–Kleitman were not all available as full text. Bibliographic metadata and attributed results were cross-checked using the publisher pages and independent scholarly summaries.
- The paper's asserted absence of prior literature on WOWII-61 was not independently re-run as a systematic literature review; exact-title/conjecture searches found no prior treatment beyond the formal corpus.

# Numbered-statement audit

| Statement | Marker | Audit of mathematical wording and marker |
|---|---|---|
| `lem:hh` | elementary | Proof complete; wording supported. |
| `fact:fms` | computational/cited | Mathematical attribution supported externally; 30,995-run marker not executable under restriction. |
| `lem:f-alpha` | elementary | Proof complete. |
| `thm:diam3` | elementary | Proof complete. |
| `lem:starforest` | elementary | Proof complete. |
| `thm:packing` | elementary | Proof complete. |
| `cor:B1` | elementary | Greedy path argument and floor bound check out. |
| `cor:B2` | elementary | Direct check of $d=1,\ldots,9$ gives exactly the printed six diameters. |
| `thm:matching` | elementary | Proof complete. |
| `cor:C1` | elementary | Proof complete. |
| `thm:equivform` | elementary | Algebraic equivalence complete. |
| `prop:dichotomy` | elementary | Conditional conclusion is stated conditionally and proved. |
| `lem:S` | certified | Mathematical proof complete; two-family marker unsupported by ledger R-12. |
| `lem:F3prime` | certified | Mathematical proof complete; computation reproduced. Review-process claim not independently inspectable. |
| `lem:T` | certified | Mathematical proof complete; two-family marker unsupported by ledger R-11/R-12. |
| `lem:Zplus` | certified | Proof complete; numerical checks reproduced. Review-process claim not independently inspectable. |
| `lem:DICH` | certified | Proof complete; boundary checks reproduced. Review-process claim not independently inspectable. |
| `thm:K` | certified | Proof complete; 114,914/1,464 check reproduced. Review-process claim not independently inspectable. |
| `cor:K1` | certified | Follows from `thm:K` and `obs:R1`; process claim not independently inspectable. |
| `lem:pair` | certified | Proof complete; root-reduction certification absent from ledger. |
| `obs:R1` | certified | Proof complete; root-reduction certification absent from ledger. |
| `fact:Fb` | certified | Main diameter-witness clause proved; singleton add-on false; root-reduction certification absent. |
| `lem:Cstar` | certified | Proof complete for witness types; root-reduction certification absent; marker's 340-graph count wrong. |
| `thm:tau2` | certified | Displayed proof is sufficient; closeout certification absent from ledger. |
| `thm:T3` | certified | Only a skeleton is present; universal case proof and two-round record could not be verified. |
| `lem:HI` | certified | Proof complete. |
| `thm:LOW` | certified | Position-sum algebra checks out; numerical check reproduced. |
| `thm:SL` | certified | Six-step contradiction checks out; numerical check reproduced, with cumulative-scope wording error noted above. |
| `cor:SLHC` | certified | Logical dependencies support $L\ge2$. |
| `thm:MB` | certified | Degree count and substitution check out. |
| `cor:L1short` | certified | Follows from MB and R1. |
| `cor:MB1` | certified | Proof complete. |
| `prop:L1` | certified | Proof complete. |
| `cor:L1prime` | certified | Immediate numerical substitution. |
| `prop:L2` | certified | All five clauses follow from the displayed squeeze and pairing argument. |
| `lem:FAN1` | certified | Tie-fixing and induction support the claim. |
| `lem:FAN3` | certified | Induction supports exactly $L+1$ steps. |
| `lem:FAN4` | certified | Decrement count checks out. |
| `obs:FAN5` | certified | Both trajectories reproduced; second follows from TAIL. |
| `lem:FAN7` | certified | Escape count and graphicality contradiction check out. |
| `lem:FAN8` | certified | Block-size inequality checks out. |
| `lem:FAN6` | certified | Backward induction checks out; mechanism run agrees. |
| `thm:FAN` | certified | Follows from FAN1/8/4/6/3; large box reproduced. |
| `obs:FANE` | computational | All printed large-box and mechanism counts reproduced. |
| `cor:FANHC` | certified | Follows from K/L1short/L2/FAN. |
| `lem:TAIL` | certified | Proof complete; 1,817-pair check reproduced. |
| `lem:CAP` | certified | One-line degree bound correct. |
| `cor:CAP1` | certified | Immediate. |
| `thm:RIG` | certified | Five clauses follow as written; targeted computation reproduced. |
| `cor:RIG2` | certified | Follows from RIG, MB1, and FAN. |
| `lem:FAN4p` | one round | Proof count correct; one-round process report unavailable. |
| `lem:FAN8p` | one round | Proof inequality correct; one-round process report unavailable. |
| `lem:FAN6p` | one round | Backward induction correct with stated second-entry convention; process report unavailable. |
| `thm:GFAN2` | one round | Eight-row and $L\ge4$ cases reproduced; process report unavailable. |
| `cor:RIG1` | one round | Follows from certified inputs; process report unavailable. |
| `cor:GFAN2HC` | one round | Proof correct; process report unavailable. |
| `cor:GFAN2L3` | one round | Immediate from previous corollary. |
| `thm:GFANnu` | zero rounds | Finite enumeration reproduced exactly for $1\le\nu\le6$; current positivity repair is present. |
| `cor:GFANnuHC` | zero rounds | Correct conditional consequence of RIG and GFANnu. |
| `prop:K5` | computational | Complete-graph family checked directly; second-implementation process claim not executable under restriction. |

# Per-citation table

The status vocabulary is exactly the one requested. “Opened” means the cited object/source was inspected, not merely that a filename existed.

| Citation/source | Status | What was checked / observed |
|---|---|---|
| `formalconjectures` | `says-what-we-claim` | [GraphConjecture61.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/WrittenOnTheWallII/GraphConjecture61.lean) has the quoted theorem, assumptions, K2 example, and Graffiti.pc attribution; [Residue.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjecturesForMathlib/Combinatorics/SimpleGraph/Residue.lean) implements the described step and residue recursion. |
| `havel` | `says-what-we-claim` | Title/year/volume/pages and Havel graphicality result resolve (DOI 10.21136/CPM.1955.108220). |
| `hakimi` | `says-what-we-claim` | [SIAM publisher record](https://epubs.siam.org/doi/abs/10.1137/0110037) confirms author/title/volume/pages and degree-sequence realizability result. |
| `fms` | `says-what-we-claim` | [Wiley record](https://doi.org/10.1002/jgt.3190150107) confirms metadata; [independent graph-theory summary](https://dwest.web.illinois.edu/regs/hhresidue.html) explicitly attributes $\res(G)\le\alpha(G)$ to Favaron–Mahéo–Saclé. |
| `gk` | `says-what-we-claim` | The same scholarly summary identifies the simpler proof; bibliographic data match Discrete Math. 127 (1994), 209–212. |
| `mathlib` | `says-what-we-claim` | CPP metadata/DOI 10.1145/3372885.3373824 resolve; current [diameter docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Diam.html) and [finite-graph docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Finite.html) contain `SimpleGraph.diam` and `degree`. |
| `batch1` | `COULD-NOT-OPEN` | Exact-title and Zenodo searches found no object; bibliography supplies no URL/DOI/venue. |
| `fernandespaper` | `COULD-NOT-OPEN` | Exact-title and Zenodo searches found no object; bibliography supplies no URL/DOI/venue. |
| `etp677` | `COULD-NOT-OPEN` | Exact-title and Zenodo searches found no object; bibliography supplies no URL/DOI/venue. |
| `funsearch` | `MISATTRIBUTED` | [Nature record](https://www.nature.com/articles/s41586-023-06924-6) confirms metadata, but the entry is never cited or attributed in the paper. |
| `erdosproblems` | `says-what-we-claim` | [Wiki policy](https://github.com/teorth/erdosproblems/wiki/AI-contribution-section-placement-system) explicitly warns of reporting bias; the official forum distinguishes an argument from formal/peer/expert verification. |
| `notes/proofs/wowii61_verify.py` | `COULD-NOT-OPEN` | Explicitly outside the hard-read permission for evidence scripts. |
| `w61_lemH.py` | `says-what-we-claim` | Ran: 116,873 connected evaluations, 36,612 reductio hits, zero listed failures. |
| `w61_blockocc.py` | `says-what-we-claim` | Ran: 116,189 evaluations, 36,664 reductio hits, zero failures. |
| `w61_thmK_check.py` | `says-what-we-claim` | Ran: 114,914 graphs, 1,464 hypothesis hits, zero non-cliques. |
| `w61_cstar.py` | `MISATTRIBUTED` | Ran: 332 frame graphs, not 340; 399 pairs and zero C* failures do match. |
| `w61_famgen.py` | `says-what-we-claim` | Ran both unbounded-frame family samples for printed ranges; zero membership violations. |
| `w61_tau3.py` | `says-what-we-claim` | Ran: 1,119,744 tuples, 591,710 frame instances, printed cell counts and minimum slack match. |
| `w61_tau3_struct.py` | `says-what-we-claim` | Ran: 147,348 instances and all structural/family checks with zero failures. |
| `w61_r5_t3check.py` | `says-what-we-claim` | Ran: 12,288 graphs and zero hard-core instances; closed-form diameter branch reproduced. |
| `w61_r3_repair.py` | `says-what-we-claim` | Ran: repair checks reproduce their stated local scope. |
| `w61_r5_jcheck.py` | `says-what-we-claim` | Ran: unique $k=0$ trajectory and infinite-family diameter argument reproduce the paper's repaired skeleton. |
| `w61_r4_low.py` | `says-what-we-claim` | Ran: 6,403 graphs, 34,040 trajectory checks, LOW identities and slack minima match. |
| `w61_r4_slack.py` | `says-what-we-claim` | Ran: 5,913 graphs, 26,514 checks, 1,240 $L=1$ cases, all profile `(1,0)`. |
| `w61_r4_thmSL.py` | `MISATTRIBUTED` | Ran: outputs 2,740 atlas then 19,710 cumulative; paper describes 19,710 as though on the added corpora. Other printed counts match. |
| `w61_r4_mb.py` | `says-what-we-claim` | Ran: no failures in MB/rigid-low checks. |
| `w61_r5_generalS.py` | `says-what-we-claim` | Ran general-$s$ terminal/head tests with zero failures; paper's 19,324/14,784 corpus comes from `w61_adjudicate_r4.py`, not this file alone. |
| `w61_r4_fanL.py` | `MISATTRIBUTED` | The enlarged published box matches exactly, but the script's default run gives 736,630 strict and 1,101,234 superset sequences, not Appendix B.4's unexplained 63,239 and 99,619. |
| `w61_r4_fanmech.py` | `says-what-we-claim` | Ran: 64,911 high-phase traces; 46,138 controls with 36,650 clique hits; zero mechanism failures. |
| `w61_r4_fanres.py` | `says-what-we-claim` | Ran: 450,303 suffix cases, all `(1,1)`; tail step counts match. |
| `w61_r4_fanE.py` | `says-what-we-claim` | Ran: 508,239 traces and zero structural failures. |
| `w61_r4_fan.py` | `says-what-we-claim` | Ran finite Fan$(\tau,2)$ box: 114,157 realizable cases and zero survivors. |
| `w61_r5_bcheck.py` | `says-what-we-claim` | Ran TAIL/FAN5 boundary checks; outputs agree with repaired text. |
| `w61_r5_rig.py` | `says-what-we-claim` | Ran all four corpora; 1,926 universal-low vertices and 31/31 targeted RIG hypotheses match. |
| `w61_r5_gfan2.py` | `says-what-we-claim` | Ran direct $\nu=2$ and lead tables; the two singleton residues are the only exact-$L$ survivors in the theorem's finite cases. |
| `w61_r12_gfannu_embed.py` | `says-what-we-claim` | Ran: complete $\nu\le6$ printed enumeration matches Appendix C. |
| `w61_r13_padding_ext.py` | `says-what-we-claim` | Ran: 964+1,745 base rows times seven paddings = 18,963, zero mismatches. |
| `w61_r12_gfannu_ext.py` | `says-what-we-claim` | Ran $\nu\le10$ extension; no missed survivors. |
| `w61_r12_c1_probe.py` | `says-what-we-claim` | Ran: 10,268 terminating lists through size 28, zero violations. |
| `w61_r12_c1k2.py` | `says-what-we-claim` | Ran: 1,830 two-part pairs to $w=60$ and 79 auxiliary cases, zero mismatches. |
| `w61_adjudicate.py` | `says-what-we-claim` | Ran: reproduces K2,3 counterexample and listed T3 repairs. |
| `w61_adjudicate_r4.py` | `says-what-we-claim` | Ran: 19,324 trajectories, 14,784 off-reductio, zero repaired-lemma failures. |
| `w61_r4_a2check.py` | `says-what-we-claim` | Ran: general-$s$ and repaired T3 checks return zero mathematical failures. |
| `w61_r5_a2check.py` | `says-what-we-claim` | Ran: Fan controls and availability claims reproduced. |
| `w61_r6_q14check.py` | `COULD-NOT-OPEN` | Source opens the forbidden draft at runtime; not executed. |
| `w61_r10_adjudicate.py` | `says-what-we-claim` | Ran: TAIL repairs and boundary controls reproduced. |
| `w61_r11_adjudicate.py` | `says-what-we-claim` | Ran: 3,125 in-scope pairs, zero mismatch; 1,211 out-of-scope pairs/462 mismatches. |
| `w61_r12_adjudicate.py` | `says-what-we-claim` | Ran: scope controls and calibration reproduced. |
| `w61_r13_adjudicate.py` | `MISATTRIBUTED` | Source parses a forbidden draft, not the published paper; not executed. |
| `w61_S3_76_sol_check.py` | `says-what-we-claim` | Ran: reports zero failures over its stated checks. |
| `w61_S3_GFAN_sol_check.py` | `says-what-we-claim` | Ran: reproduces GFAN enumeration, K5 refutation, and RIG control. |
| `w61_S3_TAIL_spark_check.py` | `says-what-we-claim` | Ran: 3,125 in-scope/zero mismatches and 1,211 out-of-scope/462 mismatches. |
| `w61_S3B_K_hh.py` | `says-what-we-claim` | Ran: 3,646 graphs, 18,230 traces, zero listed failures. |
| `w61_S3B_K_exh.py` | `says-what-we-claim` | Ran: 997,517 legal executions over 1,036 graphs plus exhaustive $\tau=2,3$ K-regime scans, zero theorem failures. |
| `w61_S3B_K_avail.py` | `says-what-we-claim` | Ran: 15,057 traces and availability/control claims reproduced. |
| `w61_S3B_K_probe.py` | `says-what-we-claim` | Ran boundary and choice-of-$A$ probes without theorem failure. |
| `w61_S3B_T3_probe.py` | `MISATTRIBUTED` | Executing it does nothing (`__main__: pass`); it is not a stand-alone executed checker as Appendix B claims. |
| `w61_r10_build_spark_brief.py` | `COULD-NOT-OPEN` | Runtime requires forbidden draft and unlisted prompt artifacts. |
| `w61_r10_build_sol_brief.py` | `COULD-NOT-OPEN` | Runtime requires forbidden draft and unlisted prompt artifacts. |
| `w61_r12_build_gfannu_brief.py` | `COULD-NOT-OPEN` | Runtime requires forbidden draft. |
| `w61_r12_build_sol_gfan_brief.py` | `COULD-NOT-OPEN` | Runtime requires forbidden draft and unlisted prompt artifact. |

# Per-number table

Rows group coupled values that are produced by one derivation/run. “Independent” means I ran the named allowed script or recomputed the arithmetic/proof directly; it does not mean the campaign's second implementation.

| Paper claim | Independent result / method | Verdict |
|---|---|---|
| $\res(K_2)=1$; $\res(C_n)=\lceil n/3\rceil$, $3\le n\le9$ | Direct HH runs in six independent allowed checkers gave `1; 1,2,2,2,3,3,3`. | `MATCH` |
| Settled diameters $\{1,2,3,5,6,9\}$ | Hand-evaluated $\lfloor(d-1)/4\rfloor+1\ge\lceil d/3\rceil$ for $1\le d\le9$. | `MATCH` |
| For $d\ge10$ the packing bound is short | Hand algebra: $(d+3)/4<d/3$ exactly when $d>9$. | `MATCH` |
| 89.7% ($n\le7$) and 78.4% ($n=8$) diameter-$\le3$ coverage | Source is forbidden primary verifier; no permitted script prints both rates. | `COULD-NOT-REDERIVE` |
| Stage A: 995 connected graphs on $2\le n\le7$ | Atlas runs in `w61_lemH.py` and others gave 995. | `MATCH` |
| Stage B: 853×127=108,331 extension evaluations | Hand multiplication and allowed stage-B loops give 108,331. | `MATCH` |
| 11,117 distinct connected graphs on 8 vertices | Deduplication count is asserted only by forbidden primary verifier/paper. | `COULD-NOT-REDERIVE` |
| Stage C: 1,209 graphs, $n\le26$ | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| D1: 7,994 graphs | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| D2: 32,376 graphs | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| Total 150,905 evaluations | Hand sum $995+108331+1209+7994+32376=150905$. | `MATCH` |
| Stage E: 30,995 rechecks, zero violations | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| Coverage P1/P2/P3/joint $=89.7/74.1/96.1/98.8\%$ ($n\le7$) | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| Coverage P1/P2/P3/joint $=78.4/98.0/93.3/99.2\%$ ($n=8$ prefix) | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| 267 graphs missed; 223/44 by $f-\alpha$; 112/155 by slack | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| Minimum-slack table for $n\le8$ | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| O3: 36.4% of 7,228 graphs | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| Dead route fails for 46.3% | Forbidden primary verifier. | `COULD-NOT-REDERIVE` |
| General-$s$ repair: 19,324 trajectories, 14,784 with $s\ne\tau$, zero failures | Ran `w61_adjudicate_r4.py`; exact output. | `MATCH` |
| Theorem K check: 114,914 graphs, 1,464 hits, zero non-cliques | Ran `w61_thmK_check.py`. | `MATCH` |
| C* marker: 340 graphs, 399 pairs, zero failures | Ran `w61_cstar.py`: 332 graphs, 399 pairs, zero failures; histogram also sums to 332. | `MISMATCH` |
| C* $\tau$ histogram $\{2:14,3:200,4:118\}$ | Ran `w61_cstar.py`; exact. | `MATCH` |
| All-high C* cells 14/14, 91/200, 5/118 | Ran `w61_cstar.py`; exact. | `MATCH` |
| $\tau=3$ box: 1,119,744 tuples; 591,710 frame cases | Ran `w61_tau3.py`. | `MATCH` |
| $\tau=3$ $e_B$ cells 224,035 / 196,075 / 171,600 | Ran `w61_tau3.py`. | `MATCH` |
| $\tau=3$ minimum slack 1, $n=7,m=9$ | Ran `w61_tau3.py`; exact witness. | `MATCH` |
| Structural box: 147,348 instances | Ran `w61_tau3_struct.py`. | `MATCH` |
| Round-B 89.8M/77.9M/7.7M, $n$ up to $10^6$, $2^{21}$, 24,013 near-misses | No executable documented invocation; too expensive and source proof unavailable. | `COULD-NOT-REDERIVE` |
| LOW corpus 6,403 graphs / 34,040 trajectory checks | Ran `w61_r4_low.py`. | `MATCH` |
| LOW slack minima $\{0:0,1:1,2:1,3:2,4:2,5:3,\ldots\}$ | Ran `w61_r4_low.py`; printed extension agrees. | `MATCH` |
| SL corpus 2,740 atlas and 19,710 added-corpus trajectories | Script gives 2,740 then 19,710 cumulative; increment 16,970. | `MISMATCH` |
| 1,925 counterexamples; 2,300 equality heads; $s_j$ histogram `{2:2300}` | Ran `w61_r4_thmSL.py`. | `MATCH` |
| Slack focused corpus 5,913 graphs / 26,514 checks / 1,240 $L=1$ | Ran `w61_r4_slack.py`. | `MATCH` |
| Appendix B.4 base Fan box 63,239 strict / 99,619 superset | Current default `w61_r4_fanL.py` run gives 736,630 / 1,101,234; no invocation is specified for the paper's figures. | `MISMATCH` |
| Fan enlarged box 1,098,141 strict / 1,700,094 superset | Ran `w61_r4_fanL.py 10 20 14`. | `MATCH` |
| Fan mechanism 64,911 runs; control 36,650/46,138 | Ran `w61_r4_fanmech.py`. | `MATCH` |
| Fan high-phase 508,239; suffix 450,303 | Ran `w61_r4_fanE.py` and `w61_r4_fanres.py`. | `MATCH` |
| TAIL 1,817 pairs, zero mismatches | Ran `w61_r11_adjudicate.py` and independent reviewer checker. | `MATCH` |
| RIG corpora 2,931 / 4,382 / 1,737 / 622 pairs | Ran `w61_r5_rig.py`. | `MATCH` |
| 1,926 universal-low vertices, 31/31 targeted hypotheses | Summed/reran `w61_r5_rig.py`. | `MATCH` |
| GFAN2 eight $L=3$ rows and exact step counts | Ran `w61_r5_gfan2.py` and `w61_S3_GFAN_sol_check.py`. | `MATCH` |
| Partition totals $p(2\nu)=2,5,11,22,42,77$; total 159 | Regenerated with `w61_r12_gfannu_embed.py`. | `MATCH` |
| Boundary pair counts 0,1,3,7,14,26; total 51 | Regenerated. | `MATCH` |
| $S(\nu)=0,3,24,110,397,1,211$; total 1,745 | Regenerated and checked closed form. | `MATCH` |
| $E\ge1$ survivor counts 0,1,4,9,20,38; total 72; zero misses | Regenerated complete roster. | `MATCH` |
| $9+72+6=87$ surviving rows killed by FAN6p | Hand sum and regenerated certificates. | `MATCH` |
| 18,963 padding pairs, zero differences | Ran `w61_r13_padding_ext.py`: $(964+1745)\times7=18963$. | `MATCH` |
| “282 printed values” diffed against this paper | Cited script parses a different forbidden draft; the unit counted by 282 is not specified. | `COULD-NOT-REDERIVE` |
| K3 through K8 satisfy the repaired counterexample-family parameters | Direct complete-graph calculation for $3\le n\le8$: $\alpha=\res=1$, $L=\tau=n-1$, $\nu=0$. | `MATCH` |
| K5 explicit $n=5,\alpha=1,f=2,\tau=L=4,\nu=0,\res=1$ | Direct calculation and `w61_S3_GFAN_sol_check.py`. | `MATCH` |
| C1 computation: 10,268 terminating cases, $n\le28$ | Ran `w61_r12_c1_probe.py`. | `MATCH` |
| C1/GFAN extension verified through $\nu\le10$ | Ran `w61_r12_gfannu_ext.py`; rows 1–10 all eliminated. | `MATCH` |
| Exactly ten one-round statements and two zero-round statements | Direct count: seven one-round and two zero-round numbered assertions. | `MISMATCH` |
| Hard core $\tau\ge4$ | Depends on omitted universal T3 proof; bounded boxes agree but do not prove it. | `COULD-NOT-REDERIVE` |
| Hard core $L\ge2$ | Hand-checked deductions from K/R1/MB/SL. | `MATCH` |
| Hard core $L\ge3$ | Hand-checked L=0,1,2 eliminations and Fan proof. | `MATCH` |
| Universal-low certified layer $2\le\nu\le L-1$ | Hand-checked RIG+MB1+FAN deductions. | `MATCH` |
| One-round universal-low layer $\nu\ge3,L\ge4$ | GFAN2 finite proof rerun; logical deduction checks. | `MATCH` |
| Zero-round universal-low layer $\nu\ge7,L\ge8$ | Full $1\le\nu\le6$ enumeration rerun; deduction checks. | `MATCH` |

# Overall verdict

The central finite $\GFan$ enumeration and most displayed elementary/structural arguments reproduce. The paper is not clean enough for an unqualified cross-family sign-off: Fact F-b contains a false clause, several `certified` markers are unsupported by the supplied ledger, Theorem T3 cannot be checked from the permitted paper/evidence, multiple stated corpus/count numbers are wrong or lack reproducible provenance, and Appendix B materially overstates what its scripts do. No repair is proposed here, per the brief.
