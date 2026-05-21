---
layout: post
title: "Tracking TamperedChef Clusters via Certificate and Code Reuse"
date: 2026-05-20 10:00:46 +0300
categories: [RSS]
tags: [malware, malvertising, infostealer, code-signing, threat-intel]
toc: true
---

Unit 42 maps multiple TamperedChef-style malware clusters by correlating reused code, shared code-signing infrastructure, corporate registration data, and advertising overlap across more than 4,000 samples and 100+ variants. The malware is packaged as legitimate-looking productivity software such as PDF editors, calendars, ZIP tools, and GIF makers, then distributed through malvertising and polished download sites that provide real functionality while embedding loaders, RAT features, or arbitrary binary execution paths. A key tradecraft detail is long dormancy combined with frequent binary rebuilds, code signing, campaign-specific domains, and EULA-backed browser or system modification language, which helps these samples evade both user suspicion and hash-based detection before later pulling stealers, proxyware, or remote access payloads. The article is useful because it reframes these apps as malware rather than mere PUP/adware, and provides cluster-level tracking methodology defenders can use to identify related campaigns beyond single hashes or brand names.

[Read original article](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/){: .btn .btn-primary }
