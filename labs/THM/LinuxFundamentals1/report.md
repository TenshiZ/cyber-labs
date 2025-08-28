# 🛡️ Lab Report — THM/Linux Fundamentals Part 1

## 🎯 Objective
Get comfortable using the Linux command line: navigation, file operations, searching, and shell operators.

## 🛠️ Tools
- THM AttackBox (Ubuntu Linux).
- Built-in commands: ls, cd, cat, pwd, find, grep, wc, echo.

## 🚀 Procedure
1. **Where Linux is used**: web servers, PoS systems, IoT, industrial control, desktops.  
2. **Distributions**: Ubuntu, Debian, many variants (open-source, UNIX-based).  
3. **Basic commands**:  
   - `ls` → list files in a directory.  
   - `cd` → change directory.  
   - `pwd` → print working directory.  
   - `cat` → output file contents.  
4. **Searching files**:  
   - `find -name filename` → locate files.  
   - `find -name *.txt` → locate by extension.  
   - `grep "string" file` → search inside files.  
5. **Counting**:  
   - `wc -l file` → count lines.  
6. **Shell operators**:  
   - `&` → run in background.  
   - `&&` → chain commands if first succeeds.  
   - `>` → redirect output to new file.  
   - `>>` → append output to existing file.

## 📂 Results (Evidence)
- Found and read `/Documents/todo.txt`.  
- Located `passwords.txt` using `find`.  
- Extracted IP entries from `access.log` with `grep`.

## ⚠️ Risk
Mismanagement of Linux commands (permissions, redirects) can overwrite critical data or expose sensitive files.

## 🛡️ Mitigation
- Always check paths before using `>` redirect.  
- Use `less` or `head/tail` instead of `cat` for large logs.  
- Apply `sudo` only when necessary.

## 📚 Takeaways
1. Linux is everywhere — knowing CLI is non-negotiable.  
2. `find` + `grep` massively speed up investigations.  
3. Shell operators allow automation and efficient workflows.
