---
layout: post
title: "Scala Security Audit"
date: 2026-05-31 22:00:00 +0300
categories: [RSS]
tags: [audit, scala, compiler, deserialization, xss]
toc: true
---

Quarkslab conducted the first security audit of Scala 3 in partnership with OSTIF, identifying 9 vulnerabilities across the compiler, standard library, and tooling. Key findings include a deserialization gadget in scala.sys.Process.ProcessBuilderImpl that could be exploited in Java deserialization chains, a stored XSS vulnerability in the Scaladoc documentation generator, and multiple implementation bugs including an infinite loop in the TASTy unpickler and uncaught exceptions in the process command parser. The audit combined manual code review, static analysis with Gadget Inspector and Opengrep, and fuzzing of critical standard library components. All findings have been disclosed with mitigation recommendations to the Scala maintainers to improve the language ecosystem's security posture.

[Read original article](http://blog.quarkslab.com/scala-security-audit.html){: .btn .btn-primary }
