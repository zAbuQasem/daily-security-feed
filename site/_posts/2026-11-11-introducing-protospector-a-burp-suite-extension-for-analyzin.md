---
layout: post
title: "Introducing ProtoSpector: A Burp Suite Extension for Analyzing, Tampering With, and Testing Protobuf and gRPC Traffic"
date: 2026-11-11 23:00:00 +0300
categories: [RSS]
tags: [grpc, protobuf, tool, testing, burp]
toc: true
---

ProtoSpector is a Burp Suite extension that automatically decodes and encodes Protocol Buffer messages in gRPC traffic, supporting both white-box testing with pre-loaded .proto schemas and black-box testing with automatic structure inference. It provides inline editing of inferred message descriptors, a type preview system to test field interpretation, and integration with Burp Repeater for seamless gRPC method invocation. The extension detects multiple Protobuf content types (application/grpc-web+proto, raw Protobuf, etc.) and can auto-generate method descriptors from unknown requests. While currently limited to specific content types and descriptor persistence, it significantly streamlines security testing of gRPC services by eliminating the need to switch between tools.

[Read original article](https://blog.doyensec.com/2026/11/12/protospector.html){: .btn .btn-primary }
