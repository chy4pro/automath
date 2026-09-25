#!/usr/bin/env python3
"""Emit a single JavaScript snippet that (1) switches the chat.qwen.ai web UI model to the requested
model, (2) writes a brief into the composer textarea via the native React setter (no clipboard), and
(3) returns 'header=<model> | len=<n>' so the caller can verify before pressing Return.

Usage: python3 engine/scripts/qwen_ui_dispatch.py BRIEF.md [--model Qwen3.8-Max] [--preamble TEXT] > /tmp/x.js
Then run the snippet with the Chrome MCP javascript_tool on a FRESH https://chat.qwen.ai/ tab, check the
returned header, and press Return (computer key) to send.  Recipe validated 2026-08-29 (dialogue).
"""
import argparse, json, sys
ap = argparse.ArgumentParser()
ap.add_argument("brief")
ap.add_argument("--model", default="Qwen3.8-Max")
ap.add_argument("--preamble", default="")
a = ap.parse_args()
text = (a.preamble + "\n\n" if a.preamble else "") + open(a.brief, encoding="utf-8").read()
js = r"""
const sleep = ms => new Promise(r => setTimeout(r, ms));
const MODEL = %s; const TEXT = %s;
const trig = document.querySelector('div[role="button"][aria-label="Select Model"]');
let log = [];
if (!trig) { log.push('no model trigger'); }
else if (trig.innerText.trim() !== MODEL) {
  const findOpt = () => [...document.querySelectorAll('[role="option"], .ant-dropdown *')]
    .find(e => e.children.length <= 3 && (e.textContent||'').trim().startsWith(MODEL));
  let opt = null;
  for (let i = 0; i < 3 && !opt; i++) { trig.click(); await sleep(700); opt = findOpt(); }
  if (opt) { (opt.closest('[role="option"]') || opt).click(); await sleep(800); }
  document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Escape', bubbles: true})); await sleep(300);
}
const hdr = document.querySelector('div[role="button"][aria-label="Select Model"]');
const ta = document.querySelector('textarea.message-input-textarea');
if (ta) {
  const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
  setter.call(ta, TEXT); ta.dispatchEvent(new Event('input', {bubbles: true})); await sleep(400);
  ta.focus();
}
'header=' + (hdr ? hdr.innerText.trim() : 'none') + ' | len=' + (ta ? ta.value.length : -1) + ' | ' + log.join(';')
""" % (json.dumps(a.model), json.dumps(text))
sys.stdout.write(js)
