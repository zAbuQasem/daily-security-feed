---
layout: post
title: "Understanding Current Threats to Kubernetes Environments"
date: 2026-04-07 00:00:00 +0300
categories: [Research]
tags: [kubernetes, cloud, token-theft, lateral-movement, apt]
toc: true
---

Unit 42 presents two real-world Kubernetes attack case studies showing a 282% year-over-year rise in Kubernetes-targeted threat operations. In the first case, North Korean APT Slow Pisces (Lazarus/TraderTraitor) compromised a cryptocurrency exchange by stealing Kubernetes service account tokens mounted in pods, then used those tokens against the Kubernetes API to pivot laterally into core financial backend systems — the same identity-scraping tradecraft seen in the $1.5B Bybit ETH heist. The second case covers CVE-2025-55182 (React2Shell), a critical RCE vulnerability exploited in the wild within two days of public disclosure to execute commands inside Kubernetes workloads, install backdoors, and exfiltrate cloud credential files and database passwords. The common attack chain is: exploit public-facing app or misconfiguration → RCE in container → extract mounted service account token → abuse overprivileged RBAC to escalate cluster-wide or into cloud control plane. The article includes MITRE ATT&CK mappings and detection/hardening guidance.

---

[Read original article](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/)
