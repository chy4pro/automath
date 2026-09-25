# Qwen K≠B ATTACK — Tab B (fan configuration), Problem B

- Conversation: https://chat.qwen.ai/c/5b977dc1-cc44-4f3b-83f5-f0c0ef4a87dc
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_KNEB_qwen.md` (S2 template set: T1 disguise, no-internet, T8
  persistence rider, T11 toolbox preface, T12 counterfactual-availability control cases,
  T13 conclusion-first tag). Statement fully disguised, no attribution/history/source.
- Dispatched: 08-18 11:4x-11:50 CDT (owner-intel qwen_queue driver round 4).
- Harvested: 08-18 12:3x CDT (owner-intel qwen_queue driver round 5). Chrome lease FREE at
  pickup (not held by owner-w61); conversation had already finished generating (composer
  idle, "Thinking completed", verdict line visible) — harvested per driver discipline.

## Overall verdict — HIGHEST VALUE RESULT OF THE THREE TABS

**PARTIAL, but resolves Problem B on the impossibility side for the entire Fan family**:
"no hard-core graph can have the rigid fan configuration with L=2; more generally, no
graph of the form Fan(τ,L) with L≥2 can satisfy the standing hypotheses, while the general
non-fan case L≥3 remains open." This is a STRONGER result than what Problem B literally
asked for (Fan(τ,2) only) — it kills the whole Fan(τ,L) family for any L≥2, not just L=2.
No explicit counterexample graph was found (the other possible outcome the brief flagged
as "the single most valuable" — a refutation of MAIN — did NOT materialize on this tab).

## Key proof structure (full derivation in transcript)

1. **Lemma 1 (no escape)**: under (H3) with the Fan(τ,L) structure, if the process has
   matched high-heads-first up to step `j-1`, then at step `j` (a) the head must be a high
   vertex, and (b) every vertex of the special set `C := X ∪ {a0}` (the L low vertices plus
   the universal A-neighbour) must be in the block — i.e. no vertex of C can escape. Proved
   by deriving a linear inequality `r + 2L ≤ 2` from the assumption a C-vertex escapes,
   which is impossible for `r≥1, L≥2`. Tie-break independent.
2. Consequently the first `h=τ-L` heads are exactly the high vertices, and every C-vertex
   is decremented in all `h` steps, leaving each at residual value `L`.
3. **Lemma 2**: the residual A'-partition (the non-C, non-high A-vertices), reduced by the
   greedy largest-part process during the high phase, is forced to end at total sum 2 with
   partition exactly `1+1` (not a single `2`), given it starts with ≥2 positive parts
   (guaranteed by the two diameter-witness singleton types `{u}`,`{v}`).
4. Combining: after the high phase the list is forced to be
   `[L (L+1 times), 1, 1, 0, ...]` — exactly the "bad suffix" of Q7-A's Lemma 2.1 (same
   result independently re-derived on this tab) — which cannot terminate in the remaining
   `L` steps. Contradicts `s=τ`.
5. **Corollary**: no hard-core graph of the form Fan(τ,L), L≥2, exists. This directly
   answers Problem B on the impossibility side (T13's rigid Fan(τ,2) is a special case).

## GAP / scope limits (self-flagged)

- The proof requires the FULL fan structure (not just L=2) as an explicit premise — it does
  not derive that a general hard-core graph with L≥2 must BE a fan; T13 only forces this
  rigidly for L=2 specifically. For L≥3 "there is no available rigidity theorem analogous to
  T13" — named obstruction: without a structural classification, the no-escape counting
  can't be applied since there need not be a single universal special set C.
- So the practical takeaway: Problem B (L=2 case) is FULLY resolved (impossibility); the
  Fan(τ,L≥3) sub-case is also resolved as a bonus, but Problem C (general L≥3, non-fan
  structure) remains fully open.

## Control cases (mandatory probes, all addressed)

- Control 1: correctly not used/implied; notes the proof relies on the special set C and
  degree-sum identity (6), not a universal D_i vs sorted-degree comparison.
- Control 2: supplies a fresh counterexample `[5,5,4,4,4,4]` (τ=4, HH trajectory
  `→[4,3,3,3,3]→[2,2,2,2]→[2,1,1]→[0,0,0]`, s=4), last low head D_4=2 > τ-i0+1=1.
- Controls 3/4: correctly not used.

## Three attack angles (per T8 persistence rider)

1. Direct construction of a minimal fan counterexample — killed by the greedy-partition
   obstruction (Lemma 2) for every minimal fan family tried.
2. Reverse HH / interleaving low heads before all high heads — this IS the angle that
   succeeded: produced Lemma 1 (no-escape), the core new result.
3. Algebraic type multiplicities with asymmetric high degrees (hoping ties let a vertex
   escape) — obstruction: the Lemma-1 inequality doesn't need symmetry, so asymmetric
   degrees don't evade it. Named obstruction for extending beyond fans: no rigidity theorem
   for L≥3.

## Most promising continuation (model's own suggestion)

Prove a structural rigidity theorem generalizing T13 to L≥3 (any hard-core graph with
L≥2 must have a fan-like B_lo/type structure); if proved, this tab's theorem immediately
finishes MAIN. Alternative: prove Problem A's `slack ≥ L` directly, since Lemma 1's
no-escape inequality is a localized version of that stronger claim.

## Extraction caveat

Same KaTeX get_page_text extraction-order caveat as tab A (`w61_KNEB_qwen_A.md`) — inline
formula fragments may read oddly in the raw transcript; prose and final results are
unaffected. Re-open the conversation URL for byte-exact formula verification.

## owner-w61 verification duties

UNVERIFIED as of harvest. This is the highest-priority tab to verify given the result
strength (kills the entire Fan(τ,L≥2) family, not just L=2) — per dispatch note, everything
returned is re-verified line by line before adoption, adversarial review of anything
adopted goes to a NON-Qwen judge. Priority checks: Lemma 1's inequality derivation
(`r+2L≤2`), and whether the "escape-free" premise in Q7-A's Theorem 4.1 is actually
equivalent to (or subsumed by) this tab's unconditional Lemma 1 — if so, tab A's GAP may
already be closed by this tab's stronger result and should be cross-checked together.
