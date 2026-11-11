---
layout: post
title: "Where to run AWS workloads and how to limit their access"
date: 2026-11-11 00:00:00 +0300
categories: [RSS]
tags: [cloud, aws, iam, access-control, architecture]
toc: true
---

Running EC2 instances in AWS management accounts is increasingly common (14% of organizations in 2026, up from 9% in 2025) but creates significant security risks: Service Control Policies (SCPs) and Resource Control Policies (RCPs) that restrict access in member accounts don't apply to the management account itself, and a compromised workload there can leverage OrganizationAccountAccessRole or sts:AssumeRoot to gain administrative access across the organization. The article provides a detailed multi-account strategy recommending separate member accounts for workloads, CI/CD pipelines, security tooling, and log archives, with guidance on using delegated administration and applying granular IAM policies to limit cross-account role assumptions to only necessary pipeline identities.

[Read original article](https://www.datadoghq.com/blog/aws-account-management/){: .btn .btn-primary }
