---
layout: post
title: "Introducing Burp AT: agentic AI, built on two decades of Burp Suite"
date: 2026-07-27 12:51:51 +0300
categories: [RSS]
tags: [tool, pentesting, ai-agent, automation]
toc: true
---

PortSwigger has released Burp AT, an agentic AI tool integrated into Burp Suite Professional that automates pentesting tasks while maintaining human control. The architecture enforces security boundaries: agents operate through Burp's battle-tested tools and can access project context (traffic, scope, issues), but execute only actions that Burp's scope and approval rules permit—agents propose, Burp enforces. Skills are purpose-built from PortSwigger Research methodology rather than general LLM knowledge. In closed beta, a pentester used it to analyze 66,000 lines of minified JavaScript in four days and surfaced a critical vulnerability that would have gone untested for at least a year. The approach prioritizes auditability and reproducibility: all requests and evidence flow through Burp's tooling so findings can be independently verified.

[Read original article](https://portswigger.net/blog/introducing-burp-at){: .btn .btn-primary }
