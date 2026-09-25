# Erdős #859: G2 prior-work and priority check

Date: 2026-09-25. Performed by a read-only G2 subagent (Claude Opus 5.5) for the coordinator.
Scope: prior work on the density `d_t` of `A_t = {n : t is a sum of distinct divisors of n}`,
compared against the project's local results (README.md upper bound; LOWER_BOUND.md effective
lower bound `C (log t)^{-2.9096...}` for `t >= 1024`; QUALITATIVE_LOWER_BOUND.md
`d_t >> (log t)^{-2.7136...}`). All web checks ran on 2026-09-25 from an anonymous (logged-out) client.

**Overall verdict: SUBSUMED.** A public arXiv preprint posted 2026-09-21 records the same upper
bound with the same proof. It also records a lower bound of exponent 1, which rests on 2013/2015
published theorems. Details are in the Verdict section.

---

## 1. Queries run

### Local
- `grep -n 859 /work/problems/erdosproblems/data/*` shows the teorth mirror (last commit 2026-09-07).
  Entry: status `open` (last_update 2025-08-31), formalized `yes` (2025-12-09), tags number theory/divisors.
- `/work/problems/formal-conjectures/FormalConjectures/ErdosProblems/859.lean` (local mirror 2026-08-24).
  It was diffed against upstream `main` via the GitHub API and differs only in module/`public import`
  boilerplate (commit 6fbb54f, 2026-09-18).
- `/work/notes/selection/primary_read_0909.md` is the project's earlier primary read of Erdős 1970 §3.
  Its G2 line said "No follow-up literature found".

### erdosproblems.com (curl, raw HTML)
- `/859`, `/forum/discuss/859` (redirects to `/forum/thread/859`), `/forum/thread/859/proof-claims`,
  `/history/859`, `/latex/859`, `/forum` (index, grepped for 859).
- A WebFetch of `/859` was also made.

### WebSearch (all queries, verbatim)
1. `"sum of distinct divisors" density "log t" Erdős`
2. `"sums of distinct divisors" density integers n such that t is a sum of distinct divisors of n`
3. `Erdős "Some extremal problems in combinatorial number theory" 1970 Macintyre cited`
4. `Erdős problem 859 distinct divisors density`
5. `Weingartner practical numbers integers with dense divisors arXiv`
6. `"sum of distinct divisors of n" "density" "t" Tenenbaum OR Weingartner OR Saias`
7. `Saias "entiers à diviseurs denses"`
8. `Pomerance Thompson Weingartner "practical" integers divisor of every degree`
9. `"A generalization of the practical numbers" International Journal of Number Theory 2018`
10. `"t-practical" OR "practical component" integers divisor sums density Weingartner`
11. `Tenenbaum "Sur un problème de crible et ses applications" 1986 practical numbers applications Erdős`
12. `Pollack Thompson "practical pretenders" cited by`
13. `site:mathoverflow.net "sum of distinct divisors" density`
14. `site:math.stackexchange.com "sum of distinct divisors" density of integers n`
15. `Ruzsa "Erdős and the integers" Journal of Number Theory 1999 pdf`
16. `Benkoski Erdős "On weird and pseudoperfect numbers" 1974 pdf`
17. `"Erdős and the integers" Ruzsa "distinct divisors" OR "practical numbers"`
18. `"sum of distinct divisors of n" "log t" density lower bound 2025 OR 2026 arXiv`
19. `"Erdős problem" 859 OR "#859" divisors arXiv 2026`
20. `leanprover zulip "Erdős" "859" divisors`
21. `"Scott D. Hughes" arXiv 2026 number theory`
22. `"The density of sums of distinct divisors"`
23. `site:leanprover.zulipchat.com Erdős problem 859`
24. `Reuijl "Representing integers with sums of proper divisors" Utrecht thesis`

### arXiv
- arXiv web search (`arxiv.org/search`, newest first):
  - abstract `"distinct divisors"` (19 hits)
  - abstract `"practical numbers"` (~55 hits)
  - title `"practical number"` (11 hits)
- The arXiv export API returned HTTP 406 and was not usable.
- Abstract pages read: 2609.25446, 2609.26014, 2609.10902, 2604.05284, 2605.00695, 1411.6974.
- LaTeX sources read in full or grepped:
  - 2609.25446 (read in full)
  - 1411.6974 (intro and theorems)
  - 1201.3168 (Theorem 1.1, lower-bound proof, bibliography)
  - 2402.08119 (citation context of Er70)
  - 1908.00488 (grepped: no distinct-divisor or practical content)

### Citation indexes
- zbMATH Open API:
  - Erdős 1970 is Zbl 0214.30602.
  - `rf:3340378` lists the documents citing it (4).
  - `"distinct divisors" py:2020-2026` returned 18 hits.
- Google Scholar:
  - `"Some extremal problems in combinatorial number theory"`
  - `"sum of distinct divisors" "density" "log t"`
  - `"Representing integers with sums of proper divisors"`
  - `Erdős 859 "distinct divisors"`
  - The "Cited by 13" list for Er70 (both pages).
  - One request hit a captcha and a retry succeeded.
- OpenAlex: Er70 is not indexed. It lists 3 works citing Pollack–Thompson, all unrelated.
- Semantic Scholar: HTTP 429 (not used).
- Weingartner's publication list (sites.google.com/a/suu.edu/weingartner/publications): 40 items.

### Q&A sites (StackExchange API)
- MathOverflow and Math.SE `search/advanced`: "sum of distinct divisors", "sums of distinct divisors",
  "practical numbers density", "erdos problem 859".
- MathOverflow `search/excerpts`: "practical number", "Erdős divisors density log",
  "t is a sum of distinct divisors".
- Bodies read: MO 515460 (2026-09-22), MO 207512, MO 46716, MSE 1892683.

### GitHub (gh API)
- `google-deepmind/formal-conjectures` issue/PR search for `859` and `Erdos859`.
- Details and comments read for PRs 1218, 1524, 1544, 1800, 2581, 2706, 2779, 3105, 3228, 3295
  and issues 984, 1542.
- Open-PR scan by title, and commit history of `859.lean`.
- `teorth/erdosproblems` search for `859`: 0 results.

### Could not access (stated, not guessed)
- **Erdős 1970 scan** (`users.renyi.hu/~p_erdos/1970-21.pdf`). It is an image-only PDF, and this
  session has no OCR or PDF renderer. The statement of Er70 therefore rests on the project's
  2026-09-09 primary read. It agrees with Hughes's quotations: `d_t < (log t)^{-c_1}`, lower bound
  `(log t)^{-c_2}` asserted without proof, and (33) `d_t = (1+o(1)) c_3/(log t)^{c_4}`, "if true may
  not be quite easy to prove".
- **Ruzsa, "Erdős and the integers"**, JNT 79 (1999). ScienceDirect returned 403. The paper cites Er70,
  and its content on `d_t` is unknown.
- **Guy, Unsolved Problems in Number Theory**, "Divisibility" chapter (Springer): not accessed.
- **Reuijl (Utrecht MSc thesis 2026)**: 403. By its abstract it concerns s-practical numbers.
- **World Scientific page for Schwab–Thompson**: 403. Its arXiv abstract was used instead.
- **Lean Zulip**: not searchable without login. Two web searches found nothing.
- **Full texts of Tenenbaum 1986 and Saias 1997**: not read. They are upstream of the hits below and
  were not needed for the verdict.

---

## 2. Hits (exact statements)

### H1. S. D. Hughes, *The density of sums of distinct divisors*, arXiv:2609.25446v1 (submitted 2026-09-21, 11 pp., math.NT)

This is the decisive hit. It is a preprint with only v1 visible and no journal reference. The source
was read in full. It cites erdosproblems.com/859 ("accessed 21 September 2026"), Er70, Ford 2008,
Pollack–Thompson 2013, and Weingartner 2015/2015pc/2020. It uses Erdős's own labelling of the
constants (Remark 1: `c_1, c_2` are the bound exponents and `c_3, c_4` belong to (33)). It notes that
the problem list swaps these labels.

- **Theorem 1.**
  - Setup: `f(n)` is the largest `Y` such that every integer in `[1,Y]` is a sum of distinct divisors
    of `n`, and `nu_t = dens{n : f(n) >= t}`.
  - Then `d_t >= nu_t` for every `t`.
  - As `t -> infinity`, `nu_t = (K/log t)(1 + O(log log t/log t))`, where `K = c e^{-gamma} = 0.75015...`
    and `c = 1.33607...` is the practical-number constant.
  - Hence `liminf d_t log t >= K`.
  - The proof is Weingartner [1411.6974, Thm 1(iv) and the display after (3)].
- **Theorem 2.**
  - `d_t << (log log t)^{delta-3/2} / (log t)^{delta}` as `t -> infinity`, with
    `delta = 1 - (1+log log 2)/log 2`. In particular `d_t = o((log t)^{-delta})`.
  - The proof is Erdős's split with the window `(t/(log t)^2, t]` plus Ford, Ann. Math. 168, Thm 1(v).
  - The no-window-divisor case is bounded through `S_y(n) = sum_{d|n, d<=y} d`, which gives
    density `<= y/t = (log t)^{-2}`.
  - The constant is not numerical, and the onset is "for large t".
- **Corollary 3.** If (33) holds with `c_3 > 0`, then `delta < c_4 <= 1`. If `c_4 = 1`, then `c_3 >= K`.
- **Theorem 4.**
  - `liminf (log t)(d_t - nu_t) >= K I` and `liminf (log t) d_t >= K(1+I)`, with
    `I = int_0^2 G = 0.0588797799...`.
  - `d_t >= 0.79/log t` for every sufficiently large integer `t`.
  - This is a two-prime construction plus a residue-coverage lemma. `I > 4/75` is certified by
    rational interval arithmetic.
- **Corollary 5.** `K` is not the asymptotic constant of `d_t log t`. If (33) holds, then either
  `c_4 < 1`, or `c_4 = 1` with `c_3 >= K(1+I) > 0.79`.
- **Author's disclaimers (verbatim):**
  - "We claim no novelty of method in either [Theorems 1, 2]."
  - "Erdős's question (33) remains open."
  - "No O(1/log t) upper bound, no limiting constant, and no numerical threshold for 'sufficiently large' are asserted."
- **Relation to our results:**
  - Theorem 2 is our README Theorem. The route, window, Ford input and the `(log t)^{-2}` class-2
    bound (our referee's 09-09 strengthening) are all the same. Our only additions are the checked
    onset `t >= 8100` and the form `C = (8·4^delta) C_F + 1`. Neither makes the constant numerical,
    because `C_F` is not numerical.
  - Corollary 3 contains our Corollary (`c_4 > delta`) and adds `c_4 <= 1`.
  - Theorems 1 and 4 have exponent 1 and dominate both of our lower bounds (2.7136 and 2.9096).
  - Theorem 4's proof was not verified here. Theorems 1–2 are short deductions from published
    theorems, and I checked them against the cited sources (H2, H3, Ford).

### H2. P. Pollack and L. Thompson, *Practical pretenders*, Publ. Math. Debrecen 82 (2013) 651–667, arXiv:1201.3168

- **Theorem 1.1.** There are absolute positive constants `c_3, c_4` such that
  `c_3 x/log y <= N(x,y) <= c_4 x/log y` for `4 <= y <= x`, where `N(x,y) = #{n <= x : f(n) >= y}`.
- **Lemma 2.1.** `f(n) = sigma(practical component of n)`.
- **One-line consequence (not stated in PT13):** `{n : f(n) >= t} ⊆ A_t`, so `d_t >= c_3/log t` for
  every integer `t >= 4`. The constant is absolute but not numerical: the proof uses Saias's
  `PR(x) >> x/log x` and a sieve lemma, with no numerical values.
- PT13 does not cite Erdős 1970 (its Erdős references are 1935 and 1950), so PT13 itself does not
  mention `d_t`. Hughes (H1) records the deduction explicitly.
- **Relation to our work:** the set `S_t = {n : F(n) >= t}` in our LOWER_BOUND.md §1–2, with
  `F(n) = max sigma(m)` over practical `m | n`, is exactly `{n : f(n) >= t}`. Every practical divisor
  of `n` divides the practical component (H1, Lemma 2), and `sigma` is monotone under divisibility.
  - Our measured `density(S_t)·log t ≈ 0.70–0.95` is consistent with `K = 0.750`.
  - We had the right set but not the reference, so its order `1/log t` was already a 2013 theorem.

### H3. A. Weingartner, *Integers with large practical component*, Publ. Math. Debrecen 87 (2015) 439–447, arXiv:1411.6974

- **Theorem 1(iv).** `N(x,y) = x nu_y + O(2^y)`, with
  `nu_y = 1 - sum_{sigma(n)<y} (chi(n)/n) prod_{p <= sigma(n)+1} (1 - 1/p)`.
- Together with display (3): `mu_y, nu_y = (c e^{-gamma}/log y)(1 + O(log log y/log y))`.
- **Corollary 1.** The density of `{n : g(n) = m}` is `alpha_m = (chi(m)/m) prod_{p<=sigma(m)+1}(1-1/p)`.
- **Consequence:** `d_t >= nu_t = (K + o(1))/log t`.
- The paper does not cite Erdős 1970.

### Background inputs (published, correctly used by the project; not competing results)
- Weingartner, QJM 66 (2015), arXiv:1405.2585: `P(x) = (cx/log x)(1 + O(log log x/log x))`.
- Weingartner, IJNT 19 (2023), arXiv:2104.07137: `T(x)` (the input of our qualitative bound).
- Weingartner, IJNT 16 (2020), arXiv:1906.07819: `1.33607322 < c < 1.33607654` (cited by H1).
- Saias, JNT 62 (1997): `PR(x) ≍ x/log x`.
- Ford, Ann. Math. 168 (2008): `H(x,y,z)`.

### Checked and unrelated
- **Hughes, arXiv:2609.10902 (2026-09-09).** Bounds `h(n!)`, the number of distinct divisors needed
  for practical `N = n!`.
- **Hou–Zhao, arXiv:2609.26014 (2026-09-22).** Close divisors and equal subset sums (Ford–Green–Koukoulopoulos).
- **Aidun–Thompson, arXiv:2604.05284.** Distribution of `sum_{d|n} s(d)`.
- **Campbell, arXiv:2605.00695.** `sum 1/d(d(n))`.
- **Schwab–Thompson, IJNT 14 (2018), arXiv:1701.08504.** f-practical numbers.
- **Pomerance–Thompson–Weingartner, Acta Arith. 175 (2016).** φ-practical numbers.
- **Papers citing Er70 (zbMATH and Scholar):** each cites Er70 for other content (pseudoperfect
  numbers, lcm-extremal sets, and so on). None concerns `d_t`.
  - Benkoski–Erdős 1974
  - Cohen et al., Acta Arith. 2020
  - Lebowitz-Lockard, Acta Arith. 2024
  - Lebowitz-Lockard–Vandehey, arXiv:2402.08119, which cites Er70 Thm 2 on pseudoperfect density
  - Tang–Zhang, arXiv:2512.20055
  - Luo–Yang–Zhu, arXiv:2609.07268
  - Alexeev et al., #1196
  - Chojecki (#858 and harmonic LCM)
  - Klotz 1977
- **Survey arXiv:1908.00488:** no distinct-divisor or practical-number content.
- **MathOverflow and Math.SE:** no thread on `d_t` or #859. The nearest hits were MO 360288 (practical
  numbers in Goldbach-type sums) and MSE threads on `n!`. None is relevant.

### Formalization and forum records
- **formal-conjectures `ErdosProblems/859.lean`** (merged 2025-12-09, #1218, by KaJabben), statement only:
  - `erdos_859` (`research open`, `sorry`)
  - `erdos_859.variants.erdos_upper_lower_bounds` (`research solved`, `sorry`)
  - `positive_density` (`textbook`, `sorry`)
  - `trivial_case` (proved, #1800)
- **Fixes:** #1524 made the density depend on `t`. Before that fix, Aristotle exploited the
  `t`-independent density at `t = 0` (issue #1542 comment).
- **Six "formally solved" PRs** (#2581, #2706, #2779, #3105, #3228, #3295; 2026-03; theaustinhatfield,
  "Claude Sonnet 4.6 in Aletheia style harness", "loophole pattern"). They only change the category
  attribute and contain no proof. All were closed unmerged.
- **Open items:** no open issue or PR for 859.

---

## 3. Verdict per item

**(a) Lower bound with an explicit or numerical exponent: YES, exponent 1, which dominates ours.**
- PT13 (2013) implies `d_t >= c/log t` for all `t >= 4`, with an absolute, non-numerical `c`.
- W15pc (2015) implies `d_t >= nu_t ~ K/log t`.
- H1 (2026-09-21) states `d_t >= nu_t`, `liminf d_t log t >= K(1+I) ≈ 0.794`, and `d_t >= 0.79/log t`
  for sufficiently large `t`.
- Our 2.7136 and 2.9096 exponents are strictly weaker.
- **Residual not found in the checked literature:** a lower bound with a numerical constant and a
  numerical range (our `C (log t)^{-2.9096}` for `t >= 1024`). H1 explicitly asserts no numerical
  threshold, and PT13's constants are not numerical. This residual is effectiveness only, at a much
  worse exponent.

**(b) Upper bound with an explicit exponent: YES, identical to ours.**
- H1 Theorem 2 gives `d_t << (log log t)^{delta-3/2}(log t)^{-delta}` by the same proof.
- Neither version has a numerical constant, because Ford's constant is not numerical.
- Our checked onset `t >= 8100` is the only textual difference.

**(c) Determination of Erdős's constants: NO determination exists; only constraints.**
- In Erdős's labelling for (33), H1 proves: if (33) holds, then `delta < c_4 <= 1`, and `c_4 = 1`
  forces `c_3 >= K(1+I) > 0.79`.
- In the erdosproblems labelling (bound exponents), the known bounds allow any lower exponent
  greater than 1 eventually, and any upper exponent `<= delta`.
- Our Corollary `c_4 > delta` is contained in H1 Corollary 3.
- **Labelling caveat:** our README and the task statement mix the two conventions. They quote the bounds
  with erdosproblems labels and (33) with Erdős labels. H1 Remark 1 flags exactly this clash, and any
  write-up should fix it.

**(d) Resolution of (33): NO.** H1 states that (33) remains open. H1 shows only that `d_t` is not
asymptotic to `K/log t`.

**(e) Current claims or activity on erdosproblems.com/859: none on the site; one active public author off-site.**
- **Page state on 2026-09-25:**
  - "Proof expositions (0)", "Comments (0)", "Proof claims (0)" ("No proof claims have been submitted yet").
  - Every reaction, including "Currently working on" and "Working on formalising", shows "None".
  - The only revision in the history is dated 2025-10-20 and is a formatting change. The forum index
    lists no activity for 859.
- **Off-site activity:** H1 (Hughes, 2026-09-21) cites the page but has not posted there. The empty
  page is therefore not evidence of inactivity.
- **Priority:** no priority claim can be made. The public record gives priority for the upper bound
  and the exponent-1 lower bound to H1, PT13 and W15pc. Our 2026-09-09 work was never published.

**(f) Open formalization or forum thread: no open PR or issue; statement-only Lean file exists.**
- formal-conjectures holds statement-only Lean with `sorry` (details in §2).
- The `upper_lower_bounds` variant is tagged `research solved` but has no Lean proof. A proof would
  need Ford 2008 (for an upper exponent) or at least PT13-type inputs. No proof is in progress.
- The erdosproblems forum thread for 859 is empty. No MathOverflow or Math.SE thread exists.
- Lean Zulip could not be checked directly, and web search found nothing.

---

## 4. Overall verdict: **SUBSUMED**

Reasoning:
1. **Upper bound and its corollary.** A public preprint (H1, 2026-09-21) proves them with the same
   argument, and adds `c_4 <= 1`. Our version differs only by a checked onset `t >= 8100`, and it has
   the same non-numerical constant.
2. **Both lower bounds.** Their exponents (2.7136, 2.9096) are dominated by exponent 1.
   - That exponent follows in one line from Pollack–Thompson 2013.
   - Its sharp constant follows from Weingartner 2015.
   - H1 states it explicitly and improves the constant to 0.79 for large `t`.
3. **The only unmatched item** is numerical effectiveness: a numerical constant and range for a lower
   bound with a weak exponent. This does not improve the known growth rate. Whether it has any
   standalone value is a coordinator decision. Any write-up must cite H1, PT13 and W15pc and must not
   make "first", priority or novelty wording about `d_t` bounds.
4. **(33) is open.** Our work does not address it beyond what H1 already records.

**Observation for the coordinator (my suggestion, not literature, not verified):**
- The events `{g(n) = m}` for practical `m` are disjoint, with explicit densities `alpha_m` (H3 Cor. 1,
  H1 Lemma 2). Hence `d_t >= sum over practical m > t of alpha_m`, with no Cauchy–Schwarz step.
- Combining this with the project's explicit `A(t)` bound (exponent 1.01, from A4) and explicit Mertens
  bounds would appear to give a numerical lower bound with exponent about 2.01 from one dyadic block,
  and lower if more blocks are used. That already beats 2.9096 and removes the `B`/θ input.
- If the effective residual is pursued at all, this is the cheaper route to examine. It still would not
  reach the known exponent 1 unless explicit practical-number counts are made numerical.
