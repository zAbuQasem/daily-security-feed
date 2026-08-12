---
layout: post
title: "Understanding unfixed Kubernetes CVEs: What you can and can’t detect"
date: 2026-08-10 00:00:00 +0300
categories: [RSS]
tags: [kubernetes, detection, cve, cloud, audit-logs]
toc: true
---

An operational guide to four unfixed Kubernetes CVEs (CVE-2020-8554, CVE-2021-25740, CVE-2020-8561, CVE-2020-8562) that remain in the codebase because fixing them would break existing functionality. The article provides a matrix of exposure conditions (untrusted permissions, cluster features, network access) and preventive controls for each CVE, then demonstrates how to build Kubernetes audit log detection rules to confirm exploitation attempts. For example, CVE-2020-8554 enables MITM via spec.externalIPs or status.loadBalancer.ingress.ip manipulation; CVE-2021-25740 allows endpoint hijacking across namespaces; CVE-2020-8561 permits webhook response control to exfiltrate logs; CVE-2020-8562 exploits DNS rebinding against service endpoints. Emphasizes that vulnerability scanners alone are insufficient—defenders must validate exposure conditions, audit RBAC permissions, and monitor specific API activity patterns to determine actual risk in multi-tenant clusters.

[Read original article](https://www.datadoghq.com/blog/how-to-manage-unfixed-kubernetes-cves/){: .btn .btn-primary }
