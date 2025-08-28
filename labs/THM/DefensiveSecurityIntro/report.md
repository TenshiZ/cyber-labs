# 🛡️ Lab Report — THM/Defensive Security Intro

## 🎯 Objective
Learn the basics of defensive security: SOC structure, incident response workflow, and basic threat handling.

## 🛠️ Tools
- Web-based THM environment (no external tools required).

## 🚀 Procedure
1. Reviewed the role of a SOC analyst (Tier 1 → Tier 2 → SOC Leader).
2. Investigated suspicious login activity by checking logs for an unusual IP.
3. Confirmed that the IP was malicious.
4. Escalated the finding to the SOC Leader.
5. Blocked the IP as part of the incident response process.

## 📂 Results (Evidence)
- Identified malicious IP address in logs.
- Escalated incident properly according to SOC hierarchy.
- Blocked malicious IP, preventing further access.

## ⚠️ Risk
If ignored, the malicious IP could continue unauthorized access, potentially leading to system compromise.

## 🛡️ Mitigation
- Maintain clear SOC escalation procedures.
- Continuously monitor logs for suspicious IP activity.
- Ensure blocking actions are taken and verified.

## 📚 Takeaways
1. SOCs operate with a clear tiered structure for incident handling.  
2. Blue Team work involves both detection and escalation, not just blocking.  
3. Proper escalation ensures threats are dealt with at the right level of authority.  
