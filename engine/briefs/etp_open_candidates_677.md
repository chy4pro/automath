# ETP open-implication candidates and transferable targets — from line-677's own knowledge
# (knowledge cutoff January 2026; NOTHING here is verified against the live ETP repository —
# every item carries a confidence tag and MUST be checked by the with-internet SCAN before any
# dispatch). Written 2026-08-30 on the owner's portfolio decision.

## 0. What our 677 machinery actually is (for transfer decisions)
(a) Exact small-order search with certificates: one-hot CNF encoders for a magma table + an
    identity (E677-style aux chains), canonical generation-order symmetry breaking for
    one-generated magmas (MONO2/3), cube-and-conquer with per-cube DRAT, proof-keeping cloud
    runners (kissat + drat-trim on the VM), Lean import of small UNSAT facts via bv_decide.
(b) Quotient/extension structure: pair-indexed extensions of a base magma by a fibre, the
    "gauge-free local core" method (fibre transport, lifted instances as permutation systems,
    UNSAT ⟹ no congruence class of that size), Lean modules for E677 (Ext677*).
(c) Construct-and-verify: switching/twisted products over affine bases, exhaustive parametric
    families (EPRIME-style census), independent multi-family verification.
(d) Group-action row templates (two-sided x*y = a_x y b_x⁻¹ over a group; orbit cubes).
Transfers best to: "does finite identity P imply identity Q" questions with small-order
decidability, existence of small algebraic structures with prescribed identities, and
"minimal counterexample is simple / has no small congruence" style reductions for any left- or
right-cancellative variety.

## 1. Equational Theories Project (ETP, 4694 equations on one binary operation) — open items I know
E1 **677 ⟹ 255 (finite magmas)** — our line. Status per my knowledge: OPEN; the infinite
   implication is FALSE (greedy/free constructions); the finite case is the flagship remaining
   "finite implication" of the project. [confidence: HIGH that it was open as of late 2025]
E2 **1485 ⟹ 151 (finite magmas)** — the other famous finite implication ("Austin pair"
   candidate: true for finite magmas, false for infinite). My recollection: it was PROVED for
   finite magmas in 2025 (a slick argument via left-cancellativity / a counting invariant),
   making it the first confirmed Austin pair; 677 ⟹ 255 would be the second. [confidence:
   MEDIUM — must be checked; if still open it is the top transfer target: same shape as ours]
E3 The rest of the 4694² implication table: as far as I know, ALL general (infinite-allowed)
   implications were resolved by early 2025 (the last ones — "Asterix" 65 ⟹ 4380?, "Obelix"
   1491 ⟹ 3456?, "Dupont", "Eq 1323/2744"-type — were closed by explicit constructions);
   the finite table: all but E1 (and possibly E2) resolved. [confidence: MEDIUM on the exact
   equation numbers; HIGH that only one or two finite implications remained]
E4 ETP "phase 2"-type follow-ups I recall being discussed (candidates only, each may already be
   done): (i) implications between laws in TWO operations / with a constant; (ii) the same
   table for COMMUTATIVE magmas or for magmas with a 2-sided unit; (iii) "how many equations of
   size ≤ n define the same theory" (Kisielewicz-style counting); (iv) decidability/strength
   of single laws (e.g. laws equivalent to associativity; "is law X's theory decidable");
   (v) magma laws with n variables of length ≤ k beyond the original 4694 (size-5 or 6 terms)
   — a natural, SAT-heavy, publicly listed extension. [confidence: LOW–MEDIUM]

## 2. Adjacent problems where the machinery transfers directly (my knowledge; verify)
T1 Finite vs. infinite for other single-law implications outside the original ETP list
   (larger terms): the systematic question "is P ⟹ Q an Austin pair" — our gauge-free core
   method (no congruence class of small size in a minimal finite counterexample) applies to
   any law that makes left translations bijective (E677 gives that; many "x = y(…)" laws do).
T2 Quasigroup / Latin-square identity problems decidable at small orders (CSPLib QG series:
   QG1–QG7 idempotent quasigroups with identities such as (xy)(yx) = x, (xy)y = x(xy), …):
   most small orders are known; the OPEN frontier orders (typically 17–25 for the harder
   identities) are exactly SAT+DRAT territory but may need days–weeks. [confidence: MEDIUM]
T3 Existence of small Moufang / Bol / Bruck loops and Steiner-type systems with a prescribed
   extra identity — mostly enumerated up to modest orders; open cases are large. [LOW value]
T4 Kourovka-Notebook items with small-case decidability (k1695 is one); other Kourovka items on
   finite groups/loops that reduce to finite searches (e.g. questions on quasigroup
   automorphisms, n-ary quasigroups) — needs the scan to pick concrete numbers. [LOW–MEDIUM]
T5 "Higman–Neumann" / "single-law bases" questions: which short laws are single axioms for
   groups/abelian groups/loops; some finite-model-decidable sub-questions; classical, mostly
   settled by ATP (McCune–Kunen–…); leftover small cases could be quick wins. [MEDIUM]
T6 The ETP's own "finite magma census" side questions: numbers of magmas of small order
   satisfying a given law up to isomorphism (OEIS-style sequences) — computable, publishable as
   data, low mathematical value unless a law's sequence is requested on a public list. [LOW]

## 3. What I would NOT recommend
- Any target that is not on a public list with a clear open status (the novelty gate fails).
- Targets whose open frontier is a single huge SAT instance (weeks): our credit (≈ $39) and
  the 1–3-day criterion exclude them.

## 4. Suggested triage for the SCAN (with internet)
1. Confirm E1/E2 status on the ETP repository/Zulip (dated). If 1485 ⟹ 151 (finite) is still
   open, it is the single best transfer: same machinery, same reductions (start with: minimal
   counterexample structure via pair-indexed extensions; small-order exhaustion; the
   left-translation structure of 1485).
2. Pull the ETP's list of "implications that were resolved only by large/non-obvious
   constructions" — those with finite counterexamples of order ≥ 12 are natural sharpness or
   uniqueness questions (e.g. "smallest finite counterexample to P ⟹ Q": exact decisions at
   the frontier order are 1–3-day SAT items and publishable as short notes/OEIS entries).
3. CSPLib QG frontier orders (T2) as a fallback with clear public status.
