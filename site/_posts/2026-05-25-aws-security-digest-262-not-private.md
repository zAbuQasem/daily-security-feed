---
layout: post
title: "AWS Security Digest #262 - Not private"
date: 2026-05-25 12:00:00 +0300
categories: [RSS]
tags: [supply-chain, aws, cloud, kubernetes, npm]
toc: true
---

The TeamPCP npm supply chain campaign (wave 5 in the post-Shai-Hulud series) hit Alibaba's @antv data visualization suite via 323 malicious packages with ~16M weekly weekly downloads; payloads grep for AWS access keys, scrape IMDS/ECS metadata/Secrets Manager, and establish persistence via trojanized GitHub Actions workflows and a malicious VSCode extension. A CISA contractor leaked high-privilege AWS GovCloud credentials in a public GitHub repo named 'Private-CISA' for six months until an external scanner caught them on May 15 — still live 48 hours post-notification. CVE-2021-25740 is a structural, unpatchable Kubernetes flaw where any user with the default `edit` role can rewrite Endpoints/EndpointSlice objects to reroute another tenant's traffic to attacker-controlled pods; in shared EKS clusters using AWS Load Balancer Controller this is live with no upstream fix, only mitigations (Gateway API migration, stripping routing-write from edit role). Also noted: an AWS API Gateway auth bypass via trailing slash earned a $12K bounty.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-262){: .btn .btn-primary }
