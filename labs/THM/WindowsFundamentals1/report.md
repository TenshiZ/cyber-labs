# 🛡️ Lab Report — THM/Windows Fundamentals Part 1

## 🎯 Objective
Gain a foundational understanding of the Windows operating system: GUI, NTFS, user accounts, UAC, Control Panel vs Settings, and Task Manager.

## 🛠️ Tools
- Windows Server 2019 Standard (via RDP).
- GUI components: Desktop, Start Menu, Taskbar, Notification Area.
- Built-in Windows utilities: lusrmgr.msc, Control Panel, Task Manager.

## 🚀 Procedure
1. **Windows History**
   - XP → Vista → 7 → 8.x → 10 → 11.
   - Server line currently at Windows Server 2025.

2. **Desktop & GUI**
   - Desktop = shortcuts for quick access.
   - Start Menu (apps, account actions, tiles).
   - Taskbar & Notification area.
   - Personalization: wallpaper, resolution, fonts.

3. **File Systems**
   - FAT16/FAT32/HPFS → legacy.
   - NTFS (current): journaling, large files, permissions, compression, encryption.
   - Permissions: Full Control, Modify, Read/Execute, List, Read, Write.
   - ADS (Alternate Data Streams) → hidden data streams, abused by malware.

4. **User Accounts**
   - Administrator vs Standard User.
   - Profiles stored under `C:\Users`.
   - Local Users and Groups: `lusrmgr.msc`.
   - Groups inherit permissions.

5. **User Account Control (UAC)**
   - Prompts for elevation on admin accounts.
   - Protects against malware running with admin privileges.

6. **Settings vs Control Panel**
   - Settings (modern, from Win 8).
   - Control Panel (legacy, more detailed).
   - Some operations redirect between them.

7. **Task Manager**
   - Provides info about processes, performance, users, services.
   - Simple view vs advanced details.

## 📂 Results (Evidence)
- Connected via RDP using provided credentials.
- Explored Desktop, Start Menu, Taskbar, Notification Area.
- Checked NTFS permissions on system folders.
- Viewed user accounts/groups in `lusrmgr.msc`.
- Triggered UAC prompt as Standard User.
- Opened Task Manager and switched to "More details".

## ⚠️ Risk
- Admin users as daily drivers → malware risk.
- ADS can hide malicious data.
- Misconfigured permissions expose critical files.

## 🛡️ Mitigation
- Enforce least privilege (Standard User by default).
- Audit NTFS permissions regularly.
- Use UAC prompts and security tools (Defender, Firewall).
- Educate users about Settings vs Control Panel.

## 📚 Takeaways
1. NTFS is powerful but also a target for abuse (ADS).  
2. User types (Admin vs Standard) define risk exposure.  
3. UAC adds a vital security layer.  
4. Task Manager is the entry point to monitoring processes.  
