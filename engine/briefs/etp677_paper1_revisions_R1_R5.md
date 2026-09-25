# CODEX TICKET (sol) — PAPER 1 revisions R1–R5 from the owner line's first grade (STEP 69). Paper source:
# problems/etp677/pub/paper1/ (main.tex, sections/*.tex, refs.bib, CLAIMS.md). Keep every theorem statement,
# axiom list and number unchanged. Rebuild the PDF at the end (tectonic; ONE build; no lake builds).
# DONE marker: DONE-PAPER1R. Report: engine/out/codex/etp677_paper1_revisions_report.md (list every edit with file:line).

R1 Remove EVERY internal reference from the paper and CLAIMS.md: strings like "registry R46 Step …", "STEP nn",
   "dialogue encoding", "dialogue", "*_dialogue.py", "engine/harvest/…", "engine/out/…", "problems/etp677/…" paths,
   bucket/prefix names (gs://, ext12, ext13, ext14, ext15, "/out"), screen/engine names (codex, luna, Pro, Qwen,
   ChatGPT, kissat-on-VM wording is fine but not VM names). Replace by public-repo artifact names as laid out by the
   GitHub package (sat/…, witness/…, lean/…, models/…, certificates/…) and by the phrase "an independent second
   implementation" where the dialogue's checkers are meant. grep the whole tree for the forbidden strings afterwards
   and list zero hits in the report.
R2 The full sha256 of the eight archived big proofs (three fibre-4 DRATs: jdef_m4 in-family, the second-implementation
   m=4+defect proof, the C8+defect proof; five A5 residual proofs) will arrive at gs://[gcp-project]/hashes/hashes.txt
   (produced by a hash VM). Poll `gsutil cat gs://[gcp-project]/hashes/hashes.txt` once per minute for up to
   30 minutes; when present, insert the hashes into §9 (certificates table) and CLAIMS.md and DELETE the "archive gap"
   wording. If the file has not appeared after 30 minutes, leave a clearly marked placeholder row "<sha256 pending>" and
   say so in the report — do not invent hashes.
R3 Fix the LaTeX typo "qquad" (missing backslash) in sections/06_sharpness.tex (the defect chain display); check the
   whole source for the same pattern (grep -n 'qquad' with no backslash).
R4 Keep the wording "relaxed local system" wherever the m=5 witness is mentioned (verify; do not weaken).
R5 Methods/disclosure sentence: find the verbatim sentence used in the previous papers (search the public repo
   chy4pro/automath-papers locally if cloned, else grep problems/*/pub/ and notes/ for "disclosure" / "were produced by"
   / "automated"); if absent from Paper 1, add it verbatim to §1 or §9. Report which sentence and where.
Constraints: no owner e-mail, no engine names, no internal paths; the implication 677 ⟹ 255 stays OPEN in every sentence.
