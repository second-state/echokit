---
slug: echokit-30-days-day-20-local-gpt-sovits
title: "Day 20: Running GPT-SoVITS Locally as EchoKit’s TTS Provider | The First 30 Days with EchoKit"
tags: [echokit30days, tts]
---


Over the past few days, we’ve been switching EchoKit between different cloud-based TTS providers and voice styles. It’s fun, it’s flexible, and it really shows how modular the EchoKit pipeline is.

But today, I want to go one step further.

**Today is about running TTS fully locally.**
No hosted APIs. No external requests. Just an open-source model running on your own machine — and EchoKit talking through it.

For Day 20, I’m using **GPT-SoVITS** as EchoKit’s local TTS provider.



## What Is GPT-SoVITS?

**GPT-SoVITS** is an open-source text-to-speech and voice cloning system that combines:

* A GPT-style text encoder for linguistic understanding
* SoVITS-based voice synthesis for natural prosody and timbre

Compared to traditional TTS systems, GPT-SoVITS stands out for two reasons.

First, it produces **very natural, expressive speech**, especially for longer sentences and conversational content.

Second, it supports **high-quality voice cloning** with relatively small reference audio, which has made it popular in open-source voice communities.

Most importantly for us:
**GPT-SoVITS can run entirely on your own hardware.**



## Running GPT-SoVITS Locally

To make local GPT-SoVITS easier to run, we also ported GPT-SoVITS to a **Rust-based implementation**.

This significantly simplifies local deployment and makes it much easier to integrate with EchoKit.

> Check out [Build and run a GPT-SoVITS server](https://echokit.dev/docs/server/gpt-sovits) for details. The following steps are on a MacBook

First, install the LibTorch dependencies:

```bash
curl -LO https://download.pytorch.org/libtorch/cpu/libtorch-macos-arm64-2.4.0.zip
unzip libtorch-macos-arm64-2.4.0.zip
```

Then, tell the system where to find LibTorch:

```bash
export LD_LIBRARY_PATH=$(pwd)/libtorch/lib:$LD_LIBRARY_PATH
export LIBTORCH=$(pwd)/libtorch
```

Next, clone the source code and build the GPT-SoVITS API server:

```bash
git clone https://github.com/second-state/gsv_tts
git clone https://github.com/second-state/gpt_sovits_rs

cd gsv_tts
cargo build --release
```

Then, download the required models.
Since I’m running GPT-SoVITS locally on my MacBook, I’m using the **CPU versions**:

```bash
cd resources
curl -L -o t2s.pt https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/t2s.cpu.pt
curl -L -o vits.pt https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/vits.cpu.pt
curl -LO https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/ssl_model.pt
curl -LO https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/bert_model.pt
curl -LO https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/g2pw_model.pt
curl -LO https://huggingface.co/L-jasmine/GPT_Sovits/resolve/main/v2pro/mini-bart-g2p.pt
```

Finally, start the GPT-SoVITS API server:

```bash
TTS_LISTEN=0.0.0.0:9094 nohup target/release/gsv_tts &
```


## Configure EchoKit to Use the Local TTS Provider

At this point, GPT-SoVITS is running as a local service and exposing a simple HTTP API.

Once the service is up, EchoKit only needs an endpoint that accepts text and returns audio.

Update the TTS section in the EchoKit server configuration:

```toml
[tts]
platform = "StreamGSV"
url = "http://localhost:9094/v1/audio/stream_speech"
speaker = "cooper"
```

Restart the EchoKit server, connect the service to the device, and EchoKit will start using the new local TTS provider.

## A Fully Local Voice AI Pipeline

With today’s setup, we can now run **the entire voice AI pipeline locally**:

* **ASR**: local speech-to-text
* **LLM**: local open-source language models
* **TTS**: GPT-SoVITS running on your own machine

That means:

* No cloud dependency
* No external APIs
* No vendor lock-in

Just a complete, end-to-end voice AI system you can understand, modify, and truly own.

---

Want to get your own EchoKit device and make it unique?

* [EchoKit Box](https://echokit.dev/echokit_box.html)
* [EchoKit DIY](https://echokit.dev/echokit_diy.html)

Join the [EchoKit Discord](https://discord.gg/Fwe3zsT5g3) to share your custom voices and see how others are personalizing their voice AI agents.
