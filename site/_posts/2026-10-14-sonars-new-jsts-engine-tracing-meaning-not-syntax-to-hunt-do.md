---
layout: post
title: "Sonar's new JS/TS engine: Tracing meaning, not syntax, to hunt down real vulnerabilities"
date: 2026-10-14 13:00:00 +0300
categories: [RSS]
tags: [static-analysis, xss, data-flow-analysis, tooling]
toc: true
---

Sonar's new JavaScript/TypeScript static analysis engine uses abstract interpretation and data-flow analysis to trace tainted values through complex, real-world code patterns that syntax-based tools miss. The article demonstrates the engine discovering a reflected HTML injection in FlowiseAI's OAuth2 callback handler, where a query parameter flows through destructuring, object repackaging, cross-module imports, and template literals before reaching res.send()—a 70-line path spanning two files and three functions. While the discovered vulnerability is low-severity and already fixed, the work is significant for showing how semantic analysis sidesteps the limitations of shallow pattern matching and call-graph approximation, enabling detection of vulnerabilities in production-style code that linters and syntax-driven tools consistently miss.

[Read original article](https://www.sonarsource.com/blog/sonars-new-js-ts-engine/){: .btn .btn-primary }
