---
layout: post
title: "Malicious Coding Agent Skills and the Risk of Dynamic Context"
date: 2026-05-11 00:00:00 +0300
categories: [RSS]
tags: [ai-agents, supply-chain, prompt-injection, credential-theft, developer-tools]
toc: true
---

Datadog Security Labs analyzes a supply-chain style attack against coding agents by abusing Claude Code skills, especially the `!` dynamic-context feature that executes shell commands before the rendered skill content is shown to the model. Because these commands run pre-prompt, model-side prompt-injection defenses cannot inspect or block them, creating a path from attacker-controlled repository content to code execution on a developer workstation. The post maps the skill loading surfaces that make this realistic, including project-local `.claude/skills/`, nested project folders, plugins, personal skill directories, and `--add-dir` paths that auto-load skills. As a concrete example, it dissects the malicious `Clawsights` skill, which uses `gh auth token` to harvest GitHub credentials and then exfiltrates them with `curl`, showing how trusted agent workflows can be turned into credential theft and source-code reconnaissance. The article also covers mitigations such as setting `"disableSkillShellExecution": true` in managed settings, code-reviewing `.claude/` changes, and monitoring for suspicious processes and outbound connections during agent use.

[Read original article](https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/){: .btn .btn-primary }
