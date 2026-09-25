# Sweep 1 — Qwen (chat.qwen.ai)

- Model: Qwen3.8-Max (mode: Thinking)
- Web search: YES (Web search tool explicitly enabled via composer toggle before sending)
- Timestamp: 2026-08-16 (session run; wall-clock generation ~ a few minutes, ran in parallel with ChatGPT sweep)
- Conversation URL: https://chat.qwen.ai/c/b98fa3de-6880-4223-95d4-a7e5baa04188
- Prompt sent: see sweep1_gptweb.md for the identical verbatim prompt text (same request sent to both models)

## Verbatim response (as extracted via get_page_text; citation markers like "www.quantamagazine.org" appear inline as Qwen renders footnote-style source chips next to claims — kept in place as extracted)

Thinking completed
Comprehensive Survey: AI Systems in Mathematical Research (2026)
The landscape of mathematical research has undergone a paradigm shift in 2026, moving from AI as a computational assistant to AI as an autonomous or semi-autonomous research partner. The period of June–August 2026 has been particularly explosive, marked by the deployment of unreleased models like OpenAI's "Astra" and the formalization of major open problems in Lean.
The following survey categorizes documented cases of AI solving, disproving, or advancing mathematical conjectures, with special emphasis on the June–August 2026 window.

### 1. The Erdős Problems Ecosystem
The erdosproblems.com database and the associated teorth/erdosproblems GitHub repository have become the primary proving ground for AI systems in number theory and combinatorics.

- [🌟 JUNE–AUGUST 2026] The ecosystem saw intensified activity from major tech companies throughout the summer (www.quantamagazine.org). Active problem pages, such as Problem #226 and #487, recorded new access citations and edits in June and July 2026 (www.erdosproblems.com).
- Problem #728 (Resolved Jan 2026): Terry Tao announced that this problem was the first Erdős problem solved "more or less autonomously" by an AI system (mathstodon.xyz, x.com). The system used was Aristotle, an AI theorem prover developed by the startup Harmonic.
- Problem #397 (Resolved Jan 2026): Neel Somani used GPT-5.2 Pro to generate a proof that was accepted by Terry Tao, leading to the problem being officially marked as "DISPROVED (LEAN)" (medium.com). The problem concerned products of central binomial coefficients.
- Problem #281 (Resolved Jan 2026): A 44-year-old number theory problem regarding covering congruences was solved by Somani using GPT-5.2 Pro (the-decoder.com). Tao described this event as a "most unambiguous instance of AI solving an open problem" (officechai.com).

### 2. arXiv Papers Reporting AI-Obtained Proofs
[🌟 JUNE–AUGUST 2026] The momentum from the spring continued into summer, with increased focus on "Autonomous Mathematics Research" and "AI Co-Mathematician" architectures (arxiv.org).

- "Formal Conjectures: An Open and Evolving Benchmark" (May 2026): Google DeepMind published a paper (arXiv:2605.13171) introducing a benchmark of 2,615 mathematical problem statements formalized in Lean 4, designed to test autonomous AI agents (google-deepmind.github.io).
- "AI Co-Mathematician: Accelerating Mathematicians with Agentic AI" (May 2026): This paper (arXiv:2605.06651) introduced a workbench allowing mathematicians to interactively leverage AI agents for open-ended research.
- "Resolution of Erdős Problem #728" (Jan 2026): A formal writeup of Aristotle's proof (arXiv:2601.07421) was published, documenting the first fully autonomous AI solution to an Erdős problem.

### 3. Announcements on X/Twitter by Leading Researchers
- [🌟 AUGUST 2026] OpenAI (Sébastien Bubeck): On August 1, 2026, OpenAI researcher Sébastien Bubeck announced on X that an internal model named "Astra" had solved 10 open problems in mathematics and theoretical computer science for approximately $2,000 (www.forbes.com). One of the headline results was the proof that "nonsofic groups exist," a major open question in group theory (x.com).
- [🌟 JULY 2026] Terence Tao: At the 2026 International Congress of Mathematicians (ICM), Fields Medalist Terence Tao discussed the future of AI in mathematics, outlining a five-stage evolution of AI-assisted proofs from generation to canonicalization in textbooks (www.simonsfoundation.org).
- [🌟 JUNE 2026] Quanta Profile: On June 8, Quanta Magazine published "How Terry Tao Became an Evangelist for AI in Math," detailing his shift in perspective regarding machine learning tools (www.quantamagazine.org).
- [🌟 MAY 2026] Ernest Ryu (OpenAI/UCLA): Featured on the OpenAI podcast, Ryu discussed how GPT-5 helped him solve a 40-year-old question in optimization theory regarding the Point Convergence of Nesterov's Accelerated Gradient Method (openai.com).
- [🌟 MAY 2026] Harmonic (Satnam Singh): Presented research on "Formally Verifying Hardware with Aristotle," Harmonic's AI theorem prover, at an Imperial College seminar (x.com).

### 4. News/Media Coverage
- [🌟 JUNE 2026] Nature: The journal Nature published a landmark article titled "AI cracks 80-year-old mathematics challenge" (www.nature.com). The piece detailed how an OpenAI chatbot disproved Paul Erdős's 1946 claim regarding his Unit Distance Problem, astonishing researchers by correcting a famous geometer's intuition.
- [🌟 AUGUST 2026] Forbes: Reported on OpenAI's Astra model solving 10 decades-old math problems for just $2,000, highlighting the collapsing cost of mathematical discovery.
- [🌟 JULY 2026] Phys.org: Covered the dawning "golden age" of mathematics, citing the breakthroughs of May and June as pivotal moments where AI began performing independent research.
- January 2026: Media outlets like The Decoder and Medium covered the initial wave of "Three Erdős Problems Fell in Seven Days," documenting the rapid success of GPT-5.2 Pro on the Erdős database.

### 5. GitHub Projects & Registries
- teorth/erdosproblems: Maintained by Terence Tao and Thomas Bloom, the GitHub wiki "AI contributions to Erdős problems" serves as the central ledger for verified AI breakthroughs in this domain.
- teorth/equational_theories: This project maps the relations between equational theories of Magmas ordered by finite implication. AI systems have been instrumental in exploring these "minimal equational theories" and verifying implications.
- google-deepmind/formal-conjectures: An evolving open repository of formalized mathematics conjectures in Lean 4. It currently hosts over 2,615 problem statements to benchmark autonomous research agents.
- whataifound.org: An independent registry of AI scientific discoveries that grades results on an eight-level verification scale, ranging from "formally machine-checked proofs" to "refuted claims."

### 6. Named/Famous Conjectures Settled in 2026
- [🌟 JUNE 2026] Erdős Unit-Distance Problem (1946): An 80-year-old geometry challenge was disproved by an AI system, overturning Paul Erdős's original conjecture (www.nature.com).
- [🌟 AUGUST 2026] Existence of Nonsofic Groups: A famous problem in group theory was resolved by OpenAI's Astra model, which constructed a counterexample group that cannot be approximated by finite sets (x.com).
- [🌟 MAY 2026] Nesterov's Accelerated Gradient Method Convergence: A 40-year-old question in optimization theory was answered by Ernest Ryu using GPT-5 (openai.com).
- [🌟 EARLY 2026] Convex Optimization Bounds: GPT-5 Pro independently tightened a critical bound in convex optimization from 1/L to 1.5/L, outperforming existing human-derived literature (openai.com).
- [🌟 JAN 2026] Erdős Problem #397 (Central Binomial Coefficients): A 30-year-old conjecture was disproved using GPT-5.2 Pro and verified in Lean (x.com).

(Response was truncated in the UI with a "+170" more-sources indicator; only the visible synthesized text above was captured via get_page_text — the underlying citation chips beyond what's shown were not individually enumerated.)

## Notes on search usage verification
- The "Web search" tool pill was explicitly clicked/enabled in the composer before sending (confirmed via screenshot showing blue "Web search ×" pill).
- Inline citation domain-chips (quantamagazine.org, erdosproblems.com, mathstodon.xyz, x.com, medium.com, the-decoder.com, officechai.com, arxiv.org, google-deepmind.github.io, forbes.com, simonsfoundation.org, nature.com, facebook.com, phys.org, github.com, teorth.github.io, whataifound.org, openai.com) appear throughout the response, confirming search was actually used and results were cited, not just recalled from training data.
- A "+170" indicator suggests significantly more underlying sources were consulted than are individually shown inline.
