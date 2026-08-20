---
layout: post
title: "SVD-2026-0808: Security Hardening Release for Splunk Apps and Add-ons - August 2026"
date: 2026-08-19 00:00:00 +0300
categories: [RSS]
tags: [rce, ssrf, access-control, splunk, privilege-escalation]
toc: true
---

Splunk released a security hardening advisory addressing 15 CVEs across multiple apps and add-ons. The most critical is CVE-2026-76404 (CVSS 9.1), a Remote Code Execution vulnerability in Splunk MCP Server via unsafe deserialization of untrusted data in the model loading REST API. Additional high-severity issues include SSRF vulnerabilities that can leak Splunk management tokens (CVE-2026-76389, CVE-2026-76402), multiple authorization bypass vulnerabilities in the AI Toolkit REST API allowing privilege escalation and data access (CVE-2026-76391, CVE-2026-76394, CVE-2026-76397, CVE-2026-76399), and hardcoded credentials in container connections (CVE-2026-76392). Affected products include Cisco Talos Intelligence, Splunk AI Toolkit, Splunk Connect for Kafka, and Splunk On-Call; patched versions are available for all affected components.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-0808){: .btn .btn-primary }
