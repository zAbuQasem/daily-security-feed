---
layout: post
title: "Gheist: Attempted Scaled Abuse of Stolen GitHub Tokens Stumbles"
date: 2026-10-25 17:55:33 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, github, token-abuse, secrets]
toc: true
---

Gheist is an automated campaign exploiting stolen GitHub tokens to inject secret-dumping workflows into every repository accessible to the compromised credentials. The attack uses no command-and-control server, instead abusing GitHub's native workflow capabilities for direct secret exfiltration, and continuously evolves to bypass defenses. Recent GitHub security improvements have significantly disrupted the campaign, but the technique demonstrates a critical supply-chain risk: a single exposed token enables repository-wide malicious automation without external infrastructure. This is a high-fidelity example of how GitHub token compromise translates to scaled infrastructure compromise.

[Read original article](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles){: .btn .btn-primary }
