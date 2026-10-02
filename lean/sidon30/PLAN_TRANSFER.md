OPEN

# Rational-kernel transfer formalization

The exact targets are defined in `Sidon30/TransferStatement.lean`, importing
only `Sidon30.Basic` (and hence Mathlib). There are no theorem claims yet.
The existing Sidon theorem and its thirteen axiom guards remain unchanged.

## Work cards

1. **T1: g-thin.** Exact nonzero ordered integer-difference multiplicity.
   Reuse the finite ramp certificate with energy `g + a_T (k-g)`.
   The integer scale is rounded from `sqrt(2) (gN)^(3/4) / g`.
2. **T2: weak Sidon.** Strictly off-diagonal unordered sums. Prove the
   repeated-difference structure and an exact finite energy bound, then
   use scale `ceil(sqrt(6) N^(3/4))` and the original onset `90^4`.
3. **T3: triangle sonar.** `Fin m → Fin n`; ordered nondiagonal vector
   injectivity. State the original powers by `Real.rpow`, with onset `48^3`.
4. **T4 (optional):** difference triangle sets, only if cheap after T1.

The original finite signed certificate already has an explicit geometric
remainder. Reusing it avoids any need to formalize continuous integration.
Any new finite comparison must be proved at its stated onset; the paper's
continuous certificate estimates are not assumed as axioms.

## Validation and ownership

Only remote CI, via the prescribed scoped push and CI scripts. No local
Lean build or installation. Root owns integration, CI, and appended axiom
guards. Existing completed worker seats were inspected before reuse.
All new headline theorems must pass `#guard_msgs` axiom checks before a
PROVED milestone. Statement audit is requested first through the inbox.

2026-10-02: initial exact definitions prepared; proofs and CI pending.
