---
layout: post
title: "Compromised AsyncAPI npm packages: inside a CI supply-chain attack"
date: 2026-07-14 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, npm, malware, credential-theft]
toc: true
---

Four popular npm packages in the @asyncapi namespace (3+ million weekly downloads) were compromised via a CI pipeline attack that stole bot account credentials, allowing an attacker to inject obfuscated malicious code across the repository. The attack uses a two-stage payload: the first stage downloads and executes a second-stage via IPFS, which then harvests cloud credentials (.aws/credentials, .kube/config, GCP tokens), package registry tokens, and communication platform secrets, while injecting persistence hooks into .vscode/tasks.json and .claude/settings.json. The second-stage payload implements sophisticated command and control using elliptic curve cryptography (secp256k1), encrypted configuration files, and resilient fallback channels including Nostr relays and libp2p mesh networks. Affected versions: @asyncapi/generator 3.3.1, @asyncapi/generator-components 0.7.1, @asyncapi/generator-helpers 1.1.1, @asyncapi/specs 6.11.2 and 6.11.2-alpha.1. This demonstrates a sophisticated threat actor with deep CI/CD infrastructure knowledge targeting developer supply chains at scale.

[Read original article](https://securitylabs.datadoghq.com/articles/compromised-asyncapi-npm-packages/){: .btn .btn-primary }
