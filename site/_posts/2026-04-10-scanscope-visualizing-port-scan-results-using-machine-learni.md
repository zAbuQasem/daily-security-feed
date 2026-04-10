---
layout: post
title: "Scanscope: Visualizing Port Scan Results Using Machine Learning Methods"
date: 2026-04-10 03:12:52 +0300
categories: [RSS]
tags: [tool, network-scanning, machine-learning, recon, visualization]
toc: true
---

Scanscope is an open-source Python tool that transforms nmap XML output into interactive 2D visualizations of large network port scan results. It models each host as a binary vector in a 2^17-dimensional space (one dimension per TCP/UDP port), then applies PCA for dimensionality reduction down to 2D, with HDBSCAN for cluster assignment. The resulting output is a self-contained HTML file (using Zundler bundling and in-browser SQLite via WASM) rendering an interactive bubble chart where bubble size reflects host group population and colors encode common port/service patterns. UMAP was evaluated and rejected in favor of PCA due to non-determinism, heavy dependencies, and no structural manifold advantage for binary port data. Practical use case is spotting anomalous hosts and comparing network posture across time or scanning vantage points — useful for pentesters and network defenders working at enterprise scale.

---

[Read original article](https://blog.syss.com/posts/scanscope/){: .btn .btn-primary }
