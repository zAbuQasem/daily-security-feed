---
layout: post
title: "HTB: DarkZero"
date: 2026-04-05 00:00:00 +0300
categories: [Research, Solid]
tags: [active-directory, mssql, adcs, kerberos, privilege-escalation]
pin: false
toc: true
---

This HTB write-up for the hard-rated DarkZero box covers a two-forest Windows AD environment connected by a bidirectional cross-forest trust. The attack chain begins with MSSQL linked server abuse: DC01's MSSQL links to DC02 in the second forest with a sysadmin-mapped account, allowing xp_cmdshell to be enabled for RCE as the SQL service account. Privilege escalation to SYSTEM on DC02 is demonstrated via four distinct paths: named pipe impersonation to recover SeImpersonatePrivilege from the original logon token, ADCS certificate enrollment to extract an NT hash and perform a password change via RunAsCS, NTLM reflection using the CMTI DNS record trick to relay the machine account to its own LDAPS, and CVE-2024-30088. As SYSTEM on DC02, cross-forest TGT delegation is abused to capture DC01's machine account TGT and perform a full domain hash dump across the forest boundary.

---

[Read original article](https://0xdf.gitlab.io/2026/04/04/htb-darkzero.html)

> Source: `0xdf.gitlab.io`
