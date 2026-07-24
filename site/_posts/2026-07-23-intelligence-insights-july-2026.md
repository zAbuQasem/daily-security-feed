---
layout: post
title: "Intelligence Insights: July 2026"
date: 2026-07-23 17:12:43 +0300
categories: [RSS]
tags: [malware, threat-intelligence, paste-and-run, detection, evasion]
toc: true
---

Red Canary's July 2026 threat intelligence report details the top 10 most prevalent threats in customer environments. ClearFake remains dominant, using JavaScript injected into compromised websites to deliver malware via fake CAPTCHA lures and paste-and-run commands. KongTuke, a WordPress-based traffic distribution system, surged in activity in June, often chaining with paste-and-run for initial execution using caret-obfuscated `curl` commands to `.top` domains. CastleLoader, a malware loader delivering infostealers and RATs, escalated through BackgroundFix campaigns (fake background removal sites) and LinkedIn/Indeed domain typosquatting using Google Ads, employing `finger.exe` for command retrieval and Bring-Your-Own-Interpreter (BYOI) techniques with portable Python distributions to avoid detection. The report provides specific attack chains, obfuscation methods, and infrastructure indicators valuable for detection and threat hunting.

[Read original article](https://redcanary.com/blog/threat-intelligence/intelligence-insights-july-2026/){: .btn .btn-primary }
