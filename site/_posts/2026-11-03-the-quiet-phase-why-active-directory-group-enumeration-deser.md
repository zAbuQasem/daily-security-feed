---
layout: post
title: "The Quiet Phase: Why Active Directory Group Enumeration Deserves Your Attention"
date: 2026-11-03 05:00:00 +0300
categories: [RSS]
tags: [active-directory, detection-engineering, threat-hunting, auditing, reconnaissance]
toc: true
---

Active Directory group enumeration (MITRE ATT&CK T1069.002) is an early-stage attacker reconnaissance technique that precedes privilege escalation, but is rarely monitored. This article explains how to detect group membership reads by configuring System Access Control Lists (SACLs) on sensitive groups and correlating Windows Event ID 4662 (or 4799 for built-in groups) with logon events to determine the source account and IP. Implementation requires enabling audit policies on domain controllers and adding SACL audit rules for the 'member' attribute (GUID bf9679c0-0de6-11d0-a285-00aa003049e2). The article provides complete PowerShell code for configuration and discusses practical challenges: legitimate tools (Entra Connect, Exchange, PAM platforms) generate substantial noise, requiring careful tuning with honeypot groups to maintain signal-to-noise ratio. Defenders can catch attackers during planning rather than after privilege escalation using native Windows features.

[Read original article](https://trustedsec.com/blog/the-quiet-phase-active-directory-group-enumeration){: .btn .btn-primary }
