---
layout: post
title: "MathJax macro redefinition allows overriding built-in operators"
date: 2026-08-14 00:00:00 +0300
categories: [RSS]
tags: [github, injection, parser, xss]
toc: true
---

A vulnerability in MathJax's newcommand package on GitHub allowed users to redefine built-in mathematical operators (like Σ/sum) through TeX macros (\def, \newcommand, \let), causing visual content spoofing across public repositories, README files, Issues, and Wiki pages. The root cause was that user-defined macros in the new-Command CommandMap were registered with priority -1, making them checked before base operator maps, allowing shadowing without any existence validation. An attacker could inject a payload in a GitHub Issue that would visually override native symbols in the same repo's README—affecting github.com, gist.github.com, and GitHub mobile apps. GitHub mitigated this by disabling the newcommand package entirely, preventing TeX macro definitions at parse time.

[Read original article](https://lab.ctbb.show/writeups/mathjax-macro-redefinition-overrides-builtin-operators){: .btn .btn-primary }
