# Common brief: finite 677 vs 255 (single-explorer adaptation of the CDC scaffold)

Definitions (magma (M, *), all quantifiers over M):
  E255:  x = ((x*x)*x)*x
  E677:  x = y*(x*((y*x)*y))
Question: does every FINITE magma satisfying E677 also satisfy E255?
Either outcome resolves it: a finite counterexample table, or a proof of the
finite implication. Assume for purposes of this task that a clean resolution
exists and is findable. Work toward the COMPLETE resolution; partial progress
does not count unless it implies the full resolution. Reductions to statements
equivalent in strength to the original question are not progress unless you
supply a genuinely new proof of that statement.

Known facts you may use (all verified):
1. In any 677-magma, every left translation L_y : z -> y*z is surjective
   (x = y*(...) for all x); hence bijective when finite. So finite 677-magmas
   are left quasigroups: each row of the Cayley table is a permutation.
2. Exhaustive/SAT search: no counterexample of order <= 7 (our runs); community
   claims (unreviewed, DRAT certificates) none of order <= 10; an order-11
   near-miss satisfies 677 in 91/121 instances while violating 255.
3. Linear models a*b = f(a)+g(b) over abelian groups, and their linear
   extensions, are forced to satisfy 255 (ETP blueprint). So counterexamples,
   if any, are essentially non-linear.
4. There IS an infinite 677-magma violating 255 (greedy construction,
   inherently infinite). The free 677-magma on one generator violates 255.
5. E677 is dual/mirror-equivalent to "E2910 vs E47" — you may work in either
   form but state which.

Discipline: do not search the internet. Return concrete lemmas, constructions,
equations, or counterexamples to proposed sublemmas — no status reports, no
vague optimism, no "routine" claims. If an approach stalls at a
theorem-strength missing lemma, name that lemma precisely and switch to a
materially different mechanism within your family. Persist through at least
three structurally different attempts within your family before concluding.
Your final report: strongest rigorously proved statements + exact remaining
gap + the single most promising continuation.
