---
layout: post
title: "System Over Model, Tested: Reproducing Mythos's FreeBSD Find on Local Open-Weight Models"
date: 2026-06-04 07:00:00 +0300
categories: [RSS]
tags: [freebsd, rce, buffer-overflow, ai-vuln-scan, vulnerability-discovery]
toc: true
---

CVE-2026-4747 is a 17-year-old RCE in FreeBSD's RPCSEC_GSS authentication caused by an unchecked buffer overflow in svc_rpc_gss_validate(), where attacker-controlled oa_length overruns a fixed 128-byte rpchdr stack buffer. This article reproduces AISLE's AI-powered nano-analyzer pipeline (a 3-stage LLM-driven scanner with context briefing, vulnerability scanning, and multi-round triage) on local open-weight models (gpt-oss-20b, gemma-4-31b-it) to find the same CVE that Anthropic's frontier model discovered. The key finding: open-weight models can locate critical vulnerabilities when paired with proper scaffolding; system design (prompts, pipeline shape, triage rounds) matters more than model choice, and adding a reachability stage dramatically reduces false positives while preserving detection of the real CVE.

[Read original article](https://clearbluejar.github.io/posts/system-over-model-tested-mythos-freebsd-local-openweight/){: .btn .btn-primary }
