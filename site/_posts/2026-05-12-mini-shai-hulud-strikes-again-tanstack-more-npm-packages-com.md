---
layout: post
title: "Mini Shai-Hulud Strikes Again: TanStack + more npm Packages Compromised"
date: 2026-05-12 01:38:56 +0300
categories: [RSS]
tags: [supply-chain, npm, javascript, ci-cd, package-compromise]
toc: true
---

Wiz details a software supply-chain intrusion in which malicious versions of TanStack and other npm packages were published, turning routine dependency installation into attacker-controlled code execution on developer machines and CI runners. The core risk in this kind of compromise is the trust placed in popular packages and transitive dependencies: once the poisoned release is installed, embedded package code or install-time behavior can steal tokens, environment secrets, and other credentials, and can tamper with downstream builds. Because these packages sit inside JavaScript build and application pipelines, the impact extends beyond direct users to any project that resolves the compromised versions during install. This is high-priority research because it shows how compromise of a trusted npm publishing path can rapidly propagate through the broader ecosystem and create immediate credential-theft and build-integrity risk.

[Read original article](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised){: .btn .btn-primary }
