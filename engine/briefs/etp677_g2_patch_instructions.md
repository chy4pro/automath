# G2 PATCH INSTRUCTIONS (line-677, verified sources) — apply EXACTLY; nothing else changes.
# Sources verified by line-677 on 2026-08-30 from the live pages: Blueprint Chapter 13
# (Lemma 13.1 left multiplications invertible; §13.1 pair-indexed extension (x,s)◇(y,t) =
# (x◇y, s◇_{x,y}t) with its functional equation; Type II examples 4x+3y and 4x+y on F_7;
# Lemma 13.4: a magma on G×M satisfying 677, G an E677+E255 magma, M an abelian group,
# (x,s)◇(y,t) = (x◇y, α_{x,y}s + β_{x,y}t + c_{x,y}) ⇒ G×M satisfies 255); ETP paper arXiv
# 2512.07087 v2 (2025-12-16; 34 authors; states the project could not prove or disprove
# E677 ⊧_fin E255); GitHub issue #1464 (open, 2026-07-22, "Equation 677 -> 255: Lean orbit
# lemma and DRAT-certified order-10 exclusion", 45 orbit cases, Glucose 4.2 + drat-trim,
# 2.8 GB certificates NOT publicly hosted, "does not resolve the full finite implication").
# NOT verified and therefore NOT to be cited: Bonatto–Fioravanti "Lemma 2.3 congruence-uniform"
# (no such statement found in arXiv 2004.05368), Bonatto–Stanovský, Dančo et al., any claim
# about which orders have been exhausted by Mace4 (not found in the ETP paper text).

## 1. main.tex — abstract
After the sentence "We prove that a minimal finite counterexample is simple, or every class of
every proper nontrivial congruence has at least five elements." insert:
"The size-two exclusion is implicit in the linear-extension lemma of the project blueprint; the
size-three and size-four exclusions are new."

## 2. main.tex — bibliography
Replace the \bibitem{etp} entry by:
\bibitem{etp}
M. Bolan, J. Breitner, J. Brox, N. Carlini, M. Carneiro, et al. (34 authors),
\emph{The Equational Theories Project: Advancing Collaborative Mathematical
Research at Scale}, arXiv:2512.07087v2, December 2025.
\url{https://arxiv.org/abs/2512.07087}.
Keep \bibitem{blueprint} unchanged. Add after it:
\bibitem{issue1464}
Equational Theories Project repository, Issue \#1464, \emph{Equation 677 -> 255:
Lean orbit lemma and DRAT-certified order-10 exclusion}, opened 22 July 2026,
\url{https://github.com/teorth/equational_theories/issues/1464}
(open at the time of writing; certificates not publicly hosted).
(Change \begin{thebibliography}{9} to {99} only if needed for label width — it is not.)

## 3. sections/01_introduction.tex
After the sentence "Nothing in this paper settles it." (end of the first paragraph) insert
a new paragraph:
\paragraph{What is known.}
Finite $E677$ magmas are left quasigroups: every left translation is
invertible \cite[Lemma~13.1]{blueprint}.  The project blueprint studies
$E677$ through pair-indexed extensions
$(x,s)\oplus(y,t)=(x\oplus y,\;s\oplus_{x,y}t)$ of a base magma and proves
that every \emph{linear} extension of an $E677+E255$ base satisfies
$E255$ \cite[\S13.1, Lemma~13.4]{blueprint}.  A two-element fibre is
automatically affine over $\F_2$, so Lemma~13.4 already excludes classes of
size two in a minimal counterexample; Theorem~\ref{thm:fibre2} records a
short self-contained proof of the slightly stronger statement that no
$E677$ extension with two-element fibres exists at all.  The exclusion of
size three (Theorem~\ref{thm:fibre3}), the exclusion of size four at a point
where $E255$ fails (Theorem~\ref{thm:fibre4}), and therefore
Theorem~\ref{thm:headline}, are new to our knowledge.  A public issue in the
project repository reports a DRAT-certified exclusion of counterexamples of
order ten by an orbit case split \cite{issue1464}; that computation had not
been integrated or reviewed at the time of writing and nothing here depends
on it.

## 4. sections/02_preliminaries.tex
(a) Immediately before "\begin{lemma}[equal fibres]" insert the sentence:
"The next lemma is elementary; we state it because the Lean development uses it."
(b) After equation (2.2) and the sentence "There is no affine, separable, or gauge assumption
in (2.2)." insert:
"Equation (2.2) is the pair-indexed extension form of the blueprint
\cite[\S13.1]{blueprint}, and (2.3) below is its functional equation read
from the outside inward."

## 5. sections/03_fibre2.tex
After the final paragraph ("The proof is gauge-free: ...") append:
"After coordinatisation, (3.1) is a linear extension in the sense of
\cite[Lemma~13.4]{blueprint}, which yields $E255$ for the total magma and
hence also excludes a two-element class in a minimal counterexample.  The
argument above shows more: no $E677$ magma with two-element fibres over an
$E677+E255$ base exists, whether or not it satisfies $E255$."

## 6. sections/06_sharpness.tex
After the proof of Proposition~\ref{prop:powers} append:
"The proposition is the routine direct-product remark; its only content is
that the defect survives the product."

## 7. sections/07_closed_routes.tex
In the paragraph after Theorem~\ref{thm:switch} (beginning "The theorem supplies controlled
idempotent-free ..."), replace its first sentence by:
"The two base laws $4q+r$ and $4q+3r$ on $\mathbb Z/7\mathbb Z$ are the
blueprint's order-seven examples \cite[\S13.1]{blueprint}; the switching
construction over them is ours, and it supplies controlled idempotent-free
$E677+E255$ models in which seemingly promising pointwise patterns fail."

## 8. sections/08_amplification.tex
After the final paragraph ("This reduction does not decide the implication. ...") append:
"Theorem~\ref{thm:amplify} is elementary; it is stated only to make the
density strategy precise."

## 9. Announcements (problems/etp677/pub/announce/, not in the freeze but owner-facing)
x_thread.md: in the post that lists the three exclusions, add the clause
"(size two is implicit in the ETP blueprint's linear-extension lemma; three and four are new)".
zenodo.json description and arxiv_abstract.md: add the abstract sentence from item 1.
github_release.md: same clause once.

## 10. Do not change
CLAIMS.md (claims unchanged), any theorem statement, any Lean pointer, the author line, the
date. Then: one PDF rebuild, mirror to pub/github/paper, grep-zero (engine names, dialogue,
registry, home paths, gs://, automath-compute, harvest), DONE-PATCH-PAPER.
