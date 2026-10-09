PROVED — the lower-onset theorem is kernel-checked. [CI run 37978411704](https://github.com/chy4pro/automath/actions/runs/37978411704), commit `fd880addd5f55d45ad528c224c4aa3fbb2471864`, passed the complete build (8759 jobs) and all 39 exact axiom guards on 2026-10-09. See [CI_LOG.md](CI_LOG.md) and [PLAN.md](PLAN.md) for the verification record.

# Sidon30 — Lean formalisation of the Sidon second-order bound

The exact target is

\[
|A|\le\sqrt N+\frac{2\sqrt2}{3}\sqrt{\sqrt N}+1
\]

for every natural number `N ≥ 4600000` and every strong Sidon set
`A ⊆ {1,…,N}`. Equality of pair sums must identify the sorted pairs, including
diagonal pairs. There is no restriction to fourth-power values of `N`.

- [Statement.lean](Sidon30/Statement.lean) defines the exact proposition using the single Sidon definition in [Basic.lean](Sidon30/Basic.lean).
- [Main.lean](Sidon30/Main.lean) proves the finite certificate and supplies it to the final reduction, yielding `sidon_second_order' : SidonSecondOrderBound'`. The original `sidon_second_order` is a corollary at `120^4`; its specification remains unchanged for transfer compatibility.
- [FinalCheck.lean](Sidon30/FinalCheck.lean) retains all 26 prior guards and adds 13 for the lower-onset proof and scalar wrapper. All 39 required diagnostics are exactly `[propext, Classical.choice, Quot.sound]`.

The proof uses finite ramp weights, a renewal recurrence with an explicit
geometric error bound, a signed finite boundary certificate, finite
Cauchy–Schwarz and exact real algebra. All hypotheses of the intermediate
conditional reductions are discharged in Main. The first-block scalar estimate
uses exact Mathlib exponential inequalities; no numerical approximation is a
proof step. The lower-onset Route B proof uses the exact block bound `r ≥ 32`,
the rational certificate `(3/4)^32 < 1/9900`, the tail bound
`η < (667/3300)x² < x²/2`, and a scalar comparison valid for every real `x ≥ 1`.

Pinned environment: Lean `v4.34.0-rc1`, Mathlib
`de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11`. GitHub Actions runs `lake build`
followed by `lake env lean Sidon30/FinalCheck.lean`; the build shell propagates
pipeline failures. The working session performs compilation only through that
CI workflow.

This formalisation concerns the explicit bound above. It does not formalise
the paper's kernel-optimality result or solve the full Erdős #30 conjecture.
The associated paper record is [Zenodo](https://doi.org/10.5281/zenodo.23103979).

## Rational-kernel transfers

[TransferStatement.lean](Sidon30/TransferStatement.lean) fixes the exact
definitions and targets using only Basic/Mathlib. The statement audit and
the full evidence ledger are in [PLAN_TRANSFER.md](PLAN_TRANSFER.md).

The following transfers passed
[CI run 37073917922](https://github.com/chy4pro/automath/actions/runs/37073917922)
at commit `3523813`, including the build and exact axiom guards:

- `g_thin_second_order`: every nonzero ordered integer difference has at
  most `g` representations; for `g,N >= 1` and `gN >= 120^4`,
  `card A <= sqrt(gN) + (2 sqrt(2)/3) sqrt(sqrt(gN)) + 1`.
- `Sidon30.weakSidon_second_order`: uniqueness of unordered sums of
  **distinct** elements; for `N >= 90^4`,
  `card A <= sqrt(N) + sqrt(8/3) sqrt(sqrt(N)) + 2`.

Both statements require `A ⊆ {1,...,N}`. The `g=1` recovery of the
ordinary Sidon specification is also checked. Its statement and the original
thirteen guards remain unchanged; the original theorem now follows from the
lower-onset theorem. The transfer proofs use the
actual finite signed certificate, with its geometric remainder; they do
not assume the continuous capacity lemma. Every guarded theorem depends
only on `[propext, Classical.choice, Quot.sound]`.

The triangle-kernel sonar theorem `sonar_triangle_bound : SonarTriangleBound`
passed [CI run 37075227591](https://github.com/chy4pro/automath/actions/runs/37075227591)
at `ca96407`, with 8755 build jobs and all 22 axiom guards passing. It states
`m <= n + 2 n^(2/3) + 3 n^(1/3)` for `n >= 48^3`, for a map
`Fin m → Fin n` whose ordered nondiagonal displacement vectors are distinct.
The formal proof uses `Real.rpow`; row values may repeat. Sliding windows
give the exact column marginal, and the signed indexed certificate supplies
the finite triangle/ramp inequality.

The optional difference-triangle bounds also passed:
[CI run 37076247531](https://github.com/chy4pro/automath/actions/runs/37076247531),
commit `2f981a701c72096c1851b8e2e3da621a80353b5c`, checked 8759 build jobs and
all 26 exact axiom guards. For `n>=1`, `k>=20365`, every normalized collection
of `n` rows with `k+1` marks per row and globally distinct positive within-row
differences has scope `m` satisfying

\[
 m>n\left(\frac{\sqrt{4k+8/9}-2\sqrt2/3}{2}\right)^4,
 \qquad
 m\ge n\left(k^2-\frac{4\sqrt2}{3}k\sqrt{k}+\frac{16}{9}k-2\sqrt{k}\right).
\]

The exported theorems are `difference_triangle_scope_bound` and
`difference_triangle_expanded_bound`. Their exact definitions and statement
audit are recorded in the transfer plan. The scope parameter `m/n` remains
real, and the finite `m+1` window error is explicitly retained.

No claim about cosine kernels, Manhattan configurations, integer boxes,
or the kernel-optimization results follows from these transfer checks.
