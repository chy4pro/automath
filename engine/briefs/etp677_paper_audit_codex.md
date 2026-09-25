# CODEX TICKET (adversarial audit; sol tier; FRESH context — do not reuse the drafting screen)
# — gate G1 for Paper 1. Repo: $HOME/workspace/claudecode/automath. Input: the draft
# problems/etp677/pub/paper1/ (main.tex, sections/, CLAIMS.md) once DONE-PAPER1 exists; sources of
# truth: lean/etp677_ext (rebuild it yourself; run #print axioms yourself), the certificate
# bundle problems/etp677/pub/bundle/ (rerun the small checks yourself), the registry only to
# locate evidence — never as evidence. DONE marker: DONE-PAPERAUDIT.

## Your job: try to break the paper
1. For every theorem/lemma/proposition: locate the cited Lean theorem or certificate; check the
   STATEMENT in the paper matches the formal statement exactly (hypotheses, quantifiers, the
   universe of the quotient, "some class" vs "all classes", the defect hypothesis); check the
   axiom list claim (clean vs one certificate axiom); flag any mismatch as BLOCKER.
2. For every written proof: re-derive it independently (fibre 2; fibre 3 both routes; Lemmas
   1–3 of fibre 4; the equal-fibres lemma; the switching theorem; the density lemma). Try to
   construct counterexamples to any step with a small model (F31, T7, 4x+3y, M49ε, M217ε, R217,
   the db tables in problems/etp677/ext/db/) — every identity used must hold on all of them.
3. Check the sharpness section: re-verify the m = 5 witness with your own code; check that the
   paper does not overclaim (the witness is a LOCAL relaxed-system solution, not a magma).
4. Check the closed-routes section: the A5 orbit count and cover logic; the S3…F21 claims are
   solver results without independent certificates except A4 — the paper must say so.
5. Leaks: no owner e-mail, no engine/model names in the body, no cloud cost details, no
   internal registry references; the AI-assistance disclosure sentence present and identical in
   spirit to the previous papers.
6. Literature: any statement about prior art must be hedged unless sourced (G2 supplies sources).
## Deliverables
engine/out/codex/etp677_paper1_audit.md: BLOCKER / MAJOR / MINOR list with exact locations and
the fix for each; a final verdict (READY / NOT READY); ending with DONE-PAPERAUDIT.
