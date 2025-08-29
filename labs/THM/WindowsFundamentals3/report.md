# 🛡️ Lab Report — THM/Windows Fundamentals Part 3

## 🎯 Objective
Explore built-in **Windows security tools**: Updates, Defender, Firewall, SmartScreen, Exploit Protection, TPM, BitLocker, and Volume Shadow Copies.

## 🛠️ Tools
- Windows Update (`control /name Microsoft.WindowsUpdate`)
- Windows Security app
- Microsoft Defender Antivirus
- Windows Defender Firewall (`WF.msc`)
- Microsoft Defender SmartScreen
- Exploit Protection
- Core Isolation / Memory Integrity
- TPM (Trusted Platform Module)
- BitLocker (with TPM)
- Volume Shadow Copy Service (VSS)

## 🚀 Procedure
1. **Windows Update**
   - Provides security + feature patches.
   - Patch Tuesday (2nd Tuesday/month).
   - Updates mandatory in Win10/11 (can delay but not avoid).

2. **Windows Security Dashboard**
   - Protection areas:
     - Virus & Threat Protection
     - Firewall & Network Protection
     - App & Browser Control
     - Device Security

3. **Virus & Threat Protection**
   - Scan options: quick, full, custom.
   - Threat history: quarantined, allowed.
   - Settings: real-time protection, cloud, sample submission.
   - Ransomware protection: Controlled Folder Access.

4. **Firewall & Network Protection**
   - Profiles: Domain, Private, Public.
   - Options: enable/disable firewall, block all incoming.
   - Allow apps through firewall.
   - Advanced config in WF.msc.

5. **App & Browser Control**
   - SmartScreen: blocks malicious apps/files.
   - Exploit protection: mitigates memory/code injection.

6. **Device Security**
   - Core isolation → memory integrity.
   - Security processor (TPM).
   - BitLocker encryption → tied to TPM.

7. **Volume Shadow Copy Service (VSS)**
   - Create restore points.
   - System restore from snapshot.
   - Malware often deletes shadow copies to disable recovery.

## 📂 Results (Evidence)
- Navigated Windows Security dashboard.
- Checked Defender scans + settings.
- Viewed firewall profiles.
- Inspected SmartScreen + Exploit Protection.
- Reviewed TPM role.
- Noted absence of BitLocker in VM.
- Confirmed System Protection options for restore points.

## ⚠️ Risks
- Disabled updates → missed critical patches.
- Turning off Defender/Firewall → exposure to malware.
- Excluding files from scans → persistence of malicious binaries.
- VSS deletion → ransomware persistence.

## 🛡️ Mitigation
- Keep updates enabled and applied.
- Always enable real-time Defender or equivalent AV.
- Use least privilege (do not run as admin by default).
- Backup offline to survive ransomware wiping VSS.

## 📚 Takeaways
1. Windows ships with strong native security tooling (Defender + Firewall + SmartScreen).  
2. TPM enables advanced features (BitLocker, credential protection).  
3. Updates and restore points are the first line of defense.  
4. Malware often abuses or disables these features (Living Off The Land).  
