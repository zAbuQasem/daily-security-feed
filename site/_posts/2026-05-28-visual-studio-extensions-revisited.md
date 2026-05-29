---
layout: post
title: "Visual Studio Extensions Revisited"
date: 2026-05-28 12:30:02 +0300
categories: [RSS]
tags: [initial-access, malware, visual-studio, red-team, supply-chain]
toc: true
---

MDSec revisits malicious Visual Studio extension development three years after their original VSCode extension research, contextualized by the recent GitHub compromise via a malicious VS Code extension. The post focuses on the newer VisualStudio.Extensibility (out-of-process, .NET 8) model rather than classic VSSDK extensions, demonstrating how an attacker can build extensions that execute code automatically on file-open events using the ITextViewOpenClosedListener interface — without requiring any user interaction beyond opening a file. The PoC is disguised as a legitimate JSON auto-formatter, providing cover for the malicious payload while triggering silently. The article (though cut off) was heading toward converting this into a full remote-access implant, underscoring how the Visual Studio Marketplace ecosystem remains an effective and underexamined initial access vector for red team engagements.

[Read original article](https://www.mdsec.co.uk/2026/05/visual-studio-extensions-revisited/){: .btn .btn-primary }
