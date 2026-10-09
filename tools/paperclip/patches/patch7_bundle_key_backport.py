#!/usr/bin/env python3
"""Patch 7 (PAPERCLIP_PATCH_BUNDLE_KEY): backport of upstream PR #15437 (merged 2026-10-07, fixes #15373) to the
installed 2026.1005.0 claude_local adapter. The per-run instructions working-copy path was baked into the
content-addressed system prompt, so the prompt bundle key changed every run and saved sessions were never
resumed. Upstream moved the path directive into the per-run prompt. Usage: patch7_bundle_key_backport.py <@paperclipai dir>"""
import sys
NM = sys.argv[1]; p = f'{NM}/adapter-claude-local/dist/server/execute.js'; s = open(p).read()
M = '/* PAPERCLIP_PATCH_BUNDLE_KEY */'
if M in s: print('already: patch 7'); sys.exit(0)
old1 = '''    let combinedInstructionsContents = null;
    if (instructionsFilePath) {
        try {
            const instructionsContent = await fs.readFile(instructionsFilePath, "utf-8");
            const pathDirective = `\\nThe above agent instructions were loaded from ${instructionsFilePath}. ` +
                `Resolve any relative file references from ${instructionsFileDir}. ` +
                `This base directory is authoritative for sibling instruction files such as ` +
                `./HEARTBEAT.md, ./SOUL.md, and ./TOOLS.md; do not resolve those from the parent agent directory.`;
            combinedInstructionsContents = instructionsContent + pathDirective;
        }'''
new1 = f'''    let combinedInstructionsContents = null;
    let instructionsPathDirective = ""; {M}
    if (instructionsFilePath) {{
        try {{
            const instructionsContent = await fs.readFile(instructionsFilePath, "utf-8");
            instructionsPathDirective = `Agent instructions for this run were loaded from ${{instructionsFilePath}}. ` +
                `Resolve any relative file references from ${{instructionsFileDir}}. ` +
                `This base directory is authoritative for sibling instruction files such as ` +
                `./HEARTBEAT.md, ./SOUL.md, and ./TOOLS.md; do not resolve those from the parent agent directory. ` +
                `This location replaces any instruction file location from earlier turns.`;
            combinedInstructionsContents = instructionsContent +
                "\\nUse the agent instruction file location supplied in the current run prompt to resolve relative file references.";
        }}'''
assert s.count(old1) == 1, 'anchor 1'
s = s.replace(old1, new1, 1)
old2 = '''        const prompt = joinPromptSections([
            renderedBootstrapPrompt,
            wakePrompt,'''
new2 = '''        const prompt = joinPromptSections([
            instructionsPathDirective,
            renderedBootstrapPrompt,
            wakePrompt,'''
assert s.count(old2) == 1, 'anchor 2'
s = s.replace(old2, new2, 1)
s = s.replace('(with path directive appended)', '(with current file location in the run prompt)')
open(p, 'w').write(s); print('patch 7 applied: bundle-key backport of #15437')
