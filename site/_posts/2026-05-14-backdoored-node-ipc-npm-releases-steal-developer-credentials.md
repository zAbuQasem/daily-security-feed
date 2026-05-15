---
layout: post
title: "Backdoored node-ipc npm releases steal developer credentials through DNS queries"
date: 2026-05-14 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, npm, malware, credential-theft, dns]
toc: true
---

Datadog analyzed three malicious `node-ipc` npm releases (`9.1.6`, `9.2.3`, and `12.0.1`) that embedded a backdoor in the package’s CommonJS entrypoint, so the payload executed on `require("node-ipc")` rather than through an npm lifecycle script. The code forks a detached child process, clears `NODE_OPTIONS`, then collects environment variables, `/etc/hosts`, `uname -a`, and a wide set of secrets including `.npmrc`, Git credentials, GitHub CLI auth, cloud provider credentials, SSH keys, Kubernetes tokens, Terraform vars, and `.env` files, packaging them into a gzip-compressed tarball. Exfiltration is done over DNS by resolving `sh.azurestaticprovider.net:443` as a custom resolver and encoding archive metadata and body into TXT lookup names under `bt.node.js`, with chunk prefixes such as `xh`, `xd`, and `xf`; the returned answers are irrelevant because the stolen data is carried in the query names themselves. This is a high-impact software supply chain incident because simply loading the compromised package can leak developer, CI/CD, cloud, and infrastructure credentials from workstations or build environments without obvious foreground behavior.

[Read original article](https://securitylabs.datadoghq.com/articles/node-ipc-npm-malware-analysis/){: .btn .btn-primary }
