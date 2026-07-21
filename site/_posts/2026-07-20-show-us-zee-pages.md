---
layout: post
title: "Show us Zee Pages"
date: 2026-07-20 13:00:00 +0300
categories: [RSS]
tags: [kubernetes, hardening, configuration, detection]
toc: true
---

A technical examination of Kubernetes z-pages—administrative debugging endpoints—with focus on the distinction between `flagz` (command-line arguments) and `configz` (actual running configuration including values from config files and defaults). The author documents how configuration merging order varies by component and demonstrates why `flagz` alone is insufficient for auditing cluster state, as it misses configuration from files and defaults. The article details authentication and authorization requirements for accessing these endpoints across different Kubernetes components (kube-apiserver lacks `configz` support; kube-proxy has none; scheduler/controller-manager require specific clusterroles and localhost network access; kubelet requires node proxy permissions), and highlights gaps where `configz` omits values when defaults are in effect.

[Read original article](https://raesene.github.io/blog/2026/07/20/show-us-zee-pages/){: .btn .btn-primary }
