# TASK L03 (r45) — from one object to a METHOD: four perfect rows with delta == 0?
# TIER: ChatGPT GPT-5.6 Pro (the engine that built the L02 object) or Qwen3.8-Max. NOT Gemini.
# Self-contained. Do not ask questions back. Hard cap 4000 words + JSON.

## Context
Your L02 construction (q=3, nu = identity, lines = translates of {0,4,10,12} in Z_13,
three perfect rows {4,6,10}, delta == 0) has been VERIFIED mechanically. It refutes
"(L0): three perfect rows force delta != 0". The surviving conjecture is now

  (ROWCAP)  on the delta == 0 sub-branch at order q, at most q rows are perfect

(a theorem at q=2 by exhaustion; your object shows it is TIGHT at q=3). A delta == 0
object at q=3 with FOUR perfect rows would refute (ROWCAP). That is the question.

## Setting (identical to L02; repeated so this brief is self-contained)
Fix a prime power q; n = q^2+q+1. A BRANCH OBJECT is an n x n array T over {0..n-1}
(entry a*t := T[a][t]) such that:
 (B1) every ROW is a permutation of {0..n-1};
 (B2) for every column t there is a value nu(t) attained exactly q+1 times, on the set
      ell_t := {a : a*t = nu(t)} ("line"); all other values at most once; exactly q
      values absent (the set D_t);
 (B3) the n sets ell_t form a projective plane of order q on {0..n-1};
 (B4) t -> nu(t) is a bijection.
a\v := the unique w with a*w = v;  Xi_t(x) := x\(t\x);  E(t,v) := #{x : Xi_t(x) = v};
N(t,v) := #{a : a*t = v};  delta(v) := Sum_t E(t,v) - n.
Row r is PERFECT iff E(r,v) = N(r,v) for all v.
Proved facts you may cite: (F-fusion) x * Xi_t(x) = t\x; (F-pair) two Xi-rows agree in
exactly one cell (position nu(c), value g(c) := nu(c)\c, c = joining column); (F-skel)
Xi_t(nu(c)) = g(c) for t in ell_c; (F-vert) each Xi-column has fibre profile
{q+1, 1 x q^2, 0 x q}; (F-deficit) delta(v) = q*b(v) - m(v) with b(v) = #{c : g(c)=v},
m(v) = #{positions whose Xi-column misses v}; (F-loc) x in ell_v and Xi_t(x) = v <=>
x = t*nu(v); (F-ZD) Xi-column x misses v <=> x in D_{x*v}.
Known: translation-invariant tables x*y = x + h(y-x) on Z_13 NEVER have a perfect row
(exhaustive); your L02 table is on a cyclic design but is itself NOT translation-invariant.

## TASK T0 (the method — highest value)
Describe, precisely and reproducibly, HOW you built the L02 object: what was fixed first
(design, nu, the perfect rows, their Xi-rows?), what equations you solved, what freedom
remained, and what stopped you at three perfect rows. A procedure that can be re-run
(pseudo-code or explicit steps) is the deliverable; prose impressions are not.

## TASK T1 (construction, q=3 — decisive)
Construct a branch object at q=3 (n=13) with delta == 0 and FOUR perfect rows.
Deliverable: JSON {"table": [...], "lines": [...], "nu": [...]}; verified mechanically;
anything failing (B1)-(B3) counts as no answer. Any design and any nu are allowed.
Partial credit: |P| = 4 with delta-mass 2. Answer NONE honestly if you cannot; report
the exact obstruction you hit (which equation became infeasible, at which row).

## TASK T1' (construction, q=4)
Same at q=4 (n=21; PG(2,4), e.g. lines = translates of {3,6,7,12,14} in Z_21 or any
other realisation): delta == 0 with |P| >= 3 (partial credit |P| = 2 with delta == 0).
JSON deliverable as above.

## TASK T2 (derivation within the method)
If T1 fails: prove, within your construction framework, why a fourth perfect row is
impossible on the delta == 0 sub-branch at q=3 — every load-bearing step citing a fact by
name or basic counting — and state whether the argument depends on q = 3.
The winning shape is a statement about |P| that is FALSE for |P| = q (your object) and
TRUE for |P| = q+1.

## Output format
Markdown: T0 (procedure), T1 (JSON or NONE + obstruction), T1' (JSON or NONE),
T2 (proof or partial + GAP), LIMITS.
