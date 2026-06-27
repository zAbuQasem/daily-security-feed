---
layout: post
title: "MCP Auto-Execution: From Git Clone to Cloud Compromise in Amazon Q VS Code Extension"
date: 2026-06-26 12:00:01 +0300
categories: [RSS]
tags: [cloud, supply-chain, aws, auto-execution, rce]
toc: true
---

A critical vulnerability in Amazon Q VS Code Extension allows automatic execution of arbitrary code via MCP (Model Context Protocol) during git clone operations, leading to direct cloud account compromise. The vulnerability chains auto-execution with untrusted repository content to escalate from local code execution to AWS credential theft and cloud infrastructure access. This affects all users of the Amazon Q extension with default settings, making it an immediate threat to development environments integrated with AWS services. Wiz researchers demonstrated the full attack path from innocent-looking malicious git repositories to live cloud compromise.

[Read original article](https://www.wiz.io/blog/amazon-q-vulnerability){: .btn .btn-primary }
