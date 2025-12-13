---
sidebar_position: 2
---

# Voice to text services (ASR)

The EchoKit server supports popular ASR providers.

| Platform  | URL example | Notes |
| ------------- | ------------- | ---- |
| `openai`  | `https://api.openai.com/v1/audio/transcriptions`  | Supports endpoint URLs from any OpenAI-compatible services, such as Groq and Open Router. |
| `paraformer_v2`  | `wss://dashscope.aliyuncs.com/api-ws/v1/inference`  | A Web socket streaming ASR service endpoint supported by the ALi Cloud |


## OpenAI and compatible services

The OpenAI `/v1/audio/transcriptions` API is supported by OpenAI, Open Router, Groq, Azure, AWS and many other providers.
This is a non-streaming service endpoint, meaning that EchoKit server must determine when the user is done
talking (via an VAD service), and then submit the entire audio to get a transscription.

OpenAI example

```toml
[asr]
platform = "openai"
url = "https://api.openai.com/v1/audio/transcriptions"
api_key = "sk_ABCD"
model = "gpt-4o-mini-transcribe"
lang = "en"
vad_url = "http://localhost:9093/v1/audio/vad"
```

Groq example

```toml
[asr]
platform = "openai"
url = "https://api.groq.com/openai/v1/audio/transcriptions"
api_key = "gsk_ABCD"
model = "whisper-large-v3"
lang = "en"
prompt = "Hello\n你好\n(noise)\n(bgm)\n(silence)\n"
vad_url = "http://localhost:9093/v1/audio/vad"
```

Notice that in both examples, we are using a locally hosted VAD service to detect when the user is finished speaking. It is optional and you can [learn about it here](../server/vad.md).

## Ali Cloud streaming ASR

The [Bailian service](https://bailian.console.aliyun.com/) from Ali Cloud provides excellent ASR models for Chinese language recognition.
It is also a streaming ASR service -- it would take an audio stream as input and 
send back text and voice activity events as they happen. There is no need to a separate VAD service in this case. 

```toml
[asr]
platform = "paraformer_v2"
url = "wss://dashscope.aliyuncs.com/api-ws/v1/inference"
paraformer_token = "sk-API-KEY"
```

## ElevenLabs streaming ASR

Coming soon ...

