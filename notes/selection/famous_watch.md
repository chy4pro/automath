# FAMOUS-WATCH shelf

Seed of the shelf defined in `SELECTION.md` §"FAMOUS-WATCH shelf" (added 2026-08-24, the
S^6 lesson). Rule: a named/famous ultimate-proposition target that fails ONLY on
P(solvable-this-week) is never DROPPED — it is SHELVED here, with an UNLOCK CONDITION: what
new tool/scaffold/precedent would make it attackable. **Every new case-library entry must be
matched against these unlock conditions** (a new case = a new public scaffold); matches get
RE-SCORE-flagged and go back to the next selection task.

Built 2026-08-24 (bounded research task, ~45 min cap). Sources read in full: `SELECTION.md`,
`notes/fc_catalog.md` (133 formal-conjectures Lean files: OEIS 76 / Arxiv 24 / Paper 23 /
MathOverflow 10), `orchestration/TARGETS.md` (685 lines, six S0/S1 gates run 2026-08-22, zero
GO), `notes/case_intel/cases.md` (August 2026 wave), plus targeted reads of
`orchestration/results/{kaplansky,lonely_runner,agrawal,kourovka2076,erdos_quartet}_s0s1.md`,
`orchestration/results/agrawal_A1_probe.md`, `orchestration/results/gate_batch_2.md`,
`orchestration/results/field_sweep_batch1.md`, `notes/selection/selection_0824.md`.

**Do not treat any openness/status claim below as re-verified now.** Structured openness
checks (arXiv API, gh, OEIS, Kourovka Notebook direct read) are the *next* selection task's
job. Rows marked UNVERIFIED are exactly that — carried from a source document, not re-checked
this task.

18 rows below. **RE-SCORE-flagged: none outright** (the one candidate — S^6 — is
CONDITIONAL, see row 1). Two genuinely new UNLOCK-relevant scaffolds surfaced this task and are
flagged inline: the CDC construction (row 14) and the Jacobian n≥3 collision technique (row 13).

---

## 1. S^6 complex structure (the Hopf problem) — CONDITIONAL, do not treat as closed or open

**Target.** Does the 6-sphere S^6 admit the structure of a complex manifold? Catalogued
`notes/fc_catalog.md` `Mathoverflow/1973.lean` (MathOverflow question 1973, asked by user
Fetchinson0234, essentially the classical Hopf/Calabi-Eckmann-era problem, open since the
1950s-60s literature on almost-complex structures on spheres).

**Fame.** ★★★★★ — one of the oldest and most cited "named" open problems in differential
geometry/topology; appears on essentially every list of famous open problems in the field.

**Ultimate proposition.** Direction 1 (existence): exhibit an explicit complex atlas /
integrable almost-complex structure on S^6. Direction 2 (non-existence, the historically
favored belief pre-2026): prove no such structure exists. Both directions are "live" per our
docs — see below.

**Why it sank / current status.** It was never scored or gated in our pool at all — it sat in
`fc_catalog.md` untouched (the exact "S^6 lesson" `SELECTION.md` names). As of this task it is
**not open by fiat**: `notes/case_intel/cases.md` (2026-08-23 entry) records a first-party
claim by Levent Alpöge (Anthropic-affiliated mathematician) + Claude — construction via the
Δ(3,4,∞) modular family of 2-tori with Kodaira logarithmic transforms at three special points,
verified by the claimants via finite matrix computations (π₁ vanishing + homology). **Status
per cases.md: "first-party-VERIFIED claim, one day old, no arXiv, NOT YET
INDEPENDENTLY/PEER VERIFIED — do not cite as established."** Primary source:
https://alpo.ge/s6.pdf (self-hosted, no arXiv, invisible to the arXiv watch). S^6 has a
graveyard of failed claims (Etesi and others), so verification discipline scales with fame.

**UNLOCK CONDITION (conditional, not a standard re-score).** This row does not need a new
scaffold to become attackable — it already has one (the modular-family + log-transform
construction, first-party verified). **The trigger is the opposite: if the Alpöge/Claude claim
is independently refuted or withdrawn, S^6 reopens instantly and should be RE-SCORE'd
immediately** — we would then hold a fresh, already-documented construction blueprint (finite
matrix pi_1/homology certificate methodology) even if the specific claimed structure fails,
which is itself a transferable scaffold for the next attempt. Watch: independent verification
of alpo.ge/s6.pdf, or an arXiv posting, or a refutation.

**Crowding note.** Alpöge is the same operator as the Jacobian n≥3 counterexample (07-2026)
and the named human verifier on Claude's RH zero-density result (arXiv:2608.13637); same
X/self-hosted-PDF announcement pattern each time — a fast, low-visibility operator to watch on
adjacent geometry/topology targets. Brendle+Hung (arXiv:2608.19068, the *curvature* Hopf
conjecture on S^2×S^2, a **different** problem) closed days apart from Alpöge's parallel
attempt on the same paper's neighborhood — illustrates the "race clock" SELECTION.md now
tracks.

---

## 2. Kaplansky's zero-divisor conjecture — DROP

**Target.** For a torsion-free group G and a field K, does the group ring K[G] have no
zero-divisors? Catalogued `FormalConjectures/Wikipedia/Kaplansky.lean`
(`zero_divisor_conjecture`).

**Fame.** ★★★★★ — one of three "Kaplansky conjectures" on group rings (with the unit and
idempotent conjectures), textbook-standard in ring theory / geometric group theory.

**Ultimate proposition.** Prove K[G] is a domain for every torsion-free G (direction: theorem),
or exhibit an explicit torsion-free G, field K, and nonzero a,b ∈ K[G] with ab=0 (direction:
finite counterexample — Kind-1 shape once G is fixed).

**Why it sank.** `orchestration/TARGETS.md` (S0/S1 GATE, `orchestration/results/kaplansky_s0s1.md`,
2026-08-22): score 188→37.5. Confirmed open (FC HEAD still `sorry`+`research open`), zero
structural competition. **Killed by a mathematical no-go, not difficulty**: the only known
attack playbook (Gardam 2021's small-support search that refuted the *unit* conjecture for a
virtually-abelian group) cannot transfer — Farkas–Snider (1976, char 0) + Cliff (1980, any
char) already prove torsion-free polycyclic-by-finite groups (which is what "virtually
abelian" gives you) yield K[G] a domain, so that search domain is provably empty for the
zero-divisor question. The group-agnostic version of the playbook was independently run and
closed by others: Garg–Mineyev (arXiv:2501.07646) all-negative for small support, Shin
(arXiv:2607.01716, 2026-07-02) proves the obstruction is structural, not a bounded-search
artifact. Remaining computational neighborhood (Tabei, Dietrich–Lee–Nies–Vinyals) is
SAT/DRAT-based, which this project's PROTOCOL bans locally.

**UNLOCK CONDITION.** A construction route for a torsion-free group **outside the
polycyclic-by-finite / virtually-abelian family** (where Farkas–Snider–Cliff does not apply),
paired with a finite zero-divisor witness — i.e., a genuinely new family, not a bigger search
over the same closed family. Also: any development that lifts the local SAT/DRAT ban would
reopen the Tabei/Dietrich-Lee-Nies-Vinyals computational neighborhood. Watch for any new
"Gardam-style" counterexample paper that explicitly targets non-polycyclic-by-finite
torsion-free groups.

**Crowding note.** A MathOverflow lead (513707, 2026-07-29, user Maximka123, "Checking one
group for torsion") was chased down this round: Henrik Rüping's answer shows the proposed
group's putative zero-divisors are just torsion-forced and trivial; Henry Wilton judged the
non-triviality claim unproven. Net: a live community thread exists but currently reads
negative, not a scoop risk today.

---

## 3. Lonely Runner Conjecture (direct attack) — DROP

**Target.** For n runners on a unit circle with distinct constant speeds, is there always a
time when all runners are at distance ≥ 1/n from the starting point? Equivalently, for n-1
nonzero distinct integer/real speeds, is max-gap(view of the origin) ≥ 1/n always achievable?
60-year-old (Wills 1967 / Cusick).

**Fame.** ★★★★★ — one of the most publicly recognized open problems in combinatorics/number
theory (Quanta Magazine coverage 2026-03-06), subject of a dedicated 4-day international
workshop at Universität Rostock, 06.10.–09.10.2026.

**Ultimate proposition.** Prove the gap bound 1/(k+1) holds for all k speeds (all n), or
exhibit an explicit finite speed tuple violating it for some n (finite, exactly-computable
rational-arithmetic certificate — this is the healthiest verification axis of any candidate
audited this round).

**Why it sank.** `orchestration/TARGETS.md` S0/S1 GATE r5 (`orchestration/results/lonely_runner_s0s1.md`,
2026-08-22): 90→27.0, "the largest overestimate in six gate rounds." Confirmed open at
n=13+ (all n≤12 already fully proven in the literature; a 2026-08-18 intel note had missed
arXiv:2604.23906 "Eleven, twelve, and thirteen lonely runners," so the real frontier is n=13,
**not** n=10 as an earlier informal note — and as this task's own instructions — assumed;
n≤12 has been closed for years). Killed by three axes together: (1) solvability — the
smallest open case n=13 has a certificate space of ~10^295.8 tuples, and FC's statement is a
pure ∀ `sorry` that cannot hold a counterexample without a hand-written `counter_` lemma; (2)
crowding — five arXiv papers in five months (latest 3 days before the gate), three
independent schools, the Rostock workshop; (3) a mis-scored "weakening" signal: two proposed
strengthenings (Kravitz's Loneliness Spectrum Conjecture, the Shifted LRC) were recently
disproven, which the pool had read as "the base conjecture might be shaky too" — recomputed
exactly this round (14,161 primitive 4-tuples, exact rational arithmetic): every one of those
disproof witnesses actually **satisfies** the base Lonely Runner bound, because both
disproofs land in the parameter region where LRC is already a proven theorem. The signal
pointed the wrong way.

**UNLOCK CONDITION.** A structured (non-exhaustive) reduction of the n=13 witness space — the
paper landscape currently has none; the field is actively working the problem by hand/computer
search, so watch specifically for a *polynomial-size* parameterization of candidate speed
tuples (the kind of reduction that flipped `orchestration/results/gate_batch_2.md`'s judgment
on an unrelated circulant-graph target from CUT to revivable). Absent that, this stays shelved
regardless of how many more n=13-15 papers appear, because the certificate-space growth
outpaces any plausible near-term algorithmic reduction.

**Crowding note.** Active, dense, and organized (named workshop, multiple competing schools,
5 papers/5 months as of the gate). This is the opposite of an empty-seat target; re-score only
if a paper introduces a genuinely new reduction technique, not merely a new n.

---

## 4. Agrawal's Conjecture (AKS primality-test conjecture, disproof route) — DROP

**Target.** From the 2002 AKS primality-test paper: is it true that for prime r not dividing
n, if (X-1)^n ≡ X^n − 1 (mod n, X^r − 1) and n has no prime factor ≤ r, then n is prime or
n² ≡ 1 (mod r)? (If true, it would let AKS drop its slow √r·log n loop.) Catalogued
`FormalConjectures/Wikipedia/Agrawal.lean`.

**Fame.** ★★★ — well known within computational number theory / primality-testing circles
(downstream of the celebrated, Gödel-Prize-adjacent AKS paper), not broadly famous outside it.

**Ultimate proposition.** The disproof direction only (Lenstra–Pomerance heuristics make the
truth direction implausible): exhibit a specific composite n and prime r satisfying the
hypotheses but violating the conclusion — a finite, exactly-checkable arithmetic certificate.

**Why it sank.** `orchestration/TARGETS.md` ran this through **two** gates.
S0/S1 GATE r3 (`orchestration/results/agrawal_s0s1.md`, 08-22): 197→81 (HOLD) — confirmed
open, zero competition, and the certificate genuinely is tiny (a handful of integers), but the
one known route to *generating* a witness (Lenstra 2003, extended by Popovych 2009 and
Hegde–Devaraj 2021) requires n to be **simultaneously a Carmichael number and a
Lucas–Carmichael number** — and whether any integer is both is itself an unsolved question
with zero known instances in the literature. The HOLD condition was probe A-1 (quantify the
double-smooth-prime pool against the counting inequality needed). **Probe A-1 then ran**
(`orchestration/results/agrawal_A1_probe.md`, per `notes/selection/selection_0824.md`):
"FAIL decisively at 1e8; 102/102 cells fail; X=1e9 excluded by ceiling arithmetic (needs
×13.65 growth vs π(X) growth ×8.67); Hegde-Devaraj kernel NOT bypassed." **Verdict: DROP, not
back to pool head — Agrawal is DEAD** as of this task's evidence trail.

**UNLOCK CONDITION.** Either (a) a new witness-generation route that does **not** require the
Carmichael-∧-Lucas-Carmichael double condition (the entire known literature — Lenstra,
Popovych, Hegde–Devaraj — keeps this kernel), or (b) an independent existence proof/witness
that some integer is both Carmichael and Lucas–Carmichael (which would itself be new and
possibly independently interesting), or (c) the counting-inequality ceiling that killed probe
A-1 loosens with a better analytic bound on the double-smooth-prime pool size (the probe's own
report has the exact inequality — re-run at a materially larger X only if someone publishes a
better bound, not by brute-force rescan).

**Crowding note.** Zero — Primaboinca (BOINC project) ran 2010→2020-05-31 across
10^10<n<10^17 with zero counterexamples and shut down; Hegde–Devaraj 2021 has zero citations.
This is a genuinely idle, structurally-blocked target, not a crowded one.

---

## 5. Kourovka 20.76 (Pyber's p-group abelian-subgroup bound) — HOLD

**Target.** For a finite p-group G, if every *normal* abelian subgroup has order ≤ p^k, does
every abelian subgroup (not necessarily normal) have order ≤ p^(2k)? Posed by
Halasi–Podoski–Pyber–Szabó (arXiv:2305.02037 / J. Algebra 2024) as an unanswered question in
their own SOTA paper; entered the Kourovka Notebook as problem 20.76.

**Fame.** ★★½ — specialist (finite group theory), but genuinely named (Pyber) and tracked in
the internationally-referenced Kourovka Notebook, with a documented history of open-problem
resolutions being harvested by AI systems (Aristotle solved 8 other Kourovka problems in the
same period).

**Ultimate proposition.** Prove the p^(2k) bound (theorem), or construct an explicit p-group
with a normal-abelian bound k but a non-normal abelian subgroup exceeding p^(2k) (finite
witness, Kind-1 shape).

**Why it sank.** `orchestration/results/kourovka2076_s0s1.md` (S0/S1 GATE r2, 08-22): 158→72,
"pool-bottom." Confirmed open with the strongest evidence of any candidate this project has
audited (direct read of the Kourovka Notebook v45 e-print source, no `\zv` answer star, no
italic-name credit — the editors themselves still list it open as of 2026-07-03). Killed on
solvability + verification: known counterexamples to the *related* claim (Alperin/Glauberman,
p≥5, exponent-p support) exist, but two published theorems (Gillam 1970, metabelian case;
Glauberman 2004, class ≤ p−1) force any 20.76 counterexample into a narrow structural corner
("non-metabelian ∧ class ≥ p"), and every easily-enumerable family is excluded by that corner.
The YES-direction proof would need to compress an O(k²) bound to 2k — described in the gate
file as "a 60-year-old frontier." A separate, twin problem (20.75, same authors, rank version,
**not yet formalized in FC**) is related but not equivalent — an exponent-p counterexample
would kill both simultaneously.

**UNLOCK CONDITION.** Either (a) an explicit construction technique for non-metabelian,
class-≥-p p-groups with controllable abelian-subgroup structure (currently absent from the
literature per the gate's search), or (b) a compression technique for the O(k²)→2k bound on
the proof side — watch specifically for any paper citing Gillam 1970 or Glauberman
*Contemp. Math.* 524 (2010) with new structural results (the gate file flags Glauberman's full
text as never retrieved — `~gg/limits.pdf` failed to extract; this is a concrete,
cheap follow-up for whoever re-scores this row).

**PROBE RESULT (2026-08-24, Qwen3.8-Max ~1h, engine/harvest/qwen_probe_k2076_r1.md).**
Difficulty CONFIRMED at gate level: strong free engine produced correct standard machinery
(self-centralizing lemma, minimal-counterexample frame |A/B|>|N/B|) plus a correct collapse
argument for the natural constructions (any p-subgroup of Sp fixes a Lagrangian — Lagrangian
count coprime to p — so extraspecial⋊Sp always yields a huge normal abelian subgroup;
1+J algebra groups collapse via square-zero top layers), independently re-deriving the
unlock condition's "controllable non-metabelian class>=p construction" as the only live
corner — but could not build it. Engine leans counterexample-exists (opinion, no weight).
Row stays HOLD; solvability prior unchanged (hard).

**Crowding note.** Zero on the specific problem (Aristotle's 8-problem Kourovka sweep
explicitly skipped 20.75/20.76, taking a different rank-inequality problem, 21.150, instead),
but the Kourovka Notebook as a whole is now an active AI-harvest zone: four arXiv
solution papers in seven weeks (2607.06434, 2607.17477, 2608.00504, 2608.03003) plus an LLM
research-orchestration paper (2607.27705) targeting the notebook generally — the empty seat
may not stay empty.

---

## 6. Erdős #699 (binomial-coefficient gcd, Sylvester–Schur neighborhood) — HOLD

**Target.** erdosproblems.com #699: a gcd statement about binomial coefficients
C(n,i)/C(n,j)-type ratios (see `orchestration/results/erdos_quartet_s0s1.md` for exact form).
Catalogued in FC as `answer(sorry) ↔ ∀…` — the one shape in this batch of four Erdős problems
that a counterexample can be written directly into.

**Fame.** ★★★ — carries inherent Erdős-numbered fame (tracked live on erdosproblems.com),
technical/niche outside number theory.

**Ultimate proposition.** Prove the gcd bound for all valid (i,j,n), or find an explicit
(i,j,n) violating it (finite arithmetic certificate, zero environmental assumptions — the
strongest verification axis of the four Erdős rows on this shelf).

**Why it sank.** `orchestration/results/erdos_quartet_s0s1.md` §3 (S0/S1 GATE, 08-22):
113→45, "highest of the four" but still a HOLD. The verification axis stayed a clean 5; what
dropped it was (1) near-misses genuinely narrow as i grows — at N≤1000, i≥10 has zero
"differ-by-one-prime" triples — and (2) crowding: erdosproblems.com's own remarks page states
verbatim that GPT-5.6 (prompted by Price) has already proved the sub-cases j≤3i/2 and n=2j,
plus 3 other people actively working it, 2 claimed proofs, 1 in-progress formalization.

**UNLOCK CONDITION.** A structural reason the margin narrows *provably* (not just empirically)
as i grows past 9-10 — that would either close the remaining cases or sharply bound where a
counterexample could live. Given the room is already crowded, this only becomes attractive
again if the current claimed-proof attempts stall or are shown incomplete (watch
erdosproblems.com's remarks page and the FC PR that links `Erdos699.sylvester_schur`, which
explicitly does **not** yet claim the open gcd statement).

**Crowding note.** Real and current — GPT-5.6/Price partial proof, 3 people working it, 2
claimed proofs, 1 formalization in progress, per the erdosproblems.com page itself.

---

## 7. Erdős #982 (convex-position distinct distances) — HOLD

**Target.** erdosproblems.com #982: a distinct-distances bound for points in convex position
(non-cocircular), tied to the classical 1946 Erdős distinct-distances program (NPPZ 2013
lower bound (13/36 + 1/22701)n − O(1)).

**Fame.** ★★★ — Erdős-numbered, sits in the historically famous distinct-distances family
(the general distinct-distances problem itself was resolved by Guth–Katz 2015; this convex
variant is a separate, still-open strengthening).

**Ultimate proposition.** Prove the ⌊n/2⌋-type distance bound for all convex, non-cocircular
point sets, or exhibit an explicit convex configuration violating it.

**Why it sank.** `orchestration/results/erdos_quartet_s0s1.md` §5 (08-22): 113→31.5. The
witness space is empty for 80 years by construction: any candidate must be convex ∧
non-cocircular ∧ have every one of its distinct-distance-achieving pairs below the ⌊n/2⌋
threshold, and every known optimal-bound construction (Erdős 1946 → ErFi 1994 → Dumitrescu
2006 → NPPZ 2013) achieves the bound exactly rather than approaching a counterexample — 80
years of progress has narrowed the *lower bound* only, never produced a near-miss on the
upper/counterexample side. A companion FC PR (#4694, open, unmerged) closes the entire
cocyclic sub-case to zero without touching the main statement — a real result, but it shrinks
rather than opens the search space.

**UNLOCK CONDITION.** A witness-family template genuinely different in kind from the
Erdős-1946-style optimal constructions — something that approaches (rather than achieves) the
bound from the wrong side. No such template exists in the literature per this gate's search
(`arXiv abs:"convex position" AND abs:"distinct distances"` → 1 hit, the 2012 NPPZ paper
itself). Watch for any new convex-point-configuration paper outside the extremal-bound
tradition.

**PROBE RESULT (2026-08-24, Qwen3.8-Max ~1h, engine/harvest/qwen_probe_982_r1.md, grade L2).**
Difficulty CONFIRMED at gate level. Delivered correct elementary structure — every vertex of a
counterexample must centre a circle through >=3 others; cocircular sets satisfy (S); minimal
counterexamples are even; isosceles-apex counts forced well above the regular polygon's; an
obtuse-middle lemma (a size->=3 distance class forces obtuse interior angles at its non-extreme
points) — plus an EXPLICIT non-cocircular sharp hexagon (Reuleaux-arc midpoints on a unit
equilateral triangle) that I verified EXACTLY in Q(sqrt3): 15/15 distance-table entries,
f = (2,3,2,3,2,3), strictly convex, non-cocircular. It MEETS the bound, is not a counterexample.
**Datum worth keeping: 3 of its 6 vertices sit strictly below the bound while the regular
hexagon has all six exactly at it** — you can push half down; the model's own analysis says the
collisions the two vertex classes need are mutually incompatible (shown explicitly for the
alternating-radius family, where they require opposite perturbation signs). Nothing approached
the analytic frontier (NPPZ). Row stays HOLD; prior unchanged. Re-shot queued as gacha T4 with
a pure-construction prompt variation.
**ESCALATION RESULT (2026-08-24 06:5x, GPT-5.6 Sol+Pro 28m, engine/harvest/
gacha_982_pro_escalation.md, grade L3 pending lit-check).** The Pro pull, seeded with the
verified Qwen scaffold, produced the **diameter-disk theorem** (all vertices in the disk
with diameter ab => strict distance monotonicity along both a-b chains => f(a), f(b) >=
ceil(n/2)) and with it a COMPLETE PROOF OF (S) FOR CENTRALLY SYMMETRIC convex 2m-gons
(farthest antipodal pair v,-v always satisfies the disk condition). Proof hand-checked;
its sharp non-symmetric hexagon verified exactly. Also proved: any counterexample must
evade EVERY pair's diameter disk (each chord seen at <90deg by some third vertex) and its
min enclosing circle must be acute-three-point supported; and it refuted the naive
obtuse-budget lever (at most 4 NON-obtuse vertices — the supply bound points the other
way). ROW STATUS: solvability prior UP for subclass results; full (S) still open.
NOVELTY UNKNOWN — lit-check required before any outward claim. This is the first gacha
escalation to produce a consolidation-worthy artifact (combine with P1's five lemmas).

**Crowding note.** Light — one active contributor (PR #4694) working a restricted variant, not
the main statement.

---

## 8. Erdős #617 (Erdős–Gyárfás balanced colouring) — DROP

**Target.** erdosproblems.com #617: existence of an r-colouring of K_n's edges avoiding
monochromatic "balanced" structures of a specified type, parameterized by r (see gate file for
exact form).

**Fame.** ★★★ — Erdős–Gyárfás-named, moderately well-known in extremal graph theory.

**Ultimate proposition.** Determine, for each r, whether the desired colouring exists (r=3,4
already published theorems; the question is the smallest still-open r).

**Why it sank.** `orchestration/TARGETS.md` §"GATE r4" (08-22): 113→12. r=5 was
**machine-verified-resolved** by a third party (`RamazanKara/erdos-617-r5-formal-verification`,
Zenodo DOI 10.5281/zenodo.21535385, Lean, no `sorryAx`, mathematical source = Robert
Sneiderman's preprint) — an r=5 fact our pool had missed. That pushes the smallest open case to
r=6: K_37, 666 edges, 6^666 colourings, C(37,7)≈10.3 million constraints — a search space that
hits this project's local PROTOCOL ban on SAT/exhaustive search directly.

**UNLOCK CONDITION.** A structural (non-exhaustive) argument for r=6 — the r=3/4/5 proofs are
presumably each ad hoc to their r; watch for a general-r technique, or for the local
SAT/exhaustive-search ban to be lifted for a bounded, justified case (both would need to be
argued explicitly, per this shelf's own rule against silently escalating solver budget).

**Crowding note.** Real: 7 people actively working the problem, 7 claimed proofs listed on
erdosproblems.com as of the gate.

---

## 9. Erdős #779 (Deaconescu: primorial-plus-p) — DROP

**Target.** erdosproblems.com #779 (Deaconescu's conjecture): a compositeness claim about
P+p for primes p in the interval defined by consecutive primorials P (exact form in gate
file). Note: distinct from Fortune's conjecture (`Wikipedia/FortuneConjecture.lean`, OEIS
A005235) — the pool's first pass conflated the two before the gate corrected it.

**Fame.** ★★½ — the lower-fame end of this shelf; a specific Erdős-catalogued number-theory
question, not broadly known.

**Ultimate proposition.** The disproof direction: exhibit a prime p in the target interval
such that P+p is composite for a prime P+p should be prime for (per Deaconescu's claim,
verified computationally through n=1000).

**Why it sank.** `orchestration/TARGETS.md` §"GATE r4" §4 (08-22): 113→2.8, the pool's lowest
score. The verification axis is the killer, quantified: the first open instance (n=1001) needs
a compositeness certificate over an interval containing roughly 10^3392.8 primes, each a
3397-digit number — a certificate count essentially uncheckable by any means this project has.
Fortune's conjecture (a strictly stronger, still-unrefuted statement) logically implies this
one, so refuting #779 is *harder* than refuting Fortune, and Fortune itself has never been
refuted.

**UNLOCK CONDITION.** A finite-certificate reformulation that does not require exhausting an
astronomical prime interval — e.g., a number-theoretic argument narrowing where a
counterexample could live to a small, checkable set, or (much more likely to arrive first) a
disproof of the strictly-stronger Fortune's conjecture, which would immediately reopen this
row via implication.

**Crowding note.** Effectively zero (`arXiv all:"Deaconescu" AND all:"prime"` → 3 hits, all
different, same-named conjectures; 0 open FC PRs, 0 claimed proofs) — genuinely idle, just
computationally unreachable, not contested.

---

## 10. Zariski Cancellation Problem — CUT (never entered TARGETS.md pool)

**Target.** Is every polynomial ring k[X][x1,...,xn] over a field k of characteristic 0
*cancellative* — i.e., if A[t] ≅ k[x1,...,xn+1] does A ≅ k[x1,...,xn]? Catalogued
`FormalConjectures/Arxiv/2208.14736/ZariskiCancellation.lean` (Neena Gupta survey). Known TRUE
for n≤2 (classical); Gupta's own famous work shows it is **false in positive characteristic**
for n≥3, but the char-0, n≥3 case is the long-standing open question.

**Fame.** ★★★★ — a well-known problem in affine algebraic geometry; Gupta's positive-
characteristic counterexamples earned her an invited ICM 2018 talk, keeping the char-0 case
visible in the field.

**Ultimate proposition.** Prove cancellativity holds for all n in char 0 (theorem), or exhibit
two non-isomorphic affine varieties A, A' with A[t] ≅ A'[t] in char 0 (counterexample).

**Why it sank.** Never reached `orchestration/TARGETS.md` at all — this is a second instance
of the exact S^6 pattern: surfaced by `orchestration/results/field_sweep_batch1.md` §3
(certkind "1–mixed", verifroute (b) self-written verifier), then independently evaluated and
CUT in `orchestration/results/gate_batch_2.md` line 52 (candidate "E29"): *"witness = two
varieties plus a non-isomorphism proof — no finite certificate... Kind 2 or blocked."* I.e.
even a constructed candidate pair of varieties requires proving non-isomorphism, which is
itself an open-ended ∀-type task, not a finite check — the certkind doctrine
(`notes/case_intel/recalibration_ytd.md`) downgrades this from the Kind-1 construction class
our apparatus is currently good at.

**UNLOCK CONDITION.** A **finite, mechanically-checkable non-isomorphism invariant** for
candidate affine-variety pairs (e.g., a discrete/computable invariant that distinguishes A
from A' without an open-ended proof) — this is exactly the kind of "Kind-1-ification" the
cscK-YTD disproof (`case_ytd_2608.19301.md`) achieved for a different problem class. Watch
specifically for any paper proposing a computable obstruction to A[t]≅A'[t]≅k[x1,...,xn+1].

**Crowding note.** Not measured this task — the field-sweep note (`field_sweep_r2.md`)
independently re-confirms it exists in FC and flags it math.AC-adjacent, but no competitor
search was run. Treat as UNMEASURED, not zero.

---

## 11. Casas-Alvero Conjecture — dormant in catalog, claimed-proof pending, never gated

**STATUS CHECK (2026-08-24, gacha T5 pre-check)**: the claimed proof arXiv:2501.09272
is CONTESTED — submitted 2025-01, revised through 2026-03-21 with comment "Major revisions",
0 citations, no journal record. Neither accepted nor collapsed after 14 months. Row parked
as CONTESTED-CLAIM WATCH: no gacha shots (target may be dead), no strike (claim unaccepted).
Re-check on new arXiv version or quarterly.

**Target.** In characteristic 0, if a monic univariate polynomial P of degree d shares a
non-trivial common factor with each of its Hasse derivatives up to order d−1, must
P = (X−α)^d for some α? Catalogued `Paper/CasasAlvero.lean`. Proven for d≤8, d=p^k, and
d=2p^k (p prime); known FALSE in positive characteristic p for degree p+1.

**Fame.** ★★★ — well known in commutative algebra / singularity theory; has generated a
sustained line of partial-case papers over two decades.

**Ultimate proposition.** Prove the conjecture for all degrees in char 0, or exhibit a
counterexample degree/polynomial.

**Why it sank.** It never sank in our pipeline — it simply sat uncatalogued-into-the-pool,
exactly the S^6 failure mode. **Flag, do not treat as open**: `notes/fc_catalog.md` itself
records *"The conjecture is now claimed to be proven in this paper: [Proof of the
Casas-Alvero conjecture: Soham Ghosh] arXiv:2501.09272."* **UNVERIFIED this task** — no
independent check was run on that claim's reception or correctness (predates this project;
January 2025). If the Ghosh proof stands, this row is closed and should be struck, not
re-scored.

**UNLOCK CONDITION.** First: verify whether arXiv:2501.09272 stands (a cheap arXiv/community-
reception check — the kind of "quick openness sanity check" this task's rules permit but that
this task did not spend budget on). If the claim has collapsed or remains genuinely
unconfirmed after 19 months, this becomes a live named-conjecture candidate with a large
partial-cases literature to build on (fixed low degree, prime-power degree already closed) —
the natural next attack surface would be the smallest unproven degree class.

**Crowding note.** UNMEASURED — no competitor search run this task; the existence of a 2025
claimed full proof is itself the dominant crowding signal and must be resolved before any
re-score.

---

## 12. Circulant Hadamard Conjecture (Ryser) — dormant in catalog, never gated

**Target.** No circulant Hadamard matrix has order greater than 4 (order n=4 example: exists;
Ryser 1963 conjectured n≤4 is the ceiling). Catalogued
`FormalConjectures/Arxiv/2402.13202/CirculantHadamard.lean`.

**Fame.** ★★★★ — classical, well-known conjecture in combinatorial design theory; the target
of substantial computational search literature (verified far beyond any plausible small
counterexample, order into the 10^28+ range per the wider literature, though that figure was
not re-verified this task).

**Ultimate proposition.** Prove no circulant Hadamard matrix of order >4 exists, or exhibit
one (a finite matrix — Kind-1 shape, trivially machine-checkable once found).

**Why it sank.** Never gated — found only via this task's fc_catalog mining pass. A companion
signal from `orchestration/results/gate_batch_2.md` §"S1" notes FC's catalogue has 5 hits
under the keyword "circulant" (Hadamard/Williamson/AME states) while evaluating a *different*
paper (signed circulant Ramanujan bound) — that evaluation is not a judgment on this
conjecture itself, just evidence FC's circulant-family catalog exists and is small.

**UNLOCK CONDITION.** The disproof direction is finitely certifiable in principle but the
search space (all circulant {±1} matrices of a given order) grows exponentially and has
already been exhausted by others to a very large bound — an UNLOCK here looks like a
*structural* reduction of the search (a number-theoretic necessary condition narrowing
candidate orders sharply below current computational limits), not more brute search. Watch for
exactly that shape of paper.

**Crowding note.** UNMEASURED this task — this is a classical problem with an active
computational-search literature; assume non-trivial crowding until checked.

---

## 13. Jacobian Conjecture — n=2 (planar case) — adjacent to an August disproof, still open

**Target.** For a polynomial map F: C^n → C^n with everywhere-nonzero constant Jacobian
determinant, is F necessarily invertible with polynomial inverse? Case n=1 trivial. Case
n=2 (the classical, most-cited form) is what remains open. Case n≥3 was **disproved** in
2026-07-20~21 by Claude Fable 5 + Alpöge (explicit degree-7 map on ℂ³, Tao-verified,
`notes/case_intel/cases.md` line 27).

**Fame.** ★★★★★ — one of the most famous open problems in algebraic geometry, on Smale's list
of mathematical problems for the 21st century.

**Ultimate proposition.** Prove every such F on ℂ² is a polynomial automorphism (the belief,
per cases.md: "仍开放且信真" — still open and believed true), or exhibit a planar
counterexample (which would be a far larger shock than the n≥3 result, given the field's
strong belief in the n=2 case).

**Why it sank.** Not evaluated by our gates at all — this is a case-intel-sourced adjacency,
not a pool candidate. Included here per this task's explicit brief (n=2 is the natural next
question after the n≥3 disproof) rather than any internal DROP/HOLD record.

**UNLOCK CONDITION.** The n≥3 disproof's construction technique (collision-generated
compression in an explicit polynomial family, per `notes/case_intel/cases.md`'s downstream
note on the Zhao Vanishing Conjecture counterexample which reused the same "collision
subalgebra" trick) is a genuine new public scaffold for this *class* of problem — but it built
a counterexample, and the n=2 case is believed TRUE, so the transfer is not direct: the n=2
attack surface is a proof, not a construction. **RE-SCORE trigger, narrowly stated:** if any
paper uses Jacobian-collision-style techniques to either (a) find a genuine planar
counterexample (which would be sensational and immediately attackable/verifiable), or (b) adapt
the technique into a proof strategy for n=2 (e.g., by showing the collision family cannot exist
in 2 variables — a negative/structural result), re-open and re-score this row.

**Crowding note.** Alpöge/Anthropic cluster is the dominant near-term risk on anything in this
neighborhood (same operator pattern as S^6, row 1, and the RH result). No independent n=2
attempt identified this task — UNMEASURED beyond that.

---

## 14. Cycle Double Cover — 5-cycle-strengthened version — adjacent to a substantiated result

**Target.** The base Cycle Double Cover (CDC) conjecture (every bridgeless graph has a
collection of cycles covering each edge exactly twice) was **substantiated, not collapsed**,
in the August wave: `notes/case_intel/cases.md` (2607.16356, GPT-5.6 Sol Ultra, 64 subagents,
08-18 status update) — public Lean 4 formalization exists, independent human-expert
expositions by Jim Geelen and Sang-il Oum, mathematical correctness "substantively confirmed by
expert review," though formal journal review is not complete. cases.md explicitly flags: **"图
论头号开放目标应看 5-cycle 强化版而非退回 CDC 本身"** — the strengthened 5-cycle version, not
the base conjecture, is the real remaining target.

**Fame.** ★★★★ — CDC is one of the best-known open problems in graph theory; a strengthened
version inherits significant fame while being a genuinely distinct, still-open statement.

**Ultimate proposition.** UNVERIFIED — this task located only the one-line cases.md pointer
("5-cycle double cover 强化版仍开放"), not the exact mathematical statement of the
strengthening. **Do not attack from this row alone**; the next selection task must first
retrieve the precise statement (likely from the same 2607.16356 paper's related-work/future-
directions section, or Sang-il Oum's exposition) before scoring.

**Why it sank.** Never scored by our pool — pure case-intel adjacency, flagged explicitly by
the case file itself as the natural next target once the base conjecture stopped being a
scoop opportunity.

**UNLOCK CONDITION.** This row is *already* unlock-eligible in the sense that a public
construction scaffold exists: the base-CDC construction method (8-cycle double cover via
nowhere-zero-flow transformation in a 3-dimensional GF(2) vector space, per cases.md) is a
directly relevant precedent for a strengthened version of the same object. **Action item for
the next selection task, not a wait-for-trigger: pull 2607.16356's own statement of what
remains open (the 5-cycle version) and score it against the base construction's transferable
machinery.**

**Crowding note.** High-attention neighborhood — this was a headline August result; assume
competitive interest in its natural strengthenings even without direct evidence.

---

## 15. Kalai's Conjecture 6(a) — adjacent to a disproven sibling, still open

**Target.** UNVERIFIED, precise statement not located this task. Context per
`notes/case_intel/cases.md` (2026-04-03 entry): Kahn–Kalai "Conjecture 7" (a strengthening
related to the Kahn–Kalai expectation-threshold theorem, itself a landmark 2022 Park–Pham
result) was **disproven** by GPT-5.5 Pro + Diskin/Kreitner (first AI+Polymath collaboration,
Lean-verified counterexample, Kalai's own blog as source). The same source line states
verbatim: **"6(a) 仍开放且 Kalai 点名"** — Conjecture 6(a), a different item in Kalai's own
numbered list of related conjectures, remains open and Kalai has flagged it by name.

**Fame.** ★★★½ — Gil Kalai is a leading combinatorialist; his numbered conjectures around the
expectation-threshold circle carry real weight in the field even where individual sub-items
(like 6(a)) are less independently famous than the headline theorem.

**Ultimate proposition.** UNVERIFIED — must be retrieved from Kalai's blog post that names it
before this row is attackable or even fully scoreable.

**Why it sank.** Never entered the pool; pure case-intel adjacency, one line of source
material.

**UNLOCK CONDITION.** Retrieve Kalai's blog post (the source cited for the Conjecture 7
disproof) and extract the exact statement of 6(a). Once retrieved, the disproof
technique that killed Conjecture 7 (Lean-verified explicit counterexample, AI+Polymath
collaborative process) is the directly relevant transferable scaffold — this is a strong
UNLOCK candidate pending only the statement lookup.

**Crowding note.** Real and specific: `orchestration/results/field_sweep_r10.md` (via
KitaKen1's 80-repo scan) found a competitor repo named literally
`kahn-kalai-conjecture-7-counterexample` — i.e. the same competitor ecosystem that is already
active in this exact neighborhood. High risk that 6(a) gets picked up by the same actors next;
do not sit on this row once the statement is retrieved.

---

## 16. Andrews–Curtis Conjecture — explicitly excluded (crowded)

**Target.** Every balanced presentation of the trivial group that is AC-trivial (obtainable
from the trivial presentation via Andrews–Curtis moves: elementary Nielsen transformations plus
conjugation) — conjecturally, is every balanced presentation of the trivial group AC-trivial?
Central to combinatorial/geometric group theory and tested as a potential source of
counterexamples to the smooth 4-dimensional Poincaré conjecture (via Akbulut–Kirby
presentations).

**Fame.** ★★★★★ — extremely well known in geometric group theory and low-dimensional topology;
DeepMind ran a dedicated RL effort (AC-trivialization search) on it in prior years, which is
itself part of why it is crowded.

**Ultimate proposition.** Prove every balanced trivial-group presentation is AC-trivial
(theorem), or exhibit an explicit presentation that resists all AC-moves under a
completeness argument (an inherently hard-to-certify negative — arguably Kind-2-shaped, since
"resists forever" is not a finite check without a separate invariant proof).

**Why it sank.** `orchestration/TARGETS.md` "明确排除" (explicit-exclusion list, line ~440):
listed alongside Collatz, Conway99, etc. as "**最拥挤**" (the most crowded) among a set of
"high-fame, no-fresh-method" items — never individually gated with a score, carried forward
unreviewed since v1.

**UNLOCK CONDITION.** A finite-certificate reformulation of the *non*-AC-trivializability
direction (currently this direction has no known finite witness shape — this is the actual
blocker, not merely search-space size), or a break in the search-technology crowding (DeepMind
and academic groups both actively mining this with RL/search methods) that opens a
distinguishable sub-family we could attack differently.

**Crowding note.** Very high, explicitly named as the most crowded item on the exclusion list;
do not re-score without a concrete reason the crowding has thinned.

---

## 17. Conway's 99-graph problem — PARK-WATCH (SAT conflict + crowded)

**Target.** Does there exist a strongly regular graph with parameters (99,14,1,2) — 99
vertices, each pair of adjacent vertices sharing exactly 1 common neighbor, each pair of
non-adjacent vertices sharing exactly 2? One of John Conway's "$1000 problems."

**Fame.** ★★★★ — well known in algebraic/computational combinatorics; carries a standing
Conway prize, actively pursued by the SAT/graph-search community.

**Ultimate proposition.** Construct the graph explicitly (a finite, directly checkable
adjacency-matrix certificate — clean Kind-1 shape), or prove no such graph exists.

**Why it sank.** `orchestration/TARGETS.md` "明确排除" list: **"Conway99 维持 PARK-WATCH（SAT
密集与本机禁令冲突+建制化竞争）"** — explicitly held at PARK-WATCH status (a lighter shelf
tier than DROP) because the natural attack is SAT-solver-dense search, which conflicts with
this project's local PROTOCOL ban on SAT/exhaustive search, compounded by established,
institutionalized competition (dedicated search groups have run this for years).

**UNLOCK CONDITION.** A non-SAT attack route — e.g., an algebraic/spectral construction
technique that narrows candidate graphs to a small structured family checkable without a SAT
solver — or a PROTOCOL exception explicitly argued and granted for a bounded, justified SAT
budget on this specific target.

**Crowding note.** Institutionalized, long-running competition (explicitly named in the source
line); treat as persistently crowded absent evidence otherwise.

---

## 18. Collatz Conjecture (general 3n+1 problem) — explicitly excluded (no method signal)

**Target.** Starting from any positive integer n, repeatedly apply (n even → n/2; n odd →
3n+1); does the sequence always reach 1? Includes the related, separately-catalogued
`Arxiv/2107.12475/CollatzLike.lean` digit-representation variant in `fc_catalog.md`
("2 ∈ Nat.digits 3 (2^n) for n>8").

**Fame.** ★★★★★ — arguably the single most famous unsolved problem in popular mathematics.

**Ultimate proposition.** Prove every positive integer's Collatz trajectory reaches 1
(theorem), or exhibit a divergent trajectory or a cycle other than {1,2,4} (a finite,
directly-checkable witness if found — Kind-1 shape — though "divergent" is not finitely
certifiable, only "cycle found" is).

**Why it sank.** `orchestration/TARGETS.md` "明确排除" list groups Collatz (via the numbered
`#1135` Erdős-adjacent entry) with Dickson/Oppermann/Hardy–Littlewood/Lemoine as "素数分布
'著名-无方法'级" (famous-but-no-method tier) — i.e. explicitly excluded not for crowding but
for the complete absence of any credible attack surface, structured or otherwise. Never
individually gated with a score.

**UNLOCK CONDITION.** Genuinely hard to specify — this is the canonical "no route known" case
the FAMOUS-WATCH shelf exists to hold rather than discard. The one concrete, narrower foothold
is the already-catalogued digit-representation variant (`CollatzLike.lean`), which is a
sharper, more tractable-looking finite-flavored sub-statement; watch specifically for any new
method targeting *that* variant rather than the general conjecture, since a technique that
cracks the narrow variant is the most plausible near-term signal worth re-scoring on.

**Crowding note.** Extremely high visibility, effectively unbounded amateur+professional
attention for decades; a new *general* claim would need extraordinary scrutiny (this is the
kind of "graveyard of failed claims" problem S^6, row 1, exemplifies at even higher volume).

---

## Rows NOT included (considered, deliberately excluded from this seed)

- **Kourovka 19.25** (same-order group / Σφ(ord g) unimorphism question) — `orchestration/TARGETS.md`
  line 408: **RESOLVED-EXTERNALLY**, confirmed via arXiv:2607.17477 (Aristotle, 8-problem
  Kourovka sweep). Closed, not a shelf candidate.
- **Kaplansky's UNIT conjecture** (distinct from row 2's zero-divisor conjecture) —
  `orchestration/results/field_sweep_batch1.md` catalogs it as certkind 1, but the general
  statement was already **definitively refuted** by Gardam's 2021 single counterexample
  (Promislow group, F_2) — since it is a universal claim, one witness closes it. Not open;
  excluded to avoid the exact "stale FC tag" trap this project has hit before.
- **Erdős #307** — still nominally ranked #4 in the live TARGETS.md pool (score ≈79,
  "downgraded but never gated") rather than DROP/HOLD; excluded because it has not actually
  sunk on P(solvable) per the shelf's own admission criterion — it is crowded (2+ independent
  FC contributors racing the same barrier PR) but still an active pool candidate, not a shelf
  item.
- **WOWII remainder items (160/100/141/19/198a/314/40)** — TARGETS.md records these as
  explicitly closed out by owner directive ("WOWII 线收官不再立同类"), not shelved.

## Maintenance note for the next reader

This file is a **seed** (18 rows), not exhaustive. `notes/fc_catalog.md` has 133 cataloged
statements and this task mined roughly a dozen by name-search under a 45-minute cap — a
systematic pass (e.g. cross-referencing every catalog entry against a "famous conjecture" name
list) would surface more. The explicit-exclusion list in `orchestration/TARGETS.md` (~line
435-441) also names several items bundled or skipped here for time (Hadamard matrix existence
conjecture, Wall–Sun–Sun primes, Hall's conjecture / abc neighborhood, Dickson's conjecture,
Oppermann's conjecture, first and second Hardy–Littlewood conjectures, Lemoine's conjecture,
Erdős #855) — worth a dedicated pass later.
