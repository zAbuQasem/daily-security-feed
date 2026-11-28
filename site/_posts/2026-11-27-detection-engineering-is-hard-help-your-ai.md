---
layout: post
title: "Detection engineering is hard, help your AI"
date: 2026-11-27 00:00:00 +0300
categories: [RSS]
tags: [detection-engineering, defender-xdr, kql, blue-team, tooling]
toc: true
---

AI-generated Kusto Query Language (KQL) detections often fail silently by hallucinating ActionTypes, missing XML/JSON structure details in nested columns like RawEventData, and creating syntactically valid queries that never detect threats. The author introduces xdrinternals.com and an associated PowerShell module that document Microsoft Defender XDR table schemas, column definitions, structured data examples (JSON/XML), and cross-table relationships (e.g., linking SigninLogs to CloudAppEvents via UniqueTokenIdentifier). The platform includes a schema explorer with extended field documentation, a relationship map showing how to correlate events across tables, an MCP Server for AI integration, and a KQL validator (using Microsoft.Azure.Kusto.Language) that checks query syntax against documented internals without executing against live instances.

[Read original article](https://cloudbrothers.info/detection-engineering-is-hard-help-your-ai/){: .btn .btn-primary }
