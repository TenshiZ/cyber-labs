# Notes — THM/Windows Fundamentals Part 2

## Key Utilities
- msconfig → startup config, troubleshooting.
- compmgmt.msc → Task Scheduler, Event Viewer, Shares, Perfmon, Device Manager.
- diskmgmt.msc → partitions and drives.
- msinfo32 → system summary and env vars.
- resmon → live CPU, RAM, Disk, Network usage.
- regedit → Registry Editor.

## CLI Commands
- hostname → show computer name.
- whoami → show current user.
- ipconfig /? → view syntax and params.
- netstat -ano → list connections and PIDs.
- net help user → syntax for managing users.
- net help share → syntax for shares.

## Observations
- UAC slider can be disabled (not recommended).
- Many GUI tools overlap with CLI commands.
- Registry is central to persistence (malware often hides keys there).

## Next Steps
- Practice Task Scheduler with benign tasks.
- Export registry key safely and re-import.
- Analyze Event Viewer logs for failed logins.
- Use netstat to identify active RDP session.
