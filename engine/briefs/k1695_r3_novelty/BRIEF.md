# TASK K3-NOV — literature/novelty check for two Kourovka-16.95 results (line k1695, round 3)

This is a LITERATURE SEARCH task, not a mathematics task. Do NOT try to prove anything.
Deliver citations or a documented absence. Every negative must be accompanied by the
positive control that proves the channel was alive when you ran it.

## Background you need (self-contained)
Kourovka Notebook problem 16.95 (J. G. Thompson, 2006): *for every field F and every
A ∈ GL(n,F) there is a permutation matrix P such that AP is cyclic* (cyclic = nonderogatory
= minimal polynomial equals characteristic polynomial). It is open. The only claimed proof,
John D. Dixon, arXiv:1606.02238, was WITHDRAWN in 2017 after A. Stasinski produced a
counterexample to its key Proposition.

HOMONYM TRAP, this is the main failure mode of this search: "Thompson's conjecture" in the
literature almost always means the conjecture on conjugacy-class sizes of finite simple
groups, which is a DIFFERENT conjecture and dominates every search term. Also "cyclic matrix"
collides with (a) "p-cyclic matrices" in SOR/iterative numerical analysis and (b) "cyclic
matrix" density results of Neumann–Praeger / Praeger–Glasby (same nonderogatory sense but
about random-matrix proportions over finite fields). Discard all three; say so explicitly
when you do.

A prior sweep (zbMATH Open REST API, ~35 queries with positive controls, plus Crossref,
OpenAlex, the author's own CV) already established: no journal version or successor to
arXiv:1606.02238 under any title, and no prior appearance of a cyclicity criterion for the
specific family aI + bJ (J = all-ones). MathSciNet was NOT reachable (subscription wall).
**Do not re-do that sweep.** The two questions below are NEW and were never searched.

## Q1 — the criterion
Is the following, or any equivalent, in the literature?

> Let F be a field, D = diag(d_1..d_n) invertible, P_c the cyclic-shift permutation matrix,
> u,w ∈ F^n, M = D·P_c + u wᵀ. Put Dp_j = d_1⋯d_j, δ = Dp_n, χ(x) = x^n − δ. Then M is
> nonderogatory ⟺ gcd(χ, Pu, Pw, Pα − δ) = 1 in F[x], where
> Pu = Σ_j (u_j/Dp_j) x^{j}, Pw = Σ_j w_j Dp_j x^{n−j}, Pα = Σ_{t≤j} w_j u_t (Dp_j/Dp_t) x^{n+t−j}.
> Equivalently: M is derogatory at λ (λ^n = δ) iff the left eigenvector of D·P_c at λ
> annihilates u, the right eigenvector annihilates w, AND a third "secular" quantity equals 1.

I already believe this is an instance of CLASSICAL machinery, and the honest expected answer
is "known modulo transformation". Specifically: a monomial cyclic matrix is diagonalisable
over a splitting field, and after that change of basis the statement becomes the standard
eigenstructure theory of a DIAGONAL PLUS RANK ONE (DPR1) matrix — where "λ = d_i is a
multiple eigenvalue iff x_i = y_i = 0 plus a secular condition" is textbook (Golub 1973;
Bunch–Nielsen–Sorensen 1978; and in control-theory form the Popov–Belevitch–Hautus test,
cf. Ferrante–Wimmer, *Reachability matrices and cyclic matrices*, ELA 20 (2010) 95–102).
**What I need from you is the specific citation to hang this on, not a verdict.** So:
1. Find the best available published statement of the DPR1 / rank-one-update derogatory
   criterion over an ARBITRARY FIELD (not just ℝ or ℂ — most numerical-analysis sources
   assume real symmetric or complex; a statement valid in characteristic p is what matters).
   Give author, title, venue, year, DOI, and the exact theorem/equation number.
2. Find any source that states the analogous criterion for a rank-one perturbation of a
   MONOMIAL or PERMUTATION matrix, or for the pencil "permutation matrix minus λ·(rank-one
   perturbation of a scalar)".
3. Report whether the "third clause" (the secular condition, the case where BOTH eigenvector
   conditions hold and derogacy still fails) appears explicitly anywhere, or whether sources
   state only the two-clause necessary condition.
4. Rank-one perturbation invariant-factor interlacing (this is R. C. Thompson's own theorem,
   a THIRD homonym — "Thompson" again — be careful): give the canonical citation.

## Q2 — the small case
Is "Kourovka 16.95 holds for n ≤ 3" (or n ≤ 4, or any n) stated anywhere — in a paper, a
survey, a thesis, a Kourovka Notebook comment, a MathOverflow/StackExchange answer, a
seminar note, a preprint, or a formalisation repository?
Also: has ANY partial result on 16.95 been published since 2017?
Search must include, and you must report per channel: arXiv full-text, zbMATH Open
(api.zbmath.org/v1 is free and needs no key), Crossref, OpenAlex, Semantic Scholar,
Google/Bing web, MathOverflow + math.StackExchange, GitHub (leanprover-community/
formal-conjectures and any Lean/Isabelle formalisation), and X/Twitter or self-hosted PDFs
(recent famous-problem work has appeared there before arXiv).

## Deliverables — format exactly this way
1. A table: one row per query actually run — the verbatim query string, the channel, the raw
   hit count, and the disposition. Queries you did not run must not appear.
2. POSITIVE CONTROLS, run in the same session, proving each channel was alive: at minimum
   a query that MUST return hits (e.g. `an:arXiv:1606.02238` on zbMATH returns exactly 1,
   with the title beginning "WITHDRAWN:"). If a channel is behind a login or rate-limited,
   report it as a DEGRADATION, separately from any negative — never fold the two together.
3. For every candidate hit: full citation + DOI/URL + the sentence you are relying on,
   quoted verbatim. Do not paraphrase a paper you did not open.
4. An explicit list of what you searched for and did NOT find, and an explicit statement of
   what your sweep does not cover.

## Rules
- No mathematics, no proofs, no opinions about whether the results are interesting.
- "Not found" is a completely acceptable and useful answer. Fabricated or unopened citations
  are the only failure mode that matters here — a made-up DOI is worse than an empty table.
- If you cannot open a source, say so and mark the row UNVERIFIED.
