---
layout: post
title: "Let’s talk about encrypted reasoning"
date: 2026-05-29 03:52:19 +0300
categories: [RSS]
tags: [llm, cryptography, replay-attack, side-channel, ai-security]
toc: true
---

OpenAI and Anthropic's reasoning APIs send encrypted chain-of-thought (CoT) blobs to API clients, ostensibly so stateless/zero-retention sessions can replay model reasoning state without the server persisting it. The author reverse-engineered the blob formats: OpenAI's appear Fernet-based, Anthropic's use a multi-field structure with 12-byte IVs (suggesting AES-GCM or ChaCha20) and a 64-byte field labeled 'signature' that does not appear to be a true signature. Direct ciphertext tampering is rejected server-side, but replay attacks succeed — unmodified old reasoning blobs can be injected into new sessions, and even across different accounts, with no API error. Side-channel leakage is also confirmed: blob length and token counts correlate with reasoning effort and may reveal information about suppressed model outputs, including content the model would otherwise withhold from users.

[Read original article](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/){: .btn .btn-primary }
