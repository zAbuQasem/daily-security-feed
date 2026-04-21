---
layout: post
title: "From Code to Pipeline: Wiz Code Now Secures Your Build Environment"
date: 2026-04-21 03:12:42 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, prompt-injection, ai-agents]
toc: true
---

Wiz frames CI/CD pipelines as a high-value attack surface because build jobs routinely run with repository write access, cloud credentials, registry tokens, SSH keys, and OIDC-issued identities, so compromising the pipeline can yield broad downstream access. The article highlights common failure modes behind recent pipeline incidents: unsafe workflow trigger configurations, over-privileged jobs, and tampered third-party actions that execute inside trusted build contexts. It also calls out a newer risk around AI agents embedded in systems like GitHub Actions, where untrusted pull requests or issue comments can supply prompt-injection content that causes the agent to run attacker-chosen commands with the job token and other CI secrets. This is more of a defensive product-positioning piece than original vulnerability research, but it is still useful as a concise summary of how modern supply-chain compromise increasingly targets build orchestration rather than application code alone.

[Read original article](https://www.wiz.io/blog/from-code-to-pipeline-wiz-code-now-secures-your-build-environment){: .btn .btn-primary }
