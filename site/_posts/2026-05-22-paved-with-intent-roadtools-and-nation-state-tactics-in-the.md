---
layout: post
title: "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud"
date: 2026-05-22 10:00:24 +0300
categories: [RSS]
tags: [cloud, entra-id, oauth, token-abuse, detection]
toc: true
---

Unit 42 analyzes how attackers operationalize ROADtools against Microsoft Entra ID, focusing on two core modules: ROADrecon for tenant enumeration and roadtx for token acquisition, exchange, and device registration. The tooling works through legitimate Microsoft APIs and supports OAuth/OIDC flows such as device code, refresh token reuse, and on-behalf-of exchanges, which lets adversaries replay or manipulate tokens, persist access, and in some cases bypass MFA while blending into normal cloud traffic with customizable user-agent strings. The article highlights how ROADrecon maps users, groups, roles, devices, service principals, and applications into a local SQLite-backed graph of privileged relationships, making it useful for discovery and escalation planning even as the ecosystem shifts from Azure AD Graph to fragmented Microsoft Graph forks. This is high-signal cloud identity tradecraft because it ties publicly available tooling to recent nation-state intrusions and pairs the offensive mechanics with concrete hunting opportunities for detecting ROADtools-style Entra ID activity.

[Read original article](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/){: .btn .btn-primary }
