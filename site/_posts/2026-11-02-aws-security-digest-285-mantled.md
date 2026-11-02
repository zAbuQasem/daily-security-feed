---
layout: post
title: "AWS Security Digest #285 - Mantled"
date: 2026-11-02 13:00:00 +0300
categories: [RSS]
tags: [rce, supply-chain, cloud, malware, ci-cd]
toc: true
---

CVE-2026-111497 is a critical RCE vulnerability in Google's Brotli decoder affecting Node.js, Python, Bun, .NET, Java, Envoy, and Istio—widely-deployed infrastructure components already under active exploitation. AWS Lambda base runtimes, CodeBuild curated images, App Runner's Node.js, and Elastic Beanstalk are patched. The article also documents 'Black October': nine AI developer platforms (Fireworks AI, Zeabur, Lightning AI, OpenCode, Railway, Warp, CommandCode, Northflank, Andromeda) disclosed breaches in October with leaked enterprise keys leading to ~2.5M fraudulent Bedrock API calls totaling over $100k at retail pricing. Includes technical resources on detection and a malicious Claude Code extension that briefly compromised the Cursor marketplace.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-285){: .btn .btn-primary }
