---
layout: post
title: "AWS Security Digest #259 - Better late"
date: 2026-05-04 12:00:00 +0300
categories: [RSS]
tags: [aws, cloud, cognito, iam, detection]
toc: true
---

This AWS Security Digest issue is a curated roundup of several technically useful cloud-security findings rather than a pure product announcement. The most actionable item is AWS's March 2026 Threat Technique Catalog update, which highlights Cognito refresh-token abuse: an attacker who steals a refresh token can repeatedly call `cognito-idp:GetTokensFromRefreshToken` to mint new access and ID tokens, potentially for up to 30 days by default or longer if administrators increase token lifetime and do not enable rotation. It also summarizes research showing unexpected AWS networking behavior where VPC peering traffic can still succeed when the source subnet routes the peer CIDR to a NAT gateway, because NAT connection tracking and route caching can override the intuitive expectation that explicit return peering routes are required. Additional coverage includes TrailTool, which pre-aggregates CloudTrail into entities such as people, sessions, roles, and resources to support AI-assisted investigation and least-privilege policy generation, plus commentary on the recurrent risk of third-party PaaS breaches exposing long-lived AWS credentials and the value of short-lived OIDC-based integrations.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-259){: .btn .btn-primary }
