---
layout: post
title: "Pathfinding Labs: Deploy, test, and learn from 100+ intentionally vulnerable AWS environments"
date: 2026-05-18 00:00:00 +0300
categories: [RSS]
tags: [aws, cloud, iam, privilege-escalation, terraform]
toc: true
---

Datadog Security Labs introduced Pathfinding Labs, a collection of more than 100 intentionally vulnerable AWS environments designed to reproduce IAM privilege-escalation paths, CSPM misconfigurations, and multi-step toxic combinations in a deployable sandbox. Each lab is implemented in Terraform and wrapped by the `plabs` Go CLI, which can enable a lab, deploy it with `plabs apply`, and run a `demo_attack.sh` script that automates exploitation to validate the attack path end to end. The project extends beyond simple one-hop role abuse to cover multi-hop chains, cross-account escalation, and cases like Lambda function URLs paired with overly privileged roles, making it useful for exercising graph-based cloud attack paths rather than isolated misconfigurations. Practically, it gives red teams, defenders, and tooling vendors a reproducible way to test whether CSPM and cloud detection products can identify exploitable AWS relationships before an attacker walks the same path.

[Read original article](https://securitylabs.datadoghq.com/articles/introducing-pathfinding-labs/){: .btn .btn-primary }
