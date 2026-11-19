---
layout: post
title: "SonarQube container scanning is now generally available"
date: 2026-11-19 14:00:00 +0300
categories: [RSS]
tags: [container-security, vulnerability-scanning, supply-chain, tooling]
toc: true
---

SonarQube Advanced Security now offers container image scanning in general availability, detecting known vulnerabilities in runtime layers (OS packages, JDKs, etc.) that escape traditional code and dependency analysis. The article uses Java4Shell (CVE-2026-114938)—a heap overflow in OpenJDK's Base64 decoder on x86-64 AVX-512 systems—as a motivating example, showing how vulnerabilities in containerized runtimes can bypass code and dependency scans and reach production. The scanner matches images against distribution advisories (Debian, Ubuntu, Alpine, Red Hat), integrates into SonarQube Cloud workflows, and can fail CI builds when vulnerabilities exceed a configured severity threshold. Practical guidance includes scanning images locally or in CI, triaging findings alongside code issues, and rebuilding on patched base images.

[Read original article](https://www.sonarsource.com/blog/sonarqube-container-scanning-is-now-available/){: .btn .btn-primary }
