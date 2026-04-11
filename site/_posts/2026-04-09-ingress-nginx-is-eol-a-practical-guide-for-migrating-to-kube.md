---
layout: post
title: "Ingress NGINX is EOL: A practical guide for migrating to Kubernetes Gateway API"
date: 2026-04-09 03:11:38 +0300
categories: [RSS]
tags: [kubernetes, ingress, cloud, migration, hardening]
toc: true
---

Ingress NGINX reached EOL in March 2026, meaning future vulnerabilities (including cluster-wide impact bugs like IngressNightmare and CVE-2026-24512/CVE-2026-3288) will have no supported fixes. This guide covers a structured migration to Kubernetes Gateway API, which moves routing config from controller-specific annotations into portable, role-scoped API resources (GatewayClass, Gateway, HTTPRoute, ReferenceGrant). The article covers controller selection (NGINX Gateway Fabric, Istio, Envoy Gateway, cloud-managed options), how to validate installation via CRDs, and how to run the old and new controllers in parallel during transition. Relevant for teams that haven't yet migrated off Ingress NGINX and are now operating on an unpatched, unsupported ingress path.

[Read original article](https://www.datadoghq.com/blog/migrate-to-gateway-api/){: .btn .btn-primary }
