---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 16"
date: 2026-04-18 03:10:51 +0300
categories: [RSS]
tags: [phishing, dprk, malware, nginx, auth-bypass]
toc: true
---

This weekly roundup aggregates three technically relevant stories: the FBI and Indonesian authorities dismantled the W3LL phishing ecosystem, a phishing-as-a-service platform that cloned login portals and used adversary-in-the-middle techniques to bypass MFA and support large-scale business email compromise. It also covers CERT-UA's report on the AgingFly campaign against Ukrainian government and healthcare targets, where phishing-delivered LNK files launch a script chain that installs a C# backdoor capable of command execution, file theft, screenshots, keylogging, Telegram-based C2 updates, and even on-host compilation of downloaded handler source code to reduce static detection. The article further summarizes active exploitation of CVE-2026-33032 in Nginx UI, where an exposed `/mcp_message` endpoint in MCP-enabled deployments allows unauthenticated attackers to establish a session, reuse a session ID, invoke privileged MCP functions, alter configuration, and restart services for full server takeover. While it is a news-style digest rather than an original deep dive, it points readers to concrete attack mechanics, affected software, and operational impact across phishing, state-backed intrusion support, commodity malware tradecraft, and exposed management-plane vulnerabilities.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-16-7/){: .btn .btn-primary }
