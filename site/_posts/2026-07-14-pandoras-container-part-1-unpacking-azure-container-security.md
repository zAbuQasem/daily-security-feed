---
layout: post
title: "Pandora’s Container Part 1: Unpacking Azure Container Security"
date: 2026-07-14 04:00:00 +0300
categories: [RSS]
tags: [azure, container, imds, supply-chain]
toc: true
---

Azure Container Registry compromise via RBAC abuse enables attackers to pull proprietary images, push backdoored containers, and overwrite tags to hijack deployments. The article introduces a novel technique embedding IMDS metadata service token theft and secret exfiltration directly into Dockerfile entrypoints, eliminating the need for persistent reverse shells. Exploitation requires specific Azure RBAC permissions (registries/write, listCredentials/action, push/write, tasks/write, etc.) granted by default in Owner, Contributor, and container-specific built-in roles. The attack chain demonstrates container registry enumeration, admin credential extraction, image manipulation, and automated token exfiltration. This represents a critical supply-chain attack vector in Azure containerized environments with broad applicability across enterprise organizations.

[Read original article](https://trustedsec.com/blog/pandoras-container-part-1-unpacking-azure-container-security){: .btn .btn-primary }
