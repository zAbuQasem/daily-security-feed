---
layout: post
title: "From DEF CON Research to Automated Supply Chain Defense, finding npx confusion vulnerabilities  with npxconfuse"
date: 2026-08-11 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, rce, npm, nodejs, zero-day]
toc: true
---

DEF CON researchers discovered npx confusion, a novel supply chain vulnerability where scoped npm packages (e.g., @mycompany/tool) export unscoped binary names that remain unclaimed on the public registry. When developers or CI/CD pipelines invoke npx <binary>, the resolution order falls through to the public registry, allowing attackers to register the unscoped package name and achieve immediate RCE on any developer workstation or CI runner. The author released npxconfuse, an open-source scanner and threat intelligence tool that automates discovery of unclaimed binary names across local codebases, GitHub organizations, and web assets using four modular engines (discovery, extraction, registry analysis, severity classification). The tool has identified zero-day vulnerabilities in major projects including Brave's MCP server, providing practical automation for proactive enterprise defense at scale.

[Read original article](https://lab.ctbb.show/research/from-defcon-research-to-automated-supply-chain-defense-with-npxconfuse){: .btn .btn-primary }
