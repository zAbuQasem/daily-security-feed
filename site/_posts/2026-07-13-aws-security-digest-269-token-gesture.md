---
layout: post
title: "AWS Security Digest #269 - Token Gesture"
date: 2026-07-13 12:00:00 +0300
categories: [RSS]
tags: [cloud, iam, auth, privilege-escalation, aws]
toc: true
---

The AWS Security Digest curates this week's significant cloud security research: Kat Traxler dissects the confused deputy problem in cloud environments, explaining that iam:PassRole is a one-shot permission check at attach time—after which workloads pull tokens from metadata endpoints with no re-validation, creating lasting privilege escalation risk. Bala Paranj documents how AWS's new OAuth support for the MCP Server silently expanded what existing IAM policies permit—any statement granting signin:* or a bare * now authorizes minting short-lived OAuth tokens via signin:CreateOAuth2Token without policy changes, with detection guidance (Stave and CloudTrail) provided. Eduard Agavriloae demonstrates autonomous offensive agents solving all 122 Datadog Pathfinding Labs using only sts:GetCallerIdentity and iam:GetUser, revealing that non-obvious privilege escalation paths remain concentrated in SageMaker, Cognito Identity, App Runner, and Batch where public playbooks are sparse.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-269){: .btn .btn-primary }
