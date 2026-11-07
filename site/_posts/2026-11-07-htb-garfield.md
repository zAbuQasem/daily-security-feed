---
layout: post
title: "HTB: Garfield"
date: 2026-11-07 14:45:00 +0300
categories: [RSS]
tags: [active-directory, privilege-escalation, kerberos, rodc, ctf]
toc: true
---

A comprehensive CTF writeup demonstrating multiple attack chains against a hardened Active Directory environment with a hidden Read-Only Domain Controller (RODC). The exploitation chain begins with SYSVOL logon script modification and password reset abuse to escalate from an initial user to admin, then demonstrates multiple techniques to compromise the RODC including writable managedBy attribute abuse, resource-based constrained delegation, password replication policy manipulation, and RODC golden ticket forging from both Windows and Linux platforms. The writeup showcases sophisticated AD attack vectors including delegation abuse and ticket forgery that are directly applicable to real-world penetration testing scenarios.

[Read original article](https://0xdf.gitlab.io/2026/11/07/htb-garfield.html){: .btn .btn-primary }
