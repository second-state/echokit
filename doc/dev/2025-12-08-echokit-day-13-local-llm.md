---
slug: echokit-30-days-day-13-local-llm
title: "Day 13 — Running an LLM Locally for EchoKit | The First 30 Days with EchoKit"
tags: [echokit30days]
---

Over the last few days, we explored several cloud-based LLM providers — OpenAI, OpenRouter, and Grok. Each offers unique advantages, but today we’re doing something completely different: we’re running the open-source **Qwen3-4B** model *locally* and using it as EchoKit’s LLM provider.


There’s no shortage of great open-source LLMs—Llama, Mistral, DeepSeek, Qwen, and many others—and you can pick whichever model best matches your use case.

Likewise, you can run a local model in several different ways. For today’s walkthrough, though, we’ll focus on a clean, lightweight, and portable setup:
**Qwen3-4B (GGUF) running inside a WASM LLM server powered by WasmEdge.**
This setup exposes an OpenAI-compatible API, which makes integrating it with EchoKit simple and seamless.

## Run the Qwen3-4B Model Locally

### Step 1 — Install WasmEdge

WasmEdge is a lightweight, secure WebAssembly runtime capable of running LLM workloads through the LlamaEdge extension.

Install it:

```bash
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install_v2.sh | bash -s
```

Verify the installation:

```bash
wasmedge --version
```

You should see a version number printed.



### Step 2 — Download Qwen3-4B in GGUF Format

We’ll use a quantized version of Qwen3-4B, which keeps memory usage manageable while delivering strong performance.

```bash
curl -Lo Qwen3-4B-Q5_K_M.gguf https://huggingface.co/second-state/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q5_K_M.gguf
```


### Step 3 — Download the LlamaEdge API Server (WASM)

This small `.wasm` application loads GGUF models and exposes an **OpenAI-compatible chat API**, which EchoKit can connect to directly.

```bash
curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm
```

### Step 4 — Start the Local LLM Server

Now let’s launch the Qwen3-4B model locally and expose the `/v1/chat/completions` endpoint:

```bash
wasmedge --dir .:. \
  --nn-preload default:GGML:AUTO:Qwen3-4B-Q5_K_M.gguf \
  llama-api-server.wasm \
  --model-name Qwen3-4B \
  --prompt-template qwen3-no-think \
  --ctx-size 4096
```

If everything starts up correctly, the server will be available at:

```
http://localhost:8080
```

## Connect EchoKit to Your Local LLM

Open your EchoKit server’s `config.toml` and update the LLM settings:

```toml
[llm]
llm_chat_url = "http://localhost:8080/v1/chat/completions"
api_key = "N/A"
model = "Qwen3-4B"
history = 5
```

Save the file and restart your EchoKit server.

Next, pair your EchoKit device and connect it to your updated server.

Now try speaking to your device:

> “EchoKit, what do you think about running local models?”

Watch your terminal — you should see EchoKit sending requests to your local endpoint.

Your EchoKit is now fully powered by a local Qwen3-4B model.

Today we reached a major milestone:
**EchoKit can now run entirely on your machine, with no external LLM provider required.**

---

If you want to share your experience or see what others are building with EchoKit:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Share your latency tests, hardware setups, and experiments — we love seeing them!

Want to get your own EchoKit device?

* **[EchoKit Box](https://echokit.dev/echokit_box.html)**
* **[EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)**
