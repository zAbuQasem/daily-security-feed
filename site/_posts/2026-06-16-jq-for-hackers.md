---
layout: post
title: "JQ for Hackers"
date: 2026-06-16 04:00:00 +0300
categories: [RSS]
tags: [tooling, methodology, recon, post-exploitation]
toc: true
---

A practical guide to mastering jq for security workflows, demonstrating how to parse, filter, and extract data from JSON output of security tools. The article covers core techniques—field selection, array iteration, filtering with select(), and object construction—then illustrates real-world applications including extracting SAM account names and UPNs from ldapdomaindump output, searching TruffleHog results for secrets, and carving DNS hostnames from domain dumps. For red teamers and pentesters who frequently work with JSON-outputting tools like httpx, TruffleHog, and post-exploitation LDAP enumeration, jq eliminates the need for manual CSV parsing and enables efficient data transformation in the field.

[Read original article](https://trustedsec.com/blog/jq-for-hackers){: .btn .btn-primary }
