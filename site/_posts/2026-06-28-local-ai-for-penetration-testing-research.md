---
layout: post
title: "Local AI for Penetration Testing & Research"
date: 2026-06-28 04:34:33 +0300
categories: [RSS]
tags: [lfi, cve, sast, ai-tooling, methodology]
toc: true
---

The author benchmarks four approaches for detecting a known PHPIPAM Authenticated LFI vulnerability (CVE-2026-12194), where user-supplied controller names are directly concatenated into require_once() without sanitization. The vuln requires API enablement (disabled by default) and valid credentials but allows executing any .php file the web server can access. Testing reveals Semgrep's automatic rules miss it, Strix AI with GLM 5.1 consumed 60M tokens (~$30) and failed, Cloud SOTA code review was inconsistent, while local AI with custom harness succeeded—demonstrating that detection framework and approach matter more than model choice. The article also discloses the CVE publicly due to no maintainer response and low practical risk (limited impact without file upload primitives).

[Read original article](https://projectblack.io/blog/local-ai-for-cyber-security/){: .btn .btn-primary }
