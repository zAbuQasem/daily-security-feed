---
layout: post
title: "ARTEX and beyond: AI-enabled penetration testing platforms"
date: 2026-11-13 20:57:13 +0300
categories: [RSS]
tags: [ai-enabled-attacks, supply-chain, attack-automation, cloud, threat-intelligence]
toc: true
---

Cisco Talos reports widespread in-the-wild deployment of AI-enabled penetration testing frameworks, notably ARTEX, which compress attack chains that previously took skilled teams hours or days into machine-speed operations. ARTEX uses a planner-agent architecture that breaks objectives into tasks, deploys worker agents with integrated tools (nmap, nuclei, Censys, Shodan, CAPTCHA bypass services, credential leak databases), and maintains a shared graph of assets and findings; it supports multiple LLMs and integrates via MCP with additional tooling including C2 frameworks. Multiple distinct threat actor groups—VAPOR PANDA (targeting 200+ orgs across 14 countries), Storm-0940 (leveraging ConnectWise compromise to target 2,250+ Microsoft 365 tenants), and Cambodia-based Storm-3358—have weaponized ARTEX within weeks of its July 2026 GitHub release for espionage, credential theft, supply chain attacks, and financial sector compromise across government, defense, telecom, and tech sectors. The frameworks present defensive challenges: reduced detection windows without known IOCs and response speeds that outpace human incident response, making AI-assisted containment and advanced threat hunting essential.

[Read original article](https://blog.talosintelligence.com/artex-and-beyond/){: .btn .btn-primary }
