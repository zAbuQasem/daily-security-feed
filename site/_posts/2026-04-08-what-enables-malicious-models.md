---
layout: post
title: "What enables malicious models?"
date: 2026-04-08 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ml-security, typosquatting, huggingface]
toc: true
---

This article analyzes the practical attack surface that makes malicious ML models on HuggingFace a viable threat beyond just the model file itself. The primary vector highlighted is namespace/organization squatting: any user can create an org with any name and send invitations that appear to originate from HuggingFace's official domain, tricking engineers into joining attacker-controlled orgs and granting them read/write on repositories. Secondary vectors include typosquatting aided by HuggingFace's UI font choices that blur visually similar characters (1/l, i/l). The author draws parallels to NPM package takeover attacks and warns that truly malicious actors will target existing popular model repositories rather than creating new ones, making supply-chain integrity of ML models a pressing concern for organizations using HuggingFace in their pipelines.

[Read original article](https://5stars217.github.io/2024-03-04-what-enables-malicious-models/)
