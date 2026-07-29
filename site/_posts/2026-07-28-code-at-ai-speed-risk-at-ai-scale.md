---
layout: post
title: "Code at AI Speed, Risk at AI Scale"
date: 2026-07-28 12:27:50 +0300
categories: [RSS]
tags: [authentication, access-control, ai-generated-code, financial, pii]
toc: true
---

A financial services onboarding application built with Claude AI contained a critical authentication bypass in the applicant resume flow: the system issued access tokens based solely on possession of a GUID without proving the requester controlled that applicant's identity or session. The vulnerability exposed highly sensitive PII including SSNs, identity verification data, payment details, and co-applicant information. The root cause was an AI-assisted implementation plan that focused on token behavior (expiration, logging, rate limiting) but omitted the fundamental pre-issuance question: what proof must be established before granting a token? The case illustrates how AI can accelerate development of functional but insecure patterns when it lacks context about institutional risk models and the distinction between identifiers that locate records and proof that authorizes access to them.

[Read original article](https://www.sygnia.co/blog/ai-generated-code-security-risks/){: .btn .btn-primary }
