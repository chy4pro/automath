#!/bin/sh
S=/work/.tools/sshd/state/$(hostname); [ -f "$S/sshd.pid" ] && kill "$(cat "$S/sshd.pid")" 2>/dev/null && echo "sshd stopped" || echo "sshd not running"
