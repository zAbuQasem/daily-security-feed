---
layout: post
title: "Introducing Package Proxy: supply-chain safety checks without client-side software"
date: 2026-06-05 06:43:41 +0300
categories: [RSS]
tags: [supply-chain, defense, package-security, cloudflare]
toc: true
---

Thinkst released Package Proxy, a Cloudflare Workers proxy that intercepts package manager requests (npm, pip, uv, cargo) to enforce supply-chain safety policies before installation. It implements fast inline checks: 10+ day package age minimum, upload method integrity verification, blocklists, and allowlists—raising attacker effort without requiring client-side wrappers. Deployed internally, it has prevented recent breaches including TanStack, Bitwarden, and TeamPCP npm attacks through age and integrity checks. The tool is open-source with one-click Cloudflare deployment, enabling uniform policy enforcement across different package manager versions.

[Read original article](https://blog.thinkst.com/2026/06/introducing-package-proxy-supply-chain-safety-checks-without-client-side-software.html){: .btn .btn-primary }
