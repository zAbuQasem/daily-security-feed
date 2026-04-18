---
layout: post
title: "Beyond the Perimeter How an On-Premises Domain Admin Compromise Unlocked the Cloud"
date: 2026-04-18 03:10:45 +0300
categories: [RSS]
tags: [entra-id, active-directory, token-theft, hybrid-identity, m365]
toc: true
---

This write-up shows how an attacker who already reached on-premises Active Directory Domain Admin can pivot into Microsoft 365 by stealing Entra ID session tokens from a privileged user's workstation, effectively bypassing MFA and Conditional Access. The operators first enumerated cloud directory roles with ROADrecon using compromised credentials, identified a Global Administrator, then used Domain Admin access and SMB/WinRM to locate that user's active workstation and inspect logged-in sessions. After confirming Outlook and Teams were running under the target context, they dumped those Office processes and extracted bearer and refresh tokens from memory using simple string matching on the dump, allowing reuse against Microsoft Graph and other cloud resources. The practical impact is that hybrid identity environments can collapse from an on-prem compromise into full cloud tenant compromise when privileged admins use ordinary domain-joined workstations for Entra administration.

[Read original article](https://labs.cognisys.group/posts/Beyond-the-Perimeter-How-an-On-Premises-Domain-Admin-Compromise-Unlocked-the-Cloud/){: .btn .btn-primary }
