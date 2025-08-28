# Notes — THM/Linux Fundamentals Part 3

## Commands
- env
- echo $PATH
- export TEST=123
- apt update && apt upgrade
- apt install nmap
- apt remove nmap
- systemctl status ssh
- systemctl start ssh
- systemctl enable apache2
- crontab -e
- nano script.sh
- chmod +x script.sh
- ./script.sh

## Observations
- env shows dozens of variables affecting shell behavior.
- PATH controls where binaries are searched.
- systemctl is the modern way to manage services.
- Cron is flexible for scheduled tasks but requires careful syntax.
- Scripts combine commands for automation.

## Next Steps
- Explore secure management of secrets (not in plain env vars).
- Learn advanced cron syntax (@daily, @reboot).
- Build more complex scripts with conditionals/loops.
