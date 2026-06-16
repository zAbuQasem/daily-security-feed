---
layout: post
title: "Holding blobs for ransom: Four methods for Azure Storage ransomware"
date: 2026-06-15 00:00:00 +0300
categories: [RSS]
tags: [cloud, ransomware, azure, encryption, detection]
toc: true
---

Datadog Security Labs documents four distinct methods for ransomware attacks against Azure Blob Storage: client-side encryption (observed in BlackCat/Sphynx attacks), customer-provided encryption keys (CPK) via HTTP headers, encryption scopes with attacker-controlled Key Vault keys (used by STORM-0501), and service-side encryption with customer-managed keys. The research provides technical curl examples, required IAM permissions for each attack path, event codes for detection, and exploitation details for methods 1 and 3 already observed in active campaigns. Critically, Methods 2 and 4 lack robust logging, making detection difficult despite their security impact.

[Read original article](https://securitylabs.datadoghq.com/articles/azure-blob-storage-ransomware-four-methods/){: .btn .btn-primary }
