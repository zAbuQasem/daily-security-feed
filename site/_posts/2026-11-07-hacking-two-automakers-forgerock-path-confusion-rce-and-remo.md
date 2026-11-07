---
layout: post
title: "Hacking Two Automakers: ForgeRock Path Confusion, RCE, and Remote Vehicle Access"
date: 2026-11-07 00:00:00 +0300
categories: [RSS]
tags: [rce, authentication-bypass, path-confusion, automotive]
toc: true
---

Security researchers discovered a vulnerability chain in ForgeRock deployments used by two major automakers that enabled remote code execution on production identity servers. The attack exploited a path confusion technique between the WAF and Java backend—using URL encoding, dot segments, and semicolon path parameters under a static asset prefix to bypass authentication checks on administrative endpoints like /system/console/configMgr. From the compromised ForgeRock servers, attackers could create valid sessions for any customer account and, if linked to a connected vehicle, gain full remote access to the vehicle (location, telemetry, lock/unlock, engine start/stop). Both vendors patched within two hours of responsible disclosure; the vulnerability affected customers across multiple regions.

[Read original article](https://samcurry.net/forgerock){: .btn .btn-primary }
