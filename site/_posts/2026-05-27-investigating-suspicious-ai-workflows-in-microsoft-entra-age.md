---
layout: post
title: "Investigating suspicious AI workflows in Microsoft Entra Agent ID: Autonomous agents"
date: 2026-05-27 12:58:44 +0300
categories: [RSS]
tags: [detection, cloud, identity, azure, ai-security]
toc: true
---

Red Canary investigates threat detection for Microsoft Entra Agent ID — a new identity class for autonomous AI agents distinct from human and workload identities. The article focuses on a scenario where an autonomous agent (using the Agent autonomous app OAuth flow) performs unauthorized privileged actions in an Entra tenant, such as adding credentials to agent identity blueprints, enabling privilege escalation and persistence. Key risk: blueprints are the sole authentication point for Agent ID, so compromising blueprint credentials or gaining permission to add creds grants the ability to authenticate as any blueprint principal and all child agent identities. The post walks through the Microsoft Graph/Entra audit log fields needed to detect and investigate such behavior, applying a 'minimum viable storytelling' methodology to build detective controls for this emerging identity class.

[Read original article](https://redcanary.com/blog/threat-detection/entra-id-ai-workflows/){: .btn .btn-primary }
