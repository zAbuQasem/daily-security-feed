---
layout: post
title: "Segmenting a Home Network with UniFi Zone Firewall — Driven by an AI Agent"
date: 2026-09-19 04:13:45 +0300
categories: [RSS]
tags: [network-segmentation, firewall, defense, unifi, configuration]
toc: true
---

A detailed write-up of implementing zero-trust network segmentation on a home UniFi network by driving the controller API through an AI agent (Claude Code + MCP server). The author transformed a flat eight-VLAN topology with zero firewall policies into a default-deny zone model, improving an audit score from 70/100 to 93/100. The core technical lesson is architectural: moving from ad-hoc rules to an exhaustive N×N inter-zone matrix, and critical operational insights include why rule previews don't validate ordering dependencies, how zone reassignments silently invalidate existing rules, and a specific pattern (enumerate exceptions in a single REJECT) to avoid coupled rule failures. The post balances practical configuration guidance with candid failure analysis—particularly a brief DNS outage caused by rule ordering issues—making it valuable for network defenders considering either UniFi zone segmentation or agent-driven infrastructure management.

[Read original article](https://www.uncommonengineer.com/docs/engineer/LAB/unifi-zone-segmentation-mcp-agent){: .btn .btn-primary }
