# Task: literature/attribution triage of prose citations with no machine-resolvable identifier

We (an automated math research project) publish papers with bibliographies. A citation gate we
built checks every reference for a resolvable arXiv id or DOI; those that have one get verified
automatically against arXiv/Crossref. But **71 of our 76 total bibliography entries, across 5
papers, carry no arXiv id or DOI at all** — they are prose citations (author, title, journal,
year, pages typed by an earlier automated literature pass) that the machine gate cannot check.
Two independent cross-family audit rounds on other parts of these papers already found real
problems in this exact category (one citation admits outright "we did not consult the original";
several are marked "as supplied by our automated literature pass" with no independent check; three
citations to live web resources could not be confirmed without a browsing tool). **This is the
axis that has produced the most findings so far**, and most of the 71 have never been individually
assessed. We want your honest, best-effort judgment on each one — not a guess dressed up as a
fact.

**We are NOT giving you internet access or asking you to browse anything.** Assess each citation
using only what you already know (your training data). If you are not confident about a specific
entry, say so plainly — "I don't know, I have no confident knowledge of this source" is exactly the
right answer for many of these, and far more useful to us than an invented-sounding confirmation.
**The failure mode we are most worried about is a fluent, confident-sounding assessment of a
citation you don't actually have reliable knowledge of.** Every claim you make will be checked
against real bibliographic databases by an independent reviewer, so overclaiming will be caught,
and it costs us more than an honest "unknown."

## Scope note — what is EXCLUDED and why

Of the 76 total bibliography entries, we exclude ~45 that are the project's own internal working
reports (things like "AutoMath campaign, internal report `problems/etp677/R9A_DO_report.md`") —
these aren't external literature, there is nothing to attribute, and their existence on disk has
already been separately confirmed. **Below is the full list of the remaining ~26 distinct external
citations** (some appear, with near-identical wording, in more than one paper — we list each
occurrence so you can see exactly what was published where). This selection is exhaustive over the
external, non-self-referential citations in the 71; nothing external has been held back.

## What we want per citation

For EACH numbered entry below, give:
1. **Plausibility verdict**: one of `MATCHES KNOWN WORK` (you have specific, reliable knowledge
   this citation is accurate as stated), `PARTIALLY MATCHES` (some details right, name the
   specific ones you believe are wrong or unverifiable), `DOES NOT MATCH / LOOKS WRONG` (name the
   specific discrepancy, e.g. wrong journal, wrong year, wrong page numbers, wrong co-authors, or
   you believe the work does not exist as described), or `NO CONFIDENT KNOWLEDGE` (you cannot
   assess it either way — this is a fine and expected answer for obscure sources, OEIS comments,
   or web-only resources).
2. **If MATCHES or PARTIALLY MATCHES**: what specifically do you know that supports this (the real
   title, venue, year, as you recall them), so a human can spot-check your memory against a
   database.
3. **If DOES NOT MATCH**: be as specific as possible about what is wrong, rather than a vague "this
   seems off."

Do not try to look anything up or simulate browsing — answer from what you already know, and be
explicit about your confidence.

---

## CITATIONS TO TRIAGE

### From `papers/a211417/main.tex` (a proof of a Bala congruence conjecture for OEIS A211417)

**A1. [oeis]** OEIS Foundation Inc., *The On-Line Encyclopedia of Integer Sequences*.
`https://oeis.org`. Sequences cited: A211417 (comments of P. Bala, 24 January 2020 and 28 August
2025), A295431 (Vasyunin's list of the 52 sporadic integral factorial ratio sequences of height
one).

**A2. [bala]** P. Bala, comments on OEIS A211417, 28 August 2025, conjecturing a constant `D(r)`
such that `D(r)*a(n) / prod(30n-i)` (product over `i` coprime to 30, `1<=i<=r`) is integral for
all `n`, and that similar results may hold for the 52 sporadic sequences of A295431.

**A3. [landau]** E. Landau, *Sur les conditions de divisibilité d'un produit de factorielles par
un autre*, Nouvelles Annales de Mathématiques (3) **19** (1900), 344-362.

**A4. [bober]** J. W. Bober, *Factorial ratios, hypergeometric series, and a family of step
functions*, J. London Math. Soc. (2) **79** (2009), 422-444.

**A5. [formalconjectures]** Google DeepMind, *formal-conjectures*: a collection of formalized
conjectures in Lean 4. `https://github.com/google-deepmind/formal-conjectures`.

**A6. [lean4]** L. de Moura and S. Ullrich, *The Lean 4 theorem prover and programming language*,
in: Automated Deduction — CADE 28, Lecture Notes in Computer Science 12699, Springer, 2021,
pp. 625-635.

**A7. [mathlib]** The mathlib Community, *The Lean mathematical library*, in: Proceedings of the
9th ACM SIGPLAN International Conference on Certified Programs and Proofs (CPP 2020), ACM, 2020,
pp. 367-381.

### From `papers/batch1/main.tex` (machine-verified resolutions of four OEIS conjectures)

**B1. [oeis]** Sequences A100434 (N. J. A. Sloane, 21 Nov 2004, suggested by C. Dement), A108211
(R. Zumkeller, 15 Jun 2005; comment of C. Kimberling, 9 Sep 2014), A114831 (J. V. Post, 19 Feb
2006), A114362 (B. Cloitre, 9 Feb 2006; comments of T. Ordowski), A348829 (T. Ordowski, 1 Nov
2021).

**B2. [kimberling]** C. Kimberling, comment on OEIS A108211, 9 September 2014, conjecturing a
closed form for `a(n)` via a floor of a reciprocal involving `log(2)` and a harmonic-type sum.

**B3. [dement]** C. Dement, comment on OEIS A100434, 18 December 2004, defining auxiliary
sequences `b,c,d,e,f,g` and conjecturing `c(n)+d(n) = e(n)+f(n) = g(n)+a(n) = b(n)`.

**B4. [ordowski]** T. Ordowski, comments on OEIS A114362 (13 Nov 2022) and A348829 (13 Nov 2022,
6 Nov 2024), involving the prime zeta function `P(x) = sum_p 1/p^x`.

**B5. [funsearch]** B. Romera-Paredes, M. Barekatain, A. Novikov, M. Balog, M. P. Kumar,
E. Dupont, F. J. R. Ruiz, J. S. Ellenberg, P. Wang, O. Fawzi, P. Kohli, and A. Fawzi,
*Mathematical discoveries from program search with large language models*, Nature **625** (2024),
468-475.

**B6. [alphaevolve]** A. Novikov et al., *AlphaEvolve: a coding agent for scientific and
algorithmic discovery*, Google DeepMind, 2025.

**B7. [erdosproblems]** T. F. Bloom (site), T. Tao (community database), and contributors,
*Erdős Problems* and the associated AI-contributions wiki. `https://www.erdosproblems.com`,
`https://github.com/teorth/erdosproblems`.

### From `papers/fernandes/main.tex` (a proof of a Fernandes-Vernitski conjecture on parity
### subgroups)

**F1. [fv]** V. H. Fernandes and A. Vernitski, *Internat. J. Algebra Comput.* (2026). **No title,
no volume, no pages are given.** The paper itself states: "Bibliographic details are as supplied
by our automated literature pass; we did not consult the article." Cited only as background on the
ranks of certain monoids.

**F2. [goursat]** É. Goursat, *Sur les substitutions orthogonales et les divisions régulières de
l'espace*, Ann. Sci. École Norm. Sup. (3) **6** (1889), 9-102. Cited as the source of a lemma
(Goursat's lemma, in the paper's terminology).

**F3. [hall]** P. Hall, *The Eulerian functions of a group*, Quart. J. Math. Oxford Ser. **7**
(1936), 134-151.

### From `papers/wowii61/body.tex` (a graph-residue conjecture, "Written on the Wall II" #61)

**W1. [formalconjectures]** Google DeepMind and contributors, *formal-conjectures*: a corpus of
open conjectures in Lean 4, attributing the specific conjecture treated to the "Written on the
Wall II" collection generated by the `Graffiti.pc` program (the paper states it consumed the
formal Lean file and did not consult the original collection).

**W2. [havel]** V. Havel, *A remark on the existence of finite graphs*, Časopis Pěst. Mat. **80**
(1955), 477-480. The paper states: "Bibliographic details as supplied by our automated literature
pass" (i.e. not independently checked). This is the paper that establishes the Havel-Hakimi
degree-sequence realizability algorithm.

**W3. [hakimi]** S. L. Hakimi, *On realizability of a set of integers as degrees of the vertices
of a linear graph*, J. Soc. Indust. Appl. Math. **10** (1962), 496-506. Same "as supplied by our
automated literature pass" caveat.

**W4. [fms]** O. Favaron, M. Mahéo and J.-F. Saclé, *On the residue of a graph*, J. Graph Theory
**15** (1991), 39-64. Same caveat; cited as the source of a specific fact about the "residue"
graph invariant (related to the Havel-Hakimi process) and largest induced forests.

**W5. [gk]** J. R. Griggs and D. J. Kleitman, *Independence and the Havel-Hakimi residue*,
Discrete Math. **127** (1994), 209-212. Same caveat; cited as giving a short alternative proof of
the fact attributed to [fms] above.

### From `papers/etp677_structure/main.tex` (structure theory of finite magmas satisfying a
### specific equational law, "Equation 677")

**E1. [blueprint]** Equational Theories Project, *Blueprint, Chapter 13: Equation 677*.
`https://teorth.github.io/equational_theories/blueprint/677-chapter.html`. (This is part of the
"Equational Theories Project", a real large collaborative formalization effort — the blueprint URL
pattern and chapter-13-for-equation-677 numbering is what we want checked for plausibility, not a
traditional print citation.)

**E2. [formalconjectures]** Google DeepMind, *formal-conjectures*, file
`FormalConjectures/Other/EquationalTheories_677_255.lean`.
`https://github.com/google-deepmind/formal-conjectures`.

**E3. [icarm]** NSF Institute for Computer-Aided Reasoning in Mathematics, *eq677 model database*.
`https://eq677.icarm.cloud`, built on a model searcher at `https://github.com/memoryleak47/eq677`.

**E4. [grisha]** G. Pochuev, *finite-magma-e677-to-e255*.
`https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255`, described as an independent project
on the same problem.

**E5. [kissat]** A. Biere et al., *Kissat SAT solver*, version 4.0.4.
`https://github.com/arminbiere/kissat`.

---

## Additionally, three specific attribution claims we could not settle ourselves and would value
## your read on (these are claims ABOUT the content of E1/E2/E3/E4, not just their existence)

**Q1.** Does the arXiv paper describing "The Equational Theories Project" (a large collaborative
project cataloguing ~2.5 million magma equations and their implications, using automated and
crowdsourced proof search, associated with Terence Tao) discuss Equation 677 and Equation 255
specifically, and if you know, is the finite implication "677 implies 255" described there (or in
associated materials you know of) as an open problem, with any stated expectation about whether it
is true or false?

**Q2.** Is "Kissat" (cited at E5) in fact a real, actively maintained SAT solver by Armin Biere and
collaborators? Does a "version 4.0.4" release sound plausible to you, or does that specific version
number look fabricated?

**Q3.** For [fms] (W4) and [gk] (W5): do these two citations, taken together, look like a real
"original result + alternative short proof" pair in the graph-residue literature (i.e. is it
plausible that Griggs-Kleitman gave a short proof of a Favaron-Mahéo-Saclé result), based on what
you know of this specific corner of graph theory?

---

## What to hand back

A table or list, one row per citation ID (A1-A7, B1-B7, F1-F3, W1-W5, E1-E5, Q1-Q3), each with the
verdict and supporting detail as specified above. End with a short honest summary: which citations
(if any) you believe are outright wrong or likely fabricated, which you are confident are correct,
and — the most important part — which ones you have NO reliable knowledge about at all (we expect
this to be the largest category, and that is fine).
