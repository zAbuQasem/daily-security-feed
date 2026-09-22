---
layout: post
title: "HTB: Hercules"
date: 2026-09-21 09:00:00 +0300
categories: [RSS]
tags: [ctf, active-directory, privilege-escalation, ldap-injection]
toc: true
---

A detailed CTF walkthrough demonstrating a complex Active Directory exploitation chain on a Windows domain controller. The attack begins with LDAP injection in an ASP.NET web application, combined with a rate-limit bypass to brute-force directory entries and extract credentials from user descriptions. The attacker then exploits an arbitrary file read vulnerability to leak the web application's machine key, enabling forged authentication cookies with elevated roles to unlock file upload functionality. An uploaded document coerces credential authentication that leads into a multi-stage AD abuse chain: shadow credentials injection, moving accounts into attacker-controlled OUs, ESC3 exploitation against the certificate authority, abusing cleanup tasks to remove protections from privileged accounts, and finally leveraging constrained delegation to reach the machine account for NTDS dumping.

[Read original article](https://0xdf.gitlab.io/2026/09/21/htb-hercules.html){: .btn .btn-primary }
