---
layout: post
title: "Using the API server proxy to bypass network policies"
date: 2026-08-21 09:00:00 +0300
categories: [RSS]
tags: [kubernetes, cloud, network-policy, ssrf, multi-tenant]
toc: true
---

A Kubernetes attacker with pod status mutation permissions can bypass network policies in multi-tenant clusters by overwriting their pod's IP address to match a target pod in a restricted namespace, then proxying through the API server (which has unrestricted network access) to reach the target workload. The technique exploits a fundamental Kubernetes design: the API server is exempted from network policies for cluster management, and any user-owned pod can be proxied through it regardless of network policy restrictions on the pod's actual network interface. This breaks the multi-tenancy assumption that network policies isolate tenant workloads, affecting any cluster where RBAC grants pod status mutation and the API server maintains a permissive network position.

[Read original article](https://raesene.github.io/blog/2026/08/21/api-server-proxy-netpol-bypass/){: .btn .btn-primary }
