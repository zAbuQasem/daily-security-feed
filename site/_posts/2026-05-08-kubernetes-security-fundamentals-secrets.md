---
layout: post
title: "Kubernetes security fundamentals: Secrets"
date: 2026-05-08 00:00:00 +0300
categories: [RSS]
tags: [kubernetes, secrets, etcd, rbac, containers]
toc: true
---

This article breaks down Kubernetes secret handling as a set of concrete threat models: secrets at rest in etcd and on worker nodes, secrets in transit between components, and API-level attacks against Kubernetes or etcd to extract them. It explains how native `Secret` objects are stored in etcd, why their values are only base64-encoded rather than encrypted, and why mounting secrets as files is safer than exposing them as environment variables that may be captured in debugging output. The piece also contrasts `Secret` objects with `ConfigMap`, noting that RBAC roles often allow `configmaps` access but not `secrets`, and uses the 2023 RKE ConfigMap exposure CVE as a case study in why that distinction matters. On the hardening side, it covers the tradeoffs of enabling etcd encryption at rest, the limited benefit when the API server and etcd share a node, and node-level risks such as privileged access or arbitrary `hostPath` mounts exposing other pods' secret volumes.

[Read original article](https://securitylabs.datadoghq.com/articles/kubernetes-security-fundamentals-part-8/){: .btn .btn-primary }
