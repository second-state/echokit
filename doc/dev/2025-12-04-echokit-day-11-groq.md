---
slug: echokit-30-days-day-11-groq
title: "Day 11: Switching EchoKit’s LLM to Groq — And Experiencing Real Speed | The First 30 Days with EchoKit"
tags: [echokit30days]
---


Over the past few days, we’ve been exploring how flexible EchoKit really is — from changing the welcome voice and boot screen to swapping between different ASR providers like Groq Whisper, OpenAI Whisper, and local models.

This week, we shifted our focus to the LLM part of the pipeline. After trying OpenAI and OpenRouter, today we’re moving on to something exciting — Groq, known for its incredibly fast inference.


## Why Groq? Speed. Real, noticeable speed.

Groq runs Llama and other open source models on its LPU™ hardware, which is built specifically for fast inference.
When you pair Groq with EchoKit:

* Responses feel **snappier**, 
* Interactions become smoother

If you want your EchoKit to feel **ultra responsive**, Groq is one of the best providers to try.


## **How to Use Groq as Your EchoKit LLM Provider**

Just like yesterday’s setup, all changes happen in  your `config.toml` of your EchoKit server.

### **Step 1 — Update your LLM section**

Locate the llm section and replace the existing LLM provider with something like:

```toml
[llm]
chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR_GROQ_API_KEY"
model = "openai/gpt-oss-120b"
history = 5
```

Replace the LLM endpoint URL, API key and model name.  [The production models from Groq](https://console.groq.com/docs/models) are `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `meta-llama/llama-guard-4-12b`, `openai/gpt-oss-120b`,  and `openai/gpt-oss-20b`.

### **Step 2 — Restart your EchoKit server**

After editing the config.toml, you will need to restart your EchoKit server.

Docker users:

```
docker run --rm \
  -p 8080:8080 \
  -v $(pwd)/config.toml:/app/config.toml \
  secondstate/echokit:latest-server-vad &
```

Or restart the Rust binary if you’re running it locally.

```
# Enable debug logging
export RUST_LOG=debug

# Run the EchoKit server in the background
nohup target/release/echokit_server &
```


Then return to the setup page, pair the device if needed. You should immediately feel the speed difference — especially on follow-up questions.

---

## **A Few Tips for Groq Users**

* Groq works best with **Llama models**
* You can experiment with smaller or larger models depending on your device’s use case
* For learning or exploring, the default Groq Llama models are a great starting point

Groq is known for ultra-fast inference, and pairing it with EchoKit makes conversations feel almost instant.

If you’re building a responsive voice AI agent, Groq is definitely worth trying.

---

If you want to share your experience or see what others are building with EchoKit + Groq:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)

