---
layout: post
title: "Block malicious packages across your organization with Supply Chain Firewall and Datadog Code Security"
date: 2026-10-01 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, malware, ci-cd, defensive, tooling]
toc: true
---

Datadog announces expanded organization-wide capabilities for Supply Chain Firewall, an open-source tool that intercepts package manager commands (npm, pip, poetry) and blocks known-malicious packages before installation by evaluating them against malicious package feeds, vulnerability advisories, and recency checks. The new features include centralized configuration management through Datadog Code Security (allowlist/blocklist policies synced across developer machines and CI systems), retroactive scanning to detect packages later identified as malicious, and GitHub Actions integration to protect CI/CD workflows. This installation-time control complements existing dependency scanning by preventing known threats from executing in the first place, addressing attack campaigns like Shai-Hulud 2.0 that spread malware through package registries.

[Read original article](https://www.datadoghq.com/blog/supply-chain-firewall-code-security/){: .btn .btn-primary }
