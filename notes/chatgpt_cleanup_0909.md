# ChatGPT Pro conversation cleanup — classification, 2026-09-09

Total conversations in the account: **251**. Classified by reading the conversation list and, for
every title that was ambiguous, by opening the chat and reading its first message.

**I did not delete anything.** Deleting conversations is irreversible, so the clicks are left to
the owner. Everything below is the list to work from.

## Rule applied

Owner: "除了数学证明以外的对话我都是需要的" — everything that is not a math proof is needed.

## Back up FIRST

Before deleting, trigger ChatGPT's own export: **Settings → Data controls → Export data**.
It emails a link to a complete JSON + HTML dump of every conversation, byte-faithful, including
the 189 non-math ones as a bonus. That is a better record than anything scraped from the page,
and it is one click. Do that, wait for the mail, then delete.

Local coverage that already exists in this repo, for the automath chats specifically:

- `engine/harvest/*_raw.md` — **34 files, 580 KB, full original transcripts** (verified: the
  round-9 file matches the live page word for word, and in proper LaTeX rather than the mangled
  page rendering).
- `engine/harvest/` — about 220 further files, mostly distilled summaries (2–10 KB each).
- `engine/harvest/PRO_CHATS_OPEN.md` — the dispatch register, 22 rows, every one marked DONE
  with its harvest path.
- `lines/DIALOGUE_STATE_0829.md` — 60 conversation URLs recorded with what each round produced.

**Full original text is confirmed present for the #708 Pro rounds r5–r14.** For the rest, only
summaries are held locally — which is exactly why the export should be run first.

## DELETE — math proof work (62 conversations)

Listed newest first, with the campaign each belongs to.

| # | title | campaign |
|---|---|---|
| 1 | Prove Tuza Constant Improvement | Tuza #167 (dropped 09-08) |
| 2 | Find Grimm Conditions | Grimm #375 (dropped 09-08) |
| 4 | Prove Erdős 2n Conjecture | #708 |
| 5 | Prove Hinge Inequality | #708 |
| 6 | Fractional Hinge Threshold | #708 |
| 7 | Prove Fractional Hinge Inequality | #708 |
| 8 | Fractional Hinge Proof Search | #708 |
| 9 | Prove Fractional Hinge Inequality | #708 |
| 10 | New chat | #709 follow-up, 1 message, no reply |
| 11 | 三层系统穷举结果 | #709 layered line systems |
| 12 | Window LP Reformulation | #708 |
| 13 | Prove Or Refute Bounds | #708 |
| 14 | Analyze Erdős Problem 708 | #708 |
| 15 | Prove Sparse Core Arithmetic | #708 |
| 16 | Prove Or Refute Sparse Core | #708 |
| 17 | Counting constant proof | #708 |
| 18 | Hinge Inequality Proof | #708 round 9 — raw archived |
| 19 | Prove Fractional Hinge Inequality | #708 |
| 20 | Counting Certificates | #708 |
| 21 | Prove Hinge Inequality | #708 |
| 23 | Prove Per Prime Inequality | #708 |
| 24 | Prove Hinge Inequality | #708 |
| 25 | Erdős Problem Campaign Structure | #708 |
| 26 | Prove Split Assignment S | #708 |
| 27 | Summarize Erdős Problem Structure | #708 |
| 28 | Turn Weighted Peierls Estimate | #708 |
| 29 | Prove Infinite Path | #1212 |
| 30 | Prove Infinite Admissible Path | #1212 |
| 34 | Prove Composite Counterexample Elimination | A067720 |
| 35 | Prove Open Lemma | A067720 |
| 38 | Ranked Slot Lists | problem selection scan |
| 39 | Prove Conjecture J | k1695 |
| 40 | Verify ETP Open Problems | ETP 677 |
| 41 | Literature Search on Finite Implications | ETP 677 G2 |
| 42 | Enumerate Witness Killing Instances | ETP 677 |
| 43 | Literature novelty check | k1695 G2 |
| 45 | Literature novelty check | k1695 G2 |
| 46 | Find M5 Unsat Instances | ETP 677 |
| 47 | Fibre Four Defect Analysis | ETP 677 |
| 48 | Extend FIBRE 3 Proof | ETP 677 |
| 49 | Finite E677 E255 Status | ETP 677 |
| 50 | Analyze X6 Ucycles conjecture | ETP 677 |
| 51 | Test 2Step Conjecture | k1695 |
| 52 | Analyze Window Problem | ETP 677 |
| 53 | Prove Monotonicity Conjecture | ETP 677 |
| 54 | Prove X6 Theorem | ETP 677 |
| 55 | Search Directions | k1695 |
| 56 | K6 Wide Problem Directions | k1695 |
| 57 | Prove E677 Magma Structure | ETP 677 |
| 63 | Construct clean placements | geometry |
| 64 | Analyze Inter Row Obstruction | geometry |
| 66 | Prove Convex Polygon Bound | geometry |
| 72 | Prove Or Disprove Conjecture | ETP |
| 73 | Graph Theory Conjecture | ETP |
| 75 | Fibre Extension Conjecture | ETP 677 |
| 76 | Proof of Left Unit | ETP 677 |
| 77 | Finite Magma Construction | ETP 677 |
| 79 | Proving Right-Cancellativity of 677-Magmas | ETP 677 |
| 82 | Finite magma resolution | ETP 677 |
| 84 | Mathematical Proof Review | referee pass |
| 85 | Proof Verification Request | referee pass |
| 86 | Web-model review | referee pass |

## KEEP — everything else (189 conversations)

Not touched, not listed here except for the four that sit inside the math block and could be
mistaken for proofs. **Check these before you start clicking:**

- **#44 "Assess Opportunities Reply"** — a recruiter exchange about a Software Engineer, Ad
  Formats role. It sits between two ETP 677 chats and the title reads like a research task.
  **Keep.**
- **#83 "AI in Math Conjectures"** — a web survey of documented AI results on open problems,
  June–August 2026. It is automath reconnaissance, not a proof, and it is reusable. **Keep.**
- **#71 "Daily briefing request"** — a personal daily briefing. **Keep.**
- **#22 "超能力案件侦查"** — sits between #708 rounds. Not math. **Keep.**

Everything from #87 onward (dated 2026-08-14 and earlier) is personal and business work —
n8n, TikTok, email drafts, stock research, autism parenting, e-commerce, hardware, travel.
None of it is math. **Do not touch any of it.**

## How to delete efficiently

Open each conversation from the list, then use the "..." menu on the sidebar row → Delete.
Work top-down; the titles above are in the same order as the sidebar's default (recently
updated first), so the list tracks the sidebar as you go.
