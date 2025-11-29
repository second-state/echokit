---
slug: echokit-30-days-day-7-openai
title: "Day 7: Use OpenAI Whisper as Your ASR Provider | The First 30 Days with EchoKit"
tags: [echokit30days]
---

*(And Today You’ll See How Easy It Is to Switch ASR Providers in EchoKit)*

Over the past few days, we’ve powered up EchoKit, [run your own EchoKit server locally](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker), [customized the boot screen](https://echokit.dev/docs/dev/echokit-30-days-day-4-bootscreen), [crafted your own welcome voice](https://echokit.dev/docs/dev/echokit-30-days-day-5-welcome-voice) and [connected it to Groq Whisper for fast speech recognition](https://echokit.dev/docs/dev/echokit-30-days-day-6-groq).

Today, we’re switching things up — literally.

We’ll configure EchoKit to use **Whisper from OpenAI** as the ASR provider.

Not because one is “better,” but because EchoKit is designed to be **modular**, letting you plug in different ASR backends depending on your workflow, API preferences, or costs.


## What's the difference between OpenAI Whisper and Groq Whisper?

Groq Whisper and OpenAI Whisper are based on the same open-source Whisper model.

What differs is the hosting:

* **Groq** runs Whisper on its custom LPU hardware (very fast inference).
* **OpenAI** runs Whisper on their internal infrastructure with its own rate limits and pricing.
* Both will return slightly different results based on their pipeline design and updates.

This isn’t a “which is better” comparison.
It’s about understanding your **options**, and EchoKit makes switching between them smooth and flexible.

And many developers already use OpenAI for other AI tasks, so trying its Whisper API can be convenient. EchoKit adopts multi-provider ASR architecture.

Today’s goal is simple:
👉 **See how easy it is to switch providers while keeping the same Whisper model.**


## How to Use OpenAI Whisper

Now let’s switch EchoKit’s ASR provider.

Open your `config.toml` and locate the `[asr]` section.
Replace it with:

```toml
[asr]
provider = "https://api.openai.com/v1/audio/transcriptions"
api_key = "sk-xxxx"
lang = "en"
model = "whisper-1"
```
A quick breakdown:

* [asr] — we’re configuring the ASR section
* url — Openai’s Whisper endpoint for transcriptions
* lang — your preferred language (en, zh, ja etc.)
* api_key — the key obtained from [OpenAI API plaform](https://platform.openai.com/docs/overview)
* model — OpenAI's supported ASR models (whisper-1 or gpt-4o-transcribe, gpt-4o-mini-transcribe,)

Save → restart your EchoKit server with Docker or from the source code → done.

EchoKit is now using **OpenAI Whisper** for real-time speech-to-text.
The rest of your pipeline (LLM → TTS) stays the same.

You can follow the same process to reconnect the server and your EchoKit device.


EchoKit’s ASR system was built to support all OpenAI-compatible provider — so feel free to try different providers, compare results, and find what works best for your setup.

If you want to share your experience or see what others are building with EchoKit + OpenAI:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

---

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)
