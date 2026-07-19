---
layout: post
title: "HTB: Logging"
date: 2026-07-18 13:45:00 +0300
categories: [RSS]
tags: [ctf, active-directory, privilege-escalation, windows, exploitation]
toc: true
---

HackTheBox write-up demonstrating a multi-stage compromise of an Active Directory domain controller starting from low-privileged user credentials. The attack chain includes password recovery from application logs via year-increment guessing, GenericWrite abuse to escalate privileges over a machine account, DLL hijacking from world-writable directories, exploitation of a certificate template vulnerability (ESC17) to forge certificates for arbitrary server names, and finally deployment of a rogue WSUS server to distribute a malicious Windows Update that adds the attacker to the administrators group for full domain control.

[Read original article](https://0xdf.gitlab.io/2026/07/18/htb-logging.html){: .btn .btn-primary }
