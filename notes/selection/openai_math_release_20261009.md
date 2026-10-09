# OpenAI "math" release (2026-10-06) — first screen against the automath portfolio

Written 2026-10-09 by the coordinator (Fable 5.1), on the owner's instruction (AUT-26) to study the
release before any further selection. Scope: a keyword/title screen of the public catalogue, not a
proof audit. Nothing here re-verifies any OpenAI claim.

## Facts (from the repository itself, read 2026-10-09 ~14:40Z)

- Repository: https://github.com/openai/math (Apache-2.0). Files read: README.md, CONTENTS.md
  (manuscript map, 639 KB), overview.tex (catalogue by discipline), history.md, lean/formalization.yaml.
- Catalogue: **719 manuscripts in 372 result families** (press said 722 on 10-06; 3 were withdrawn on
  10-07 — the Weil-classes/Kuga–Satake/K3 Hodge chain, sign error). 14 other manuscripts were revised
  on 10-07. The family list is kept in `openai_math_families_20261009.txt` (372 titles).
- Production: one unreleased internal model, ~3 h of "ChatGPT Pro thinking compute" per result,
  ~4,000 problems posed; exceptions: the zeta zero-free region and the CM-Hodge work.
- Formalization: the README says ~42 % of top-line results (300/719) have Lean proofs; 242 of the 372
  families carry a `lean/docs/NNN.md` link in CONTENTS.md. **Not checked by us**: what exactly the Lean
  statements cover (full theorem vs. a component), and no Lean build was run here.
- Reception (Nature 10-07, Daily Nous 10-07, AHM statement 10-08): manuscripts described as hard to
  read without AI help; the AHM asked for prompts and reasoning traces; community review is expected
  to take a long time. Treat every unformalized family as a **claim**, not a result, for G2 purposes.

## Disciplines (families)

Number theory 001–031; combinatorics 155–192; convex/metric geometry 087–101; TCS 102–154 (approx.);
the rest is algebraic geometry, analysis, dynamics, algebra, probability, logic, groups, physics,
operator algebras, topology, functional analysis, differential geometry, PDE.

Number theory (31): Milne rationality; BSD in Selmer corank ≤ 1; quasi-RH (zero-free Re s > 11/12,
also stated as 7/8 in press); Hilbert 10 over Q; irrationality of Catalan; Goldfeld; two-point
Chowla/corrected Elliott; Deligne–Drinfeld; Bogomolov–Pop; Fontaine–Mazur at 2; Ford–Konyagin–Luca;
joint Dickman law for consecutive integers (Erdős–Pomerance); Ostmann inverse Goldbach; Langlands/
Ramanujan–Arthur; torus-packet equidistribution; Zilber–Pink; μ(π)=2; Margulis–Platonov; p-adic
section; squarefree quartics; Jacobsthal quadratic bound; weak inhomogeneous Duffin–Schaeffer;
Patterson cubic Gauss sums; asymptotic for V(x) totients (+ Erdős large-fibre conjecture); **short
Egyptian fractions O(log log b)**; positive density of large prime gaps (Erdős–Prachar); Litt
integral density; Gaussian moat; Artin primitive roots infinitude; modularity over imaginary quadratic
fields; Uchida.

Combinatorics (38): periodic tiling counterexample in R³; Borsuk fails in dim 9; **Hadwiger
disproved** (+ Colin de Verdière); plane is not 5-colourable (χ(R²) ≥ 6); **Erdős reciprocal-sum
conjecture + quasipolynomial r_k(N)**; superexponential van der Waerden; Sidorenko/forcing
counterexamples; Ryser/Gyárfás counterexamples; Hindman sums-and-products; exact crossing numbers
(Zarankiewicz/Hill); **higher-dim distinct distances c_d n^{2/d}**; **weak pinned planar distances
n^{1−ε} + unit distances O(n^{4/3−δ})**; KL combinatorial invariance; Shareshian–Wachs; off-diagonal
Ramsey r(s,t) sharp log exponents; **Burr–Erdős hypercube Ramsey Θ(2^n)**; Euclidean Ramsey
classification; Seymour second neighbourhood; thin trees; Talagrand expectation thresholds; second
Kahn–Kalai; coboundary expanders; Ramanujan graphs every degree; **circulant Hadamard (orders 1, 4
only) + Barker**; Barnette; Erdős–Gallai cycle decomposition O(n); intersective polynomial
differences power saving (incl. square-difference-free N^{1−c}); halving lines n^{4/3−ε} (no three
collinear); Alon–Krivelevich–Sudakov; infinite matroid counterexamples; Friedgut–Kalai thresholds;
Snaky; random triangle removal constant; **cycle–clique Ramsey exact**; ordered-matrix removal;
**Heilbronn triangles n^{−2+c}**; Gopalan–Servedio counterexample.

## Portfolio overlap screen (keyword + title level)

| Our line / target | OpenAI family touching it | Verdict |
| --- | --- | --- |
| Erdős #30 Sidon second-order bound (published) | none ("Sidon" 0 hits) | no overlap |
| Erdős #156 minimal maximal Sidon | none | no overlap |
| Erdős #241 B₃ constant (AUT-24 running) | none ("B_3", "B₃", "Ruzsa" only in MUB family 266) | no overlap |
| Erdős #86 hypercube C₄ density (AUT-23 running) | 171 is hypercube *Ramsey*, not C₄-free density | no overlap |
| Erdős #1066 penny graphs (AUT-25 running) | none ("penny", "independence number" only in Hadwiger family) | no overlap |
| Erdős #1082 distinct distances from a point, no three collinear (AUT-22 running) | 167 weak pinned planar distances (all but o(n) points see n^{1−ε}); 183 halving lines with no three collinear | **adjacent, not the same statement**: #1082 is the exact-coefficient question (Szemerédi (n−1)/3); 167 is the ε-power statement. Attacker keeps running; the referee/G2 for AUT-22 must cite 167. |
| Zaremba explicit M (stopped) | none ("Zaremba", "continued fraction" 0) | no overlap |
| Erdős #708, #377, #859, #624, #889 | none on the keywords (binomial, Selfridge, covering, divisors, v₁) | no overlap |
| Capacity-transfer paper (sonar, weak Sidon, DTS) | none | no overlap |

## Catalogue entries that must change (selection library)

- `old_records_20261003.md` row 13 (#304/#18 short Egyptian fractions, "HOLD/LOW-FIT", frontier Vose
  √log b): family **025** claims the Erdős conjecture O(log log b) with a Lean link → mark CLAIMED-CLOSED
  (OpenAI 2026-10-06), pending community verification; drop from candidate pool.
- `old_records_20261003.md` exclusion row "#167" (unit distances) and `targets_20261003.md` card "Plane
  unit-distance upper coefficient": family **167** claims O(n^{4/3−δ}) → the old coefficient game is
  moot; keep NO-GO, update reason.
- `old_records_20261003.md` row 3 (#1082): add the adjacency note above (family 167/183).
- `famous_watch.md`: row 2 Kaplansky zero-divisor → family **196** claims a counterexample (finitely
  presented torsion-free group); row 10 Zariski cancellation → family **047** (affine fourfold); row 12
  circulant Hadamard → family **179** (proved, Lean); row 1 S^6 → one mention only, check. Rows 3
  (lonely runner), 4 (Agrawal), 6 (#699), 7 (#982), 8 (#617), 9 (#779), 13 (Jacobian n=2 — two
  "Jacobian" hits, check), 14 (CDC), 15 (Kalai 6(a)), 16, 17, 18: no title hit.
- `targets_20261003.md` cards "Diagonal Ramsey base" (family 170 is off-diagonal only — no change),
  "Hypercube C4 density" (no change), "Finite B3 leading constant" (no change), "Linnik exponent"
  (no hit), "Infinite-sequence star discrepancy" (no hit), "Minimum overlap" (no hit),
  "Directed triangles / Caccetta–Häggkvist" (no hit), "Union-closed" (no hit).
- `SELECTION.md` / strategy: the "famous problem × quantitative frontier" selector now has a new
  negative list: anything in the 372 families is crowded and, if formalized, closed. Also a new
  positive list: unformalized families in our area (e.g. 166 higher-dim distinct distances has no
  Lean link) are **referee-able claims**, which is a different kind of target (verification work,
  owner decision needed on whether automath does that).

## Actions taken / dispatched (2026-10-09)

1. This note + the family list committed.
2. Scout child issue: full G2 sweep of the 372 families against every catalogue file
   (famous_watch, old_records, targets_20261003, transfer_targets, shortlist/thin_screen, fc_catalog,
   TARGETS.md pool), reading the abstracts, not only titles; report which rows close, which are
   adjacent, and which unformalized families in additive/combinatorial number theory could be referee
   targets. Output: notes/selection/G2_OPENAI_RELEASE_20261009.md.
3. Round-4 part-2 probes (AUT-22..25) continue: none of their four targets appears in the catalogue.
4. No publication, no outward message. Owner decision requested separately on whether automath should
   referee OpenAI claims in its own area.

## Caveats

- Keyword screen only; abstracts of the 31 + 38 + 15 families in our disciplines were skimmed, the
  rest only by title. The scout sweep (item 2) is the real G2.
- Press numbers vary (722 vs 719; "20 %" vs "42 %" formalized); the repository README is the source
  of record and was read directly.
