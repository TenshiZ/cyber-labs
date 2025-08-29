# 📓 Notes — Active Directory Basics

## Quick Commands
- Open ADUC: dsa.msc
- Open GPMC: gpmc.msc
- System Info: msinfo32
- Group membership: whoami /groups
- Force policy update: gpupdate /force
- Show applied policies: gpresult /R

## PowerShell Snippets
- Create OU:
    New-ADOrganizationalUnit -Name "OUName" -Path "DC=thm,DC=local"

- Move Computer:
    Move-ADObject -Identity "CN=PC1,CN=Computers,DC=thm,DC=local" -TargetPath "OU=Workstations,DC=thm,DC=local"

- Reset User Password:
    Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password')

- Force user password reset at next login:
    Set-ADUser -ChangePasswordAtLogon $true -Identity sophie

## Concepts
- OU = policy application scope. Organizes users/computers for GPOs.
- Security Group = permission management over resources.
- Delegation = grant limited admin rights (e.g., IT support resets passwords).
- GPO = enforce configuration/security baselines across OUs.
- Kerberos = secure, ticket-based authentication (default).
- NetNTLM = legacy challenge-response, prone to relay attacks.
- Tree = multiple domains under same namespace (e.g. us.thm.local).
- Forest = multiple trees under different namespaces (e.g. thm.local + mht.local).
- Trusts = allow cross-domain access (one-way or two-way).
