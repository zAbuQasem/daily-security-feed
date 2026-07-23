---
layout: post
title: "Unbiased Java CPU profiling with JFR in JDK 25"
date: 2026-07-22 00:00:00 +0300
categories: [RSS]
tags: [jvm, profiling, performance, tooling, devops]
toc: true
---

JDK 25 introduces CPUTimeSample, a new first-class JFR event addressing limitations in the existing ExecutionSample mechanism for CPU profiling. ExecutionSample samples threads as observed by the JVM rather than strictly by CPU time, causing inaccurate results in CPU-saturated and reactive workloads where hotspots are underreported. The new event, developed with SAP, Amazon, and the OpenJDK community, provides accurate CPU-time sampling via cooperative stack walking without relying on unsupported JVM internals like AsyncGetCallTrace or vmstructs walking, stabilizing production profiling across scales and application patterns.

[Read original article](https://www.datadoghq.com/blog/engineering/jfr-cpu-time-profiling/){: .btn .btn-primary }
