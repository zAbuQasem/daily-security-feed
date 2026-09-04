---
layout: post
title: "LLMHaxor Update"
date: 2026-09-03 04:00:00 +0300
categories: [RSS]
tags: [llm, testing, tool, websocket, burp-suite]
toc: true
---

LLMHaxor is an updated tool for AI-powered application security testing, designed to work in restricted environments (corporate VDI, no internet, no special permissions) where heavyweight tools like Burp's native AI features cannot run. The update adds a WebSocket proxy that converts streaming WebSocket responses (common in chat APIs and real-time features) into an HTTP interface compatible with Burp Suite Intruder, enabling fuzzing of modern API patterns. The tool runs locally with Ollama and lightweight models (Granite, Llama3.2), requires only a JRuby.jar and home-directory installation, and fills a practical niche for penetration testers facing environment constraints that other LLM testing frameworks (PyRIT, Garak, Augustus) cannot easily overcome.

[Read original article](https://trustedsec.com/blog/llmhaxor-update){: .btn .btn-primary }
