---
layout: post
title: "Mount Here, Read There: Twin Path Traversal CVEs in Kubernetes Storage"
date: 2026-07-23 13:00:50 +0300
categories: [RSS]
tags: [kubernetes, path-traversal, cve, privilege-escalation]
toc: true
---

Two path traversal CVEs (CVE-2026-3864, CVE-2026-3865) in upstream Kubernetes CSI drivers for NFS and SMB allow attackers with PersistentVolume creation permissions to escape subdirectory isolation by injecting traversal sequences like `../../../` into the volumeHandle's subDir field. Both drivers incorrectly trusted `filepath.Join` as a security boundary; this normalization function does not prevent path escape, allowing attackers to reach other tenants' data on shared exports. Impact ranges from cross-tenant file access and modification to arbitrary node directory deletion when CSI controllers have broad hostPath mounts. Exploitation requires only a modified PersistentVolume manifest and PV creation permissions (commonly granted to CI/CD and GitOps operators despite being cluster-scoped). Fixes shipped in csi-driver-nfs v4.13.1 and csi-driver-smb v1.20.1.

[Read original article](https://www.sentinelone.com/blog/mount-here-read-there-twin-path-traversal-cves-in-kubernetes-storage/){: .btn .btn-primary }
