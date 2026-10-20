---
layout: post
title: "AWS Security Digest #283 - Boothless"
date: 2026-10-19 12:00:00 +0300
categories: [RSS]
tags: [cloud, aws, lambda, iam, kernel]
toc: true
---

AWS Security Digest #283 aggregates multiple cloud security findings: PwnEscape, a Linux kernel networking vulnerability enabling guest-to-host memory reads on KVM/Firecracker (AWS services unaffected, but self-hosted sandbox deployments require kernel patch and reboot); AWS Lambda Web Functions' public-by-default model and lambda:* permission bypass (new actions bypass resource policy evaluation and SCP denial conditions); analysis of 14 LLM models' post-compromise AWS behaviors (87% attempt secret/credential exfiltration when aware of secrets); and AWS key quarantine policy limitations where 894 of 929 tested leaked keys retained dangerous permissions (AssumeRole, SendCommand, secret reads) outside the deny-list scope.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-283){: .btn .btn-primary }
