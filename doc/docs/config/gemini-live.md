---
sidebar_position: 5
---

# Configure an End-to-End Pipeline for EchoKit

EchoKit supports real-time models that can reduce latency. However, this approach has several limitations:

* **High API costs** – Real-time API can cost up to $25 per million tokens
* **No voice customization** – You cannot modify the generated voice
* **Limited knowledge integration** – External knowledge bases cannot be added to the model
* **No MCP support** – Model Control Protocol is not supported in most cases

## Prerequisites

Before setting up your end-to-end pipeline, ensure you have:

* **EchoKit server source code** – Follow the [guide](../get-started/echokit-server.md) if you haven't already
* **Gemini API key** – Obtain from [Google AI Studio](https://aistudio.google.com/)
* **TTS service** (optional)

## Gemini API Setup

Google's Gemini is one of the most advanced models supporting voice-to-voice interactions, and EchoKit fully supports it. For detailed implementation, see the [Gemini example](https://github.com/second-state/echokit_server/tree/main/examples/gemini).

### Getting Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "Get API Key" in the left sidebar
4. Create a new API key for your project
5. Copy the key – you'll need it for the configuration

### Basic Configuration

Here's the complete configuration file for Gemini:

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

[gemini]
api_key = "your_api_key_here"

[[gemini.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Please answer user questions as concisely as possible while being accurate and truthful. Use short sentences. Try to be humorous and light-hearted.
"""
```

## Gemini + TTS (Custom Voice)

While real-time models typically don't allow voice customization, EchoKit enables you to customize the voice even when using Gemini!

### Configuration with Custom TTS

Simply add TTS-related parameters to your `config.toml` file:

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

[gemini]
api_key = "your_api_key_here"

[tts]
platform = "StreamGSV"
url = "http://localhost:9094/v1/audio/stream_speech"
speaker = "cooper"

[[gemini.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Please answer user questions as concisely as possible while being accurate and truthful. Use short sentences. Try to be humorous and light-hearted.
"""
```

With these TTS settings configured, you can now use your preferred custom voice.
