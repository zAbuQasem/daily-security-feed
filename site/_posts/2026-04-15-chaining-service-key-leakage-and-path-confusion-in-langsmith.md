---
layout: post
title: "Chaining service key leakage and path confusion in LangSmith (Resolved)"
date: 2026-04-15 03:12:35 +0300
categories: [RSS]
tags: [auth-bypass, path-confusion, jwt, api-security, langsmith]
toc: true
---

This write-up describes an authorization bypass in LangSmith that chained two issues: an Agent API response exposed an internal `X-Service-Key` JWT, and a path normalization mismatch let requests reach internal-only routes by encoding slashes as `%2F`. The root cause was inconsistent handling between the GCP load balancer and the FastAPI application, which allowed routing restrictions on sensitive control-plane endpoints to be bypassed even though those endpoints were meant to stay internal. With a leaked service key, the attacker could access agent deployment APIs across arbitrary workspaces and obtain read/write access to deployment data, including connected third-party service credentials. The remediation blocked encoded slashes at the WAF, removed service keys from API responses, and tightened default authorization behavior, making the post a useful case study in privilege scoping and proxy/app path parsing bugs.

[Read original article](https://lab.ctbb.show/writeups/chaining-service-key-leakage-and-path-confusion-in-langsmith){: .btn .btn-primary }
