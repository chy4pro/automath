PROVED — the exact theorem is kernel-checked. [CI run37060176909](https://github.com/chy4pro/automath/actions/runs/37060176909), commit `f8e97665f26ea40ec867d8d054d352b5fc5ec56c`, passed the complete build (8737 jobs) and all thirteen exact axiom guards on 2026-10-02. See [CI_LOG.md](CI_LOG.md) and [PLAN.md](PLAN.md) for the verification record.

# Sidon30 — Lean formalisation of the Sidon second-order bound

The exact target is

\[
|A|\le\sqrt N+\frac{2\sqrt2}{3}\sqrt{\sqrt N}+1
\]

for every natural number `N ≥ 120^4 = 207360000` and every strong Sidon set
`A ⊆ {1,…,N}`. Equality of pair sums must identify the sorted pairs, including
diagonal pairs. There is no restriction to fourth-power values of `N`.

- [Statement.lean](Sidon30/Statement.lean) defines the exact proposition using the single Sidon definition in [Basic.lean](Sidon30/Basic.lean).
- [Main.lean](Sidon30/Main.lean) proves the finite certificate and supplies it to the final reduction, yielding the global theorem `sidon_second_order`.
- [FinalCheck.lean](Sidon30/FinalCheck.lean) guards the axiom dependencies of the actual theorem and twelve intermediate milestones. Its required output is exactly `[propext, Classical.choice, Quot.sound]` for each theorem.

The proof uses finite ramp weights, a renewal recurrence with an explicit
geometric error bound, a signed finite boundary certificate, finite
Cauchy–Schwarz and exact real algebra. All hypotheses of the intermediate
conditional reductions are discharged in Main. The first-block scalar estimate
uses exact Mathlib exponential inequalities; no numerical approximation is a
proof step.

Pinned environment: Lean `v4.34.0-rc1`, Mathlib
`de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11`. GitHub Actions runs `lake build`
followed by `lake env lean Sidon30/FinalCheck.lean`; the build shell propagates
pipeline failures. The working session performs compilation only through that
CI workflow.

This formalisation concerns the explicit bound above. It does not formalise
the paper's kernel-optimality result or solve the full Erdős #30 conjecture.
The associated paper record is [Zenodo](https://doi.org/10.5281/zenodo.23103979).
