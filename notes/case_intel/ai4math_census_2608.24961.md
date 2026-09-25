# Case intel: "The Gold Rush in AI4Math" (arXiv:2608.24961)

Source: arXiv:2608.24961v1, Jin/Ke/Sui, submitted 2026-08-25. Read via HTML rendering
(`arxiv.org/html/2608.24961`), abstract cross-checked at `arxiv.org/abs/2608.24961`; PDF
fallback not needed. arXiv HTML is unpaginated — citations below use section/table/figure
numbers, not page numbers.

## 1. Methodology (§2 "Data and study design")

Corpus: all 32,944 arXiv submissions tagged Mathematics (primary or secondary) 2026-03-01
through 2026-08-20 (partial month). PDFs → page-marked text; 1,007/32,944 flagged truncated
(articles >300k chars kept only first/last 150k). Classification instrument: a fixed
questionnaire — (a) 2×4 non-exclusive AI-use subcategories (substantive: proof construction /
problem formulation / formalization&verification / other; non-substantive: language / code /
literature / other), each yes/no, 1–3 confidence, **required verbatim quoted evidence**; (b) an
open-problem block recording status as open / partially resolved / resolved true / resolved
false / unclear, plus whether AI played "a critical role"; (c) author institution/country,
partly web-search-inferred. Classifier: **GPT-5.6 Terra, low reasoning effort**, 100 parallel
workers — explicitly **not** a correctness check: "the responses are based on the authors'
disclosures rather than on assessment of the mathematical content" (§2). "Fully resolved" =
resolved-true + resolved-false, purely from authors' self-description; the paper states this
"do[es] not constitute independent mathematical verification" (§3.3) and is "not a substitute
for peer review... or independent verification of mathematical correctness" (§4). A manual
validation exists but is partial/ongoing: keyword screen over parsed text → ~5,000 candidates →
hand-coded by "more than 10 volunteers" (§2); **no inter-rater agreement or error-rate numbers
are reported anywhere**. The 717 open-problem records are the count of named problem entries
the questionnaire extracted across the 1,712 substantive-use papers (§3.3); one paper can
contribute multiple records.

## 2. Public dataset?

**NOT PUBLIC.** Full-text search of the HTML (body, tables, references, footers) found no
GitHub/Hugging Face/Zenodo/OSF/data-availability link for this paper's own data; the only
Zenodo hit is an unrelated bibliography entry (Alper et al., "Leiden declaration"). The paper's
only concrete listing is **Table 3** (§3.3): the **50 earliest-proposed, fully-resolved,
proposed-year-known** records (of 717), each with arXiv ID / name / subfields / proposed year /
outcome / AI model — an illustrative sample, not the full 717.

Cross-check (full-text + Table-3 grep) against our targets:
- **(a) ETP 677⟹255 / finite magma**: zero hits anywhere in the paper.
- **(b) Kourovka 16.95 / Thompson cyclic-matrix / Dixon**: zero hits.
- **famous_watch.md's 18 rows** (S^6/Hopf, Kaplansky, Lonely Runner, Agrawal, Kourovka 20.76,
  Erdős #699/#982/#617/#779, Zariski Cancellation, Casas-Alvero, Circulant Hadamard/Ryser,
  Jacobian n=2, Cycle Double Cover [5-cycle strengthened], Kalai 6(a), Andrews-Curtis, Conway's
  99-graph, Collatz): **zero exact matches**. One **near match**: Table 3 row 17 lists "Cycle
  Double Cover Conjecture," arXiv **2607.14140**, math.CO, proposed 1973, proved, credited to
  **OpenAI Codex** — same object family as famous_watch row 14, but a **different arXiv ID**
  than our own source for the base-CDC substantiation (2607.16356) and a different credited
  model (our note: GPT-5.6 Sol Ultra, 64 subagents). UNVERIFIED whether these are the same
  underlying claim described two ways or two independent papers — flag for the next
  selection/openness task rather than treat as identity.
- One **adjacent, non-matching mention**: §1 intro cites "an explicit counterexample to the
  Jacobian conjecture in dimension three" (Alpöge and Claude Fable 5, 2026) as a headline
  anecdote — the n≥3 event our row 13 already treats as background, not our n=2 target. It does
  not appear in Table 3 (no proposed year shown), so its status inside the 717 is UNVERIFIED.
- **TARGETS.md names beyond famous_watch** (Erdős #307/#835/#97, Bermond–Thomassen, Hadwiger's,
  Fortune's, Loneliness Spectrum): also zero hits.

## 3. Distribution & verification failures

By status (§3.3, n=717): 103 open, 93 partially resolved, 510 fully resolved (329 true / 181
false), 11 unclear; proofs outnumber disproofs among the resolved. By field (§3.2–3.3, Fig. 3c):
Combinatorics leads both substantive-use papers and open-problem records, then Number Theory,
Algebraic Geometry, Probability. By proposed year (§3.3): of 329 records with a known year, 92
pre-2000 (68 pre-1990), 36 from 2026 itself; 388 records have no reported year. By
model/toolchain (§3.5, Fig. 6 — counts are non-exclusive, over the full 3,575 confirmed-use
manuscripts, **not** open-problem-specific): OpenAI 2,148 (60.08%), Anthropic 776 (21.71%),
Google 334 (9.34%), DeepSeek 80 (2.24%). No Lean/formal-verification breakdown is given for the
717 records specifically (the broader "formalization and verification" subcategory is 427
papers total). **Verification failures/retractions/contested claims: none mentioned anywhere**
(checked retract/dispute/contest/error-rate/withdraw — only unrelated hit is the math term
"Lindenstrauss retraction problem"). The authors state plainly they have not independently
verified any resolution claim and flag this as their central limitation (§4).

## 4. Headline numbers for our posture

Substantive-use share: 1.39% (Mar) → 14.09% (through Aug 20, partial) (§3.1); any-AI-use share
4.75%→24.14%. Monthly substantive counts/denominators (Table 1): Mar 73/5,265, Apr 110/5,097,
May 174/5,525, Jun 253/6,106, Jul 470/6,464, Aug(partial) 632/4,487. **Venue: arXiv Mathematics
submissions only** — no mention anywhere of X/Twitter, blogs, or any non-arXiv channel for these
claims (confirmed absent by full-text search). **Speed of independent verification: not
addressed** — §4 explicitly defers this to future work ("independent verification of
mathematical claims" is listed as what would determine whether the "gold rush" is durable).
Geography (abstract, §3.4): US + China ≈ two-thirds of weighted-author-count share.
