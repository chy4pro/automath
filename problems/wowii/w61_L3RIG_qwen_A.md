# Qwen L≥3 RIGIDITY pre-chew — Tab A (Problem R, full classification at L=3)

- Conversation: https://chat.qwen.ai/c/3141ab7d-b0a2-4526-a994-86c898c11b41
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_L3RIG_qwen.md` (S2 template set: T1 disguise, no-internet, T8
  persistence rider, T11 toolbox preface with the proved L=2 classification as a worked
  precedent, T12 counterfactual-availability control section, T13 conclusion-first tag).
- Dispatched: 08-18 13:4x CDT (owner-intel qwen_queue driver round 6).
- Harvested: 08-18 14:4x CDT (owner-intel qwen_queue driver round 8). Chrome lease was held
  by owner-intel the whole time; conversation had already finished generating (composer
  idle, action-icon row visible under the final paragraph, verdict line present, page text
  length static across two checks ~3 min apart) — harvested per driver discipline.

## Overall verdict

**PARTIAL** (`VERDICT: PARTIAL`, self-reported). Role split per planner TIGHT ruling: this
tab was asked to pre-chew Problem R (full L=3 classification); owner-w61 holds the
decisive-step role and must re-verify everything below line by line before adoption.

## What it proves

1. **Exhaustive candidate table for L=3** (§1, "Exhaustive local skeleton table"): every
   admissible graph with `L=3` must have its local data `(n=ν(B_lo), p=|B_lo⁺|, c, m̄)`
   land in one of a finite list of rows, derived purely from (R1)/(L4)/(Fb)/(C*)/(MB)/(SL).
   Several rows are proved **impossible** outright (contradicting (R1) or (Fb)); a few are
   **realized** by explicit graphs `G1` (the requested `L=3` witness, tuple
   `(1,2,1,0,2,{3,2,1})`), `G2`, `G3`; the remaining rows are left **"undecided."**
2. **Two new general lemmas** (Lemma 2.1 "pair condition inside B", Lemma 2.2), proved from
   the stated facts, used to derive the skeleton inequalities.
3. **Problem T (explicit L=3 admissible graph)**: fully constructed and verified against all
   four admissibility conditions (connected+not-forest, diam=4, independent-set maximality
   `α(G)=4`, `f(G)=α(G)+1=5` via an explicit 6-vertex-deletion forest-freeness case check).
   This is the highest-value literal ask in the brief and Qwen delivers it in full.
4. Self-reports which given facts were load-bearing vs. redundant, e.g. notes (R1) is
   available but never actually needed once (Fb) is invoked directly.

## Self-flagged obstruction list (verbatim substance, not closed)

- **The candidate table is necessary, not known sufficient**: most "undecided" rows have
  neither a construction nor a contradiction.
- **Main obstruction = global control of `f(G)=α+1`**: the local inequalities (MB)/(SL) do
  not by themselves rule out large induced forests using fewer `A`-vertices / more
  `B`-vertices; a near-miss control graph (built to test exactly this) is exhibited showing
  the failure mode concretely.
- **`ν` is not pinned down in most rows**: (MB) controls `ν(B_lo)` and `m̄` but not the
  cross-nonedge count `x` between `B_lo` and `B_hi`.
- **General `L≥4` is explicitly left open**, though a first-layer dichotomy is proved for
  all `L≥3` (universal low vertex + universal `A`-neighbour `a0`, or else
  `c+m̄ ≤ ν(B_lo)-1`).
- **A plausible but unproved structural conjecture** is flagged, not assumed: that in many
  admissible graphs `T1 = N_B(a)`, `T2 = N_B(a')` for a diametral pair `a,a' ∈ A` — Qwen
  notes this is not among the supplied facts and did not use it.

## Owner-w61 verification duties on adoption

Line-by-line re-verification of the skeleton table (especially the "undecided" rows and the
impossibility claims), independent check of the explicit `G1`/`G2`/`G3` witnesses and the
Problem-T graph's four admissibility conditions, and adversarial review by a NON-Qwen judge
before anything here is adopted into the draft. Full transcript stays live at the
conversation URL above for byte-exact re-derivation.
