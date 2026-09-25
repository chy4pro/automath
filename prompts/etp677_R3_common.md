# R3 common addendum: established facts and BLOCKED routes (do not re-tread)

All facts below are PROVED for finite 677-magmas (M,*), |M| = n. E677:
x = y*(x*((y*x)*y)); E255: x = ((x*x)*x)*x. L_y(z)=y*z is a permutation
(write Λ_y = L_y^{-1}); rows of the Cayley table are permutations.

PROVED TOOLKIT:
(KEY)  (y*x)*y = x\(y\x); equivalently Θ_t := R_t∘L_t has Θ_t(x) = (t*x)*t
       = Λ_x(Λ_t(x)). E677 ⟺ KEY in a left quasigroup.
(T1)   E255 ⟺ every column of the table contains its own index ⟺
       Σ_z |Fix(L_z)| = n (always ≤ n; the sets Fix(L_z) are pairwise
       disjoint; if z*x = x then z = (x*x)*x, unique).
(Q')   THE TARGET: a*t = b*t ⟹ a = b (⟺ table is a Latin square ⟺
       {L_y} sharply transitive ⟺ displacement group G⁰ = ⟨L_p^{-1}L_q⟩
       semiregular). (Q') ⟹ E255, resolving the last open finite
       implication of Tao's Equational Theories Project.
(L1)   z ↦ L_z is injective (n distinct row permutations).
(L4)   p*x = q*x AND p\x = q\x ⟹ p = q.
(T3)   For p≠q, F_{pq} := {x : p*x = q*x} contains no two L_p-consecutive
       points; hence |F_{pq}| ≤ ⌊n/2⌋ (rows = code with min distance ≥ n/2).
(N)    N(t,v) := |Fix(L_t∘R_v)| = #{a : a*t = v} = multiplicity of v in
       column t. ALL row sums and column sums of N equal n. Diagonal
       N(v,v) ≤ 1. Support bound N(t,v) ≤ #{p : N(v,p) > 0}. Goal ⟺ N ≡ 1.
(P)    P(r,s) := (r*s, r) is a bijection of M²; iterates give
       x_{k+1} = x_k * x_{k-1}, and E677 adds x_{k-1} = x_k*(x_{k-1}*x_{k+2}).
(Cyc)  m(y) := length of L_y-cycle through y is never 2 or 3; m=1 ⟹ E255
       at y; m=4 ⟹ E255 fails at y. Empirically m ∈ {1,6,7,9,...}.
(Mods) [CORRECTED 08-16 ≤13:46 (file mtime)] Affine models x*y = Fx+Gy+c over an abelian
       group A exist iff P(G) = Φ₁₀(G)·(G⁴+G³+2G²+2G+1) = 0 in End(A) with
       F = (G+G³)^{-1}. Over CYCLIC Z_m this forces odd m (P(G) always odd);
       over general abelian groups EVEN orders exist: 2 is inert in Q(ζ₅)
       (residue degree 4), so even order ⟹ 16 | n, and n = 16 is achieved:
       F₁₆ = F₂[z]/(z⁴+z³+z²+z+1), x*y = (1+z)x + z·y (verified: E677, E255,
       Latin, idempotent — an Alexander quandle). Even spectrum 16,80,112,…;
       odd spectrum includes 1,5,7,9,11,13,19,25,31,35,37,41,43,45,49,…
       Φ₁₀-branch ⟺ F = 1−G ⟺ idempotent ⟺ Alexander quandle.
       Orders 2,3,4,6,8,10(?),12,14 have no models (10 pending). All known
       models remain affine quasigroups satisfying E255. PARITY/SIGN/2-adic/
       Sylow-2 proof routes: BLOCKED (sign identity provably uninformative).
(NEW)  Two single-variable bijectivity reductions (the B3-type linking form):
       column t is a permutation ⟺ Θ_t : x ↦ Λ_x(Λ_t(x)) is bijective;
       row x of N ≡ 1 ⟺ y ↦ (y*x)*y is bijective. (Q') ⟺ all Θ_t bijective.

BLOCKED ROUTES (proved dead or circular — do not spend time):
(B1) Equational/quasi-equational derivation of E255 (or Q') from E677 +
     left-cancellation: congruence-closure saturation shows no collapse;
     any proof must use GLOBAL counting/finiteness.
(B2) Proving surjectivity/injectivity of the state map
     T(t,v,x) = (v, Λ_t x, Λ_v x) on ℰ = {(t,v,x): x ∈ Fix(L_t R_v)}
     (|ℰ| = n²): PROVED equivalent to (Q') itself — circular.
(B3) Pure marginal counting on N (row/col sums + diagonal + support):
     insufficient — explicit numerical matrix satisfies all yet isn't ≡1.
     A NEW constraint LINKING entries of N is required.
(B5) Congruence/block ("self-referential collision") arguments: the block at a
     collision pair can be an ARBITRARY finite 677-magma (R6-A Prop 1.6), so
     "the block map is left-injective" IS (Q'). Blocked as circular.
(B6) Term-level "up-step" along the L_x-orbit ("a*(x*v)=x => T(x,a,v)*v=x"):
     impossible — it forces L_x-invariance of column x of N (or of its support),
     both refuted by m176 (11264/30976; 0/176 columns) (R6-A §3).
(NEW-ID) Sum_z N(z*x,z) = n for every x  [PROVED, R6-A Thm 2.1]; hence
     A(x,z) := N(z*x,z) has all line sums n and tr A = tr N, and E255 <=> tr A >= n.
(NEW-ID) Psi_k := Sum_x N(Lam_x^k(x), x): Psi_{-1} = Psi_0 = tr N <= n [PROVED],
     Psi_1 >= n [PROVED].  Psi_1 <= Psi_0  ==>  E255.
(WARN)  Every known non-right-cancellative 677-magma is IDEMPOTENT, hence satisfies
     E255 trivially and cannot test any orbit/diagonal-curve conjecture; direct
     products are multiplicative. Term searches MUST include m176 and m496.
(R6-C UPDATE) The preceding WARN is retained verbatim as the requested R6-A
     toolkit update, but its first sentence is now superseded: the R6-C order-77
     model is non-idempotent and non-right-cancellative and should be included as
     an additional term-search benchmark.
(R6-E UPDATE) First NON-translation-invariant blueprint extension exists (order
     77, diagonal-decoupling: idempotent bases allow INDEPENDENT diagonal fibre
     blocks — R6E_codex_report.md). R6-B-2 (e=x\x an automorphism) is FALSE
     (1050/5929 hom failures there). Benchmark filter set for all term/matrix
     claims is now {m77, m77NT (R6-E), m176, m496}.
(R6-D UPDATE) [R6D_eaut_report.md] R6-E's refutation INDEPENDENTLY REPRODUCED
     (m77NT rebuilt from its prose spec, not its code: E677 0/5929, 1050/5929
     hom failures, hand-checkable instance X=(0,1),Y=(2,0)). ADDITIONALLY the
     OTHER half of R6-B-2 is also FALSE: e need not even be INJECTIVE.
  (T1') [PROVED, exact dual of T1] {w : x*w = x} = {e(x)} is a singleton for
     every x, so Sum_w |Fix(R_w)| = n EXACTLY (vs T1's Sum_z |Fix(L_z)| <= n).
     Hence e injective <=> e surjective <=> e bijective <=> every w has some x
     with x*w = x.  All three CAN FAIL.
  (AFF-e) [PROVED] For affine x*y = Fx+Gy+c: e(x) = G^-1((1-F)x - c), so
     e bijective <=> (1-F) invertible <=> (G^3+G-1) invertible; G^3+G-1 = 0
     makes e CONSTANT.
  (M9) NEW BENCHMARK, minimal counterexample: M = F_3^2, G = [[0,1],[1,1]]
     (G+G^3 = I), x*y = x + Gy.  Order 9, quasigroup, satisfies E255, 0 is a
     RIGHT IDENTITY, e == 0 constant.  n=9 is MINIMAL (mace4 exhausted n=5,7).
     Note Z_9 carries NO affine 677 model -- 9 lives only on the NON-CYCLIC
     F_3^2, which is why every earlier benchmark (all cyclic / F16 / TI-fibred)
     missed it.  Benchmark filter set is now {m77, m77NT, m176, m496, M9}.
     M9 is the designated killer for any "e / diagonal map is a permutation"
     claim; m77NT for any "diagonal map is a homomorphism" claim.
  (WARN-2) [METHODOLOGY] EVERY known 677-magma satisfies E255. Therefore
     "holds in all known models" carries ZERO information for separating
     consequences of E677 from consequences of E677+E255; term mining on the
     model set literally re-derives E255 itself (x = ((x*x)*x)*x) as a "law".
     No model-mined identity may be used on the E255/(Q') main line until an
     ATP has derived it from E677 alone.
  (SALVAGE) "Idem(B) = Fix(e)" is definitional and UNAFFECTED. "Idem(B) is a
     subalgebra" is NOT refuted (holds in 13/13 models incl. m77NT, M9) but its
     proof route via e in Aut is dead.  Clean replacement target:
        Idem(B) closed  <=>  (a*b)*(a*b) = a*b for all idempotent a,b
                        <=>  SQ  ((x*y)^2 = x^2*y^2)  restricted to idempotent pairs.
     m77NT violates SQ 1050 times globally but NOT on idempotent pairs, so this
     is strictly weaker and still live.  R6-B-3 (31 | each <e>-orbit) has lost
     its carrier entirely: e need not be a permutation, so <e>-orbits are not
     even defined; reviving it first requires "idempotent-free => e injective"
     (open, untouched).
  (TOOLS) Self-contained ATPs built this round, no global installs:
     tools/ladr_build/LADR-2009-11A/bin/{prover9,mace4}  (needs
     CFLAGS="-O2 -w -std=gnu89" for modern clang) and tools/E/PROVER/eprover
     (E 3.1.0).  Prover9 AND E both fail (<=300 s, 3 GB) on e-hom and on SQ,
     with or without E255 -- consistent with both being false.  mace4 by fixed
     order: e-hom exhausted 0 models at n=5,7,9; e-injectivity exhausted at
     n=5,7 and FOUND M9 at n=9; n=11 unfinished (timeout).
(R9 FALSIFICATION, root-verified) Transport law (T) and kernel law (A) are FALSE
     in general: the order-385 model (GPT-constructed, root rebuilt byte-identical
     SHA a5c6e1eb...; F11 x F5 x F7, F5-diagonal-gated piecewise fibres, genuine
     tau-dependent degeneracy) violates (T) massively (5819/18000 sampled) and (A)
     (438/514) while PASSING F1/F2 and SATISFYING E255. All (T)-conditional theorems
     (R8-B section 5, Delta-dichotomy, F7-base death) are void in general; they
     survive only on separable-fibre classes where (T) was exhaustively verified.
     S_a-constancy SURVIVES (S_a=595 on m385). Benchmark set is now
     {m5, M9, m77, m77NT, m176, m385, m496}. THE open question: what actually
     protects E255 in m385-type models (the R7 three-instance wall analysis is
     (T)-independent and remains the best handle).
## 10. Toolkit additions (append to `prompts/etp677_R3_common.md`)

```
(R9-A/eq4) [PROVED] GENERAL pair-indexed compatibility.  Base B a LATIN 677-magma,
  fibre ops <>_{x,y} left quasigroups on V, (x,s)*(y,t)=(x<>y, s<>_{x,y}t).
  With z3=y<>x, z4=z3<>y, z2=x<>z4 and P1=(y,z2), P2=(x,z4), P3=(y,x), P4=(z3,y):
     E677  <=>  t <>_{P1} ( s <>_{P2} ( (t <>_{P3} s) <>_{P4} t ) ) = s   for all s,t.
  (R6-E's two affine scalar equations are the affine specialisation.)
(R9-A/transfer) [PROVED] DEGENERACY TRANSFER:  rho^{P4}_t o lam^{P3}_t = Theta_t,
  Theta_t(s) := s \_{P2}(t \_{P1} s).  Hence the column-collapse structure of the
  fibre op at P4 -- INCLUDING its dependence on t -- is determined by P1 and P2
  ALONE; P3 only relabels.  Corollary: N_{P4}(t,w) = |Fix(lam^{P1}_t o rho^{P2}_w)|
  (the pair-indexed form of toolkit (N)).
(R9-A/rigidity) [PROVED] (x,y) |-> P4(x,y) = ((y<>x)<>y, y) is a BIJECTION of B^2
  when the base is Latin.  Hence EVERY fibre op is determined by three others:
     u <>_{P4} t = sigma \_{P2}(t \_{P1} sigma),  sigma = t \_{P3} u,
  so no single fibre operation can be perturbed alone.  (Contains GPT-5.6-Pro's
  "STAR = <>" order-77 theorem as the special case "all other ops held fixed".)
(R9-A/absorb) [PROVED] If <>_{P2} is CONSTANT-COLUMN (s<>t = c(t)) then <>_{P4} is
  LATIN.  If <>_{P1} is constant-column then Theta_t is INDEPENDENT of t, so <>_{P4}
  has no tau-dependence.  => a tau-dependent fibre op needs BOTH P1 and P2 non-
  constant-column.
(R9-A/dichotomy) [PROVED] A fibre op is CLEAN iff it is Latin or constant-column
  (s<>t=c(t), c a permutation).  All fibre ops of m77/m77NT/m176/m496 are clean --
  which is exactly why (T),(W),(A) cost them nothing.
(R9-A/DO) [CONSTRUCTED + triple-verified + negative control] m77D: order 77,
  base F_11 (6x+6y), fibre 7, U on QR offsets and W on non-QR offsets NON-AFFINE
  (tables in R9A_DO_report.md §6 / R9A_scripts/r9a_DO.py).  W is injective at
  t in {0,2,3,4} and NOT at t in {1,5,6}: TAU-DEPENDENT DEGENERACY.
  m77D REFUTES:  (T) [174900/1041810], (T*), (T-flat), (W) [2112/17787],
  (D) [528/2541], (A) [165/231], FILTER 1 (S_a in {247,257}) and FILTER 2
  (H,G in {207,287}, Sigma/n = 19459/77 not an integer), hence also R8-D Cor D.6,
  D.6.1, D.7 and R8-B Thm B.4 with all its corollaries.
  m77D SATISFIES: E677, E255, all left translations bijective, T3, T1, T1',
  Sum_z N(z*x,z)=n, (R) [0/17787], (B) (rho* is a congruence, 11 classes), C1,
  theta_kappa != nabla (44 distinct ker R_t).  It is NOT simple, so (S) is NOT
  refuted.  22 further order-77 examples were harvested.
(R9-A/retract) The following are now FALSE or VOID: R8-A (W),(D); R8-A Thm 4's
  leg (A); R8-B (T),(T-flat),Thm B.4,Cor B.4.1/B.4.2/B.4.3 -- IN PARTICULAR
  "the F_7(4x+3y) base is dead" is RETRACTED, that base is ALIVE again;
(R9-A APPEND NOTE by root) The block above is R9-A's toolkit update (retractions
included). CRITICAL: benchmark set is now {m5, M9, m77, m77NT, m176, m385, m496,
m77D} and ANY term/counting claim MUST be tested on m77D and m385 FIRST — they
are the only non-separable-fibre models; "holds on all models" without them is
zero evidence. (T),(A),(W),(D),FILTER1/2, S_a-constancy: ALL FALSIFIED (m77D).
Survivors: (R), (B), C1, T1/T1'/T3, Sum_z N(z*x,z)=n, quotient/dictionary
theorems. New single target for (S): (Prop) rho* != nabla on simple non-Latin
magmas.
(v5.1 AUDIT, root-verified 21:25) TWO MORE m77D kills: (S') Sum_z N(z,z*x)=n is
FALSE (values {42,77,112,147} on m77D) — R8-G target dead; Idem(B) subalgebra
closure is FALSE (55/121 idempotent pairs escape on m77D) — R6-D salvage target
dead. Surviving counting identities: Thm 2.1 (Sum_z N(z*x,z)=n), Psi_0=trN<=n,
Psi_1>=n, Sum|Fix(L_yR_w)|=n^2, refined T3, T1/T1'. Every conjecture that
survived only on the pre-m77D zoo is presumed dead until tested on m77D.

(R9-D/psi-def) [DEFINITION FROZEN, root-checkable] Psi_1 = Sum_x N(x\x, x)
     (= Sum_x N(Lam_x(x), x)).  The HANDOVER formula Sum_x N(x*x, x) is
     Psi_{-1} = Psi_0 = tr N, a DIFFERENT quantity.  They agree on every known
     model only because tr N = n there; on A7 they are 21 vs 7, and A7 PASSES
     the wrong version.  Registry L353 was right, HANDOVER was wrong.
(R9-D/F) [PROVED] Psi_1 = n  <=>  (F) a*(x\x) = x => a = x  <=>  no block B of
     any ker R_t with |B| >= 2 contains its own value R_t(B).  So Psi_1 = n is a
     statement about WHERE BLOCK VALUES SIT, not about the collapse design.
(R9-D/vacuous) [PROVED] Psi-EQ ("every finite E677 magma has Psi_1 = n") makes
     Cor 2.4 (Psi_1 <= tr N => E255) VACUOUS: it degenerates to "n <= tr N =>
     E255", i.e. E255 => E255.  Psi-EQ gives Psi_1 >= tr N, the WRONG direction.
     The statement with content remains Psi_1 <= tr N (injection S_1 -> S_0),
     and R6-A Thm 7.4 (free diagonal) forbids any term-definable such injection.
(R9-D/A7psi) [CONSTRUCTED, hand-checkable, independently re-verified] A7psi and
     A7psiE, order 7 over Z_7 with x*y = x + h(y-x):
        A7psi  h = (6,2,4,0,3,1,5)   (= A7 with values recoloured v -> v+5)
        A7psiE h = (0,2,3,6,5,4,1)   (idempotent, so E255 holds)
     BOTH have rho = nabla, Fano column design, all |F_ab| = 1, Sigma = 91 =
     2n^2-n, dBE equality b = 7, AND pass the ENTIRE toolbox: L1, L4, T1, T1',
     T3, refined T3, transversality, double resolution, no constant column,
     NEW-ID, dichotomy, (Cyc), BIRT_2..5, Psi_0 <= n, Psi_1 >= n -- AND
     **Psi_1 = n**.  A7psiE additionally has tr N = n (E255) so Psi_1 = Psi_0 = n,
     the FULL Psi identity.  KEY/E677 violated 42/49.
     => Psi_1 = n and even Psi_1 = tr N CANNOT exclude rho = nabla.  Root's
     "Psi_1 = n is the discriminator that kills A7-type objects" is REFUTED:
     A7's Psi_1 = 21 was an accident of its value labelling.
     Census (all 5040 h over Z_7): 1820 have rho = nabla, 342 pass the toolbox,
     150 also have Psi_1 = n, 48 also have E255.  General construction
     (R9-D Thm D.5'): any prime power q, Singer difference set D in Z_{q^2+q+1}
     with 0 not in D, c with -c not in D, k = c on D and injective off D with
     k != c there, k(0) = 0, h = id+k a permutation.  Realised q=2 (n=7, 48
     objects) and q=3 (n=13, h = (0,2,3,1,5,7,10,12,4,8,11,6,9), Sigma = 325 =
     2n^2-n).  A7psiE JOINS THE MANDATORY BENCHMARK SET, ahead of A7: any claim
     "identity X forbids rho = nabla" must be tested on A7psiE FIRST.
(R9-D/recolour) [PROVED, SCREENING RULE] For rho in Sym(M) put x *_rho y :=
     rho(x*y).  Then (M,*_rho) is a left quasigroup with the SAME column kernels,
     hence the same rho-relation, rho*, all F_ab, Sigma, S_a, covering design and
     dBE data -- but Psi_1, Psi_0, tr N, T1, (Cyc), dichotomy, transversality and
     NEW-ID are NOT invariant.  RULE: any proposed obstruction to rho = nabla
     that is not invariant under value-recolouring is defeated by an n!-orbit
     unless it is fused with KEY.  (Sigma >= 2n^2-n, dBE, Fisher ARE invariant
     and were killed by A7; Psi_1 = n, Psi_1 = tr N, NEW-ID, T1, (Cyc) are NOT
     invariant and are killed by the rho-orbit of A7.)  KEY is not invariant --
     it is precisely what glues the value labelling to the design, which is why
     R9-C Claim 4.1 (no constant column) is the only first-order fact that bites.

(R9-E/CORRECTION) [PROVED, independently re-verified] **A7 does NOT satisfy every
     recorded first-order consequence of E677.**  It VIOLATES toolkit item (N)
     -- the identity in (N)'s own defining line, N(t,v) = |Fix(L_t o R_v)| =
     #{a : a*t = v} -- in 21 of 49 cells.  Hand-checkable: A7's column 0 is
     (1,1,5,1,6,4,3) so N(0,0) = 0, while Fix(L_0 R_0) = {x : 0*(x*0) = x} =
     {5} has size 1 (5*0 = 4, 0*4 = 5).  A7psi violates it 21/49, A7psiE 28/49.
     CONSEQUENCE: R9-C Claim 6.3 ("design route dead, certificate A7") and
     R9-D Cor D.6 are BOTH OVERSTATED and are hereby downgraded -- each proves
     only that the DESIGN-LEVEL items (Sigma, dBE, Fisher, resolvability, T1,
     T3, refined T3, transversality, NEW-ID, Psi_1 = n) cannot refute rho =
     nabla.  Neither phantom hunt ever tested (N).
(R9-E/N-is-B3) [PROVED] (N) is exactly the constraint (B3) demanded.  The matrix
     Fix(t,v) := |Fix(L_t R_v)| has row sums n in ANY left quasigroup, and
     column sums Sum_t Fix(t,v) = Sum_x N(x*v,x) = n by NEW-ID.  So Fix and N
     agree on every margin automatically; (N) is a CELLWISE identity linking
     entries of N, which marginal counting provably cannot supply.
     Proof of (N): a |-> w := t\a is a bijection and a*t = (t*w)*t = w\(t\w) by
     KEY, so a*t = v <=> w*v = t\w <=> t*(w*v) = w <=> w in Fix(L_t R_v).
(R9-E/N-weaker) [PROVED] (N) is STRICTLY WEAKER than KEY, so it is not circular:
     over Z_7, x*y = 2y - x satisfies (N) in all 49 cells but violates KEY 42
     times.  Exhaustively, 27 of the 5040 translation-invariant order-7 left
     quasigroups satisfy (N) cellwise and NONE of them is an E677 magma.
(R9-E/N-Prop) [CONJECTURE, strong separation, independently re-verified]
     **(N) => rho != nabla, i.e. (N) => (Prop_exists).**  Measured: of the 5040
     value-recolourings of A7 (Fano design, rho = nabla throughout) **0** satisfy
     (N); of the 1820 order-7 translation-invariant tables with rho = nabla
     **0** satisfy (N); of the 186 PG(2,3) tables at n = 13 (R9-D Thm D.5')
     **0** satisfy (N); while all 7 real E677 magmas satisfy it and 27 non-E677
     left quasigroups satisfy it.  HONEST GAP: all three rho = nabla families are
     translation-invariant over a cyclic group or recolourings of one such
     object; NOT representative.  Do not promote before a non-cyclic test or a
     proof.  THIS IS THE NEW PRIMARY TARGET OF THE (Prop) LINE.
(R9-E/L4-saturated) [PROVED] The assigned "generalise Claim 4.1 from a constant
     column to a large block" route is a DEAD END.  KEY on a block B = R_t^{-1}(v)
     gives a\t = (L_t L_v)(a) for a in B, whose first-order shadow is exactly
     toolkit (L4) ("a |-> a\t injective on every block of ker R_t", equivalently
     |R_t^{-1}(v) ∩ R_u^{-1}(t)| <= 1 for all t,u,v -- the partition ker R_t and
     the value-t partition are ORTHOGONAL; T1 is the case u = t = v).  The
     projective-plane design SATURATES (L4) with equality, because two lines of
     PG(2,q) meet in exactly one point.  0 violations on all 150 order-7
     Psi_1 = n phantoms.  It therefore cannot bound the block size.
(R9-E/KB2) [PROVED, NEW] For a block B = R_t^{-1}(v): KEY gives w*v = t\w for
     every w in Lam_t(B), so R_v agrees with Lam_t on Lam_t(B) and in particular
     **R_v is INJECTIVE on Lam_t(B)**.  This is NOT R9-C Claim 3.1 (which gives
     R_v injective on B itself); the two sets differ.  Bite: kills 60 of the 150
     order-7 Psi_1 = n phantoms; 0 violations on every real model.  It does NOT
     kill A7, A7psi or A7psiE.
(R9-D/recolour v2) [PROVED -- SUPERSEDES the (R9-D/recolour) entry above, whose
     wording was too strong] Value-recolouring x *_rho y := rho(x*y) preserves
     the column kernels, hence rho, rho*, all F_ab, Sigma, S_a, the covering
     design and the dBE data, but NOT Psi_1, Psi_0, tr N, T1, (Cyc), the
     dichotomy, transversality, NEW-ID or (N).  CORRECT RULE: an identity X can
     obstruct rho = nabla only if X fails on the ENTIRE recolouring orbit of
     every table carrying that design.  Measured consequences: Psi_1 = n is
     satisfied by 150 members of the orbit, so Psi_1 = n CANNOT obstruct;
     (N) is satisfied by 0 members, so (N) REMAINS A CANDIDATE.  (The earlier
     wording "any non-invariant obstruction is defeated by an n!-orbit" is
     wrong: non-invariance is necessary for the orbit test to have content, not
     sufficient for the obstruction to fail.)
(R9-E/benchmark) Any future phantom or "identity X forbids rho = nabla" claim
     must be run against **(N)** and (KB2) as well as the R9-C design list.
     A7/A7psi/A7psiE certify the DESIGN layer only.
(R9-E/N-form) [PROVED] Working reformulation of (N) for the attack on (N-Prop).
     With Theta_t(w) := (t*w)*t and Xi_t(w) := w\(t\w):
        N(t,v) = |Theta_t^{-1}(v)|      (bijection a |-> t\a)
        |Fix(L_t R_v)| = |Xi_t^{-1}(v)| (Xi_t(w)=v <=> w*v = t\w <=> t*(w*v)=w)
     so (N) <=> for all t,v the maps Theta_t and Xi_t have EQUAL-SIZED FIBRES
     over v, whereas KEY says Theta_t = Xi_t POINTWISE.  Both fibre matrices are
     doubly n-regular automatically (columns by NEW-ID) [CORRECTED 08-18 R9-I: only
     under E677 — on the abstract branch E's column sums are n + delta(v), see
     (R9-I/deficit); under (N) itself E = N is doubly regular, so the conclusion
     about (N)'s global-counting shape stands], so (N) is a cellwise
     matching of two doubly-n-regular matrices -- the global-counting shape (B1)
     predicted any proof must have.
(R9-E/noncyclic) [COMPUTATIONAL, exact scope] The (N-Prop) evidence is no longer
     confined to cyclic/translation-invariant objects: 721 UNIFORMLY RANDOM
     order-7 left quasigroups with rho = nabla (from 3e6 draws) and 736 000
     Fano-design tables with ARBITRARY resolution (all 46 orbit representatives
     of {columns}->{lines} under Aut(Fano), independently enumerated sigma
     families, random block-value bijections) -- 0 of either satisfies (N).
     Running total: 743 767 rho = nabla objects in five structurally unrelated
     families, NONE satisfies (N); all 7 real E677 magmas do.  Still missing: a
     proof, and a test at q = 9 (n = 91) where non-desarguesian planes exist.
(R9-F/q9) [COMPUTATIONAL, exact scope] (N-Prop) SURVIVES the q=9 pressure test.
     All four planes of order 9 were targeted; three were built and verified:
     PG(2,9) (cyclic Singer resolution AND general resolution), the HALL plane
     (built by DERIVATION of PG(2,9): the 2-dim GF(3)-subspaces of GF(9)^2 whose
     four GF(3)-lines have four distinct GF(9)-directions; 30 direction sets
     carry exactly 4 such subspaces, which partition the 32 vectors of those
     directions; delete the 36 affine lines with direction in D, insert the 36
     cosets), and the DUAL HALL plane.  Hall and dual Hall are certified
     NON-DESARGUESIAN by explicit Desargues failures (witnesses
     (84,78,63,44,14,11,73) and (55,1,44,8,89,48,27)); PG(2,9) shows none.
     1257 rho = nabla left quasigroups built on these planes (row-by-row
     bipartite matching), 0 satisfy (N).  HUGHES PLANE: NOT BUILT [PENDING] --
     the nearfield/PGL(3,3)-orbit construction was not reproducible with enough
     confidence, and an unverified "Hughes" was deliberately not shipped.  Safe
     recipe for a later round: gate any candidate on (i) the design check,
     (ii) an explicit Desargues failure, (iii) non-isomorphism to Hall and dual
     Hall -- there are exactly 4 planes of order 9, so a fourth pairwise
     non-isomorphic plane IS Hughes however it was produced.
     Running (N) tally: 745 024 rho = nabla objects across seven families, NONE
     satisfies (N); all 7 real E677 magmas do; 27 non-E677 left quasigroups do.
(R9-F/Nfast) [PROVED] The (N) test is O(n^2), not O(n^3): t*(x*v) = x <=>
     v = Lam_x(Lam_t(x)) = Xi_t(x) has EXACTLY ONE solution v per (t,x), so
     |Fix(L_t R_v)| = |Xi_t^{-1}(v)| and (N) is a per-column histogram compare.
     This is what makes n = 91 feasible.
(R9-F/agree) [PROVED] Fix(L_t R_v) = {x : x*v = t\x} is the AGREEMENT SET of the
     BIJECTION Lam_t with the MAP R_v.  Hence |Fix(L_t R_v) ∩ (block of ker R_v)|
     <= 1 (R_v is constant on a block, Lam_t is injective), so on a resolvable
     linear space all but one of the q+1 agreements (N) demands must occur on the
     q^2 singleton part of column v.  Also, for fixed x, #{t : Xi_t(x) = v} =
     N(x*v, x) with no use of KEY; so E(t,v) := |Xi_t^{-1}(v)| has row sums n
     trivially and column sums n by NEW-ID [CORRECTED 08-18 R9-I: the per-cell
     identity is fine, but "column sums n" holds only under E677; on the abstract
     branch Sum_t E(t,v) = n + delta(v) with delta = q*b - m, FALSE in general
     (witness column sums [4,11,10,7,5,6,6]) — see (R9-I/deficit).  NEVER paste
     this entry's last sentence to a solver without the correction], and (N) is
     exactly "E = N cellwise" between two doubly-n-regular matrices.
(R9-F/N-conc) [**REFUTED 08-18 by R9-G, see (R9-G/conc-false); the entry is kept only
     for the record -- do NOT use it as a target or a filter**] The (N) failure on
     covering designs is QUANTITATIVE, not marginal.  (N) forces
     |Fix(L_t R_{nu(t)})| = q+1 at every block cell; measured on the q=9 objects
     the observed value there is min 0 / max 5 / mean ~1, and the maximum of
     |Fix(L_t R_v)| over the WHOLE matrix is only 6-7 against a required 10
     (2 against 3 at q=2).  Since Sum_t |Fix(L_t R_v)| = n automatically (that IS
     NEW-ID), the average is exactly 1 and (N) demands the profile
     {q+1, 1 x q^2, 0 x q}.  SO: proving ANY bound of the form
     max_{t,v} |Fix(L_t R_v)| < max_{t,v} N(t,v) for covering designs proves
     (N-Prop), hence (Prop_exists), on the extremal branch.  This is a
     CONCENTRATION bound, not a design or parity argument.

(R9-G/NU-BIJ) [PROVED, new 08-18] On the EXTREMAL branch (column kernels = a projective
     plane of order q, n = q^2+q+1) the block-value map nu: t -> nu(t) is AUTOMATICALLY
     a bijection.  Proof: if nu(t) = nu(t') = v with t != t', the two distinct lines
     ell_t, ell_{t'} meet in a unique point a; then a*t = v = a*t', so row a is not a
     permutation.  Consequences: every column of N has profile EXACTLY
     {q+1 once, 1 x q^2, 0 x q} (k_v = 1, z_v = q are forced, not free), and under (N)
     each column of E has exactly one entry > 1, at t = nu^{-1}(v), equal to q+1.
(R9-G/conc-false) [REFUTES (R9-F/N-conc), explicit verified witnesses, planner-verified]
     The per-cell concentration bound is FALSE.  |Fix(L_t R_v)| <= q^2+1 is the only
     bound (from (R9-F/agree)), and it is SATURATED by random tables.  Witnesses:
     n=7 Fano rho=nabla left quasigroup with |Fix(L_6 R_5)| = 4 > q+1 = 3
     (R9G_witness.py, rows [[2,5,1,0,4,3,6],[2,0,6,3,1,5,4],[5,0,3,4,2,1,6],
     [2,4,3,1,6,0,5],[6,0,5,1,4,2,3],[0,6,3,2,4,5,1],[3,2,4,1,0,5,6]], Fix = {2,3,4,5},
     nu = (2,0,3,1,4,5,6)); n=13 PG(2,3) with |Fix(L_3 R_12)| = 6 > 4
     (R9G_witness13.py).  Random n=7 tables reach the ceiling 5 = q^2+1.  Two of that
     witness's block cells already equal q+1, so even the cell (N) needs is attainable.
     REASON the local route cannot work: fixing x*v = y and t*y = x constrains two cells
     in DIFFERENT columns and the design constraints on them are one-directional; the
     coupling between the line through x,y and the line through t\x,t\y IS KEY.
     NO bound of the form max E < max N exists at any q.  Do not re-open.
(R9-G/moments) [PROVED; premise CORRECTED 08-18 R9-I] Neither the first nor the SECOND
     moment can obstruct (N) on the extremal branch.  First: E and N are both doubly
     n-regular (rows by definition, columns by NEW-ID) [CORRECTION: E-column
     regularity is NOT automatic on the abstract branch — delta(v) := column sum - n
     satisfies delta = q*b - m and is usually nonzero; delta == 0 is a per-table
     NECESSARY condition for (N).  The entry's conclusion survives because delta == 0
     is SATISFIABLE (A7psiE + 6 of the 8 block-perfect tables), so the first moment is
     a FILTER, not an obstruction — see (R9-I/deficit)] -- this is (B3).  Second: Sum_{t,v} N(t,v)^2 = 2n^2 - n from the
     design alone, while Sum_{t,v} E(t,v)^2 = n^2 + Sum_{x != y} Sum_v
     |R_{x*v}^{-1}(x) ^ R_{y*v}^{-1}(y)|, where the v with x*v = y*v contributes 0 and
     every other v contributes AT MOST 1 (two fibres of two different columns: a
     singleton, or two lines of a plane meeting in one point).  So (N) only asks this to
     average 1 per ordered pair, inside the available range [0, n-1].  No contradiction.
(R9-G/null) [METHODOLOGY, mandatory filter -- planner discipline 08-18] Under the null
     "Xi_t behaves like a uniform random map", each row of E is multinomial(n; uniform),
     which already reproduces every proved constraint (row and column sums n)
     [CORRECTED 08-18 R9-I: read "row sums n exactly, column sums n in expectation" —
     exact E-column regularity is neither a branch theorem (see (R9-I/deficit)) nor a
     property of the null; the probability computations are per-row and unaffected].  Against
     that null: (a) the q=9 "max |Fix| = 6-7 vs required 10" that motivated (N-conc) is
     the expected maximum of 8281 Poisson(1) cells -- pure sample size; (b) the block-cell
     probability is (e^-1/(q+1)!)^n = 3e-9 (n=7), 2.6e-24 (n=13), so failing to find an
     object with all block cells at q+1 is uninformative; (c) P(a table satisfies (N) in
     all n^2 cells) = (n!/(q+1)! / n^n)^n = 1.2e-21 (n=7), 1.3e-79 (n=13), so the
     expected number of (N)-satisfiers among R9-F's 745 024 sampled rho=nabla objects is
     ~1e-15.  THEREFORE the 745 024 tally is NOT evidence for (N-Prop); sampling on this
     line can only ever REFUTE, never support.  Any future "gap" claim on this campaign
     must be reported together with its null prediction.
(R9-G/N-sum) [REFUTED at q=3] The corrected aggregate concentration statement
     Sum_t |Fix(L_t R_{nu(t)})| < n(q+1) is also false: annealing produced a verified
     order-13 rho=nabla object whose nu-diagonal carries exactly 52 = n(q+1) (profile
     (5,6,1,5,2,3,4,4,4,4,3,4,7)).  What (N) needs is the exact PROFILE, not the mass.
(R9-G/N-blocks) [CONJECTURE, weak] All n block cells equal to q+1 simultaneously: best
     found 3/7 (n=7) and 8/13 (n=13), and the best value grows monotonically with the
     search budget (3, 6, 8 at 10x4k, 25x12k, 60x30k) with no plateau -- the signature of
     a search-limited, not structure-limited, quantity.  It is the last local relaxation
     standing, but per (R9-G/null) the search evidence for it is worth nothing.  Attack
     and adversarially search it simultaneously.
(R9-H/q2-theorem) [PROVED, exhaustion, PLANNER-CERTIFIED 08-18] **(N-Prop) holds on the
     ENTIRE q=2 extremal branch**: all 46 assignment orbits under Aut(Fano), all nu up
     to Stab(A), all tables -- 151 626 (A,nu)-orbit reps x 3888 = 589 521 888
     representative tables covering all 5040x5040x3888 = 98 761 420 800 labeled branch
     objects (fixed line set; relabeling-invariant decision).  ZERO satisfy (N).  46 s
     in C (accepted deviation; authorized local compute).  Verification: in-binary
     positive/negative controls, independent Python orbit arithmetic (Burnside=direct=46),
     exact cellwise distribution match vs round-4 machinery, cyclic orbit reproduces
     R9G_exhaust7.out, planner recompiled+reran identically.  Scripts/outputs
     problems/etp677/R9H_*.  Supersedes the cyclic-class-only entry of R9-G section 4b.
(R9-H/3888) [PROVED at q=2, exhaustive; explanation OPEN] The branch table count is
     exactly 3888 for EVERY (assignment, nu) pair -- constant across all 46 orbits.
(R9-H/rigidity-q2) [PROVED, exhaustive scope] Branch-wide extremes at q=2: max agree
     cells 36/49 (single rep table => (N) always fails in >= 13 = 2n-1 cells); max
     perfect rows of E-N = 3 = q+1 (25 rep tables); max perfect cols = 3; joint max
     (3,1); the margin argument alone would only give <= 5.  No incidence law governs
     the perfect-row triples (collinear 4/20, assigned-lines-concurrent 5/20,
     nu-image-collinear 5/20).  The max-agree witness's 13 failures touch ALL 7 columns
     and all three N-classes -- spread, not localized, even at the frontier.
(R9-H/N-blocks-sat) [REFUTED as obstruction at q=2, explicit witnesses] (R9-G/N-blocks)
     is satisfiable: exactly 8 representative tables have all 7 block cells = q+1
     simultaneously (5 assignment orbits incl. the cyclic class; all re-verified by
     brute force; listed in R9H_stats_q2.out).  Null predicted ~1.8 hits in 5.9e8; got
     8 -- no enrichment or suppression.  Round 4's 3/7 plateau was pure search failure.
     Also (N-sum)'s mass 21 is attained 1447x and exceeded up to 27 at q=2.  TENSION:
     block-perfect tables reach agree only 14-29 (max-agree table has 3/7 blocks) --
     block correctness costs off-block agreement; only the full 49-cell system fails.
(R9-H/rowcap) [CONJECTURE 08-18; THEOREM at q=2 ONLY — **REFUTED at q=3 (|P|=5) and q=4
     (|P|=6) on 08-24 as a FULL-branch statement, see (R45/ROWCAP-FULL-REFUTED); the
     delta==0-restricted form survives as (R45/ROWCAP-D0)**]
     On the extremal branch at most q+1 rows (dually q+1 columns) of E coincide with N.
     THEOREM at q=2 (exhaustive).  Since q+1 < n this gives (N-Prop) at each q.  A q=3
     annealing refutation attempt reached only 1 perfect row -- uninformative per
     (R9-G/null) and (R9-H/searcher-blind).
(R9-H/searcher-blind) [METHODOLOGY, PROVED at q=2 by ground truth] The campaign's
     annealing reaches agree 24-25 vs true 36, blocks 3/7 vs true 7/7, perfect rows 0
     vs true 3; its move guards reject ~93% of proposals (real budget ~14x below
     nominal).  An annealing plateau on this line is a fact about the SEARCHER, not the
     structure: no future plateau may be cited as evidence of an obstruction.  Sharpens
     (R9-G/null) from randomness to optimization.
(R9-I/vert-profile) [PROVED, all q, 08-18; Qwen Q4/Q2 claim CERTIFIED by owner-677] For
     every point a on the extremal branch, the transpose map T_a^Xi : t |-> Xi_t(a) has
     fibre-size multiset EXACTLY {q+1 once, 1 x q^2, 0 x q} (= column a of N), with the
     unique big fibre over v0 = a\nu^{-1}(a), while T_a^R : t |-> a*t is a permutation.
     Proof: #{t : Xi_t(a)=v} = N(a*v,a) ((R9-F/agree) identity), v |-> a*v is a
     bijection, then NU-BIJ.  KEY-free, pointwise separation mu_a(R)=1 < q+1=mu_a(Xi).
     CAUTION: does NOT bite on (N) — under E=N both marginals are exactly these; and the
     LITERAL Q4.2 (single-map fibre-multiset invariant separating Xi_t from R_t) is at
     least as strong as (N-Prop): under (N) the horizontal fibre multisets of Xi_t and
     R_t coincide for every t.
(R9-I/deficit) [PROVED 08-18, exact] On the abstract branch define delta(v) :=
     Sum_x N(x*v,x) - n = (column-v sum of E) - n.  Then delta(v) = q*b(v) - m(v) with
     b(v) = #{x : x*v = nu^{-1}(x)} and m(v) = #{x : x in D_{x*v}} (missed values of
     column x*v); Sum_v delta = 0.  delta == 0 (the TRACE of NEW-ID; automatic in any
     real finite 677 magma via NEW-ID at x := v) is a NECESSARY condition for (N) and is
     SATISFIABLE: A7psiE + q=3 sibling (forced by translation-invariance) AND 6 of the 8
     q=2 block-perfect ground-truth tables; but 0/25 rowcap witnesses and 0/2000 random
     branch tables.  A perfect COLUMN v forces delta(v)=0 pointwise; perfect rows force
     nothing pointwise.  (Also: |g^{-1}(v)| = b(v) for g(c) = nu(c)\c — proved identity.)
(R9-I/g-refuted) [REFUTED as stated 08-18] The dead-round claim |g^{-1}(v)| <= q is
     FALSE: 8 of the 25 three-perfect witnesses attain b(v) = q+1 (R9I_adjudicate.out);
     its "general proof" used the retracted branch E-column regularity.  Do not use.
(R9-I/trace-rowcap) [CONJECTURE 08-18; THEOREM at q=2 ONLY — **REFUTED AT q=3 on 08-24,
     see (R45/ROWCAP-REFUTED) at the end of this file; kept for the record**] On the
     delta==0 sub-branch at any q, at most q rows of E are perfect.  q=2 proof: the 25
     exhaustion-certified 3-perfect attainers all have delta != 0, and delta==0 is
     relabeling-invariant.  Since delta==0 is necessary for (N), (N-Prop) is EQUIVALENT
     to its trace-sub-branch restriction, and ANY perfect-row bound < n there implies
     (N-Prop) at that q.  Attainment at q=2: >= 1 (asg=1356420 nu=0516432, rows=1
     cols=2, delta==0, R9I_trace.out); whether 2 is attained needs a filtered
     enumeration pass (open).  (R9-H/rowcap) stays open as the full-branch statement.
(R9-J/norm-refuted) [ADJUDICATION 08-18, witnesses R9J_adjudicate.out] The Q8 tabs'
     "WLOG nu = id by relabeling columns by block value (does not affect
     perfectness/delta/E/N)" is FALSE: x *' y := x*nu^{-1}(y) gives nu' = id but
     Xi'_t = nu o Xi_t while N'(t,.) = N(nu^{-1}(t),.), so perfectness and delta
     are twisted -- 519/530 stock tables change (pr,pc,delta==0); the unique
     delta==0 perfection witness goes (1,2,True)->(0,0,False).  NEVER cite Q8
     statements in nu = id form; the general-nu forms below are the certified ones.
(R9-J/b-cap) [PROVED all q, 08-18; general form of Q8-A Prop 3.1] Ladder:
     delta(v) >= b(v)(q+1) - n for every v (from m(v) <= n - b(v)).  Hence
     delta(v) <= 0 ==> b(v) <= q (so b <= q on the whole trace sub-branch), and
     b(v) = q+1 ==> delta(v) >= q.  Attainment RESOLVED at q=2 [R9-K,
     exhaustive]: delta==0 does NOT force b == 1 — 6561/17195 delta==0 rep
     tables attain b = 2 = q (the old "all 10 known delta==0 objects have
     b == 1" note was dump-set bias; do not cite it).
(R9-J/pair-count) [PROVED all q, 08-18; general form of Q8-A Prop 3.2] With
     e_v := #{unordered Xi-row pairs whose unique common value is v} (well-defined
     by (R9-F/agree)+skeleton: distinct Xi-rows t,u agree exactly at position
     nu(c0), value g(c0), c0 = joining column):  e_v = b(v)(n-1)/2.
     Also: the Xi-array skeleton is FORCED with no perfectness hypothesis --
     Xi_t(nu(c)) = g(c) for every t in ell_c -- so the pairwise-agreement
     structure is implied by the design data (asg, nu) + the g-values.
(R9-J/pencil) [PROVED all q, 08-18; general form of Q8-B Thm 3/4 + Cor 5] For a
     perfect row r: (i) g(c) not in D_r for every c in pencil(r); (ii) g is
     injective on pencil(r) except repeats with value nu(r).  For perfect r != s
     with joining column c0: g(c0) not in D_r u D_s, and if g(c0) not in
     {nu(r), nu(s)} then nu(c0) is the unique Xi_r- and Xi_s-preimage of g(c0).
     Arc form: q+2 perfect rows, no 3 collinear ==> from each, the pencil
     g-values are distinct-or-nu(r).  BITE WARNING: if b == 1, g is bijective
     and (ii) is VACUOUS; note b == 1 is NOT forced by delta==0 (R9-K), so
     (ii) retains bite on the b > 1 part of the trace sub-branch.
(R9-J/marginal-vacuity) [PROVED 08-18; Q8-C Thm 4.1/5.1 certified+sharpened]
     The tensor-marginal/Gale-Ryser system for the perfect-row set P is TIGHT at
     P = X: for every value set U, the exact column capacity is
     n|U| + Sum_{v in U} delta(v), which under delta==0 EQUALS the P = X demand
     n|U|.  NO bound |P| < n is derivable from the (t,x,v)-marginals + column
     structure alone, at any q -- marginal counting is a closed route on the
     rowcap line (extends (B3)/(R9-E/N-is-B3)).  Off the trace sub-branch the
     singleton form Sum_{t in P} N(t,v) <= n + delta(v) DOES bite when
     delta(v) < 0.
(R9-J/phi-fusion) [PROVED 08-18; THE exact missing coupling, feeds Q13] For every
     t the map phi_t : x |-> x * Xi_t(x) equals Lam_t, hence is a BIJECTION --
     this is the entire content of "the Xi-array is realized by a table" (KEY's
     shape, available KEY-free on the abstract branch).  Consequences: R_v
     injective on Xi_t^{-1}(v) for all t,v; for fixed t the images
     {R_v(Xi_t^{-1}(v))}_v partition M.  Q8-A's Target Lemma is equivalent to:
     Fix(L_r R_{nu(r)}) pairwise DISJOINT over perfect rows r (each has size q+1
     under perfectness) -- which FAILS off the trace sub-branch (70/76 stock
     perfect pairs intersect, R9J_adjudicate.out (8)) and is now REFUTED ON IT
     as well: see (R9-K/target-refuted).
     KEY-shadow REFUTED [R9J_probe.out]: |C_r ^ Lam_r(ell_r)| sits at the
     independence level (mean 1.30 vs (q+1)^2/n = 1.29 at q=2); C_r is not a
     plane line beyond chance.  The coupling must be BUILT from phi-fusion, not
     FOUND in the design.
(R9-J/dual) [PROVED + COMPUTATIONAL 08-18] The division table D(a,b) := a\b of a
     branch object is itself a branch object with nu_D = nu^{-1},
     line_D(b) = ell_{nu^{-1}(b)}, N_D = N^T; double dual = primal.  Duality
     preserves NEITHER delta==0 NOR perfect counts (trace witness
     (1,2,True) -> (1,0,False); 8/10 delta==0 tables stay delta==0).  A KEY-free
     transport symmetry (every branch theorem has a dual), NOT a sub-branch
     automorphism.
(R9-K/fork-resolved) [ADJUDICATION + PROVED 08-18; the strategic fork of R9-J §3
     is CLOSED] The abstract system {plane design + forced skeleton + exact
     column structure + delta==0 (as global counts, PROVED equivalent to
     m_col == q*b under the column structure) + perfect-row multisets +
     missed-by <= q} admits |P| = q+1 phantoms at q = 2 — explicit verified
     7x7 witnesses on disk (Qwen Q13-A array, P={0,3,4}, R9K_q13_verify.out;
     independent P={0,1,2} witness, R9K_abstract_q2.out).  Real perfectness
     implies the abstract profile, so the abstract system is a faithful
     relaxation; the real delta==0 cap 2 = q [THEOREM] is therefore NOT a
     consequence of facts (a)-(e)+delta==0: **every trace-rowcap proof must
     use realizability; (R9-J/phi-fusion) is the only certified handle.**
     Landscape at q=2 [INSTANCE scope, Qwen design nu=id g=id, exhaustive]:
     all 35 triples feasible (P-collinearity NOT forced); |P|=4 feasible
     except {1,2,5,6} = complement of ell_1 (so the abstract system also
     misses the real full-branch cap q+1); max abstract |P| = 6 = n-1;
     |P| = n impossible.
(R9-K/trace-attain) [THEOREM at q=2, exhaustive 08-18; closes R9-I's open
     attainment] On the delta==0 sub-branch at q=2 the max number of perfect
     rows is EXACTLY 2 = q — (R9-I/trace-rowcap) is TIGHT at q=2.  Unique
     representative attainer asg=4653120 nu=4362015 (perfect rows {2,3},
     b==1, table in R9K_trace_q2.out; re-verified R9K_witness_verify.out).
     17195/589521888 rep tables have delta==0.  Trace rigidity: max perfect
     cols on delta==0 = 2; max agree = 35.
(R9-K/target-refuted) [THEOREM-grade witness 08-18] On the unique 2-perfect
     delta==0 witness: C_2 = {1,4,5}, C_3 = {0,3,5}, C_2 n C_3 = {5}.
     Pairwise disjointness of C_r (Q8-A Target Lemma) FAILS on the delta==0
     sub-branch even with b == 1.  The disjointness route |P|(q+1) <= n is
     DEAD; and the weakening |C_r n C_s| <= 1 is INSUFFICIENT at q = 2
     (union bound 3*3 - 3 = 6 <= 7).  Any candidate phi-fusion coupling must
     reproduce C_2 n C_3 = {5} on this witness (mandatory test object).
     Also on real perfect rows: r in C_r and beta(r) = nu(r) are FALSE in
     general (both real witnesses violate one or both) — do not assume.
(R9-K/b-not-forced) [THEOREM at q=2, exhaustive 08-18] delta==0 does not
     imply b == 1: max_v b(v) histogram over the 17195 delta==0 rep tables
     is {1: 10634, 2: 6561}.  Any argument assuming g bijective on the trace
     sub-branch must add b == 1 as an explicit hypothesis and lose the
     b = q part of the class.
(R9-I/blockinflate) [COMPUTATIONAL at q=2, exact scope; designated mechanism route]
     sigma-factoring [PROVED]: a single-row graft (replace row u by permutation
     rho = sigma^{-1}) has Xi'_u(x) = x\sigma(x) (x != u), Xi'_u(u) = sigma(sigma(u)),
     with sigma(nu(c)) = c forced on pencil(u).  Enumerating ALL such grafts of the 25
     q=2 witnesses that satisfy every necessary condition for 4 perfect rows EXCEPT
     column integrity: exactly 3 survive, and each fails ONLY by BLOCK INFLATION
     (block -> line + {u}, zero off-block collisions).  Row-local packages admit
     39/27/11 phantoms => NO row-local proof of any rowcap exists.  General-q target:
     q+1 (trace) / q+2 perfect rows must force a column value multiplicity >= q+2.
(R9-L/trans-all-or-nothing) [PROVED 08-18] For a TRANSLATION-INVARIANT table
     x*y = x + h(y-x) on Z_n (h a permutation, k := h^{-1}):
     a\v = a + k(v-a), and with u = x-t,
         Xi_t(x) = t + psi(u),   psi(u) = u + k(k(u) - u),
     so  E(t,v) = F(v-t),  F(c) = #{u : psi(u) = c},
     and N(t,v) = G(v-t),  G(c) = #{d : h(d) - d = c}.
     Consequences: nu(t) = t + c* where c* is the 4-fold (q+1-fold) displacement
     value; ell_t = t - S with S = {d : h(d)-d = c*}; the blocks form a plane iff
     S is a planar difference set; **the perfect-row count is 0 or n, NEVER
     strictly between**; (N) <=> F = G; and delta == 0 holds IDENTICALLY
     (Sum_t E(t,v) = Sum_c F(c) = n for every v), so delta carries ZERO
     information on this family.
(R9-L/trans-q3) [COMPUTATIONAL, EXHAUSTIVE over the family, 08-18] There are
     exactly 1,070,784 translation-invariant branch objects of order 13 (q = 3)
     — 52 planar difference 4-sets of Z_13, 13 values of c*, all bijections off
     S with pairwise-distinct displacements — and NOT ONE has a single perfect
     row.  The cyclic/translation-invariant class is DEAD at q = 3: do not
     dispatch it again, and forbid it explicitly in any q = 3 construction brief.
     (At q = 2 the unique 2-perfect witness is NOT translation invariant, so this
     is not an artifact of small order.)
(R9-L/pencil) [PROVED 08-18] In ANY branch object, for every column c and every
     r in ell_c (perfect or not):  Xi_r(nu(c)) = g(c),  g(c) := nu(c)\c.
     Proof: r in ell_c => r*c = nu(c) => r\nu(c) = c, so
     Xi_r(nu(c)) = nu(c)\(r\nu(c)) = nu(c)\c = g(c). ∎
     CONSEQUENCE — a correction to how condition (d) may be used: the POSITIONAL
     clause "nu(c0) is the position where Xi_r takes the value g(c0)" is
     automatic at a joining column and carries NO information.  The only content
     of (d) there is the non-missed / uniqueness clause  g(c) not in D_r
     (equivalently E(r, g(c)) = 1) for perfect r with c in pencil(r).  Arguments
     that derive a contradiction from the positional clause alone are VACUOUS
     (this is exactly how Q17-B's "collinear 4-set" kill fails).  STATUS AS OF
     r19 — REPLACES the r15 status line, which was true but weaker than what is
     now proved: the collinear CONFIGURATION question (can 3 or more perfect
     rows be collinear?) is still open, and the ENTIRE PAIR LEVEL is retired as
     a route to it, not merely the pair COUNT.  With k_c := |P ^ ell_c|, the two
     plane identities Sum_c k_c = (q+1)|P| and Sum_c C(k_c,2) = C(|P|,2) are
     exactly the first two binomial moments of k, and (R19/MOMENTS) [PROVED, all
     q] is that both sides are functions of |P| ALONE: they hold for EVERY point
     set, so after aggregation the pair level retains NO information about the
     CONFIGURATION of P.  Concretely, a LINE and a (q+1)-ARC have identical
     moments 1 and 2 and differ first at moment 3.  Hence every configurational
     conclusion must enter through a per-line cap k_c <= K, and (R14/PAIRCAP)
     turns ANY such cap into |P| <= (K-1)(q+1) + 1; the best cap the pencil route
     supplies is K = q, giving |P| <= q^2 (tight at q = 2,3,4,5,7), and K = 1 is
     unavailable because any two points of a plane are collinear.  The SAME
     reason retires the SPECTRAL / eigenvalue family: the axioms give
     A A^T = qI + J, so ||A^T 1_P||^2 = q|P| + |P|^2 — moments 1 and 2 again,
     |P|-determined.  And it is why the r18-r19 pair-uniqueness SEPARATOR is
     retired: measured on a printed delta==0 object, a NON-perfect row with
     d_r = 0 satisfies the full (F15) pair-uniqueness clause.  Do not dispatch
     any of these again; see the registry r15/r19 sections, REFUSED-AT-DISPATCH
     items (3) and (6).
(R20/MODP) [PROVED 08-22, every projective plane of order q = p^h, EVERY point
     set S — the array-side quantity that computes k mod p]
     1_S in C_p(Pi)  ==>  k_c := |S ^ ell_c| == |S| (mod p) for EVERY line c.
     Proof: over GF(p), <1_S, 1_ell_c> = k_c; two lines meet in exactly one point
     and |ell| = q+1 == 1 (mod p) since p | q, so ALL pairwise inner products of
     line vectors are 1; writing 1_S = Sum lam_ell 1_ell gives k_c == Sum lam,
     independent of c; summing over the n lines, Sum_c k_c = (q+1)|S| == |S| and
     == n*(Sum lam) == Sum lam since n == 1 (mod p).  QED
     Verified on PG(2,2/3/4/5) over 408/414/422/432 point sets, 0 counterexamples.
     NOTE, standing: "k is in the code" is a SELF-SATISFIED INVARIANT (k = A^T 1_P
     is in the image of A^T by construction) and must never be reported as a
     check; the content is membership of 1_S itself.  (R20_codegate.py/.out.)
(R20/EQUIV) [PROVED 08-22 at q = p PRIME; MEASURED at q = 4] for |S| = q+1:
     k constant mod p  <=>  1_S in C_p(Pi)  <=>  S is a LINE.
     Left equivalence: with B := span{1_ell - 1_ell'} one has B <= C_p^perp <= C_p
     and dim B = dim C_p - 1, so "k const mod p" is 1_S in B^perp, which equals
     C_p exactly when dim C_p = (n+1)/2, i.e. exactly when h = 1.  Measured
     dim C_p / (n+1)/2 / dim B^perp = 4/4/4, 7/7/7, 10/11/12, 16/16/16 at
     q = 2,3,4,5; explicit q=4 witness with constant k mod 2 and NOT in C_2:
     S = {0,1,5,10,16,19}.  Right equivalence: Assmus-Key.
     Exhaustion over ALL (q+1)-subsets at q = 2,3,4,5 (35/715/20349/736281): the
     sets with constant k mod p number exactly n = 7/13/21/31 and are exactly the
     LINES — so the h >= 2 gap does not bite at weight q+1 on those planes
     (MEASUREMENT, not a theorem at general q).
     CONSEQUENCE, and it is a DISPATCH condition: "|P| = q+1 ==> k const mod p" is
     LOGICALLY IDENTICAL to "|P| = q+1 ==> P is a line".  The p-ary code RENAMES
     the line case rather than supplying a stepping stone to it.  Proving it by
     first proving P is a line is a SELF-SATISFIED INVARIANT AT ROUTE LEVEL.  The
     import pays in exactly one direction: derive 1_P in C_p ALGEBRAICALLY, from
     delta == 0 and its mod-p vanishings, WITHOUT knowing the configuration of P.
(R20/NO-UNCOND) [PROVED 08-22, refutation] "delta == 0 ==> 1_P in C_p(Pi)" is
     FALSE, and so is its mod-p form "delta == 0 ==> k constant mod p".  Reason,
     one line: the target |P| <= q is TIGHT at q = 2 (delta == 0 objects with
     |P| = q exist, exhaustive), and a nonzero codeword has weight >= q+1 = 3, so
     1_P is not a codeword there.  The printed q=2 instance IS such a witness: its
     k-profile is not constant mod 2 and 1_P not in C_2.  Do NOT attempt the
     unconditional form; a proof of it is a proof of something false.
     Two standing riders on the conditional form: (VOID TEST) any proof must
     CONSUME |P| = q+1, else it has proved the unconditional form; (VACUITY) at
     q = 2, |P| = q+1 = 3 is unrealizable on delta == 0 ((R9-H)), so the
     conditional form is VACUOUSLY TRUE at q = 2 and no q = 2 object can test it —
     first testable order is q = 3.
     NARROWINGS carried on every claim from this route: N1 C_p(Pi) needs q = p^h
     (prime-power only); N2 the mod-p k-profile certifies membership only at h = 1
     (prime order only, as a general-q argument -- N2 IS A LIMITATION OF **OUR
     CERTIFICATE**, NOT OF THE THEOREM: the literature has the minimum-weight
     characterisation for ALL q = p^h (Assmus-Key, Designs and their Codes, Thm
     5.7.9; small-weight-codeword line, Szonyi-Weiner et al.), see
     (R28/CODEWORD-LIT); it does NOT reopen the route, whose wall is the import's
     own arity-3 hypothesis 1_P in C_p); N3 vacuous at q = 2.
(R20/PN) [PROVED 08-22, all q, ANY set P — no perfectness used, so an IDENTITY and
     NOT a constraint] Sum_{r in P} N(r,v) = |P| + q*[nu^{-1}(v) in P] - |P ^ C_v|
     at every value v, with C_v = {c : v in D_c} = {v*w : w in Z(v)}, |C_v| = q.
     Mod p, since p | q:  Sum_{r in P} N(r,v) == |P| - |P ^ C_v|.  Row-side twin
     of the column-side vanishing m(v) = q*b(v) == 0 (mod p) that delta == 0
     supplies through (F2).  Verified 7/7 on the printed instance; negative
     control: it holds on non-P sets too, which is exactly why it has no bite.
(R20/LINECAP) [PROVED 08-22, all q, from (F15)(i)] for every column c,
     k_c = |P ^ ell_c| <= (q+1) - |ell_c ^ C_{g(c)}|, since a perfect r in ell_c
     has g(c) not in D_r, i.e. r not in C_{g(c)}.  Verified 7/7 columns on the
     printed instance; teeth confirmed (4 of the 35 3-subsets violate it).  It is
     a PER-LINE CAP, and r21 settles exactly what that costs: see (R21/VARCAP),
     (R21/CAPDEFICIT) and (R21/LINE-KILL) immediately below.  Write
     t_c := |ell_c ^ C_{g(c)}| in [0,q], so the cap profile is K_c = (q+1) - t_c.
(R21/VARCAP) [PROVED 08-22, all q, ANY cap profile — settles whether a VARIABLE
     per-line cap aggregates like a uniform one]  From k_c <= K_c and the pair
     identity alone:  C(p,2) = Sum_c C(k_c,2) <= Sum_c k_c(K_c-1)/2
     <= (Kmax-1)/2 * Sum_c k_c = (Kmax-1)(q+1)p/2, so p <= (Kmax-1)(q+1)+1 with
     Kmax := max_c K_c.  **(R14/PAIRCAP)'s closed form transfers VERBATIM to a
     variable cap at K := max_c K_c**, so through the PAIR identity variability
     can only HURT: the target needs Kmax = 1, i.e. K_c = 1 at EVERY line, which
     is strictly MORE than the uniform reading demanded.  Through MOMENT 1 a
     variable cap IS profile-sensitive — see (R21/CAPDEFICIT) for the exact price.
(R21/CAPDEFICIT) [PROVED 08-22, all q; exact integer arithmetic q = 2..13]
     Put DELTA_cap := Sum_c (q - t_c).  Moment 1 gives (q+1)p <= n(q+1) - Sum_c t_c,
     hence p <= n - (nq - DELTA_cap)/(q+1), and since n = q^2+q+1:
         the aggregative reading of (R20/LINECAP) reaches |P| <= q
                                 <==>  DELTA_cap <= q-1.
     I.e. C_{g(c)} must sit INSIDE the line ell_c at all but at most q-1 of the
     q^2+q+1 lines, each exception by at most one point.  MEASURED on the printed
     q=2 instance: t-profile (1,0,1,1,0,0,1), Sum t_c = 4 against the maximum
     nq = 14, DELTA_cap = 10 >> q-1 = 1; the three aggregative bounds there are
     7 (naive transfer), 5 (moment 1), 5 (exact two-moment LP) against q^2 = 4.
     CONCLUSION, and it is a DISPATCH condition: the AGGREGATIVE reading of
     (R20/LINECAP) is refused route (3) in a variable dress and is now
     REFUSED-AT-DISPATCH entry (7) `linecap-agg`.  Do not re-derive it.
(R21/LINE-KILL) [PROVED 08-22, all q — the NON-aggregative reading, and it is NOT
     refused] At a single column, (R20/LINECAP) bounds k_c and says nothing about
     |P|; the ONLY hypothesis under which one column bounds |P| is P subset ell_c,
     i.e. the LINE CASE.  There:  P = ell_{c*} ==> q+1 = k_{c*} <= (q+1) - t_{c*}
     ==> t_{c*} = 0.  CONTRAPOSITIVE: any column with t_{c*} >= 1 cannot have its
     whole line perfect.  Arity-1 in the lines; no sum over lines, neither moment
     identity used; passes q2_gate as `configuration`.
     TWO LIMITS, declared with it and not to be dropped: (i) it closes the LINE
     branch ONLY — it says NOTHING about (q+1)-sets that are not lines, so it is a
     branch-discharge inside the (B) code route, NOT a route to |P| <= q; (ii)
     `t_c >= 1` is a CONDITION on design data, not a theorem — measured on the
     printed instance t_c = 0 at columns 1,4,5 and t_c = 0 is attainable at EVERY
     column under free g ((R11C/A-free)).  Carry the hypothesis printed.
(F18) BRIEF TEXT — REQUIRED FORM (RULING AN, 08-23).  When a brief prints
     (R20/LINECAP) as its (F18), it MUST use this sentence and not a shorter one:
       "This is the ONLY per-line upper bound on k the toolkit supplies.  Its
        AGGREGATIVE use — summing it over the n lines — is REFUSED AT DISPATCH,
        entry (7) `linecap-agg`.  ITS NON-AGGREGATIVE USE IS ALIVE: at ONE column,
        under P subset ell_c, it forces t_{c*} = 0 ((R21/LINE-KILL)), with no sum
        and neither moment identity.  Use it locally; never as your aggregation."
     WHY THIS IS PINNED: the r20 briefs printed "it is a per-line CAP, so by
     refused route (3) it can never on its own deliver the target".  That is TRUE
     of the aggregative use and OVER-BROAD as printed; one of two r20 samples read
     it as a blanket refusal and discarded (R21/LINE-KILL), which the other sample
     derived independently and correctly.  RULING AN, standing: a refusal names a
     USE, not a tool — where a nearby use survives, the refusal must SAY SO.
     Machine-enforced: R16_dispatch_gate.SURVIVES_NEARBY + refused_printed_block().
(R22/BRIDGE) [PROVED 08-23, all q — and it COLLAPSES, which is the point]
     For any set S of PERFECT rows and every value v:
        Sum_{r in S} E(r,v) + |S ^ C_v| == |S|  (mod p).
     From (R20/PN) mod p plus the definition of perfectness.  Written as a matrix,
     G[v][r] := E(r,v) + [r in C_v] - 1, the system is G . 1_S == 0.  BUT (R20/PN)
     at the SINGLETON S = {r} gives N(r,v) == 1 - [r in C_v], hence
        G[v][r] == E(r,v) - N(r,v)  (mod p)      [asserted 49/49 cells, R22_arity]
     so (R22/BRIDGE) IS THE DEFINITION OF PERFECTNESS REDUCED MOD p.  It is ARITY 1
     and ROW-LOCAL, it defines Fp := {r : E(r,.) == N(r,.) mod p} >= P, and it adds
     NOTHING to the hypothesis.  Do not present it as an ingredient.
(R22/ROWLOCAL) [PROVED 08-23, all q — why the p-ary code route cannot be completed
     from the current toolkit]  A row-local necessary condition is a SET condition:
     it asserts P subset Fp and therefore assigns the SAME verdict to every
     (q+1)-subset of Fp.  So `P subset Fp AND |P| = q+1' entails `P is a LINE' iff
     every (q+1)-subset of Fp is a line, i.e. iff |Fp| <= q+1 and Fp is that line —
     which IS the conclusion.  LEMMA (all q): if |X| >= q+2 then X has a non-line
     (q+1)-subset (if X holds no line, any subset works; else take ell minus a point
     plus an outside point y — it meets ell in q >= 2 points, so a line through it
     would BE ell).  Verified exhaustively on PG(2,2) and PG(2,3).
     CONSEQUENCE, and it is the r22 verdict: (COND) cannot be proved from
     (F0)-(F18).  Classes that could contribute: P-FREE facts (delta==0, (F2),
     (F17)) cut nothing — measured, 1 distinct value over all 35 candidates;
     moments 1-2 cut nothing at fixed |P| ((R19/MOMENTS)); (R20/PN) is an identity,
     0 exclusions; (F18) cuts only LINES (all 4 of its exclusions on the printed
     instance are lines), i.e. it works AGAINST the conclusion; and (R22/BRIDGE) is
     the hypothesis mod p.  Maximum arity in P anywhere in the toolkit = 2; the
     TARGET requires arity 3 ((R23/ARITY3) — r22 printed q+1 here, which was the
     arity of the FORMULATION `1_P in C_p', not of the condition; corrected r23).
     DO NOT RE-OPEN without a NON-ROW-LOCAL ARRAY-SIDE ingredient of arity >= 3
     in P THAT CONSUMES delta == 0.  An IMPORT will not do: see (R23/IMPORT-VOID);
     and an arity-3 fact that does NOT consume delta == 0 is FALSE, on 16 of 20
     real q=2 design classes: see (R24/VOID3).
(R23/ARITY3) [PROVED 08-23, all q; EXHAUSTED on PG(2,2)/PG(2,3)/PG(2,5), 0
     disagreements over 35/715/736281 candidate sets]  For |S| = q+1 in PG(2,q)
     the following are EQUIVALENT: (i) S is a LINE; (ii) EVERY 3-SUBSET of S is
     collinear [arity 3]; (iii) moment 3 is maximal, Sum_c C(k_c,3) = C(q+1,3).
     Proof: (ii)=>(i) any c in S is collinear with a fixed pair a,b of S and the
     only line through a,b is ab, so S subset ab and |S| = q+1 = |ab|; (iii)<=>(ii)
     because Sum_c C(k_c,3) COUNTS the collinear 3-subsets, each on one line.
     CONSEQUENCE — this is the replacement SPECIFICATION and it replaces the r22
     one: a new ingredient needs ARITY 3, not q+1.  The gap between the stock
     (max arity 2) and the target is ONE.  Equivalently: the stock supplies only
     UPPER bounds on the k_c and |P|-determined values for moments 1-2, while the
     target is a LOWER bound on moment 3.  ARITY-2 PRICING, measured the r22 way:
     `every 2-subset of S is collinear' takes 1 distinct value over ALL candidates
     at q = 2,3,5 — it excludes 0, because any two points of a plane are collinear.
     (R23_arity3.py PART 2, with a non-line negative control that fires.)
(R23/CLIQUE) [PROVED 08-23, all q — extends (R22/ROWLOCAL) from arity 1 to arity 2,
     which the actual stock needs because (F15)(ii) is arity 2]  If a stock's whole
     P-content is `P subset F' plus `for all distinct r,r' in P: psi(r,r')', let
     Gamma be the graph on F with edges the psi-pairs.  The stock's models at
     |P| = q+1 are EXACTLY the (q+1)-cliques of Gamma, so the stock entails `P is a
     line' IFF every (q+1)-clique of Gamma is a line.  With (R23/ARITY3)'s arity-2
     pricing, a psi built from collinearity gives Gamma = K_F and the cliques are
     all (q+1)-subsets, so (R22/ROWLOCAL)'s lemma applies unchanged.  Measured:
     28 of 35 cliques at q=2 and 702 of 715 at q=3 are NOT lines.
(R23/IMPORT-VOID) [PROVED 08-23, all q — r18's exit (B) was never an exit]
     If I is VALID over the model class (true of every point set in every plane of
     order q) then Cons(T u {I}) = Cons(T) for every theory T: a model of T that
     falsifies X also models I, so T u {I} does not entail X either.  Every
     candidate r18 named under exit (B) — Assmus-Key, Bose-Burton / blocking sets,
     Redei / direction sets, Blokhuis-Ball, Szonyi — is a theorem of PG(2,q), hence
     valid, hence structurally incapable of changing what the stock entails,
     WHATEVER its arity.  r22 named the symptom ("the import moved the wall to its
     own hypothesis"); this is the disease.  THE DICHOTOMY IT LEAVES, and it is the
     usable form: either the stock already entails (COND) — in which case the work
     is to FIND the derivation and no import is needed — or it does not, in which
     case no import can help and the work is to ADD AN ARRAY-SIDE FACT.  Exit (B)
     is not a third option.  LIMIT, declared: this is about ENTAILMENT, not about
     proof discovery; an import can still shorten a derivation that already exists.
     MEASURED, and it is why each import FELT like progress: at weight EXACTLY q+1
     both `S blocks every line' (Bose-Burton) and `1_S in C_p' (Assmus-Key) are
     EQUIVALENT to `S is a line' on PG(2,2) and PG(2,3) — 7/7 and 13/13, so each
     import is a RENAMING, the (R20/EQUIV) species, third instance.  NEGATIVE
     CONTROL: at weight q+2 there are 28 (q=2) and 117 (q=3) blocking sets and 0
     lines, so the equivalence is a weight-(q+1) accident and the test is not blind.
     Machine-enforced: R16_dispatch_gate.import_gate + REFUSED-AT-DISPATCH entry (8)
     `valid-plane-import`.  STILL ALIVE under that entry: an ARRAY-SIDE fact of
     arity 3 on TRIPLES of perfect rows THAT CONSUMES delta == 0 ((R24/VOID3)), and
     — AS A COORDINATE ONLY, never as a target (r24: as a TARGET it is a RENAMING and
     is REFUSED) — any SUPPORT-valued functional of the
     k-profile, e.g. the secant count #{c : k_c >= 2}, EXHAUSTED at q = 2,3,5 to be
     1 on every line and q+1 .. up to 15 on every non-line (r23 printed `3-11' off an
     8031-SAMPLE at q=5; the full range there is 6..15 — corrected r24, and the
     correction STRENGTHENS the separation), while moments 1 and 2 each take a
     SINGLE value over all candidates.  See (R24/SECANT-THRESHOLD) for what that
     coordinate is worth: a good COORDINATE and a bad TARGET.  A support is not a moment; the loose reading
     "everything of arity <= 2 aggregates through moments 1-2" is true only of the
     two moment IDENTITIES the stock holds, not of arity-2 DATA in general.
(R24/VOID3) [PROVED 08-23 by 20 REAL q=2 tables — the VOID TEST for the arity-3
     search, and it is CHEAP]  The 25 rowcap-extremal witnesses of the COMPLETE
     R9-H q=2 enumeration each carry exactly 3 = q+1 PERFECT ROWS.  Rebuilt from
     their tables (E, N, P, nu, the line set from the table's own column kernels,
     delta — nothing read from the file's labels except as a cross-check that must
     agree): 20 distinct (asg,nu) design classes, of which **16 have their q+1
     perfect rows in NON-LINE position** and 4 collinear.  ALL 25 have delta != 0
     ((R9-I/trace-rowcap), reproduced).  CONSEQUENCE: (COND) is FALSE on the branch
     WITHOUT delta == 0, so ANY candidate arity-3 array-side fact `perfect triple
     ==> collinear' MUST CONSUME delta == 0 — a candidate that does not is a proof
     of something FALSE.  Run every candidate against the 20 stored designs BEFORE
     costing it.  Arity-3 twin of (R20/NO-UNCOND)'s VOID TEST.
     AND IT SHARPENS THE SPECIFICATION ONE MORE STEP: delta == 0 is a P-FREE fact
     that excludes NOTHING by itself (r22 CLASS 1, 1 distinct value over all
     candidates), while the perfect-row-local arity-3 data is refuted here.  So the
     missing ingredient must be a COUPLING of delta == 0 to the CONFIGURATION of P;
     neither factor alone can close the gap.
     SECOND USE — it is also a SEPARATING MODEL, with REALIZABILITY, for the branch
     stock MINUS delta == 0, and it is the first one this campaign has owned at the
     level of real tables (the r23 one was on the abstract relaxation).  Keep the
     three negative statements apart: WITNESSED on the abstract subsystem (r23,
     q=2); WITNESSED on the stock-minus-delta==0 with realizability (r24, 16 real
     q=2 tables); PROVED-BUT-UNWITNESSED for the full stock with delta == 0.
     A draft merging any two of them would overclaim.  (R24_arity3_search.py PART 1-2.)
(R24/CLIQUE3) [PROVED 08-23, all q, all arities m — the general form of
     (R22/ROWLOCAL) (m=1) and (R23/CLIQUE) (m=2)]  If a stock's whole P-content is
     `P subset F' plus an m-ary clause `for all distinct r_1..r_m in P: psi', its
     models at |P| = q+1 are EXACTLY the (q+1)-CLIQUES of the m-uniform hypergraph
     H_psi on F, so it entails `P is a line' IFF every (q+1)-clique of H_psi is a
     line.  AT m = 3 this prices the search: psi holds on every triple of every
     realizable perfect-row set and a line's triples are collinear, so H_psi
     contains ALL collinear triples; entailment needs psi's non-collinear triples
     to complete no (q+1)-clique.  SLACK MEASURED: 0 at q = 2 (a (q+1)-clique IS a
     triple — 28/28 additions break it), and >= 1 at q >= 3 (PROVED: a 4-set
     containing a non-collinear {a,b,c} needs x on ab ^ ac = {a}; verified 0/234
     single additions break it at q=3).  READING: the slack is real, small, and in
     the wrong place — psi may be formally weaker than collinearity but must still
     BE collinearity on every set it is applied to.  The arity-3 specification is
     RIGID; cost a candidate psi only if it is a genuine `perfect triple ==>
     collinear'.
(R24/SECANT-THRESHOLD) [PROVED 08-23, all q; EXHAUSTED over ALL (q+1)-subsets of
     PG(2,2)/PG(2,3)/PG(2,5), 35/715/736281]  For |S| = q+1, with
     sec(S) := #{c : k_c >= 2}:  S is a LINE  <=>  sec(S) = 1  <=>  sec(S) <= q,
     and the minimum over NON-lines is EXACTLY q+1, attained by the near-pencil
     (q collinear points plus one off the line).  Measured line/non-line ranges:
     1 vs 3 (q=2), 1 vs 4..6 (q=3), 1 vs 6..15 (q=5).
     WHAT THE STOCK ALREADY HAS IN THIS COORDINATE: moment 2 is an identity the
     stock holds, Sum_c C(k_c,2) = C(q+1,2), and every secant contributes >= 1, so
     **sec(S) <= C(q+1,2) UNCONDITIONALLY**.  The target needs sec <= q, so the
     DISTANCE FROM THE STOCK TO (COND) IS THE INTEGER q(q-1)/2 — 1, 3, 10 at
     q = 2,3,5.  This is the first coordinate in which that distance is a number.
     At q = 2 the stock's bound (3) EQUALS the non-line minimum (3): zero margin,
     which is the exact sense in which q=2 cannot test the arity-3 condition.
     VERDICT ON THE SHAPE, and it cuts both ways: the secant count is a GOOD
     COORDINATE and a BAD TARGET.  As a TARGET every threshold j in [1,q] is
     LOGICALLY IDENTICAL to `S is a line' — the (R20/EQUIV) RENAMING species,
     FOURTH instance.  As a COORDINATE it prices the gap at q(q-1)/2, and that is
     what an ingredient has to buy.  DO NOT try to bound sec from (R20/LINECAP):
     sec <= #{c : t_c <= q-1} <= DELTA_cap, so `sec <= q' demands DELTA_cap <= q,
     which is (R21/CAPDEFICIT) in a new dress — REFUSED-AT-DISPATCH entry (7).
     Measured on the printed delta==0 instance: DELTA_cap = 10 against the 2 needed.
(R21/PAIRCAP-INT) [PROVED 08-22 by exact integer feasibility — a SHARPENING of
     (R14/PAIRCAP), not a correction; no campaign verdict changes]  (R14/PAIRCAP)'s
     closed form (K-1)(q+1)+1 is a valid upper bound at every (q,K) tested and is
     EXACTLY TIGHT at the case the campaign relies on, K = q -> q^2.  It is NOT
     integrally tight at K = q-1: q=4,K=3 gives 11 but the exact LP gives 10;
     q=5,K=4 gives 19 but the LP gives 18.  The gap is ONE POINT and the bound
     still lands at order q^2 — it brings no per-line cap route near the target.
(R10/loc) [PROVED 08-22, all q; contains and supersedes the ad-hoc "FUS1"]
     x in ell_v AND Xi_t(x) = v   <=>   x = t*nu(v).
     Proof (=>): phi_t(x) = x*Xi_t(x) = Lam_t(x) by (R9-J/phi-fusion), and
     x in ell_v => x*v = nu(v); so Lam_t(x) = nu(v), i.e. t*nu(v) = x.
     (<=): if x := t*nu(v) lies in ell_v then Lam_t(x) = nu(v) and
     Xi_t(x) = Lam_x(nu(v)) = x\nu(v) = v.  ∎
     COROLLARY: |Xi_t^{-1}(v) ^ ell_v| <= 1 for all t,v — a fibre of Xi_t meets
     the block of its own column at most once.  0 violations on all 3888 real
     branch tables of the R9-K witness design (R10A_tcount.out).
(R10/T-count) [PROVED 08-22, all q — THE cross-row coupling the rowcap line was
     missing] With T_v := {t : some x in ell_v has Xi_t(x) = v}:
        T_v = R_{nu(v)}^{-1}(ell_v),  hence EXACTLY
        |T_v| = (q+1) + q*[nu^2(v) in ell_v] - |ell_v ^ D_{nu(v)}| .
     Proof: (R10/loc) gives t in T_v <=> t*nu(v) in ell_v; the fibres of
     R_{nu(v)} have size q+1 over nu^2(v), 0 over D_{nu(v)}, 1 elsewhere, and
     nu^2(v) is not in D_{nu(v)}.  ∎  Since |ell_v ^ D_{nu(v)}| <= q we get
     |T_v| >= 1 always and Sum_v |T_v| >= n(q+1) + q*A - nq, A := #{v : nu^2(v)
     in ell_v}.  **BITE: when row nu(v) is PERFECT, D_{nu(v)} is read off the
     array (a perfect row's missing set IS its column's missing set), so |T_v| is
     PINNED EXACTLY.**  0 violations on all 3888 real tables; real objects carry
     23..35 total block hits Sum_t h_t, h_t := #{x : x in ell_{Xi_t(x)}}.
(R10/REAL-1) [PROVED 08-22, all q; DESIGN-LEVEL realizability gate]
     For every c:   g(c) = nu^{-1}(c)  <=>  nu(c) in ell_{nu^{-1}(c)}.
     Proof: nu(c)*g(c) = c by definition of g.  If nu(c) in ell_{g(c)} the entry
     there is the block value nu(g(c)), so nu(g(c)) = c.  Conversely if
     g(c) = nu^{-1}(c) then that entry equals nu(g(c)), and value nu(g(c)) occurs
     in column g(c) exactly on ell_{g(c)}.  ∎
     CONSEQUENCE: g is NOT free design data — it is FORCED to nu^{-1} on
     A(nu) := {c : nu(c) in ell_{nu^{-1}(c)}} and FORBIDDEN to equal nu^{-1} off
     A(nu).  **MANDATORY GATE: any abstract/phantom instance (lines, nu, g) must
     pass (R10/REAL-1) before any search; an instance that fails it certifies
     nothing.**  The R9-K/Q13-A instance (nu = id, g = id) FAILS at 4 of 7
     columns — see the retraction note below.
(R10/closure) [PROVED rule + COMPUTATIONAL power, 08-22] Read (R9-J/phi-fusion)
     Lam_t(x) = x * Xi_t(x) as a table rule with v := Xi_t(x):
        forward   x*v = u known  ==>  t*u = x
        backward  Lam_t(x) = c known  ==>  x*v = c
     Seed with the design entries a*c = nu(c) for a in ell_c (so the first
     forward round IS (R10/loc)), propagate to a fixpoint together with "rows are
     permutations" and, for a PERFECT row c, "column c carries exactly
     M \ ({nu(c)} u D_c) off the block".  Every realization satisfies the
     closure, so a closure conflict CERTIFIES UNREALIZABILITY of the Xi-array.
     POWER [q=2, exhaustive on one design]: on all 3888 real branch tables the
     closure is consistent and determines 49/49 table cells — **the Xi-array plus
     the design DETERMINES the multiplication table**.  BITE: all 90 R9-K
     abstract phantom witnesses are closure-inconsistent.
     LIMIT: the closure alone is evaded by arrays with ZERO block hits; it must
     be FUSED with (R10/T-count) (which forces >= n(q+1) - nq + qA block hits).
(R10/landscape) [COMPUTATIONAL, INSTANCE, exhaustive per subset, 08-22 — CORRECTS
     the landscape clause of (R9-K/fork-resolved)] On the REALIZABLE design of the
     unique delta==0 2-perfect witness (real max perfect rows there = 2 = q,
     verified by enumerating all 3888 branch tables) the abstract system's max
     feasible |P| is: bare 7 = n (so even (N) itself is abstractly feasible);
     +(R10/loc) partial table 7; +(R10/T-count) 7; +closure alone 6;
     **closure + (R10/T-count): 3 = q+1** (all 35 4-sets infeasible).
     So the fused first-order phi-fusion content reaches EXACTLY the real
     FULL-branch cap (R9-H); the residual gap to (R9-I/trace-rowcap) is exactly
     q+1 -> q, one row, and must come from something separating delta==0 from the
     full branch (candidate: fuse (R10/T-count)'s exact form with
     delta(v) = q*b(v) - m(v) = 0 — both are statements about b and the D-sets).
(R10/RETRACTION of the R9-K landscape fine structure) The R9-K abstract instance
     (Qwen's Fano lines, nu = id, g = id) is UNREALIZABLE AS DESIGN DATA:
     nu = id & g = id force c*c = c for every c, hence c in ell_c for every c,
     and that assignment has only 3 absolute points ((R10/REAL-1) fails at
     c = 1,2,5,6).  Therefore R9-K's landscape FINE STRUCTURE — "max abstract
     |P| = 6 = n-1", "unique |P|=4 obstruction {1,2,5,6} = complement of ell_1",
     "|P| = 7 impossible", the |P|=5/6 obstruction lists — is an artifact of
     unrealizable data and is RETRACTED as a statement about the abstract system
     (it remains a correct statement about that one instance).  R9-K's EXISTENCE
     claim (phantoms with |P| = q+1 exist, so facts (a)-(e)+delta==0 cannot cap
     perfect rows) SURVIVES and is STRENGTHENED: on realizable design data the
     bare abstract system admits |P| = n.  The fork verdict is unchanged.
(R11/ZD) [PROVED 08-22, all q — THE pointwise form of the (R10/T-count) x delta==0
     fusion] With Z(x) := {v : v not in {Xi_t(x) : t in M}} (the values MISSED by
     COLUMN x of the Xi-array; |Z(x)| = q by the vertical profile):
        v in Z(x)   <=>   x in D_{x*v} .
     Proof: (R9-F/agree), KEY-free, gives #{t : Xi_t(x) = v} = N(x*v, x); the left
     side is 0 iff v in Z(x), the right side is 0 iff x in D_{x*v}. ∎
     EQUIVALENT FORMS: D_c = {x : x\c in Z(x)} for every column c;
     C_x := {c : x in D_c} = {x*v : v in Z(x)} (both of size q).
     CONSEQUENCE (ZD-delta): m(v) = #{x : v in Z(x)} is ARRAY-VISIBLE, so
     delta(v) = q*b(v) - m(v) is exactly "value v occurs n + delta(v) times in the
     array".  This IDENTIFIES the R9-K abstract system's delta==0 clause with the
     deficit law: delta==0 was ALREADY fully used by R10-A, and the round-10
     "fuse T-count with delta==0" candidate cannot come from re-imposing it — the
     new content is the POINTWISE identification of the D-sets.
     0 violations on all 3888 real branch tables of the R10-A design (R11_zd.out).
(R11/ZD-block) [PROVED 08-22, all q] For x in ell_v one has x*v = nu(v), hence
     v in Z(x) <=> x in D_{nu(v)}, so
        |ell_v ^ D_{nu(v)}| = #{x in ell_v : v in Z(x)}
     is ARRAY-VISIBLE for EVERY v (no perfectness hypothesis).  When row nu(v) is
     perfect this says WHICH points of ell_v lie in D_{nu(v)}, where (R10/T-count)
     said only HOW MANY.
(R11/T-exact) [PROVED 08-22, all q] Substituting (R11/ZD-block) into (R10/T-count):
        |T_v| + #{x in ell_v : v in Z(x)} = (q+1) + q*[nu^2(v) in ell_v]
     for EVERY v — an unconditional identity between array data and design data,
     n equations instead of (R10/T-count)'s |P|.  0 violations on all 3888 real
     tables (R11_texact.out).
(R11/ZD-C) [PROVED 08-22, all q] |C_x| = q with C_x = {x*v : v in Z(x)}; every
     v in pencil(x) ^ Z(x) FORCES the column nu(v) into C_x and every
     v in pencil(x) \ Z(x) FORBIDS it; and for a perfect row r, r in C_x <=>
     x in D_r is array-visible.  So the pencil forcing and the perfect rows compete
     for the same q slots.
(R11/landscape) [COMPUTATIONAL, INSTANCE, exhaustive per subset, 08-22 — closes the
     R10-A residual q+1 -> q gap AT q=2 ON ONE INSTANCE] On the same realizable
     design as (R10/landscape), feasible |P| = 3 subsets: closure + (R10/T-count)
     = 18/35 (R10-A); + (R11/ZD-block) alone = 6/35; + (R11/ZD) full (pointwise +
     |D_c| = q consistency + (R11/ZD-C)) = **0/35**; closure + (R11/T-exact) =
     **0/35** (an independent combination).  Reproduction control: the same binary's
     mode 5 reproduces R10-A node-for-node.  CAVEAT: the |P| = 2 subsets TIMEOUT at
     the 20M-node cap in the new modes, so the measured statement is exactly "no
     |P| = q+1", not "cap = 2 by search"; |P| = q is attained in reality and the new
     filters are 0-violation on all 3888 real tables, so soundness is not at issue.
     **The general-q target is now sharply named: derive |P| <= q from (R11/ZD) +
     the phi-fusion closure.  "delta==0 ==> |P| <= q" remains a CONJECTURE.**
(R11C/A-free) [COMPUTATIONAL, EXHAUSTIVE over nu, q = 2 on the R9-K line set, 08-22]
     On the FIXED line set of the R9-K witness design, ALL 5040 permutations nu
     admit at least one branch table, and A(nu) := #{v : nu^2(v) in ell_v} takes
     EVERY value 0..7 on realizable designs (counts: A=0:140, 1:337, 2:1347,
     3:1020, 4:1278, 5:801, 6:67, 7:50).  So A is FREE design data and
     **"A = n always" / "g == nu^{-1} always" is FALSE**; (R10/REAL-1) cannot be
     sharpened that way, and b == 1 is NOT automatic (e.g. nu = [1,2,3,0,5,6,4]
     gives g = [0,2,0,3,1,0,1], b = [3,2,1,1,0,0,0]).  Control: (R11/ZD) has 0
     violations on the new objects.
     **GUARD (added r14, 08-22): this witness has b(0) = 3 > q, so (R9-J/b-cap)
     forbids it under delta <= 0 — it is NOT a delta == 0 object.  Cite it ONLY for
     "b == 1 is not automatic for branch objects".  Do NOT attach an "even under
     delta == 0" rider to it; on the delta == 0 sub-branch the sharpest PROVED
     statement is b(v) <= q.  The r12 brief set attached that rider and was wrong.**  (R11C_aparam.py/.out, R11C_proofgate.py/.out.)
(R11C/DEAD ROUTES — refuted ox-alpha r11b claims, do not re-dispatch)
     1. "A = n for every branch object" (Aparam L1) — REFUTED by (R11C/A-free).
     2. "delta(v) = q - m(v) identically", hence "b == 1 unconditionally" (bzero
        Thm A / Cor B) — REFUTED (b vectors above).  ERROR: the step "x |-> x*v is
        a bijection by the row-permutation property" varies the ROW index at fixed
        column, i.e. it is a COLUMN of the table, and columns of a branch table are
        NOT permutations (profile q+1,1,...,1,0,...,0).  The heavy-term count is
        #{x : x*v = nu^{-1}(x)}, not 1.
     3. "For perfect r, EVERY x in ell_{nu(r)} has Xi_r(x) = nu(r)" (bzero P1/Cor D)
        — REFUTED by (R10/loc), whose corollary caps that count at 1; measured = 1
        in 57/57 perfect rows, never q+1.  Same bijection-abuse family as the
        already-refuted zdcount/hprofile.
     4. "r perfect => C_r = D_r" (system L2, and L4's perfect half, and the whole
        Phi = n - |P| functional resting on it) — REFUTED: 57/57 perfect rows on
        real tables have C_r != D_r (e.g. C_3 = {0,4} vs D_3 = {0,5}).  ERROR: with
        C_x := {c : x in D_c} the statement "r in C_x <=> x in D_r" is DEFINITIONAL,
        not the symmetry r in D_c <=> c in D_r that C_r = D_r asserts.
     5. "|P ^ C_x| <= q - |F_x|" (zdpencil Thm 4's load-bearing step) — needs
        F_x ^ P = empty, which is unproved and FALSE (9 violations / 27216 pairs),
        so Thm 4's averaged bound |P| <= n - (1/q)Sum_v s_v is NOT proved (it is
        data-consistent: 0/3888 violations).  Route dead anyway: its key gap
        "delta==0 => Sum_v s_v >= q(q^2+1) = 10" is REFUTED — the 7 real delta==0
        objects carry Sum_v s_v in {2,4,7,8}, and the |P| = q = 2 object carries 7.
     6. ZERO-BITE (true but content-free, logged not promoted): mechanism Lemmas
        A/B/C are the already-proved UNCONDITIONAL (R11/ZD) forms with a redundant
        "r in P" hypothesis; zdproof Lemmas 1-4 use only |D_c| = q, so the identity
        z = e+1 holds for EVERY (q+1)-set of columns, perfect or not (35/35), and
        says nothing about perfect rows.
(R12/DEGEN) [PROVED 08-22, all q — a NEGATIVE result: it RETIRES the global
     double-count angle.  Machine-confirmed 0/4248 violations, R12_proofgate2.py]
     Let P be the perfect rows, k = |P|, C_x = {c : x in D_c}, f(x) = |P ^ C_x|,
     f = f_pen + f_off split by pencil(x), and A_P = #{s in nu^{-1}(P) : nu^2(s) in
     ell_s}.  The exact pencil/off-pencil split of the ground identity
     q|P| = Sum_x f(x) is, via (F12)+(F13),
       (**)  q|P| = Sum_{s in nu^{-1}(P)} [ (q+1) + q*[nu^2(s) in ell_s] - |T_s| ]
                    + Sum_x f_off(x).
     (**) is TRUE for all q.  **But k cancels identically**: (**) is equivalent to
       Sum_{s in nu^{-1}(P)} ( |T_s| - 1 - q*[nu^2(s) in ell_s] ) = Sum_x f_off(x),
     which contains no |P| at all.  REASON: Sum_x |P ^ C_x| = Sum_{r in P} |D_r| =
     q|P| counts each perfect column exactly q times, and (F13) only re-expresses the
     pencil share of that SAME count; the two sides are one count read twice.
     CONSEQUENCE (do not re-dispatch): **no bound on |P| can come from double-counting
     I = {(x,c) : x in D_c} against P**, however the pencil/off-pencil or T-data
     substitutions are arranged.  Any route through I must introduce a term that is
     NOT a re-expression of Sum_x |P ^ C_x|.  Corollaries also proved along the way,
     free and correct but with no bite: |T_v| >= 1 for every v (= (F13) + |D_c| = q);
     and the corrected competition bound q|P| <= nq - W_Pbar, W_Pbar :=
     Sum_{v : nu(v) notin P} |ell_v ^ D_{nu(v)}| (0/4248 violations), which is the
     same identity with f_off(x) <= q - s_x and is therefore retired too.
(R12/DEAD ROUTES — refuted ox-alpha r12 claims, do not re-dispatch)
     7. "|g(pencil r) ^ g(pencil r')| <= 1 for r != r'" (dprofile L2) — REFUTED
        3084/89208 row pairs.  ERROR (**fibre-collapse**): the proof gets
        pencil(r) ^ pencil(r') = {c} and then reads off IMAGES; image-of-intersection
        = intersection-of-images needs g INJECTIVE, i.e. b == 1, forbidden by
        (R11C/A-free).  Witness nu = [1,2,3,0,5,6,4], rows 0,1, intersection {0,1}.
     8. "Sum_x theta(x) = (q+1)^2, theta(x) = |S ^ Union_{c in g^{-1}(x)} ell_c|"
        (dprofile P2, and P4 with it) — REFUTED 9782/148680 (q+1)-subsets (witness
        S = {0,1,2}: 8, not 9).  ERROR (**fibre-collapse**): a UNION over the g-fibre
        counted as a SUM.  Correct form is "<=", the wrong direction for P4.
        SALVAGE: dprofile L1(i)(ii) and (P1) e(x) + theta(x) <= |S| are CORRECT.
     9. "nu(c)*(a*g(c)) = a for all a in ell_c" (closure Lemma A) — REFUTED
        70135/89208.  ERROR (**argument/index swap**): the proof transports along
        "phi_a = Lam_{nu(c)}", but (F3) gives phi_a = Lam_a, and phi_a(nu(c)) =
        nu(c)*Xi_a(nu(c)) = nu(c)*g(c), NOT a*g(c) — the row index was put in the
        argument slot.  The correct output nu(c)*g(c) = c is DEFINITIONAL
        (g(c) := nu(c)\c).  Its "in particular" step additionally assumes the
        unjustified incidence nu(c) in ell_c (false 21060/29736).
     10. ZERO-BITE (true, logged not promoted): texact L1 is (F13) summed — the
        dispatch brief's own step-1 formula; texact L2 is (R10/loc); texact's
        delivered bound |P| <= [n(q+1)+qA-q*Sum max(b-q,0)]/L evaluates to 8.75
        against target q = 2 (T-sum route caps |P| at order q^2).  global Claim 1 is
        (F11)/(F14) restated; global Claim 2 uses only |D_r| = q + the definitional
        r in C_x <=> x in D_r; closure Lemma C(i) is (F3) verbatim.
     11. **PHANTOM-MEASUREMENT** (automatic void): compete declared "EXECUTION: none"
        and then asserted a q = 2 measurement ("phantoms are exactly the objects with
        W_Pbar - W_P < q^3") — fabricated, and REFUTED 3967/4248.  Any number not
        derivable in-text voids the answer.

(R25/NZ2) [PROVED 08-23, all q, one line; machine-verified on all 517 stored q=2
     tables]  sum_v E[t][v] = n for every t, hence sum_v delta(v) = 0 IDENTICALLY.
     A single nonzero coordinate cannot sum to zero, so nz(delta) := #{v : delta(v)
     != 0} is NEVER 1.  CONSEQUENCE: `nz(delta) <= 1' is LOGICALLY EQUIVALENT to
     `delta == 0' — it is a RENAMING of the r24 hypothesis, not a weakening — and
     the FIRST genuine scalar relaxation available is `nz(delta) <= 2'.
(R25/MARGIN) [PROVED 08-23 on the 20 real q=2 design classes]  How far the
     (R24/VOID3) void test relaxes in the scalar delta direction, as a NUMBER:
     min nz(delta) over the 16 non-collinear counterexamples is 3 and min sum|delta|
     is 4, so `nz(delta) <= k' survives for k in [0,2] and `sum|delta| <= k' for
     k in [0,3].  With (R25/NZ2) that leaves EXACTLY ONE genuine scalar weakening of
     the r24 hypothesis: `nz(delta) <= 2'.  ALSO: delta-deviation does NOT predict
     collinearity — the 4 collinear designs sit INSIDE the non-collinear range on
     both scalars (nz 5,6,7,7 inside 3..7; sum|delta| 12,12,14,20 inside 4..20), so
     every candidate of the shape `delta small ==> P is a line' is REFUSED on data.
(R25/ONESIDED) [PROVED 08-23, q=2]  On the delta==0 sub-branch at q=2 the max number
     of perfect rows is EXACTLY 2 = q ((R9-K/trace-attain), 17195/589521888 rep
     tables, complete; re-confirmed r25 against all 517 stored dumps).  The arity-3
     candidate's antecedent is `delta == 0 AND three perfect rows', which is
     therefore UNSATISFIABLE ON REAL q=2 TABLES.  So no q=2 object can refute a
     delta==0-consuming candidate, and none can confirm one: the 16 (R24/VOID3)
     controls are a ONE-SIDED instrument.  Ship them (a delta-FREE candidate still
     dies against them for free) but NEVER present them as a test of the hypothesis
     the brief writes down.  A control set that can only ever return PASS is not a
     control set.  BUILDING A TWO-SIDED ONE REQUIRES q >= 3 — objects with
     delta == 0 AND |P| >= 3 exist only there.
(R25/POWER) [MEASURED 08-23, 16 real designs x all 35 (q+1)-subsets]  A void test
     must be reported WITH ITS NULL MODEL.  Screening 10 candidate couplings against
     the 16 stored counterexamples returns 12 satisfactions against a null
     expectation of 11.37 — the screen's output is statistically indistinguishable
     from chance, candidate by candidate (X1 0 vs 0.14, X2 3 vs 1.86, X3 9 vs 7.71,
     X4 0 vs 0.74).  (R24/VOID3) bit because its candidate was P-FREE and the null
     expectation was 16/16.  Against a P-RESTRICTED coupling — exactly the class the
     sharpened specification points at — the null expectation is BELOW 1, so `0 of
     16' is not evidence of safety, it is what an empty screen returns.  RULE: before
     citing a screen's PASS, print what the screen would have returned by chance.
(R25/LISTDRIFT) [FOUND 08-23, and it is a QUESTION-LOCALITY catch]  Every round since
     r22 has asked `does the printed REFUSED block match the machine list?' and every
     round it passed.  NO ROUND HAS ASKED `does the machine list match what we now
     KNOW?'  It did not: entry (8)'s STILL-ALIVE clause still advertised the secant
     count as an available ingredient after (R24/SECANT-THRESHOLD) priced that shape
     as a RENAMING.  Fixed r25 in R16_dispatch_gate.py and here.  A drift check
     between two artifacts we control is not a correctness check against the ledger.
(R26/TRANS-DELTA0) [PROVED 08-23, all n; machine-verified on ALL 1,070,784 q=3
     objects and on 400 arbitrary non-branch permutations]  The `delta == 0
     IDENTICALLY' half of (R9-L/trans-all-or-nothing) uses NONE of the branch
     conditions: for x*y = x + h(y-x) on Z_n with h ANY permutation,
     Sum_t E(t,v) = Sum_c F(c) = n for every v, so delta == 0.  Hence delta == 0
     on a translation-invariant object is a SELF-SATISFIED INVARIANT (RULING L
     species): a scan confirming it carries ZERO information and MUST NOT be
     reported as a check.  Exhaustive measurement: delta == 0 on 1,070,784 of
     1,070,784, max Sum|delta| = 0.
(R26/CTRL-EMPTY) [EXHAUSTIVE over the family 08-23, q=3]  The delta distribution of
     R9-L's 1,070,784 objects, extracted object by object from the RAW tables (F/G
     used only as the CHECKED quantity, 0 cell mismatches — the F/G shortcut
     presupposes what it would be proving, which is the Q17-A circular-verification
     failure mode): delta == 0 on 100.0000%, |P| = 0 on 100.0000%, |P| >= 3 on ZERO.
     So the two-sided control set `delta == 0 AND |P| >= 3' is EMPTY here, and empty
     on the |P| coordinate, not the delta one.  AS A SCREEN THIS FAMILY HAS CHANCE
     RATE 100% AND POWER ZERO: |P| = 0 makes every P-restricted coupling VACUOUSLY
     TRUE on all 1,070,784.  Do not offer these objects as controls.
(R26/GRADE-COST) [PROVED from the ledger 08-23]  `delta == 0 AND |P| >= 3' is
     UNSATISFIABLE at q=2 ((R25/ONESIDED)) and has no witness in the only q>=3
     exhaustion the campaign owns ((R26/CTRL-EMPTY)).  At q=3 such an object has
     |P| in {3,4}: |P| = 3 = q is ATTAINMENT AT THE delta==0 ROWCAP (a THEOREM at
     q=2, OPEN at q=3), |P| = 4 = q+1 REFUTES (N-Prop) at q=3.  The control set is
     therefore one of the campaign's two open outcomes: THE ADJUDICATION CANNOT BE
     CHEAPER THAN THE OPEN PROBLEM IT WAS MEANT TO HELP SETTLE.  Consequence for
     brief design: an arity-3 coupling brief must be graded by DERIVATION
     (derivability_gate / held-out rows, the latter cited ONLY AS A CONJUNCTION at
     the rate COMPUTED IN (R27/ROWRATE) on 677 rows), NEVER by control objects,
     until q>=3 attainment exists.
(R26/PRIOR-ANSWER) [FOUND 08-23, and it is the mirror of RULING BF]  r25 registered
     "R9-L's delta distribution was NEVER EXTRACTED" as the campaign's most valuable
     open question.  It was recorded in THREE places already: registry :1435-1438
     (R9-L's own bullet list), registry :3206-3216 (a later round declining the
     family for exactly that reason), and THIS FILE at (R9-L/trans-all-or-nothing)
     ("delta carries ZERO information on this family").  RULING BF guards against a
     false "already known"; NOTHING guarded against a false "NEVER ASKED", and it
     costs the same.  Before registering a question as unasked, grep the ledger AND
     this file FOR ITS ANSWER.

(R27/RATE-IMPORT) [ESTABLISHED BY GREP 08-23 — a NUMBER with the wrong provenance]
     The "~1/240 blind-guess rate" the 677 ledger attached to its held-out rows and
     labelled COMPUTED is **w133's GATE A rate on w133's Tier-H tables**.  It was
     never measured on any 677 table.  Worse, the import INVERTED it: w133's own
     finding is "GATE A is strong IN CONJUNCTION ONLY; no single row is worth
     anything", and 677 recorded it as "~1/240 PER ROW".  Project rule S-9
     (PROVENANCE IS NOT INHERITABLE) applies to numbers, not only to claims.  A
     number that passes a chance-rate INVENTORY is not thereby a MEASURED number:
     RULING BR is discharged by a COMPUTATION, never by a CITATION.
(R27/ROWRATE) [COMPUTED 08-23, all 14 held-out rows the campaign has ever shipped]
     Blind-guess rates under a null model generous to us (the guesser is told every
     size/parity constraint) span 1/2 to 1/1.8e9.  NO ROW IS NEAR 1/240.  The two
     worst rows are the two VERDICT rows (r20 H6, r18 H3c) and they are COIN FLIPS —
     and r20 H6 was independently found NON-DISCRIMINATING by the r22 audit, so the
     cheapest row to guess is also the easiest to shortcut.  RULE, re-derived on 677
     data rather than borrowed: **A HELD-OUT TABLE IS CITABLE ONLY AS A CONJUNCTION,
     AND A VERDICT ROW IS NEVER A CITED ROW.**
(R27/ROWDEP) [COMPUTED 08-23]  A conjunction rate may multiply ONLY rows that are
     mutually UNDERIVABLE.  The r27 table's first draft had 6 rows of which 3 are
     functions of the others given the data the brief prints; the naive product
     overstated it by 3.3e7.  Check row dependence BEFORE quoting a table's rate.
(R27/DERIV-SCOPE) [PROVED 08-23 from the instrument definitions]  Grading a return
     has THREE axes: (i) PROVENANCE — is every load-bearing step derivable from the
     stock? (ii) EXECUTION — can the engine compute, blind, the quantities its proof
     manipulates? (iii) TRUTH ON WITNESSES — does the conclusion hold on objects
     satisfying the antecedent?  On this branch (i) and (ii) are AVAILABLE at price
     zero and (iii) is EMPTY AT EVERY REACHABLE q for PROVED reasons ((R25/ONESIDED),
     (R26/CTRL-EMPTY)).  Consequence, and it must be printed ON THE BRIEF'S FACE:
     a derivation passing every check is a CANDIDATE, not a theorem.  So the brief
     asks for A DERIVATION EVERY STEP OF WHICH CITES A NAMED STOCK FACT — turning
     adjudication into CITATION CHECKING, which axis (i) does cover.
(R27/BIAS1-STRING) [FOUND 08-23 — the second BIAS-1 blindness in two rounds]
     `bias1_gate` refuses a single-design promotion only when `promotes_to` is the
     literal string 'open' or 'true'; 5 of 7 natural promotion targets pass.  Its own
     docstring states the broader rule ("a single design may REFUTE; it may never
     PROMOTE").  Cf r26: a gate that COUNTS OBJECTS cannot see a VACUOUS POPULATION.
     Same shape both times: **the gate checks the ARGUMENT IT WAS GIVEN, not the
     thing the rule is about.**  Reported, NOT patched in the round that found it.
(R28/ARITY-NAME) [LITERATURE 08-23 — the arity obstruction HAS A NAME, in two
     literatures, neither of them ours]  "P is a line" as a (q+1)-ary relation is
     NOT BINARY-DECOMPOSABLE (CSP/clone theory: a relation is binary-decomposable iff
     expressible by a network of binary constraints; ours is not, its binary closure
     being the COMPLETE graph — which is (R23/CLIQUE) verbatim).  Neighbours: bounded
     width / k-consistency, Sherali-Adams / SoS degree lower bounds, the arity gap
     (Couceiro-Lehtonen).  In FINITE GEOMETRY the moment-1/2 identities are the
     classical STANDARD EQUATIONS for the characters of a k-set (Hirschfeld;
     Hirschfeld-Szonyi 1991) and the sets they control are SETS OF TYPE (m,n).
     CONSEQUENCE FOR ANY WRITE-UP: the PHENOMENON may not be claimed, only this
     target's INSTANTIATION of it, with both names cited.  No closed route reopens.
(R28/CODEWORD-LIT) [LITERATURE 08-23]  See N2 above.  Our "prime-order-only" was
     OUR limitation reported as THE limitation — the ~1/240 species with the sign
     flipped (there we imported another line's number as ours; here we exported our
     own limitation as the world's).  Both are S-9 provenance defects.
(R28/EVEN16) [COMPUTED 08-23, re-derived from the table, NOT cited]  The campaign's
     ODD-ORDER CONJECTURE (all finite 677-magmas of odd order) is FALSE: an order-16
     finite 677-magma exists (E677 verified on all 256 pairs here; two perturbation
     negative controls both break E677).  It ALSO satisfies E255, so it is NOT a
     counterexample and NOTHING about the target moves.
(R28/BIAS1-CORPUS)/(R28/BIAS1-SITES) [08-23 — RULING CF step 3 discharged]
     `bias1_gate` PATCHED BY INVERSION: at n_designs < 2 it is now DEFAULT-DENY and
     only an explicit REFUTATION target passes; an unseen target REFUSES.  Widening
     the refuse-list would reproduce the defect one synonym out.  Demonstrated
     INDEPENDENTLY of the round that found the hole: (a) 14 of 14 promotion tags
     extracted MECHANICALLY from the pre-r28 registry pass the old gate; (b) the
     gate's own production call sites, incl. R27_derivgrade.py:622 (1 design,
     "a general-q candidate") which the old gate PASSED.  Eight negative controls.
THE TARGET IS OPEN AND **CONTESTED** [08-23, gh, merged AND UNMERGED PRs]
     teorth/equational_theories PR #1440 "Dedicated 677" (Timeroot) is an OPEN,
     UNMERGED draft on the exact target, +36,508 lines, EMPTY BODY, ZERO COMMENTS —
     carrying a FINITE conditional theorem 677 AND Eq8 => 255 and finite 677-magmas
     at orders 11,13,16,19,21,25,29,31,249.  Also memoryleak47/eq677 and the database
     site eq677.icarm.cloud ("the main open question remaining").  A merged-only
     search shows ZERO live competitors.  Never settle openness on merged PRs alone.
(R43/MISSCAP) [PROVED 08-24, all q; CONSUMES delta==0] On the delta==0 sub-branch every
     perfect row r forces M(nu(r)) >= q whole-row misses of the value nu(r) (X = M
     pointwise under delta==0, and row r's block cell alone gives X(nu(r)) >= q); every
     missing row t satisfies pencil(t) ^ g^{-1}(nu(r)) = empty, i.e. t lies OFF
     U_r := Union_{c: g(c)=nu(r)} ell_c (skeleton).  At q=2, beta = b(nu(r)) = 2 pins
     the missing set exactly (complement of U_r has size exactly q).  Verified:
     exhaustive over the R10-A design (3888 tables) + wrong-set control fired; the
     conclusion FAILS on 23/75 perfect rows of the delta!=0 witnesses (delta-consumption
     evidence).  Scripts R43_misscap.py/.out.
(R43/GEN-BUDGET) [PROVED 08-24, all q, delta-free, ANY perfect set P] For every value w:
     Sum_{c in g^{-1}(w)} k_c + S_w(P) = |P| - dP(w) + q*[w in nu(P)], k_c := |P ^ ell_c|,
     dP(w) := #{r in P : w in D_r}, S_w(P) >= 0 the single-column hits of w by P.
     THE ROW SIDE IS EXACTLY (R20/PN); the new content is the column-side split
     (big-fibre hits = Sum k_c over the g-fibre, by skeleton + (R9-I/vert-profile)).
     Line-case evaluation (R43/LINE-BUDGET): P = ell_{c*} gives, for w* := g(c*),
     q*[w* in nu(P)] = b(w*) - 1 + S_{w*}; in particular w* not in nu(P) ==> b(w*) = 1
     and S_{w*} = 0.  Verified on all 25 three-perfect q=2 reps + subsets + negative
     controls (R43_genbudget.py, R43_linebudget.py).
(R44/NUAVAIL) [PROVED 08-24; q=2 bite, general-q slack] A perfect row r must place
     q+1-k_r copies of nu(r) in its q^2 free positions; unavailable free positions:
     big-columns of nu(r) without r in the fibre (beta - k_r) and missing-columns of
     nu(r).  At q=2 the big-column part alone gives b(nu(r)) <= 1 + 2*k_r (k_r = 0
     forces b(nu(r)) <= 1, delta==0 via b-cap).  At q >= 3 the inequality is slack on
     all real objects — quantifies why availability counting dies as q grows.
(R45/CAP2) [PRE-REGISTERED CONJECTURE 08-24; **REFUTED AT q=3 the same day — see
     (R45/CAP2-REFUTED) below; kept for the record; it is a THEOREM at q=2 ONLY**]
     On the extremal branch, |P| >= 3 forces Sum_v |delta(v)| >= 4; equivalently the
     delta==0 sub-branch carries AT MOST TWO perfect rows (uniform cap 2, stronger
     than (R9-I/trace-rowcap), sufficient for (N-Prop)-on-branch at every q).
     TIGHT at q=2 (exhaustive: min mass over 3-perfect = 4 on every one of the 20
     capable designs) and at q=3 (9 verified mass-4 boundary objects,
     R45_q3_mass4_pool.json; patterns (+1,+1,-1,-1) and (+1,+1,-2)).
     **The POINTWISE variant max delta >= 2 is REFUTED at q=3** (flat pattern exists) —
     do not use it.  Decomposition: (L0) 3-perfect ^ delta==0 impossible; (L1)
     3-perfect ^ single (+1,-1) pair impossible; both EXHAUSTIVE THEOREMS at q=2, open
     q >= 3.  **No aggregate-level proof exists: the R9-K abstract phantoms satisfy
     the full named-fact stock with |P| = q+1 and delta==0, so any proof of (L0)/(L1)
     must consume REALIZABILITY (the phi-fusion closure), per (R9-K/fork-resolved).**
(R43-45/WITNESS-POOLS) [CONSTRUCTED + INDEPENDENTLY VERIFIED 08-24] delta==0 objects
     with perfect rows now exist at q=2 (|P|<=2, exhaustive), q=3 (|P|=1 and two
     |P|=2, R43_q3_hits.json, codex-cross-verified), q=4 (two |P|=1,
     R45_q4_candidates.json).  Boundary pool: 9 mass-4 3-perfect q=3 objects + 1
     non-collinear 3-perfect delta!=0 q=3 object (R44_q3_3perf_deltanz.json) — the
     (R24/VOID3) void test now has a q=3 instance.  Any-q mechanical verifier:
     R45_verify_any.py (dual-route E and delta, plane check, negative-control tested).
(R45/L01-SIGMA) [PROVED 08-24, all q; Qwen L01 derivation owner-checked, machine-consistent
     on 77 776 tables / 1370 perfect rows, controls fire — R45_l01_check.py]  sigma(v) :=
     #{positions x : the Xi-column x carries v exactly once} = n − (q+1) b(v) + delta(v).
(R45/L01-HBOUND) [PROVED 08-24, all q, same provenance]  For a perfect row p, w = nu(p),
     h_p(w) := #{c : p in ell_c, g(c) = w} (skeletal copies of w in Xi-row p):
        h_p(w) >= (q+1) b(w) − q^2 − delta(w),   i.e.  q+1 − h_p(w) <= sigma(w).
     Corollaries: delta(w) = −1 ==> b(w) <= q−1;  delta(w) = 0 and b(w) = q ==> h_p(w) = q,
     sigma(w) = 1, and for any perfect P ∋ p with |P| >= 3 the (R43/GEN-BUDGET) lock
     A_w = q+2−d_w, S_w = 1 holds, with d_w <= 1 when P is non-collinear.
     SCOPE WARNING (measured): the bound bites only at b(w) = q, which occurs on q=2
     objects (b = 2) and on NO stored q=3/q=4 object (b(nu(p)) in {0,1,2} there); a
     perfect row may draw ALL q+1 copies of nu(p) from singleton positions (h_p = 0
     attained on real delta==0 objects at q=3,4).  No per-row singleton-concentration
     lemma is true; the (L0)/(L1) differentiator must be inter-row and consume (F-fusion).
(R45/CAP2-REFUTED) [WITNESS 08-24, verified by R45_verify_any.py (dual-route E and delta,
     plane 78/78, rows permutations, negative control fires) + R45_l01_check.py family (0
     violations of every banked fact)]  `R45_L02_q3_3perf_delta0.json` (ChatGPT GPT-5.6
     Pro, brief L02, T1): q=3, n=13, nu = id, lines = translates of {0,4,10,12} in Z_13,
     table NOT translation-invariant, **P = {4,6,10} (3 perfect rows, NON-collinear,
     joining columns 0,6,7), delta == 0 everywhere, b == 1, F-fusion 0/169 violations**;
     D_4={2,3,11}, D_6={4,8,10}, D_10={2,8,9}; 95/169 agree cells, 0 perfect columns.
     CONSEQUENCES: (L0) is FALSE at q=3; (R45/CAP2) is FALSE at q=3 (|P|=3 with mass 0);
     the "uniform cap 2" route to (N-Prop)-on-branch is DEAD.  (R9-I/trace-rowcap)
     "|P| <= q on delta==0" is NOT touched — it is now ATTAINED (tight) at q=3 as well as
     q=2.  The q=3 two-sided control set `delta==0 AND |P| >= 3` that (R25/ONESIDED) and
     (R26/GRADE-COST) said did not exist NOW EXISTS (this object): every arity-3
     candidate coupling must be run against it.  A |P| = 4 delta==0 object at q=3 would
     refute (R9-I/trace-rowcap) itself (not (N-Prop), which needs |P| = n) — that is the
     decisive next probe.  Cyclic DESIGNS are not dead at q=3: (R9-L/trans-q3) kills only
     translation-invariant TABLES; this non-TI table lives on the cyclic design.
(R45/ROWCAP-REFUTED) [WITNESSES 08-24, verified by R45_verify_any.py (negative controls
     fire) + 0 violations of every banked fact (R45_l01_check family); ChatGPT GPT-5.6 Pro,
     brief L03, method = inverse-table SMT seed + simulated annealing on intra-row cyclic
     swaps preserving (B1)-(B4) with incremental E/N/delta]
     `L03_q3_four_perfect_delta0.json`: q=3, nu = id, cyclic lines, NOT translation-
     invariant, **P = {4,5,6,10}, |P| = 4 = q+1, delta == 0**, b == 1, P is a NEAR-PENCIL
     (k-profile 3,2,2,2 — NOT a line), D_4={6,8,10} D_5={0,3,11} D_6={1,10,12}
     D_10={4,8,9}, 99/169 agree cells, no perfect column.
     `L03_q4_three_perfect_delta0.json`: q=4, n=21, nu = id, lines = translates of
     {3,6,7,12,14} in Z_21, non-TI, **P = {0,1,2} (triangle), delta == 0**, b in {0,1,2}.
     CONSEQUENCES: (R9-I/trace-rowcap) "delta==0 ⟹ |P| <= q" is FALSE at q=3.  The
     conditional (COND) "delta==0 ∧ |P| = q+1 ⟹ P is a line" (the p-ary-code route's
     target, (R20/EQUIV)/(R22)/(R23)/(R24)) is FALSE at q=3 (near-pencil witness) — that
     route is closed by refutation, not by arity.  (R9-H/rowcap) "|P| <= q+1 on the full
     branch" is ATTAINED at q=3 on the delta==0 sub-branch (|P| = 4) and is the LAST
     standing cap.  RECORD: every q=2-exhaustion-born cap conjecture tested at q=3 today
     died (CAP2', CAP2, trace-rowcap): treat (R9-H/rowcap) as UNSUPPORTED beyond q=2 until
     a q=3 push fails to exceed 4.  If |P| reaches n = 13 on delta==0, the object satisfies
     (N) and (R9-E/N-Prop) is FALSE at q=3.  The searcher gap is ours: own SD4 hunts
     (550k+ restarts, KTARGET=3) never left mass 4; the Pro annealer went 4 → 2 → 0 and on
     to |P| = 4 — (R9-H/searcher-blind), third instance.
(R45/ROWCAP-FULL-REFUTED) [WITNESSES 08-24, graded by R45_grade_object.py (banked verifier
     + negative control + 0 banked-fact violations + design recomputation); ChatGPT
     GPT-5.6 Pro brief L04, annealer `L04/branch_anneal.c` (SHA-256 546b4105…6676)]
     `L04/L04_q3_P5_mass18_diagnostic.json` (SHA 18c7ed11…d077): q=3, **P = {0,1,2,3,9},
     |P| = 5 = q+2**, delta = (3,0,2,0,-1,0,0,2,0,1,-5,1,-3), mass 18, k-profile 3,2,2,2,2.
     `L04/L04_q4_P6_mass2_diagnostic.json` (SHA 72654b97…856e): q=4, **P =
     {0,1,2,5,15,17}, |P| = 6 = q+2**, delta = +1 at 7, -1 at 10, mass 2.
     So "at most q+1 perfect rows on the extremal branch" is FALSE at q = 3 and q = 4; the
     q=2 theorem (R9-H/rigidity-q2) is a q=2 fact.  Nothing about (N-Prop) moves: (N)
     needs delta == 0, so only the delta==0-restricted cap matters — see the next entry.
(R45/ROWCAP-D0) [CONJECTURE, pre-registered 08-24 — the LAST cap-shaped statement on the
     (N-Prop)-on-branch route]  On the delta == 0 sub-branch at order q, at most q+1 rows
     are perfect.  ATTAINED (tight) at q=3 (`L03_q3_four_perfect_delta0.json`, |P|=4) and
     q=4 (`L04/L04_q4_P5_delta0.json`, SHA 366234a8…3cfc, P = {0,1,2,15,17}, NOT a line —
     k-profile 3,2,2,2,2 — so (COND) is refuted at q=4 as well).  EVIDENCE STATUS: search
     plateau only — >= 5.1e8 annealer iterations at q=3 found no |P| = 5 with delta == 0
     (best 5-row state mass 18); at q=4 the annealer sits at |P| = 6 with mass 2 (one
     delta pair from refutation).  Per (R9-H/searcher-blind) a plateau is not evidence;
     the coincidence "exactly q+1 at two orders, from a searcher that broke every other
     cap within hours" is the only support it has.  Pre-registered: |P| = 6 with
     delta == 0 at q=4, or |P| = 5 with delta == 0 at q=3, REFUTES it; the proof-side
     target, if ever wanted, is "no |P| = q+2 on delta == 0" at one order (route (c),
     STEP 18).  Any bound < n on delta == 0 still gives (N-Prop) at that order.
(R45/ROWCAP-D0-REFUTED) [WITNESS 08-24, graded VERIFIED by R45_grade_object.py; ChatGPT
     GPT-5.6 Pro brief L05, annealer v2 SHA-256 e8aae0e7…03f7]  `L05/L05_q4_P6_delta0.json`
     (SHA caa96eb9…077c): q=4, n=21, nu = id, cyclic lines, **P = {0,1,2,5,15,17},
     |P| = 6 = q+2, delta == 0**, k-profile 3,3,2,2,2 (not a line), b in {0,1,2},
     251/441 agree cells, D_0={4,6,14,18} D_1={5,6,15,19} D_2={3,9,10,14} D_5={7,8,15,18}
     D_15={1,2,6,20} D_17={3,9,10,13}.  (R45/ROWCAP-D0) is FALSE at q=4.
     ROUTE VERDICT (owner-677, 08-24): the PERFECT-ROW-CAP PROGRAM (R9-H rowcap → R9-I
     trace-rowcap → R45 CAP2 → R45 ROWCAP-D0) is CLOSED NEGATIVELY as a route to
     (N-Prop): every cap of the form |P| <= f(q) < n that was ever stated is refuted at
     q = 3 or 4, and the verified delta==0 record is 3 (q=2, exhaustive max), >= 4 (q=3),
     >= 6 (q=4), reportedly >= 8 (q=5, pending grading).  Counting perfect rows does not
     separate the branch from (N); whatever forbids E == N on ALL rows (if anything does)
     is not visible in |P| at small |P|.  Do not state another cap without a q >= 3 proof.
     Fraction |P|/n of the records: 0.43, 0.31, 0.29, 0.26 — the count grows, the fraction
     shrinks; both readings are searcher-limited.
(R45/LADDER) [VERIFIED WITNESSES 08-24, all graded by R45_grade_object.py] delta==0
     perfect-row records: q=2: 3 (exhaustive maximum); q=3: >= 4 (L03); q=4: >= 6 (L05);
     q=5: >= 8 (L05); q=7: >= 14 = 2q (`L06/L06_q7_P14_delta0_best.json`, n=57). All
     on cyclic designs with nu = id (annealer family). Not a cap of the form q+c.
     Searcher distance to (N): q=2 13 failing cells (exhaustive), q=3 <= 40/169 (L06).
     The exact q=3 (N) verdict is a pending certified SAT run (STEP 23 outcome map).
