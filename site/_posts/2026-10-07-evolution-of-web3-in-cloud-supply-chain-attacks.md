---
layout: post
title: "Evolution of Web3 in Cloud Supply Chain Attacks"
date: 2026-10-07 22:00:16 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, cloud, malware, web3]
toc: true
---

Threat actors have evolved supply chain attack infrastructure to use blockchain-based command-and-control channels instead of hardcoded endpoints, enabling dynamic botnet updates via smart contracts. Recent campaigns including ChainDrop (npm worm infecting 400+ packages) and PolinRider (multi-registry: npm, Go modules, Packagist) specifically target developer endpoints and CI/CD runners, injecting malicious scripts that exfiltrate ephemeral cloud IAM tokens, service account keys, and deployment secrets through memory scanning. Malware resolves C2 endpoints using Web3 mechanisms like EtherHiding (smart contract queries) and zero-data transaction decoding across multiple blockchains (TRON, Aptos, BSC), bypassing traditional DNS sinkholing and network monitoring. North Korea-affiliated state-sponsored actors (Alluring Pisces/Sapphire Sleet) have operationalized these techniques, targeting high-profile projects including Axios, Mastra AI, and Rust's arrayref.

[Read original article](https://unit42.paloaltonetworks.com/web3-cloud-supply-chain-attacks/){: .btn .btn-primary }
