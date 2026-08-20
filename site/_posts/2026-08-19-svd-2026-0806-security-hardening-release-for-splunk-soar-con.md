---
layout: post
title: "SVD-2026-0806: Security Hardening Release for Splunk SOAR Connectors - August 2026"
date: 2026-08-19 00:00:00 +0300
categories: [RSS]
tags: [advisory, cve, information-disclosure, permission-bypass, soar]
toc: true
---

Splunk released a security hardening advisory addressing 16 CVEs across 14 SOAR connectors, with CVSS scores ranging from 2.7 to 6.6. Key vulnerabilities include incorrect permission assignment allowing unauthorized file list modifications in FireAMP and Nmap Scanner (CVE-2026-76371/72), LDAP filter injection in the AD LDAP connector enabling parameter manipulation (CVE-2026-76373), and widespread information disclosure through sensitive data logging and action parameter exposure across AWS IAM, Azure AD Graph, Cisco, CrowdStrike, MS Graph, Phantom, RSA SecurID, Splunk Attack Analyzer, Venafi, and Zoom connectors (CVE-2026-76374-86). All affected connectors require immediate upgrade to patched versions listed in the advisory.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-0806){: .btn .btn-primary }
