---
layout: post
title: "N4D Mesh Controller: New infrastructure, a UPX-packed agent labeled \"go-titan,\" and how to hunt for it"
date: 2026-08-20 00:00:00 +0300
categories: [RSS]
tags: [malware, rce, cloud, ai-infrastructure, detection]
toc: true
---

N4D Mesh Controller is an active Linux malware framework that exploits exposed Model Context Protocol (MCP) servers to gain command execution and lateral movement. The attack methodology—automated MCP service enumeration, tool classification, and invocation of dangerous capabilities like `execute_command`—eliminates the need for memory corruption exploits; unauthenticated command-execution tools are compromised directly. The newer agent (`go-titan`) contains service-specific exploit paths for PostgreSQL, MySQL, Redis, Docker, Kubernetes, Ray Dashboard, and LightLLM, enabling beachhead-to-lateral-movement chains. Persistence achieved via hidden cron entries, shell-profile modification, SSH key injection, and systemd units; secondary C2 via Cloudflare Quick Tunnel. Datadog observed new infrastructure rotation (209.99.186.235) and an evolved loader-to-agent chain, confirming active campaign development and ongoing threat to AI/LLM and cloud infrastructure.

[Read original article](https://securitylabs.datadoghq.com/articles/n4d-mesh-controller-go-titan-new-infrastructure-hunting/){: .btn .btn-primary }
