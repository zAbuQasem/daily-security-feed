---
layout: post
title: "Field Notes: NSSM - the Non-Sucking Service Manager"
date: 2026-07-27 04:04:20 +0300
categories: [RSS]
tags: [persistence, detection, windows, incident-response, hunting]
toc: true
---

NSSM (Non-Sucking Service Manager) is a legitimate tool that attackers abuse to wrap persistent backdoors and tunneling utilities (e.g., ngrok) as auto-restarting Windows services. The technique masks the true payload behind an nssm.exe ImagePath entry; the actual executable and arguments are stored in the service's Parameters registry subkey (HKLM\System\CurrentControlSet\Services\[ServiceName]\Parameters). Detection methods include: monitoring Event ID 7045 for unexpected nssm.exe installations, inspecting the Parameters registry key for hidden executables and command-line arguments, and analyzing live process command lines with Process Explorer or Velociraptor. The article provides concrete hunting guidance with real-world examples (ngrok tunnels, Komari Agent C2) and demonstrates how to distinguish the wrapper from the payload during incident response.

[Read original article](https://dfir.ch/posts/field_notes_nssm/){: .btn .btn-primary }
