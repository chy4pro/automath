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
