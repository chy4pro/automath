# ATTACK — Erdős Problem #835 via Steiner systems (single-shot variant, TEMPLATE v2.2)

## The problem
Let J(2k,k) be the Johnson graph: vertices are the k-subsets of [2k] = {1,...,2k}, two adjacent iff they
share exactly k-1 elements. Prove that there exists k > 2 with chromatic number χ(J(2k,k)) = k+1, by
exhibiting such a k and an explicit (k+1)-colouring — OR prove that no such k exists.

## Known givens — PROVED; use freely, re-derive if you prefer
G1 (Erdős–Rosenfeld) k+1 <= χ(J(2k,k)) <= 2k for all k >= 2; equality k+1 holds for k = 2.
G2 (computed) χ(J(2k,k)) > k+1 for 3 <= k <= 8.
G3 (Ma–Tang 2025) If χ(J(2k,k)) = k+1 then t | C(k+t, t-1) for every 1 <= t <= k; by Lucas' theorem this
   fails whenever k+1 is composite. When k+1 = p is prime ALL these divisibilities hold, so the counting
   argument cannot decide the case k = p-1. First open case: k = 10, J(20,10), 184,756 vertices.
G4 (exact reformulation, proved by double counting + complementation) χ(J(2k,k)) = k+1 iff the k-subsets of
   [2k] can be partitioned into k+1 families each of which meets every (k+1)-subset in exactly one member;
   taking complements, iff the k-subsets of [2k] partition into k+1 Steiner systems S(k-1, k, 2k), i.e. a
   LARGE SET LS(k-1, k, 2k) exists. Each class has exactly C(2k,k)/(k+1) = Catalan(k) members.
G5 Consequences: k=3 fails since S(2,3,6) does not exist; k=4: S(3,4,8) exists (extended Hamming code /
   SQS(8)) but no 5 pairwise disjoint copies; k=6: S(5,6,12) exists (extended ternary Golay code / small
   Witt design) but no 7 pairwise disjoint copies. For k = 10 a positive answer requires an S(9,10,20)
   (16,796 blocks); no Steiner system S(t,k,v) with t >= 6 is currently known to exist, and the two known
   members of the family S(t,t+1,2t+2) (t = 3, 5) both come from perfect codes, which are classified.
G6 All integrality conditions for S(9,10,20) hold: C(20-i, 9-i)/(10-i) is an integer for i = 0..9
   (16796, 8398, 3978, 1768, 728, 273, 91, 26, 6, 1).

## Current task statement
Give a rigorous standalone resolution using your own knowledge, computation, and reasoning, without
searching the public web, connected sources, previous conversations, or project contexts. Assume for
purposes of this task that a complete resolution exists and can be found. Work iteratively until it is
reached. Human experts consider the t >= 6 Steiner question hard; that is not evidence that it cannot be
done here — treat every "well-known difficulty" as a claim to be tested, not a wall.

Partial progress does not count unless it implies exactly the resolution of the entire statement.
Restating G1–G6 is not progress. Bounded verification is insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) algebraic construction of S(9,10,20) and of a large set of them: identify [20] with a structure
      carrying an action of a group of order divisible by 11 (e.g. PSL(2,19) on the projective line
      over F_19, or Z_19 ∪ {∞}, or 2×F_10-like structures) and look for orbit unions of 10-subsets
      forming a Steiner system; then use a group element of order 11 acting on the systems to produce
      11 disjoint copies (the classical trick that produces large sets from a cyclic automorphism);
  (ii) code-theoretic: search for a length-20 code (binary or over F_4/F_5) whose weight-10 words form an
      S(9,10,20), analogous to Golay/Hamming; prove or disprove existence via the Assmus–Mattson theorem
      and weight-enumerator constraints;
  (iii) impossibility: derive a NEW necessary condition beyond counting — e.g. via the Delsarte LP bound
      or eigenvalue (Hoffman) structure of independent sets attaining C(2k,k)/(k+1) in J(2k,k), via
      derived/residual designs of a putative S(9,10,20) (the derived design S(8,9,19), residual, etc.,
      each must satisfy its own integrality and known nonexistence results), or via the Fisher-type
      inequalities for t-designs (Ray-Chaudhuri–Wilson);
  (iv) intersection-number analysis: the block intersection numbers of an S(9,10,20) are forced; compute
      them (Mendelsohn equations) and test for a contradiction, then do the same for a large set;
  (v) prove a general theorem: S(t, t+1, 2t+2) exists only for t in {1, 3, 5}, or find the mechanism that
      produces t = 9.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: every candidate Steiner system must be checked block-by-block (every
  9-subset in exactly one block); every impossibility argument checked for hidden assumptions.
- Require concrete objects, equations and inequalities — not plans.
- Do not stop after the first wave fails.

Return a complete resolution if one survives adversarial audit. If none does, return instead: (1) the
strongest rigorously proved derivation you reached, as numbered lemmas — e.g. the forced intersection
numbers of S(9,10,20), a proved nonexistence for some k = p-1, or an explicit partial design with its
exact deficiency; (2) the exact remaining gap as a precise open statement; (3) every machine-checkable
artefact you built (explicit block lists, weight enumerators, orbit descriptions) so it can be re-run and
reused. Do not return an empty answer, a bare statement of failure, a status report, or an explanation
of why the problem is hard. Do not search the web to determine whether the statement is open, and do not
answer that it is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; any construction given as an explicit
block list or generating group + base blocks so a script can verify the Steiner property; what a Lean
formalisation needs; every finite computation stated so it can be re-run. A check that cannot fail
counts as no check.
