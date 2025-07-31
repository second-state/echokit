---
sidebar_position: 1
---

# EchoKit

**EchoKit** is an open-source platform that helps you build your own voice-based AI assistant — combining both hardware and software in one unified stack. You can assemble a smart, customizable device that listens, talks, thinks, and even connects with the physical world.

Whether you're creating a language learning partner, a personal companion, or a voice-controlled interface for your smart home, EchoKit gives you full control, privacy, and flexibility — with no cloud required.

## What’s Inside

EchoKit is more than just a DIY project — it’s a learning tool, a developer kit, and a foundation for serious voice AI applications. This documentation will guide you through:

- Assembling and flashing your EchoKit device
- Running and customizing the voice AI system
- Cloning voices and integrating large language models
- Interacting with the EchoKit Voice
- Exploring and contributing to our fully open-source codebase

Let’s start with the hardware overview.

## Hardware overview

The EchoKit firmware is written in **Rust** and open-sourced in the [echoKit_box](https://github.com/second-state/echokit_box) repository.

We officially support the EchoKit device, but you can also add support for your own hardware by submitting a pull request.

**Basic hardware requirements:**

- ESP32-S3 development board  
- 16MB external flash storage  
- Microphone  
- Amplifier + audio decoder module  
- Speaker  
- WiFi and Bluetooth (typically included in ESP32-S3)

> 📘 Why Rust? It’s fast, safe, and well-suited for embedded systems. Learn more by reading Why we Choose Rust.


## Software overviews

EchoKit’s software stack is also 100% open source — designed to be lightweight, efficient, and hackable.

- **[WebSocket Server](https://github.com/second-state/echokit_server)** – Acts as the central hub of your voice agent. It manages VAD (voice activity detection), speech recognition, speech synthesis, large language model interaction, and MCP integration. Written in Rust. 
- **[VAD Server](https://github.com/second-state/silero_vad_server)** – A Rust port of the Silero VAD library that helps focus only on human speech.
- **[TTS Server](https://github.com/second-state/gsv_tts)** – A Rust implementation of GPT-SoVITS for streaming voice synthesis and cloning.
  - **[Voice Clone Tool](https://echokit.dev/voice_clone/)** – A lightweight utility to create a personal voice model from your recordings or the voice you like.
 
Besides this, we also offer tools to run Whisper (Speech to Text), LLM, TTS model on your own machine and several MCP servers that can integrated with EchoKit. 

With EchoKit, you're not just using AI — you're building it, learning from it, and shaping it to fit your world.

Let’s get started.

