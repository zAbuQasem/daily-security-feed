---
layout: post
title: "Building a Detection Foundation: Part 5 - Correlation in Practice"
date: 2026-04-08 00:00:00 +0300
categories: [Research, Solid]
tags: [detection, windows, siem, threat-hunting, dfir]
pin: false
toc: true
---

TrustedSec's final installment in their detection foundation series focuses on correlating Windows event logs for detection engineering and incident response. The core technique uses the LogonID field (from Event 4624) as a thread linking process creation (4688/Sysmon 1), object access (4656/4663), PowerShell execution (4103/4104), and network connections (Sysmon 3) across a single logon session. A worked phishing scenario traces a malicious PowerShell download cradle (IEX + certificate validation bypass) back through the parent process chain to Outlook, confirms C2 connectivity via Sysmon Event 3, and scopes the compromise window using logon/logoff events. The article also provides concrete Sigma rules and pseudocode correlation logic for high-value detections: LSASS access from non-standard parents (GrantedAccess 0x1010/0x1FFFFF), download-and-execute patterns within 30-second windows, and persistence-then-execution via registry Run key monitoring (Sysmon Event 13 → Event 1).

---

[Read original article](https://trustedsec.com/blog/building-a-detection-foundation-part-5-correlation-in-practice)

> Source: `trustedsec.com`
