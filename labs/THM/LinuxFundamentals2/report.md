# 🛡️ Lab Report — THM/Linux Fundamentals Part 2

## 🎯 Objective
Learn about Linux users, permissions, processes, and how to manage them via the command line.

## 🛠️ Tools
- THM AttackBox (Ubuntu Linux).
- Built-in commands: id, whoami, su, sudo, ps, top, kill, chmod, chown, passwd.

## 🚀 Procedure
1. **Users and Groups**
   - `whoami` → current user.
   - `id` → show UID, GID, groups.
   - `su user` → switch user.
   - `sudo command` → run command with elevated privileges.
   - `passwd` → change password.

2. **Permissions**
   - Files and directories have **owner, group, others**.
   - `ls -l` → shows permissions (`rwx`).
   - `chmod` → change permissions (symbolic or numeric).
     - Example: `chmod 755 file`.
   - `chown` → change owner/group.

3. **Processes**
   - `ps aux` → list processes.
   - `top` → real-time process monitoring.
   - `kill PID` → terminate process.

## 📂 Results (Evidence)
- Successfully switched users with `su`.
- Modified file permissions using `chmod`.
- Observed and killed processes with `ps` and `kill`.

## ⚠️ Risk
- Misconfigured permissions may expose sensitive files.
- Improper use of `sudo` can lead to privilege escalation risks.

## 🛡️ Mitigation
- Follow least-privilege principle.
- Regularly audit file permissions.
- Monitor processes for anomalies.

## 📚 Takeaways
1. Linux permissions (`rwx`) are crucial for security.  
2. Users and groups control access separation.  
3. Process management is key for stability and security.  
