---
layout: post
title: "The beast needs a cage: What's next for AppSec post-Mythos"
date: 2026-05-12 14:18:47 +0300
categories: [RSS]
tags: [ai, appsec, agentic, governance, burp-suite]
toc: true
---

PortSwigger argues that end-to-end AppSec workflows such as vulnerability discovery, validation, and remediation are becoming automatable with frontier and open-weight LLMs, but that the limiting factor is no longer raw model capability. The core technical point is that agentic models are structurally non-deterministic, so giving them offensive tooling without controls creates risks such as attacking the wrong target, leaking sensitive data, taking irreversible actions, or obscuring what they did. The post proposes a deterministic governance layer around the model that mediates every action with policy enforcement, human-in-the-loop approval, reproducibility safeguards, and a full audit trail rather than relying on prompting for safety. It also sketches how Burp Suite is evolving toward supervised agentic testing, where repetitive tasks like configuring Intruder-style attacks are automated while practitioners retain responsibility for attack selection, risk decisions, and oversight.

[Read original article](https://portswigger.net/blog/the-beast-needs-a-cage-whats-next-for-appsec-post-mythos){: .btn .btn-primary }
