---
layout: post
title: "More than just data: The hidden security risks in Jupyter notebooks"
date: 2026-07-06 13:00:00 +0300
categories: [RSS]
tags: [rce, xss, developer-tools, supply-chain, electron]
toc: true
---

SonarSource disclosed multiple critical CVEs affecting Jupyter implementations: CVE-2025-59842 in JupyterLab Desktop and CVE-2026-25847 in the JetBrains Jupyter plugin. Both vulnerabilities chain XSS attacks to achieve remote code execution and arbitrary command injection on a victim's machine. JupyterLab Desktop is vulnerable when a user connects to an untrusted Jupyter server or opens a malicious notebook, while the JetBrains plugin can be exploited when a developer visits a malicious website with a notebook tab open. The root cause involves insufficient input sanitization and weak IPC privilege isolation in Electron-based applications. JupyterLab Desktop will not receive patches due to the project being unmaintained, while JetBrains released a fix in PyCharm 2025.3.2.

[Read original article](https://www.sonarsource.com/blog/hidden-security-risks-in-jupyter-notebooks/){: .btn .btn-primary }
