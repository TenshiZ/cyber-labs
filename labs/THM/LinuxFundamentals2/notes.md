# Notes — THM/Linux Fundamentals Part 2

## Commands
- whoami
- id
- su username
- sudo <command>
- passwd
- ls -l
- chmod 644 file.txt
- chmod +x script.sh
- chown user:group file.txt
- ps aux
- top
- kill <PID>

## Observations
- `id` gives quick overview of user context.
- Numeric chmod (e.g., 755) = efficient way to set permissions.
- Killing processes requires correct PID (double-check with ps/top).

## Next Steps
- Practice privilege escalation paths.
- Explore `systemctl` and service management in Part 3.
