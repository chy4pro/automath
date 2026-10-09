#!/usr/bin/env python3
"""Tiny board-API client: pc.py METHOD /path ['{json}']  (token from PAPERCLIP_BOARD_TOKEN_FILE)."""
import json, os, sys, urllib.request
API = "http://wb-proj-656d7af54e8b:3100/api"
TOK = open(os.environ.get("PAPERCLIP_BOARD_TOKEN_FILE", "/work/.paperclip/board.token")).read().strip()
def call(m, p, b=None):
    r = urllib.request.Request(API + p, method=m, data=json.dumps(b).encode() if b is not None else None,
        headers={"Authorization": "Bearer " + TOK, "Content-Type": "application/json", "Origin": "https://automath.mozone.io"})
    try:
        with urllib.request.urlopen(r) as x: return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e: print(m, p, e.code, e.read().decode()[:600], file=sys.stderr); sys.exit(1)
if __name__ == "__main__":
    m, p = sys.argv[1], sys.argv[2]; b = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
    print(json.dumps(call(m, p, b), indent=1))
