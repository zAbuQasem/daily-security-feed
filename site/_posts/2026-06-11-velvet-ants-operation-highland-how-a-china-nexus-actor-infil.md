---
layout: post
title: "Velvet Ant’s Operation Highland: How a China-Nexus Actor Infiltrated an Internal Network Undetected"
date: 2026-06-11 14:57:37 +0300
categories: [RSS]
tags: [apt, persistence, infrastructure, forensics, lateral-movement]
toc: true
---

Sygnia's forensic analysis reveals Velvet Ant maintained nearly a decade of undetected presence in a segregated critical infrastructure network by engineering a multi-stage attack chain from internet-facing systems through the IT network. The attacker achieved deep persistence by compromising the authentication layer—replacing PAM modules and OpenSSH binaries with nine separately-compiled backdoored variants that captured credentials and disabled their own forensic logging. Initial internet access was established via a modified GS-Netcat variant disguised as 'auditdb,' with SOCKS5 proxies and Nginx/FastCGI abuse enabling lateral movement into the isolated network. The attack exemplifies nation-state operational discipline: custom-built persistence primitives, authentication stack control to survive password changes and session terminations, and careful argv[0] manipulation to evade process monitoring.

[Read original article](https://www.sygnia.co/blog/operation-highland-velvet-ant/){: .btn .btn-primary }
