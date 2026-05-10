---
layout: post
title: "HTB: Overwatch"
date: 2026-05-09 13:45:00 +0300
categories: [RSS]
tags: [ctf, active-directory, wcf, command-injection, sql-server]
toc: true
---

This Hack The Box write-up chains several Windows attack techniques on a domain controller running SMB, MSSQL 2022, WinRM, and a .NET Message Framing/WCF service. The initial foothold comes from anonymous access to an SMB software share hosting a custom .NET monitoring binary; reversing that binary reveals SQL Server credentials and exposes a localhost WCF `KillProcess` operation that passes attacker-controlled input into PowerShell, creating a command-injection path. The author then abuses an MSSQL linked server configuration that targets an unresolvable hostname by using `CREATE_CHILD` rights on the AD-integrated DNS zone to register that hostname to an attacker IP, coercing the SQL service into authenticating outward and leaking cleartext SQL credentials to Responder. Those credentials enable WinRM access, after which the vulnerable SOAP endpoint is used for SYSTEM-level code execution, making the article a solid practical study in AD DNS abuse, credential capture, .NET/WCF service interaction, and Windows privilege escalation.

[Read original article](https://0xdf.gitlab.io/2026/05/09/htb-overwatch.html){: .btn .btn-primary }
