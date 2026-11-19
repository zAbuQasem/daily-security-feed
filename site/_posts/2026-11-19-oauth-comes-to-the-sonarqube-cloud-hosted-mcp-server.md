---
layout: post
title: "OAuth comes to the SonarQube Cloud-hosted MCP server"
date: 2026-11-19 14:00:00 +0300
categories: [RSS]
tags: [oauth, mcp, authentication, credential-management, devops]
toc: true
---

SonarQube MCP Server v1.30.0 introduces OAuth 2.1 authentication for SonarQube Cloud-hosted MCP endpoints, eliminating personal access tokens. The implementation uses PKCE and Client ID Metadata Documents (CIMD) for client verification, enforces scoped access (mcp:tools:read vs mcp:tools:write) via RFC 8707 resource binding, and performs per-call token exchange to apply the signed-in user's SonarQube permissions. Configuration simplifies to a single URL with no headers; multi-organization support via the new list_organizations tool enables platform teams to centrally roll out AI coding agent integration without credentials sprawl across developer machines.

[Read original article](https://www.sonarsource.com/blog/oauth-comes-to-the-sonarqube-cloud-mcp-server/){: .btn .btn-primary }
