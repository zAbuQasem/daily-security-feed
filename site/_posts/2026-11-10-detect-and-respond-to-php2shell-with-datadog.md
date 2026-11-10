---
layout: post
title: "Detect and respond to PHP2Shell with Datadog"
date: 2026-11-10 00:00:00 +0300
categories: [RSS]
tags: [rce, php, detection, vulnerability-management, cve]
toc: true
---

PHP2Shell comprises two critical RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619) in the PHP interpreter with CVSS 9.2 scores, exploitable without authentication before PHP executes application code. The attack exploits PHP's request shutdown procedure in mod_php deployments, bypassing application-level authentication and input validation entirely. The post provides operational guidance for identifying affected PHP hosts and container images, prioritizing remediation based on exposure factors (public accessibility, production status), and detecting exploitation through runtime infrastructure and security event correlation. AWS observed exploitation in the wild on October 17, 2026, prior to patch availability, making detection and rapid remediation critical.

[Read original article](https://www.datadoghq.com/blog/detect-respond-php2shell-datadog/){: .btn .btn-primary }
