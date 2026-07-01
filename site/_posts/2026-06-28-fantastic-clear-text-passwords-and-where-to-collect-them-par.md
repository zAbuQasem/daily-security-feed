---
layout: post
title: "Fantastic clear-text passwords and where to collect them (Part 2 - Windows)"
date: 2026-06-28 23:03:20 +0300
categories: [RSS]
tags: [credential-access, windows, detection, privilege-escalation, incident-response]
toc: true
---

A detailed guide to Windows credential extraction techniques beyond LSASS dumping, which are increasingly detected by EDR. Key techniques include re-enabling WDigest plaintext credential caching via registry modification (`UseLogonCredential`), searching for passwords in Group Policy Objects and PowerShell command history, and collecting stolen credentials from purchased stealer logs. The author includes real incident examples—such as attackers buying Raccoon stealer logs and domain admin access on darknet forums—and practical detection strategies using Sysmon Event ID 13, file access logging, and Defender for Endpoint alerts. Blue team defenses include using Snaffler for proactive credential hunting, deploying Canarytokens on file shares, and enforcing policies to prevent password storage in plaintext applications.

[Read original article](https://dfir.ch/posts/fantastic_passwords_windows/){: .btn .btn-primary }
