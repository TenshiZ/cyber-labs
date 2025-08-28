# 🛡️ Lab Report — THM/Linux Fundamentals Part 3

## 🎯 Objective
Learn about Linux service management, environment variables, package management, and automation with scripting.

## 🛠️ Tools
- THM AttackBox (Ubuntu Linux).
- Commands: env, echo $VAR, export, apt, systemctl, service, crontab, nano/vim.

## 🚀 Procedure
1. **Environment Variables**
   - `env` → list variables.
   - `echo $PATH` → print variable.
   - `export VAR=value` → set variable.
   - Variables can control program behavior.

2. **Package Management**
   - Debian/Ubuntu: `apt update`, `apt upgrade`.
   - Install packages: `apt install package`.
   - Remove packages: `apt remove package`.

3. **Services**
   - `systemctl status service` → check service.
   - `systemctl start/stop service`.
   - `systemctl enable service` → run at boot.

4. **Cron Jobs**
   - `crontab -e` → edit cron jobs.
   - Schedule tasks with syntax: `minute hour day month weekday command`.

5. **Scripting Basics**
   - Write scripts with `nano script.sh`.
   - Add shebang `#!/bin/bash`.
   - Make executable with `chmod +x script.sh`.
   - Run with `./script.sh`.

## 📂 Results (Evidence)
- Listed environment variables with `env`.
- Installed and removed packages with `apt`.
- Managed services with `systemctl`.
- Scheduled a simple cron job.
- Created and executed a shell script.

## ⚠️ Risk
- Misconfigured cron jobs may expose sensitive data or break services.
- Environment variables can leak credentials if not secured.
- Outdated packages may contain vulnerabilities.

## 🛡️ Mitigation
- Limit sensitive info in environment variables.
- Regularly update packages.
- Audit cron jobs and scripts for security.

## 📚 Takeaways
1. Environment variables are powerful but must be secured.  
2. Package management is central to maintaining a secure Linux system.  
3. Cron jobs and scripting provide automation, essential for sysadmins.  
