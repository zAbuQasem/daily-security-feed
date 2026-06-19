---
layout: post
title: "Entra Agent ID: Inside a cross-tenant agent compromise"
date: 2026-06-18 00:00:00 +0300
categories: [RSS]
tags: [azure, identity, cloud, supply-chain, privilege-escalation]
toc: true
---

Datadog Security Labs demonstrates a cross-tenant compromise of Azure Entra agents through third-party blueprint manipulation. An attacker with Agent ID Administrator role can inject a credential into a shared blueprint, then use that credential to authenticate as any agent instance derived from that blueprint across multiple Entra tenants, regardless of tenant relationship. In the demonstrated scenario, the attacker gains access to agents with UserAuthMethod-TAP.ReadWrite.All and User.Read.All permissions, enabling account takeover and MFA reset. This attack mirrors Midnight Blizzard tactics and highlights the supply-chain risk of trusting third-party agent identity blueprints with high-privilege permissions.

[Read original article](https://securitylabs.datadoghq.com/articles/agent-id-inside-agent-compromise/){: .btn .btn-primary }
