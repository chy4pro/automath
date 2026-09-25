#!/usr/bin/env python3
"""Recover a text file from the clipboard (ChatGPT page + open file viewer): try every plausible
start line (shebang / import / from / docstring / comment) and both newline variants; save the slice
whose SHA-256 equals the expected hash. Usage: extract_text_by_hash.py <sha256> <out>."""
import hashlib, re, subprocess, sys
exp, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(['pbpaste'], capture_output=True, text=True).stdout
starts = [m.start() for m in re.finditer(r'(?m)^(#!|import |from |"""|# )', raw)]
for j in starts:
    body = raw[j:]
    for v in (body, body.rstrip("\n") + "\n", body.rstrip("\n")):
        if hashlib.sha256(v.encode()).hexdigest() == exp:
            open(out, "w").write(v); print("MATCH ->", out, "| bytes", len(v), "| start", j); sys.exit(0)
print("NO MATCH; clip len", len(raw), "| candidate starts", len(starts), "| tail:", repr(raw[-120:])); sys.exit(1)
