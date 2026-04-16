---
layout: post
title: "Shadow Admins in Active Directory: Hidden Privilege Paths Attackers Exploit"
date: 2026-04-16 03:12:34 +0300
categories: [RSS]
tags: [active-directory, privilege-escalation, adfs, rbcd, identity]
toc: true
---

Praetorian outlines how "shadow admin" accounts in Active Directory gain Domain Admin-equivalent power through indirect control paths rather than membership in obvious privileged groups. The post highlights several concrete mechanisms: administrators of ADFS servers can steal the token-signing certificate and perform Golden SAML-style federation abuse; VMware/ESXi admins can snapshot or clone domain controller VMs, access VM consoles, and extract NTDS.dit or otherwise compromise Tier 0 guests; and overbroad write access on computer objects lets helpdesk-style delegates modify msDS-AllowedToActOnBehalfOfOtherIdentity to abuse Resource-Based Constrained Delegation via S4U2Self/S4U2Proxy. It also calls out Azure AD Connect MSOL_ sync accounts as especially dangerous because they hold DCSync rights, creating another non-obvious path to password-hash replication across the domain. The value here is less a new vulnerability than a practical attack-path analysis showing how identity, virtualization, and cloud federation permissions combine into hidden privilege-escalation chains that many IAM and PAM views miss.

[Read original article](https://www.praetorian.com/blog/shadow-admins-active-directory/){: .btn .btn-primary }
