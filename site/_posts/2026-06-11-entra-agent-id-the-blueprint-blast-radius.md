---
layout: post
title: "Entra Agent ID: The blueprint blast radius"
date: 2026-06-11 00:00:00 +0300
categories: [RSS]
tags: [cloud, entra, identity, supply-chain]
toc: true
---

Microsoft's Entra Agent ID framework allows a single blueprint (app registration) to create multiple agent identities and users across multiple tenants. If an attacker compromises a blueprint's credentials, they gain access to all agent identities derived from it, regardless of tenant — a significantly larger blast radius than the standard Entra application model, which creates only one identity per tenant. This risk parallels third-party application compromises (like Midnight Blizzard) but is amplified by the agent model's multi-identity architecture. The framework is already deployed in production Microsoft services (Copilot Studio, Microsoft Foundry), making this threat model immediately relevant to enterprise Entra deployments.

[Read original article](https://securitylabs.datadoghq.com/articles/agent-id-blueprint-blast-radius/){: .btn .btn-primary }
