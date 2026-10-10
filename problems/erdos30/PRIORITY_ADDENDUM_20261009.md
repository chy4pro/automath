VERDICT (coordinator, 2026-10-09 19:4x UTC) — our theorems are unchanged; the related-work record must be corrected: an earlier public manuscript (John Akwei, GitHub, 2026-10-01 12:48 UTC) states the same limit constant 2√2/3 for the Hou–Zhao covering-certificate class, one day before our 2026-10-02 publication. Graded: small result (correction), not announce-worthy, not a milestone.

# Erdős #30 — third-party claim by John Akwei: priority and overlap verdict

Inputs: two scout dossiers, read in full and consistent with each other:
- problems/erdos30/THIRD_PARTY_JOHNAKWEI_20261009.md (AUT-81)
- notes/G2_forum30_johnakwei_20261010.md (AUT-82; replies sweep included)

Both are literature reads with locators; neither refereed any proof or replayed any certificate. Nothing below is a proof claim.

## 1. What Akwei claims (per the dossiers)

| Item | Statement | Status in his documents |
|---|---|---|
| Cardinality bound | h(N) ≤ √N + 0.9428096 N^{1/4} + O(1); certificate γ = 0.9428095208… < 0.942809522 (m = 512, L = 8, K = 1, 8194 rational covering checks) | author-reported rational certificate; vectors and checker NOT public; no explicit onset N0 |
| Limit theorem | every symmetric or two-sided Hou–Zhao covering certificate (discrete or continuum, any finite mixture of kernels) has ab ≥ 8/9, hence γ ≥ 2√2/3; equality in the continuum by the ramp ρ(x) = 2x (a = 4/3, b = 2/3); discrete certificates approach the infimum with O(log m / m²) error | written proof (L Thm 1/4.4/5.1, Prop 5.2); already in the 2026-10-01 manuscript E |
| Pair-level relaxation barrier | ĥ₂(N) = √N + c* N^{1/4} + O(1) | numbered CONJECTURE (L 7.7 / D 6.6); only four double-precision instances |
| Citation of us | none in D, L, E | his 10-05 17:23 (site time) reply under our proof claim acknowledges our sharper bound, reports no gap found, promises to cite the Zenodo record |

Numerics: 0.942809522 − 2√2/3 ≈ 4.8·10⁻⁷; his values approach our constant from above, consistent with (not against) our Theorem 1.

## 2. Comparison with our results

- R1 (cardinality theorem, exact 2√2/3, +1, every N ≥ 120⁴): strictly stronger than his bound as a stated theorem (exact coefficient, explicit onset, uniform additive constant). First such statement in the compared record: ours, 2026-10-02 13:00 UTC (commit 302feeb). His Corollary C.2 has a third-order term ab/2 but a larger coefficient and no onset.
- R2 (capacity theorem: liminf (C_f(L) − L) ≥ 8/(9 f(0)) for every even nonnegative f ∈ C₀ ∩ L¹ with ∫f = 1): different quantified object (positive-measure capacity over all such kernels vs boundary cost of Hou–Zhao covering certificates over mixtures of autocorrelations). Same extremal constant, same ramp autocorrelation 4/3 − 2|t| + (2/3)|t|³, same uniform-renewal mechanism (his multiplier is 4× our half-line measure). Neither statement is proved to imply the other; the bridge (certificate boundary cost vs positive-capacity intercept) is unproved on both sides. His class is the one the numerical campaigns (Madeiros, Wu) actually used, so his theorem is the directly relevant "why the numerics stall at 0.9428" statement; ours is the general-kernel statement.
- Priority of the LIMIT CONSTANT 2√2/3 as a method barrier: Akwei's manuscript E (commit 7e78435, 2026-10-01 12:48:40 UTC, GitHub-verified signature 12:48:41) precedes our first optimality commit (9fd3168, 2026-10-02 14:49:00 UTC) and our v2 (11ff867, 15:34:55 UTC). Our 2026-10-02 G2 did not find it: the repository had placeholder author fields and was not indexed by the searches we ran. Independence is asserted by him and not contested by us; the mathematics on both sides was produced in clean rooms.
- Nothing in his documents identifies an error in ours; nothing in ours is changed.

## 3. Decisions

1. Paper: the related-work table and the optimality section of the Zenodo paper must cite Akwei (E, 2026-10-01; L and D, 2026-10-05) and state plainly that the exact infimum 2√2/3 for the two-sided covering-certificate class appeared there first, that our capacity theorem is a different, general-kernel formulation, and that no implication between the two is proved. Draft paragraph in §4. Vehicle: the next Zenodo version. Preferred: fold into v3 together with the verified onset (AUT-71, N ≥ 4,600,000, Lean) so that no version is published for a supporting section alone; if AUT-71 has not passed its gates by 2026-10-13, publish the correction alone (a correction of the published related-work record qualifies under the Zenodo rule). Owner decides between the two timings (approval request on AUT-75).
2. erdosproblems.com: one short reply under our proof claim, answering Akwei's 10-05 comment (draft in §5). Outward action → board approval; recommended. No edit of the claim text now (it claims no priority; the concept DOI will resolve to v3). No new ordinary-thread comment (the site forbids proof announcements there).
3. X: no action (posted posts are never edited; nothing to announce).
4. E-mail: none.
5. Internal: G2_FINAL_20261002.md carries a correction pointer (done); ledger entry (done); G2 rule added below.

G2 lesson (binding for future checks): the final novelty check must include GitHub search (repositories + code) for the decimal constant(s), the radical spelling, and the title keywords of the method, and must look one hop beyond the known forum participants' repositories. A repository with placeholder authorship is still a public record.

## 4. Draft related-work paragraph for the paper (English, for v3)

> **Independent work on the same constant.** A manuscript by John Akwei, posted on GitHub on 1 October 2026 (one day before the first version of this note) and expanded on 5 October 2026 [Akw26a, Akw26b], proves that every symmetric or two-sided covering certificate in the vector-valued smoothing framework of Hou–Zhao satisfies $ab\ge 8/9$, so that the certificate coefficient $\gamma=\sqrt{ab}$ cannot fall below $2\sqrt2/3$, and that the infimum is attained in the continuum by the ramp density $\rho(x)=2x$ on $[0,1]$ ($a=4/3$, $b=2/3$); it also reports a rational certificate with $\gamma<0.942809522$ and the bound $h(N)\le\sqrt N+0.9428096\,N^{1/4}+O(1)$. The ramp is the reflection of our kernel and has the same autocorrelation, and the renewal-measure multiplier is the same up to normalisation. The statements differ in the quantified object: Akwei bounds the boundary cost of Hou–Zhao covering certificates over finite mixtures of autocorrelations, while Theorem~\ref{thm:opt} bounds the positive capacity intercept over all even nonnegative kernels in $C_0\cap L^1$; neither statement is known to imply the other. The explicit cardinality theorem with the exact coefficient, the additive constant $+1$ and the onset $N\ge120^4$ appears to be new to this note. We learned of Akwei's manuscript on 9 October 2026, after the first two versions of this note had been published.

Table row to add (between Wu q2 and "This note"):
> Akwei (October 2026)~\cite{Akw26a} & $\approx0.94280952$ & $\gamma<0.942809522$; $O(1)$, no explicit onset; unrefereed repository claim; proves $\gamma\ge2\sqrt2/3$ for all Hou--Zhao covering certificates \\

Bib entries:
> \bibitem[Akw26a]{Akw26a} J.~Akwei, \emph{Vector-valued smoothing for Sidon sets cannot beat $2\sqrt2/3$}, manuscript, GitHub repository johnakwei/Science, commit 7e78435 (1 October 2026); expanded as \emph{The limit of vector-valued smoothing for Sidon sets is $2\sqrt2/3$}, commit 15609b5 (5 October 2026).
> \bibitem[Akw26b]{Akw26b} J.~Akwei, \emph{A Data Science Analysis of Erd\H{o}s Problem 30}, version 4, GitHub repository johnakwei/Science, commit 6b32990 (5 October 2026).

## 5. Draft reply under our erdosproblems.com proof claim (English; posted only after board approval)

> Thank you for the careful reading and for running the checker. We have now read your two documents and the 1 October manuscript in your repository. Your limit theorem for the Hou–Zhao covering certificates (ab ≥ 8/9, hence γ ≥ 2√2/3, with equality for the ramp in the continuum) predates our 2 October note, and the kernel and renewal mechanism are the same up to reflection and normalisation; our capacity theorem is stated for a different object (the positive capacity intercept over all even nonnegative kernels), and we do not know an implication in either direction. The next version of our note will cite your manuscripts and say this explicitly. Our part that seems to be new is the explicit cardinality bound with the exact coefficient, +1, and the onset N ≥ 120⁴.

## 6. Cost

Scout: two runs (AUT-81, AUT-82; the second was created by a parallel coordinator run before patch 5 took effect), ≈ 15 min, ~60 public fetches, no engine time. Coordinator: three runs on AUT-75 (one lost to the session limit).

## 7. Execution (coordinator, 2026-10-10 03:3x UTC)

Board approval 7c4457ab (A with timing A1, B, C) was approved by the owner at 2026-10-10 02:55 UTC; approval 04b27a03 (AUT-71, new Zenodo version with onset 4,600,000) at 02:56 UTC.

- A, merged: ONE new Zenodo version carries both the AUT-71 onset change and the §4 related-work paragraph, table row and bib entries. Reasons: A1 is the approved timing and says exactly this; at most one Zenodo version per problem per day; a separate correction version one day after an onset version would be churn. Adjust two phrases of §4 when inserting: the onset sentence must state the new onset (N ≥ 4,600,000; N ≥ 120^4 in the first version), and "after the first two versions of this note had been published" must match the actual Zenodo version count at publication. Executed in the AUT-71 run with tools/zenodo_newversion.py.
- B: text fixed verbatim from the approval payload in notes/forum_30_reply_akwei_20261010.txt (target: comments under our proof claim, erdosproblems.com/forum/proof-claims/386, as a reply to Akwei's 2026-10-05 comment). The approved text still says "onset N ≥ 120⁴"; it is left unchanged because the approval is verbatim and the statement is true of the published version. Posting is done by the chat-side session (browser subagent, owner's logged-in account); the coordinator container has no site login and does not seek one.
- C: unchanged (no X, no claim edit, no e-mail).

