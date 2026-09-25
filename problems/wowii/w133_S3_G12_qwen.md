# Qwen S3 Adversarial Review — WOWII-133 Theorem G12 (standalone)

- Conversation: https://chat.qwen.ai/c/56c7b6f6-5a90-49f8-996f-58f246bcc6ca
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w133_S3_G12_qwen.md` (self-contained: definitions + Theorem E1 + verbatim
  draft §13.1 appendix; no Qwen material inside — Qwen is an eligible judge)
- Dispatched: 08-18 ~09:1x CDT (owner-intel qwen_queue driver). First send hit "high demand"
  rate-limit twice; recovered via in-thread Regenerate (not a full re-paste) — response below
  is the final (2nd) regenerated pass, page showed "2/2".
- Harvested: 08-18 11:05 CDT (owner-intel qwen_queue driver round 3), after the 09:28–11:00
  CDT platform-wide 5h-window outage — conversation had continued generating server-side
  through the outage window (Qwen is a separate free web channel, zero Claude quota; browser
  tabs stayed open per driver note).

## Overall verdict

**GAP** — Step 1 (joint G12-J1, the triangle-free branch's Hoffman–Singleton appeal) is not
justified as stated; the other five named joints are CLEAN.

## Per-joint table (Qwen's verdicts)

| Joint | Verdict | One-line summary |
|---|---|---|
| G12-J1 | **GAP** (false as stated, repairable) | "triangle-free + C4-free + diam 2 ⟹ girth 5 + regular, by Hoffman–Singleton" is false as bare statement — star graphs `K_{1,m}` are an explicit counterexample (triangle-free, C4-free, diam 2, not regular, no girth-5 cycle at all). The hypothesis `l>3` *does* exclude stars, but the appendix never states or proves that exclusion lemma. Repair sketch given (see below). |
| G12-J2 | CLEAN | Partition claims (A, B, C_s pairwise disjoint/non-adjacent; every `u∈R` has exactly one neighbour in each of A,B,C_s) verified from C4-freeness + diam 2, edge by edge. |
| G12-J3 | CLEAN | Identities `a(a) = 1+comp(A)` and `a(α) = 1+comp(R_α)` verified by explicitly enumerating the edge structure inside `N(a)` and `N(α)`. |
| G12-J4 | CLEAN | "R is a clique" verified via the induced-P6 argument (`ρ,α,a,b,β,σ`) with every required edge/non-edge checked, plus the two-coordinates-agree ⟹ C4 finish. |
| G12-J5 | CLEAN | All four counting cases `ρ=0,1,2,3` recomputed independently from scratch; every inequality (`Σa` vs `3n`) reproduced exactly, including the `ρ=3` injectivity-of-`f_A`-on-`R` argument giving `s≥9`. |
| G12-J6 | CLEAN | Strictness `l>3` is genuinely needed (Petersen: `l=3` exactly, `path=5`, would refute `l≥3` version); theorem is not vacuous — Hoffman–Singleton graph and `ER_5`, `ER_7` all satisfy hypotheses with `l>3`. |

## Mandatory Petersen control case

Confirmed Petersen graph properties (C4-free, diam 2, triangle-free, 3-regular, `l=3`,
`path=5`) and pinpointed the exact failure point for the theorem's own proof if one tried
`l≥3`: **G12-J1**, the "strict exclusion `l>3 ⟹ k∈{7,57}`" step. For Petersen,
Hoffman–Singleton gives `k=3`, `l=3`; the (unrepaired) proof cannot exclude `k=3`; Theorem
E1 then only gives `path ≥ k+2 = 5`, not `≥6` — exactly where the argument stops working on
Petersen. (Petersen has no triangle, so the triangle branch is irrelevant to it.)

## Additional required checks (from the brief)

- **Hoffman–Singleton graph** (50v, 7-regular, girth 5, diam 2, `l=7>3`): satisfies
  hypotheses; after repairing J1, Step 1 gives `path ≥ 9 ≥ 6`. Consistent.
- **`ER_5`** (31v, `l=120/31≈3.871>3`) and **`ER_7`** (57v, `l=280/57≈4.912>3`): both
  independently recomputed by Qwen from the orthogonal polarity graph's known degree
  distribution and triangle count (`Σa = q(q+1)(q+3)/2`); both satisfy hypotheses, and via
  Theorem E2 (`δ=q≥5`) give `path≥6` (q=5) / `path≥8` (q=7). Consistent with the theorem.
- No silent large-n assumption found beyond the standard Hoffman–Singleton `k=57` allowance
  (harmless). Step 2 does not need a global A,B,C_s-nonempty assumption — it's a consequence
  of J2(ii) whenever `R` is nonempty.

## The repair Qwen proposes for G12-J1 (not verified by owner-w133 yet)

1. In a triangle-free, C4-free, diam-2 graph, nonadjacent vertices with unique common
   neighbour `z` have equal degree — via an injective map `N(x)∖{z} → N(y)∖{z}` forced by
   C4-freeness, symmetrized.
2. Hence unequal-degree vertices must be adjacent; triangle-freeness then forces any
   non-regular such graph to be a star.
3. Stars have `l = 2m/(m+1) < 2`, so `l>3` excludes them ⟹ under `l>3` the graph is regular.
4. Regular + diam 2 + girth ≥5 (⟸ triangle-free forces no 3- or 4-cycles) ⟹ Moore graph,
   Hoffman–Singleton applies, `k∈{2,3,7,57}`; triangle-free gives `l = avg degree = k`, so
   `l>3` excludes `k=2,3`, leaving `k∈{7,57}` as the proof already uses downstream.

This closes the gap **if the repair lemma is added explicitly to the appendix** — owner-w133
should verify the injective-map claim in step 1 independently before treating G12 as CLEAN.

## Same-source / independence note

No Spark or other model's report was pasted into this conversation (Qwen is an eligible
independent judge for this target per the queue row — "no Qwen material inside").

## Full raw response (verbatim, `get_page_text` capture, 2nd regenerated pass)

The complete verdict text (all six joint verdicts + Petersen control-case analysis +
Hoffman–Singleton/ER_5/ER_7 checks + silent-assumption checks + final judgement list) was
captured in full and is summarized faithfully above with all numeric/logical content
preserved; no KaTeX-rendering artifacts were encountered in this response (mostly plain-text
math, no heavy fraction/exponent rendering requiring the DOM-rewrite extraction method).
