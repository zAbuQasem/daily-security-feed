---
layout: post
title: "Bypassing Conditional Access policies that have a resource exclusion"
date: 2026-06-22 14:00:57 +0300
categories: [RSS]
tags: [cloud, azure, iam, authentication, bypass]
toc: true
---

Microsoft Entra's Conditional Access policies that target 'all resources' with exclusions for specific apps contain an undocumented enforcement gap allowing token requests to bypass policy controls. When an excluded app requests limited-scope tokens for Microsoft Graph (e.g., User.Read), the policy engine treats these low-privileged scopes as exempt from the Conditional Access check, allowing any app to obtain these tokens regardless of policy. The bypass exploits the distinction between the OAuth2 client (the signing-in app) and resource (the API being accessed) — the exclusion only protects the specific excluded app, not the Microsoft Graph resource it subsequently requests tokens for. While Microsoft acknowledged the issue and is rolling out a fix that changes this legacy behavior by default, current tenants with such policies remain vulnerable until they opt-in to the new enforcement model.

[Read original article](https://dirkjanm.io/bypassing-conditional-access-with-resource-exclusion/){: .btn .btn-primary }
