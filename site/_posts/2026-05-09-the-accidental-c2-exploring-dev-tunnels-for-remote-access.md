---
layout: post
title: "The Accidental C2 - Exploring Dev Tunnels for Remote Access"
date: 2026-05-09 19:19:16 +0300
categories: [RSS]
tags: [vscode, dev-tunnels, remote-access, c2, red-team]
toc: true
---

This research dissects Visual Studio Code Dev Tunnels as a potential remote-access and C2 channel rather than just a developer convenience feature. The author shows that tunnel discovery starts with authenticated REST calls to `global.rel.tunnels.api.visualstudio.com`, where a GitHub token can enumerate globally available tunnels tagged `vscode-server-launcher` and reveal metadata such as `clusterId`, `tunnelId`, relay WebSocket URIs, and forwarded port information. Using the discovered `clusterId` and `tunnelId`, a client can request a `tokenScopes=connect` access token from the cluster-specific tunnels API, which is the first step toward interacting with an existing VS Code remote server. The practical relevance is that VS Code’s tunneling stack appears layered and non-standard, but exposes enough management and connection primitives that an operator who understands the protocol can potentially repurpose it for stealthy remote shell access and file movement during assessments.

[Read original article](https://blog.xpnsec.com/accidental-c2/){: .btn .btn-primary }
