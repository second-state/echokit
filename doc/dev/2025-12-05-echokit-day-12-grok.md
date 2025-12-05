---
slug: echokit-30-days-day-12-grok
title: "Day 12 — Switching EchoKit to Grok (with Built-in Web Search) | The First 30 Days with EchoKit"
tags: [echokit30days]
---


# Day 11 — Switching EchoKit to Grok (with Built-in Web Search)

Over the past days, we’ve been exploring how EchoKit’s **ASR → LLM → TTS** pipeline works. We learned how to replace different ASR providers, and this week we shifted our focus to the **LLM** — the part that thinks, reasons, and decides how EchoKit should reply.

We have connected EchoKit to [OpenAI](https://echokit.dev/docs/dev/echokit-30-days-day-9-chatgpt) and [OpenRouter](https://echokit.dev/docs/dev/echokit-30-days-day-10-openrouter).
**Today, we’re trying something different: Grok — a super-fast LLM with built-in web search.**


## Why Grok?

Grok, developed by X, stands out for a few practical reasons:

* **⚡ Extremely fast inference**
  Great for voice AI agents like EchoKit.

* **🔍 Built-in web search**
  Your device can answer questions using fresh information from the internet.

* **🔌 OpenAI-compatible API**
  Minimizes changes — EchoKit can talk to it just like it talks to OpenAI.

For a small device that depends on fast responses, Grok is an excellent option.

## How to Use Grok as Your LLM in EchoKit

All you need to do is update your `config.toml`.
No code changes, no rewriting your server — just swap URLs and keys.

### **1. Set Grok as the LLM provider**

In your `config.toml`, make sure the `[llm]` section points to Grok:

```toml
[llm]
llm_chat_url = "https://api.x.ai/v1/chat/completions"
api_key = "YOUR_API_KEY"
model = "grok-4-1-fast-non-reasoning"
history = 5
```

You can find your Grok API key in your **[xAI account dashboard](https://console.x.ai/)**. You will need to buy credits before using the Grok API.

Don't rush to close the `config.toml` window.

## 2. Enable Grok’s Web Search

This is the special part.

Add the following section in the config.toml file:

```toml
[llm.extra]
search_parameters = { mode = "auto" }
```

`mode = "auto"` allows Grok to decide when it should fetch information from the web.
Ask anything news-related, trending, or timely — Grok will search when needed. 

### Restart the EchoKit server

After that, save these changes, and restart your EchoKit server.

## **Try It Out**

Press the K0 button to chat with EchoKit and try these prompts:

* “What’s the latest news in AI today?”
* “How’s the Bitcoin price right now?”
* “What's the current time in San Francisco?”

If everything is configured correctly, you’ll notice Grok pulling fresh information in its responses.
It feels different — the answers are more grounded in what’s happening *right now*.


Switching EchoKit to Grok was surprisingly simple — just a few lines in a config file.
Now my device can do real-time search when a question needs up-to-date info.

---

If you want to share your experience or see what others are building with EchoKit + Grok:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)


