---
layout: post
title: "Detect runtime threats in Python Lambda functions with Datadog AAP"
date: 2026-04-15 03:12:31 +0300
categories: [RSS]
tags: [aws-lambda, python, rasp, detection, serverless]
toc: true
---

Datadog describes extending its App and API Protection engine into Python AWS Lambda runtimes by embedding detection in the application process through its tracing library instead of relying only on the external Lambda Extension/WAF model. The main technical change is in-process visibility over request context, function calls, and execution paths, which lets the product correlate untrusted input with vulnerable sinks and flag successful exploitation conditions rather than just suspicious request patterns. The post says this runtime instrumentation can detect SSRF, shell injection, SQL injection, and local file inclusion, and attach stack traces showing the affected code path for triage. It also covers account-takeover detection in serverless apps by emitting application-level auth events such as `user.login` and `session.create`, then analyzing cross-invocation patterns like repeated failures, high login velocity, and multi-IP credential stuffing.

[Read original article](https://www.datadoghq.com/blog/app-api-protection-python-lambda-monitoring/){: .btn .btn-primary }
