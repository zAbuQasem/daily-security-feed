---
layout: post
title: "HTB: Checkpoint"
date: 2026-10-24 14:45:00 +0300
categories: [RSS]
tags: [active-directory, privilege-escalation, ad-recycle-bin, malware, credential-theft]
toc: true
---

A detailed CTF walkthrough demonstrating an Active Directory exploitation chain starting from an assume-breach scenario. The attack abuses unusual AD Recycle Bin privileges to restore a deleted user, then plants a malicious VS Code extension via share write access to gain execution. The attacker then uses the BetterSuccessor technique to extract an NTLM hash (after BadSuccessor patching), accesses VMware backups with elevated credentials, and uses vmkatz to extract an administrator hash from a memory snapshot. The walkthrough covers multiple technical primitives including AD object manipulation, extension-based code execution, and forensic analysis of memory snapshots.

[Read original article](https://0xdf.gitlab.io/2026/10/24/htb-checkpoint.html){: .btn .btn-primary }
