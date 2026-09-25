# TICKET K6-N4n — rank-2 stratum (a): the odd-characteristic all-six-fail family — normal form, rescue, and the remaining 70 conjuncts

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4n/` (create): `REPORT.md`
ending with `DONE-K6N4N`, scripts, logs. Exact arithmetic; sympy; msolve at `~/.local/bin/msolve`.
Caps 20 min / 8 GB per computation. Read `engine/harvest/k1695_r6_n4m/REPORT.md` first (16 shape
orbits, 92 conjuncts, the 22 conjuncts with verdicts, the GF(7) counterexample to the char-2 reading).

## The new object
A = [[2,3,4,6],[3,2,6,4],[4,6,2,3],[6,4,3,2]] over GF(7): symmetric, every row a permutation of the
same four entries, constant row/column sums (= 1 mod 7), spectrum {1,1,2,4}, rank(A − I) = 2, all six
transpositions non-cyclic, double transpositions rescue. 𝟙 is a right AND left eigenvector (constant
sums): this is the constant-eigenvector sub-case that N4f/N4j/N4m's partition-graph reasoning
excluded ("L_ν or R_ν complete"). Note the structure: A = c·I + (a circulant-like / "Klein
four-group" pattern): A_{ij} = f(i ⊕ j) for the Klein group Z₂×Z₂ acting on {0,1,2,3} — i.e. A is in the
group algebra of V₄ = {0, (01)(23), (02)(13), (03)(12)}: A = Σ_g f(g) P_g! Check this (the entries
2 at g = id, 3 at (01)(23), 4 at (02)(13), 6 at (03)(12)). If so, A commutes with the three double
transpositions and A P_τ for τ a transposition has extra structure — explain the six failures from
this symmetry, and the rescue by double transpositions (A·P_g = Σ f(h) P_{hg} is again in the group
algebra — cyclic iff … the four characters χ of V₄ give eigenvalues Σ_h f(h)χ(h) …). Work this out
exactly: for A = Σ_{g∈V₄} f(g)P_g invertible, when is A·P_σ cyclic for each σ ∈ S₄?

## Tasks
1. Normal form of the odd-characteristic all-six-fail family: is every all-six-fail input in odd
   characteristic (from the shape/conjunct data of N4m, restricted to non-char-2 components) in the
   V₄-group-algebra family up to relabelling/transpose/scaling, or are there others? Use N4m's
   non-[1] components: extract their varieties (msolve rational parametrisation / describe positive-
   dimensional parts), give explicit parametrised normal forms, and PROVE (over every field where
   they exist) that some double transposition (or other permutation) works there — with the exact
   rank-two criterion (K6-N4d) or a direct Krylov certificate as N4f did. Machine-check each family:
   10⁵ constrained samples over GF(3,5,7,11,13) and the exhaustive GF(3) rank-2 census (477 750).
2. The remaining 70 conjuncts of N4m: run them (msolve, per characteristic ℚ, 2, 3, 5, 7, 11, 13) and
   record [1] / not [1] (with the variety) / capped. Aim: a complete table "conjunct × characteristic".
3. Consistency: every all-six-fail input found by search (GF(4) 216; GF(7): enumerate the V₄ family
   exhaustively and also a 10⁶-presentation search over GF(5), GF(7), GF(9), GF(11)) must land in a
   classified family with a proved rescue.
4. Report the exact statement certified: "rank-2 stratum (a) at n = 4: in characteristic p ∈ {…} every
   input has a cyclic A P_σ with σ a transposition or a double transposition [or …]". End with
   `DONE-K6N4N`.
