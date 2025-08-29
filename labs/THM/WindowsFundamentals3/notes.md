# Notes — THM/Windows Fundamentals Part 3

## Key Concepts
- **Patch Tuesday** → Microsoft pushes security fixes every 2nd Tuesday.
- **Defender AV** → built-in, offers real-time + cloud + ransomware protection.
- **Firewall Profiles**:
  - Domain → corp networks.
  - Private → home LAN.
  - Public → WiFi hotspots.
- **SmartScreen** → blocks phishing/malware sites and files.
- **Exploit Protection** → mitigates memory/code injection.
- **Core Isolation** → memory integrity for process isolation.
- **TPM** → hardware crypto for key storage, required by BitLocker.
- **BitLocker** → full-disk encryption, best with TPM.
- **VSS (Shadow Copies)** → restore points, often targeted by ransomware.

## Commands & Shortcuts
- `control /name Microsoft.WindowsUpdate` → Windows Update.
- `WF.msc` → Firewall advanced settings.
- Right-click file → "Scan with Microsoft Defender".
- Create restore point → System Properties > System Protection.

## Observations
- Real-time Defender disabled in VM → only for lab performance.
- BitLocker not included in Server 2019 VM.
- Attackers often delete shadow copies (`vssadmin delete shadows`) in ransomware.

## Next Steps
- Explore Defender logs in Event Viewer.
- Practice configuring custom firewall rules.
- Test shadow copy creation/restoration.
- Research Living Off The Land Binaries (LOLBins).  
