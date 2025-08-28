# 🛡️ Lab Report — THM/FakeBank

## 🎯 Objective
Find hidden functionality on a fake banking app and assess impact.

## 🛠️ Tools
- `dirb` — brute forcing directories/URLs to discover hidden endpoints.

## 🚀 Procedure
1. Fuzz the web root:
   ```bash
   dirb http://fakebank.thm
2. Visit discovered endpoints and validate behavior.

## 📂 Results (Evidence)
- Discovered:
/images (301)
- `/bank-deposit` exposed a sensitive action (deposit/transfer).

## ⚠️ Risk
Unprotected functionality could allow unauthorized money movement (direct financial loss).

## 🛡️ Mitigation
Enforce authentication/authorization on all sensitive endpoints; do not rely on hidden URLs. Add server-side checks & logging.

## 📚 Takeaways
1. Hidden endpoints are common; fuzzing quickly reveals them.
2. Security by obscurity is not a defense.
