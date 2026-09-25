# TICKET K6-N4z — ALL characteristics for rank 1 at n = 4: the integer N with N ∈ I_ℤ (ℤ-Gröbner basis), then the bad primes

Output to `engine/harvest/k1695_r6_n4z/` (create): `REPORT.md` ending with `DONE-K6N4Z`, scripts,
inputs, outputs, logs. Exact arithmetic. Load rule: at most 2 heavy processes; caps 40 min / 8 GB per
computation. You may download and build Singular (https://www.singular.uni-kl.de, source tarball or
GitHub Singular/Singular) INTO `~/.local` only (autotools, GMP, MPFR, FLINT are already built in
~/.local by K6-T4 — reuse: `~/.local/{bin,lib,include}`; NTL/readline: build into ~/.local if the
configure demands them, or disable). No system directories, no Homebrew.

## The ideal
The 15 nonzero integer polynomials D_{0,j,τ}(a,b,c,y₁,y₂,y₃) of the fixed-row family
R = [x, e₁+y₁x, e₂+y₂x, e₃+y₃x], x = (a,b,c): D_{0,j,τ} = det[c_j, M c_j, M² c_j], j ∈ {1,2,3}, M = the
other three columns of R in the order τ (18 expressions, 3 identically zero). Regenerate them YOURSELF
with sympy over ℤ (do not copy from `engine/harvest/k1695_r6_n4k/ideals/`; compare afterwards — they
must coincide up to sign with the determinants in `r1_S_a_p0.ms` minus its S/t/r generators).
Known (msolve, reproduced by the line): the ideal I = ⟨D_1..D_15⟩ ⊂ ℚ[a,b,c,y₁,y₂,y₃] is the UNIT
ideal, and the same over GF(p) for p ∈ {2,3,5,7,11,13,17,19,23,29,31}. Hence I_ℤ ∩ ℤ = (N) for some
integer N ≠ 0, and the rank-1 stratum of Kourovka 16.95 at n = 4 holds in every characteristic not
dividing N. Goal: compute N (or a multiple of it), factor it, and run msolve over GF(p) for every
prime p | N — then the statement is proved in EVERY characteristic.

## Method A (preferred): strong Gröbner basis over ℤ
Singular: `ring r = integer,(a,b,c,y1,y2,y3),dp; ideal I = ...; ideal G = std(I);` — the constant
element of G generates G ∩ ℤ = (N). Print G's constant, factor N (Singular `factorize` or Python).
Verify: for each prime p | N, msolve over GF(p) on the same 15 generators: if `[1]`, the characteristic
p is fine; if not `[1]`, print the basis (that characteristic would be a genuine gap — check it
against exhaustive finite-field data: over GF(p) enumerate all (x, y) ∈ GF(p)⁶ and evaluate the 15
determinants — p ≤ 31 is already covered, so any bad prime must be ≥ 37).
Controls: (i) the toy ideal ⟨2x, 3x⟩ over ℤ has G ∩ ℤ = (0) and ⟨x, 2⟩ gives (2)…; use
⟨x² − 2, x − 3⟩: N = 7 (since 9 − 2 = 7) — assert Singular returns 7; (ii) a sub-ideal of 3 of the
determinants must NOT be the unit ideal over ℚ (msolve), showing the pipeline distinguishes.
## Method B (fallback if Singular does not build): modular Macaulay certificate
Find the minimal degree D such that 1 ∈ ⟨D_k⟩ in degree ≤ D over GF(P) for a large prime P (e.g.
P = 2³¹ − 1), by solving the sparse Macaulay linear system mod P (write the elimination in C or use
numpy int64 with careful modular reduction; exploit sparsity); then compute the rational certificate
at that degree by solving mod several primes and rational reconstruction (CRT + Wang's algorithm),
clear denominators, verify Σ g_k D_k = N by exact expansion (sympy), factor N, and finish as in A.
Report the degree D, the sizes, timings, N, its factorisation, and the per-prime msolve results.
End with `DONE-K6N4Z`.
