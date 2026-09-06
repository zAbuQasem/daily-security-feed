---
layout: post
title: "HTB: Pirate"
date: 2026-09-05 13:45:00 +0300
categories: [RSS]
tags: [active-directory, constrained-delegation, spn-jacking, ctf-writeup, lateral-movement]
toc: true
---

A detailed walkthrough of the HackTheBox Pirate machine, demonstrating a multi-stage Active Directory attack chain. Starting from a low-privileged domain account, the attacker discovers pre-Windows 2000 machine accounts with passwords matching hostnames, gaining membership in a group that can read group-managed service account (gMSA) passwords for WinRM access to the domain controller. From there, authentication coercion and NTLM relay are used to configure resource-based constrained delegation (RBCD) on an internal web server, followed by password reset and SPN-jacking attacks that move a service principal name to the domain controller and change service classes to impersonate the domain administrator. The write-up also documents an alternate cross-session relay technique using RemotePotato0, showcasing practical exploitation of Windows credential delegation mechanisms.

[Read original article](https://0xdf.gitlab.io/2026/09/05/htb-pirate.html){: .btn .btn-primary }
