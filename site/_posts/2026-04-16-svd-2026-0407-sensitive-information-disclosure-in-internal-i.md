---
layout: post
title: "SVD-2026-0407: Sensitive Information Disclosure in ''_internal'' index in Splunk MCP Server app"
date: 2026-04-16 03:12:32 +0300
categories: [RSS]
tags: [splunk, token-leak, logging, session-tokens, cve]
toc: true
---

CVE-2026-20205 affects Splunk MCP Server app versions before 1.0.3 and stems from CWE-532-style logging of sensitive data, exposing user session tokens and authorization tokens in clear text. An attacker needs either local access to the log files, access to the Splunk `_internal` index, or the high-privilege `mcp_tool_admin` capability to retrieve the leaked credentials. The issue is effectively a credential disclosure bug in Splunk's internal logging/telemetry path rather than a remote unauthenticated flaw, but stolen tokens could enable session hijacking or misuse of authenticated MCP access. Splunk's fix is to upgrade to 1.0.3+ and restrict `_internal` index visibility and related administrative capabilities to administrator-level roles only.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0407){: .btn .btn-primary }
