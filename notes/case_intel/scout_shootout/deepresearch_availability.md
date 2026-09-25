# Contender (b) — gemini.google.com Deep Research — AVAILABILITY FINDING

- Contender: Gemini Deep Research mode
- Driver: gemini-shootout-r1
- Investigation window: `date` start 09:41 CDT 2026-08-22 -> end 09:47 CDT 2026-08-22
- Account: Roy Chen (the user's private Gmail address (literal never written in this repo)), signed in, Gemini "Pro" tier visible
- URL probed: https://gemini.google.com/app

## Finding: Deep Research is NOT exposed in this account's current Gemini web UI

Thorough search of the UI surfaced no "Deep Research" control anywhere:

1. **Mode picker** ("Open mode picker, currently Pro" button next to composer) — opened
   and enumerated via accessibility tree. Full list of 5 options: `3.5 Flash-Lite`,
   `3.7 Flash`, `3.1 Pro` (checked/default), `Extended thinking`, `Deep Think`. No
   "Deep Research" entry. `Deep Think` is a distinct extended-reasoning model, not the
   agentic web-research report generator.
2. **Left sidebar** — full nav enumerated via accessibility tree: Temporary chat, New
   chat, Search chats, Daily brief, Images, Videos, Library. No "Deep Research" / "Gems"
   / "Agent" entry.
3. **"Upload & tools" (+) menu** next to composer — contains only: Add photos & files,
   Add from Drive, More uploads, Create image, Create video, Create music. No research
   tool entry (window resized to 1400x760 via resize_window to rule out a viewport-cutoff
   false negative; same 6 items, no scroll revealed more).
4. Typing the literal T1 probe text into the composer produced no "Try Deep Research"
   suggestion chip or upsell of any kind before/after typing.
5. `find` tool queried broadly for "Deep Research option in sidebar or tools menu" and
   separately "Research or Agent mode option anywhere on page, including hidden menus" —
   both searches confirmed no such control exists in the current DOM/accessibility tree.

## Conclusion

Contender (b) is **unavailable** for this account on gemini.google.com as of 2026-08-22.
Per shoot-out protocol (login-wall discipline: probe what the existing login gives you,
never register/change account settings, record unavailability and move on), no attempt
was made to enable it via settings changes, upgrades, or a different account. No CAPTCHA
or verification wall was encountered — this is a plain feature-not-present finding, not
a paywall/blocker signal.

T1/T2/T3 were NOT dispatched to Deep Research. Scoring slice should treat contender (b)
as a hard "N/A — not exposed to this account" row rather than a wall-clock/quality entry.
