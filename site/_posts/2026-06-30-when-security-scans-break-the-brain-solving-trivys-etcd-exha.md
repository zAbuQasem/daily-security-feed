---
layout: post
title: "When Security Scans Break the Brain: Solving Trivy’s etcd Exhaustion Problem"
date: 2026-06-30 22:37:11 +0300
categories: [RSS]
tags: [kubernetes, etcd, infrastructure, devops]
toc: true
---

The Trivy Operator, a Kubernetes security standard, can inadvertently exhaust etcd storage and force clusters into read-only mode when vulnerability reports are stored as CRDs. Each update creates a new MVCC revision in etcd rather than overwriting; combined with optional fields (Links, CVSS, Description), individual reports can exceed the 1.5 MiB API server hard limit, while historical revisions accumulate. Compaction marks space as reusable internally, but only defragmentation releases physical disk back to the OS, requiring explicit maintenance. Solutions include: using PVC-based alternate report storage (OPERATOR_ALTERNATE_REPORT_STORAGE_ENABLED), implementing aggressive TTL policies (OPERATOR_SCANNER_REPORT_TTL), switching to client-server scanning mode to avoid per-pod database downloads, and filtering low-severity findings. Monitoring apiserver_storage_size_bytes trending toward 80% of quota triggers the need for defragmentation.

[Read original article](https://www.aquasec.com/blog/when-security-scans-break-the-brain-solving-trivys-etcd-exhaustion-problem/){: .btn .btn-primary }
