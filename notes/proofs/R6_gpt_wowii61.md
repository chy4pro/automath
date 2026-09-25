# WOWII-61 ChatGPT Session (Graph Theory Conjecture)

**URL:** [chat link removed]

**Status:** Reasoning interrupted by user directive; incomplete proof

**Date:** 2026-08-17

## Problem Statement

Graph theory research problem (Graffiti.pc Conjecture 61).

**Definitions:**
- For a connected graph G: diam(G) = diameter
- f(G) = maximum number of vertices inducing a forest (max induced forest size)
- residue res(G) = number of zeros remaining when Havel-Hakimi process terminates

**Classical theorem** (Favaron-Maheo-Sacle 1991): res(G) ≤ α(G) (independence number)

**CONJECTURE:** f(G) ≥ res(G) + ⌈diam(G)/3⌉

## Known Partial Results

1. f ≥ α+1 for every connected G (settles diam ≤ 3)
2. Star-forest lemma: greedy along diametral path gives f ≥ α + ⌊(d-1)/4⌋ + 1 (settles d ∈ {5,6,9})
3. Conjecture equivalent to s(G) ≥ (n - f(G)) + ⌈d/3⌉ where s(G) = Havel-Hakimi steps
4. All trees/forests settled via matching bound α + μ ≤ n
5. Exhaustive verification: all connected graphs n ≤ 8 plus 150,000+ candidates, zero counterexamples; every tight case has d ≤ 4

## Main Gap

Graphs with diameter exactly 4 and induction d → d+3.

**Key obstacles:**
- (O2) 2-packing argument yields only d/4; bottleneck is controlling C₄ through packing vertex pairs
- (O1) Slacks α-res and f-α can degenerate independently

## Verified Subconjectures

- **(SC1)** f ≥ α + max(1, ⌈(d-1)/3⌉)
- **(SC2)** If d ≡ 1 (mod 3), d ≥ 4 and f = α + ⌈(d-1)/3⌉, then res ≤ α - 1

## Session Activity Summary

The model pursued three parallel routes:
1. Diameter-4 structure analysis
2. d ↦ d+3 Havel–Hakimi recursion
3. Verification/refinement of residue machinery

**Key finding:** SC1 is false (counterexample: diameter-8 chained-C₄ with α=7, f=9)

**Alternative target:** f ≥ res + ν_ind, or equivalently s ≥ τ_FVS + ν_ind

**Proposed sharper approach:** Use Jelen's 2-residue: verify R₂(G) - R₁(G) ≥ ⌈diam(G)/3⌉

The session shows extensive computational testing across multiple graph families and refinements but was interrupted by user request to provide complete proof/counterexample rather than partial results.

---

**Conclusion:** Diameter-4 case progress via maximum-independent-set core lemma; bridge inequalities f ≥ res + γ under testing. Proof incomplete as of session end.
