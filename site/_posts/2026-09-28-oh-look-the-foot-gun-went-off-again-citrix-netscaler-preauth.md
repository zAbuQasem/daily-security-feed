---
layout: post
title: "Oh Look, The Foot Gun Went Off Again (Citrix NetScaler PreAuth Command Injection CVE-2026-88771)"
date: 2026-09-28 10:55:54 +0300
categories: [RSS]
tags: [rce, citrix, zero-day, preauth, critical]
toc: true
---

CVE-2026-88771 is a pre-authentication command injection vulnerability in Citrix NetScaler ADC and NetScaler Gateway caused by improper input validation, allowing unauthenticated attackers to execute arbitrary commands in the default configuration. The vulnerability is rated 9.5 CVSS critical, affects ubiquitous enterprise VPN and load-balancing appliances, and was actively exploited in the wild before patches were available. Citrix disclosed eight related vulnerabilities simultaneously (CVE-2026-88771 through CVE-2026-88778), including a DTLS memory overflow (CVE-2026-88772) and HTTP request smuggling (CVE-2026-88773). watchTowr's analysis compares vulnerable (14.1-73.30) to patched (14.1-73.37) builds to identify the root cause, highlighting Citrix's delayed communication and the real-world impact on thousands of organizations with exposed remote access infrastructure.

[Read original article](https://labs.watchtowr.com/oh-look-the-foot-gun-went-off-again-citrix-netscaler-preauth-command-injection-cve-2026-88771/){: .btn .btn-primary }
