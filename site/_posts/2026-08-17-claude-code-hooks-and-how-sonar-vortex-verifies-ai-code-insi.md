---
layout: post
title: "Claude Code hooks and how Sonar Vortex verifies AI code inside the loop"
date: 2026-08-17 13:00:00 +0300
categories: [RSS]
tags: [ai-safety, tooling, agent-security, verification, detection]
toc: true
---

Claude Code introduces deterministic hooks—commands that run at fixed points in an AI agent's execution loop (PreToolUse, PostToolUse, SessionStart)—to enforce safety constraints that probabilistic prompts cannot guarantee. Unlike instruction-based safety ("never delete files"), hooks intercept tool calls before execution, receive a JSON description of the action on stdin, and return allow/deny/ask decisions via exit code or JSON stdout. The article provides concrete hook architecture (30+ event types), the JSON contract for tool payloads, and working examples: a bash guardrail that blocks recursive rm of home paths by pattern-matching commands before execution, and post-action verification hooks that check file edits. This addresses the real failure mode where AI agents delete user files due to tilde expansion or path confusion, solving it with deterministic verification wired into the agent's loop rather than relying on model behavior.

[Read original article](https://www.sonarsource.com/blog/claude-code-hooks-and-how-sonar-vortex-verifies-ai-code/){: .btn .btn-primary }
