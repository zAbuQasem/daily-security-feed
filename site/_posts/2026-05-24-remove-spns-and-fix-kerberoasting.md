---
layout: post
title: "Remove SPNs and Fix Kerberoasting"
date: 2026-05-24 05:55:46 +0300
categories: [RSS]
tags: [kerberoasting, active-directory, defense, kerberos, detection]
toc: true
---

This article covers defensive remediation of Kerberoasting in Active Directory environments. Kerberoasting abuses standard Kerberos behavior: any authenticated domain user can request a service ticket (ST) encrypted with the target service account's NTLM hash, enabling offline cracking when SPNs are assigned to user accounts (not computer accounts, which use 120-char random passwords). The guide walks through auditing SPN usage via Event ID 4769 (Kerberos service ticket requests), safely removing unused SPNs via `setspn` or ADUC, and enumerating all user-account SPNs with PowerShell. As an alternative to removal, setting long randomly-generated service account passwords renders cracking computationally infeasible, while least-privilege reduces blast radius if a hash is ever cracked.

[Read original article](https://projectblack.io/blog/remove-spn-fix-kerberoasting/){: .btn .btn-primary }
