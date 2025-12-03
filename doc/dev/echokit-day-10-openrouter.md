---
slug: echokit-30-days-day-10-openrouter
title: "Day 10: Using OpenRouter as Your EchoKit LLM Provider | The First 30 Days with EchoKit"
tags: [echokit30days]
---


Over the past two weeks, we’ve explored many moving parts inside the **ASR → LLM → TTS** pipeline.
We’ve changed [the welcome voice](https://echokit.dev/docs/dev/echokit-30-days-day-5-welcome-voic), [updated the boot screen](https://echokit.dev/docs/dev/echokit-30-days-day-4-bootscreen), [switched between multiple ASR providers](https://echokit.dev/docs/dev/echokit-30-days-day-6-groq), and learned how to run the EchoKit server both via [Docker](https://echokit.dev/docs/dev/echokit-30-days-day-2-docker) and [from source](https://echokit.dev/docs/dev/echokit-30-days-day-3-rust).

This week, we shifted our focus to the **LLM**, the part of the pipeline that interprets what you say and decides how EchoKit should respond.

Yesterday, we [used **OpenAI** as the LLM provider](https://echokit.dev/docs/dev/echokit-30-days-day-9-chatgpt).
Today, we’re going to try something more flexible — **OpenRouter**.


##  What Is OpenRouter?

**OpenRouter** is a unified API gateway that gives you access to many different LLMs without changing your code structure.
It’s fully **OpenAI-API compatible** in the context of text generation models, which means EchoKit can work with it right away.

Some reasons I like OpenRouter:

* You can choose from a wide selection of open source LLMs: Qwen, Llama, DeepSeek, Mistral, etc.
* Switching models doesn’t require code changes — just update the model name.
* Often more cost-effective and more customizable.
* Great for exploring different personalities and response styles for EchoKit.


## How to Use OpenRouter as Your LLM Provider

### 1. Get Your OpenRouter API Key

Go to [your OpenRouter dashboard](https://openrouter.ai/settings/keys) and generate an API key.
Keep it private — it works just like an OpenAI API key.


### 2. Update `config.toml`

Open your EchoKit server configuration file and locate LLM:

```
[llm]
provider = "openrouter"
chat_url = "https://openrouter.ai/api/v1/chat/completions"
api_key = "YOUR_API_KEY_HERE"
model = "qwen/qwen3-14b"
history = 5
```

You can replace the model with [any supported model on OpenRouter](https://openrouter.ai/models).


### 3. Restart Your EchoKit Server

If you’re running from the Rust source code, after saving the updated `config.toml`:

```
# Enable debug logging
export RUST_LOG=debug

# Run the EchoKit server in the background
nohup target/release/echokit_server &
```

Or using Docker:

```
docker run --rm \
  -p 8080:8080 \
  -v $(pwd)/config.toml:/app/config.toml \
  secondstate/echokit:latest-server-vad &
```

Then return to the setup page, pair the device if needed, and EchoKit will now respond using OpenRouter. That's it.



Connecting EchoKit to OpenRouter feels like I unlocked a new layer of creativity.
OpenAI gives you a clean and reliable default, but OpenRouter opens the door to experimenting with different model behaviors, tones, and personalities — all without changing your application logic.

If you enjoy tweaking, tuning, and exploring how different models shape your EchoKit’s “brain”, OpenRouter is one of the best tools for that.


---

If you want to share your experience or see what others are building with EchoKit + OpenRouter:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)



