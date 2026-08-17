---
layout: post
title: "Supply Chain Security Analysis of a 9.5M-Install VS Code Extension"
date: 2026-08-16 13:08:38 +0300
categories: [RSS]
tags: [supply-chain, rce, xss, cve, developer-tools]
toc: true
---

ProjectDiscovery disclosed five CVEs in Markdown Preview Enhanced (9.5M VS Code installs), a developer tool with auto-update and host-level privileges. A WaveDrom rendering bug evaluates Markdown content as JavaScript via `window.eval()`, achieving webview XSS; the extension then dispatches attacker-controlled webview messages directly to VS Code commands without validation, allowing arbitrary file write via `updateMarkdown()` (CVE-2026-50733). A second attack surface abuses `.crossnote/config.js` evaluation with `vm.runInNewContext()` — Node's VM is not a security boundary, and prototype-chain escape via `this.constructor.constructor` reaches `process.execSync()` for arbitrary OS commands under the developer's account (CVE-2026-54566). Additional XSS vectors exist in `.crossnote/head.html` injection and webview-to-host message dispatch. All five CVEs are now fixed; supply-chain risk is severe given auto-update, developer-machine access (SSH keys, credentials, source code), and lack of SBOM visibility into extensions.

[Read original article](https://projectdiscovery.io/blog/a-9-5m-install-vs-code-extension-one-markdown-file-and-a-supply-chain-foothold){: .btn .btn-primary }
