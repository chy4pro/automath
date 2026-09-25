# Computational attack task: Kourovka Notebook Problem 19.25

Problem (Curtin & Pourgholi, Kourovka Notebook 19.25): Let G and H be finite
groups of the same order with sum_{g in G} phi(|g|) = sum_{h in H} phi(|h|),
where phi is Euler's totient and |g| the element order. If G is simple, must
H be simple?

Useful reformulation (verify it first): sum_g phi(ord g) = sum over cyclic
subgroups C of phi(|C|)^2, since each cyclic subgroup of order d has phi(d)
generators each contributing phi(d).

Your task: hunt for a COUNTEREXAMPLE computationally, and/or prove partial
positive results. Plan:
1. For each nonabelian simple group order up to a feasible bound
   (60, 168, 360, 504, 660, 1092, 2448, 2520(A7)...): compute the invariant
   T(G) = sum_g phi(ord g) for the simple group(s) of that order.
2. Enumerate OTHER groups of the same order and compute T. A full group
   enumeration needs care without GAP: for order 60 the classification is
   known (13 groups; list them explicitly as direct/semidirect products and
   construct each as permutation groups or via generators in python).
   For orders where full enumeration is infeasible, generate large families
   (abelian, dihedral-like, C_n semidirect products, direct products of
   smaller groups) — a counterexample just needs ONE matching non-simple H.
3. Also think structurally: T(G) is determined by the element-order
   distribution. Are there known "same order spectrum" pairs (simple vs
   non-simple)? Note T is coarser than the order spectrum — matching T is
   EASIER than matching the full spectrum, which helps the hunt.
4. You may install nothing system-wide; pure python3 only
   ($HOME/workspace/claudecode/automath/.venv/bin/python has sympy).
   Permutation group closure code is fine for these orders.

If no counterexample emerges in feasible ranges, report exactly what was
covered (orders, families) and any structural observations (e.g. lower
bounds on T for simple groups). Absolute honesty about coverage. Write
everything to notes/reviews/kourovka1925_codex_work.md. Do not search the
internet.
