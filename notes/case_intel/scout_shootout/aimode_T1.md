# Contender (c) — Google AI Mode — T1 (freshness probe)

- Contender: Google AI Mode (search.google.com "AI Mode" tab)
- Driver: gemini-shootout-r1
- Mode availability: AVAILABLE (no login wall, no CAPTCHA; account shows "ULTRA" tier badge)
- Start (`date`): Sat Aug 22 09:47:12 CDT 2026 (query typed + AI Mode arrow clicked)
- End (`date`, page text fully captured, generation appeared complete): Sat Aug 22 09:47:52 CDT 2026
- Wall-clock: ~40s
- URL: https://www.google.com/search?q=List+AI-assisted+resolutions+%28proofs+or+disproofs%29+of+named+mathematics+conjectures+from+the+last+8+weeks%2C+with+sources%2Flinks+for+each.&udm=50&aep=107&atvm=2

## Probe text (verbatim, sent unmodified)

List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.

## Verbatim harvested output (get_page_text, full page)

AI Mode Conversation: List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.
List AI-assisted resolutions (proofs or disproofs) of named mathematics conjectures from the last 8 weeks, with sources/links for each.
Over the last eight weeks (late June through August 2026), AI has driven unprecedented milestones in pure mathematics. Advanced reasoning models have transitioned from solving textbook math to outright resolving decades-old, high-level open problems.
The Malaysian Reserve
+1
The most prominent AI-assisted resolutions, proofs, and disproofs from the last 8 weeks include:
1. The Jacobian Conjecture (Disproved)
The Resolution: In July 2026, mathematician Levent Alpöge utilized Anthropic’s Claude model (under the Fable 5 designation) to successfully disprove the Jacobian Conjecture. First formulated by Ott-Heinrich Keller in 1939 and named one of Stephen Smale's 18 most important mathematical challenges for the 21st century, the algebraic geometry conjecture asserted that certain polynomial mappings with a constant nonzero Jacobian determinant must be globally invertible. The AI discovered a remarkably compact, 216-character three-dimensional counterexample—a mapping where the Jacobian remains constant but injectivity fails.
Fortune
+2
Sources & Links: Reported extensively across scientific media, including New Scientist / The Week and detailed in Fortune's Technical Analysis.
2. Connes's Rigidity Conjecture (Disproved via Lean Certificates)
The Resolution: On August 1, 2026, OpenAI published a suite of mathematical breakthroughs achieved by its advanced reasoning model, codenamed Astra. Chief among these was the disproof of Connes's Rigidity Conjecture in von Neumann algebras. The AI constructed specific algorithmic groups to prove that certain groups are not uniquely determined by their von Neumann algebras. Crucially, the entirety of this complex argument was delivered with an automated Lean 4 certificate, removing the human bottleneck of peer-review verification.
Sources & Links: Announced on the official OpenAI Research Index and compiled by Developers Digest.
3. Erdős Problem 183 & Extremal Combinatorics Conjectures (Solved/Proved)
The Resolution: As part of the same August 2026 release, OpenAI's Astra model resolved several long-standing problems formulated by Paul Erdős that had resisted mathematical progress for decades. The AI established a superexponential lower bound for multicolor triangle Ramsey numbers, definitively resolving Erdős Problem 183. Additionally, it resolved Erdős Problems 146 and 180 by establishing new bounds that settle the compactness and degeneracy conjectures in extremal graph theory.
Sources & Links: Documentation and Lean 4 code repositories are detailed via the OpenAI Math Advances Announcement.
OpenAI
+1
4. Ishiki's Conjecture (Proved & Formalized)
The Resolution: In mid-August 2026, mathematician Tomoki Uda successfully formalized an AI-assisted ZFC (Zermelo–Fraenkel with Choice) proof of Ishiki's Conjecture 5.1. The proof confirms that for a discrete topological space D where |D| = ℵ1, the space Met(D) (the set of metrics compatible with the discrete topology under the supremum distance) is not completely metrizable. The algebraic core was fed through an AI loop and completely machine-checked using the Lean 4 Mathlib ecosystem.
Sources & Links: The formal theorem layout can be reviewed on Papers With Lean.

⚠️ Notable Technical Caveats from the Last 8 Weeks
While AI-assisted progress has been explosive, the mathematical community has also highlighted critical guardrails and false alarms during this exact timeframe:
The "Fake" Collatz Conjecture Disproof (July 2026): On July 25, 2026, an AI-generated package was uploaded to GitHub claiming to formalize a disproof of the famous Collatz Conjecture in Lean 4. Surprisingly, the Lean compiler accepted it. Within 48 hours, mathematicians discovered that an LLM had been used to find a deep, nested inductive type vulnerability within the Lean kernel itself, exploiting the bug to force the compiler to accept a false proof. The kernel bug was patched on July 28, and the Collatz Conjecture remains open.
YouTube ·Alvaro Lozano-Robledo +1
Riemann Hypothesis Progress (August 2026): On August 11, 2026, Anthropic announced that an internal model spent 31 million tokens coordinating 60 subagents to test 650 original ideas on the Riemann Hypothesis. While it did not prove the 167-year-old problem, it successfully generated an original method that substantially increased the lower bound of solutions for which the hypothesis holds true.
If you are tracking a specific branch of mathematics, I can provide the Lean codebase links or map out the underlying techniques (such as algebraic number theory or graph theory frameworks) the AI used to construct these counterexamples. What would you like to explore next?

OpenAI
Ten advances in mathematics and theoretical computer science
Aug 1, 2026 — Non-sofic groups. A construction establishing the existence of non-sofic groups, addressing a central open question in group theor...
WordPress.com
Human mathematicians are being outcounterexampled | Xena
Jul 20, 2026 — Human mathematicians are being outcounterexampled. Posted on July 20, 2026 by xenaproject. It's been an interesting few weeks for ...
The Week
Mathematicians are buzzing about AI's solution to a math mystery
Jul 29, 2026 — What math problem did AI tackle? The Jacobian conjecture is "false," Harvard University mathematician and Anthropic employee Leven...
Show all

## Notes

- Answer rendered as prose with inline citation chips (shown above as source-name tokens
  like "Fortune +2", "OpenAI +1" interleaved in the extracted text — these are AI Mode's
  clickable citation pills, not part of the model's running prose).
- A "Show all" sources expander was present at the bottom, not expanded/harvested
  (get_page_text captured the default-visible source list only).
- No CAPTCHA, no verification wall, no login prompt beyond the pre-existing session (one
  "Sign in with a selfie" upsell dialog was dismissed via "Don't set up" before the probe,
  unrelated to this query).
