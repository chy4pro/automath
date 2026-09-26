# 017 CLEAN-ROOM attack — the exact missing set-energy estimate SE(1/20,1)
priority: high · parallel: yes · clean-room: yes · report: /work/campaigns/zaremba-M/phase1/CLEANROOM_SE.md
Run ≥ 3 independent clean-room sub-agents (fresh context; NO web, NO papers, NO campaign files; only the text below), then one comparison report: complete proof (with the exponent/coefficient achieved), best partial statement, obstructions. Do not tell them what the literature or our route reports say.

TEXT FOR THE CLEAN-ROOM AGENTS (the statement is copied verbatim from an internal note; take it as the definition of the problem):
    ## A. Exact missing estimate
    
    Let G=SL2(F_p), D=|G|=p(p^2-1), n=|A|, and
    
        E(A)=#{(a,b,c,d) in A^4:ab^(-1)=cd^(-1)},
        alpha(A)=max_{x,H<G}|A intersect xH|/n.
    
    All quadruples are ordered and the diagonal is included. The desired assertion is, for all nonempty symmetric A and all sufficiently large primes,
    
        E(A)/n^3 <= C[n^(-1/20)+alpha(A)+n/D],                   (A1)
    
    with an absolute coefficient C. Branch A neither proved nor refuted this. The complete weaker replacement is
    
        E(A)/n^3 <= Cweak[n^(-1/1611)+alpha(A)^(1/11)+n/D].      (A2)
    
    The coefficient Cweak is given explicitly below as a formula in two numerically unextracted constants of the symmetric growth theorem. This is a BSG-dependent deduction, not a removal of BSG.
    
Goal: prove the estimate stated above (the "exact missing estimate") with an absolute coefficient C and the stated exponents, for all large primes p and all sets A satisfying its hypotheses; if you cannot, prove the strongest version you can (weaker exponent, extra hypothesis) and state precisely where the loss occurs. You may use standard facts about SL2(F_p): subgroup structure (Borel, split/non-split tori and their normalizers, exceptional subgroups, orders), Frobenius/character-sum bounds, Cauchy–Schwarz/energy manipulations, and any sum-product or growth phenomenon you can PROVE from scratch here. Every inequality must be justified; state clearly which steps are complete.
