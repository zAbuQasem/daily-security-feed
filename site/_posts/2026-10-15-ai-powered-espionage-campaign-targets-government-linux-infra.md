---
layout: post
title: "AI-Powered Espionage Campaign Targets Government Linux Infrastructure"
date: 2026-10-15 22:00:09 +0300
categories: [RSS]
tags: [apt, linux, web-shell, persistence, ai-malware]
toc: true
---

Unit 42 tracked CL-UNK-1211, an APT campaign targeting government and state-affiliated Linux infrastructure from October 2025–April 2026, notable for using AI-generated payloads to streamline attack code. Attackers deployed multiple web shells on Linux servers and modified PHP auto_prepend_file configurations across /etc/php/ and /opt/plesk/php/ directories to achieve automatic persistence and backdoor execution. The campaign combined open-source utilities and custom cross-platform backdoors for reconnaissance, database dumping, mailbox enumeration to harvest social media credentials, and data exfiltration, while employing defense evasion through endpoint protection disabling and log tampering. Payload analysis revealed conversational AI-generated comments, extensive Base64 encoding, and seamless multi-language switching (PHP, JavaScript, Bash, Python), indicating operators used LLMs to accelerate payload development—an emerging pattern in nation-state espionage.

[Read original article](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/){: .btn .btn-primary }
