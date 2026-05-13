---
layout: post
title: "Slamming the Door on Quick Assist Tech Support Scams and Abuse"
date: 2026-05-12 04:00:00 +0300
categories: [RSS]
tags: [quick-assist, social-engineering, windows, detection, rmm]
toc: true
---

TrustedSec documents a recurring attack pattern where adversaries prime victims with phishing emails, then call them over Microsoft Teams while impersonating IT and walk them into starting a Windows Quick Assist remote-support session. The useful technical detail is on detection: Quick Assist sessions generate outbound requests to legitimate Microsoft endpoints such as `/roleselection`, `/screenshare`, and `/status/ended`, which can be hunted in proxy logs, browser cache, and forensic artifacts, and newer Microsoft Store builds also emit Application event log entries under the `Quick Assist` source. The post distinguishes the legacy binary in `C:\Windows\System32\` from the newer WindowsApps version, noting the latter has better logging for incident reconstruction. It also gives concrete hardening guidance: remove or denylist Quick Assist if not needed, alert on reinstallation attempts, and consider replacing it with Intune Remote Help, which enforces authenticated sessions and improves accountability.

[Read original article](https://trustedsec.com/blog/slamming-the-door-on-quick-assist-tech-support-scams-and-abuse){: .btn .btn-primary }
