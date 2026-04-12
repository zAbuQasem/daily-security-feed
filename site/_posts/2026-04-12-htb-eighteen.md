---
layout: post
title: "HTB: Eighteen"
date: 2026-04-12 03:12:28 +0300
categories: [RSS]
tags: [windows, active-directory, mssql, privilege-escalation, password-cracking]
toc: true
---

This Hack The Box write-up walks through a Windows Server 2025 compromise that starts with valid MSSQL credentials and turns them into full domain admin. The attack abuses MSSQL login impersonation to access a financial-planner database, extract a Werkzeug PBKDF2 password hash for the web admin account, and crack it for reuse against domain users until a valid WinRM login is found. After landing on the host, the key escalation step is exploiting the new Windows 2025 functional-level dMSA migration behavior in the Bad Successor technique: creating a delegated managed service account that inherits the Administrator account's group memberships. The write-up is useful because it ties together SQL abuse, credential reuse, and a modern Active Directory privilege-escalation path that defenders need to understand as Server 2025 deployments appear.

[Read original article](https://0xdf.gitlab.io/2026/04/11/htb-eighteen.html){: .btn .btn-primary }
