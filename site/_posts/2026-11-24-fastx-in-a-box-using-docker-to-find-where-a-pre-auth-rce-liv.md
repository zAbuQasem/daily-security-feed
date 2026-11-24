---
layout: post
title: "FastX in a Box: Using Docker to Find Where a Pre-Auth RCE Lived (and How It Died)"
date: 2026-11-24 05:00:00 +0300
categories: [RSS]
tags: [rce, cve, fastx, vulnerability-research, pre-auth]
toc: true
---

A pre-auth RCE vulnerability exists in FastX (StarNet's browser-based remote desktop server) versions 3.0.41 through 3.1.27, allowing unauthenticated users to spawn terminal sessions and execute arbitrary commands. The root cause is a Socket.IO server initialization flaw in the terminal module: the `start()` function receives an Express app object but attempts to access an undefined `.server` property, resulting in `socketIo(undefined)`, which creates a dangling server never mounted to the HTTP listener. The vulnerability was accidentally fixed in 3.2.27 when the terminal feature broke due to refactoring. The researcher developed a methodical testing approach using Docker containers and static package analysis to identify the exact vulnerable version range and confirm exploitation across multiple builds.

[Read original article](https://trustedsec.com/blog/fastx-in-a-box){: .btn .btn-primary }
