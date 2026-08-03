---
layout: post
title: "Guide to Bypassing Hotel Wi-Fi Captive Portals (With Permission)"
date: 2026-08-02 10:54:20 +0300
categories: [RSS]
tags: [network, captive-portal, mac-spoofing, tunneling]
toc: true
---

Guide covering three techniques to bypass hotel and airport Wi-Fi captive portals with network owner permission. MAC spoofing (changing local MAC address or cloning connected devices' MACs) remains reliable since portals track connected devices by MAC—trivial to rotate on Windows (Device Manager) or Linux (macchanger). ICMP tunneling requires an internet-accessible server running Hans; client tunnels IP traffic through ICMP echo requests after establishing a virtual interface (10.1.2.0/24 range). DNS tunneling using Iodine provides an alternative tunnel over DNS queries, requiring domain setup (NS + A records) and a server process. All techniques require outbound access to either ICMP or DNS traffic; network operators can block by filtering outbound ICMP entirely or restricting DNS to recursive queries only.

[Read original article](https://projectblack.io/blog/bypassing-hotel-wi-fi-captive-portals/){: .btn .btn-primary }
