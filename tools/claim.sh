#!/bin/bash
# Minimal claim/lock for serialised work items (prospector rounds, gate batches, audits).
# Fixes the gap exposed by the r13 duplicate-dispatch incident: reading a live ledger does NOT
# serialise anything -- two correct reads still collide. A claim is an atomic create.
#   claim.sh take <item>   -> exits 0 if claimed, 1 if already held (prints holder + age)
#   claim.sh release <item>
#   claim.sh status <item>
set -u
DIR="$(cd "$(dirname "$0")/.." && pwd)/logs/claims"; mkdir -p "$DIR"
ACT="${1:-status}"; ITEM="${2:-}"; [ -z "$ITEM" ] && { echo "usage: claim.sh {take|release|status} <item>"; exit 2; }
F="$DIR/$ITEM.claim"
case "$ACT" in
  take)
    # O_EXCL via noclobber: atomic, no race between test and create.
    if ( set -o noclobber; echo "$(date '+%Y-%m-%d %H:%M:%S') pid=$$" > "$F" ) 2>/dev/null; then
      echo "CLAIMED $ITEM"; exit 0
    else
      echo "ALREADY HELD: $ITEM -- $(cat "$F" 2>/dev/null)"; exit 1
    fi ;;
  release) rm -f "$F" && echo "RELEASED $ITEM" ;;
  status)  [ -f "$F" ] && echo "HELD: $(cat "$F")" || echo "FREE: $ITEM" ;;
  *) echo "usage: claim.sh {take|release|status} <item>"; exit 2 ;;
esac
