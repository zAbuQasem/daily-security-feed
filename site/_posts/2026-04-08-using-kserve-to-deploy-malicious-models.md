---
layout: post
title: "Using KServe to deploy malicious models"
date: 2026-04-08 00:00:00 +0300
categories: [Research]
tags: [supply-chain, kubernetes, mlops, container-security, malware]
toc: true
---

This research demonstrates how KServe — a Kubernetes-native ML model serving platform — can be abused to deploy malicious models as part of pre/post-exploitation in MLOps environments. The attack embeds a malicious TensorFlow model inside a container image that still performs valid inference (preserving accuracy), making detection extremely difficult for both sandboxes and runtime scanners. The container is pushed to an internal or external registry and deployed via a KServe InferenceService YAML, landing attacker-controlled code inside the organization's Kubernetes cluster with access to sensitive ML data pipelines ('crown jewels'). The technique works as both an insider pivot and an external supply chain attack vector. Defensive recommendations include eBPF-based runtime detection (Tracee, Cilium), restricting model formats to safetensors, and enforcing internal-only model/container registries.

---

[Read original article](https://5stars217.github.io/2023-10-25-using-KServe-to-deploy-malicious-models/)
