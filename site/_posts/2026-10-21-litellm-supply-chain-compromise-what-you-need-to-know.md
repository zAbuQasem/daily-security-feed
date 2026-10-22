---
layout: post
title: "LiteLLM supply chain compromise: What you need to know"
date: 2026-10-21 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, cloud, malware, rce]
toc: true
---

Attackers compromised LiteLLM (23 million weekly downloads) on PyPI and Docker by using stolen GitHub OAuth tokens from three engineers to launch the release pipeline against a malicious fork named `Berri-AI/litellm` (vs. legitimate `BerriAI/litellm`). The malicious version 1.107.0 injected `cook.pth`, `cook.py`, and `sitecustomize.py` into site-packages, executing on every Python interpreter startup regardless of whether LiteLLM was imported. The payload steals cloud credentials (AWS, GCP, Azure, Kubernetes), developer secrets (SSH, GPG, git/npm/PyPI tokens), and LLM API keys, exfiltrating them via AES-256 and RSA-4096 encrypted channels to a lookalike domain. A second-stage RAT capability fetches and executes arbitrary Python code from a GitHub repository, marking the second LiteLLM supply chain compromise in 2026.

[Read original article](https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/){: .btn .btn-primary }
