---
layout: post
title: "Surface Pro - EoP"
date: 2026-06-20 21:01:50 +0300
categories: [RSS]
tags: [eop, windows, rpc, registry, surface]
toc: true
---

Local privilege escalation in Microsoft SurfaceBroker (MSRC 107703), a SYSTEM-level service running on all Surface devices. The vulnerability combines two bugs: (1) SurfaceBroker authenticates callers by checking for AppContainer capability SIDs, but AppContainers are sandboxing primitives that any standard user can create with arbitrary capabilities—should use PackageFamilySid instead; (2) the RegistryDm microservice behind the RPC endpoint allows unrestricted HKLM writes as SYSTEM with no allowlist or scope validation, enabling writes to SYSTEM\CurrentControlSet\Services, SAM, SECURITY, and Run keys. An unelevated user can spawn a child process in a self-created AppContainer with spoofed capabilities, authenticate to SurfaceBroker, and write arbitrary registry values to escalate to SYSTEM.

[Read original article](https://thecontractor.io/ms-surface-eop-system/){: .btn .btn-primary }
