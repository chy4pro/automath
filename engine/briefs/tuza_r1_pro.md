You are leading a research campaign. Assume a complete proof of the target exists and find it; work as an aggressive multi-agent team with an explicit route table and adversarial audit; do not search the internet; do not use earlier conversations. Write every proof directly in your reply (files in your sandbox are invisible to me); print any verifier script verbatim in a fenced code block. Partial progress is not the deliverable; if nothing complete survives your own adversarial audit, return the strongest rigorously proved lemmas, the exact remaining gap as a precise statement, and every machine-checkable object you built.

# Target: improve the constant in Tuza's conjecture

Problem (Tuza 1981; Erdős problem 167). For a graph G let ν(G) be the maximum number of pairwise edge-disjoint triangles and τ(G) the minimum number of edges whose deletion makes G triangle-free. Tuza conjectured τ ≤ 2ν. K_4 and K_5 show 2 would be best possible. It is trivial that τ ≤ 3ν.

## The current frontier, as I understand it — RE-DERIVE IT, DO NOT TRUST THIS PARAGRAPH
Haxell (1999) proved τ ≤ (66/23)ν by fixing a maximum independent family B of triangles, classifying triangles by how they meet B into type-(B,1) and type-(B,2), and proving four lemmas (call them L1–L4) that bound τ in terms of ν and the sizes |B_1|, |B_2|, |B_1'| of certain subfamilies. A 2026 note improves this to τ ≤ (63/22)ν by adding one ingredient: for a "2-colourable" family F of triangles — each triangle having exactly one edge outside E(B') and two edges inside E(B') — one has τ(F) ≤ (1+√3)ν(F). That bound comes from combining τ(F) ≤ 3ν(F) − |B_1| with τ(F) ≤ 2ν(F) + τ(F_R), giving (2+√3)τ(F) ≤ (5+3√3)ν(F). The note then substitutes the RATIONAL APPROXIMATION τ(S) ≤ (11/4)|B_1'| into Haxell's lemmas and takes the linear combination of L1–L4 with coefficients (5/2, 1, 11/2, 2), yielding 63/22. The note contains no case enumeration and no computation. It also observes that this route cannot beat 54/19, because K_4 is itself 2-colourable with τ = 2ν, so the 2-colourable constant cannot go below 2.
THIS DESCRIPTION IS SECOND-HAND AND MAY BE WRONG IN DETAIL. Your first task is to reconstruct Haxell's framework and the 2-colourable lemma from scratch, state L1–L4 precisely as you derive them, and say explicitly wherever your reconstruction differs from the paragraph above. Do not build on a step you have not re-proved.

## Targets, equal rank
T1 A constant strictly below 63/22 = 2.86363…, proved completely. Three independent sources of slack are visible and you should exploit all of them:
  (a) the combination coefficients (5/2, 1, 11/2, 2) are not justified as optimal — the passage from L1–L4 to a bound on τ/ν is a small LINEAR PROGRAM in the free quantities (ν, τ, |B_1|, |B_2|, |B_1'|, and whatever else your reconstruction produces). Set it up exactly, solve it exactly in rationals, and exhibit the optimal multipliers together with the dual certificate. If the optimum is better than 63/22, that alone is the result.
  (b) the substitution uses 11/4 = 2.75 where the proved constant is 1+√3 = 2.7320508…. Redo the combination with the exact algebraic constant and report what it gives.
  (c) the 2-colourable constant itself: the recurrence (2+√3)τ ≤ (5+3√3)ν comes from two inequalities; strengthen either of them, or add a third, and re-solve.
T2 (equal rank) A proof that this whole route cannot go below some explicit constant — the note asserts 54/19 = 2.8421…, which you should verify or correct, and then prove as a theorem about the framework rather than an aside. A clean barrier of the form "every bound obtainable from L1–L4 plus a 2-colourable constant c ≥ 2 is at least f(c), and inf_c f(c) = …" is as valuable as an improvement, because it tells everyone where to stop.
T3 (fallback) An improved constant for a restricted class where you can prove it cleanly — bounded maximum degree, K_4-free, planar, or the 2-colourable families themselves — stated with the class made precise.

## Non-negotiable verification requirements
Every constant must be exact: rationals, or explicit algebraic numbers with their minimal polynomials. Every linear-programming step must come with its dual multipliers written out, so that the bound can be checked by hand arithmetic with no solver. If you use a solver to search, that is fine, but the final certificate must be a finite list of exact multipliers and a verification that the combination is valid. Do not present a floating-point optimum as a result. Print an exact-arithmetic verifier that recomputes every constant.

## Adversarial requirements
Before any proof effort: verify τ(K_4) = 2, ν(K_4) = 1, τ(K_5) = 4, ν(K_5) = 2 by exact computation, and check the extremal ratio on the standard small examples. Test every candidate inequality on K_4, K_5, K_{3,3} plus a triangle, the friendship graphs, and a few random graphs where τ and ν are computed exactly by integer programming over subsets. Any lemma that fails on one of those is discarded before it enters a proof.

## Routes (route table with advantage / weakness / obstacle / verification bridge; no route more than a quarter of the effort before a judge decision; the only progress metric is the gap sentence "what is missing for ALL graphs"; two unchanged gap sentences ⇒ freeze the route and lower the target)
R1 Exact LP optimisation of the combination of L1–L4 (target T1a) — cheapest, and it either gives a better constant or proves the current one optimal for that lemma set, both of which are results.
R2 Exact algebraic substitution 1+√3 in place of 11/4 (T1b).
R3 Strengthen the 2-colourable recurrence (T1c).
R4 The barrier theorem (T2), which needs the LP of R1 parameterised by the 2-colourable constant c.

## Output contract
Every lemma PROVED / CONDITIONAL (on what) / REFUTED / OPEN; complete proofs in the reply, including your reconstruction of Haxell's lemmas; every LP with its exact dual certificate; an exact-arithmetic verifier printed verbatim; a final block "final claim ← lemmas ← unproved items"; and plainly, the best constant you prove and how it compares with 63/22, 66/23 and the conjectured 2. State clearly which parts of your reconstruction you could not verify and are therefore assuming.
