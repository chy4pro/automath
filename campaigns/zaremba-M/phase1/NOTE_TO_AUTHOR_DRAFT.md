DONE — private draft prepared for the owner's review; nothing has been sent.

# Technical note draft

Dear Professor Shkredov,

Could you help clarify four points in the numerical appendix of [arXiv:2603.14116v2](https://arxiv.org/html/2603.14116v2#S6)? We may be missing a normalization or an intermediate lemma.

1. **The doubling parameter.** Equation (60) in your [2021 survey](https://www.mathnet.ru/eng/rm10029) reads
   \[
   T_{2s}(f)\ll T_s(f)|A|^{2s}K_*^{-c}.
   \]
   Dividing by |A|^{4s}, we read this as R_{2s}<<R_s K_*^{-c}, where R_s=T_s(f)/|A|^{2s}. With K_*=p^{tau/6}, this gives a squared-mass gain p^{-tau c/6}. [MMS, (19)](https://arxiv.org/html/2212.14646v1#S2) displays
   \[
   \sum_sF(s)\sum_{x\in B}B(sx)\ll |B|\|F\|_1p^{-\delta},
   \quad\delta=2^{-k-2},\quad k\ll\frac{\log p}{\log K(f)},
   \]
   with the following sentence requiring balanced functions. In the appendix, the displays after (159) instead give k=ceil(1/c)+1 and delta=c/2^{k+4}. Is c redefined there as a p-scale exponent? If the initial excess is at most p^{-h_0}, crossing exponent 2 with a strict margin using the literal survey gain would suggest k=ceil(6(2-h_0)/(tau c))+1. At tau=1/4 and c=1/1640 this is 68881 if h_0=1/4, or 77081 if h_0=1/24. Could you indicate the starting-measure estimate and conversion that give 1641?

2. **Symmetry.** The accessible [Rudnev–Shkredov growth theorem](https://arxiv.org/html/1812.01671v3#S1), Theorem 2 there, assumes a symmetric generating set above an absolute size threshold and gives either A^3=SL_2(F_p) or |A^3|/|A|>>|A|^{1/20}. Appendix Lemma 40 omits symmetry, while Theorem 39 supplies a subset A_* of a translate without asserting A_*=A_*^{-1}. Which symmetric-set reduction is intended, and what quantitative cost does it have in C_2?

3. **The BSG exponents.** Could you supply the intermediate inequalities giving (C_1,C_2)=(9,32)? We could not reconstruct the translated positive-cube bound from Tao–Vu Theorem 2.29/Lemma 2.13 and [Tao Proposition 4.5](https://arxiv.org/html/math/0601431v3#S4). The noncommutative graph statement is Tao–Vu Theorem 2.44; its product bound involves two refinements, while Proposition 4.5 bounds AS^nA^{-1}. How are these converted to the asserted A_*^3 bound? [Murphy Lemma 12](https://arxiv.org/html/1907.13569) leaves the polynomial exponent unspecified.

4. **The last rounding.** Keeping k=1641 for this arithmetic question alone, the displayed delta=c/2^{k+4}, kappa=delta/6 and c=1/1640 give
   \[
   \kappa=\frac1{9840\,2^{1645}},\qquad
   \log_2\kappa^{-1}=1658.2644426002\ldots.
   \]
   Should the integer lower bound consequently read kappa>=2^{-1659}, rather than 2^{-1656}, or is a sharper value of c being used?

Thank you for any clarification. These questions concern the displayed quantitative calculation; we are not drawing a conclusion about the qualitative theorem from them.

Best regards,

[Owner's chosen signature]

---

## For the owner only — do not include in the note

**Possible benefits:** clarification may identify an omitted argument, improve the numerical record, prevent work based on an incorrect normalization, or open a useful technical exchange.

**Possible risks:** the author or collaborators may already be addressing these points; an exchange can overlap with their ongoing work. The author may supply a repair and post a revised version, changing the research opportunity or timeline. A version mismatch, particularly the accepted MMS paper versus its accessible arXiv version, could make part of the question redundant. None of these possibilities is established fact. The note makes no allegation and includes no unpublished route, internal report, or project plan.

This is a text draft targeting approximately one printed page; no typeset page-count check was performed. It was checked against G0 and the independent F1 audit. The appendix, MMS (19), and the growth statement were also reopened in their primary HTML sources. The survey PDF redirected on direct opening; its displayed inequality is taken from the two audits and checked against the primary PDF's indexed proof text on p.1099. No claim of a new independent full-PDF inspection is made. No email, message, post, or repository publication was performed. The owner decides whether, when, and under what signature to send.
