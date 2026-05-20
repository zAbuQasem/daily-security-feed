---
layout: post
title: "durabletask: TeamPCP's Latest PyPi Compromise"
date: 2026-05-19 17:30:20 +0300
categories: [RSS]
tags: [supply-chain, pypi, python, credential-theft, ci-cd]
toc: true
---

Wiz documents a TeamPCP supply-chain compromise involving the PyPI package durabletask, where a trojanized package release turned a normal Python dependency install into an attacker foothold. The key mechanism is registry-distributed malicious code delivered through the package itself, letting the actor target developer workstations and CI environments that automatically fetch and execute Python package contents during install or runtime. Systems are affected if they pulled the poisoned durabletask version from PyPI, with the practical impact centered on credential theft, account takeover, and downstream pipeline compromise rather than a single-application bug. This is high-signal because it shows TeamPCP continuing cross-ecosystem package attacks and using trusted software distribution channels for persistence and wider supply-chain reach.

[Read original article](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack){: .btn .btn-primary }
