---
layout: post
title: "IAM the Captain Now – Hijacking Azure Identity Access"
date: 2026-04-10 03:12:56 +0300
categories: [RSS]
tags: [azure, cloud, iam, privilege-escalation, rbac]
toc: true
---

TrustedSec documents three Azure IAM permissions that enable privilege escalation: `Microsoft.Authorization/roleAssignments/write` (assign any role to any principal), `Microsoft.Authorization/roleDefinitions/write` (create custom roles with arbitrary permissions), and `Microsoft.Authorization/federatedIdentityCredentials/write` (create Federated Identity Credentials to hijack managed identities via OIDC). An attacker with any of these permissions on a subscription scope can elevate to Owner or retrieve Key Vault secrets without needing broader access. The post includes a hands-on lab walkthrough using Azure CLI to demonstrate each escalation path — enumerating role assignments, assigning privileged roles, and abusing FIC to impersonate service principals. These misconfigurations are commonly encountered in real engagements and represent high-impact lateral movement / privilege escalation vectors in Azure tenant compromise scenarios.

[Read original article](https://trustedsec.com/blog/iam-the-captain-now-hijacking-azure-identity-access){: .btn .btn-primary }
