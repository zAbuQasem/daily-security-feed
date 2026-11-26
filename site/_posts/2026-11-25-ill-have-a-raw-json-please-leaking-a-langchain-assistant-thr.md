---
layout: post
title: "I'll Have a Raw JSON, Please: Leaking a LangChain Assistant Through Format Coercion"
date: 2026-11-25 23:00:00 +0300
categories: [RSS]
tags: [llm-security, langchain, format-coercion, prompt-injection, information-disclosure]
toc: true
---

Format coercion attack against LangChain-based assistants bypasses guardrails by requesting output in raw JSON format instead of prose, causing the LLM to leak internal state including router configuration, agent instructions, tool definitions, retrieved documents with metadata, and safety classifier outputs. Demonstrated against a production healthcare chatbot that refused direct meta-questions after 130+ attempts; systematic probing using format constraints succeeded reliably. The vulnerability stems from the LLM following output-format instructions which override system-prompt guardrails that only protect the question-answer content. Quarkslab determined that framework design is not at fault—only server-side output sanitization and filtering can prevent leakage of the tool graph, knowledge base, and internal procedures.

[Read original article](http://blog.quarkslab.com/ill-have-a-raw-json-please-leaking-a-langchain-assistant-through-format-coercion.html){: .btn .btn-primary }
