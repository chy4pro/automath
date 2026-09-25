# TASK K3-ADV — adversarial attack on a claimed theorem (self-contained; no repo needed)

Your job is to BREAK the claim below, or to fail honestly trying. Do not write a review that
says it looks correct. Either produce a concrete counterexample, or name a specific inference
step that does not follow and say why. Build things and run them; do not adjudicate by prose.

Write your report to
`$HOME/workspace/claudecode/automath/engine/out/codex/k1695_n3_adversarial.md`
and end it with the literal token DONE-K3-ADV.

## Definitions
F is an arbitrary field, F̄ its algebraic closure. M ∈ M_n(F) is CYCLIC (= nonderogatory) iff
its minimal polynomial equals its characteristic polynomial, equivalently
dim ker(M − λI) ≤ 1 for every λ ∈ F̄. P_π is the permutation matrix with P_π e_j = e_{π(j)};
A P_π permutes the columns of A.

## THE CLAIM (Kourovka 16.95 for n = 3)
> For every field F and every A ∈ GL(3,F) there is a permutation matrix P with AP cyclic.

## THE PROOF I AM ASKING YOU TO BREAK
**Lemma 0.** For X ∈ M_n(F̄), u,w ∈ F̄^n, K = ker X:
`nullity(X + u wᵀ) = dim(K ∩ wᵀ⊥) + ε`, where ε = 1 iff ∃x with Xx = −u and wᵀx = 1, else 0.

**Step 1.** If A is cyclic take P = I. Otherwise some λ ∈ F̄ has dim ker(A−λI) ≥ 2.

**Step 2.** That λ lies in F: geometric multiplicity is Galois-stable, so each of the
[F(λ):F] = d conjugates of λ has algebraic multiplicity ≥ 2, giving 2d ≤ 3, so d = 1.
Hence rank(A − λI) ≤ 1 and λ ≠ 0 (A is invertible), so A = λ(I + u vᵀ) for some u,v ∈ F³.
Cyclicity of AP is scaling-invariant, so assume A = I + u vᵀ, invertible iff 1 + vᵀu ≠ 0.
If u = 0 or v = 0 then A = I and any 3-cycle P gives AP = P, the companion matrix of x³−1,
which is cyclic. So assume u,v ≠ 0.

**Step 3 (criterion for a transposition).** Let π = (i j) with fixed point k, and
M = A P_π = P_π + u wᵀ with w_t = v_{π(t)}. Since spec(P_π) ⊆ {1,−1}, Lemma 0 says only
λ = ±1 can give nullity ≥ 2. Then M is NOT cyclic if and only if (T1) or (T2) holds:
 (T1) [S_v = 0 and v_k = 0] or [S_u = 0 and u_k = 0];      (failure at λ = 1)
 (T2) char F ≠ 2, u_i = u_j, v_i = v_j, and u_i v_i + u_k v_k / 2 = −1.  (failure at λ = −1)
 (Here S_u = u_1+u_2+u_3, S_v = v_1+v_2+v_3.)

**Step 4 (case analysis).** Suppose all six permutations fail. Note that if u ≠ 0 and S_u = 0
then at most one coordinate of u vanishes.
- **S_u ≠ 0 and S_v ≠ 0.** (T1) is impossible, so all three transpositions fail by (T2);
  running (T2) for k = 1,2,3 forces u = a·1 and v = b·1 with a,b ≠ 0, and 3ab/2 = −1, so
  char ∉ {2,3} and ab = −2/3. Then take a 3-cycle: at λ = 1 clause (ii) reads 3a ≠ 0, so
  λ = 1 is not a failure; at a primitive cube root of unity ω the two eigenvector clauses do
  vanish (Σ_i ω^i = 0) but the third quantity is α = ab(3ω²+2ω+1) = −ab(2+ω), and α = 1 would
  give (−2/3)(2+ω) = −1, i.e. ω = −1/2, whence ω³ = 1 forces 9 = 0, i.e. char = 3 — excluded.
  So the 3-cycle works. Contradiction.
- **S_u = 0, S_v ≠ 0.** (T1) can only fire via u_k = 0, for at most one k, so at least two
  transpositions fail by (T2), which forces u = a·1, v = b·1 with a ≠ 0; then S_u = 3a = 0
  gives char = 3, hence S_v = 3b = 0, contradicting S_v ≠ 0.
- **S_u ≠ 0, S_v = 0.** Symmetric: two (T2) failures force u = a·1, v = b·1; S_u = 3a ≠ 0
  gives char ≠ 3, so S_v = 3b = 0 forces b = 0, i.e. v = 0 — excluded.
- **S_u = S_v = 0.** (T1) for k reduces to [u_k = 0 or v_k = 0]; u and v each have at most one
  zero coordinate, so some k escapes (T1). If two such k exist, (T2) at both forces
  u = a·1, v = b·1, so 3a = 0 with a ≠ 0, i.e. char = 3, and then (T2)'s equation reads
  3ab/2 = 0 = −1, false — so that transposition works. If exactly one such k exists, the other
  two indices each kill u or kill v; since u and v each have a single zero coordinate, one
  index kills u and the other kills v, so the pair {i,j} moved by the transposition fixing k
  has u_i ≠ u_j, so (T2) fails and that transposition works. Contradiction. ∎

## WHAT TO DO — in this order
1. **Re-derive Step 3 yourself** from Lemma 0. Compute ker(P_π − I) and ker(P_π + I) for a
   transposition in 3 variables, in EVERY characteristic (2 is special — say what happens),
   and state the λ = ±1 conditions in your own notation. Report whether you get (T1),(T2)
   exactly, or something different. If different, say precisely where.
2. **Attack by machine.** Write a self-contained python3 script (stdlib only, exact arithmetic,
   NO floating point) that, for GF(q) with q ∈ {2,3,4,5,7,8,9} — you must build GF(4), GF(8),
   GF(9) yourself, do not skip the non-prime fields — enumerates EVERY pair (u,v) ∈ (F³)² with
   1 + vᵀu ≠ 0, forms A = I + u vᵀ, and tests all six permutation matrices with an exact
   cyclicity oracle. Report: (a) the number of A for which NO permutation works — the claim
   says 0, and any single hit refutes a 20-year-old open problem, so print it in full;
   (b) the number for which the ONLY witnesses are 3-cycles, and the number for which the only
   witnesses are transpositions; (c) a direct test of Step 3 as an IFF: for every (u,v) and
   every transposition, compare "(T1) or (T2)" against the oracle's verdict, and print the
   count of disagreements.
   Your script MUST include and print a NEGATIVE CONTROL that fails: e.g. show your oracle
   judges the identity matrix NON-cyclic, otherwise your zero-disagreement count means nothing.
3. **Attack the case analysis by hand.** For each of the four bullets in Step 4, try to find a
   configuration (F, u, v) that satisfies the bullet's hypotheses but escapes its conclusion.
   Pay particular attention to: characteristic 2 and characteristic 3; the step "at most one
   coordinate of u vanishes"; the step that concludes u = a·1 from two (T2) failures; and the
   claim in bullet 4 that "one index kills u and the other kills v".
4. **Attack Step 2.** Is the Galois argument right in EVERY characteristic, including
   inseparable situations? Give a counterexample or a clean justification. Also check the claim
   that λ ≠ 0 and that the reduction to A = I + u vᵀ loses nothing.

## Ground rules
- Do not tell me the proof is correct. Tell me what you tested and what came back.
- Any counterexample must be printed in full (field, u, v, and the six products' verdicts) so
  I can re-run it.
- If your search finds nothing and your re-derivation matches, say exactly that, and state
  what your search did NOT cover (which fields, which n) — that limitation is part of the answer.
