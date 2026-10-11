#!/usr/bin/env python3
"""Patch 11 (PAPERCLIP_PATCH_AGY_REMOTE): let the external agy_local adapter (Antigravity CLI,
github.com/evgemar/agy-paperclip-adapter, installed from /work/.paperclip/adapters) use ssh environments.
Paperclip only allows ssh/sandbox environments for adapters named in a hard-coded REMOTE_MANAGED_ADAPTERS set
(upstream issue #14843 reports the same gap for hermes_local). This adds "agy_local" to that set, the same
one-line change the community AGY adapter PR #14938 makes in packages/shared/src/environment-support.ts.
The adapter itself already runs through adapter-utils' execution-target helpers.
Usage: patch11_agy_remote.py <@paperclipai dir>"""
import sys
p = f"{sys.argv[1]}/shared/dist/environment-support.js"; s = open(p).read()
M = "/* PAPERCLIP_PATCH_AGY_REMOTE */"
if M in s: print("already: patch 11"); sys.exit(0)
old = '    "gemini_local",\n'
assert s.count(old) == 1 and "REMOTE_MANAGED_ADAPTERS" in s, "anchor"
s = s.replace(old, old + f'    "agy_local", {M}\n', 1)
open(p, "w").write(s); print("patched: 11 agy_local remote environments")
