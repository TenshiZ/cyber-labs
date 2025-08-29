# Notes — THM/Windows Fundamentals Part 1

## Access
- RDP: `mstsc` → IP: 10.10.x.x, user: administrator, pass: letmein123!

## Key Tools
- lusrmgr.msc → local users & groups.
- Control Panel → legacy settings.
- Settings → modern config.
- Task Manager → process/performance view.

## File System
- NTFS features: large file support, permissions, compression, EFS encryption, ADS.
- ADS example: hidden streams can be checked with PowerShell.

## User Management
- Admin = full control.
- Standard = limited, safer default.
- Profiles in `C:\Users\`.

## UAC
- Prompts for elevation on admin tasks.
- Prevents silent privilege escalation.

## Observations
- ADS is both useful and a potential backdoor.
- UAC shield icon = visual cue for elevated privilege required.
- GUI navigation (Start, Taskbar, Notification area) maps to underlying system functions.

## Next Steps
- Explore ADS with PowerShell (`Get-Item -Stream`).
- Compare Control Panel vs Settings in depth.
- Practice task and service management.
