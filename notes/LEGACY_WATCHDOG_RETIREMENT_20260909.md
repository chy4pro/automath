# Legacy watchdog retirement — 2026-09-09

Reason: operation transferred from Claude to Codex. The old launchd job is broken and its
recovery command would restart the retired Claude coordinator against an ETP677-era prompt.
This is not a repair and does not establish replacement unattended operation.

## Observed pre-change state

- User domain: `gui/501`.
- Label: `com.user.automath-watchdog`.
- `launchctl list com.user.automath-watchdog` returned the loaded job.
- Program: `/bin/zsh`, argument `$HOME/workspace/claudecode/automath/tools/watchdog.sh`.
- Output/error log: `logs/watchdog.launchd.log`.
- No explicit override for this label appeared in `launchctl print-disabled gui/501`.
- Plist retained at `$HOME/Library/LaunchAgents/com.user.automath-watchdog.plist`.
- Script and plist are not edited or deleted by retirement.

## Requested state change

Disable this exact label and remove this exact loaded job from the user domain. No other
launchd job, Claude process, Codex worker, memory-protection process or project file is a target.
Completed at 05:11:40 CDT on 2026-09-09:

- `launchctl disable gui/501/com.user.automath-watchdog`: exit 0.
- `launchctl bootout gui/501/com.user.automath-watchdog`: exit 0.
- `launchctl list com.user.automath-watchdog`: exit 113, service not found (expected).
- `launchctl print-disabled gui/501`: this exact label is explicitly disabled.

A subsequent read-only check reproduced the unloaded/disabled state. No files or other jobs
were removed. The script and plist remain available for the conditional reversal below.

## Reversal

Only after reconciling coordinator ownership and replacing the stale revival prompt, use:

```sh
launchctl enable gui/501/com.user.automath-watchdog
launchctl bootstrap gui/501 $HOME/Library/LaunchAgents/com.user.automath-watchdog.plist
```

Reversal restores the old launcher configuration, not a working mathematical research loop.
Do not run it merely to remove a warning while Codex owns the project.
