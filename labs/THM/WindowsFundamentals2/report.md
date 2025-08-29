# 🛡️ Lab Report — THM/Windows Fundamentals Part 2

## 🎯 Objective
Understand advanced Windows tools for configuration and troubleshooting: MSConfig, Computer Management, Event Viewer, Resource Monitor, and the Registry.

## 🛠️ Tools
- MSConfig (`msconfig`)
- UAC Settings
- Computer Management (`compmgmt.msc`)
- Task Scheduler
- Event Viewer (`eventvwr.msc`)
- Shared Folders
- Local Users and Groups (`lusrmgr.msc`)
- Performance Monitor (`perfmon`)
- Device Manager (`devmgmt.msc`)
- Disk Management (`diskmgmt.msc`)
- Services and Applications
- System Information (`msinfo32`)
- Resource Monitor (`resmon`)
- Command Prompt (`cmd`)
- Registry Editor (`regedit`)

## 🚀 Procedure
1. **MSConfig**
   - General (Normal, Diagnostic, Selective startup).
   - Boot options.
   - Services list.
   - Startup tab → redirect to Task Manager.
   - Tools tab → shortcuts to system utilities.

2. **User Account Control (UAC)**
   - Change prompt behavior via slider.
   - Default protects against silent privilege escalation.

3. **Computer Management**
   - **Task Scheduler**: create/run scheduled tasks.
   - **Event Viewer**: audit trail of system/application events.
   - **Shared Folders**: view shares, sessions, open files.
   - **Local Users and Groups**: manage accounts and groups.
   - **Performance**: access Performance Monitor.
   - **Device Manager**: view/disable hardware.

4. **Storage**
   - Disk Management: partitions, extend/shrink volumes, assign drive letters.

5. **Services and Applications**
   - Start/stop services, configure properties.
   - WMI Control → scripting interface for management.

6. **System Information (msinfo32)**
   - System Summary: hardware/software specs.
   - Components: device-specific info.
   - Software Environment: env vars, drivers, connections.

7. **Resource Monitor (resmon)**
   - Tabs: CPU, Memory, Disk, Network.
   - Real-time graphs.
   - Identify processes, deadlocks, and resource usage.

8. **Command Prompt (cmd)**
   - `hostname`, `whoami`
   - `ipconfig`, `ipconfig /?`
   - `netstat` with flags (`-a`, `-b`, etc.)
   - `net` and `net help` for subcommands (user, localgroup, share).

9. **Windows Registry**
   - Hierarchical database for config (HKLM, HKCU, etc.).
   - Critical for system operation.
   - Editable with `regedit`.

## 📂 Results (Evidence)
- Explored MSConfig tabs.
- Changed UAC settings.
- Viewed events in Event Viewer.
- Checked shared folders and open sessions.
- Monitored resources with `resmon`.
- Ran system info with `msinfo32`.
- Queried network config with `ipconfig`.
- Opened Registry Editor and browsed hives.

## ⚠️ Risk
- Misconfiguring MSConfig → boot issues.
- Registry edits → system instability.
- Disabling services → break OS features.
- Elevated privileges → malware persistence.

## 🛡️ Mitigation
- Use MSConfig for troubleshooting only.
- Backup registry before edits.
- Limit admin rights; prefer Standard Users.
- Monitor logs/events for suspicious activity.

## 📚 Takeaways
1. MSConfig centralizes access to many troubleshooting tools.  
2. Event Viewer and Resource Monitor are key for system forensics.  
3. Registry = backbone of Windows config. Handle with care.  
4. CLI commands (`ipconfig`, `netstat`, `net`) still essential for admins.  
