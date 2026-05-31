---
layout: post
title: "Why Custom Attributes in .NET give me Nightmares"
date: 2026-05-30 00:00:00 +0300
categories: [RSS]
tags: [dotnet, file-format, reverse-engineering, parsing, malware-analysis]
toc: true
---

A deep technical analysis of .NET Custom Attribute binary encoding and why parsing them correctly is extraordinarily difficult. The author, maintainer of the AsmResolver PE parsing library, explains that enum-typed attribute arguments have no type indicator in the blob signature — the underlying type must be resolved at parse time, requiring full assembly resolution (DLL probing, JSON/XML config parsing, metadata stream traversal) and TypeDef table scanning across potentially thousands of rows. This has cascading implications for tools that statically analyze .NET binaries (malware analyzers, decompilers, PE parsers), since misreading enum sizes corrupts all subsequent argument parsing. The article is primarily a format deep-dive relevant to anyone building .NET binary analysis tooling.

[Read original article](https://blog.washi.dev/posts/custom-attributes-and-why-they-suck/){: .btn .btn-primary }
