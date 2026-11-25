---
layout: post
title: "Ephyra: A new agentic property-based testing library to find the bugs you missed"
date: 2026-11-24 00:00:00 +0300
categories: [RSS]
tags: [tool, testing, fuzzing, ai, bug-finding]
toc: true
---

Ephyra is an open-source property-based testing framework that uses coding agents to autonomously generate and optimize test case generators. Rather than hand-crafted test cases, engineers define abstract properties (rules the code must follow), and agents iteratively improve random input generators through coverage-driven feedback loops. Across 26 widely-used open-source projects, Ephyra uncovered 535 previously-unknown bugs, including 24-year-old memory-safety vulnerabilities in OCaml, 21-year-old exponential parsing bugs in PostgreSQL, and 13-year-old database corruption in SQLite—bugs that survived years of manual testing and extensive review. The approach uses techniques like Ternary Logic Partitioning (TLP) for SQL systems to discover subtle logic errors; SQLite's incorrect sum(b ORDER BY a) result is a concrete example of the class of bugs found. The tool, written in Rust and usable for C++, Python, and other languages, includes a research paper accepted to POPL 27 and open-source code with case studies.

[Read original article](https://www.datadoghq.com/blog/ai/agentic-property-based-testing-with-ephyra/){: .btn .btn-primary }
