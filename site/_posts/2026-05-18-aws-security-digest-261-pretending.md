---
layout: post
title: "AWS Security Digest #261 - Pretending"
date: 2026-05-18 12:00:00 +0300
categories: [RSS]
tags: [aws, cloud, ai-agents, authorization-bypass, supply-chain]
toc: true
---

This issue is a curated AWS-focused security roundup rather than original research, but it highlights several technically relevant items for cloud defenders. The strongest entries include an Amazon Quick Chat Agent authorization bypass caused by a missing server-side check that allowed direct API use despite UI-level restrictions, and Datadog's analysis of Claude Code skills where `!`-based dynamic context executes shell commands before model safeguards can inspect the rendered prompt. It also calls out a public guest-to-host QEMU escape exploit chain targeting an experimental memory-device emulation feature, noting the feature is off by default and likely not exposed by major cloud providers. The rest of the digest mixes AWS AI security guidance, defensive blog posts, and numerous product/update announcements, so its value is mainly as a triage feed for practitioners tracking cloud and AI-adjacent security developments.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-261){: .btn .btn-primary }
