---
layout: post
title: "We hardened zizmor's GitHub Actions static analyzer"
date: 2026-05-22 11:00:00 +0300
categories: [RSS]
tags: [ci-cd, yaml, static-analysis, supply-chain]
toc: true
---

Trail of Bits describes hardening `zizmor`, a static analyzer for GitHub Actions workflows, after GitHub's addition of YAML anchors exposed parsing and analysis gaps in a tool meant to catch CI/CD misconfigurations like `pull_request_target` abuse. Using a corpus of 41,253 workflow files from 6,612 high-value open-source repositories, they found and fixed four anchor-related bugs: aliases in sequences being flattened incorrectly, anchor prefixes leaking into resolved values, duplicate anchors causing panics, and the `template-injection` audit crashing when `run:` used an aliased scalar. The work also uncovered deserialization edge cases in otherwise valid workflows such as `if: 0`, `timeout-minutes: 0.5`, and `secrets: inherit`, plus expression-evaluator mismatches that were corrected against GitHub's Known Answer Tests. This is practically relevant because `zizmor` is used to detect workflow security issues before deployment, and robustness around real-world YAML and expression handling directly affects defenders' ability to catch supply-chain-relevant GitHub Actions misconfigurations.

[Read original article](https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/){: .btn .btn-primary }
