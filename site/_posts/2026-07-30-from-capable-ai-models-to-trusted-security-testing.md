---
layout: post
title: "From capable AI models to trusted security testing"
date: 2026-07-30 14:58:47 +0300
categories: [RSS]
tags: [ai-security, methodology, defensive, appsec]
toc: true
---

PortSwigger Research published findings on safely integrating AI agents into security testing workflows, resulting in Burp AT. The core insight is that control must sit outside the probabilistic model—scope boundaries and permissions are enforced by Burp, not by prompting; agents generate hypotheses but cannot override policy or produce unauditable actions. The product integrates agentic reasoning with 20+ years of battle-tested security tooling (authentication, protocol handling, session management), allowing models to focus on hypotheses and interpretation rather than reimplementing tooling mechanics. James Kettle's research methodology for hypothesis generation and testing is being translated into reusable, task-specific skills within the agent framework. This represents a pragmatic architectural approach to agentic security testing where human judgment remains central to scope decisions, risk assessment, and conclusion validation.

[Read original article](https://portswigger.net/blog/from-capable-ai-models-to-trusted-security-testing){: .btn .btn-primary }
