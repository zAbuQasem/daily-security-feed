---
layout: post
title: "Should I Azure AD Sync/Entra Cloud Sync Domain Admins?"
date: 2026-09-22 03:59:10 +0300
categories: [RSS]
tags: [cloud, identity-and-access, privilege-escalation, defense, hybrid]
toc: true
---

Organizations migrating to cloud-native Entra ID often mistakenly sync on-premises Domain Admin accounts as Global Admins, creating a bidirectional cross-boundary pivot risk. An attacker with on-prem DA compromise can escalate to cloud GA and take over the Entra environment; conversely, if password writeback is enabled, cloud GA compromise allows reverse pivoting to on-prem AD. This practice violates CIS control 1.1.1 and Microsoft's own best-practice guidance. Remediation involves creating cloud-only administrative accounts, syncing only non-privileged end-user accounts, and leveraging Entra ID P2 PIM for just-in-time privilege elevation rather than standing privileged hybrid accounts.

[Read original article](https://projectblack.io/blog/ensure-administrative-accounts-are-cloud-only/){: .btn .btn-primary }
