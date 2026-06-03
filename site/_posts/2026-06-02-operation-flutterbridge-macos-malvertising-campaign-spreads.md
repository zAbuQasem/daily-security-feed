---
layout: post
title: "Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor"
date: 2026-06-02 10:00:31 +0300
categories: [RSS]
tags: [malware, macos, backdoor, adware, malvertising]
toc: true
---

Unit 42 identified FlutterShell, a macOS backdoor delivered via widespread malvertising campaigns using hundreds of Google-verified shell company ads. The malware is built with the Flutter framework and uses a WebView-based JavaScript-to-native bridge architecture that allows attackers to dynamically modify malicious behavior from remote servers without recompiling binaries. FlutterShell provides shell command execution, file system manipulation, and environment variable exfiltration capabilities, while primarily functioning as adware that hijacks Chrome configuration files to route traffic through attacker-controlled ad servers. Some variants weaponize AI summarization features to exfiltrate documents by routing them through attacker infrastructure. All samples were signed with valid Apple Developer IDs and passed notarization, indicating successful evasion of Apple's automated security checks.

[Read original article](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/){: .btn .btn-primary }
