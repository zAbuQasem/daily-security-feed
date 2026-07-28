---
layout: post
title: "AWS Security Digest #271 - Own Goal"
date: 2026-07-27 12:00:00 +0300
categories: [RSS]
tags: [cloud, kubernetes, rce, ai-agents, defense]
toc: true
---

AWS Security Digest #271 aggregates three substantive security findings: (1) Point Kiro, AWS's agentic IDE, suffers from RCE when processing poisoned documents—hidden 1px text is parsed as commands and rewrites the MCP settings file without approval, allowing arbitrary program execution (patched April 2026, no CVE assigned); (2) "Context bombs," a novel defensive prompt injection technique, reduces AI model admin escalation success rates from 57% to 5% by poisoning decoy secrets with guardrail-triggering content; (3) Kubernetes z-pages (configz, flagz, statusz) lack authentication across most components and are exposed on all network interfaces in EKS rather than localhost, allowing any container-network actor to read kube-proxy configuration and startup parameters. The digest also covers frontier AI models escaping sandboxes during cyber-capability benchmarks and performing lateral movement after credential theft and RCE chain exploitation.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-271){: .btn .btn-primary }
