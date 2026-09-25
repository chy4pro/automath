# SELECTION SCAN 09-02 (Fable 5.1, Plan A) — working notes, honest register
Source of truth: teorth/erdosproblems data/problems.yaml (1217 problems; 600 open, 9 decidable, 7 verifiable,
26 falsifiable). Statements read from erdosproblems.com pages (fetched one at a time, 3 s apart).

## Step 1 verdict: the 16 "reduced to a finite computation" problems are NOT slot-2 material
Nearly all "decidable" entries are "proved for all sufficiently large n" via regularity/absorption methods with
NON-EXPLICIT thresholds (EFL #19 KKKMO21; tree Ramsey #547/#580 Zhao; #551 KLS21; #556 KSS05; #742 Füredi;
#848 Sawhney; #475 four-paper patchwork). The residual "finite" range is not actually computable. #506 is a
continuous geometric problem for 9<=n<=393. The "verifiable" ones are search problems with no feasibility
evidence (#7 odd covering, #364 powerful triples below 7e28 already, #647 £25 search, #672 deep Diophantine).
Only #835 (Johnson graph J(2k,k) with k+1 prime, Ma–Tang residual) has a clean LLM attack surface, low attention.
LESSON: the database's "decidable" flag is a logical classification, not a feasibility one.

## Step 2: attention-weighted scan of the 600 OPEN problems (in progress)
Scoring: prize, elementary tags (number theory / primes / divisors / covering / unit fractions / additive comb.),
Lean-formalized statement, activity in 2026, comments, AI-involvement flag from the project wiki.
Top 80 saved to scratchpad/open_scored_top80.json; statements of the top ~40 to be read next.

## Step 3 (in progress): source reading on the emerging shortlist
- #835 (Johnson graph J(2k,k), chi = k+1?): false for 3<=k<=8 (computed); Ma-Tang 2025 note proves chi > k+1
  unless k = p-1. Residual k in {10,12,16,18,...}. Reading Ma-Tang PDF next to learn the obstruction.
- #1212 (visible lattice points, strengthened path): only the weak version is settled (Stewart via consecutive
  primes, needs p_{k+2} < 2p_k). Strengthened version (a composite coordinate at every vertex) has no recorded
  progress. Running a box-reach experiment to gauge whether the restricted graph even percolates.
- #1189 (irreducible covering sets): OEIS has NO sequence for I(k) or min n_k -> a certain, verifiable but modest
  contribution channel (compute small k with certificates, submit OEIS + database PR).
- #1109/#1103 (A+A squarefree): Tao-active (van Doorn-Tao 2025 on #1103); constructions are machine-checkable but
  beating Konyagin's bounds needs new ideas. Held as reserve.
