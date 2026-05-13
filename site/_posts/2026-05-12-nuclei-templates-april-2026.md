---
layout: post
title: "Nuclei Templates - April 2026"
date: 2026-05-12 11:26:09 +0300
categories: [RSS]
tags: [nuclei, vulnerability-scanning, cve, detection, llm]
toc: true
---

ProjectDiscovery's April 2026 Nuclei template release adds 226 templates covering 123 CVEs, including multiple CISA KEV entries and high-impact checks for auth bypass, RCE, SSRF, path traversal, SQLi, and arbitrary file read across products like Fortinet, ActiveMQ, Flowise, Langflow, LiteLLM, and Vite. The technically useful part is not just new coverage but detection engineering detail: the update fixes false negatives in templates such as LearnPress SQLi by adding a random-string technique to bypass database query caching, and adjusts Tomcat default-login payload ordering to avoid LockOutRealm shunning. It also reduces false positives by tightening overly broad regex-based credential leak detection and requiring stronger match conditions for cases like the ActiveMQ Artemis console default-login check. Beyond CVE coverage, the release expands exposure discovery for AI/LLM infrastructure, Perforce, blockchain RPC endpoints, default-logins, installer pages, and unauthenticated dashboards, making it a practical update for operators using Nuclei as an internet-exposure and vuln-detection feed.

[Read original article](https://projectdiscovery.io/blog/nuclei-templates-april-2026){: .btn .btn-primary }
