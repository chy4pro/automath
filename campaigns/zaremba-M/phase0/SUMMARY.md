# Phase 0 synthesis (recovered from the workflow result; N4/N5, N6, N7, N8 tasks failed on the weekly limit)

**Inputs.**
- Read: A, B (with `B_ledger.py`/`.out`), N1, N3, N9, `BRIEF.md`, `DESIGN.md`, `ledger.md`.
- No report file from anyone: N2 (B §5 settles it), N4, N5 (partly covered by B and N9), N6.
- N7 and N8 exist only as scripts. I ran N7 parts B and F, and N8 `sparse 100003 T1/T2 4,16,64` (Appendix B).
- The owner paused the campaign after Phase 0 (`ledger.md`, 2026-09-26T06:17:48Z). Section 6 applies only once the owner releases Phase 1.

## (1) K0 verdict (collision check): CLEAR

- **No explicit M < 2^2000 is in print or on arXiv** as of 2026-09-26, for large primes or for all q. The only explicit value is Shkredov arXiv:2603.14116v2, Appendix eq. (158): "for sufficiently large q = p one can take M = 2^2000". N9 re-extracted it from the v2 PDF, and A confirms.
- **No v3.** The abs page lists v1 (2026-03-14) and v2 (2026-06-24) only. The OAI datestamp 2026-07-10 is a metadata-only change. N9 and A checked independently.
- **Zhang 2605.02518** has v1 (2026-05-04) and v2 (2026-05-08). Remark 1.3 says M is "effectively computable" and "would produce a large number". No value is given.
- **Other 2025â26 Zaremba-conjecture items** give no explicit absolute M. N9 §2.1 lists 9. ChanâHeilmanâPanova use D = A+1 with A uncomputed.
- **MMS IMRN 2026 rnag048** proves O(log p/log log p), so it cannot contain an absolute M. Its full text is unread (closed access).
- **Citations** (Semantic Scholar, 2026-09-26): 2 for 2603.14116, both read; 0 for 2605.02518.
- **AI-lab and informal sources:** nothing on HN, arXiv cs.*, formal-conjectures or the Quanta API.
  - github cahlen/idontknow calls itself an "incomplete" framework for A = 5, and its Tauberian step is invalid (N9 §3.1). It is not prior art.
- **Coverage gaps:** no agent had general web search. X, Reddit, Google Scholar and the lab blogs are unread. A metadata sweep cannot see an M that appears only in a paper's body.
- **G2 must be re-run before any announcement:** the two abs pages, plus `arxiv.org/search/?query=Zaremba&order=-announced_date_first`.

## (4) Sensitivity table

**Formula ("B-reading").** log2 M_B = 14.785 + log2(1/κ_L14), where:
- 14.785 = log2(4Â·39.6Â·89.1Â·2);
- κ_L14 = c/(6Â·2^{k+4});
- k = â1/câ+1.

Baseline inputs: c_H = 1/20, C1 = 9, C2 = 32, Ï = 1/4. Every row assumes the appendix's step count k (flag F1, see C7).

### 4a. Single changes to the chain

| Change | c | log2 M_B | Î bits | Status |
|---|---|---|---|---|
| Baseline (printed chain, corrected κ) | 1/1640 | **1673.05** | 0 | B. Readings A/C give 1665.8 / 1672.4 |
| **F1 pessimistic** (gain K_*^{-c} per doubling, K_* = p^{Ï/6}, fed into N3 Lemma B) | 1/1640 | â 7Â·10â´ (69kâ79k doublings) | **+6.7Â·10â´** | Unresolved (C7) |
| Symmetrise after BSG, slack formula 0.5c_H/(C1+3C2) | 1/4200 | 4234.4 | +2561 | Needed if no non-symmetric 1/20 exists |
| Symmetrise, sharp formula c_H/(3C2+c_H(1+C1)) | 1/1930 | 1963.3 | +290 | N1 §4(i) |
| Ï read as MMS22's m-coefficient (1/20) | 1/2560 | 2593.7 | +921 | A reading only, not a claim |
| All overheads removed | 1/1640 | 1643.6 | â29.5 | B |
| c_H = 1/15 (needs an SL2 SzÅnyi analogue) | 1/1230 | 1262.6 | â410 | Conditional |
| C2 halved | 1/1000 | 1032.3 | â641 | No source |
| Any c_H â¥ 0.16 | 1/512 (Ï/(4C2) binds) | 543.4 | â1130 | Floor for improving c_H alone |
| **Sharp growth-case bookkeeping** | 1/650 | **681.7** | **â991** | Largest drop from existing lemmas. Bookkeeping, not announceable. Valid only if Lemma 40 holds without symmetry |
| **Remove BSG from all C2-terms** (c_E = c_H = 1/20, slack 0.5) | 1/40 | **67.7** | **â1605** | Largest structural drop. Needs a lemma not in print |
| Same, sharp c_E/(1+c_E) | 1/21 | 47.8 | â1625 | Same |
| BSG-free ceiling (the 1/3 term) | 1/3 | 27.0 | â1646 | Ceiling for any flattening route |

**Biggest single drop:**
- Removing the BSG loss from the flattening step takes 1673 to 68.
- Using existing lemmas only, sharp growth-case bookkeeping takes 1673 to 682. That is not announceable, and it becomes 1963 if the set must be symmetrised.
- The biggest risk is F1, which would raise the baseline by a factor of about 40.

### 4b. Best log2 M per route, if its gap lemma held

| Route | log2 M if the lemma holds | Needed for 500 / 150 |
|---|---|---|
| R1 substitution | â¥ 543.4 for any c_H under the printed min. Sharp bookkeeping gives 681.7. Sharp bookkeeping plus c_H = 1/15 gives 521.3 | Unreachable |
| **R2** (âÂ²-norm gain p^{-c} per doubling) | â1/câ + 5 + log2(6/c) + 14.785. Gives 499.2 at c = 1/468, 149.3 at 1/120, 67.7 at 1/40, 27.0 at 1/3 | c â¥ 1/468 / c â¥ 1/120 |
| **R3** (Cor 16 at interval length N* with saving N*^{-κ0}) | 13.785 + log2(1/κ0). Gives 20.4 at κ0 = 1/100 and 14.8 at the square-root ceiling κ0 = 1/2 | κ0 â¥ 2^{-486.2} / κ0 â¥ 2^{-136.2} |
| **R4** (automorphic gap giving the Cor 16 exponent κ0) | Same formula as R3; at best 14.8 | Same as R3 |
| **R5** (after R3 or R4 succeeds) | 9.10 + log2(1/κ_C), i.e. 10.1 at κ_C = 1/2 (Lemma 10 factor â 1, M*/M â 10, 0.99 â 6/ÏÂ²) | Moonshot only |

## (6) Phase 1: route order, budgets, gap indicators (only once the owner releases it)

About 24M tokens remain under DESIGN (27.5M minus the 3.5M allocated to Phase 0; actual Phase 0 spend is not in `ledger.md`). The hard cap is 30M.

**G0: gate audit (early RB1 plus what remains of R1). 2.0M, 1 agent, about 8 h.** It blocks any claim, but not exploration.
- Settle F1 by re-deriving MMS22 (19) and survey (60) for SL2(F_p) with every constant explicit, giving k as a function of (c, Ï, h0).
- Settle C6: does Lemma 40 need a symmetric set?
- Settle F5: Cor 16 is proved with Lemma 15, but the appendix computes κ for Lemma 14.
- Verify C1 = 9 and C2 = 32, or keep them marked unverified.
- Run the numerics still owed: the N8 grid (p â¤ 2e6, N â¤ 256, T1 and T2) and N7 parts A, C, D, E, G.
- **Gap indicator:** an exact-rational log2 M = F(c, Ï, h0, C1, C2, c_H, overheads), with every term traced to a displayed inequality. It must either reproduce 1673.05 or document the reading under which it does not.
- If F1 comes out pessimistic, report it as a finding about the literature only, and only after RB1 and RB4 have checked it.

**R2: BSG-free flattening. 6.5M. Priority 1.**
- Staffing: explorers E1 (energy / LarsenâPink) and E2 (group action / asymmetric BSG), isolated from each other; then at most 2 provers.
- Why first:
  - A success does not depend on how F1 comes out: the p-scale gain is exactly the reading under which the appendix's k formula holds.
  - It is the only lever inside the growth paradigm.
  - The obvious coset obstruction does not refute it. If μ â¥ p^{-a}u_{gB}, then âμâμâÂ²â â¥ p^{-4a-2}, which only conflicts with the target when h > 2 â 2c + 4a. That is outside the range needed.
- **Gap indicator.** Take any symmetric probability μ on SL2(F_p) with:
  - μ(gH) â¤ p^{-Ï/6} for every coset of every proper subgroup, and
  - p^{-2+2c} â¤ âμâÂ²â â 1/|G| â¤ p^{-h0}.

  Then **âμâμâÂ²â â 1/|G| â¤ p^{-2c}(âμâÂ²â â 1/|G|)**, with c â¥ 1/468 to announce and c â¥ 1/120 for strong. By N3 Lemmas A and B this needs â1/câ+1 doublings.
- Kill (K2): a family inside the range where the inequality fails, or a best provable c < 1/468.
- Give the explorers Lewko 2609.27023 (unrefereed).

**R3: bilinear / incidence bound for Cor 16. 4.0M. Priority 2.**
- Staffing: 1 explorer for at most 18 h. It should first deliver N4 (the Weil / completion ceiling). Then 1 prover.
- Tools: BlomerâPascadi 2607.24311, Pascadi 2511.08445, Lewko 2609.27023.
- **Gap indicator.** Let I = [N*] with **N* = p^{1/90}** (see C9). Take any A = I â Î1 and B = I â Î2 of density â¥ p^{-Î·}, with Î· = 2(1âw_M) â¤ 1.98/M. Then **| |Aâ©B^{-1}| â |A||B|/p | â¤ CÂ·â(|A||B|)Â·N*^{-κ0}** with κ0 explicit and C absolute. This gives log2 M_B = 13.785 + log2(1/κ0).
- Kill (K3): the lemma is shown equivalent to beating the square-root barrier at length p^{1/90}, or the numerics refute it.

**R4: automorphic / thin-group gap. 1.5M (cut from 4.5M). Priority 3, feasibility only.**
- Staffing: 1 explorer for at most 12 h.
- Why cut, from my N7 run:
  - The 3-letter Bruhat words are only about 3.2/N of the lattice points in their box.
  - 5-letter words are thinner: about 10^{-4} at N = 20.
  - The Cor-16 box has about p^{4/90} points, far fewer than the index p+1. So the argument needs long words, where the thinness compounds.
- **Gap indicator** (trace form on PÂ¹, using the operator that Cor 16 actually uses: T2, or T1 if F5 is repaired). For explicit A and κ0 > 0 and some 2k â¤ AÂ·log_N p: **E_{wâS_N^{2k}}[#Fix_{PÂ¹(F_p)}(w)] â 1 â¤ N^{-2kκ0}**. Here the expectation equals 1 exactly for a uniform element (Burnside). This gives Ï(T0) â¤ N^{-κ0}.
- Kill (K4): no fattening lemma whose loss is below the Selberg / KimâSarnak saving.

**R5: overheads. 0.5M, held.** Run only if R3 or R4 produces κ0.
- **Gap indicator:** log2(MÂ·κ_L14) â¤ 10 (baseline 14.785).

**Rest of the budget:** referees RB1âRB4 4.0M, Fable judging and checkpoints 1.5M, reserve 4.0M. Total 24.0M.
- K1 at hour 18 is unchanged.
- Announce only if all of these hold: log2 M â¤ 500 from a new lemma; RB1âRB4 pass; G0 is closed; G2 is re-run clean.

## (2) Negative list (condensed)

1. **Announcing the re-bookkept chain (~1673).** Dead: it is bookkeeping, and it depends on F1.
2. **Improving c_H alone.** Dead. With C2 = 32, c â¤ min{1/256, Ï/128} = 1/512, so log2 M â¥ 543.4. The best c_H in print is still 1/20 (N9 found nothing newer).
3. **BSG constant substitution.** Dead as an announce route. It would need C1+C2 â¤ 11.25 and C2 â¤ 29.25. C1 = 9 and C2 = 32 are themselves unverified: they are not in Murphy's paper, and TaoâVu is unread.
4. **R5 on its own.** Dead: all overheads together are worth at most 29.45 bits.
5. **Re-optimising the iteration.** Dead by N3 Lemma B: the optimum is (2âh0)/g + log2(1/g) + O(1), so re-bookkeeping gains only O(1) bits.
6. **A one-shot Frobenius step, or a pure-girth route.** Dead by N3 Lemma A: it needs certified h > 2, while girth gives h0 â 0.1â0.25. Girth would need to be â³ 4 log_N p; the proven value is 1/4 and the heuristic is about 3.
7. **Asymmetric flattening against a fixed Î½.** Dead: it is circular, since it amounts to Î»(Î½) â¤ p^{-c}.
8. **Lifting the frozen coset cap with âÂ² bounds.** Dead for Borel cosets (N3 Lemma C). Dihedral and exceptional cosets were not analysed.
9. **Fixed-generator explicit gaps** (Kowalski, CalderÃ³nâMagee, BourgainâVarjÃº, BeckerâBreuillard). Dead: the generating set depends on q, with |S| â q^{2Ï}. Soares's result is GRH-conditional.
10. **R4 through Gamburd's Î´ > 5/6.** Dead: Î´_eff â¤ 0.42 at every size tested (N7 F, a crude proxy).
    - The R2 "â70" and DESIGN's "κ = 1/2 â 2^21" (B gives 15.8) must not be quoted. The first needs an SL2 energy lemma with exponent 1/20 and no BSG loss, which is not in any source read.

## (3) Machinery map (condensed)

The chain: (158) â §5.4 condition 1âw_M < 2Îµκ_C/10 â Cor 16 (κ_C = κ/2) â Lemma 15 (used in the proof) / Lemma 14 (κ computed for it) â κ = Î´/6, Î´ = c/2^{k+4}, k = â1/câ+1 â c = min{1/3, 1/(8C2), Ï/(4C2), 0.5c_H/(C1+C2)} = 1/1640.

Nodes, with what could replace each:

- **Flattening count (about 1645 of the 1673 bits).** Structural for dyadic BourgainâGamburd. Replaceable by R2, R3 or R4. Normalisation unresolved (F1).
- **Growth-case term.** No derivation in print; the survey is only an outline. Sharp bookkeeping gives 1/650.
- **Thm 39 (BSG), C1 = 9, C2 = 32.** Unverified. Replaceable by N6 results, or bypassed by R2.
- **Lemma 40, c_H = 1/20.** The RS theorem assumes a symmetric set. "[50, Thm 5]" is the journal numbering; in arXiv v3 the SL2 result is Thm 2. Alternatives: 1/15 (conditional); ceiling 0.3012.
- **1/(8C2).** Its structure is reproduced (the case P*Â³ = G), but not the 8; the sharp value is 1/34.
- **Ï/(4C2).** Not reproduced.
- **1/3 term.** Reproduced exactly; BSG-free. It caps log2 M â¥ 27.0.
- **Girth stage.** Changes the κ prefactor by O(1) bits. Replaceable by Lemma 15 (girth-free).
- **F5.** Cor 16 uses Lemma 15, whose κ is never made explicit.
- **§5.4.** N* = N^{1/10} â¤ q^{1/90}.
- **Thm 38.** Costs 1.97 + 1.41 bits (Hensley; PollicottâVytnova).
- **Prop 35.** Îµ < 1/18; no growth input.
- **Lemma 10.** Costs 2 bits (Remark 11).
- **The true gap is polynomial.** The T1 operator matches 2â(Nâ1)/N, and T2 also has a polynomial gap (Appendix B).

## (5) Contradictions between tasks, resolved

- **C1. 2^-1656 vs 2^-1658.26.** 2^-1656 is Î´; the /6 was dropped. Correct values: κ_L14 = 2^-1658.264 and κ_C = 2^-1659.264. *Resolved.*
- **C2. Ï.**
  - Ï only matters through Ï/(4C2), which binds iff Ï < 16/205. So 1/4, 1/5 and 1/8 all give 1673.05. Only 1/20 binds.
  - The κ prefactor is aÎ´/b, where K = p^a and m = b log_N p: Shkredov Î´/6, MMS22 2Î´/3, MMS18 Î´/4. That is at most about 2 bits apart.
  - *Resolved for the printed chain.* It stays open only through F1 and the unreproduced Ï-term.
- **C3. Baseline.** The spread (1671â1680) comes from different overhead choices. B's 1673.05 is canonical, with 327 bits of slack. *Resolved.*
- **C4. Targets.** Use 1/c â¤ 468 and â¤ 120 (B's exact values). The 470/122 figures come from N3's smaller overhead. *Resolved.*
- **C5. A's "c_H = 0.3 â 273".** Wrong: the 1/256 and 1/512 terms cap c. Saturation is at 543 (B, N1). *Resolved.*
- **C6. Symmetrisation, A's 1/4200 vs N1's 1/1930.** Both are correct under different bookkeeping (slack vs sharp). It matters: slack with symmetrisation gives 4234 > 2000; sharp gives 1963. *Open (RB1).*
- **C7. F1: N3's "within 3â5 bits" vs A/B/N1's "Ã48â72".** N3 did not have the survey. Combining its proved Lemma B with the survey's (60) as N1 read it:
  - The appendix's k = 1641 is reproduced **only** if the gain per doubling is p^{-c} in âÂ² norm, from h0 = 0.
  - K-scale additive gain gives 68,881â77,081 doublings.
  - Survey Thm 49 read literally gives 118,080.
  - My own reconstruction (unverified): the growth-case gain rises with the level h, giving multiplicative flattening with Î² = 1/650 and 1353â2518 doublings. With the slack Î² = 1/1640 it is 3411â6351; with Î² = 1/1930 it is 4014â7473.
  - None of these reproduces 1641 at c = 1/1640, except the p-scale reading and the sharp-Î², h0 = 1/4 case.
  - This does not claim the paper is wrong: the IMRN [43, p.9] it cites is unread. *Open; this is the G0 gate.*
- **C8. Numerics comparator.** Use 2â(Nâ1)/N, the Kesten radius for (Z/2)^{*N}, because the g_j are involutions. The AkemannâOstrand free-group value is the wrong comparator. *Resolved.*
- **C9. R3's interval length is N* â¤ p^{1/90}, not p^{1/9}.** Source: S §5.4 as read by A and B. *Resolved.*
- **C10. Zhang's N^{1/100}.** This is his paraphrase and does not change anything. *Resolved.*

## Appendix A. Derived numbers

- log2 M_B for each c: 1/650 â 681.71; 1/1930 â 1963.28; 1/4200 â 4234.41; 1/490 â 521.31; 1/468 â 499.24; 1/120 â 149.28; 1/40 â 67.69; 1/21 â 47.76; 1/3 â 26.95.
- R3/R4 values of κ0: 1/2 â 14.78; 1/10 â 17.11; 1/100 â 20.43; 1/1000 â 23.75.
- Subgroup cap per doubling: (Ï/6)(2/19) = 0.004386, against a growth gain of 2/650 = 0.003077 at h = 2. The cap does not bind.

## Appendix B. My script runs (p = 100003)

N8 values are Lanczos estimates, which are lower bounds on Ï.

| N | T1 Ï | 2â(Nâ1)/N | T2 Ï | κ_emp(T2) | Harness "free model" for T2 (not valid) |
|---|---|---|---|---|---|
| 4 | 0.86594 | 0.86603 | 0.89676 | 0.0786 | 0.7545 |
| 16 | 0.48416 | 0.48412 | 0.51721 | 0.2378 | 0.4210 |
| 64 | 0.24813 | 0.24804 | 0.24371 | 0.3395 | 0.2162 |

- **N7 part B:** words make up NÂ·ratio = 3.125, 3.125, 3.237, 3.265, 3.230 (divided by N) of the box's lattice points, at N = 10, 20, 30, 40, 50. The predicted limit is ÏÂ²/3.
- **N7 part F:** the words behave as a free product (Z/2)^{*N} in every tested case; Î´_eff â¤ 0.416."
  },
  "workflowProgress": [
    {
      "type": "workflow_phase",
      "index": 1,
      "title": "Warm-up"
    },
    {
      "type": "workflow_phase",
      "index": 2,
      "title": "Synthesis"
    },
    {
      "type": "workflow_agent",
      "index": 1,
      "label": "A_machinery_map",
      "phaseIndex": 1,
      "phaseTitle": "Warm-up",
      "agentId": "af2e6774e06c53223",
      "model": "claude-opus-5-5[1m]",
      "state": "done",
      "startedAt": 1790396666335,
      "queuedAt": 1790396666323,
      "attempt": 1,
      "lastToolName": "StructuredOutput",
      "lastToolSummary": "Zaremba campaign Phase 0, Agent A: map of the machinery in â¦",
      "promptPreview": "ZAREMBA CAMPAIGN, Phase 0 (automath, slot 1). Read first: /work/campaigns/zaremba-M/BRIEF.md and /work/campaigns/zaremba-M/DESIGN.md (the full design: routes R1âR5, negative-list tasks N1âN9, referee briefs). Primary sources to fetch yourself (load WebSearch/WebFetch via ToolSearch "select:WebSearch,WebFetch"; arXiv PDFs via https://arxiv.org/pdf/<id>): Shkredov arXiv:2603.14116v2 (Zaremba for larâ¦",
      "promptFramed": true,
      "lastProgressAt": 1790397288470,
      "tokens": 225362,
      "toolCalls": 50,
      "durationMs": 622132,
      "resultPreview": "{"task":"Zaremba campaign Phase 0, Agent A: map of the machinery in Shkredov arXiv:2603.14116v2, from Theorem 8 down to M = 2^2000. For each node: exact statement, constants it introduces, external inputs, and whether it is structural or replaceable.","status":"done","key_findings":["Dependency tree written. Top: (158) M=2^2000, then (157) max{10(kappa*eps)^-1, M~}. Under that: Section 5.4 conditiâ¦"
    },
    {
      "type": "workflow_agent",
      "index": 2,
      "label": "B_constant_ledger",
      "phaseIndex": 1,
      "phaseTitle": "Warm-up",
      "agentId": "ad2fb709fbafbe668",
      "model": "claude-opus-5-5[1m]",
      "state": "done",
      "startedAt": 1790396666336,
      "queuedAt": 1790396666323,
      "attempt": 1,
      "lastToolName": "StructuredOutput",
      "lastToolSummary": "Zaremba campaign Phase 0, Agent B: exact constant ledger foâ¦",
      "promptPreview": "ZAREMBA CAMPAIGN, Phase 0 (automath, slot 1). Read first: /work/campaigns/zaremba-M/BRIEF.md and /work/campaigns/zaremba-M/DESIGN.md (the full design: routes R1âR5, negative-list tasks N1âN9, referee briefs). Primary sources to fetch yourself (load WebSearch/WebFetch via ToolSearch "select:WebSearch,WebFetch"; arXiv PDFs via https://arxiv.org/pdf/<id>): Shkredov arXiv:2603.14116v2 (Zaremba for larâ¦",
      "promptFramed": true,
      "lastProgressAt": 1790397276958,
      "tokens": 165756,
      "toolCalls": 48,
      "durationMs": 609832,
      "resultPreview": "{"task":"Zaremba campaign Phase 0, Agent B: exact constant ledger for Shkredov arXiv:2603.14116v2 (reproduce ~1680 and the 2^2000 round-up, sensitivity table, settle N2)","status":"done","key_findings":["With Shkredov's own formulas and inputs the chain gives log2 M = 1665.8 (eq. 157 read literally, with the correct kappa), 1673.0 (full visible chain: Cor 16 halving, Thm 38 factors 0.99*5 and M*=3â¦"
    },
    {
      "type": "workflow_agent",
      "index": 3,
      "label": "N1_min_provenance",
      "phaseIndex": 1,
      "phaseTitle": "Warm-up",
      "agentId": "a456212c38de1cc69",
      "model": "claude-opus-5-5[1m]",
      "state": "done",
      "startedAt": 1790396666336,
      "queuedAt": 1790396666324,
      "attempt": 1,
      "lastToolName": "StructuredOutput",
      "lastToolSummary": "N1 â provenance of c â¥ min{1/3, 1/(8C2), tau/(4C2), 0.5 c_Hâ¦",
      "promptPreview": "ZAREMBA CAMPAIGN, Phase 0 (automath, slot 1). Read first: /work/campaigns/zaremba-M/BRIEF.md and /work/campaigns/zaremba-M/DESIGN.md (the full design: routes R1âR5, negative-list tasks N1âN9, referee briefs). Primary sources to fetch yourself (load WebSearch/WebFetch via ToolSearch "select:WebSearch,WebFetch"; arXiv PDFs via https://arxiv.org/pdf/<id>): Shkredov arXiv:2603.14116v2 (Zaremba for larâ¦",
      "promp