---
layout: post
title: "Password spraying campaign targets AWS root user accounts across 150+ organizations"
date: 2026-08-31 00:00:00 +0300
categories: [RSS]
tags: [threat-intelligence, cloud, aws, iam, brute-force]
toc: true
---

Datadog Security Research identified an active password spraying campaign targeting AWS root user accounts across 150+ organizations from July 24 to August 23, 2026. Attackers used two browser user agents (Chrome/Edge and Firefox 120.0) tunneled through residential proxies and hosting infrastructure to make repeated failed ConsoleLogin authentication attempts, with organizations typically seeing 2–8 attempts each. The fact that ConsoleLogin failures require knowledge of root user email addresses suggests attackers either possess a leaked email list or are enumerating valid AWS account emails. No successful authentication was observed, but the report provides specific CloudTrail detection queries (filtering by user agent and ConsoleLogin failures) and remediation guidance including MFA enforcement, SCPs to restrict root activity, and centralized root access management via AWS Organizations.

[Read original article](https://securitylabs.datadoghq.com/articles/aws-root-user-bruteforce-campaign/){: .btn .btn-primary }
