---
layout: post
title: "Claude Code Cost Tracking: AWS Bedrock vs Pro Max (Part 2) — Tag Propagation, Sydney Migration, Bug Fixes"
date: 2026-05-08 02:43:23 +0300
categories: [RSS]
tags: [aws, bedrock, cloud, tagging, cost-explorer]
toc: true
---

The post is a technical postmortem on why AWS Bedrock Claude usage was showing as effectively $0 when filtered by a cost-allocation tag, despite more than $62 in real spend. The author traced the issue to routing: their wrapper was invoking AWS system-defined cross-region inference profiles such as `us.anthropic.claude-opus-4-7`, which do not inherit user-defined tags, instead of sending traffic through their own tagged Application Inference Profiles (AIPs). They also found a logic bug in the `claude-cost` script, where a fallback warning only triggered on `total == 0`, so a tiny tagged value of `0.000044` suppressed detection of the broader attribution failure; changing the threshold to something like `< 0.01` fixed the silent failure. The article is most useful for teams using Bedrock, Cost Explorer, and AIPs to attribute model spend, because it documents the exact failure mode, the relevant AWS APIs (`ce get-cost-and-usage`, `list-inference-profiles`), and the practical implications of cross-region profile selection.

[Read original article](https://www.uncommonengineer.com/docs/engineer/AI/claude-code-cost-tracking-bedrock-vs-pro-max-part-2){: .btn .btn-primary }
