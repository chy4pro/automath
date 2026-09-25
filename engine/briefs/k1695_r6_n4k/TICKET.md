# TICKET K6-N4k — msolve on the rank-1 residual systems (6 variables) and the rank-2 charts (14 variables); integer certificates

Self-contained; no internet. Output to `engine/harvest/k1695_r6_n4k/` (create): `REPORT.md` ending with
`DONE-K6N4K`, every ideal file, basis, log. Exact arithmetic. Caps: 40 min / 8 GB per computation
(reuse `engine/harvest/k1695_r6_T3/run_capped.py`); sequential.
**Tool:** msolve was built by K6-T4 into `~/.local/msolve` (check `engine/harvest/k1695_r6_T4/` for the
binary path and its build log; if it is not there, build it the same way — autotools/GMP/MPFR/FLINT
into ~/.local are allowed). Verify on the two toy ideals first (⟨x²,y²,1−txy⟩ → [1]; ⟨xy,1−tx⟩ → not [1]).

## Part 1 — rank 1 (closes the rank-1 stratum of n = 4 if [1])
Read `engine/harvest/k1695_r6_n4h/REPORT.md` §2–3 and `symbolic.log`. The fixed-row family is
R = [x, e₁+y₁x, e₂+y₂x, e₃+y₃x], x = (a,b,c), y = (y₁,y₂,y₃) (deleted row i with v_i normalised to 1;
scaling u ↦ v_i u, v ↦ v/v_i leaves A = I + uvᵀ unchanged). The F1 column works iff S·Q ≠ 0
(S = a+b+c, Q = a²+b²+c²−ab−bc−ca). Residual systems, each with Rabinowitsch inequations:
  (10) 𝒰_S: S = 0, all 18 F2 determinants D_{0,j,τ}(a,b,c,y) = 0 (j ∈ {1,2,3}, τ ∈ S₃), and
       1 − t·(1 + vᵀu) = 0 where 1 + vᵀu is expressed in the normalised variables (write it out:
       with v_i = 1 and u′ = x, vᵀu = u_i + Σ_k y_k x_k … derive the exact expression from (2)–(3) of
       the N4h report and SAY what it is);
  (11) 𝒰_Q: Q = 0 and the same.
  Also add the inequation x ≠ 0 (rank one): Rabinowitsch on a chosen coordinate, i.e. three charts
  (a ≠ 0), (a = 0, b ≠ 0), (a = b = 0, c ≠ 0) — or argue why x = 0 is already excluded.
Run each over ℚ and over GF(p) for p ∈ {2,3,5,7,11,13,17,19,23,29,31}. A basis [1] on both systems
in a characteristic proves: for every invertible I + uvᵀ over every field of that characteristic,
the least i with v_i ≠ 0 admits a column and an ordering — i.e. e_i is a cyclic vector of some A P_σ
— i.e. **Kourovka 16.95 for all rank-one A at n = 4 in that characteristic**. Print the exact
statement you have certified, per characteristic.
If some basis is NOT [1]: compute the variety (msolve can output a rational parametrisation for
zero-dimensional components; otherwise describe the positive-dimensional component) and produce a
concrete point (u, v); test it with `problems/k1695/round6_controllable.py:T_test` on R and with the
full 4×4 cyclicity over all 24 permutations — it may be a point where a DIFFERENT deleted row works
(the observation, not the theorem, fails), or a genuine 16.95 counterexample (re-verify three ways).

## Part 2 — integer certificate (all characteristics at once), rank 1
For each system that is [1] over ℚ: find an explicit Nullstellensatz certificate over ℤ:
integers N ≠ 0 and polynomials g_k with N = Σ_k g_k f_k (f_k the generators incl. the Rabinowitsch
ones). Method: fix a degree bound D (start at the max generator degree + 2), set up the linear system
for the unknown coefficients of the g_k (Macaulay-matrix style) over ℚ, solve with exact rational
linear algebra (sympy or fraction-free Gaussian elimination in Python), clear denominators, and
verify the identity by exact polynomial expansion. Print N and its prime factorisation: the
statement then holds in every characteristic not dividing N; the primes dividing N are exactly the
ones needing the separate msolve runs of Part 1 (run them). If the linear system is too big at the
needed degree, say so and report the degree reached.

## Part 3 — rank 2 (as far as msolve gets)
From `engine/harvest/k1695_r6_n4i/REPORT.md` §3: the three 14-variable charts (8) (U = [I₂; a b; c d],
W free with the pivot-pair chart J ∈ {01, 02, 23}, Rabinowitsch for det(I₂ + WᵀU) ≠ 0 and det W_J ≠ 0,
92 determinants). Run msolve on the 12-simplest-determinant subideal first (a [1] there closes the
chart), then the full system, over GF(2), GF(3), GF(5), GF(7) and ℚ, within the caps. Report
per (chart, characteristic): [1] / not [1] / capped.

## Report
Per system: generators (file), command, result, time; the certified statements per characteristic;
Part 2's N and factorisation; residuals exactly. End with `DONE-K6N4K`.
