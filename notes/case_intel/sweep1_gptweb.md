# Sweep 1 — ChatGPT (chatgpt.com) — PARTIAL / INCOMPLETE

- Model: GPT-5.6 Sol (confirmed via Advanced panel: Model = "GPT-5.6 Sol", Effort = "Pro" — both were already account defaults, explicitly verified via screenshot before sending)
- Web search: YES — explicitly enabled via the "Web search" tool tag in the composer (blue "Web search" pill visible throughout the run; confirmed active with "Searching the web" / "Searched N websites" steps appearing repeatedly)
- Timestamp started: 2026-08-16, sent in a NEW chat (title auto-generated: "AI in Math Conjectures")
- Conversation URL: [chat link removed]
- **STATUS: PARTIAL — generation did not complete.** Polled continuously (30s intervals) for well over one hour (~70+ minutes of wall-clock time) without the model producing any final synthesized answer text. Per coordinator instruction, capturing the rendered partial state now rather than continuing to wait or resending.

## Prompt sent (verbatim)

Please do a thorough web-search-based survey: ALL documented cases of AI systems solving, disproving, or making decisive progress on mathematical conjectures and open problems, with emphasis on June-August 2026 (the most recent months). Cover: (1) the Erdős problems ecosystem (erdosproblems.com, teorth/erdosproblems GitHub wiki — anything after June 30, 2026); (2) arXiv papers reporting AI-obtained proofs (search recent listings); (3) announcements on X/Twitter by researchers (Tao, Bubeck, Ryu, Aaronson, DeepMind, OpenAI, Harmonic, etc.); (4) news/media coverage; (5) GitHub projects (equational_theories finite implications, formal-conjectures resolutions, whataifound.org); (6) named/famous conjectures specifically (anything with a person's name attached that AI settled in 2026). For each case: date, problem name + how famous it is, which AI system, method, how it was verified, and source URLs. Mark clearly which cases are from June-August 2026. Be exhaustive — include minor cases too, but flag the famous ones.

## Rendered tool-use trace at time of capture (no narrative answer text ever appeared — this IS everything that rendered)

I'll build a cross-verified case table spanning Erdős resources, arXiv, GitHub, researcher announcements, and media, prioritizing primary sources and clearly flagging June–August 2026 results by evidentiary status.

- Searched 8 websites
- Searched 11 websites
- Downloaded JSON data via cURL
- (reasoning note) The June 30 Erdős AI Wiki cutoff requires reconstructing July–August activity independently; several July database status changes need attribution checks to separate AI discoveries from human or formalization updates.
- Searched 1 website
- Searched 13 websites
- Cloned Erdős Problems Repository and read the failure log
- Searched 1 website
- Searching the web (x2)
- Used container tool
- Searching arxiv.org
- Cloned the Formal Conjectures repository
- (reasoning note) Cross-checking has uncovered many less-publicized cases, including Crouzeix, Vandermonde, thin-shell, and Umans–Wang results. OpenAI's August release also exposes ten substantial Lean 4 certificates for independent checking.
- Searching github.com
- Inspected local Erdős problems YAML file
- Inspected YAML structure and recent status changes
- Parsed YAML and filtered recent updates
- Searched 1 website
- Parsed YAML problems with future updates
- Searching the web (multiple more rounds)
- Searched 1 website (x2)
- Tested Internet access to the arXiv API
- Searched 1 website
- Searching the web
- Searched 1 website
- Tested arXiv internet access
- Searching the web / Searching "Feige" "2607.14068" / Searching Scott Aaronson Jacobian AI 2026 / Searching "Maxwell conjecture is false" arxiv 2026 (specific targeted lookups)
- (reasoning note) The arXiv census now has 72 GPT-5.6 records to filter, while GitHub formalizations require actual proof certificates. I'm also searching acknowledgments and provenance for otherwise-hidden AI discoveries.
- Searching aimath.robertj1.com
- Tested internet download via curl
- Searched 1 website
- Searching openai.com
- Retrieved AI Math Page HTML
- Searching the web (still in progress at time of capture — this was the last visible step)
- Organized the survey / Organized the survey and cataloged recent cases / Cataloging summer results (these organizing steps appeared intermittently, suggesting the model made multiple passes attempting to synthesize the final answer but kept returning to search)

## Notable signal despite incompleteness

Even without a final synthesized report, the tool-trace itself surfaces real leads worth following up on directly:
- Named/keyword searches the model ran on its own initiative suggest specific June–August 2026 candidate cases: "Crouzeix conjecture" (with a search for "Crouzeix conjecture AI proof Jin 2026"), "Vandermonde", "thin-shell", "Umans–Wang" results, a "Maxwell conjecture is false" arXiv 2026 search, and "Scott Aaronson Jacobian AI 2026".
- "OpenAI's August release... exposes ten substantial Lean 4 certificates for independent checking" — matches/corroborates the Qwen sweep's finding about OpenAI's "Astra" model solving 10 problems in August 2026 (see sweep1_qwenweb.md, section 3).
- It directly cloned teorth/erdosproblems and google-deepmind/formal-conjectures GitHub repos and parsed the underlying YAML data for recent status changes — a more rigorous approach than typical web search, but this depth is likely also why the run never completed within a reasonable time budget.
- 72 candidate arXiv records mentioning GPT-5.6 were found and were being filtered for relevance at the point of capture.

## Recommendation for next sweep

This request was too heavy for a single ChatGPT Pro turn to complete in reasonable time (the agentic tool-use — repo cloning, YAML parsing, arXiv API testing — multiplied the work far beyond a normal web-search response). For a future retry, consider: (a) narrowing scope per-request (e.g. one request for June–August 2026 Erdős-only, a separate request for arXiv-only, a separate one for named/famous conjectures), or (b) accepting the Qwen sweep (sweep1_qwenweb.md) as the primary source for this round since it completed successfully with real citations, and treating a ChatGPT deep-dive as a slower, secondary corroboration pass to check back on later (the conversation URL above remains live and could theoretically still be polled/resumed in a future session — it was not stopped or discarded, just no longer actively watched).
