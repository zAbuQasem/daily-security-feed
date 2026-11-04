---
layout: post
title: "Pulling the right strings for RCE on a Puppet"
date: 2026-11-03 00:00:00 +0300
categories: [RSS]
tags: [rce, puppet, deserialization, supply-chain, cve]
toc: true
---

Critical RCE vulnerabilities in Puppet configuration management were discovered through unsafe deserialization in the agent event reporting endpoint (`/puppet/v3/report/{agent_name}`). The vulnerability exploits Puppet's `FromDataConverter.convert()` method, which processes attacker-controlled JSON and passes user input to Ruby's `class_eval()` via `RubyGenerator.create_class()`. By crafting a JSON payload with a malicious `__ptype` field containing a `RubyMethod` annotation with arbitrary Ruby code in the `body` field, an attacker with a valid agent certificate can execute system commands at class evaluation time using backticks. CVE-2026-115731 and related vulnerabilities affect Puppet Enterprise and open-source versions dating back to 6.24.0 (July 2021), allowing complete compromise of the Puppet management server infrastructure.

[Read original article](https://neodyme.io/en/blog/puppet_rce/){: .btn .btn-primary }
