---
layout: post
title: "Automating AI Hacking with Tree of Attack"
date: 2026-09-30 16:08:25 +0300
categories: [RSS]
tags: [llm-security, jailbreak, prompt-injection, adversarial-ai, red-team]
toc: true
---

Tree of Attacks with Pruning (TAP) automates LLM jailbreak generation by using one LLM to iteratively propose attack prompts, a target LLM to respond, and an evaluator LLM to score success—building a tree of candidates and pruning weak branches. The approach combines tree-of-thoughts exploration with the PAIR algorithm to achieve >80% jailbreak success rates on state-of-the-art models with <20 queries per attack. Special Token Injection attacks are particularly effective: adversaries embed architecture-specific control tokens (e.g., OpenAI's `<|im_start|>`, Llama's `[INST]`, Mistral/DeepSeek variants) to manipulate role interpretation and bypass safety guardrails. The authors released parley-ng, an improved attack framework with interactive visualization and proof-of-concept exploits for manual testing against LLMs.

[Read original article](https://whiteknightlabs.com/2026/09/30/automating-ai-hacking-with-tree-of-attack/){: .btn .btn-primary }
