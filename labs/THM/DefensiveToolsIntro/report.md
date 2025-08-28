# 🛡️ Lab Report — THM/Defensive Tools Intro

## 🎯 Objective
Get familiar with specialized search engines, vulnerability databases, and official documentation sources used in cybersecurity.

## 🛠️ Tools & Platforms
- **Shodan** → search engine for Internet-connected devices and systems.  
- **Censys** → Internet assets, certificates, ports, rogue assets.  
- **VirusTotal** → multi-engine malware and URL scanner.  
- **Have I Been Pwned (HIBP)** → check if emails/passwords appeared in breaches.  
- **CVE/NVD** → standardized vulnerability identifiers and database (MITRE + NIST).  
- **Exploit Database** → repository of public exploits and PoCs.  
- **GitHub** → PoCs, security tools, exploit code.  
- **Linux man pages** → built-in command documentation.  
- **Windows Docs** → official Microsoft technical documentation.  
- **Product Docs** → official documentation for specific software (Snort, Apache, PHP, Node.js, etc.).

## 🚀 Procedure
1. Reviewed Shodan and Censys differences.  
2. Learned to look up vulnerabilities via CVE IDs.  
3. Practiced checking malware samples/hashes on VirusTotal.  
4. Used HIBP to check if an email was leaked.  
5. Understood the role of ExploitDB and GitHub for PoCs.  
6. Accessed Linux `man` command for documentation.  
7. Checked Microsoft technical documentation for Windows commands.  
8. Saw how official docs are critical for up-to-date information.

## 📂 Results (Evidence)
- Shodan → found Apache 2.4.1 servers worldwide.  
- VirusTotal → scanned a file with 67 AV engines.  
- HIBP → confirmed if email appears in breaches.  
- CVE → example CVE-2014-0160 (Heartbleed).  
- ExploitDB/GitHub → verified presence of public exploits.

## ⚠️ Risk
Ignoring these resources means missing critical context about vulnerabilities, exploits, and asset exposure.

## 🛡️ Mitigation
- Regularly monitor CVEs and NVD feeds.  
- Train teams to use Shodan/Censys for asset discovery.  
- Integrate VirusTotal and HIBP in security workflows.  
- Always validate with **official product documentation**.

## 📚 Takeaways
1. Specialized search engines = faster, deeper visibility than Google.  
2. CVE IDs provide a universal language for vulnerabilities.  
3. Exploit databases + GitHub PoCs help validate risk (with permission).  
4. Official docs (Linux, Windows, products) are the most reliable references.  
