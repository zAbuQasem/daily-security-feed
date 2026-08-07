---
layout: post
title: "ChainDrop: Inside a Self-Propagating npm Worm"
date: 2026-08-06 22:26:39 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, cloud, malware, npm]
toc: true
---

ChainDrop is a self-propagating npm worm that compromised 400+ packages with hundreds of millions of weekly downloads. The worm injects a preinstall hook in package.json that downloads Bun runtime and executes a 727KB obfuscated payload, which harvests cloud IAM credentials, npm/GitHub tokens, SSH keys, developer tool secrets, and temporary GitHub Actions runner credentials. The attacker then uses stolen npm tokens to republish infected versions of legitimate packages while maintaining functionality. The worm employs blockchain-based (Ethereum) C2 resolution and can reconfigure its entire infrastructure via a single Ethereum transaction without requiring malware updates. Unit 42 detected 453 compromised repositories and identified persistence mechanisms targeting developer tools and AI coding assistants.

[Read original article](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/){: .btn .btn-primary }
