---
layout: post
title: "A new era for software testing"
date: 2026-06-07 09:46:06 +0300
categories: [RSS]
tags: [testing, qa, llm, methodology]
toc: true
---

Salvatore Sanfilippo (Redis creator) proposes using LLMs as automated QA engineers to supplement traditional test suites. The approach involves providing AI agents with markdown specifications detailing test objectives, infrastructure details (SSH endpoints, paths, keys), and recent code changes, then asking them to perform manual testing tasks like regression detection, distributed system verification, and user experience auditing. This addresses structural limitations of traditional testing: code coverage doesn't guarantee state coverage, timing issues in integration tests are difficult to automate, and many quality checks require manual inspection. Real-world applications include testing Redis Arrays for multi-user simulation with persistence and replication, and DwarfStar inference engine for distributed execution and performance regression. The method potentially raises release quality by automating previously-skipped manual testing while complementing the lower code quality of AI-assisted development.

[Read original article](http://antirez.com/news/168){: .btn .btn-primary }
