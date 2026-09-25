# Qwen K≠B ATTACK — Tab C (general case), Problem C

- Conversation: https://chat.qwen.ai/c/095fe3a0-8591-4885-9af2-e15eae3b875d
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_KNEB_qwen.md` (S2 template set: T1 disguise, no-internet, T8
  persistence rider, T11 toolbox preface, T12 counterfactual-availability control cases,
  T13 conclusion-first tag). Statement fully disguised, no attribution/history/source.
- Dispatched: 08-18 11:4x-11:50 CDT (owner-intel qwen_queue driver round 4).
- Harvested: 08-18 12:3x CDT (owner-intel qwen_queue driver round 5). Chrome lease FREE at
  pickup (not held by owner-w61); conversation had already finished generating (composer
  idle, "Thinking completed", verdict line visible) — harvested per driver discipline.

## Overall verdict

**PARTIAL** — proved rigorous Havel-Hakimi obstruction lemmas that exclude the Fan(τ,2)
trajectory in the forced **high-before-low** ordering case, but the unconditional
elimination of all tie-breaks for L=2, and the general L≥3 case, both remain open. Weaker
result than tab B (which closed Fan(τ,L≥2) unconditionally); this tab's own approach was
superseded mid-brief by the escape-buffer technique but left a tie-break GAP tab B does not
have.

## Key results (summary; full derivations in transcript)

1. **Lemma 1 (largest-entry process cannot collapse to one positive entry ≥2)**: in a
   greedy largest-decrement process, if the final state has exactly one positive entry with
   value `c≥2`, the initial state already had exactly one positive entry. (Explicitly notes
   this is FALSE for `c=1`, e.g. `[2,1]→[1,1]→[0,1]` — a useful boundary distinction.)
2. **Lemma 2 (escape buffer lemma, Fan form)**: in the Fan(τ,2) situation with high-before-
   low ordering, if a low vertex `p` escapes exactly one high block at step `j`, then at
   least two entries of `C = A∖{a0}` are forced to value ≥2 by the end of the high phase.
3. Applying these: under the additional **ordering assumption** that the two low heads are
   the last two heads (high-before-low), BOTH possible terminal low-head pairs — `(2,2)` via
   Lemma 1, and `(3,1)` via Lemma 2 — are shown impossible. Conditional conclusion: no
   hard-core Fan(τ,2) exists under high-before-low ordering.

## GAP (self-flagged, explicitly named)

"I have not proved that in every admissible tie-break for a Fan(τ,2) hard-core graph the
two low heads are the last two heads." If ties let a low head interleave earlier, the
terminal-shape bookkeeping needs redoing with shifted positions; the escape-buffer
mechanism (Lemma 2) still applies but the full tie-independent position analysis was not
completed. **This gap is subsumed by tab B's Lemma 1 (no-escape)**, which proves
unconditionally (no ordering assumption, tie-break independent) that no C-vertex — and by
the same argument structure no low-phase escape either — can occur before all high heads
are removed. Cross-reference: `w61_KNEB_qwen_B.md`.

## Control cases (mandatory probes, all addressed)

- Control 1: correctly not used/implied; Lemmas 1/2 are about escape/collapse dynamics, not
  a universal `D_i` vs sorted-degree bound.
- Control 2: fresh counterexample `[5,5,4,4,4,4]` (τ=4, s=4, last low head D_4=2 > τ-4+1=1);
  correctly notes Lemma 1 explicitly allows a single positive entry of value 1, and Lemma 2
  only controls escapes forcing buffers ≥2, so neither implies the false statement.
- Controls 3/4: correctly not used.

## Three attack angles (per T8 persistence rider)

1. Direct construction of Fan(τ,2) via type multiplicities — obstruction named "the buffer
   pyramid": any escape-enabling buffer construction regresses to needing higher buffers,
   while the Fan degree cap `deg(c)≤|B_hi|` blocks it; no successful construction found.
2. Prove `slack ≥ L` directly (Problem A) — obstruction: the graphical sequence
   `[5,5,4,4,4,4]` (τ=4, L=2) achieves slack exactly `L-1=1`, so any proof of `slack≥L` must
   use Fan/diameter/type structure beyond the bare HH sequence; could not complete the
   generalization.
3. Pure counting via T10/T8/T9 — obstruction: counting inequalities alone are compatible
   with Fan-like structures for L≥3 (offsetting `deg_A` increases against `ν(B_lo)`
   increases), so they don't detect the HH escape-buffer mechanism; insufficient alone.

## Most promising continuation (model's own suggestion)

(1) Close the tie-break ordering GAP for Fan(τ,2) [now superseded by tab B]; (2) generalize
the escape-buffer lemma to L≥3 low-phase escapes; (3) deduce `slack≥L` and combine with
T10 to force an impossibility via the diameter-witness types. Materially the same direction
tab B's own continuation suggests.

## Cross-tab note (driver observation, not independently verified)

Tabs B and C attacked overlapping ground (both proved Fan(τ,2)-type impossibility results)
via different technique paths — B via a clean unconditional "no C-vertex escape" lemma
covering all of Fan(τ,L≥2), C via a two-lemma (collapse + escape-buffer) argument that only
closes Fan(τ,2) and only under an ordering assumption it could not remove. B's result
appears to strictly dominate C's on this reading, but this comparison is the driver's own
and needs owner-w61's independent check — the two proofs use different explicit
inequalities and it is not guaranteed they are interchangeable without re-verification.

## Extraction caveat

Same KaTeX get_page_text extraction-order caveat as tabs A/B — inline formula fragments may
read oddly in the raw transcript; prose and final results are unaffected. Re-open the
conversation URL for byte-exact formula verification.

## owner-w61 verification duties

UNVERIFIED as of harvest. Per dispatch note: everything returned is re-verified line by
line before adoption, adversarial review of anything adopted goes to a NON-Qwen judge.
Given tab B likely supersedes this tab's core result, prioritize verifying B first; this
tab's Lemma 1/Lemma 2 (collapse and escape-buffer mechanics) are still worth checking as
an independent cross-check on B's Lemma 1, since they were derived via a different route
and agree on the qualitative conclusion.
