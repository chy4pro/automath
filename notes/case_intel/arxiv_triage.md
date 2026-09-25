# arXiv watch triage — relevance/crowding check

Triage of flagged entries in `arxiv_watch_ledger.md` against active-work targets. This is a
crowding/prior-art screen, not a literature review: entries are checked only against (1) the
ETP finite-implication line ("equation 677 ⟹ 255", `problems/etp677/campaign_registry.md`),
(2) Kourovka 16.95 / R.C. Thompson's cyclic-matrix conjecture, (3) the 18-row FAMOUS-WATCH
shelf (`notes/selection/famous_watch.md`), (4) any paper claiming a conjecture/problem solved
with AI assistance.

---

## 2026-08-29 — triage of 20260825 / 20260826 / 20260827 (93 flagged entries)

Scope: all rows under the `## 20260825`, `## 20260826`, `## 20260827` headers in
`arxiv_watch_ledger.md` (33 + 30 + 30 = 93 entries). Screened by title/abstract text in the
ledger; 11 arXiv abstract pages fetched for disambiguation (budget was 15). No PDFs opened, no
ledger/registry files modified.

**Result: 3 hits, all target 4 (AI-CASE). Zero hits on targets 1, 2, 3** — no title or abstract
in this batch touches finite magmas/equational-implication/SAT-certificate vocabulary, cyclic
companion-matrix / permutation-similarity / Kourovka 16.95 vocabulary, or any of the 18
famous-watch names (S^6/Hopf, Kaplansky, Lonely Runner, Agrawal, Kourovka 20.76, Erdős
#699/#982/#617/#779, Zariski Cancellation, Casas-Alvero, Circulant Hadamard, Jacobian n=2,
Cycle Double Cover 5-cycle version, Kalai 6(a), Andrews-Curtis, Conway's 99-graph, Collatz).

### Hits

1. **arXiv:2608.24797** — "Fröberg's Conjecture for Quintics and Septics in Four Variables"
   (Qihang Wang, Dongming Zhang; math.AC; ledger arm: ai-disclosure; day 20260825)
   Target: 4 (AI-CASE). Why: proves Fröberg's predicted Hilbert-series ranges for quintic (d=5)
   and septic (d=7) forms in 4 variables via Macaulay-matrix endpoint-rank certificates;
   abstract states verbatim "The main results of this paper were obtained through a
   generative-AI workflow using OpenAI GPT-5.6 Sol, Anthropic Claude Fable 5, and Grok 4.6."
   Severity: AI-CASE. Secondary note: names **Claude Fable 5** by name as one of three models
   in a multi-model generative-AI proof workflow for a named conjecture — same-tier signal to
   the model-tier-discipline memory; worth a glance as a possible external precedent for
   multi-model conjecture-cracking methodology, independent of ETP/Kourovka relevance.

2. **arXiv:2608.25220** — "FLARE: Verifying MILP Reformulations with LLM-Based Theorem
   Proving" (Henry Robbins, Connor Lawless, Madeleine Udell; cs.AI/cs.LO/math.OC; ledger arm:
   ai-disclosure; day 20260825)
   Target: 4 (AI-CASE, weaker fit). Why: LLM-based agent + Lean proof assistant produce
   machine-checked certificates verifying MILP reformulations (FormulationBench, 100% accuracy
   on the NP-hard subset). Not a named-conjecture resolution, but explicit Lean+AI
   theorem-proving tooling matches the target-4 examples list. Severity: AI-CASE.

3. **arXiv:2608.24961** — "The Gold Rush in AI4Math: Where Are We Now?" (Jiashun Jin, Zheng
   Tracy Ke, Bingcheng Sui; stat.AP/cs.CY/cs.DL; ledger arm: resolution; day 20260825)
   Target: 4 (AI-CASE, landscape/meta). Why: bibliometric census of all math-category arXiv
   submissions 2026-03-01 to 2026-08-20 (32,944 total); 3,575 disclose AI use, 1,712 with
   "substantive mathematical contribution"; substantive-use rate grew 1.39% (March) to 14.09%
   (through Aug 20); 717 named open-problem records tied to substantive AI use, of which **71%
   are self-reported as fully resolved** (proofs more common than disproofs); usage concentrated
   in Combinatorics (volume) and Metric Geometry (rate); OpenAI systems most-used, Anthropic
   second. Severity: AI-CASE. No specific conjecture, tool version, or research group named in
   the abstract — this is crowding *context* (how saturated the AI-solves-open-problems space
   is generally) rather than a specific competitor lead, but directly load-bearing for the
   project's overall crowding posture and worth a full read outside this triage.

### Non-hits worth recording (checked, ruled out)

- **arXiv:2608.25092** "Complete Mappings of Semigroups" (Araújo/Bentz/Cameron) — fetched on
  target-1 suspicion (semigroup/Latin-square adjacency to magma theory). Abstract confirms:
  complete-mapping/transversal theory for finite semigroups (Hall–Paige-conjecture adjacent),
  no equational-theories-project vocabulary, no SAT/CNF, no numbered-equation-implication
  content. NOISE.
- **arXiv:2608.26294** "An Elementary Proof of Hopf's Curvatura Integra Theorem" — fetched on
  target-3 suspicion (name collision with the S^6/Hopf famous-watch row). Abstract confirms:
  classical total-curvature-of-hypersurfaces theorem, unrelated to complex structures on S^6.
  NOISE.
- **arXiv:2608.27416** "Refutation of the Non-Cancelling-Intersections Conjecture" — fetched on
  target-3 suspicion (name collision with Zariski Cancellation Problem). Abstract confirms:
  combinatorial lattice/dot-algebra representation theory, unrelated to Zariski Cancellation.
  NOISE.
- **arXiv:2608.26628** "Open Problems in Mathematical Logic" (Tianyuan Workshop problem list)
  — fetched as a general open-problems survey that might catalog Kourovka/Thompson-adjacent
  items. Abstract is pure workshop metadata (no problem list content) — no reference to
  Kourovka, Thompson, or magma/equational-implication problems recoverable from the abstract.
  NOISE (title-only signal was the only reason to check).
- ai-disclosure-arm entries checked and ruled out as NOT conjecture-solved-by-AI: **2608.25099**
  (control theory for LLM multi-agent consensus — subject is AI systems, not a math conjecture),
  **2608.23986** (queueing/economics model of LLM inference degradation), **2608.26288** (Muon
  optimizer convergence proof — ML theory, no named conjecture), **2608.27143** (probability
  bounds for random sums, generative-AI response times used only as one of three application
  examples). All four: NOISE — "ai-disclosure" ledger arm flags AI-tool disclosure generally,
  not conjecture resolution.

### Severity counts

- COMPETITOR: 0
- PRIOR-ART: 0
- FAMOUS-WATCH: 0
- AI-CASE: 3 (2608.24797, 2608.25220, 2608.24961)
- NOISE: 90 (all remaining entries across the three days, including the 7 explicitly checked
  above)
