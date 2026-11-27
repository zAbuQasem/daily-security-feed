---
layout: post
title: "Hack fixing the lack of Kubernetes certificate revocation"
date: 2026-11-27 07:00:00 +0300
categories: [RSS]
tags: [kubernetes, certificate-auth, access-control, rbac]
toc: true
---

Kubernetes lacks native certificate revocation support despite its long-standing known issue (since 2015). This write-up presents a practical proof-of-concept workaround leveraging Kubernetes v1.32's new credential ID feature—a SHA-256 hash of the certificate attached by the API server—to enable certificate-level revocation. The certrevoker tool tracks issued certificates by watching CSR objects and stores them as IssuedCertificate resources, then intercepts authorization decisions via a webhook that explicitly denies revoked credentials before RBAC evaluation. The approach includes a web portal for administrative revocation management and audit logging through Kubernetes API server logs. Key limitations: system:masters group certificates are exempt (since they bypass authorizers), and the system fails open by design to prevent breaking critical components if the revocation service becomes unavailable.

[Read original article](https://raesene.github.io/blog/2026/11/27/hack-fixing-k8s-lack-of-cert-revocation/){: .btn .btn-primary }
