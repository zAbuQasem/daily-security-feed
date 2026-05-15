---
layout: post
title: "Backdoored Cemu release linked to TanStack and Mistral supply chain campaign"
date: 2026-05-14 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, github, npm, pypi, malware]
toc: true
---

Datadog traces a coordinated supply-chain campaign that poisoned 170 legitimate npm and PyPI packages and links it to a separate compromise of the official Cemu GitHub release assets. The malicious Linux AppImage on cemu-project/Cemu contained a foreign Python zipapp at `usr/share/Cemu/scripts/startup.pyz`, which was byte-for-byte identical to the `transformers.pyz` payload seen in the backdoored `mistralai` package and included collectors for AWS, GCP, Azure, Kubernetes, Vault, passwords, and filesystem data. By querying the GitHub Releases API, the researchers showed the Linux assets for `v2.6` were deleted and re-uploaded a year after the original release by user `MangelSpec`, while all historical assets had been uploaded by `github-actions[bot]`, indicating direct abuse of repository release permissions rather than CI compromise. The case is notable because it extends the same credential-driven campaign across npm, PyPI, and GitHub Releases, demonstrating how a compromised maintainer account can silently replace trusted binaries under a legitimate tag and project page.

[Read original article](https://securitylabs.datadoghq.com/articles/backdoored-cemu-release-teampcp-supply-chain-campaign/){: .btn .btn-primary }
