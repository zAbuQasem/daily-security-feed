---
layout: post
title: "Context.ai OAuth Token Compromise"
date: 2026-04-21 03:12:41 +0300
categories: [RSS]
tags: [oauth, supply-chain, saas, token-compromise]
toc: true
---

This post describes a compromise of Context.ai OAuth tokens that let attackers operate through an already-trusted SaaS integration, turning delegated access into a supply-chain attack path. The core issue is the exposure or theft of OAuth tokens with pre-granted scopes, which can let an adversary call connected APIs and act as the integration against downstream services without needing the victim's primary credentials. The affected systems are environments that authorized Context.ai and any linked platforms reachable through those tokens, with impact depending on the scopes granted and the integrations present. Practically, it is a reminder that OAuth grants to third-party SaaS apps create a transitive trust boundary: if the vendor or token is compromised, the blast radius can extend into internal data, workflows, and potentially development tooling.

[Read original article](https://www.wiz.io/blog/contextai-oauth-token-compromise){: .btn .btn-primary }
