# Q25 — w61 GFAN FAMILY S3, §7.12 + §7.13, zero-rounds text (Qwen3.8-Max)

- Target: Lemma CAP / Theorem RIG / Corollaries RIG-1, RIG-2 / Lemmas
  FAN-4′, FAN-8′, FAN-6′ / Theorem GFAN2 / Theorem GFANν (`ν ≤ 6`) /
  Corollaries GFAN2-HC, GFAN2-L3, GFANν-HC. Three of these (Theorem RIG,
  Theorem GFAN2, Theorem GFANν) are the provisional theorems this round
  reviews.
- Dispatched: 08-18, third attempt (first two draws hit the slider CAPTCHA —
  see `notes/web_model_ops.md`), conversation
  `https://chat.qwen.ai/c/8009e918-dbf2-4804-823c-7164d307e70c`, resumed
  cleanly after a human cleared the slider ~21:1x CDT.
- Harvested: 08-18 23:0x CDT, owner-intel round-18 (short check/harvest round)
- Conversation: https://chat.qwen.ai/c/8009e918-dbf2-4804-823c-7164d307e70c
- Model confirmed: Qwen3.8-Max (header badge, per prior driver's ref-click
  confirmation before dispatch)
- Completion confirmed via the action-icon row appearing under the final
  message and staying static across two polls (scroll-to-bottom, 5s apart,
  page content unchanged).

## VERDICT (model's own line) — FLAG PROMINENTLY

> VERDICT: GAP — I found no mathematical counterexample to the hand-proved
> GFAN-family statements, but the computer-assisted enumeration supporting
> Theorem GFANν (ν = 3…6) is not reproducible from the text as written, so
> that theorem is not certified in this review.

**This is a GAP verdict, not CLEAN or PARTIAL-with-zero-mathematics-defects.**
The gap is scoped narrowly: it does **not** claim a mathematical falsity
anywhere. Lemma CAP, Theorem RIG (including the "Consequently exactly GFan"
clause), Corollaries RIG-1/RIG-2, Lemmas FAN-4′/FAN-8′/FAN-6′, and Theorem
GFAN2 (including its full L≥4 case + the eight-row L=3 table) are all
independently re-derived CLEAN by the judge's own calculation. The GAP is
specifically that **Theorem GFANν's computer-assisted ν=3…6 enumeration
cannot be reproduced from the text alone** — the judge reconstructed and
matched the *shape counts* (0/3/24/110/397/1211, independently re-derived
via its own partition-number formula) but could not rerun the decisive
"rows FAN-6′ misses = none" step-count table for ν=3…6, because the script
(`w61_r5_gfan2.py`) and its complete output are referenced but not included
in the reviewed text. The judge explicitly classifies this as "MATHEMATICS,
in the sense of an unverified proof obligation; no mathematical falsity was
found" (Defect D2).

## Joint table (11 named joints)

| joint | verdict | note |
|---|---|---|
| J-CAP | CLEAN | Lower bound needs only maximality (not maximum); upper bound arithmetic correct at all tested boundaries (n_b=0, n_b=τ−1); no hidden frame/reductio/diam hypothesis. |
| J-RIG | CLEAN | (a)–(e) verified clause by clause; Lemma 4 used in correct adjacent-pair form; diam=4 enters only in (d) via R1; "exactly GFan" clause-wise earned, though converse not spelled out (→ D4, bookkeeping). |
| J-RIG-NU | CLEAN | Import of Corollary MB1 correct: hypothesis matches, conclusion matches, scope demarcation correct; did not referee MB1's own proof (out of scope, per brief). |
| J-RIG12 | CLEAN | RIG-1 removes the tightness argument cleanly; RIG-2 chain (ν=1 killed by Fan, L=2 empty, L=3 → single config GFan(τ,3,2)) valid. |
| J-FAN4P | CLEAN | Independent re-derivation reproduces residue mass 2ν−E and C-entry L+e_c exactly; decrement split exhaustive/disjoint; escape definition consistent with FAN-8′. |
| J-FAN8P | CLEAN | Escape-step counting correct; two subtracted sets disjoint and in-block; prefix inequality tie-safe; lemma vacuous-but-not-false at E=0. |
| J-FAN6P | PARTIAL | Induction sound under the positive-part convention; one bookkeeping ambiguity — the bracketed claim "[w] killed for every w≥1" depends on undefined treatment of a singleton's second-largest entry (→ D1). Does not affect load-bearing residues [2ν], 2ν≥2. |
| J-GFAN2 | CLEAN | Step 1 escape budget, Step 2's three L≥4 trajectories, and all eight L=3 rows independently reproduced by the judge's own simulation; row list confirmed complete (E≥2 excluded by FAN-8′ arithmetic). |
| **J-GFANNU** | **GAP** | **The joint the round turns on.** Finiteness argument: hand-proved and exhaustive (E=0/L≥λ1 via TAIL, E=0/ν+1≤L<λ1 direct, E≥1 via FAN-8′ — case split verified disjoint+exhaustive, λ1≤2ν justified, MB1 import legitimate). Enumeration reproducibility: shape counts reconstructed independently and match (0/3/24/110/397/1211 via own partition-number formula, not reused); but the full step-count "misses" table for ν=3…6 is **not reproducible** — script/output absent from text. Only ν=1,2 independently certified end-to-end. |
| J-CORHC | CLEAN | GFAN2-HC, GFAN2-L3, GFANν-HC chains correct; GFANν-HC implies GFAN2-HC; arithmetic (ν≥3,L≥4 then ν≥7,L≥8) correct. |
| J-SCOPE | PARTIAL | New §7.12/§7.13 statements need weaker tiers than "hard core" in several cases; the existing T-tier excerpt does not explicitly assign them (→ D3, bookkeeping). |

## Defects (4 total: 1 MATHEMATICS-unverified, 3 BOOKKEEPING)

- **D1 (BOOKKEEPING)** — FAN-6′'s bracketed residue list "[w] for every w≥1"
  is ambiguous for [1]: depends on an unstated convention for a singleton's
  second-largest entry (0 vs −∞). Repairable by stating the convention or
  restricting to w≥2. Conclusion survives — load-bearing single-part
  residues in the GFAN argument are [2ν] with 2ν≥2.
- **D2 (MATHEMATICS, unverified-proof-obligation flavor — the load-bearing
  one)** — Theorem GFANν's enumeration (script `w61_r5_gfan2.py`,
  functions `tail_check`/`escape_check`/`complete_check`, output
  `w61_r5_gfan2_complete.out`) is referenced but not included in the
  reviewed text; several admissibility details (labelled vs unlabelled
  shapes, graphicality filtering, zero-entry treatment, p-feasibility) are
  underspecified. Not refuted — the theorem is "not certified in this
  review," distinct from "found false." Repairable by archiving/including
  the script, full output, and a precise shape-generation spec (the
  underlying script and .out files DO exist locally at
  `problems/wowii/w61_r5_gfan2.py` / `w61_r5_gfan2_complete.out` /
  `w61_r5_gfan2.out` / `w61_r5_gfan2_L3.out` — they were apparently just
  not pasted into the brief text the judge reviewed).
- **D3 (BOOKKEEPING)** — Appendix section T's tier list covers §7.6/§7.8
  but does not explicitly assign tiers to the new §7.12/§7.13 statements
  (Lemma CAP/CAP1, Theorem RIG, primed FAN lemmas, GFAN2, GFANν, GFAN
  corollaries). Conclusion survives.
- **D4 (BOOKKEEPING)** — Theorem RIG's "Consequently G carries exactly the
  configuration GFan(τ,L,ν)" proves the forward direction clause-by-clause
  but never states the converse sentence explicitly (it is definitional).
  One-sentence fix supplied by the judge. Conclusion survives.

## Refutation log / own implementation (highlights)

- Independent Havel–Hakimi `residueAux` implementation from the spec,
  calibrated against K2 (residue 1) and C3..C9 (all match ⌈n/3⌉) before use.
- Re-derived FAN-4′'s residue-mass identity `2ν−E` from scratch via the
  degree-sum bookkeeping (own algebra shown in full, p-terms cancel via
  τ=p+L).
- Re-derived FAN-8′'s escape bound `L≤2ν−E` from scratch via the block/prefix
  inequality chain.
- Independently simulated all three GFAN2 L≥4 trajectories ([2,2]→3 further
  steps, [2,1,1]→3 further steps, [1,1,1,1]→4 further steps) and all eight
  L=3 rows (E=0 residue partitions of 4; E=1 residue partitions of 3),
  matching the author's printed step counts in every row.
- Independently re-derived the GFANν E≥1 shape-count formula
  `S(ν) = Σ_{E=1}^{ν−1} (ν−E)·p(E)·p(2ν−E)` and evaluated it via its own
  partition-number table, reproducing 0/3/24/110/397/1211 for ν=1..6
  **without reusing the brief's printed numbers**.
- T12 counterfactual-availability control: built a Fan/GFan-shaped degree
  sequence failing the reductio (τ=4, L=2, ν=1, degrees
  [5,5,4,4,4,2,1,1]) and confirmed its own HH run (residue=3=α−1) satisfies
  the numerical structure but is unavailable to FAN-4′/8′/6′ — confirming
  the reductio hypothesis is load-bearing, not decorative.
- Explicitly could NOT independently construct a small graph witness
  satisfying the full hard-core GFan frame (connected, diam=4, f=α+1, all
  GFan clauses) — logged as an unchecked item under "What I could NOT
  check," not as a refutation.

## What the judge explicitly could not check

- Full ν=3…6 step-count enumeration (the D2 gap).
- The exact admissibility specification (labelled/unlabelled, graphicality
  filter, zero-entry convention, p-feasibility) — inferred from printed
  counts only.
- Independent construction of the (L,ν)=(1,3) frame witness for the
  ν≤L−1 failure, or the 31 GFan-frame instances mentioned in §7.12 E.
- A full graph-level non-vacuity witness for the hard-core GFan frame.
- MB1 and TAIL proofs themselves (explicitly out of scope per the brief;
  only their imports were checked, and both imports were found legitimate).

## Consequence for the pipeline

Per the row's own gate note: this GAP means **Theorem GFANν (ν≤6) is not
cleared by this round** — the enumeration needs to be made reproducible
(archive the script + complete output + shape-generation spec) before a
future round can certify it, or a future judge needs to be handed the
script directly and asked to re-run/audit it rather than reconstruct it
from prose. Theorem RIG, Theorem GFAN2, and the CAP/FAN-4′/FAN-8′/FAN-6′
lemma chain are all independently CLEAN from this first adversarial round —
only the GFANν ν=3…6 computer-assisted claim remains uncertified.
UNVERIFIED by owner-w61 — this harvest is a verbatim capture of the model's
own report, not an owner adjudication.
