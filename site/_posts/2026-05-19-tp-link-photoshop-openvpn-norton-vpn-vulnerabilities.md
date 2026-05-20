---
layout: post
title: "TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities"
date: 2026-05-19 15:39:37 +0300
categories: [RSS]
tags: [router, rce, command-injection, lpe, vpn]
toc: true
---

Cisco Talos disclosed a batch of patched vulnerabilities spanning TP-Link Archer AX53 firmware, Adobe Photoshop's Microsoft Store installer, OpenVPN, and Norton VPN, with the most serious issues enabling code execution or privilege escalation. The TP-Link set includes a stack-based buffer overflow in tmpServer opcode 0x436 (CVE-2026-30814) that can be triggered by crafted network packets for potential RCE, plus multiple command injection and external-config-control bugs in OpenVPN and dnsmasq restore paths such as script_security, dhcpscript, client_connect, client_disconnect, and route_up, reachable through malicious uploaded configuration files. Talos also reports installer race/file-replacement privilege escalations in Photoshop_Set-Up.exe 2.11.0.30 and Norton VPN's Microsoft Store installation flow, where a low-privilege user can swap files during install to gain elevated effects, including arbitrary file deletion in the Norton case. OpenVPN 2.6.x and 2.8_git are affected by a reachable assertion in TLS Crypt v2 Client Key Extraction (CVE-2026-35058), allowing a remote attacker to send crafted packets that crash the process and cause denial of service.

[Read original article](https://blog.talosintelligence.com/tp-link-photoshop-openvpn-norton-vpn-vulnerabilities/){: .btn .btn-primary }
