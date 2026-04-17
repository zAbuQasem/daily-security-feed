---
layout: post
title: "The case for dependency cooldowns in a post-axios world"
date: 2026-04-17 03:12:26 +0300
categories: [RSS]
tags: [supply-chain, npm, dependencies, ci-cd, defense]
toc: true
---

Datadog argues for enforcing dependency "cooldowns" to reduce the risk of consuming freshly published malicious package versions, using the recent Axios npm compromise and prior s1ngularity/Shai-Hulud campaigns as case studies. The core technical issue is that modern package managers and CI pipelines automatically trust newly released versions—especially when semver ranges like ^ and ~ are used—so attacker-controlled releases can be pulled into builds within minutes without human review. The article highlights newly added package-age controls such as npm's `min-release-age`, pnpm's `minimumReleaseAge`, Yarn's `npmMinimalAgeGate`, and Dependabot cooldown policies, showing how a 12-hour to 7-day delay would have blocked several recent malicious releases. It also notes the limits of the approach: patient attackers can delay payload execution past the waiting window, and cooldowns do not address ordinary vulnerable-but-non-malicious dependency updates.

[Read original article](https://securitylabs.datadoghq.com/articles/dependency-cooldowns/){: .btn .btn-primary }
