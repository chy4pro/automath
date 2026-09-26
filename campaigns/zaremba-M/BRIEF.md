# Campaign: Zaremba's conjecture — explicit M for all large primes (slot 1, started 2026-09-26)

Design: DESIGN.md (from notes/selection/selection_v3_20260926.md §3.1). Strategy: notes/SELECTION_V3_20260926.md.
Record: Shkredov, arXiv:2603.14116v2 (2026): Zaremba holds for all sufficiently large primes q with M = 2^2000
(bookkeeping of his own chain gives log2 M ≈ 1680). Zhang arXiv:2605.02518: all q, effective but uncomputed M.
Numerics (zaremba_kappa_numerics.*): the true spectral gap of the Lemma-14 operator is ≈ 2√(N−1)/N (κ → 1/2),
against the proven 2^-1658 — the loss is entirely in the proof.
Targets: announce-worthy = log2 M ≤ 500 by a NEW LEMMA (not constant substitution), 4 referees + G2 clear;
strong = log2 M ≤ 150; moonshot = κ polynomial (M ~ 2^20–2^40).
Rules: no "first"/priority wording; owner rules on publication apply (announce only if announce-worthy);
no local SAT; numerics = numpy/mpmath on the 10-core box; every claim → 2–4 isolated adversarial referees.
Budget: 27.5M tokens / ≤ 3 days, hard cap 30M. Kill: K0 (h6) explicit M < 2^2000 already in print → re-scope;
K1 (h18) proceed only if a route has a written candidate gap lemma with conditional consequence log2 M ≤ 500.
Ledger: ledger.md (append-only, UTC timestamps from `date -u`).
