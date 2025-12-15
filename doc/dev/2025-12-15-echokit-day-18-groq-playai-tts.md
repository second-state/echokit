---
slug: echokit-30-days-day-18-groq-playai-tts
title: "Day 18: Switching EchoKit to Groq PlayAI TTS | The First 30 Days with EchoKit"
tags: [echokit30days, tts]
---


Over the past two weeks, we’ve built almost every core component of a voice AI agent on EchoKit:

ASR to turn speech into text.
LLMs to reason, chat, and call tools.
[System prompts to shape personality](https://echokit.dev/docs/dev/echokit-30-days-day-14-personality).
[MCP servers to let the agent take real actions](https://echokit.dev/docs/dev/echokit-30-days-day-15-mcp-web-search).
[TTS to give EchoKit a voice](https://echokit.dev/docs/dev/echokit-30-days-day-17-elevenlabs）.

Today, we close the loop again — but this time, with a **new voice engine**.

We’re switching EchoKit’s TTS backend to **[Groq’s PlayAI TTS](https://console.groq.com/docs/model/playai-tts)**.

### Why change TTS?

Text-to-speech is often treated as the “last step” in a voice pipeline, but in practice, it’s the part users feel the most.

Latency, voice stability, and natural prosody directly affect whether a voice agent feels responsive or awkward. Since Groq already powers our ASR and LLM experiments with very low latency, it made sense to test their TTS offering as well.

PlayAI TTS fits EchoKit’s design goals nicely:
It’s fast, simple to integrate, and exposed through an OpenAI-compatible API.

That means **no special SDK**, and no changes to EchoKit’s core architecture.

### Switching EchoKit to Groq PlayAI TTS

On EchoKit, swapping TTS providers is mostly a configuration change.

To use Groq PlayAI TTS, we update the `tts` section in `config.toml` like this:

```toml
[tts]
platform = "openai"
url = "https://api.groq.com/openai/v1/audio/speech"
model = "Playai-tts"
api_key = "gsk_xxx"
voice = "Fritz-PlayAI"
```

A few things worth calling out:

The `platform` stays as `openai` because Groq exposes an OpenAI-compatible endpoint.
We point the `url` directly to Groq’s audio speech API.
The model is set to `Playai-tts`.
Voices are selected via the `voice` field — here we’re using `Fritz-PlayAI`.

Once this is in place, no other code changes are required.

Restart the EchoKit server, reconnect the EchoKit device and the new server, and the agent speaks with a new voice.

### The bigger picture

Most importantly, switching different tts providers reinforces one of EchoKit’s core ideas:
**every part of the voice pipeline should be swappable.**


It’s about treating voice as a first-class system component — something you can experiment with, replace, and optimize just like models or prompts.

EchoKit doesn’t lock you into one vendor or one voice.
If tomorrow you want to try a different TTS engine, or even run one locally, the architecture already supports that.

---

Want to get your own EchoKit device and make it unique?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY](https://echokit.dev/echokit_diy.html)

Join the [EchoKit Discord](https://discord.gg/Fwe3zsT5g3) to share your welcome voices and see how others are personalizing their voice AI agents!

