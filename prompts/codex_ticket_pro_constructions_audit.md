# CODEX TICKET — THIRD-FAMILY AUDIT of today's five Pro-constructed objects — DONE marker: DONE-PROAUDIT
Engine: codex on gpt-5.6-sol. Heavy processes: ≤ 2 (pure Python/C, small). No internet. No cloud. Write ALL code from scratch;
do NOT import or read engine/harvest/*_pro.md scripts or problems/etp677/window217/*.py before your own run (read them only
afterwards, for comparison). Adversarial stance: your job is to try to BREAK each claim.

## Objects and claims to re-verify independently
A. R217 = F7×F31, (q,s)*(r,t) = (4q+3r mod 7, 5s−4t+[q=r=0] mod 31). Claims: satisfies E677 x = y*(x*((y*x)*y)) for all x,y;
   every left translation is a bijection; KEY (y*x)*y = x\(y\x); E255 ((xx)x)x = x; NO idempotent; U(x) := (xx)*x is a bijection
   with cycle type one 31-cycle + 31 six-cycles; with W(x)=x\x, P(x)=x\U(x), F(x)=x\P(x), b=F(a), d=bb, v=db, c=W(b), u=U(a),
   p=P(a), w=W(a): the condition X6(a) := (v≠u ∧ c≠p ∧ v≠w ∧ c≠w ∧ c≠u) FAILS at exactly the 186 points with q≠0 and every
   failure is c=u; holds at all 31 points with q=0.
B. M217ε = F7×F31 with (4q+r, 5s−4t+[q=r=0]). Claims: E677, E255, no idempotent; a=(1,0) has v=u and c=p (a "window");
   186 of 217 elements are windows; at a=(1,0) none of u, u*u, U(u) is idempotent; the L_u-cycle (u, uu, u(uu), …) has length 10.
C. J1519 = Z7 × M217ε with (Q,x)*(R,y) = (4Q+R, x∘y) if Q=R=0 else (4Q+R, x⋆y), where ∘ is M217ε and x⋆y = π(π(x)∘π(y)),
   π swapping (1,0)↔(0,0). Claims: E677, E255, no idempotent; A=(0,(1,0)) is a window (v=u, c=p) and A = U((1,(0,0))).
D. (Mono) counterexample: over GF(2), n=6, M with rows (0,0,0,1,0,0),(1,0,0,0,0,0),(1,1,1,1,0,1),(0,0,1,0,0,0),(1,0,1,1,1,0),
   (0,0,0,0,0,1); i=1. Definitions: column transpositions act by B ↦ B·P_τ (P_τ swaps two columns); kd(B,1) = rank of the Krylov
   matrix [e1, B e1, …, B^{n−1} e1]; a transposition τ is neutral at B if kd(B P_τ,1) = kd(B,1), ascending if larger; ν(B) = number
   of neutral transpositions. Claims: rank M = 6, kd(M,1) = 5 is a kd-local maximum (no transposition increases kd), ν = 3 with
   neutral transpositions (1,5),(2,5),(3,5), and their ν values are 8, 4, 4 (so no neutral move lowers ν).
E. (2Step) counterexample: read the matrices C and T and the F4 convention from engine/harvest/k1695_r6_2step_pro.md §二/§三
   (ONLY the matrices and the field convention; not its code). Claims: over F4, n=5, i=1: C is a kd-local maximum with kd=4
   having exactly two neutral transpositions, and from each neutral neighbour NO transposition raises kd above 4; T is a strict
   local maximum (all ten transpositions lower kd); both C and T reach kd=5 within two unrestricted transpositions.

## Deliverables → engine/out/codex/pro_constructions_audit.md
For each claim: VERIFIED / REFUTED (with the explicit witness) / COULD-NOT-CHECK (why). Include your code inline (single file,
Python, no dependencies beyond the standard library) and the exact printed output. Add one negative control per object (a
perturbed operation or matrix that must FAIL a check, and does). Report run time. Print DONE-PROAUDIT on its own line in the
report and in your final message. No prose beyond the verdicts; no new conjectures.
