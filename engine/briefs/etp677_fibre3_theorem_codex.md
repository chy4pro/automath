# CODEX TICKET (mathematics, sol tier) — "no congruence with all classes of size 3" in finite
# 677-magmas: PROVE or REFUTE. Repo: $HOME/workspace/claudecode/automath. English.
# Local compute allowed: pure Python + kissat runs ≤ 120 s each (tools/kissat/build/kissat,
# encoder problems/etp677/ext/ext_cnf.py with --no-defect; decoder ext_decode_verify.py).

## Setting (all facts below are PROVED in the campaign; cite them, do not re-prove)
Finite magma (M,*) with E677: x = y*(x*((y*x)*y)). Then every L_y: z ↦ y*z is a bijection.
(R7-C/quotient, Lean-certified in lean/etp677_ext/Ext677.lean L2): for a surjective
homomorphism f: N → B of finite 677-magmas all fibres have the same size m, and N is a
pair-indexed extension: N ≅ B × M with (x,s)*(y,t) = (x<>y, s <>_{x,y} t), each fibre op
having permutation rows, and E677 on N ⟺ blueprint eq.(4) for all base pairs (L3):
  s = t <>_{P1} ( s <>_{P2} ( (t <>_{P3} s) <>_{P4} t ) ),
  P1 = (y, y\x), P2 = (x, (y<>x)<>y), P3 = (y,x), P4 = (y<>x, y).
At an idempotent a of B the instance (a,a) has P1=P2=P3=P4=(a,a), so <>_{a,a} is itself a
677-magma of order m (L6). Known: there is NO 677-magma of order 2, 3, 4, 6 (exhaustive,
community + our own runs). Known theorem (registry R8-C Thm B): no finite 677-magma has a
congruence with exactly two classes... [NOTE: that theorem is about the NUMBER of classes;
the present question is about the SIZE of the classes — do not conflate].

## Computational facts (this campaign, 2026-08-29; DRAT-verified where stated)
- Over the idempotent-free base F_31 with x<>y = 5x−4y+1 (blueprint Type II, c≠0):
  NO extension with fibre size 2 exists (UNSAT, drat-trim VERIFIED) and NO extension with
  fibre size 3 exists (UNSAT 0.9–2.9 s, drat-trim VERIFIED, proof 6.9 MB). Files:
  problems/etp677/ext/in3/ctl_f31c_m{2,3}_nodefect.cnf, proofs in ext/out/drat/.
- Over bases WITH an idempotent (F_7 4x+3y, F_7 4x+y, M9, F_13 9x+11y) fibre sizes 2 and 3
  are UNSAT instantly — explained by the diagonal instance (no order-2/3 677-magma).
- Fibre size 4 over F_31: existence UNKNOWN locally at 60 s; running on the cloud.

## The question
CONJECTURE (F3): no finite 677-magma has a congruence all of whose classes have size 3.
(Equivalently: no pair-indexed extension of ANY finite 677-magma by a 3-element fibre.)
Step 0 (easy, do it): such a base B must be idempotent-free (diagonal instance).
Step 1: with m = 3 every fibre op is a map B×B → (S_3)^3 (three permutation rows). Look
for a proof from eq.(4): parity/sign of the rows, the (R7-B/trichotomy) local structure at a
non-idempotent level (star op occurs in exactly three instances with the {1,3} collision),
counting fixed points (toolkit T1/T1': Σ_z|Fix(L_z)| ≤ n, Σ_w|Fix(R_w)| = n in N), or the
KEY identity (y*x)*y = x\(y\x) inside N. The F_31 DRAT proof exists; you may also extract a
small UNSAT core: try deleting instances (base pairs) from the F_31 m=3 CNF and re-solving
(kissat, 120 s cap each, at most 40 solver calls) to see how few instances suffice — a
tiny core is a strong hint for a human proof.
Step 2: if a proof does not close, try to REFUTE: search for a 3-fibre extension over other
idempotent-free bases (F_31 with other c; are there idempotent-free 677-magmas of order
13 or 19? — check the Type-II affine family p ≡ 1 mod 3 with c ≠ 0: x<>y = αx+βy+c has an
idempotent iff (1−α−β) is invertible or c = 0; list which (p,α,β,c) are idempotent-free),
encode with ext_cnf.py (add the base table to BASES in a COPY of the encoder under
problems/etp677/ext/fibre3/, do not edit the original), solve with the cap.

## Deliverables
`problems/etp677/ext/fibre3/{notes.md, scripts…}` and `engine/out/codex/etp677_fibre3_report.md`:
Step 0 proof; Step 1 either a complete proof (every step citing a named fact) or the
precise obstruction + the measured UNSAT core size; Step 2 results (which bases tested,
verdicts); end with DONE-FIBRE3. Honesty: a proof that uses a fact you did not prove or cite
is not a proof — label it CONJECTURED. Time box 3 h.
