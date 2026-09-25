# BUILT FROM OWNER ROUND 3 — line zc1a7 (ZC1 for A_7), brief A
**Self-contained. Nothing is withheld, including my own known defects and the places I am stuck.**
**"I could not finish, and here is exactly where I stopped" is a VALUED answer — preferred over a
confident wrong one. Say plainly which of my claims you could not check.**

## 0. The one question
Let G = A_7 and let u be a hypothetical torsion unit of V(ZG) of order 4 whose only non-vanishing
partial augmentations are eps_{2a}(u) = 2, eps_{4a}(u) = -1. This is the unique open case of the
first Zassenhaus Conjecture (ZC1) for A_7 (Baechle-Margolis, arXiv:2006.09031, Indian J. Pure Appl.
Math. 52 (2021) 669-686; their closing words: "We are not aware of an argument which could show that
u does not exist in ZG").
**QUESTION: produce a 2-local argument that rules u out — i.e. one that works when the 2'-part of u
is trivial — or show precisely why the known 2-local machinery cannot.**

## 1. Facts I have PROVED by computation (you may use them; flag any you think is wrong)
- A_7 classes: 1a,2a,3a,3b,4a,5a,6a,7a,7b, sizes 1,105,70,280,630,504,210,360,360.
- HeLP over the COMPLETE admissible system (9 ordinary + all 6 three-modular + all 8 five-modular +
  all 7 seven-modular irreducible Brauer characters; p=2 is INADMISSIBLE for |u|=4 by Hertweck's
  hypothesis p does not divide |u|) leaves EXACTLY {(eps_2a,eps_4a) = (0,1) trivial, (2,-1) open}.
  I computed the full modular tables myself with a from-scratch MeatAxe; completeness certified by
  Brauer's and Berman's counts. **HeLP is therefore provably EXHAUSTED on A_7.**
- u^2 is rationally conjugate to an element of 2a (MRSW), but the paper proves u^2 is NOT conjugate
  in Z_2 G to a trivial unit.
- Eigenvalue multiplicities of u at (2,-1), mu = (mu(1), mu(i), mu(-1), mu(-i)):
   deg 1 : (1,0,0,0)      deg 6 : (4,1,0,1)      deg 10 (x2): (0,3,4,3)
   (the remaining ordinary degrees are 14,14,15,21,35; I can supply them, but the two rows above
   are the tight ones: mu(1)=0 on BOTH degree-10 characters; mu(-1)=0 on degrees 1 and 6.)
- A_7's Sylow 2-subgroup is dihedral of order 8. There are no 2-blocks of defect 0.

## 2. What I have RULED OUT, with the reason (do not re-walk these)
(a) **Eisele-Margolis, "Units in group rings and blocks of Klein four or dihedral defect"
    (arXiv:2412.09525, Bull. LMS 2025)** — the only new p=2 lattice technology, aimed at exactly
    dihedral-defect-8 blocks. It describes the part of the block on which the NON-TRIVIAL 2'-part of
    the unit acts. An order-4 unit has trivial 2'-part. Structurally blind to this case.
(b) **Cliff-Weiss inequalities (Margolis-del Rio, J. Algebra 507 (2018) 78-101, arXiv:1706.02483)** —
    the strongest known strengthening of HeLP. Read at source: they are stated for u in V(ZG,N) with
    N a NILPOTENT NORMAL subgroup, and their extra strength comes from the matrix strategy
    Phi: ZG -> M_k(ZN), k = [G:N]. A_7 is simple, so N = 1 and V(ZG,N) = 1: vacuous.
    Moreover I computed that the "global" inequality of that paper, <chi_alpha, psi> >= 0 for the
    double-action character chi_alpha(u^i,h) = |C_G(h)| eps_h(u^i), evaluated against psi = lambda_j
    (x) theta, equals EXACTLY the HeLP multiplicity mu(zeta^{-j}, u, theta). So for N = G the
    Cliff-Weiss inequalities COLLAPSE TO HeLP.  **Please check this collapse claim independently.**
(c) The degree-10 tight rows do NOT give the paper's degree-6 lattice contradiction: the {i,-i} pair
    occurs three times there (once in degree 6), forcing >= 4 indecomposable summands - less rigid.

## 3. The specific technical claim I want checked, and possibly beaten
Write z = ubar - 1 acting on Lbar = L/2L for a Z_2 G-lattice L; r_j(Lbar) = rank_{F_2}(z^j | Lbar).
Note z^2 = ubar^2 - 1 in characteristic 2.
- **(UPPER)** Using Berman-Gudkov (an indecomposable Z_2 C_4-lattice contains each of the three
  simple Z_2 C_4-modules -- trivial, sign, and the 2-dimensional one with eigenvalues i,-i -- at most
  once as a composition factor; Curtis-Reiner Section 34C):
      r_2(Lbar) <= min(mu(1), mu(i)) + min(mu(-1), mu(i)).
  Sanity: degree 6 gives min(4,1)+min(0,1) = 1, exactly the paper's own bound (a genuine element of
  2a gives 2 there), so this reproduces their argument.
- **(LOWER)** If 0 -> A -> V -> B -> 0 of F_2<ubar>-modules then rank(z^j|V) >= rank(z^j|A) +
  rank(z^j|B). Hence r_j(Lbar_chi) >= sum_S d_{chi,S} r_j(S), d = 2-modular decomposition matrix,
  S running over the six 2-modular simples of A_7 (degrees 1,4,4,6,14,20). Crucially r_j(S) is
  well-defined per isomorphism type, because ubar is ONE element of F_2 A_7.
- **MY PROBLEM**: the lattice side gives only UPPER bounds on r_2 and the composition-factor side
  only LOWER bounds with unknowns r_j(S) >= 0, so r_j(S) = 0 for all S satisfies everything and the
  system is trivially feasible. **A contradiction needs a nonzero LOWER bound on r_2(S) for some
  2-modular simple S, or a genuinely different invariant.** I have not found one.
  I can prove only: ubar^2 != 1 in F_2 A_7 (if ubar^2 = 1 then u^2 = 1 - 2e for an idempotent e, and
  eps_{2a}(u^2) = 1 forces eps_{2a}(e) = -1/2, not an integer).
**TASK 3.1** Is there an invariant of the F_2 A_7-module Lbar, or of the element ubar in F_2 A_7,
that is bounded BELOW by the Z_2 C_4-lattice structure and ABOVE by the composition factors (i.e. the
opposite direction to mine)? Socle/radical layers, vertices and sources, Green correspondence,
Scott modules, the Brauer construction / Brauer homomorphism at a subgroup of the Sylow D_8?
**TASK 3.2** Hertweck's A_6 argument gets its lower bound by splitting L with the idempotent
(1+u^3)/2 coming from the 2'-part of a unit of order 6. With |u| = 4 the p'-part is trivial and there
is NO such idempotent. Is there a substitute -- e.g. splitting by a central idempotent of Z_2 A_7
(the 2-block decomposition), or by an idempotent of the endomorphism ring?

## 4. Other angles you may prefer
- The refuting branch: a unit u in ZA_7 with u^4 = 1 and these partial augmentations is 2520 integer
  coefficients satisfying a quartic system, additionally forced to satisfy 13 tightness conditions
  (mu = 0) and the 2-adic obstruction above. Is there a structural reason it cannot exist -- or a
  construction? Eisele-Margolis (Rev. Mat. Complut. 2024) built a 3- and 5-LOCAL counterexample to
  ZC1 inside V(Z_{(3,5)} PSL(2,16)) and wrote that they hope their methods lead to a global
  counterexample among simple groups, so the refuting branch is not obviously hopeless.
- Weiss's theorem (permutation lattices) applied to Z_2 A_7 as a Z_2<u>-lattice. I know
  ZG free over Z_2<u> would give u conjugate to a group element in Z_2 G; and Hertweck's
  Lemma 2.2 already forbids that, since eps is nonzero on the two DIFFERENT classes 2a and 4a whose
  2-parts are not G-conjugate. So Z_2 A_7 is NOT Z_2<u>-free. Does that non-freeness have a
  quantitative consequence I am missing?

## 5. Rules
- **Exact arithmetic only.** No SAT, no brute-force search over 2520 coefficients.
- **State every hypothesis you use and where it comes from.** If you invoke a theorem, name it and
  give the reference. If you are unsure a theorem says what you need, SAY SO.
- **Do not assert a number you have not computed.**
- Answer in at most 1800 words. Structure: (1) verdict on my claim (2)(b) collapse; (2) verdict on
  3.1/3.2; (3) the single most promising concrete next step and why; (4) exactly where you stopped.
