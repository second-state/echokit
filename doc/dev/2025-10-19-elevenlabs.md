---
slug: echokit-elevenlabs
title: "EchoKit Now Supports ElevenLabs for High-Quality Voice Generation"
tags: [echokit]
---


We’re excited to share a new update — **EchoKit now supports ElevenLabs**, one of the most advanced voice synthesis platforms in the world. This means your EchoKit can now speak with **natural, expressive, and human-like voices** in multiple languages and styles.

### What’s New

With ElevenLabs integration, EchoKit users can:

* Generate **lifelike speech** with rich tone and emotion
* Choose from **dozens of AI voices** or create your own
* Support **multi-language and multilingual** voice output
* Combine with local AI models for **smarter, private conversations**

Whether you’re building a smart home assistant, a talking robot, or an AI tutor, 11labs voices make your EchoKit sound more alive and engaging.

### How It Works

Using ElevenLabs voices with EchoKit is simple! All you need to do is **configure your TTS parameters** in the `config.toml` file.

1. **Get your API key** from ElevenLabs.
2. **Choose a voice model** from ElevenLabs and note its Voice ID.
3. Update your `config.toml` file like this:

```toml
[tts]
platform = "Elevenlabs"
token = "YOUR_API_KEY_HERE"
voice = "VOICE_ID_HERE"
```

4. Save the file and [rerun your EchoKit server](https://echokit.dev/docs/server/echokit-server).
5. Connect the new server with your device again

### Why It Matters

EchoKit’s mission is to help everyone **build and own their own AI voice agent**.
With the power of ElevenLabs, you can now customize the voice with ease.

### Try It Today

Update your EchoKit server to the latest version and experience **the new generation of AI voice synthesis**.
If you haven’t tried EchoKit yet, [get one now](https://echokit.dev/echokit_diy.html) to build your own voice AI agent at home.

