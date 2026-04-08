---
layout: post
title: "Remote Session Enumeration via Undocumented Windows APIs"
date: 2026-04-08 00:00:00 +0300
categories: [RSS]
tags: [windows, enumeration, red-team, undocumented-api, rdp]
toc: true
---

This article demonstrates remote user session enumeration on Windows hosts using undocumented WinStation APIs from winsta.dll — specifically WinStationOpenServerW, WinStationEnumerateW, and WinStationQueryInformationW — without requiring Remote Desktop to be enabled on the target. Unlike the well-documented Terminal Services (WTS) API via wtsapi32.h, the WinStation API has no SDK header, requiring manual function prototype definitions and dynamic loading via LoadLibrary/GetProcAddress. The technique works by opening a server handle to a remote host, enumerating session IDs and their states, then querying per-session info to retrieve logged-on usernames and session state (active vs. disconnected). This provides a stealthy reconnaissance primitive for lateral movement and host profiling, since defenders may not expect session enumeration on hosts where RDP is explicitly disabled.

---

[Read original article](https://0xv1n.github.io/posts/sessionenumeration/)
