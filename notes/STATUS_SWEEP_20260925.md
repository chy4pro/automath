# automath status sweep — 2026-09-25 (completeness critic)

Author: a read-only completeness-critic subagent (Claude Opus 5.5), working for the Fable 5.1 coordinator.
Inputs: 14 per-line reports, each with an independent verification pass, plus primary files opened for this
sweep. This is the only file this pass wrote. No research, dispatch, publication or remote write was made.
This sweep does not rank or choose targets. That is the coordinator's job.

Status vocabulary: `kernel-verified` (a named FinalCheck/axiom record exists), `proved-refereed`,
`proved-unrefereed`, `computed-certified` (two independent methods agree), `computed-uncertified`,
`conjectural`, `refuted`, `unknown`.

Environment fact that affects every Lean claim below: in this container `/work/lean/proofenv/.lake` holds only
`config/` and `packages/`. The Mathlib cache was installed 09-25 11:31 (ledger line 1304), and **0 `.olean`
files exist for `Erdos708` or any other project module** (checked with `find`). Every "kernel-verified" label
below therefore rests on a recorded check in the old macOS environment: `FinalCheck.lean` `#guard_msgs`
blocks, replay logs, and the 09-07/09-08 recompile entries in the ledger. None of it has been rebuilt in this
container. The ledger says the smoke test was "running" at 11:31 and records no result.

---

## 1. Verifier corrections adopted

In every case where the verifier corrected the reader, the files support the verifier. I found no case where
the verifier was wrong. I added one correction that both passes missed (1188, marked NEW).

| Line | Reader said | Adopted (verifier / primary file) |
| --- | --- | --- |
| erdos708 | 11n and the barrier are "refereed" (citing README prose only); g(4)≥5, g(5)≥6 omitted | Referee file is `problems/erdos708/repo/engine_transcripts/run35_pro_r19/referee_opus.md` (+`referee_checks.py`, 66 exact checks). The 11n threshold verdict is **PASS-WITH-REPAIRS**; the barrier verdict is PASS (ledger line 861). The README line 93 values g(4)≥5 and g(5)≥6 are added as computed-uncertified. |
| erdos1212 | ML′ "refuted"; the formal-conjectures 1212.lean lemmas "kernel-verified" | ML′ is **conditionally refuted** (NOTES.md 09-03 20:4x), so conjectural. The upstream 1212.lean lemmas are third-party work (Alper Ferudun, c4b3807a, 2026-06-24) and have no build record, so they drop to proved-unrefereed. |
| k1695 | Run-11 closed 1 terminal (5 total); r0434/r0504 ch1 still open; Lean evidence in `k1695_r6_lean6..10` | Run 11 finished 17/17 with **5 SPLITOK**, so **9 terminals are closed and 12 are method-limited** (`cloud_archive_0904/k1695_r6k2/out/ALL_RESULTS.txt`, ledger 588). The Lean evidence for `krylov_det_feedback` and `krylov_reduce_of_zero` is in `engine/harvest/k1695_leanfam/REPORT.md` and registry §R6.128. |
| erdos700_770 | Tables "computed-certified" | computed-uncertified: the Kummer and gcd-order cross-checks were run by the same pipeline. |
| misc_lines | A100434, A108211, A114362, A114831, A211417, Fernandes and M77 "kernel-verified" | computed-uncertified **in this repo**: 0 `sorry` by grep, but there is no build or axiom record under `/work`. `publish/automath-papers/README.md` asserts a clean compile and clean axioms. That is a self-report, not a record reproduced here. |
| selection_notes | #1109 described as "square-sum-free subset" | #1109 is "largest A ⊆ {1..N} with A+A squarefree" (`notes/selection/thin_screen_0908.md`). |
| publications | #708 "81n (v6)"; v10 X post deleted "after v14's thread"; only the v14 thread is live | v6 was the c·lnln m constant. 81n first appeared in v10, restricted to n ≤ 10^962, and for all n in v11 (ledger 708/736/807). v10 was deleted 09-07 02:0x **after the v11 thread** (ledger 814). The owner then said on 09-08 to **keep the 09-07 v11 thread** (ledger 875). Two #708 threads are live; see §4. |
| etp677 | "~seven weeks idle"; q=7 timing 138.73 s | The last file activity was 09-06/09-08, so the line has been idle **about 2.5 weeks**. The timing detail is immaterial. |
| **erdos1188 (NEW)** | G(36) run "fate unrecorded, may still be running" (PID 11619) | **Ledger line 738 (09-05 01:53):** "G(36) job killed 20+ min past its 3600 s cap … log empty (buffered) — recorded as 'capped, incomplete', no value claimed; G(48) not started." PID 11619 belonged to the old macOS host and cannot be alive in this container. |

---

## 2. Contradictions, resolved from primary files

1. **#859 state.** The selection_notes and publications reports, the #377 row of the OPERATIONS table ("Reassess
   after the active #859 verification gate"), the "Verification queue" and "Worker seats" sections of
   OPERATIONS, and STRATEGY_RESTART §4 all treat #859 as active and awaiting review or publication.
   **Resolution:** #859 is **CLOSED (subsumed) as of 2026-09-25**. Evidence: `problems/erdos859/CLOSURE_20260925.md`,
   `G2_LITERATURE_20260925.md`, ledger line 1304, and commit `ab0f0e5` (already on `origin/main`). Hughes
   (arXiv:2609.25446) has the same upper bound. Pollack–Thompson 2013 and Weingartner 2015 give exponent 1,
   which is stronger than our 2.71 and 2.91. Consequences: in OPERATIONS, the "Verification queue" bullets 1–4,
   the "Worker seats" section (Codex screens; no Codex CLI exists in the container) and the #377 row's
   dependency are stale. STRATEGY §4 items 1 and 3 are void. Slot 1 is empty.
2. **"#859 and #377 are currently local-only"** (OPERATIONS publication gate; repeated in the publications
   report). **Contradicted by git.** `git ls-files` shows `problems/erdos859/*`, `problems/erdos377/*`,
   `problems/erdos709/*`, `lines/DIALOGUE_STATE_0829.md`, the k1695 and etp677 trees and the notes all tracked
   in `chy4pro/automath`, and `main...origin/main` shows no divergence. STRATEGY_RESTART and the 09-25 ledger
   RESTART entry describe that repo as public. So these are **public repository files, not publications** (no
   Zenodo, site claim or X). The gate text is stale. Before any further push, the coordinator or owner should
   review what is already public. The ledger contains verbatim owner quotes, chatgpt.com/qwen conversation
   URLs, a GCP project id and key-rotation to-dos.
3. **#708 X presence.** The publications report says only the v14 thread is live. Per ledger 813, 814 and 875,
   both are live: the **v11 thread of 09-07** (ids 2096853629399339126 / 2096855426855784653 /
   2096855764560130513; 81n content, now superseded; kept on the owner's instruction) and the **v14 thread of
   09-08** (2097308346374148202 / …348374827206 / …350312522030). The erdos708 report's `x` field is empty; it
   should list both.
4. **Claim-262 fix route and link.** STRATEGY §4 and §5 say the owner edits claim 262 and adds
   `…/chy4pro/automath/tree/main/lean/proofenv/Erdos708`. What happened instead (ledger line 1302 and
   `notes/dm_708_claim_update_20260925.txt`): the site has no self-service edit (Delete only), so a one-time,
   owner-authorised DM went to the moderator 09-25 11:18 with the link
   `…/erdos-708-explicit-upper-bounds/tree/main/lean`. The STRATEGY to-do is superseded by the DM. The outcome
   waits on the moderator, and the two documents cite different Lean URLs. Both paths exist.
5. **"Cached FinalCheck rerun passed during handoff"** (OPERATIONS #708 row). That rerun was on the macOS host
   (09-09). In this container no Erdos708 module has been built (see the header). `Erdos708` is also **not a
   root in `lean/proofenv/lakefile.toml`**: the roots are Proofenv plus 11 K1695 modules. A container rerun
   would therefore need `lake env lean` on `FinalCheck.lean` or a lakefile change. The label "kernel-verified in
   the recorded setup" is accurate. It has not been reproduced here.
6. **Global-memory / AGENTS.md.** AGENTS.md requires `recall_presets` before a task. OPERATIONS records that it
   timed out at the 09-09 takeover. This sweep had no global-memory tool available and did not invent a notice.
7. **misc_lines recommended "active"** for WOWII #61/#133, zc1a7, tdn and MinedS5. No file for any of them is
   dated after 2026-08-24. None appears in OPERATIONS or STRATEGY, and the STRATEGY two-slot plan does not
   include them. Honest state: **park** (dormant by omission, not an explicit decision).
8. **etp677.** The report calls issue #1464 "automath's own". `problems/etp677/OPEN_STATE.md` line 28 says "our
   issue #1464", while ledger line 379 calls it an "order-10 claim public-but-unreviewed". Attribution is taken
   from OPEN_STATE. No conflict in substance.
9. **thin_screen_0908.md** says "Four failed the hard gate at stage 8" but lists five (#160, #1063, #302, #817,
   #872). This is a defect in the source document, recorded as is.
10. **STRATEGY_RESTART vs OPERATIONS on engines.** They agree (Claude only). The OPERATIONS sentence
    "Historical note — genuine non-OpenAI alternatives included … Qwen" is residual text, not a current roster.
11. **Continuation.** OPERATIONS now says CronCreate was tested (one-shot fired 11:33Z; the ledger entry is
    uncommitted, `git diff`), with the production tick "armed after the 09-25 selection pass". That is
    consistent with the ledger. A recurring tick is **not yet armed**, so unattended operation is not yet
    claimed.

---

## 3. Gaps: directories with no report or a thin one

### /work/problems
| Path | Report? | Contents (ls + README/NOTES head) |
| --- | --- | --- |
| `erdos709/` | **none** (mentioned only inside the 700/770 report) | Erdős #709 working notes, G2.md, referee_r1.md, MILP/search scripts. Exact f(1..11)=1,2,2,2,2,3,3,3,3,3,3; f(17)=f(18)=4; f(62)≥5 (verified by `verify_s1.py`); the P30 upper bound f(n) ≤ ⌈√n⌉ passed its referee, but its 2-block core = van Doorn–Li–Tang arXiv:2603.28636. **Superseded asymptotically** by Star Fleet Math's f(n) ≤ 7(⌊n^{3/7}⌋+1), kernel-rebuilt locally 09-07 (G2.md). HOLD since 09-07; no paper. |
| `erdos859/` | none (excluded from the sweep) | Closed 09-25, see §2.1. README, LOWER_BOUND, QUALITATIVE_LOWER_BOUND, REFEREE_CLAUDE_20260925, G2, CLOSURE, scripts. The A4 weights JSON was regenerated 09-25, so the takeover-review SHA `9d1ef6…` no longer matches (ledger 1303). |
| `erdosproblems/` | none | Vendored teorth/erdosproblems DB (problems.yaml), last commit 2026-09-07. Selection input only. |
| `formal-conjectures/` | thin (used in 1188/1212) | google-deepmind upstream, checked out on **our PR branch `a211417-general-divisib…` at ad5cf02d (2026-08-24)**, not upstream main. Its content is therefore a PR snapshot. |
| `cache/` | none | Cached erdosproblems HTML pages (287, 488, 835, 1041 …) and OEIS JSON. Selection input only. |
| `parked/` | thin (misc) | Chinese parked-problem table: erdos-287, erdos-488, a63880-mod216, crystals-unique, a103425-tribonacci, krenn-gu-n6d3, conway99 (PARK-WATCH), with restart conditions. No activity since 08-17. |
| `recon/` | thin (misc) | Recon notes and verify scripts: a211417/a63880, conway99_s1, e287/e488 searches, fernandes_verify, kourovka1925_search, wowii triage. |
| `candidates.md/.json`, `ai_contributions.md`, `select_candidates.py` | none | The Erdős candidate pipeline from the August selection. Superseded by `notes/selection/*`. |
| `erdos700/`, `erdos770/` | covered via 700_770 | Pre-repo scripts and tables. |

### /work/lean
| Path | Report? | Contents |
| --- | --- | --- |
| `lean-toolchain-master/` | none | A single file named `lean-toolchain-master`, a toolchain pin artifact. |
| `proofenv/{S5Base,Smoke,Proofenv.lean,Proofenv/Basic,Scratch/Ping}` | none | Scaffolding: `Smoke.lean` = `n+0=n` with `#print axioms` (the container smoke test); `S5Base.lean` = `import Mathlib`; README is the default template. |
| `proofenv/lakefile.toml` | none | Roots = Proofenv plus 11 K1695 modules. **The Erdos708, OEIS, Fernandes, M77 and MinedS5 files are not build roots.** |
| `etp677_ext/Blitz/` | thin (mentioned in the etp677 report) | 09-05 blitz Lean: O4 Graham–Pollak and Kővári–Sós–Turán, O5 finite/infinite Ramsey, R(3,3)=6 and Schur. Sorry-free and recompiled by the coordinator 09-05 (per the ledger and the blitz README). Mathlib PRs #43482/#43483/#43488 were **closed 09-06** (AI policy, duplicates of human PRs). |

### /work/engine
| Path | Report? | Contents |
| --- | --- | --- |
| `README.md` | none | "QUARANTINE ZONE for untrusted engines" (08-22 rules for ox-alpha / muse-spark). Historical; those engines are not in the current roster. |
| `out/claude_blitz_0905/` | **none** | 9-agent blitz: #324 (x⁵+Ax⁴ never Sidon, coordinator-verified), #68 (route autopsy), #595 (structure theory, folklore risk), #23 (regime map), #1159 (k(n)≥5, novelty unchecked), #128 (O6), Lean O4/O5. Nothing published; nothing refereed except F1 (#708). |
| `out/astra_324_r1/`, `harvest/astra_324_r1.md` | **none** | Erdős #324, Astra r1 (09-07): no closure. (x+1)^5 Sidon is **conditional** on Lander–Parkin–Selfridge, which is already on the problem page. A finite box to 10^5 is clean. "Nothing to publish." |
| `harvest/erdos835_*` | **none** | Erdős #835: Steiner reformulation plus a Qwen fallback (Mendelsohn numbers of a hypothetical S(9,10,20)). The owner ordered a site comment after an audit (09-02). **It was never posted**, and the current rules now bar AI-authored community comments. |
| `harvest/tuza_r1_pro.md`, `out/pro_tuza_r1` | covered in selection_notes | #167 Tuza: correct but not new; dropped 09-08. |
| `danus/` (+ submodule `/work/danus-eval`) | none | 08-24 evaluation of the Danus harness on ox-alpha via a GCP VM: toy target accepted in round 1, then throttled (429). Historical; GCP is retired. |
| `gcp/` | none | k1695 run-8..11 launch/startup scripts and zlift worker. Historical; GCP is retired. |
| `briefs/` (308), `harvest/` (286), `out/` (25), `logs/`, `scripts/`, `cache/vm_dataset.json` | thin (indirect) | Engine prompts and outputs for all lines. `scripts/qwen_ui_dispatch.py` and the other Qwen/codex drivers are obsolete under Claude-only. `cache/vm_dataset.json` is the VibeMathed G2 cache (689 entries, 09-07). |

### /work/publish
| Path | Report? | Contents |
| --- | --- | --- |
| `automath-papers/batch1/` | via publications | OEIS quartet paper (tex/md/pdf). |
| `automath-papers/fernandes/` | via publications | Fernandes paper (tex/md/pdf). |
| `automath-papers/lean/` | via publications | "Moved" stub pointing to chy4pro/automath-lean-proofs. |
| `automath-papers/wowii133/` | thin | Single-version PDF, record 22054835, md5 checked 08-23. No LaTeX source stored. |

---

## 4. Publication inventory

"Local record" means what the files in /work say. Nothing was checked live on the web in this pass.

### Zenodo
| DOI / record | Line | Local record status |
| --- | --- | --- |
| 10.5281/zenodo.22267395 (concept) → v14 10.5281/zenodo.22660853 (09-08) | #708 | **Current.** v1–v9 records (22267396…22293074, incl. v5 22287131) edited in place as "Superseded" (ledger 741). v10–v13 are superseded by v14; their record numbers are not in the files read. The repo has 5 GitHub-only commits after v14 (Section 19, verification stack) that are not on Zenodo, by design. |
| 10.5281/zenodo.22186784 | k1695 | Current (the only deposit; aI+bJ theorem; "problem remains open"). |
| 10.5281/zenodo.21995715 | A211417 | Current record, but **the published PDF carries the uncorrected Corollary 3.8 coverage wording**. The correction exists only in the source (since 08-23). |
| 10.5281/zenodo.21995453 | OEIS quartet | Current. Priority for A114831 ceded to Kitamura (FC PR #4969). |
| 10.5281/zenodo.21995604 | Fernandes | Current. Priority ceded to Kitamura (FC PR #4868). |
| 10.5281/zenodo.21995799 (concept) → v8_2 22070405 | ETP-677 structure | v8_2 current (a correction release). 21995800 (v7.2), 22054879 (v8) and 22069570 (v8_1) are superseded. Internal name v9/v10 vs public v8_1/v8_2 (commit 061cfcb). |
| 10.5281/zenodo.22054650 (concept) → v2 22069069 | WOWII-61 | v2 current (correction). v1 22054651 is superseded and marked "should not be relied on". |
| 10.5281/zenodo.22054835 | WOWII-133 | Current, only version, no correction. |
| `10.5281/zenodo.TODO` (placeholder) | etp677 fibre-size package (`problems/etp677/pub/github`) | **Not deposited.** Staged only. |

### GitHub (owner chy4pro unless noted)
| Repo | Line | Status |
| --- | --- | --- |
| automath (main, public per STRATEGY) | all | Current. Contains the #859/#377/#709 notes, ledger and k1695/etp677 trees (see §2.2). |
| automath-papers | A211417, quartet, Fernandes, ETP-677, WOWII | Current (061cfcb). |
| automath-lean-proofs | OEIS/Fernandes/A211417 Lean | Exists per README. Not fetched; no local build record. |
| erdos-708-explicit-upper-bounds | #708 | Current (8b9c1c1, in sync with origin). The README "v1–v13 changelog" line is stale relative to v14. |
| erdos-693-divisor-gaps | #693 | Current (19d0c55). |
| erdos-1189-irreducible-covering-sets | #1189, #1188 G(x) addendum | Current (1bbd77a). |
| erdos-1212-arithmetic-percolation-notes | #1212 | Current (c5dc65c). Notes only, "NO theorem". |
| erdos-357-distinct-block-sums | #357 (+ #463 secondary data) | Current (8ff17d1). |
| erdos-128-sparse-halves | #128 | Current (93e78de). Relabelled as a re-verification of Cormundus's 07-26 values. |
| erdos-700-770-tables | #700, #770 | Current (2c8ea90). |
| kourovka-16-95 (releases v1–v1.3) | k1695 | Current. Not a submodule here. |
| Community: formal-conjectures PR #5023 (A211417); #5027/#5029 (mentioned in `notes/methodology.md`); issue #5025 (A100434 sign error) | OEIS lines | **Status unknown.** Last local note is 08-24. The local submodule sits on the PR branch. |
| Community: Mathlib PRs #43482, #43483, #43488 | Blitz Lean | **Closed 09-06** (triage/AI policy; duplicates). An owner apology on #43483 was pending (ledger 796). |
| Community: ETP issue #1464 | etp677 | Open as of 08-23, no maintainer response. |

### erdosproblems.com
| Item | Line | Status |
| --- | --- | --- |
| Proof claim (claim_id 262, submitted 09-05, public by 09-05 12:02; kind partial, verdict "other", `lean_url` empty) | #708 | **Stale summary (pre-v14).** Update requested by DM 09-25 11:18. Moderator action pending. |
| Comment 09-04 00:39 | #708 | Approved 09-04 05:09, public. |
| Comments 09-04 11:33 (v3) and 09-04 15:12 (v5) | #708 | Not approved. `problems/erdos709/NOTES.md` says the v5 comment "no longer appears … presumably rejected". |
| Comment 09-07 06:49 (v11, 81n) | #708 | Not visible as of 09-09 (50 h+). Decision: do not chase (ledger 910–912). |
| Moderator DM thread (moderator's 04 Sep DM; our 09-25 reply) | #708 | Sent. The reply was a one-time owner authorisation, not a standing permission. |
| Comment 09-04 (G(x) computation) | #1188 | Approved 09-04 06:19, public (self-report; not re-verified). |
| #835 Steiner reformulation comment | #835 | **Never posted** (draft `engine/harvest/erdos835_comment_draft.md`). Now barred by the no-AI-community-communications rule. |
| No claims or comments | #859, #377, #709, #128, #357, #693, #700/770, #1189, #1212, #324 | none |

### X (@HaoyuChn)
| Post | Line | Status |
| --- | --- | --- |
| v14 thread 2097308346374148202 / 2097308348374827206 / 2097308350312522030 (09-08) | #708 | **Current.** |
| v11 thread 2096853629399339126 / 2096855426855784653 / 2096855764560130513 (09-07) | #708 | **Live but superseded** (81n). Kept on the owner's instruction 09-08 (ledger 875). |
| v1–v6, v8, v9 (8 posts; deleted 09-05) and v10 2095766497201119553 (deleted 09-07) | #708 | Deleted. |
| 2094286298366275893 | k1695 | Live, current, hedged ("remains open"). |
| none | all other lines | none |

### Other
- Prove2Me private mission 5204b3d1 (#708 sparse core): goal theorem accepted 09-07 04:57. Private, not a public artefact.
- Dashboard: claude.ai artifact b3511490-… (source `notes/automath-dashboard-src.html`). Stale since about 09-08 per OPERATIONS.
- OEIS: the #1189 I(k) draft (`problems/erdos1189/OEIS_DRAFT.md`) was **never submitted** (no OEIS account).

---

## 5. Portfolio table

"Honest state" is this critic's reading of the files, not a recommendation to work on a line. The table is not
ranked.

| Line | Best verified result (status) | Lean | Published? | Last activity | Verified next step | Blockers | Honest state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Erdős #859 | Explicit upper bound with onset t ≥ 8100 (proved-refereed). Lower-bound exponents 2.91 (effective) and 2.71 (qualitative), refereed 09-25. **Subsumed** by Hughes 2026 and Pollack–Thompson 2013 | none | No (repo files public, no publication) | 09-25 11:4x closure | None (CLOSURE_20260925.md) | none | **closed** |
| Erdős #708 | g(n) ≤ 12n (kernel-verified, recorded setup); 81n/33n/19n kernel-verified; 11n proved-refereed (PASS-WITH-REPAIRS); c<2 barrier proved-refereed (PASS); g(4)≥5, g(5)≥6 computed-uncertified; 2n open | FinalCheck.lean pins 7 axiom sets; H97 replay PASS; **not rebuilt in this container**; Erdos708 not a lakefile root | Zenodo v14, GitHub, claim 262, 2 X threads | 09-25 11:18 DM | Moderator applies the DM (external); optional container rebuild of FinalCheck | Moderator; 11n formalisation depended on Astra (gone); route floor 4n | **park** (idle, published) |
| Erdős #377 | D2: EGRS 1975 Thm 4 direction correction (computed-uncertified; README says it needs a second referee). D3: saturation barrier for the termwise-Mertens method (computed-uncertified). D1 (explicit c′<1) empty | none | No (repo files public) | 09-09 03:0x | Referee D2 **or** supply the named effective prime-distribution input | No method for D1; D3 barrier | **park** |
| Erdős #709 | f(1..11), f(17)=f(18)=4, f(62)≥5 (computed, verify_s1.py); f(n) ≤ ⌈√n⌉ (proved-refereed, but its core is published and the result is asymptotically superseded by SFM's 7n^{3/7}) | none (SFM's Lean rebuilt locally 09-07; not ours) | No (repo files public) | 09-07 05:18 | Only if a new idea: multi-slice projection inequalities to beat 3/7 (G2.md) | Superseded; active external group | **park** (HOLD) |
| Erdős #693 | Max-gap tables k=2 n≤22930, k=3 n≤600 (computed-uncertified; 10001–22930 not cross-checked) | none | GitHub | 09-04/05 | Only data extension | none; no proof route | **park** |
| Erdős #1189 | I(k) k≤8 = 0,0,0,0,1,4,15,65 (computed-certified, SAT+DFS; verifier rerun 85/85); private-prime-power lemma (proved-unrefereed) | none | GitHub | 09-04 | Owed G2 (Krukenberg/Simpson/Sun **and the StarFleetMath "Solution Proposed" listing**, ledger 801) before any OEIS step | k=9 is algorithmically out of reach; no OEIS account | **closed** (published table) |
| Erdős #1188 / #463 | G(x): 0 (x<12), 1 (12–23), 5 (x=24) exhaustive (computed-certified); G(36..96) lower bounds only. #463: F(n) to 2·10⁶ (computed-uncertified) | none (upstream 1188.lean is a different quantity, `sorry` locally) | GitHub (inside the 1189 and 357 repos); #1188 site comment | G(36) killed 09-05 01:53 (ledger 738) | Only a cheap retry of G(36) with an honest cap | none | **park** |
| Erdős #1212 | L1–L13 (computed-uncertified); open question "disjoint Jacobsthal"; ML′ conditionally refuted | none of ours | GitHub (notes, "NO theorem") | 09-03 | none | Peierls route dead | **closed** (method limit) |
| Erdős #357 | f(n) n≤53 (computed-uncertified; brute-force cross-check n≤22) | none | GitHub | 09-03 | none planned | none | **park** |
| Erdős #128 | β for 4 SRGs (computed-uncertified; a re-derivation of public values) | none | GitHub (relabelled) | 09-05 (repo), 09-08 (rejection) | none | Flag-algebra frontier; existing claim | **closed** |
| Erdős #700 / #770 | Tables n≤2000 / n≤1000 (computed-uncertified); #770 identity false in general per data | none | GitHub | 09-03 | none planned | none | **park** |
| Erdős #375 (Grimm) | Elementary k ≤ 2+log n/log 4 (computed-uncertified; weaker than 1962/1975) | none | No | 09-08 | none | Frontier needs Baker theory | **closed** |
| Erdős #167 (Tuza) | LP f(c)=(12c+30)/(4c+11) (correct, not new) | none | No | 09-08 | none | Already in the target paper | **closed** |
| Blitz 09-05 (#324, #68, #595, #23, #1159) + Astra #324 r1 | #324: x⁵+Ax⁴ never Sidon (coordinator-verified); others are route maps or unchecked novelty | Ramsey/Schur/Graham–Pollak/KST sorry-free (recompiled 09-05, macOS) | No (Mathlib PRs closed) | 09-07 (#324 Astra) | none recorded | Novelty and G2 unchecked | **closed** (unreported, see §3) |
| Kourovka 16.95 | aI+bJ theorem, all fields (computed-certified + analytic proof, proved-unrefereed); GL(n,q) census 1.7M, 0 counterexamples; R6: 9 terminals closed, 12 method-limited | 2 supporting lemmas kernel-verified (leanfam REPORT) | Zenodo 22186784, GitHub v1–v1.3, X | 09-04 23:05 (GCP shutdown) | Coordinator decision: mark R6 exact-d_S permanently method-limited, or re-plan without GCP | GCP retired; no general-A route | **park** (needs explicit decision) |
| ETP-677 (+ etp_o5 / E17260) | Minimal counterexample is simple or all fibres ≥5 (kernel-verified modulo one named `bv_decide` axiom for fibre 4); q=3/4/7 branch certificates kernel-verified (native_decide); E17260 UNSAT n≤6 (computed-uncertified); E677⟹E255 open | etp677_certs, etp677_ext (AXIOMS files) | Zenodo v8_2 (structure paper); fibre package **not deposited** | ~09-06 | Deposit the staged package (placeholder DOI) after a cold `verify.sh`, **or** record a no-deposit decision | Register A open; E17260 n≥7 needed GCP | **park** |
| OEIS quartet / A211417 / Fernandes / M77 | Theorems with Lean (computed-uncertified here: 0 `sorry`, no local build record; publication README claims a clean compile) | 7 files, 0 `sorry`, not build roots | Zenodo ×3; automath-lean-proofs; FC PR #5023 | 08-24 | A211417 corrected PDF (pending since 08-23); check FC PR #5023 status | Priority to Kitamura on 2 of them | **closed** (published) |
| WOWII-61 / WOWII-133 | Partial results (published v2 / v1); S3_TAIL lemma clean; #291 refuted externally | none | Zenodo ×2 | ~08-24 | none recorded | Needs a non-Qwen verifier for #133 fragments | **park** |
| zc1a7, tdn_2606_27961, MinedS5 | Reproductions / small computations; MinedS5 is a statement-only stub (1 `sorry`) | MinedS5 stub | No | ~08-24 | Named open sub-items only | none | **park** |
| Parked backlog (287, 488, a63880, crystals, a103425, krenn-gu, conway99) | none new | none | No | 08-17 | Restart conditions in parked/README | as listed | **park** |
| Selection pipeline | thin_screen 09-09: survivors #377, #859 (now closed), #1084, #1109. G2 procedure amended 09-25 (literature on the quantity itself) | n/a | n/a | 09-25 (#859 G2 lesson) | Coordinator's 09-25 selection pass (slot 1 empty). Site-state re-checks are stale (09-09) | none | **active** (process, not a math line) |

---

## 6. In flight at the 2026-09-09 handoff, and still not closed

Sources: `lines/DIALOGUE_STATE_0829.md` (last 120 lines) and `notes/CODEX_TAKEOVER_REVIEW_20260909.md`, plus
the older open items those documents point to. Ledger lines 1306–1327 below the `12:3x CHROME RESET` anchor
are **obsolete 08-29-era text** (Chrome tab ids, GCP VMs, 677 R46, k1695 R6, ~20-min tick routine). OPERATIONS
flags them as not current, so they are not in-flight work.

Closed since 09-09 (listed for completeness):
- #859 A4/A5, cross-vendor review of B′, the qualitative derivation and "first proof" wording: closed 09-25
  (Claude referee, then G2 subsumed). The `8*4^delta` typo is fixed (README line 165). A4 weights JSON was
  regenerated 09-25; the takeover-review SHA is stale (a record note, not an error).
- The question to the owner about an independent Claude referee was overtaken by the 09-25 Claude-only restart.
  OPERATIONS still lists it as pending (stale text).
- Unattended continuation: CronCreate one-shot tested 09-25. A recurring tick is not yet armed (see §2.11).

**Still open, never closed out:**
1. **Owner-only items** (09-09 list; OPERATIONS still carries them): ChatGPT account export-then-delete (62 to
   delete, 189 to keep); Prove2Me key rotation; Lean FRO comparator and nanoda (open since 09-07). The
   "codex_apps MCP recovered?" item is moot now that Codex is gone.
2. **#708 Section 18 (11n) formalisation.** It was deferred to "after the Astra reset 14 Sep" (ledger 882/889)
   and never started. Astra is not in the current engine roster.
3. **#708 09-07 site comment.** Never visible. The 09-09 decision was not to chase it. The live claim summary
   stays stale until the moderator acts on the 09-25 DM.
4. **Owner apology on Mathlib PR #43483** (09-06, owner action). Status unknown.
5. **Worker seats `2185.codex` / `61406.codex_b`.** Listed in OPERATIONS as idle and "recheck before future
   input". They ran on the macOS host and cannot be reached from this container. The section should be retired.
6. **Dashboard.** It was stale at 09-09 and is still stale.
7. **#859 and #377 "local and unpushed"** at 09-09. Both are now in the public main repo (§2.2). No privacy or
   scope decision was recorded before the push.
8. **Global-memory recall timeout and the revoked web-lookup token** (takeover review). Neither is recorded as
   resolved.
9. Older open items the handoff carried implicitly:
   - #1189 G2 and OEIS (owed since 09-02; StarFleetMath signal since 09-07).
   - The k1695 run-12 / R6 decision (since 09-04).
   - The etp677 package deposit and E17260 orders 7–16 (since about 09-06).
   - The A211417 corrected PDF (since 08-23).
   - FC PRs #5023/#5027/#5029 (last touched 08-24).
   - The #835 site comment (owner-ordered 09-02, never posted, now barred).
   - #709 "route idea" (09-07, never started; line on HOLD).
10. **New since 09-25 and not yet resolved.** The container Lean smoke test, and the absence of any container
    build of Erdos708 FinalCheck. The ledger records the cache install at 11:31 and no result.
