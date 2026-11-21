---
layout: post
title: "HTB: PingPong"
date: 2026-11-21 14:45:00 +0300
categories: [RSS]
tags: [active-directory, ad-cs, privilege-escalation, constrained-delegation, ctf]
toc: true
---

A detailed write-up of an Insane-difficulty Active Directory CTF challenge demonstrating a complex exploitation chain across two forests joined by bidirectional trust. The attacker abuses ESC13 to obtain a certificate with issuance policy mapping to WinRM-privileged groups, then leverages trust relationships and constrained delegation to pivot across forests, extract gMSA passwords, escape JEA sandbox via script block injection, abuse resource-based constrained delegation (RBCD) for MSSQL access, and use GodPotato for domain compromise before finally exploiting ESC4 to reach Administrator on the first DC. The write-up covers practical exploitation of real Active Directory misconfigurations including certificate services weaknesses, trust abuse, and delegation vulnerabilities.

[Read original article](https://0xdf.gitlab.io/2026/11/21/htb-pingpong.html){: .btn .btn-primary }
