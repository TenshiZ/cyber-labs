# 🛡️ Lab Report — THM/Active Directory Basics

## 🎯 Objective
Understand core Active Directory concepts and practice basic administration (OUs, groups, delegation, GPOs, auth protocols, trees/forests/trusts).

## 🛠️ Tools
- Domain Controller (Windows Server) with AD DS
- MMC consoles: `dsa.msc` (AD Users & Computers), `gpmc.msc` (Group Policy Management)
- PowerShell (RSAT AD cmdlets)
- RDP access: `THM\Administrator / Password321` → MACHINE_IP

## 🚀 Procedure
1) **AD Fundamentals**  
   - Domain Controller role, AD DS objects (users, computers, groups), security principals.  
   - Difference **OUs (policies)** vs **Security Groups (permissions)**.

2) **Inventory & Cleanup**  
   - Enable *Advanced Features* to remove protected OUs no usadas.  
   - Crear OU demostración `Students` bajo `THM`.

3) **Delegation**  
   - Delegar a `phillip` “Reset user passwords” en OU `Sales`.  
   - Probar con PowerShell: reset de `sophie` y `ChangePasswordAtLogon`.

4) **Device OUs**  
   - Crear OUs raíz: `Workstations` y `Servers`.  
   - Mover endpoints desde `Computers` al OU correspondiente.

5) **GPOs**  
   - Revisar **Default Domain Policy** (password/lockout).  
   - Endurecer `Minimum password length = 10`.  
   - GPO **Restrict Control Panel** (User Config) → link a `Marketing`, `Management`, `Sales`.  
   - GPO **Auto Lock Screen** (Computer Config) → link al **dominio raíz** (inactividad 5 min).  
   - Forzar replicación: `gpupdate /force`.

6) **Auth Protocols**  
   - **Kerberos** (TGT/TGS con KDC) vs **NetNTLM** (challenge/response).  
   - Minimizar NTLM; preferir Kerberos.

7) **Trees, Forests & Trusts**  
   - Trees (mismo namespace), Forests (namespaces distintos).  
   - Trusts one-way / two-way; **habilitan autorizar**, no conceden acceso por sí mismos.

## 📂 Results (Evidence)
- OUs de departamentos y dispositivos organizadas.  
- Delegación aplicada a `phillip`; reset de `sophie` verificado.  
- GPOs creadas/enlazadas; password policy endurecida; `gpupdate /force` ejecutado.

## ⚠️ Risk
- Borrado de OUs puede eliminar objetos críticos.  
- Delegaciones excesivas amplían superficie de ataque.  
- GPO mal enlazadas afectan todo el dominio.  
- Mantener NetNTLM abierto facilita relay.

## 🛡️ Mitigation
- Backups/Recycle Bin de AD; cambio controlado.  
- Principio de **mínimos privilegios** en delegación y grupos.  
- Filtrado de seguridad/WMI en GPOs; scoping claro.  
- Deshabilitar/limitar NTLM donde sea viable; priorizar Kerberos.

## 📚 Takeaways
1. **OUs = políticas**, **Grupos = permisos**.  
2. Delegación bien diseñada descarga al Domain Admin sin perder control.  
3. GPO es la palanca central de configuración/hardening.  
4. Kerberos reduce exposición de credenciales; NTLM es legado.
