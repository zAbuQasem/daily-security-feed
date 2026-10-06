---
layout: post
title: "Guarding the gates: Assessing dangerous permissions granted to Kubernetes built-in principals"
date: 2026-10-05 00:00:00 +0300
categories: [RSS]
tags: [kubernetes, rbac, cloud, access-control, privilege-escalation]
toc: true
---

Datadog Security Labs analyzed 65,000+ Kubernetes clusters from ~10,000 organizations to characterize dangerous RBAC bindings to built-in principals (`system:anonymous`, `system:unauthenticated`, `system:authenticated`). Across 320,000+ total bindings, they identified 3,500+ that grant dangerous permissions including cluster-admin, pod creation with privilege escalation, and node access—permissions that violate least-privilege principles when granted to unauthenticated or broadly-authenticated users. The study reveals widespread RBAC misconfigurations even on major distributions (EKS, GKE, AKS), with namespace-level admins in multi-tenant clusters particularly exposed to creating cluster-wide risks through permissive bindings. Findings underscore the need for regular RBAC audits and stricter default configurations across Kubernetes deployments.

[Read original article](https://securitylabs.datadoghq.com/articles/kubernetes-rbac-built-in-principals-dangerous-permissions/){: .btn .btn-primary }
