---
layout: post
title: "Investigate Kubernetes health and processes with the Datadog MCP Server"
date: 2026-11-09 00:00:00 +0300
categories: [RSS]
tags: [kubernetes, infrastructure, cloud, devops]
toc: true
---

Datadog's expanded MCP Server now includes four Kubernetes control plane health tools that aggregate API server, scheduler, controller manager, and etcd metrics (error rates, scheduling latency, work queue depth, leader availability, failed writes) in single queries. A new `search_datadog_live_processes` tool queries process observations by executable, command line, or metadata tags over the past 36 hours to detect restarts and configuration changes. These tools enable AI agents to investigate infrastructure issues—pods stuck in Pending, slow API responses, process instability—by correlating process-level and control plane telemetry without requiring manual metric construction. The tools operate on Datadog's existing telemetry and follow user RBAC permissions.

[Read original article](https://www.datadoghq.com/blog/kubernetes-processes-datadog-mcp-server/){: .btn .btn-primary }
