---
layout: post
title: "HTB: AirTouch"
date: 2026-04-19 03:12:15 +0300
categories: [RSS]
tags: [ctf, wifi, snmp, rce, evil-twin]
toc: true
---

This Hack The Box write-up chains multiple wireless and web weaknesses in a simulated enterprise environment, starting with an SNMP-exposed default consultant password that grants SSH access to a containerized workstation. From there, the attacker captures and cracks a WPA2-PSK handshake, uses the recovered key to decrypt packet captures in Wireshark, and extracts session cookies for a router management interface where a client-side role cookie unlocks an admin upload feature. The web foothold becomes RCE by bypassing a PHP extension filter with a `.phtml` upload, and hardcoded credentials in source code provide the next local pivot. The final stage abuses leaked CA/server certs to run an evil twin AP with eaphammer, capture a PEAP-MSCHAPv2 challenge, crack a user password, and then recover an admin credential from `hostapd`'s `eap_user` file to reach root on the corporate wireless segment.

[Read original article](https://0xdf.gitlab.io/2026/04/18/htb-airtouch.html){: .btn .btn-primary }
