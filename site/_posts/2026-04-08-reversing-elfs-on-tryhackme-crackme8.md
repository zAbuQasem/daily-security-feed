---
layout: post
title: "Reversing ELFs on TryHackMe: Crackme8"
source_url: https://0xv1n.github.io/posts/crackme8/
date: 2026-04-08
priority: 3
tags: [reverse-engineering, ctf, binary-analysis, gdb, elf, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://0xv1n.github.io/index.xml
---

A CTF write-up for TryHackMe's crackme8 challenge, walking through static and dynamic analysis of a 32-bit ELF binary. The binary has two sequential checks: argument count must equal 2, and the argument converted via atoi() must equal 0xcafef00d (3405705229). The author demonstrates using GDB with pwndbg to set a breakpoint at the second comparison and patch the EAX register in-flight using `set $eax=3405705229` to bypass the check and trigger the giveFlag() function. Techniques shown include strings enumeration, disassembly in Intel syntax, breakpoint setting, and register manipulation — useful as an introductory GDB tutorial for binary reversing.
