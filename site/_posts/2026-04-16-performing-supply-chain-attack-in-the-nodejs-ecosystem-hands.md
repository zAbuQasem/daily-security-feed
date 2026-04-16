---
layout: post
title: "Performing Supply-Chain Attack in the NodeJS Ecosystem [hands-on exercise]"
date: 2026-04-16 03:12:29 +0300
categories: [RSS]
tags: [supply-chain, nodejs, ssrf, verdaccio, ctf]
toc: true
---

This hands-on CTF write-up models a Node.js supply-chain compromise against an application that consumes a private `prisoner-db` package from a local Verdaccio registry. The target stack includes a cron job that runs `npm outdated prisoner-db`, automatically executes `npm update prisoner-db`, and restarts the PM2-managed app, so publishing a higher package version yields code execution in the application path. The initial foothold is a full-read SSRF in the package's `importPrisoner()` method, which calls `curl.get(url)` on attacker-supplied URLs and stores the response body, enabling internal service access and local file disclosure to recover material useful for registry authentication. The post is useful because it ties together private npm registry abuse, dependency auto-update behavior, and SSRF-to-package-publishing as a realistic supply-chain attack chain rather than treating malicious package publication as an isolated step.

[Read original article](https://rayhan0x01.github.io/ctf/2024/09/14/performing-supply-chain-attack-in-the-nodejs-realm-hands-on.html){: .btn .btn-primary }
