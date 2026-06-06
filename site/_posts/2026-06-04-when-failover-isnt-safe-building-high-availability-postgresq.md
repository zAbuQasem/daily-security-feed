---
layout: post
title: "When failover isn’t safe: Building high-availability PostgreSQL on Kubernetes"
date: 2026-06-04 00:00:00 +0300
categories: [RSS]
tags: [kubernetes, database, failover, infrastructure]
toc: true
---

Datadog describes how a simulated zonal failure with elevated network latency exposed a critical weakness in their PostgreSQL-on-Kubernetes architecture: asynchronous replication caused replicas to lag beyond safe promotion thresholds, making failover impossible without risking data loss. They rearchitected their clusters to use synchronous replication for failover candidates, coordinated by Patroni and ZooKeeper, ensuring that only replicas within an acceptable LSN distance can be promoted. The article explains how Patroni safely elects new leaders during network partitions, the trade-offs between availability and durability, and validation through benchmarking—practical guidance for operators managing stateful workloads on Kubernetes.

[Read original article](https://www.datadoghq.com/blog/engineering/postgresql-ha-kubernetes/){: .btn .btn-primary }
