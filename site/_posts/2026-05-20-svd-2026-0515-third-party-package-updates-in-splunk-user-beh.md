---
layout: post
title: "SVD-2026-0515: Third-Party Package Updates in Splunk User Behavior Analytics - May 2026"
date: 2026-05-20 00:00:00 +0300
categories: [RSS]
tags: [splunk, uba, dependency-updates, cve, supply-chain]
toc: true
---

Splunk's May 2026 UBA advisory is a dependency remediation bulletin rather than a root-cause write-up, documenting security fixes delivered by upgrading or removing dozens of bundled third-party components. The changes include major version bumps for Apache Spark (3.5.5 to 3.5.6), jackson-databind (2.13.5 to 2.16.2), Hive (3.1.3 to 4.0.1), Redis (7.0.15 to 7.2.11), Kubernetes (1.31.3 to 1.31.11), Docker/containerd components, OpenJDK, Node.js, Python, and multiple Python and Java libraries. Splunk also notes explicit package removals or patches such as removing jackson-mapper and patching netty and underscore.js, with the advisory mapping these updates to a large set of CVEs ranging from deserialization issues to HTTP/2, crypto, and container-runtime related flaws. There is little exploit or root-cause detail, but the advisory is operationally useful for defenders tracking the transitive attack surface of Splunk UBA deployments and assessing whether bundled vulnerable components have been remediated.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0515){: .btn .btn-primary }
