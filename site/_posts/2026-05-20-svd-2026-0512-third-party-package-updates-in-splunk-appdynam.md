---
layout: post
title: "SVD-2026-0512: Third-Party Package Updates in Splunk AppDynamics Private Synthetic Agent (PSA) - May 2026"
date: 2026-05-20 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, dependency-management, splunk, appdynamics, advisory]
toc: true
---

Splunk's advisory for AppDynamics Private Synthetic Agent 26.4.0 is a bundled dependency remediation notice rather than a root-cause write-up: the release updates or removes a large set of embedded components, including Alpine 3.23.4, axios 1.15.0, Chromium 147.0.7727.101, cryptography 46.0.7, Node.js 24.14.1, Spring Security 6.5.9, Spring Framework 6.2.17, Jetty 12.0.33, Netty 4.1.132.Final, OpenJDK 17.0.18u8, and OpenSSL point releases. The PSA appliance was affected below 26.4.0, and the fix is a full product upgrade rather than individual patching of libraries such as tar, mio, rustls, bytes, and ring, several of which were removed entirely to address specific CVEs. Practically, this matters because PSA appears to ship a broad runtime stack spanning browser automation, Java services, Python packages, and OS libraries, so a single version lag can expose the agent to a large cluster of upstream vulnerabilities at once. The advisory is useful for asset owners tracking third-party risk in Splunk AppDynamics deployments, but it does not provide exploit details, affected code paths, or technical analysis of any individual CVE.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0512){: .btn .btn-primary }
