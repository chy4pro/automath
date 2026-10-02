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

## Evidence ledger

- 2026-10-02: exact definitions passed CI `37072461005` / `f6bdf41`.
  The coordinator read the statement module and approved all three
  definitions and target propositions through the inbox. They are frozen.
- CI `37073205929` / `044351c` passed the arbitrary-set and indexed-row
  capacity certificates, g-thin difference counting and scale estimates,
  and the initial sliding-window identities. The indexed certificate
  explicitly allows repeated row values.
- The complete g-thin proof and weak-Sidon proof are assembled as
  candidates. Headline axiom gates are appended after the original thirteen
  guards; their passing run is still required before a theorem milestone.
- The sonar finite route sums the indexed capacity inequality over every
  horizontal window. Its exact squared column count is
  `m U^2 - (U^3-U)/3`; uniqueness of displacement vectors bounds the summed
  row energy by `m U a_V + U(U-1)`. This yields the discrete triangle/ramp
  sandwich without continuous integration. At `x=n^(1/3) >= 48`, use
  `U=ceil(2x^2)`, `V=ceil(x^2)` and the explicit geometric tail `< 1`.
  These final sonar cards are still candidates, not a kernel milestone.

Only actual CI outcomes are listed as checked. Mathematical review and
source inspection of a candidate are not substitutes for compilation and
the headline axiom guards. No local Lean build has been run.
