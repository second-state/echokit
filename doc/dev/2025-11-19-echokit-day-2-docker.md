---
slug: echokit-30-days-day-2-docker
title: "Day 2: Running Your EchoKit Server Locally with Docker | The First 30 Days with EchoKit"
tags: [echokit30days]
---

*(Today, I take control of my EchoKit )*

Yesterday, after [getting started with EchoKit](dev/2025-11-17-echokit-day-1.md), it could finally talk back to us.

Today, we’re taking it one step further—**connecting it to an EchoKit Server running on your own computer** to make it truly come alive.

Honestly, this step gave me a really special feeling:
*"Wow, this little guy is actually talking to my computer."*
Not an official server, not a third-party platform—just **my own local environment, my own AI workflow**.
It felt a bit like lighting up my first LED: simple, yet surprisingly meaningful.

✨ **Why running your own EchoKit Server is so important**

Once **EchoKit Server** is running locally, you can:

* Fully customize ASR, TTS, and LLM
* Swap AI models, change voices, tweak system prompts
* Add an MCP server or integrate your own toolchains
* Later, even enable command control or **Home Assistant integration**

> These features will be covered in more detail in upcoming EchoKit30Days articles. Stay tuned!

At this point, EchoKit stops being just a “factory robot.”
It starts becoming **your AI companion**—with the personality you shape and the skills you create.

There're two ways to run EchoKit server locally. One is Docker, the other one is to use rust compiler. However, Docker is the simplest and most recommended way because you don’t have to worry about environment setup.

## Step 1 — Edit your config.toml

First, we will need to create a config.toml file in your root folder.

The **config.toml** is the “soul file” of your EchoKit Server.
It decides which AI model, which voice, and how your EchoKit talks.
Today, we’ll use services from **Groq** and **ElevenLabs** for a starter configuration:

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

[tts]
platform = "Elevenlabs"
token = "sk_1234"
voice = "pNInz6obpgDQGcFmaJgB"

[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
api_key = "gsk_1234"
model = "whisper-large-v3"
lang = "en"
prompt = "Hello\n你好\n(noise)\n(bgm)\n(silence)\n"
vad_url = "http://localhost:8000/v1/audio/vad"

[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_1234"
model = "openai/gpt-oss-20b"
history = 15

[[llm.sys_prompts]]
role = "system"
content = """
You are a helpful assistant. Answer truthfully and concisely. Always answer in English.
"""
```

Remember to **replace the API keys with your own**.



## Step 2 —  Launch EchoKit Server with Docker

Make sure you have **Docker Desktop installed** and the Docker engine running.

```bash
docker run --rm \
  -p 8080:8080 \
  -v $(pwd)/config.toml:/app/config.toml \
  secondstate/echokit:latest-server-vad &
```

This command will run the server on the `8080` port.

## Step 3 — Connect EchoKit to your Server**

Next, connect your EchoKit device to the server. If you’ve followed **Day 1** to make your EchoKit speak, you will need to reset your device.

1. Press the **RST button**
2. Hold **K0** until the QR code reappears

Then, go to the setup page and enter your **Wi-Fi name, password, and server URL in the format of `ws://789.123.3.45:8080/ws`**.

> The server URL should be your IP address starting with `192.168`. Go to WiFi setting to get the IP address. 

Suddenly, your little AI starts working **exactly the way you configured it**:
Your Groq model, your ElevenLabs voice, your system prompt.

That moment really feels like… *you’ve trained it yourself.*

