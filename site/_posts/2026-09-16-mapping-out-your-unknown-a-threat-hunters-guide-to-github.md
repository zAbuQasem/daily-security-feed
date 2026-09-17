---
layout: post
title: "Mapping out your unknown: A threat hunter’s guide to GitHub"
date: 2026-09-16 00:00:00 +0300
categories: [RSS]
tags: [threat-hunting, github, detection, credential-theft, ci-cd]
toc: true
---

Datadog Security Research presents a practical threat-hunting guide for detecting compromised GitHub accounts and tokens in audit logs. The article outlines the attacker progression (initial access via stolen tokens/OAuth phishing → discovery of private repos → credential exfiltration and CI/CD pivoting) and documents key logging quirks in GitHub audit logs that complicate attribution (missing external identity in API requests, inconsistent repository visibility fields). The guide provides concrete detection queries for each stage: monitoring sign-ins from new geos and devices (T1078), tracking unauthorized OAuth app authorizations (T1528), and detecting enumeration of secrets and private repositories. Effective hunting depends on establishing baselines of normal activity (token usage from expected ASNs, API request patterns) and correlating GitHub audit logs with SIEM and identity provider logs to fill gaps where GitHub omits source IP or geolocation data.

[Read original article](https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-github/){: .btn .btn-primary }
