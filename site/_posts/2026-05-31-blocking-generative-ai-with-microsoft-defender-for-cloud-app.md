---
layout: post
title: "Blocking Generative AI with Microsoft Defender for Cloud Apps and Microsoft Defender for Endpoint"
date: 2026-05-31 05:00:00 +0300
categories: [RSS]
tags: [cloud, defense, microsoft, data-governance, endpoint-security]
toc: true
---

This article walks through a layered approach to blocking unsanctioned generative AI tools using Microsoft Defender for Cloud Apps (MDA), Microsoft Defender for Endpoint (MDE), and Microsoft Purview. The enforcement mechanism relies on MDE's Network Protection, which blocks access at the network level — covering all HTTP clients, not just browsers — once an app is tagged 'Unsanctioned' in MDA's app catalog. The workflow involves sanctioning allowed apps (e.g., M365 Copilot, Claude), creating an App Discovery Policy targeting the Generative AI category, and validating enforcement via device timeline and activity logs. Microsoft Purview sensitivity labels are then used to enforce data-level controls within sanctioned tools, distinguishing between data that stays in the M365 tenant versus data sent to external services.

[Read original article](https://thalpius.com/2026/05/31/blocking-generative-ai-with-microsoft-defender-for-cloud-apps-and-microsoft-defender-for-endpoint/){: .btn .btn-primary }
