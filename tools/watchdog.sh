#!/bin/zsh
# automath perpetual-loop watchdog (layer 2).
# Healthy path: the interactive session's ScheduleWakeup ticks touch logs/heartbeat.
# If heartbeat is stale (>45 min), revive the loop with a headless claude tick.
# Reversal: launchctl unload ~/Library/LaunchAgents/com.user.automath-watchdog.plist
set -u
export PATH="$HOME/.local/bin:$HOME/.local/node/bin:/usr/local/bin:/usr/bin:/bin"
ROOT="$HOME/workspace/claudecode/automath"
HB="$ROOT/logs/heartbeat"
LOCK="$ROOT/logs/watchdog.lock"
LOG="$ROOT/logs/watchdog.log"
now=$(date +%s)

log() { print "$(date '+%F %H:%M:%S') $1" >> "$LOG"; }

# heartbeat fresh? (45 min threshold)
if [[ -f "$HB" ]]; then
  hb=$(cat "$HB" 2>/dev/null || echo 0)
  if (( now - hb < 2700 )); then
    exit 0
  fi
fi

# stale-lock cleanup (>90 min) then single-instance guard
if [[ -f "$LOCK" ]]; then
  lts=$(stat -f '%m' "$LOCK" 2>/dev/null || echo 0)
  if (( now - lts > 5400 )); then
    log "removing stale lock"
    rm -f "$LOCK"
  else
    exit 0
  fi
fi
echo $$ > "$LOCK"
log "heartbeat stale ($(( (now - ${hb:-0}) / 60 )) min) — reviving loop"

cd "$ROOT"
claude --continue -p "看门狗唤醒（layer 2）：automath 永续任务主循环已静默超过 45 分钟（会话可能崩溃/机器可能重启过）。执行一个恢复 tick：1) 读 memory 与 problems/etp677/campaign_registry.md 恢复上下文；2) 盘点幸存状态（codex screen 是否存活、在途 agent、日志/文件 mtime——时间戳必须取自 date/mtime）；3) 重建能重建的（codex screen 死了就 screen -dmS codex $HOME/.local/node/bin/codex 并续派任务）；4) 推进最有价值的一步并把状态写入 campaign_registry.md；5) 结束前执行 date '+%s' > logs/heartbeat；6) 在 registry 中注明这是 watchdog 恢复 tick、用户需重开交互会话才能恢复完整节奏。禁止启动 SAT/穷举等本地重计算。" >> "$LOG" 2>&1
rc=$?
log "revival tick finished rc=$rc"
rm -f "$LOCK"
