---
layout: post
title: "The serpent’s tongue: Luring the Python out of its den"
date: 2026-07-14 10:00:06 +0300
categories: [RSS]
tags: [supply-chain, python, malware, rce]
toc: true
---

Talos Intelligence analyzes the Python package supply chain attack landscape through the complete installation lifecycle: hosting (PyPI, VCS, custom servers), distribution (sdist vs. wheel formats), and installation layers. The research exposes that malicious packages establish footholds during installation itself—not just at import—by abusing setup.py arbitrary code execution and pip configuration vectors (index URLs, environment variables, config files). The work contextualizes this with GitHub's data showing 69% YoY growth in malware advisories and 17% of GitHub Advisory Database entries targeting the Pip ecosystem, including real campaigns like TeamPCP's infrastructure compromise. Defensive measures include dependency auditing, version pinning, and installation-time access controls.

[Read original article](https://blog.talosintelligence.com/the-serpents-tongue-luring-the-python-out-of-its-den/){: .btn .btn-primary }
