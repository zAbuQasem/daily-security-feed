---
layout: post
title: "Discovering Vulnerabilities in Enterprise Audiovisual Hardware"
date: 2026-05-01 00:00:00 +0300
categories: [RSS]
tags: [rce, command-injection, iot, firmware, hardware]
toc: true
---

This post analyzes enterprise audiovisual hardware used in meeting rooms and documents multiple serious flaws, starting with CVE-2026-26461 in the Aver PTC320UV2 camera. The author reversed the firmware's `cgi-bin` handler and showed that the `/action?Get=` endpoint passes attacker-controlled input into `snprintf(... "/mnt/sky/webui/opt_GetData.sh %s 2>&1")` before invoking it, making a request like `/action?Get=acc;ls;` an unauthenticated root command injection rather than merely a client-side auth bypass. The article also examines the Crestron TSW-1060 tablet attack surface, noting residual user data after factory resets plus exposed services including FTP, SSH, telnet, a web UI, and the proprietary Crestron Terminal Protocol. It further traces how restricted commands were historically protected by a deterministic `crengsuperuser` password derived from the device MAC address with hard-coded cryptographic material, highlighting how discontinued AV gear can retain exploitable management interfaces and sensitive data in real enterprise environments.

[Read original article](https://spaceraccoon.dev/discovering-vulnerabilities-enterprise-audiovisual-hardware/){: .btn .btn-primary }
