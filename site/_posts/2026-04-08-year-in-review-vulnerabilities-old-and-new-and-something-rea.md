---
layout: post
title: "Year in Review: Vulnerabilities old and new and something React2"
date: 2026-04-08 00:00:00 +0300
categories: [Research, Solid]
tags: [threat-intelligence, rce, exploit, detection, cve]
pin: false
toc: true
---

Talos's 2025 Year in Review highlights the year's most exploited vulnerabilities, with React2Shell (a 2025 RCE chain) spiking to the #1 attacked CVE in the final three weeks of the year, followed by perennial staples PHPUnit (CVE from 2017) and Log4j (2021). The report identifies a structural attacker shift: targeting is now driven by exposure and proximity to identity/trust systems rather than vulnerability age, with network appliances, SSO components, and legacy open-source dependencies (ColdFusion, Log4j, PHPUnit) as primary vectors. RCE-class flaws dominate because they require no user interaction, and identity-adjacent systems are disproportionately targeted because compromising them invalidates MFA and bypasses network segmentation. AI-assisted exploit development is shortening time-to-exploit, shrinking the defender reaction window between disclosure and mass exploitation. Organizations are advised to prioritize patching of perimeter and identity-centric components ahead of standard patch cycle cadence.

---

[Read original article](https://blog.talosintelligence.com/year-in-review-vulnerabilities-old-and-new-and-something-react2/)

> Source: `blog.talosintelligence.com`
