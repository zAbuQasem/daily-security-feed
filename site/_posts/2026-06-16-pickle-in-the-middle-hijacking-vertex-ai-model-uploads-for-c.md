---
layout: post
title: "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE"
date: 2026-06-16 10:00:29 +0300
categories: [RSS]
tags: [cloud, rce, gcp, bucket-squatting, ai-security]
toc: true
---

A bucket squatting vulnerability in Google Cloud Vertex AI SDK for Python (versions 1.139.0–1.140.0) allows an attacker with a separate GCP project to hijack victims' model uploads without any initial access to their account. The SDK constructs deterministic default staging bucket names from the project ID and region, then fails to verify bucket ownership—enabling attackers to preemptively create matching buckets in their own projects. Once a victim uploads a model, the attacker replaces it with a malicious pickle-serialized model that executes arbitrary code via deserialization when the model is deployed and loaded by Vertex AI's serving infrastructure. The vulnerability enables zero-access RCE, data exfiltration, and lateral movement within victims' cloud environments. Google patched the issue in SDK v1.148.0 (April 15, 2026).

[Read original article](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/){: .btn .btn-primary }
