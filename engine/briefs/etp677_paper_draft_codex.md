# CODEX TICKET (writing + verification; sol tier) — DRAFT the paper of problems/etp677/pub/PLAN_0830.md.
# Repo: $HOME/workspace/claudecode/automath. Sources of truth: the registry
# problems/etp677/campaign_registry.md (R46 STEP 16–66: grep "## R46 STEP"), the Lean project
# lean/etp677_ext (modules Ext677Fibre2, Ext677Core7Free, Ext677Core7Hand, Ext677Minimal,
# Ext677Fibre4, Ext677Amplify, Ext677Switch, Ext677Objects, Ext677Window, Ext677EprimeRed,
# AXIOMS.txt), the hand proofs problems/etp677/simple/fibre_core/handproof/proof.md and the Pro
# harvests engine/harvest/etp677_{fibre3,fibre4,ultimate,window,ucycle}_r46_pro.md (for the
# parity proof, Lemmas 1–3, the A5/group-action results, the witness), the encoders
# problems/etp677/simple/fibre_core/{core7_free.py,core_joint.py}, problems/etp677/diag/, and
# the certificates in the bucket listings recorded in the registry (STEP 48/49/60/61/63/64/65).
# Look at the previous papers' LaTeX under problems/*/pub/ (if present) for the house style and
# the AI-assistance disclosure sentence; reuse the template. English. DONE marker: DONE-PAPER1.

## Rules
- Every theorem statement must match its Lean statement or its DRAT-certified CNF exactly; cite
  the Lean theorem name (and its axiom list) or the certificate (CNF generator + sha256 + size)
  next to each result. Nothing without a certificate or a written proof may be called a theorem;
  use "verified on models" for numerical facts and "conjecture" for open items.
- Write the human proofs in full (fibre 2; fibre 3 both routes; fibre 4 Lemmas 1–3 + the finite
  lemma statement) — re-derive each step from the sources, do not paraphrase claims you have not
  checked; flag in the report every step you could not verify.
- Sharpness section: include the m = 5 witness table (engine/harvest/etp677_fibre4_m5witness_pro.md)
  and the statement "Core-10 + defect is satisfiable at m = 5 in the relaxed local system".
- Closed routes section per PLAN §7 (a)–(c); keep it factual and short; refuted intermediate
  conjectures only as remarks with their refuting model.
- No cloud costs, no engine names in the body; the methods paragraph uses the disclosure
  wording of the previous papers.
- Build the PDF (pdflatex or tectonic if available under tools/; else deliver the .tex and a
  compile log attempt).

## Deliverables
problems/etp677/pub/paper1/ (main.tex, sections/*.tex, refs.bib, figures/tables, build log,
PDF if built), a CLAIMS.md listing every theorem/lemma with its certificate pointer, and
engine/out/codex/etp677_paper1_report.md (what was verified, what was flagged) ending with
DONE-PAPER1.
