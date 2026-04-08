---
layout: post
title: "Yandex Services Source Code Leak"
source_url: https://arseniyshestakov.com/2023/01/26/yandex-services-source-code-leak/
date: 2026-04-08
priority: 2
tags: [source-code-leak, data-breach, threat-intelligence, api-keys, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://arseniyshestakov.com/index.xml
---

Proprietary source code for virtually all major Yandex services was leaked via torrent on BreachForums in January 2023, with files dated to 24 February 2022. The leak covers backend code for Yandex Search, Maps, Alice AI, Taxi, Mail, Disk, Market, Pay, Metrika, and dozens of other services — essentially the entire internal monorepo. The dump does not include git history, pre-built binaries, or pre-trained ML models, but does contain at least some API keys (likely test/staging credentials per the author). The security implications include potential exposure of internal architecture, proprietary anti-bot/anti-ad-block logic (antirobot, antiadblock archives present), captcha systems, CI pipelines, and authentication infrastructure (passport archive included) — all of which could inform future vulnerability research or targeted attacks against Yandex infrastructure.
