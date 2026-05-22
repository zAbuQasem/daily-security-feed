---
layout: post
title: "Shai-Hulud Is Back, and This Time It Ate the Whole Ecosystem"
date: 2026-05-21 04:00:00 +0300
categories: [RSS]
tags: [supply-chain, npm, ci-cd, malware]
toc: true
---

TrustedSec documents a renewed Shai-Hulud npm supply-chain campaign in which a compromised maintainer account published malicious versions of more than 300 packages across the @antv ecosystem, plus high-volume packages like timeago.js, echarts-for-react, and jest-canvas-mock. The malware executes from preinstall/postinstall hooks, then deobfuscates into a multi-stage payload that scrapes `/proc/self/maps` and `/proc/<pid>/mem` to recover unmasked `ACTIONS_` secrets from GitHub Actions runner heap memory, bypassing normal log masking protections. It also harvests credentials from more than 130 filesystem paths including `~/.aws/credentials`, `~/.config/gcloud/...`, `~/.azure/...`, `~/.kube/config`, `~/.npmrc`, SSH keys, and Docker config, affecting both CI runners and developer workstations that installed the packages. Exfiltration is performed by abusing the GitHub API to write base64-encoded loot into `antvis/G2` repository contents and via a fallback C2 endpoint at `t.m-kosche.com/v1/traces`, with the campaign further distinguished by persistence into VS Code and Claude Code configuration, making any host that installed an affected package effectively fully compromised.

[Read original article](https://trustedsec.com/blog/shai-hulud-is-back){: .btn .btn-primary }
