# CASE INTAKE SOP (v5, 2026-08-24 — the standing "absorb what works" loop)
Owner question that created this: "is there a method to CONTINUOUSLY absorb successful AI
cases and apply them?" The pieces existed; v5 removed the daily carrier. This page is the
carrier. Executed by the dialogue session; steps are cheap and mechanical.

## DISCOVERY (owner cadence ruling 08-24: standing DAILY scan, exactly once per day)
- DAILY CASE SCAN (dialogue tick; state file logs/case_scan_last, skip if <24h): a bounded
  sweep for new AI-solved-mathematics cases OUTSIDE arXiv — web search (recent-days queries:
  AI/LLM + conjecture/proof/counterexample/solved), X/blog/self-hosted-PDF channels (the S^6
  lesson: major claims announce there first), optionally one Gemini search seat (search-only
  rule compliant). Minutes, not hours; findings become intake EVENTS.
- Self-hosted AI claim boards (added 09-07 after the #709 miss): VibeMathed dataset/RSS (tools/vm_g2.py
  --refresh; new 'partial/candidate' Erdős rows are intake EVENTS) and starfleetmath.com (tools/sfm_g2.py).
- arXiv daily watch (tools/arxiv_daily_watch.py): resolution + positive + ai-disclosure arms
  cover the arXiv side automatically; flagged AI/resolution papers = intake EVENTS.
- Owner-verbal intel = an intake EVENT (rule R6: same-session cases.md entry, never just a
  citation in a planning doc).
- pub-watch feedback and line-session discoveries (e.g. E23-style sweeps) = intake EVENTS.

## INTAKE (per event, same tick it arrives — 3 steps, ~minutes)
1. CASE ROW: append to notes/case_intel/cases.md (date | problem+fame | system | method |
   verification | source | lesson). PENDING-source stub if the primary source is not yet
   visible. Wrong-attribution risk: verify AI-credit against the PRIMARY source (F1 trap:
   DR summaries misread object names as collaborators).
2. TRANSPLANT SCAN: does the case carry a portable element? Four bins:
   - prompt element -> prompts/case_prompt_archaeology.md + templates.md
   - scaffold/method -> a scaffold file (model: cdc_style_scaffold.md)
   - verification trick -> VERIFY_CHECKLIST margin note (checklist itself stays frozen;
     accumulate, fold in at the next authorized revision)
   - process pattern -> ARCHITECTURE/SELECTION amendment PROPOSAL (owner approves)
3. SHELF MATCH: run the new case against notes/selection/famous_watch.md unlock conditions;
   flag RE-SCORE rows for the next selection task (SELECTION.md trigger).

## ABSORPTION IS EVENT-DRIVEN (owner ruling 08-24: no weekly batch)
Method absorption happens AT INTAKE TIME, whenever a new case lands — as part of the same
event, not on a schedule: prompt archaeology if the case has published prompts/transcripts;
capability-prior recalibration if it moves a class prior (model: recalibration_ytd.md);
miss-comparison reflection (retrospectives.md R-series) if we neither recorded nor attacked
a famous result; transplant bins and shelf match per INTAKE above. A case with nothing
portable gets a cases.md row and nothing else — do not manufacture absorption.

## EVIDENCE THIS LOOP PAYS (why it stays funded)
- CDC scaffold absorbed 08-16 -> our campaign methodology (root/family structure of line-677).
- Feige case prompt element ("carpet-search literature first") -> prompt templates.
- YTD case -> recalibration of construction-type priors -> SELECTION.md prior.
- Alpoge S^6 case (today) -> certificate-first packaging + race clock + FAMOUS-WATCH shelf.

## PROMPT ARCHAEOLOGY (owner rule, 2026-09-01) — mandatory for every new case
For each newly intaken AI-solved-conjecture case: try hard for the VERBATIM prompt (authors often
publish it — GitHub repo, appendix, X thread; Jin's Crouzeix prompt was in the repo root). Save it to
notes/case_intel/scaffolds/<case>_prompt_verbatim.txt. Then run a line-by-line comparison against our
current briefs, write the delta into memory feedback-prompt-doctrine, and APPLY it to the NEXT dispatch
(never mid-flight: running sessions finish untouched). Summaries are not a substitute for the原文.
