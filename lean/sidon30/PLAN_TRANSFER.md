PROVED — all four transfer targets, including strict D1 and expanded D2, passed CI and exact axiom guards.

# Rational-kernel transfer formalization

The exact targets are defined in `Sidon30/TransferStatement.lean`, importing
only `Sidon30.Basic` (and hence Mathlib). T4 has its own definitions-only
`DifferenceTriangleStatement.lean`. Both statement audits passed.
The existing Sidon theorem and its thirteen axiom guards remain unchanged.

## Work cards

1. **T1: g-thin — PROVED.** Exact nonzero ordered integer-difference multiplicity.
   Uses the finite ramp certificate with energy `g + a_T (k-g)`.
   The integer scale is rounded from `sqrt(2) (gN)^(3/4) / g`.
2. **T2: weak Sidon — PROVED.** Strictly off-diagonal unordered sums. Proved the
   repeated-difference structure and an exact finite energy bound, then
   used scale `ceil(sqrt(6) N^(3/4))` and the original onset `90^4`.
3. **T3: triangle sonar — PROVED.** `Fin m → Fin n`; ordered nondiagonal vector
   injectivity. Uses the original powers via `Real.rpow`, with onset `48^3`.
4. **T4 (optional) — PROVED:** difference triangle
   sets. The exact D1 and D2 targets are in the separate definitions-only
   `DifferenceTriangleStatement.lean`. A normalized configuration consists
   of `n` rows of `k+1` marks including zero, all at most `m`, with globally
   unique positive within-row differences. There is no cross-row constraint.
   The strict D1 and expanded D2 theorems keep `n>=1`, `k>=20365`.

With `gamma = 2 sqrt(2)/3`, the two T4 conclusions are exactly

\[
 n\left(\frac{\sqrt{4k+8/9}-\gamma}{2}\right)^4<m,
 \qquad
 n\left(k^2-2\gamma k\sqrt{k}+\frac{16}{9}k-2\sqrt{k}\right)\le m.
\]

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
- CI `37073917922` / `3523813` passed **8749 build jobs and the Axioms step**.
  The job-step conclusions were independently read from the Actions API.
  This checks `g_thin_second_order : GThinSecondOrderBound`, its `g=1`
  recovery `sidon_second_order_from_gThin`, and
  `Sidon30.weakSidon_second_order : WeakSidonSecondOrderBound`.
  Each headline guard allows exactly `[propext, Classical.choice, Quot.sound]`.
  Additional guards check the weak-Sidon multiplicity-two theorem and the
  repeated-difference count `<= k-2`. All original thirteen guards passed
  unchanged; the old Sidon main theorem and specification are unchanged.
- The sonar finite route sums the indexed capacity inequality over every
  horizontal window. Its exact squared column count is
  `m U^2 - (U^3-U)/3`; uniqueness of displacement vectors bounds the summed
  row energy by `m U a_V + U(U-1)`. This yields the discrete triangle/ramp
  sandwich without continuous integration. At `x=n^(1/3) >= 48`, use
  `U=ceil(2x^2)`, `V=ceil(x^2)` and the explicit geometric tail `< 1`.
  CI `37075227591` / `ca96407` passed **8755 build jobs and all 22 axiom
  guards**, including `sonar_triangle_bound : SonarTriangleBound` and the
  actual finite sandwich. Build and Axioms step outcomes were separately
  verified through the Actions API. The statement uses exact `Real.rpow`
  exponents and allows repeated rows, with no unstated restriction on `m`.
  A separate informed source review found no convention or algebra error.
  The review seat also reported exact finite checks (231 marginal identities,
  60270 pair counts, 21400 energy/window tests). These were not rerun by the
  integrating seat and are not the evidence for the kernel milestone.
- T4 reuses the real scope parameter `x^4=m/n` with the actual finite
  window `N=m+1`. The additional `1/n` belongs to the explicit error term;
  it is not discarded. A strict scalar comparison is retained so that D1
  has no extra `-1`. Counting, scale, strict inversion and expanded remainder
  are all proved. The coordinator read and approved
  the exact T4 configuration definition and both scope statements through
  the inbox. No further Lean targets are authorized for this package after T4.
- Final proof CI [37076247531](https://github.com/chy4pro/automath/actions/runs/37076247531),
  commit `2f981a701c72096c1851b8e2e3da621a80353b5c`, passed **8759 build jobs
  and all 26 exact axiom guards**. The Actions API independently confirmed
  Build and Axioms success. This additionally checks
  `difference_triangle_scope_bound : DifferenceTriangleScopeBound` and
  `difference_triangle_expanded_bound : DifferenceTriangleExpandedBound`,
  plus the shared difference count and the actual summed-row certificate.
- The integrating seat checked byte-for-byte preservation of the original
  theorem, original specification, frozen T1–T3 definitions, toolchain and
  dependency pins, and the complete original thirteen-guard prefix. A scan
  of every project Lean source found no `sorry`, `admit`, `native_decide`, or
  project axiom declaration.

## Recorded execution cost and limits

The proof/statement loop used ten remote workflow runs: five successful
snapshots and five snapshots requiring elaboration repairs. The Actions
API reported 2051 seconds (34 minutes 11 seconds) in summed workflow elapsed
time, measured from `run_started_at` to `updated_at` for those ten runs.
This is a workflow-duration record; no monetary billing figure is available.
The documentation follow-up run is separate from this proof-loop total.

The new theorem proofs are entirely finite. They do not formalize the
paper's continuous signed-measure construction, cosine or perturbed kernels,
Manhattan or box bounds, or kernel-optimization results. The original
Erdős #30 conjecture remains outside these proved explicit upper bounds.

Only actual CI outcomes are listed as checked. Mathematical review and
source inspection of a candidate are not substitutes for compilation and
the headline axiom guards. No local Lean build has been run.
