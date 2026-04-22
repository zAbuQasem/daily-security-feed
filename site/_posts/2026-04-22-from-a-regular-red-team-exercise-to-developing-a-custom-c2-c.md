---
layout: post
title: "From a Regular Red Team Exercise to Developing a Custom C2 Channel over MS Teams"
date: 2026-04-22 03:12:32 +0300
categories: [RSS]
tags: [red-team, c2, microsoft-teams, html-smuggling, edr-evasion]
toc: true
---

The post walks through a red-team operation that initially used HTML smuggling to deliver a 7z archive containing a signed executable and malicious DLLs, then relied on DLL hijacking to drop a payload into the current user's AppData so it would be loaded by Microsoft Teams on startup. The implant itself supported HTTPS beaconing, proxy detection, transparent proxy authentication with the victim's credentials, and tunneling, but it consistently failed in the target environment even though the full chain worked in the lab and bypassed EDR. The root cause was an enterprise egress architecture that chained a traditional web proxy with a virtual browsing / remote browser isolation layer, meaning outbound web content was rendered in a remote container and returned as sanitized HTML, which broke conventional C2 retrieval paths. The article's main value is in showing how modern browser-isolation controls can invalidate otherwise viable post-exploitation channels and force operators to pivot to alternate, application-native communications such as a custom C2 channel over Microsoft Teams.

[Read original article](https://blog.scrt.ch/2026/04/21/from-a-regular-red-team-exercise-to-developing-a-custom-c2-channel-over-ms-teams/){: .btn .btn-primary }
