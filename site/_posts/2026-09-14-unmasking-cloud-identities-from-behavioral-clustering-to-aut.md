---
layout: post
title: "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection"
date: 2026-09-14 10:00:01 +0300
categories: [RSS]
tags: [cloud, detection, identity, behavioral-analysis, ml]
toc: true
---

Palo Alto Unit 42 presents a behavioral clustering methodology using unsupervised ML (UMAP and HDBSCAN) to map cloud identities to functional roles by analyzing AWS CloudTrail audit logs from 40,000+ identities across 125 environments. The research addresses the critical detection gap between what an identity is permitted to do (IAM policies) versus what it actually does (observed API behavior), enabling defenders to detect masquerading attacks where adversaries exploit over-privileged identities or use benign labels to hide malicious activity. The approach identifies distinct clusters for administrators, backup services, security tools, and DevOps roles; the authors show how lightweight heuristics extracted from the clustering model can be implemented in standard SQL for continuous operational visibility without resource-intensive ML pipelines. Applicable beyond AWS to other cloud providers, SaaS, and Kubernetes environments.

[Read original article](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/){: .btn .btn-primary }
