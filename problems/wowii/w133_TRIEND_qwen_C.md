# Qwen TRIANGULAR-ENDPOINT attack — Entry C (independent re-derivation of the sister branch)

- Conversation: https://chat.qwen.ai/c/84892e46-6b3d-4933-9b1b-2baa00943e6a
- Model: Qwen3.8-Max (confirmed via find-tool ref-click after model-selector auto-close
  broke coordinate clicks — see `notes/web_model_ops.md`).
- Brief: `prompts/w133_r6_TRIEND_qwen.md` (same S2 template set as Entries A/B). Entry C is
  an **independent re-derivation, NOT a review** of the `a(u)=a(z)=2` six-slot mass count
  that Q3 (owner-w133 round 5) claimed but did not deliver verifiably — same-source firewall
  honored, the Q3 tabs' text was NOT pasted into this conversation.
- Dispatched: 08-18 13:5x-14:0x CDT (owner-intel qwen_queue driver round 7).
- Harvested: 08-18 14:4x CDT (owner-intel qwen_queue driver round 8). Chrome lease held by
  owner-intel throughout; conversation had already finished generating (composer idle,
  page text length static across two checks ~3 min apart) — harvested per driver
  discipline.

## Overall verdict

**SOLVED-EMPTY** (`VERDICT: SOLVED-EMPTY`, self-reported) — independently reaches the same
conclusion as Q3's claimed (but unverifiable) six-slot classification, this time with a
transcript that shows the actual derivation.

## Proof sketch (as given)

- Establishes the branch implies an induced 6-cycle `Z` and restricts all hubs outside `Z`
  to 7 specific slots (4 bounded, 3 unbounded).
- Core accounting device: a score `S = Σ(a(v)-2)` over `Z` plus additions; in C4-free
  graphs, adding an edge increases `a(v)` by at most 1 per endpoint, and adding a non-hub
  vertex contributes at most `-1` to `S`.
- Direct slot-by-slot bound: only `(v3,v4)` can share an edge without forming a triangle or
  a C4 (adding it brings both to `a=3`, i.e. score 0 each); all vertices in `Z` are capped
  at `a(v)≤2` (worked explicitly for e.g. `u1`, forced into a triangle via `v3∼u2`).
- **Non-hub addition case analysis**: any new vertex `w` connecting to one slot vertex
  contributes `≤0` net to `S`; connecting to two slot vertices either recreates a forbidden
  C4 (explicit example: `w∼u1∼u∼x∼w`), reproduces the already-excluded `v5` slot, or (if the
  two neighbours share a common neighbour, forcing a triangle) contributes `-1` net.
- **Conclusion**: every valid addition to the base graph `Z` leaves `S` unchanged or
  strictly decreases it; the maximum achievable score is `S = -6` (at
  `Z ∪ {v3,v4}` with edge `(v3,v4)`), which is `≤ 0` and contradicts `l(G)>3`. Branch empty.

## Self-audit

- **Uncertainty flagged**: did not exhaustively check every combination of 3+ inter-slot
  edges for obscure C4s, but explicitly argues this doesn't matter — even the most
  permissive single edge `(v3,v4)` only reaches `S=-6`, so the exact edge count is
  irrelevant to the sign of the final contradiction.
- **Hypotheses used**: C4-freeness (heavily, for the `Δa≤1` bound and common-neighbour
  limits), (C6)/P6-freeness (used implicitly via F6 to initially motivate slot degree
  bounds, though the final `ΔS` structural accounting superseded the need for explicit
  degree caps — flags this rather than silently dropping the dependency), (C5)
  `ecc(h)≤2` (forces hubs into the slots), `l>3` (the target contradiction `S>0`).
- **What was tried and failed**: an initial attempt to bound `v5`/`v6` degrees via
  algebraic eigenvalue bounds and extremal counting stalled on overlapping-neighbourhood
  complexity; switching to the exact structural `ΔS` accounting was the route that closed.

## Cross-check note for owner-w133

This is an **independent** re-derivation (fresh conversation, no Q3 material pasted in) that
lands on the same conclusion (branch empty) as Q3's earlier unverifiable claim, using a
visibly different accounting device (`ΔS` score over the 6-cycle + slots) than what Q3
described. If the underlying mechanism genuinely matches, this converts Q3's registered
"Claim Q6.1 (unverified)" into a result with an actual checkable transcript — but convergence
between one Qwen tab and an earlier unverifiable Qwen claim is not independent confirmation
in the adjudication sense; owner-w133's own re-derivation is still required.

## Owner-w133 verification duties on adoption

Line-by-line re-verification of the slot-by-slot `Δa` bounds and the non-hub addition case
split (the C4-recreation and triangle-forcing sub-cases are the tightest steps); confirm the
(C6)-via-F6 dependency claim is accurate; adversarial review by a NON-Qwen judge before
adoption. Full transcript stays live at the conversation URL above.
