# Candidate problems for the toolkit (small-scale decidable, publicly listed, closable in days) — from line k1695's own knowledge (2026-08-30)

Caveat first: everything below is from memory (knowledge cutoff early 2026). Kourovka numbers and
"open/closed" statuses MUST be verified against the current Kourovka Notebook edition and the
literature by the internet scan before any dispatch. Where I am unsure of the number I say so. Each
entry: statement · status as I believe it · first finite reduction · toolkit fit · effort.

## A. Matrix problems over fields (closest to 16.95; msolve/SAT/exhaustive fit)

### A1. 16.95 itself — remaining pieces we can still close computationally
* n = 4 over every field: needs the characteristic-free step (K6-R2UNIFORM / R1HAND) — in progress.
* Publishable side results already closed (see §R6.104).
* NOT on the portfolio list beyond the publication; n ≥ 5 is a 48-h budgeted exploration.

### A2. Products of two cyclic (nonderogatory) matrices
* Statement (folklore / literature, not sure it is a Kourovka item): is every square matrix over a
  field F a product of two cyclic matrices? Over fields with enough elements this is known
  (Sourour-type factorisation results: every nonscalar matrix is a product of two matrices with
  prescribed eigenvalues), and small fields are the question.
* Status: I believe it is settled for |F| large; small fields (F₂, F₃) may be open or scattered.
* First finite reduction: n ≤ 4 over F₂, F₃ exhaustively (GL and singular classes separately); a
  counterexample or a "yes for n ≤ 4" is a one-day computation with our cyclic() oracle.
* Fit: high (exhaustive + certificates). Effort: 1 day. Novelty risk: high — check literature.

### A3. Waring-type problems for matrices over finite fields
* Statement: for which (n, q, k) is every matrix in M_n(F_q) a sum of two k-th powers? (Analogues:
  sums of two squares, sums of two cubes; also "every matrix is a sum of two nilpotents/idempotents"
  variants.) These appear in the linear-algebra literature (Katre–Garge, Larsen–Shalev–Tiep on
  Waring problems in groups) and, I believe, at least one Kourovka entry asks a Waring-type question
  for matrix groups (number not recalled).
* Status: many cases known; small-(n,q,k) tables incomplete.
* First finite reduction: n ≤ 3, q ≤ 5, k ≤ 4 exhaustive (|M_3(F_5)| = 5⁹ ≈ 2·10⁶; sums of two k-th
  powers by meet-in-the-middle).
* Fit: high. Effort: 1–2 days per table. Publishable as "complete small tables + a conjecture",
  only if the literature scan confirms gaps.

### A4. Products of involutions / commutators in small matrix groups
* Statement family: every element of SL(n, q) is a product of two/three involutions? (Gustafson–
  Halmos–Radjavi: products of ≤ 4 involutions over fields; "two involutions ⟺ similar to inverse".)
  Every element of GL(n,q) a commutator? (Thompson's conjecture / Ore — settled for simple groups
  2010.) I list these to be EXCLUDED unless the scan finds an open small-q case.

### A5. Permutation-matrix companions of 16.95 (our own; NOT publicly listed — research, not portfolio)
* (GC_n) good-count conjecture g(A) ≥ (n−1)!; (OC_n) opposite-chart; "AP cyclic with P in a given
  conjugacy class"; "A + P cyclic for some permutation P" (additive version — small cases decidable
  in hours; might be a nice companion result but it is not on a list).

## B. Permutation / combinatorial problems in the Kourovka Notebook (SAT/exhaustive fit)

### B1. Hamiltonian cycles in Cayley graphs (folklore conjecture; Kourovka has a related entry by
    Kutnar/Marušič-style, number not recalled)
* Statement: every connected Cayley graph on a finite group (order ≥ 3) has a Hamiltonian cycle.
* Status: open; verified for groups of order up to some bound (Kutnar–Marušič–Morris–Morris–Šparl:
  all Cayley graphs on groups of order ≤ 47 (?) and many families).
* First finite reduction: extend the verified bound by one order class with SAT (Hamiltonian cycle
  encoding) — GAP needed to enumerate groups/generating sets (installable self-contained).
* Fit: medium (SAT); novelty: incremental. Effort: 2–3 days. Publishable only as a data note.

### B2. Transversals in Latin squares / Brualdi–Ryser–Stein
* Statement: every n × n Latin square has a partial transversal of size n − 1 (Brualdi); every
  Latin square of odd order has a transversal (Ryser). Status: Brualdi open; large-n asymptotics
  known (Montgomery 2023 proved n − 1 for large n? — verify). Small n verified computationally to
  n ≈ 9–11.
* First finite reduction: n = 10 or 11 exhaustive is a large enumeration (Latin squares of order 11
  are ~10¹⁴ up to isotopy) — probably beyond a 1–3 day budget; EXCLUDE unless a smarter reduction
  exists.

### B3. Kourovka problems on small-group properties (GAP-decidable)
* Family: "does there exist a finite group with property X?" entries (e.g. groups with a given
  automorphism-tower behaviour, Sylow/normaliser conditions, minimal counterexample orders).
  Several such entries have been closed by GAP searches over the SmallGroups library. I cannot cite
  numbers reliably; the scan should filter entries whose statement begins "Does there exist a finite
  group…" or "Is it true that every finite group of order < N …".
* First finite reduction: SmallGroups library up to order 2000 (excluding 1024) — hours.
* Fit: high if GAP is installed; effort 1–2 days per item; novelty depends on the entry.

### B4. Recognition by spectrum (Mazurov's programme; many Kourovka entries)
* Statement: is a given finite simple group G recognisable by its set of element orders ω(G)
  among finite groups? Many specific cases remain (e.g. some L_n(q), unitary groups).
* Status: most alternating/sporadic cases settled; scattered open cases.
* First finite reduction: for a fixed small G, the standard method reduces to checking candidate
  groups with the same spectrum — needs group theory + GAP; heavy on theory. Fit: low–medium.

## C. What I recommend for the first portfolio batch
1. A3 (matrix Waring tables over F_q, small n) — exhaustive, certificate-free, fast, publishable as
   data + conjecture IF the scan confirms the tables are incomplete in the literature.
2. A2 (products of two cyclic matrices over F₂, F₃, n ≤ 4) — one day; publishable if open.
3. B3 (GAP-decidable "does there exist a finite group…" Kourovka entries) — install GAP self-
   contained (~15 min), then each entry is hours; best ratio of "publicly listed open" to effort —
   the scan must supply the exact entry numbers.
4. B1 (Cayley graph Hamiltonicity, next order bound) — only if 1–3 look empty.

## D. Explicitly NOT recommended (methods at their limit or not finite-decidable)
* 16.95 for n ≥ 5 by the case-decomposition (explodes) — only the 48-h uniform-argument budget.
* Ore/Thompson-type conjugacy-class products in large simple groups; recognition-by-spectrum
  families requiring new theory; Brualdi at n ≥ 11.
