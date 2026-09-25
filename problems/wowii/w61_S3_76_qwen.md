# Q23 — w61 §7.6 CHAIN S3, first-ever adversarial round (Qwen3.8-Max)

- Target: Theorem LOW -> Theorem SL -> Theorem MB -> Corollary L1-short ->
  Corollary MB1 -> Proposition L2 -> Corollary SL-HC (Corollary FAN-HC's own
  proof is already certified; FAN-HC's promotion is blocked only on this chain).
- Dispatched: 08-18 18:2x CDT, owner-intel round 14 (brief `prompts/w61_S3_76_qwen.md`, 80 KB)
- Harvested: 08-18 19:0x CDT, owner-intel round 15 (evening harvest)
- Conversation: https://chat.qwen.ai/c/4a2594fc-2a60-421b-ad9a-f2a1a6f10565
- Model confirmed: Qwen3.8-Max
- Completion confirmed via true-bottom scroll to the static action-icon row
  (copy/thumbs-up/thumbs-down/share/regenerate/more), held static across a
  follow-up poll.

## VERDICT (model's own line)

> VERDICT: PARTIAL — I found no load-bearing MATHEMATICS defect in the
> conclusions of the chain (all named statements survive after small
> repairs), but there are real bookkeeping/proof-presentation defects, most
> notably in Proposition L2(c) and in one over-broad quantifier in Theorem MB.

**This is §7.6's first-ever adversarial round (0 -> 1 clean-of-mathematics
round). The two-family bar for promoting Corollary FAN-HC still needs a
second family/judge on this chain** (per the row's own gate note).

## Joint table (all CLEAN except two BOOKKEEPING/PARTIAL)

| joint | verdict | note |
|---|---|---|
| J-LOW | CLEAN | position-sum collapse + LOW2/LOW3 algebra verified at L=0,1,τ |
| J-SL (Steps 1-6) | CLEAN | all six steps individually verified, incl. tie-safety of prefix-domination |
| J-MB | CLEAN after wording repair | over-broad quantifier "every b in T1∪T2 lies in B_lo+" should read "every **low** b" |
| J-L1s | CLEAN | L=1 kill verified, chain not circular |
| J-MB1 | CLEAN | correct under hard-core hypotheses + universal B_lo |
| J-L2(a),(b),(d),(e) | CLEAN | |
| J-L2(c) | PARTIAL/BOOKKEEPING | tightness argument under-explained; repair supplied, conclusion survives |
| J-SLHC | CLEAN | both L=0 and L=1 eliminations valid, τ≥4 available |
| J-SCOPE | PARTIAL | LOW/SL correctly moved to reductio-only; but Lemma HI, Corollary MB1, Corollary L1' omitted from tier list; several statements over-hypothesised (filed under τ≥4 hard-core though proofs only need frame+reductio+τ≥2) |

## Defects (all BOOKKEEPING, all repairable, conclusion survives in every case)

1. **Proposition L2(c)** — tightness sentence doesn't spell out that BOTH the
   Theorem MB lower bound and the Theorem SL upper bound are being re-run
   simultaneously. Repair supplied (3-line derivation); conclusion unaffected.
2. **Theorem MB** — "every such b lies in B_lo+" is over-broad if b is high;
   true statement is "every **low** b in B_lo∩(T1∪T2) lies in B_lo+". Witness:
   the Prop L2 rigid config (B = K_τ minus edge uv) has u,v high and NOT in
   B_lo+. Degree count itself unaffected since it only uses c = |B_lo∩(T1∪T2)|.
3. **Section T scope list** — omits Lemma HI, Corollary MB1, Corollary L1';
   over-hypothesises Theorem MB / Corollary L1-short / Corollary MB1 /
   Proposition L1 / Corollary L1' under τ≥4 though their proofs need at most
   τ≥2 + frame; non-forest flagged as likely redundant given diam=4 + f=α+1.
4. **"Where this leaves the line" Fan(τ,L) slack rider** — correct
   (`slack = L-1`) but the one-line calculation was missing from the text;
   not load-bearing.

## Repair-species probes

- Probe 1 (statement riders): all 4 named candidates checked, all verified
  correct except the Fan-slack rider (bookkeeping only, see Defect 4).
- Probe 2 (scope-widening contagion): confirms Repair V2's LOW/SL
  reductio-only widening is mathematically sound, but the tier-list update
  was not fully propagated to dependent statements (residue of Defect 3).
- Probe 3 (box-vs-branch): no artifact found; [SLACK]/[HARDCORE] histograms
  and the MB degree-count histogram are correctly treated as illustrative,
  not as proof.

## T12 controls (counterfactual availability + witness validation)

- **Control R (C4)**: reductio holds, hard-core frame fails (diam=2).
  Theorem LOW/SL available and true; **Lemma SL1 is available but never
  executes** in the final dependency chain (the named non-executing lemma
  required by the T12 amendment); (F-b) correctly fails to apply so Theorem
  MB is correctly unavailable.
- **Control F (F7, 7-vertex hard-core frame w/o reductio)**: explicit graph
  A={u,v,w,e}, B={x,y,z}, edges ux,uy,uz,vx,vy,vz,wx,wy,ez. Validated against
  all defining constraints (connected, A maximum independent α=4, non-forest,
  diam=4, f=α+1, residue=3=α-1 so reductio fails) — hard-core frame present,
  hard core absent, matching the text's scoping. Hand Havel-Hakimi trace
  included, own-calibrated (K2, C3..C9 residues all match ⌈n/3⌉).

## What the model could NOT check

Did not execute the cited Python scripts or reproduce the large §7.6 C/H
corpus counts; did not exhaustively enumerate all connected graphs n≤8; did
not computationally randomize tie-breaks (proof-read + hand examples only);
could not directly falsify hard-core-with-reductio statements numerically
(conjecturally empty class, no explicit instance); did not referee Lemma 4,
Lemma 5, Theorem 6, Observation R1, Lemma Z+, Lemma DICH, Theorem K,
Corollary K1 (out of scope per the brief, only checked how §7.6 uses them);
could not verify the Lean formalisation's exact `residueAux` tie-order
against the informal HH tie-break model (assumed "arbitrary descending
tie-break").

## Out-of-scope observations (noticed anyway, non-load-bearing)

- Lemma 4 scope note (doesn't affect §7.6's use).
- Non-forest redundancy observation for connected diam=4 graphs.
- §7.4 D tight example notation gap (missing 4th head entry `1`).
- Fan-slack remark: correct but was only a comment, not a proved theorem in text.

## Caveats for owner-w61 / planner

- **UNVERIFIED by owner-w61** — re-verify line by line before any gate action.
- This round found **zero mathematics defects**, only bookkeeping. Per the
  row's own gate note: "Verdict gate: CLEAN with both mandatory sections =>
  §7.6 chain has 1 clean round => report to planner for the Corollary FAN-HC
  promotion decision (a second family is still required by the two-family
  bar)." The verdict tag returned is PARTIAL (not CLEAN) because of the
  bookkeeping defects, but **no MATHEMATICS defect was found** — flagging
  this distinction explicitly for planner/owner-w61 to decide whether a
  "PARTIAL, zero mathematics defects, all bookkeeping repairable" round
  counts toward the same threshold as a CLEAN round, or whether the 3
  bookkeeping repairs must land in the text first before this counts as
  round 1 of the two-family bar.
- Both T12 mandatory sections present and substantive (named a genuinely
  non-executing lemma on a real control, per the T12 counterfactual-
  availability amendment).
