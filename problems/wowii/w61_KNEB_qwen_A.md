# Qwen K≠B ATTACK — Tab A (slack bound), Problem A

- Conversation: https://chat.qwen.ai/c/66f31ade-4caf-4eb2-86c6-4a40779ca325
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_KNEB_qwen.md` (S2 template set: T1 disguise, no-internet, T8
  persistence rider, T11 toolbox preface, T12 counterfactual-availability control cases,
  T13 conclusion-first tag). Statement fully disguised, no attribution/history/source.
- Dispatched: 08-18 11:4x-11:50 CDT (owner-intel qwen_queue driver round 4).
- Harvested: 08-18 12:3x CDT (owner-intel qwen_queue driver round 5). Chrome lease FREE at
  pickup (not held by owner-w61); conversation had already finished generating (composer
  idle, "Thinking completed", verdict line visible) — harvested per driver discipline.

## Overall verdict

**PARTIAL** — proves a genuine, non-trivial obstruction result (Theorem 4.1: the
"escape-free Fan" configuration cannot be hard-core, via a suffix-multiset Havel-Hakimi
lemma) and derives the minimal Fan(τ,2) as a corollary (Corollary 5.1: cannot be
hard-core). Does NOT close Problem A itself (the general `slack ≥ L` strengthening) — the
model explicitly names the precise remaining obstruction (see GAP below) rather than
papering over it.

## Key results (summary; full derivations in transcript)

1. **Lemma 2.1 (bad suffix)**: a Havel-Hakimi process started from the multiset
   `{L,...,L (L+1 times), 1, 1}` cannot terminate in exactly `L` steps (at least three 1's
   remain), for every admissible tie-break.
2. **Lemma 3.1 (greedy leaves two ones)**: a multiset with at least two 1's, reduced by
   repeatedly subtracting 1 from a largest element until the sum is 2, must end at `{1,1}`
   (not `{2}`), independent of tie-breaking.
3. **Theorem 4.1 (escape-free Fan obstruction)**: under an explicit "escape-free" condition
   (the `L` low vertices plus the universal `A`-neighbour `a0` are all decremented in every
   one of the `h=τ-L` high-head blocks), the HH process cannot terminate at step `τ` — no
   such hard-core graph exists. Full algebraic derivation of the residual value `d'-2` left
   on `A'` after the high phase, combined with Lemmas 2.1/3.1.
4. **Corollary 5.1**: the *minimal* Fan(τ,L) configuration (exactly 3 extra `A`-vertices:
   one of type `{u}`, one of type `{v}`, one universal to `B_hi`) is forced to be
   escape-free, hence by Theorem 4.1 cannot be hard-core. This is a rigorous disproof of
   the most natural candidate counterexample for Problem B.

## GAP (self-flagged, not closed)

Theorem 4.1 assumes the escape-free condition; it does not prove every Fan(τ,L)
configuration is escape-free. Concrete counterexample to the naive extension: for `L=2`,
the residual multiset `{3,2,1,1,1}` (which CAN arise if a low vertex escapes a high block)
terminates in two further steps (`{3,2,1,1,1}→{1,1}→{0}`) — i.e. escape is not
automatically fatal, and the model could not rule this out under the full Fan hypotheses.
Explicitly named as "the precise obstruction to turning Theorem 4.1 into a full resolution
of Problem B or Problem A."

## Control cases (mandatory probes, all addressed)

- Control 1 (`D_i ≤ d_i-(i-1)` false bound): correctly notes the proof does not use or
  imply it; the standard control sequence `[3,3,3,3,3,2,1]` is flagged as irrelevant to
  the Fan-specific argument (does not satisfy Fan structure).
- Control 2 (naive "last low head is strict" claim): supplies an explicit fresh
  counterexample `[3,3,3,3,2]` (τ=s=3, heads `(3,2,2)`), showing `D_3=2 > τ-i0+1=1`.
- Controls 3/4: correctly notes non-use.

## Three attack angles (per T8 persistence rider)

1. Direct iterative slack-chain argument — proved only the first slack unit; named
   obstruction "critical escaper clustering" (tie-breaking allows multiple low heads at
   threshold value without forcing per-head slack).
2. Type/residual compression + Fan analysis — produced Theorem 4.1; named obstruction is
   the GAP above (high-block escape by a low vertex).
3. Algebraic/type-multiplicity formulation — recovers T10/T11 but doesn't control
   trajectory order/tie-breaking; no extra slack extracted.

## Most promising continuation (model's own suggestion)

Classify all possible residual multisets after the high-head phase for `L=2` under Fan
constraints + T4 survivor decay; show every escaping residual shape either violates T4,
forces too many `A'`-vertices to the survivor threshold, or contradicts the T8/T9 type
constraints. If completed for `L=2`, Problem B is fully resolved; iterating over the
number of escapes is suggested as the route to Problem A.

## Extraction caveat

`get_page_text` on this KaTeX-heavy response interleaves LaTeX source fragments with
rendered-text duplicates in places (known extraction-order issue, `notes/web_model_ops.md`)
— inline formula fragments in the raw transcript may read oddly (e.g. variable names
appearing both as rendered subscript and adjacent LaTeX token). The mathematical content
above was cross-checked against the surrounding prose, which is unaffected. For byte-exact
formula verification, re-open the conversation URL and screenshot the relevant section
rather than trusting the raw text extraction line-for-line.

## owner-w61 verification duties

UNVERIFIED as of harvest. Per the K≠B ATTACK dispatch note: everything returned is to be
re-verified line by line by owner-w61 before adoption, and adversarial review of anything
adopted goes to a NON-Qwen judge. Priority: verify Theorem 4.1's algebraic derivation
(the `E = d'-2` computation) and Corollary 5.1 (the minimal-Fan disproof), since these are
the load-bearing new results — Lemmas 2.1/3.1 are short and easy to independently check.
