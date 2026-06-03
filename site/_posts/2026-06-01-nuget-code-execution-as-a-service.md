---
layout: post
title: "NuGet Code Execution As A Service"
date: 2026-06-01 12:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, nuget, dotnet, rce]
toc: true
---

NuGet packages can execute arbitrary code during restore operations via malicious MSBuild .targets files containing exec tasks, which run before a project is even built. The attack leverages NuGet's design where custom build targets in packages automatically execute as part of restore, CollectPackageReferences, and other early-stage operations. Visual Studio's Mark of the Web protection fails to apply when cloning repositories directly (vs opening downloaded archives), allowing silent code execution when a developer opens a cloned malicious project. Microsoft has classified this behavior as 'by design' despite its clear supply chain attack implications for .NET CI/CD pipelines.

[Read original article](https://tierzerosecurity.co.nz/2026/06/02/nuget-code-execution.html){: .btn .btn-primary }
