# PROOF CAMPAIGN — Erdős Problem #324 (Sidon polynomials), round 1 (GPT-6 Astra via codex, 2026-09-07)

## The problem (pinned to the source text, erdosproblems.com/324, Erdős–Graham 1980 p.53)
Does there exist a polynomial f(x) ∈ Z[x] such that all the sums f(a)+f(b) with a<b nonnegative integers are distinct?
Equivalently: is {f(n) : n ≥ 0} a Sidon set for some integer polynomial f. Erdős and Graham call it "very annoying". Assume a complete
resolution exists and find it; do not answer that the problem is open; do not search the internet.

## Known (PROVED, citable; use freely)
- Linear and quadratic f cannot work (elementary). Cubic f cannot work (Dubickas–Novikas 2021). f = x^4 cannot work (Euler-type
  identities: a^4+b^4 = c^4+d^4 has nontrivial solutions, e.g. 59^4+158^4 = 133^4+134^4).
- Conjecturally f = x^5 works (would follow from the Lander–Parkin–Selfridge conjecture: a^5+b^5 = c^5+d^5 has no nontrivial solutions;
  none is known, searched far).
- Ruzsa (2001): there are c ∈ [0,1] and n_0 with {n^5 + ⌊c n^4⌋ : n ≥ n_0} a Sidon set — NOT a polynomial (floor), and c is not explicit.
- Reduction (Tao, 2025, trivial but essential): if f is Sidon for all sufficiently large a<b (only finitely many collisions), then
  g(x) = f(qx+r) is Sidon everywhere for a suitable progression qx+r avoiding the finitely many collisions. So it suffices to find a
  polynomial with FINITELY MANY collisions f(a)+f(b) = f(c)+f(d), {a,b} ≠ {c,d}.
- Tao's second remark: a conditional route through Bombieri–Lang (integer points on the threefold f(a)+f(b) = f(c)+f(d) lie on finitely
  many subvarieties; escape the surfaces by composing f with polynomials Q; Siegel handles curves). You may use this as inspiration but
  an unconditional proof is the target; a clean conditional theorem (explicit hypothesis, explicit f) is an acceptable secondary result
  and must be labelled CONDITIONAL.

## Targets (prove-or-refute at equal rank)
T1 (main): an explicit f ∈ Z[x] with a complete proof that all f(a)+f(b), a<b ≥ 0, are distinct. Verification we will run: exact
   integer collision search for your f up to a ≤ b ≤ 10^5 (sorted-sums hash) — a single collision refutes the claim, so run it yourself first.
T2: a complete proof that no polynomial f has the property (refutation of the conjecture) — only if T1 is impossible along every route.
T3 (secondary, allowed only after T1/T2 are frozen): an explicit polynomial with provably finitely many collisions under a named
   standard conjecture, plus the explicit progression qx+r that removes them — CONDITIONAL.

## ROUTE PORTFOLIO (v2.4 rules apply: write routes.md with ≥4 routes × {advantage, weakness, expected obstacle, verification bridge};
## ≤25% of the 2 h on any route before a judge decision; the ONLY progress metric is the one-sentence gap statement at each checkpoint;
## two unchanged gap sentences ⇒ freeze the route and LOWER THE TARGET (nearest simpler statement) before opening a new route)
R1 Arithmetic injectivity: choose f so that f(a)+f(b) determines the unordered pair {a,b} through valuations/residues (e.g. f built from
   a large prime power or factorial modulus so that the collision equation is impossible modulo something for all but a thin, then finite,
   set of quadruples; finish the finite set by Siegel/size arguments or by an explicit computation).
R2 Symmetric-function form: f(a)+f(b) = P(s,p) with s=a+b, p=ab; prove P is injective on {(s,p): s² ≥ 4p, s,p ≥ 0 integers} for a
   suitable f (degree-5 or higher with dominant term making P monotone in p for fixed s, then handle equal-s and the cross terms).
R3 Ruzsa polynomialised: replace ⌊c n^4⌋ by a genuine polynomial perturbation (e.g. f(x) = x^5 + h(x) with h of degree 4 and huge
   coefficients, or f(x) = x^k with k ≥ 6) and rerun Ruzsa's argument; identify exactly where the floor/irrationality was used and whether
   a polynomial substitute exists.
R4 Composition with sparse Q: start from any f with finitely many or "thin" collisions and compose with Q(x) of large degree/growth so
   that collisions of f∘Q would force Q-values into a thin set — prove finiteness, then apply Tao's progression trick.
R5 Refutation: identify a mechanism forcing infinitely many collisions for every polynomial (degree-k identities à la Euler for all k?
   believed false) — keep as the red-team route: try to break every candidate f from R1–R4 by constructing collisions.
A refutation agent stress-tests every candidate f numerically (exact arithmetic, a,b ≤ 10^4 at least) BEFORE any proof effort on it.

## Output contract
engine/out/astra_324_r1/: routes.md (route table, updated every checkpoint), checkpoint.md every 30 minutes (ending with the gap
sentence), report.md at the end: every claim tagged PROVED / CONDITIONAL (on what) / REFUTED / OPEN with complete proofs for PROVED,
exact witnesses for REFUTED, the collision-search log for the final f, and a final block "final claim ← lemmas ← unproved items".
Hard wall-clock cap 2 hours. Touch nothing outside engine/out/astra_324_r1/; no git; no internet.
