# TICKET K6-T3 — (T_3) by computer algebra: Gröbner/saturation certificates over ℚ and over 𝔽_p

Self-contained; no internet EXCEPT to fetch the msolve source (see §2); no essay. Output to
`engine/harvest/k1695_r6_T3/` (create): `REPORT.md` ending with the literal line `DONE-K6T3`, every
script, every log, every certificate file. Hard caps: every single computation ≤ 20 min wall and
≤ 8 GB (`ulimit -v 8000000`; use `/usr/bin/time -l`); print progress; a computation that hits a cap
is reported as UNRESOLVED with the cap named. Never run more than one heavy computation at a time.

## The statement and its two cases (proved facts; use)
(T_3): for every 3×4 matrix R of rank 3 over a field F there are a column j and an ordering τ of the
other three columns with `det[b, Mb, M²b] ≠ 0`, where b = R[:,j] and M = R[:,≠j]P_τ.
Kernel split: κ_j := (−1)^j det R[:,≠j] gives Rκ = 0, and κ_j ≠ 0 iff R[:,≠j] is invertible.
**Case B (all κ_j ≠ 0):** R = C·[e₁ e₂ e₃ β] with C ∈ GL₃, β ∈ (F^×)³, and the 24 Krylov determinants
are det(C)·det[v_j, B C v_j, B C B C v_j] with v_j ∈ {e₁,e₂,e₃,β} and B the 3×3 coefficient matrix
of the ordering (a permutation matrix when j = 4; explicit otherwise — see the identity (6) in
`engine/harvest/k1695_r6_T2/REPORT.md` §3, which you should read first; its checks.c is exact).
**Case A (some κ_j = 0):** at least one 3×3 minor vanishes; the singleton-column reduction to (T_2)
handles columns with one nonzero entry; the hard core has every column of weight ≥ 2 (example over
GF(2): R = [[1,1,1,1],[1,1,0,1],[0,0,1,1]]).
Known: (T_3) has no counterexample over GF(2), GF(3), GF(4), GF(5), GF(7), GF(8) (exhaustive).

## 1. Formulate the certificate problem
Case B: variables = the 9 entries of C and β₂, β₃ (normalise β₁ = 1: scaling b does not change
controllability; check that this normalisation is legitimate for the j ≠ 4 choices too — if not,
keep β₁). Ideal I_B = ⟨the 24 cubics⟩ (after removing the common factor det C where it appears).
Claim to certify: V(I_B) ⊆ V(det C · β₁β₂β₃), i.e. `(det C · β₁β₂β₃)^N ∈ I_B` for some N, i.e.
(Rabinowitsch) `1 ∈ I_B + ⟨1 − t·det C·β₁β₂β₃⟩` in F[C, β, t].
Case A: split by which κ_j vanish and by the support pattern; formulate each sub-case as a similar
membership problem (the hypothesis "rank R = 3" = some 3×3 minor nonzero, Rabinowitsch again; the
hypothesis κ_j = 0 = a polynomial equation added to the ideal). Enumerate the sub-cases explicitly
(there are finitely many support patterns up to row/column permutation for 3×4 matrices); use the
singleton-column reduction to discard patterns with a weight-1 column.

## 2. Tool
Use `msolve` (INRIA, C, Gröbner bases over ℚ and 𝔽_p with F4): clone https://github.com/algebraic-solving/msolve
and build it INTO `~/.local/msolve` (no system directories, no Homebrew; `./autogen.sh && ./configure
--prefix=$HOME/.local/msolve && make -j4 && make install`; if GMP/FLINT are missing, build them into
~/.local too, or fall back to sympy's `groebner` for the smallest sub-cases — state which). Verify the
install on a toy ideal where you know the answer (e.g. ⟨x², y²⟩ + ⟨1 − t·xy⟩ must give [1]; ⟨x·y⟩ +
⟨1 − t·x⟩ must NOT). A Gröbner basis equal to [1] over 𝔽_p certifies the statement for EVERY field
of characteristic p; over ℚ, for every field of characteristic 0 AND for all but finitely many p —
extract the primes dividing the denominators/leading coefficients of the certificate if msolve
can output it, else run separately over p ∈ {2,3,5,7,11,13,17,19,23,29,31} and say which primes
remain uncovered. Print every basis that equals [1] and every one that does not.

## 3. Deliverables
For each (case, field) pair: the exact ideal (generators as text), the msolve/sympy command, the
result ([1] or not, with the basis size and time), and the certificate interpretation. A sub-case
whose basis is NOT [1] is a potential counterexample family: solve/describe V (msolve can compute
rational parametrisations of zero-dimensional parts) and print a concrete point — then check it
against `problems/k1695/round6_controllable.py:T_test` (the reference decision procedure) BEFORE
calling it a failure of (T_3). Report which characteristics are certified and which are not. End
with `DONE-K6T3`.
