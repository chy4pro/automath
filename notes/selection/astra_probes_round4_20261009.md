# Round 4 clean-room probes through Paperclip — verdict (2026-10-09)

Coordinator: Fable 5.1 (Paperclip issue AUT-11). Chain: AUT-12/13 (attackers, gpt-6-astra, Codex
container, clean room) → AUT-14/15/16/17 (Claude referees, cross-vendor) → this file. Nothing was
published, nobody was contacted. The attacker reports are left exactly as reviewed; the status
downgrades below are the coordinator's verdict, not edits to the reviewed files.

## T1 — Erdős #156, minimal maximal Sidon sets (AUT-12, attacker-1)

- **STATUS: OPEN** for the target s(N) ≪ N^{1/3}(log N)^θ, θ < 1/3. The attacker wrote PARTIAL;
  both referees require OPEN (the report's own line 9 says the target remains open, and its line 446
  contradicts that). Coordinator agrees: nothing proved is a bound on s(N) beyond the classical one.
- **Proved (all re-derived by both referees, every finite table reproduced to the digit):**
  - exact blocking criterion (A ∪ {x} fails to be Sidon iff x ∈ T(A) ∪ Q(A)) and the lower bound
    2N ≤ m³ + m for every maximal set (classical, explicit constant);
  - fibre criterion (3)–(4): stacking integer levels over a modular Sidon support D ⊆ Z/MZ is Sidon
    iff the positive differences inside the level sets are globally distinct;
  - lift-repair bound (5): s(HM) ≤ k + H − 1 + u, k = |D|, u = number of initially unblocked points
    in unoccupied residues — reduces route (a) to bounding u;
  - Singer perfect difference set (6); exact coverage counts (7)–(10) for the cubic curve in F_p³:
    roughly half of the group stays unblocked, so it is not a host (group model only);
  - witness structure of perfect difference sets (k ordered representations, degree ≤ 3, ≤ 1 shared
    triple), Harris/FKG two-sided recurrence (13), first and second moment (14)–(16), and theorem (17):
    independent thinning of a perfect difference set at density ρ = C k^{−1/3}(log k)^θ, θ < 1/3,
    leaves unblocked outside points with probability ≥ 1 − J(C)k^{−1/6}. Onset astronomically large
    (k ≥ exp(2.35·10^11) at C = 1, θ = 0.3; k ≥ e^128 at C = 2, θ = 0) and vacuous at every testable k.
- **Referee verdicts:** referee-1 PASS-WITH-REPAIRS (`notes/review/REF_referee-1_erdos156_20261009.md`),
  referee-2 PASS-WITH-REPAIRS (`notes/review/REF_referee-2_erdos156_20261009.md`). No mathematical
  error, no circularity, no quantifier slip. Repairs: status word; line 446 contradiction; scope
  qualifiers "in F_p³" and "in Z/MZ, outside-D coverage only"; "k ≥ e" → "k ≥ K(C,0)"; state the
  general dependence λTr(z)+μTr(αz)=0 in §2.4; say frankly that the onset is astronomical.
- **Reading of the seeds.** Seed (b) as stated is dead: for the natural sampler the union bound is
  not the lossy step, the sampler itself fails below the logarithmic scale, and it can never give a
  maximal set unless A = D. Seed (a) reduces to one question: u ≤ Ck at H ≍ k. Referee-2's heuristic
  (not a claim of the report): an outside residue r is blocked at level j iff j = h_a + h_b − h_c +
  carry for one of its ≈ k/2 witnesses, so independent heights pay a coupon-collector factor and give
  H ≍ k/log k, i.e. exactly (N log N)^{1/3}; the missing step is a correlated, design-like choice of
  heights under which the witness levels of almost every outside residue cover {0,…,H−1}, then passage
  from N = HM to every N.
- **Obstruction (exact):** no construction in the report controls u, and no repair bound for the holes
  left by thinning; both routes stop exactly where Ruzsa's log factor enters.
- **Grade: small result** (one reusable reduction lemma, two correct model-specific negative lemmas).
  Reason: no statement about s(N), no restricted case, no interval statement. Not publishable;
  repository note only.

## T6 — Erdős #30 beyond the kernel barrier (AUT-13, attacker-2)

- **STATUS: OPEN** for F(N) ≤ √N + cN^{1/4} + o(N^{1/4}) with c < 2√2/3. Attacker wrote PARTIAL; both
  referees require OPEN. Coordinator agrees: no inequality on c, no κ > 0, no restriction of the
  extremal profile.
- **Proved (re-derived by both referees; all finite checks reproduced, including exhaustive Sidon
  enumeration through N = 24 and 60-digit mpmath for (13)/(14)):**
  - exact window-moment identities (1)–(4) (Σr = S, Σr² = S + 2P, Σr³ = S + 6P + 6H, and the
    decomposition of the third moment into residual Q, centred third moment R and H);
  - integrality and third-order correlation bounds (5)–(11), in particular C₃(u,v) ≤ 1, hence only
    UPPER bounds on H from the Sidon property;
  - Proposition 1.4: the single-scale triangular-kernel + scalar-cubic + integrality relaxation admits
    Q/(Tm) ≤ 1/(2s) for every cardinality in its range, so this relaxation cannot give κ > 0;
  - §1.5: two six-point homometric sets with different H (pair data do not determine H);
  - §2: an explicit infinite Sidon family (b_i = 2pi + (i² mod p)) of total size 2m ≈ 1.38 N^{1/4}
    whose two halves sit in the two end windows — the end-cluster COUNTS are realisable, which is
    automatic since m² ≈ 0.48 N^{1/2} ≪ L ≈ 0.1 N^{3/4};
  - difference budgets (15)–(16): end-cluster counting is slack by a factor of order N^{1/4}.
- **Referee verdicts:** referee-1 PASS-WITH-REPAIRS (`notes/review/REF_referee-1_erdos30_20261009.md`),
  referee-2 PASS-WITH-REPAIRS (`notes/review/REF_referee-2_erdos30_20261009.md`). No error. Repairs:
  status word; "realizing both endpoint clusters" → "realizing the cluster counts, no bulk, no
  difference below p+1"; state that Prop. 1.4 lives at the triangular-kernel level c = 1 — its range
  includes cardinalities m > s² + (2√2/3)s + 1 already excluded by the published bound, and its
  witnessing arrays violate r(1) ≤ 1 — so it is a no-go for that relaxation only, not for third-order
  information on top of the optimal kernel; cosmetic wording (k_d ≤ √(2d); p ≥ 5 suffices).
- **Reading of the seeds.** Seed (a) in its literal form cannot work: the Sidon property gives only
  upper bounds on third-order correlations, and by identity (4) an upper bound on H never lower-bounds
  Q; one needs a third-order LOWER bound, or control of the centred third moment R, extracted from
  the 0/1 structure, and it must be combined with the optimal kernel, not the triangular one. Seed (b):
  the clusters cannot be refuted by counting differences inside or across the two windows; any
  realizability obstruction must couple the clusters to the ≈ √N hyperuniform bulk and to the
  saturation of every difference below ≈ 1.5 N^{3/4} (a positional constraint on the window profile).
- **Obstruction (exact):** unchanged from the brief — no quantity of order |A| in the residual energy
  that distinguishes 0/1 sets from the balanced relaxations has been identified.
- **Grade: small result** (negative lemma: scalar third-moment relaxations are dead at the triangular
  level; the homometric pair is a clean witness). Not publishable; repository note only.

## Decisions

- Both lines are at the method limit for probe-level work. T1 is parked: a further probe is justified
  only with a concrete correlated-height design (the one identified live step). T6 "beyond the kernel
  barrier" is parked: the published bound stands; the next useful work on #30 remains the follow-ups
  listed in OPERATIONS (onset, kernel optimality, Lean), not a third-moment attack.
- No referee repairs are applied to the attacker files (provenance of the reviewed artefacts); this
  file is the status of record. Both probes and all four referee reports are committed as research
  record. No Zenodo, no X, no site claim, no e-mail.

## Cost (from the instance run logs; the run-scoped bridge blocks GET /api/heartbeat-runs/{id})

| Run | Agent / model | Wall | Input (cached / cache-read) | Output | List cost |
| --- | --- | --- | --- | --- | --- |
| 2d342033 (AUT-12) | attacker-1, gpt-6-astra | 05:05→05:20 | 610,003 (547,840 cached) | 33,967 (19,341 reasoning) | subscription-included |
| af4e020e (AUT-13) | attacker-2, gpt-6-astra | 05:05→05:18 | 486,509 (423,424 cached) | 29,063 (17,133 reasoning) | subscription-included |
| ae57cc89 (AUT-14) | referee-1, claude-fable-5-1 | 05:24→05:33 | 292 + 626,467 cache-read + 92,871 cache-write | 37,089 | USD 3.87 |
| dff4dd25 (AUT-16) | referee-1, claude-fable-5-1 | 05:24→05:33 | 260 + 575,288 cache-read + 90,020 cache-write | 37,910 | USD 3.84 |
| fb142af8 (AUT-15) | referee-2, claude-opus-5-5 | 05:24→05:38 | 54 + 2,328,627 cache-read + 134,644 cache-write | 75,633 | USD 3.06 |
| 9558217b (AUT-17) | referee-2, claude-opus-5-5 | 05:24→05:40 | 40 + 1,589,735 cache-read + 123,448 cache-write | 69,630 | USD 2.70 |
| feb9c1d6 (AUT-11 step 1) | coordinator, claude-fable-5-1 | 05:02→05:07 | 548 + 1,075,767 cache-read + 71,371 cache-write | 13,247 | USD 2.36 |
| fa0f844c (AUT-11 step 2) | coordinator, claude-fable-5-1 | 05:20→05:27 | 674 + 1,623,983 cache-read + 99,979 cache-write | 20,246 | USD 3.42 |
| 8f811b2f (AUT-11 step 3) | coordinator, claude-fable-5-1 | 05:40→ | written before the run closed; read its log for the final figure | — | — |

Overhead not in the table: two `setup_failed` first runs per attacker (zero tokens, no log; the
low_trust_review preset needed a boundary scope, fixed in commit f178e84 before the retries ran).
Mathematical compute inside the probes: 0.58 and 0.31 CPU-seconds (node, single thread); referees
under 1–5 CPU-minutes of python3 each. No solvers, no paid cloud.
Chain totals: Claude list cost USD 19.25 for referees + coordinator steps 1–2 (step 3 excluded);
Astra tokens 1,096,512 input / 63,030 output, subscription-included. Wall time dispatch→last referee
report: 05:02 → 05:41 (39 minutes) for two probes and four cross-vendor reviews.

## Comparison line: did the Paperclip chain cost less coordinator attention than the inbox lane?

Yes for attention, with caveats. The whole round took three coordinator heartbeats (about 5, 7 and
~10 minutes of run time) and roughly 50k output tokens of my own; everything in between (dispatch,
clean-room enforcement by issue text, wake-on-close, referee fan-out, status propagation) was done by
the control plane without polling. In the inbox lane the coordinator writes the brief file, waits on
inbox/STATUS.md, reads the harvest, then hand-dispatches each referee through Workbench session_run
and hand-collects their output; for round 3 no token or dollar total was available at all
(g2_prep_round3_20261003.md records clock intervals only). Caveats: (i) dollars are not comparable —
the inbox lane was never metered, and the four Claude referee runs cost USD 13.47 at list price;
(ii) the clean room is enforced only by the child-issue text — the attackers did read Paperclip skill
instructions outside /work, as they declare; (iii) the two setup failures and the adapter patches of
04:3x are one-time orchestration cost that an inbox round does not have; (iv) per-step cost is
dominated by cache reads of the long issue thread, so long chains should keep comments short.

---

# Part 2 — T2 #1082, T3 #86, T4 #241, T5 #1066 (AUT-21, verdict 2026-10-09 15:1x)

Chain: AUT-22/23/24/25 (attackers, gpt-6-astra, Codex container, clean room) → AUT-38…45 (Claude
referees, cross-vendor, two per probe) → this section. Same rules as Part 1: attacker files are left
exactly as reviewed; status words below are the coordinator's verdict. Nothing was published, nobody
was contacted. All four attackers wrote PARTIAL; all eight referees found no mathematical error and
reproduced every finite check exactly with their own code. Three of the four probes are downgraded to
OPEN by both referees and by me; the fourth (#1066) keeps PARTIAL for a restricted-class statement.

## T2 — Erdős #1082, distinct distances from a point (AUT-22, attacker-1; `problems/erdos1082/PROBE_ASTRA_3_20261009.md`)

- **STATUS: OPEN** for M ≥ (1/3+δ)n − O(1). Attacker wrote PARTIAL; both referees require OPEN
  (`notes/review/REF_referee-1_erdos1082_20261009.md`, `REF_referee-2_…`, both PASS-WITH-REPAIRS).
- **Proved (re-derived by both referees; all finite tables reproduced, including the 4×4 grid over
  all 65,536 subsets, the eight-point K₄, the polygon family m ≤ 31 at 60 digits, F₄^d for d ≤ 3,
  and the Petersen search 13,810 nodes / 288 leaves):**
  - exact accounting 3T = N + D + C, hence M ≥ (n−1)/3 + (D+C)/(3n), with D = missing apexes and
    C ≥ 0 the class-size defect; 9T = 3N + 2D + E; re-proof of M > (n−1)/3, so M ≥ ⌈n/3⌉ (known);
  - stability package: if M ≤ (1/3+ε)n + B then all but ≤ 18(3εn² + (3B+1)n) bases are kites whose
    two apex classes have size 3, and the kite graph H is 3-regular up to that many missing half-edges;
  - a planar saturated K₄ component of H exists (eight integer points), so component-local
    propagation of defects fails;
  - the F₄^d metric model satisfies every combinatorial hypothesis used (k_b ≤ 2, class sizes,
    pairwise class intersections ≤ 2, triple uniqueness, histogram moments) with D = C = 0 and
    M = (n−1)/3 < ⌈n/3⌉: no argument from those hypotheses alone can even recover the known bound.
- **Referee repairs:** status word; "obstructions to both routes" → "to the purely combinatorial
  relaxations of both routes, and a counterexample to one local propagation variant"; the §3.2
  polygon family bounds only D, not R = D + C; cosmetic label clash.
- **Obstruction (exact):** a Euclidean lower bound R = D + C ≥ cn² (or any direct bound on max_p t_p)
  from the geometry of an almost 3-regular kite graph whose edges are perpendicular-bisector kites.
  The planar fact the model violates is "no four pairwise-equidistant points" (equivalently, the
  centres of a K₄ component cannot collapse onto its base points); neither seed converts it into a
  quantitative gain. Referee-2's random triangular-lattice samples reach R/N = 0.5, no evidence either way.
- **Grade: small result** (one exact reformulation with explicit stability constants; one correct
  model-theoretic negative lemma). Not publishable; repository note only.

## T3 — Erdős #86, C₄-free subgraphs of the hypercube (AUT-23, attacker-2; `problems/erdos86/PROBE_ASTRA_4_20261009.md`)

- **STATUS: OPEN** for a human-readable π₄ ≤ c with c < 0.60318. Attacker wrote PARTIAL; both referees
  require OPEN because both proved bounds sit above both known bounds (`REF_referee-1_erdos86_…`,
  `REF_referee-2_erdos86_…`, both PASS-WITH-REPAIRS).
- **Proved (re-derived; Q₃ and Q₄ exhaustive counts reproduced by both referees with different
  decompositions — 2,902 C₄-free Q₃ graphs, 1,226,436,381 C₄-free Q₄ graphs, 828 degree histograms,
  47,775,744 rooted candidates / 25,002,059 valid, zero violations):**
  - hand proof π₄ ≤ 4^{−1/3} ≈ 0.62996 (≤ 2 full vertices per C₄-free Q₃ + Jensen);
  - certified Q₄ inequality n₁ + n₂ ≥ 3n₄ (⇔ T₃ + n₀ ≤ 16) for every C₄-free subgraph of Q₄, tight
    at 3 and 4 full vertices; face averaging gives p ≤ r + 3/n for n ≥ 4, r³ + 6r − 4 = 0,
    r = 0.625816818958…; hence π₄ ≤ r;
  - exact 5/8 mixture of five C₄-free Q₄ graphs whose averaged histogram is Binomial(4,5/8).
- **Referee finding beyond the report (both referees independently):** the face-averaged Q₄
  degree-histogram relaxation (any Q₄ histogram inequality + any one-vertex degree law) has value
  exactly r: referee-1 by the convex hull of the 828 histograms (8 facets, bisection p_max =
  0.625816819, unique tight facet = the certified inequality), referee-2 by an exact rational
  mixture at p = 0.6258168. So seed (a) at the 4-cube level is exhausted at r > 0.6068 > 0.60318,
  and single-root direction entropy (seed (b)) cannot see below 5/8.
- **Repairs:** status word plus the explicit sentence that r is weaker than 0.6068 and 0.60318;
  state the sharp obstruction (r, not 5/8); Appendix C's compression code projects instead of
  applying OR/AND (conclusion unaffected); "3/4 attained" → infimum. Referee-2 recalls from memory
  that 0.6068 is Thomason–Wagner and Chung's constant was ≈ 0.623 (not checked; the brief's
  attribution may be wrong — scout item if the line is ever reopened).
- **Obstruction (exact):** any proof below r must use information that is not a function of the
  per-face degree histogram: correlations between overlapping 4-faces, Q₅ configurations beyond
  their averaged Q₄ faces, or coloured/rooted flag-type data. ex(Q₅,C₄) = 56 was taken from the
  brief by everyone and not verified.
- **Grade: small result** (a cleanly certified, reusable Q₄ lemma with onset-exact averaging; a sharp
  negative result that closes the "Q₄ degree profile + Jensen" route). Not publishable.

## T4 — Erdős #241, B₃ sets (AUT-24, attacker-1; `problems/erdos241/PROBE_ASTRA_5_20261009.md`)

- **STATUS: OPEN** for c < 1.5154. Attacker wrote PARTIAL; both referees require OPEN
  (`REF_referee-1_erdos241_…`, `REF_referee-2_erdos241_…`, both PASS-WITH-REPAIRS).
- **Proved (re-derived; all 2,089 B₃ subsets of {1..20} and 36 explicit sets up to N = 20,971,523
  re-checked by both referees, referee-2 additionally all 49,544 B₃ subsets of {1..37} with m ≥ 2):**
  - exact representation structure: r = 2m−1 on A, 1 on T = {2a−b}, 2 on the rest of S = A+A−A,
    |S| = m + m²(m−1)/2, rigid one-point moments Σrᵏ; shift identity C(h) = 2m − 2H(h) + (2m−3)d(h) − B(h)
    with C = 2m²−m at 0, 4m−4 on D∖{0}, ≤ 2m off D; first-moment endpoint balance (22)–(24);
  - smoothing at scale L = ⌈N^{5/6}⌉: |A|³ ≤ 4N + 32N^{5/6} for all N ≥ 1 (limit 4^{1/3} ≈ 1.5874,
    weaker than 1.5154), and the conditional "weighted hole fraction θ_L ≥ 13/100 near A for N ≥ N_*
    ⇒ limsup ≤ 1.5153984", correctly quantified and labelled conditional;
  - the unsmoothed E₄ route gives constant 8; the endpoint balance gives only an O(N^{−1/6}) hole fraction.
- **Referee findings beyond the report:** referee-2 shows from the report's own identity (11) that
  θ_L = 1 − E_L/(2mL²) ± 5N^{−1/6}, i.e. the "hole fraction" hypothesis is a reparametrisation of the
  smoothed autoconvolution energy bound that the target itself requires — seed (a) as formalised
  supplies no new handle. Referee-1 argues the hypothesis fails in the density relaxation (the cap
  binds at h = 0), so it is genuinely a realizability statement, and that with the known
  autoconvolution inequality in place of Cauchy–Schwarz any fixed θ₀ > 0 would suffice. Both note the
  13/100 instance beats 1.5154 by 1.6·10^{−6}, inside the brief's rounding, and lies above the
  density barrier 1.5152 (a beyond-density improvement needs θ₀ > 0.130339). At N ≤ 37, 162 sets in
  the density regime have θ_L < 0.13, so no small onset exists.
- **Repairs:** status word; say in the status line that 4^{1/3} > 1.5154; (21)'s "substantial global
  hole fraction" is weaker than what the known bound already implies (0.42 vs 1/3); label the matching
  constraint as §2.1 uniqueness restated.
- **Obstruction (exact):** an upper bound E_L = Σ_h w_L(h)C(h) ≤ 2(1−θ₀)mL² with θ₀ > 0.130339 for
  B₃ sets with m ≥ 1.5N^{1/3} — the smoothed autoconvolution L²-norm problem itself. Nothing in the
  report uses the integrality of r or the matching structure quantitatively.
- **Grade: small result** (exact, effective identities with onset N ≥ 1; three correct negative
  lemmas). Not publishable.

## T5 — Erdős #1066, independence number of penny graphs (AUT-25, attacker-2; `problems/erdos1066/PROBE_ASTRA_6_20261009.md`)

- **STATUS: PARTIAL (restricted class), no progress on the target.** Both referees PASS without
  repairs (`REF_referee-1_erdos1066_…`, `REF_referee-2_erdos1066_…`) and both hold that PARTIAL is
  honest: a fully proved bound strictly above 6/23 holds on a non-empty restricted class. Coordinator
  agrees, with the project rule applied: a restricted case is not a bound for all penny graphs, and
  nothing here touches the target c > 6/23.
- **Proved (re-derived; 27 exact α values, 4 star unions, and 1,800 random multi-lattice penny
  graphs re-checked by the referees):**
  - rigidity: degree-6 vertices at graph distance ≤ 2 share one triangular lattice that also contains
    all their neighbours (H-components); all degree-6 neighbours of a non-degree-6 vertex lie in one component;
  - weighted certificate (1): α_w ≥ w(S)/3 + w(T₀)/4 + w(T₁)/6 + w(T₂)/12 by a random 3-colouring per
    component plus the 4-colour repair (penny graphs are 3-degenerate); hence
    α ≥ max{⌈n/4⌉, ⌈(n+3s)/12⌉} for every penny graph, and α ≥ 13n/48 > 6n/23 when s ≥ 3n/4
    (beats 8/31 once s > 65n/93; non-vacuous: hexagonal patches B_r, r ≥ 7, and rhombi R_m, m ≥ 15);
  - the triangle–square strip family F_(W,H): no degree-6 vertices, all but 4M−4 vertices of degree 5,
    zero combinatorial curvature, α = n/3; on it every degree-only Caro–Wei certificate is ≤ n/6 + O(M),
    below 6/23 for M ≥ 70 and below 1/4 for M ≥ 78 (the report's onsets 72/80 are sufficient, not sharp).
- **Obstruction (exact):** the degree-5-dense regime s ≤ 2n/3 (and s = o(n)), where (1) gives
  exactly n/4 and no Euclidean rigidity is available; the target needs a gain of more than n/92 over
  the four-colour bound there, i.e. a selection or reducible-configuration argument, which the
  report does not have. Editorial: notation clashes (H, M), "sufficient onsets".
- **Grade: small result** (reusable rigidity lemma + weighted certificate with explicit loss term;
  one correct negative family). Not publishable; repository note only.

## Decisions (Part 2)

- **All four lines parked at the probe-level method limit.** No campaign is proposed; no selection
  record is opened.
  - #1082: park. A further probe is justified only with a concrete quantitative Euclidean lemma
    candidate for R ≥ cn² (kite geometry / no four equidistant points), not with counting.
  - #86: park. The Q₄-histogram route is provably exhausted at r; a human-readable proof below
    0.60318 needs flag-type correlation data and is beyond a bounded probe. If reopened, the scout
    first checks the attribution of 0.6068 / 0.623.
  - #241: park. Seed (a) is the autoconvolution energy problem in disguise; seed (b) is dead (rigid
    one-point moments). Same conclusion as the brief's own density barrier.
  - #1066: park. The only identified next step is in the degree-5-dense regime and would reproduce
    the discharging programme behind the published 8/31 and the unrefereed 7/27, 6/23 claims; before
    any second probe the scout would have to establish what those claims' reducible configurations are
    (G2-type status check), which is a selection prerequisite, not a probe.
- **Round-4 summary (Parts 1 + 2):** six clean-room Astra probes, six OPEN/PARTIAL, twelve
  cross-vendor referee reports with zero mathematical errors, zero statements toward any target.
  What the probes reliably produce in ≈ 20 minutes: exact reformulations of the classical bound,
  explicit stability constants, and sharp negative results about the relaxation a seed lives in.
  What they do not produce: the Euclidean / correlation / realizability input that each target
  needs. Selection lesson for the next pass: the round-4 seeds named the lossy step correctly but
  offered no machinery for it; a target should enter the probe list only with a candidate lemma
  that the relaxation obstructions found here do not already refute.
- No referee repairs are applied to the attacker files; this section is the status of record.
  All four probes and all eight referee reports are committed as research record. No Zenodo, no X,
  no site claim, no e-mail.

## Cost (Part 2; from `data/run-logs/<company>/<agent>/<run>.ndjson`, the company heartbeat-runs route is blocked for the run-scoped bridge)

| Run | Agent / model | Wall (UTC) | Input (cached / cache-read) | Output | List cost |
| --- | --- | --- | --- | --- | --- |
| 612c37da, 907643d9 (AUT-22/24 first attempts) | attacker-1, gpt-6-astra | 06:55→07:16 | not recorded | — | — |
| 04d74e44, 7fe3f79c (AUT-23/25 first attempts) | attacker-2, gpt-6-astra | 06:55→07:16 | not recorded | — | — |
| d4e5559c (AUT-22, #1082) | attacker-1, gpt-6-astra | 14:17→14:36 | 741,542 (678,656 cached) | 34,762 (19,530 reasoning) | subscription-included |
| e1b50ec1 (AUT-24, #241) | attacker-1, gpt-6-astra | 14:17→14:32 | 628,982 (574,208 cached) | 30,218 (14,727 reasoning) | subscription-included |
| cde5f86c (AUT-23, #86) | attacker-2, gpt-6-astra | 14:17→14:35 | 944,058 (878,848 cached) | 37,474 (18,190 reasoning) | subscription-included |
| 04766583 (AUT-25, #1066) | attacker-2, gpt-6-astra | 14:17→14:30 | 615,984 (557,056 cached) | 24,768 (13,836 reasoning) | subscription-included |
| 78b164db (AUT-38, #1082) | referee-1, claude-fable-5-1 | 14:41→14:49 | 420 + 911,122 cache-read + 96,484 cache-write | 40,370 | USD 4.18 |
| b8b05c8b (AUT-40, #86) | referee-1, claude-fable-5-1 | 14:41→14:50 | 388 + 698,912 cache-read + 92,039 cache-write | 40,480 | USD 4.04 |
| 6a688ad6 (AUT-42, #241) | referee-1, claude-fable-5-1 | 14:41→15:02 | 390 + 1,078,443 cache-read + 109,501 cache-write | 52,680 | USD 5.10 |
| bf8dab9e (AUT-44, #1066) | referee-1, claude-fable-5-1 | 14:41→14:47 | 260 + 562,002 cache-read + 80,527 cache-write | 30,554 | USD 3.28 |
| 20931954 (AUT-39, #1082) | referee-2, claude-opus-5-5 | 14:41→14:49 | 32 + 1,013,634 cache-read + 85,360 cache-write | 55,251 | USD 1.99 |
| cdfd4aae (AUT-41, #86) | referee-2, claude-opus-5-5 | 14:41→14:50 | 36 + 1,232,742 cache-read + 107,957 cache-write | 57,221 | USD 2.25 |
| 3bbbab26 (AUT-43, #241) | referee-2, claude-opus-5-5 | 14:41→14:50 | 38 + 1,338,224 cache-read + 111,252 cache-write | 59,714 | USD 2.35 |
| 1e0e37d6 (AUT-45, #1066) | referee-2, claude-opus-5-5 | 14:41→14:48 | 32 + 991,426 cache-read + 93,493 cache-write | 44,573 | USD 1.84 |
| c2c1fa62 (AUT-21 step 1) | coordinator, claude-fable-5-1 | 06:53→06:55 | 386 + 575,103 cache-read + 53,116 cache-write | 13,315 | USD 1.88 |
| fb1a9ae8 (AUT-21 step 2) | coordinator, claude-fable-5-1 | 14:36→14:42 | 866 + 2,038,504 cache-read + 96,825 cache-write | 25,456 | USD 3.73 |
| 7d8c4526 (AUT-21 step 3) | coordinator, claude-fable-5-1 | 15:02→ | written before the run closed; read its log for the final figure | — | — |

Chain totals (Part 2): Claude list cost USD 25.03 for the eight referees (referee-1 16.60,
referee-2 8.43) + USD 5.61 coordinator steps 1–2 = USD 30.64 (step 3 and the hourly ticks that
only read AUT-21 excluded); Astra 2,930,566 input (2,688,768 cached) / 127,222 output tokens,
subscription-included, first attempts unmetered. Mathematical compute inside the probes: 0.151,
32.58, 1.327 and 0.058 CPU-seconds (node, one thread); referees 2 s to 3.5 CPU-minutes of python3
each. No solvers, no paid cloud.

Overhead not in the table: the four first attempts (06:55→07:16) died when the Codex container
closed its ssh connection ("Connection to … closed by remote host", workspace restore refused);
their tokens are not recorded. The retries started 14:17 and carried the first attempts' partial
comments as "continuation" context, which every attacker re-derived rather than accepted. Working
wall time dispatch→last referee: 06:53→06:55 + 14:17→15:02 ≈ 47 minutes of activity for four probes
and eight cross-vendor reviews; calendar time 8 h 09 min because of the 7-hour container outage.
Referee runs are 2–3× the Part 1 price per report (longer attacker files, 345–776 lines); the
referee-1 (Fable) reports cost about twice the referee-2 (Opus) reports for comparable depth.
