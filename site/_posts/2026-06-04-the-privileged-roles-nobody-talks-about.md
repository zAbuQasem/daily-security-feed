---
layout: post
title: "The Privileged Roles Nobody Talks About"
date: 2026-06-04 04:00:00 +0300
categories: [RSS]
tags: [cloud, identity, privilege-escalation, infrastructure, iam]
toc: true
---

TrustedSec's analysis reveals that MDM platform administrators (Intune, SCCM) hold infrastructure-level control equivalent to or exceeding Domain Admin privileges—capable of deploying arbitrary code as SYSTEM, issuing remote wipes, and modifying security baselines across entire device fleets—yet are routinely under-protected compared to traditional admin roles. The article documents a consistent pattern across IR engagements: lack of account separation (admins using the same account for email/browsing), no dedicated administrative workstations, no just-in-time elevation via PIM, and critically, over-permissioned Graph API app registrations holding `DeviceManagementConfiguration.ReadWrite.All` that enable programmatic full Intune control without portal access. A single compromised Intune admin session (or leaked app registration secret) gains persistent, scalable access to every managed device, with most organizations having no monitoring on Graph API-initiated changes and Multi-Admin Approval disabled. This represents a systematic blind spot in privilege models: these roles are treated as operational IT functions rather than security-tier controls.

[Read original article](https://trustedsec.com/blog/the-privileged-roles-nobody-talks-about){: .btn .btn-primary }
