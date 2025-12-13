---
sidebar_position: 6
---

# Text to speech services (TTS)

The EchoKit server utilizes TTS services to synthesize voice from LLM responses.
For interactive applications, you should select a TTS service that supports streaming.
Streaming allows the TTS to "speak" as the LLM returns text, instead of waiting for the LLM
to complete and then for the TTS to synthesize the whole text.


| Platform  | URL example | Notes |
| ------------- | ------------- | ---- |
| `openai`  | `https://api.openai.com/v1/audio/speech`  | Supports endpoint URLs from any OpenAI-compatible services, such as Groq and Open Router. |
| `elevenlabs`  | `wss://api.elevenlabs.io/v1/text-to-speech`  | Supports ElevenLabs TTS endpoint URL. |
| `fish`  | `https://api.fish.audio/v1/tts`  | Supports Fish Audio TTS endpoint URL. |
| `stream_gsv`  | `http://localhost:9094/v1/audio/stream_speech`  | Supports self-hosted GPT-SoVITS model API server. This is a streaming TTS endpoint. |
| `gsv`  | `http://localhost:9094/v1/audio/speech`  | Supports self-hosted GPT-SoVITS model API server. |
| `cosyvoice`  | `wss://dashscope.aliyuncs.com/api-ws/v1/inference`  | A Web socket streaming TTS service endpoint supported by the Ali Cloud. |

## ElevenLabs streaming service

ElevenLabs provide state-of-the-art TTS models for many languages. It also provides a large library
of voice characters to choose from, including cloning your own voice. 
Furthermore, ElevenLabs provides a fast streaming API, which can
return the first byte of voice audio within 300 ms.

With an [API key from ElevenLabs](https://elevenlabs.io/app/developers/api-keys), you can use the following example to configure the ElevenLabs TTS in `config.toml`.

```toml
[tts]
platform = "elevenlabs"
url = "wss://api.elevenlabs.io/v1/text-to-speech/"
token = "sk_1234"
voice = "YOUR-VOICE-ID"
```

## GPT-SoVITS streaming service

[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) is a leading open-source TTS model and inference library.
It can emulate a speaker with only 5 seconds of audio sample, and no change to the model itself (zero shot). 
With a 1 minute audio sample, you could finetune the model to clone the voice. 

We have created a [Rust-based API server](https://github.com/second-state/gsv_tts) that supports streaming TTS based on GPT-SoVITS models.
You can [start a streaming TTS server](../server/gpt-sovits.md), and then use it in `config.toml`.

The example below shows a streaming GTP-SoVITS server running at local host port 9094.

```toml
[tts]
platform = "stream_gsv"
url = "http://localhost:9094/v1/audio/stream_speech"
speaker = "texan"
```

## Ali Cloud CosyVoice

The [CosyVoice service](https://bailian.console.aliyun.com/) from Ali Cloud is a great streaming TTS service, esepcially for Chinese languages.

```toml
[tts]
platform = "cosyvoice"
url = "wss://dashscope.aliyuncs.com/api-ws/v1/inference"
token = "sk-API-KEY"
speaker = "longhua_v2"
```

## OpenAI and compatible services

Many providers support the OpenAI TTS API. EchoKit supports it as well. However, it is not a streaming
API. So, it is NOT recommended for production.

OpenAI example

```toml
[tts]
platform = "openai"
url = "https://api.openai.com/v1/audio/speech"
model = "gpt-4o-mini-tts"
api_key = "sk_ABCD"
voice = "ash"
```

Groq example

```toml
[tts]
platform = "openai"
url = "https://api.groq.com/openai/v1/audio/speech"
model = "playai-tts"
api_key = "gsk_ABCD"
voice = "Fritz-PlayAI"
```


## OpenAI streaming and compatible services

Coming soon ...

