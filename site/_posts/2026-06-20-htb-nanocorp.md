---
layout: post
title: "HTB: NanoCorp"
date: 2026-06-20 13:45:00 +0300
categories: [RSS]
tags: [ctf, active-directory, privilege-escalation, kerberos, cve-2024-0670]
toc: true
---

A HackTheBox write-up demonstrating a complete Active Directory compromise chain. The exploit begins with uploading a malicious archive to a careers portal that leaks a service account's NTLM hash during automated extraction, then uses BloodHound to map a permissions chain enabling group membership escalation and password reset of a Protected Users account. Authentication occurs via Kerberos, followed by abuse of CVE-2024-0670 in the Checkmk monitoring agent to drop write-protected files into a temp directory executed as SYSTEM, achieving full host compromise. The write-up covers NTLM relay to LDAP, credential crafting, and exploitation of privileged automation workflows.

[Read original article](https://0xdf.gitlab.io/2026/06/20/htb-nanocorp.html){: .btn .btn-primary }
