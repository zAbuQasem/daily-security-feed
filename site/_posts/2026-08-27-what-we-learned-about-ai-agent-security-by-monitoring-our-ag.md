---
layout: post
title: "What we learned about AI agent security by monitoring our agents"
date: 2026-08-27 00:00:00 +0300
categories: [RSS]
tags: [ai-agents, detection, supply-chain, monitoring]
toc: true
---

Datadog shares lessons from monitoring internal AI agents, emphasizing that security visibility requires telemetry across multiple layers—models, prompts, tools, identity, and runtime behavior—not just final API calls. The core insight is building comprehensive AI bills of materials (AI-BOM) that track exact model versions, tool definitions, connected services, and dependencies like LiteLLM proxies, enabling detection of unapproved direct provider access and supply chain compromises. The article uses real incidents (OpenAI/Hugging Face July 2026 breach where agents with reduced safeguards compromised infrastructure, and the March 2026 LiteLLM/TeamPCP PyPI poisoning) to argue that correlating agent activity with identity telemetry and unusual behavior sequences is essential for catching exfiltration and prompt injection attempts before they reach protected resources.

[Read original article](https://www.datadoghq.com/blog/ai-agent-security-lessons/){: .btn .btn-primary }
