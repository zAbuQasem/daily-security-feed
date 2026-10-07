---
layout: post
title: "Today I learned: Python's .start Files as a Persistence Mechanism"
date: 2026-10-04 14:04:20 +0300
categories: [RSS]
tags: [persistence, python, dfir, code-execution]
toc: true
---

Python 3.15 introduces `.start` files as startup entry points in site-packages containing `package.module:callable` references that execute during interpreter initialization before user code runs. This structured replacement for deprecated executable `.pth` imports (PEP 829) improves auditability but retains arbitrary code execution capability. An attacker with site-packages write access can achieve persistence by placing a `.start` file that executes on every interpreter start, regardless of whether the application imports the module. The article provides forensic investigation techniques (using `-S` flag to safely examine without triggering startup code), documents the `.pth` migration, and includes a practical lab demonstrating code execution, with the caveat that when both `.start` and `.pth` files share basenames, the `.pth` import lines are ignored—affecting forensic reconstruction.

[Read original article](https://dfir.ch/posts/today_i_learned_python_start_files/){: .btn .btn-primary }
