---
layout: post
title: "Trusted by Default: Qubole Cross-Account Access Abused in the Wild"
date: 2026-11-09 14:56:32 +0300
categories: [RSS]
tags: [cloud, iam, cross-account, supply-chain, threat-intel]
toc: true
---

Wiz Research reports active exploitation of Qubole's cross-account AWS access feature, where misconfigured trust relationships between customer and Qubole accounts are abused by threat actors to laterally move into customer cloud environments. The vulnerability stems from overly permissive default cross-account IAM roles that grant broad access without proper boundary policies. Attackers leverage compromised Qubole credentials or platform vulnerabilities to assume customer roles, enabling data exfiltration and infrastructure compromise. This represents a critical supply-chain attack vector affecting all Qubole customers relying on the platform's multi-account architecture.

[Read original article](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild){: .btn .btn-primary }
