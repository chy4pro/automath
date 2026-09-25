# Qwen TRIANGULAR-ENDPOINT attack — Entry B (high-degree sub-branch, F9 configuration)

- Conversation: https://chat.qwen.ai/c/901113ec-6cd0-4120-83b9-bc65335d82bd
- Model: Qwen3.8-Max (confirmed via find-tool ref-click after model-selector auto-close
  broke coordinate clicks — see `notes/web_model_ops.md`).
- Brief: `prompts/w133_r6_TRIEND_qwen.md` (same S2 template set as Entry A — see that file
  for details). Entry B = "some hub of degree ≥ 6 — the F9 configuration, `6 ≤ |H| ≤ 8`."
- Dispatched: 08-18 13:5x-14:0x CDT (owner-intel qwen_queue driver round 7).
- Harvested: 08-18 14:4x CDT (owner-intel qwen_queue driver round 8). Chrome lease held by
  owner-intel throughout; conversation had already finished generating (composer idle,
  page text length static across two checks ~3 min apart) — harvested per driver
  discipline.

## Overall verdict

**SOLVED-EMPTY** (`VERDICT: SOLVED-EMPTY`, self-reported). Companion to Entry A
(bounded-degree, also SOLVED-EMPTY) — see `w133_TRIEND_qwen_A.md`. If both hold up under
owner-w133 verification, the whole triangular-endpoint branch (both sub-branches) closes.

## Proof sketch (as given)

1. F8 applied at `u` forces `H ⊆ {p,q} ∪ B_p ∪ B_q` (using (C5) and `u ∉ H`).
2. F8 applied at `y` forces `H ⊆ N[h] ∪ N[y*]` (using (C5) and `y ∉ H`).
3. Intersecting these two constraints and applying F7(c) bounds `|H| ≤ 5` in **two of three**
   sub-cases for where `y*` sits, violating F2 (`|H| ≥ 6`).
4. The **borderline case** (`y* ∈ B_q`, `|H|=6`, `p,q ∈ H`) gives
   `|H'∩B_p|·|H'∩B_q| = 4`, contradicting F8(d) (`≥ 6`).
5. Petersen and friendship graphs are correctly excluded as controls because they fail
   `diam=3` and `l>3`; no step of the argument is claimed to apply to them.

## Self-audit and control validation (mandatory probes)

- **Explicit control-case check against Petersen**: `l=3` exactly (fails `l>3`), `diam=2`
  (fails `diam=3`, so no distance-3 pair `u,u'` exists at all, meaning branch (TRI)'s setup
  is inapplicable from Step 0) — correctly identifies the first failing step as "Step 2 (no
  D layer exists)," not a downstream step.
- **Explicit control-case check against friendship graph `F_k`**: `l<3/2`, `diam=2`,
  `rad=1≠2`, no induced `P5` at all — F1/F2 fail, `rad≠2` fails, F6 vacuously satisfied
  (consistent with the brief's own warning about this control).
- **Full hypothesis-usage log** (table format): every step tagged with which of
  F1/F2/(C5)/C4-freeness/F8(d)/F9/(C6)-via-F6/branch-setup it uses.
- **Self-flagged uncertainty**: names Case B's reliance on F8(d) as a "black box" as the
  weakest link, but explicitly re-derives the `|D2|≥6` claim from
  `Σ|N(h')∩D| > |D|+5` (checking each `v∈D2` contributes 2 to the sum, others ≤1) rather
  than trusting it blindly — reports this derivation as sound.
- **What was tried and failed**: an initial direct mass-bound attempt (`Σ(a-2)>n` carried by
  few hubs with near-disjoint neighbourhoods) stalled on messy F7(c) degree caps, pivoted to
  the cleaner intersection-counting argument above; an initial worry that Case B might admit
  a graph was resolved cleanly once F8(d)'s product bound was applied (only 2 hubs per side
  available).

## Owner-w133 verification duties on adoption

Line-by-line re-verification of the three-way case split on `y*`'s location and the
borderline-case F8(d) contradiction (step 4 above is the tightest step — worth extra
scrutiny); confirm the Petersen/friendship control exclusions are airtight; adversarial
review by a NON-Qwen judge before adoption. Full transcript stays live at the conversation
URL above.
