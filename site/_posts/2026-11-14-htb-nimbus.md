---
layout: post
title: "HTB: Nimbus"
date: 2026-11-14 14:45:00 +0300
categories: [RSS]
tags: [ssrf, cloud, rce, privilege-escalation, container]
toc: true
---

A multi-stage exploitation chain begins with SSRF in a job-scheduler application; decimal IP encoding bypasses filtering to reach the AWS metadata service and steal EC2 credentials. These credentials enable access to an SQS queue where unsafe PyYAML deserialization achieves container RCE. From the container, discovered AWS credentials interact directly with a Floci AWS emulator through CodeBuild project creation, with bash exported functions in environment variables maintaining access to a privileged container. A kernel modprobe privilege escalation exploit completes the chain with root access on the host, demonstrating integrated SSRF, credential exfiltration, deserialization, and kernel PE techniques.

[Read original article](https://0xdf.gitlab.io/2026/11/14/htb-nimbus.html){: .btn .btn-primary }
