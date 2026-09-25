# BUILT FROM OWNER ROUND 3 — line zc1a7 (ZC1 for A_7), brief B — LITERATURE / TECHNIQUE CENSUS
**Self-contained. Nothing withheld, including my own defects.**
**"I could not finish, and here is exactly where I stopped" is a VALUED answer.**
**Do NOT invent references. If you are not sure a paper exists, say "I am not sure this exists".
A fabricated citation is worse than no answer, because it costs me a round to disprove.**

## 0. The one question
**Name every technique in the literature on torsion units of integral group rings that can rule out a
torsion unit u of V(ZG) of PRIME-POWER order p^n in a group G where the HeLP / Luthar-Passi method
is not sufficient — and say, for each, whether it needs any of the following, because A_7 has NONE
of them:**
   (i) a non-trivial p'-part of u  (our u has order 4, p = 2, so its 2'-part is trivial);
   (ii) a non-trivial normal subgroup of G  (A_7 is simple);
   (iii) a cyclic Sylow p-subgroup / a block of defect 1  (A_7's Sylow 2 is dihedral of order 8,
         defect 3; A_7 has NO 2-block of defect 0);
   (iv) G solvable, supersolvable, nilpotent, metabelian, cyclic-by-abelian, or Frobenius.

## 1. The concrete case, so you can judge relevance
G = A_7. u in V(ZG) of order 4, non-vanishing partial augmentations exactly eps_{2a}(u) = 2,
eps_{4a}(u) = -1. This is the unique open case of ZC1 for A_7 (Baechle-Margolis, arXiv:2006.09031;
published Indian J. Pure Appl. Math. 52 (2021) 669-686), whose last line before "Problem: Prove that
(ZC1) holds for A_7" is "We are not aware of an argument which could show that u does not exist".
u^2 is rationally conjugate to 2a but is NOT conjugate in Z_2 G to a trivial unit.

## 2. What I have ALREADY checked myself — do not repeat, but DO tell me if I am wrong
- **HeLP is exhausted.** I computed the complete 3-, 5- and 7-modular Brauer character tables of A_7
  from scratch and ran HeLP over the complete admissible system (p = 2 is inadmissible for a unit of
  order 4 by Hertweck's hypothesis). (2,-1) survives all 40 constraints that can discriminate it.
- **Eisele-Margolis, arXiv:2412.09525 / Bull. LMS 2025** (Klein four or dihedral defect, the only new
  p = 2 lattice technology): works through the non-trivial 2'-part of the unit. Blind to our case.
- **Cliff-Weiss inequalities, Margolis-del Rio, J. Algebra 507 (2018), arXiv:1706.02483**: stated for
  V(ZG,N), N a nilpotent normal subgroup; A_7 simple => vacuous. I also computed that with N = G the
  "global" inequality collapses to HeLP exactly.
- **Margolis, "A theorem of Hertweck on p-adic conjugacy of p-torsion units in group rings"
  (arXiv:1706.02117)**: needs N a normal p-subgroup. A_7 simple => vacuous.
- **Caicedo-Margolis, blocks of defect 1**: needs Sylow of order p. Handles A_7 at p = 5, 7 (already
  done in the 2020 paper); our open case is at p = 2, defect 3.
- **Hertweck's lattice method as used for A_6**: splits the lattice with the idempotent (1+u^3)/2
  coming from the 2'-part of a unit of order 6. With |u| = 4 there is no such idempotent.
- Literature verdict from my round 1: ZC1 for A_7 is OPEN as of 2026. The Eisele-Margolis 2025
  introduction says PSL(2,p^f) "include the ONLY non-abelian simple groups for which the Zassenhaus
  conjecture is known to hold"; A_7 is not of that form.

## 3. What I specifically want from you
**3.1** Techniques I may not know. Candidates to assess (add others): Weiss's theorem on permutation
lattices (J. reine angew. Math. 415 (1991) / Ann. of Math. 1988); Roggenkamp-Scott and the "double
action" formalism; Scott's "On a conjecture of Zassenhaus, and beyond"; Bleher-Hiss-Kimmerle
autoequivalences of blocks; Herman-Singh reality-based algebras / extensions of coefficients (the
"F-conjugacy" / Q(zeta)-coefficient strengthening of HeLP); Bovdi-Maroti, "On partial augmentations of
elements in integral group rings" (2023); Margolis-del Rio, "Partial augmentations power property"
(2019); Bovdi-Breuer-Maroti, "Finite simple groups with short Galois orbits on conjugacy classes"
(2020); Kimmerle-Konovalov Gruenberg-Kegel graph work; anything using Green correspondence, vertices
and sources, or the Brauer construction on the double-action module.
For EACH: does it need (i)-(iv) above? One sentence each is enough. Say "I do not know" freely.
**3.2** Is there ANY published instance of ZC1 being settled for a unit of prime-power order p^n
(n >= 2) in a NON-SOLVABLE group by a method other than HeLP? If yes, which paper, which group, and
what was the mechanism? This is the single most valuable thing you could tell me.
**3.3** Is there a published statement of the classification of indecomposable Z_2 C_4-lattices with
their reductions mod 2 (Berman-Gudkov 1964; Curtis-Reiner Section 34C)? How many indecomposables are
there, and what are their mod-2 Jordan types? I need this to be exact, not approximate; if you are
not certain, say so rather than guessing a number.

## 4. Rules
- **Never fabricate a citation.** Mark anything you are unsure of with "UNVERIFIED".
- Do not restate my own findings back to me.
- At most 1500 words. End with a section "WHERE I STOPPED" naming what you could not check.
