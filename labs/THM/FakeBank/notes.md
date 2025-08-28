# Notes — THM/FakeBank

## Commands
- THM VPN: sudo openvpn --config ~/Downloads/your.ovpn --auth-nocache
- Fuzzing: dirb http://fakebank.thm

## Observations
- dirb discovered: /bank-deposit (200), /images (301)
- /bank-deposit exposed a sensitive deposit/transfer action.

## Next Steps
- Try alternative wordlists with gobuster or ffuf.
- Validate authentication/authorization on sensitive endpoints.
- Keep screenshots locally (do not commit large images to the repo).
