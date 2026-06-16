---
layout: post
title: "Claude Fable 5 built a Java module in 13 minutes"
date: 2026-06-11 16:00:00 +0300
categories: [RSS]
tags: [ai-generated-code, toctou, temporary-file, java, container-security]
toc: true
---

SonarSource ran Claude Fable 5 on a Java coding task and discovered a HIGH-severity TOCTOU (time-of-check-time-of-use) vulnerability in the AI-generated code. The model called Files.createTempDirectory() without secure options, creating a world-writable staging directory vulnerable to symlink attacks on shared hosts and containers. An attacker can exploit the race condition between directory creation and file write to redirect GC log output (which contains JVM arguments, database credentials, API keys) or pre-populate the directory with malicious content. The vulnerability (java:S5443) reveals that AI models can generate this class of insecure pattern despite defending against other attacks like path traversal, exposing gaps between training-data patterns and OS-level domain knowledge.

[Read original article](https://www.sonarsource.com/blog/claude-fable-5-built-a-java-module-in-13-minutes/){: .btn .btn-primary }
