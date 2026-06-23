---
layout: post
title: "Fantastic clear-text passwords and where to collect them (Part 1 - Linux)"
date: 2026-06-21 23:03:20 +0300
categories: [RSS]
tags: [linux, dfir, credential-theft, lateral-movement, cloud]
toc: true
---

A DFIR research article documenting real-world techniques for harvesting plaintext credentials on Linux systems, including bash history dumping, process memory extraction via GDB and truffleproc, and command-line snooping via pspy. The post demonstrates critical impact through a real incident where a Siemens keystore password found in bash history enabled lateral movement to Azure cloud infrastructure via certificate-based authentication to the Microsoft Graph API. Covers defensive hardening including ptrace scope restrictions, secrets management via environment variables or interactive prompts, and Azure Conditional Access for workload identities. Essential for DFIR teams and defenders understanding how root-level compromises cascade through cloud environments and compromise organizational cloud email.

[Read original article](https://dfir.ch/posts/fantastic_passwords_linux/){: .btn .btn-primary }
