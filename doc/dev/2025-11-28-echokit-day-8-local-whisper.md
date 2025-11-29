---
slug: echokit-30-days-day-8-local-whisper
title: "Day 8: Run Whisper Locally on Your Machine | The First 30 Days with EchoKit"
tags: [echokit30days]
---
*(And Today You’ll See How Easy It Is to Run ASR Service Locally)*

Up to now, your EchoKit has worked with Whisper via Groq, and Whisper via OpenAI.

Today, we’re taking a major step forward—your EchoKit will run **fully local ASR** using **Whisper + WasmEdge**.

No cloud requests.
No latency spikes.
No API keys.
Everything runs **on your own machine**, giving you full control over privacy, performance, and cost.

Whisper is an amazing ASR model. Let’s get your local Whisper server running and connect it to EchoKit.

You can also use other tool to run whisper locally as long as the API server is OpenAI-compatible.

## Run the whisper model locally

### 1. Install WasmEdge

Open your terminal and run:

```bash
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install_v2.sh | bash -s
```

This installs WasmEdge along with all base components.


### 2. Install the Whisper Plugin (wasi-nn-whisper)

My computer is a Mac with Apple Silicon, so I will download the whisper plugin using the following command lines


```bash
# Download the whisper plugin
curl -LO https://github.com/WasmEdge/WasmEdge/releases/download/0.14.1/WasmEdge-plugin-wasi_nn-whisper-0.14.1-darwin_arm64.tar.gz

# Extract into the WasmEdge plugin directory
tar -xzf WasmEdge-plugin-wasi_nn-whisper-0.14.1-darwin_arm64.tar.gz -C $HOME/.wasmedge/plugin
```

For other platforms, please refer to [Quick Start with Whisper and LlamaEdge](https://llamaedge.com/docs/ai-models/speech-to-text/quick-start-whisper)


### **3. Download the Portable Whisper API Server**

This app is just a `.wasm` file — lightweight (Size: **3.7 MB**) and cross-platform.

```bash
curl -LO https://github.com/LlamaEdge/whisper-api-server/releases/download/0.3.9/whisper-api-server.wasm
```

### **4. Download a Whisper Model**

You can browse models here:

[https://huggingface.co/ggerganov/whisper.cpp/tree/main](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

Today we’ll use the `medium` model:

```bash
curl -LO https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin
```

### **5. Start the Whisper API Server**

Run Whisper locally:

```bash
wasmedge --dir .:. whisper-api-server.wasm -m ggml-medium.bin
```

You’ll see:

```
Server started on http://localhost:8080
```

This server is **OpenAI API compatible**, so EchoKit can use it directly.




## Connect EchoKit to Your Local Whisper Server

Update your `config.toml` and locate the asr section:

```
[asr]
provider = "http://localhost:8080/v1/audio/transcriptions"
api_key = "sk-xxxx"
lang = "en"
model = "whisper"
```
Yes, you only need to replace the endpoint.

Restart the EchoKit server, pair your device, connect the echockit server to the devicer, and speak.


If you want to share your experience or see what others are building with EchoKit + local whisper:

* Join the **[EchoKit Discord](https://discord.gg/Fwe3zsT5g3)**
* Or share your latency tests, setups, and experiments — we love seeing them

---

Want to get your own EchoKit device?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY Kit](https://echokit.dev/echokit_diy.html)







