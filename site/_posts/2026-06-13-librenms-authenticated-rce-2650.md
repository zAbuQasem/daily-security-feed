---
layout: post
title: "LibreNMS Authenticated RCE (< 26.5.0)"
date: 2026-06-13 02:35:02 +0300
categories: [RSS]
tags: [rce, command-injection, librenms, authenticated]
toc: true
---

Three authenticated remote code execution vulnerabilities in LibreNMS allow admin users to execute arbitrary commands as the librenms system user. The primary vulnerability (CVE-affecting < 26.4.1) stems from unsanitized user input in LibreNMS/OS/Traits/VminfoLibvirt.php passed directly to exec() via Libvirt Username and Protocols fields; injected commands execute when the poller runs discovery jobs. A secondary chain attack (< 26.5.0) bypasses escapeshellarg() in Signal.php by manipulating the signal-cli binary path to point to scripts/composer_wrapper.php, which concatenates arguments directly into a passthru() command without sanitization. A third technique allows arbitrary file writes by modifying the virsh binary path to wget and hosting malicious PHP on an internal device. All exploitation paths are documented with step-by-step PoC using webhook exfiltration and remote shell access.

[Read original article](https://projectblack.io/blog/librenms-authenticated-rce-26-5-0/){: .btn .btn-primary }
