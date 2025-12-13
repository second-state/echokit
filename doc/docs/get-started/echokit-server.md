---
sidebar_position: 3
---

# Quick Start with EchoKit Server

EchoKit Server is the central component that manages communication between the EchoKit device and AI services. It can be deployed locally or connected to preset servers, allowing developers to customize LLM endpoints, plan the LLM prompt, configure speech models, and integrate additional AI features like MCP servers.

The easiest way to start an EchoKit server on your own computer is to use Docker.
If you prefer to build from the source code, please refer to [this guide](../server/echokit-server.md).

```
docker run --rm \
  -p 8080:8080 \
  -v $(pwd)/config.toml:/app/config.toml \
  secondstate/echokit:latest-server-vad &
```

The required `config.toml` file for the local EchoKit server could be the following. You will need 
free [Groq](https://console.groq.com/keys) and [ElevenLabs](https://elevenlabs.io/app/settings/api-keys) API keys.

```
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

[asr]
platform = "openai"
url = "https://api.groq.com/openai/v1/audio/transcriptions"
api_key = "gsk_XYZ"
model = "whisper-large-v3"
lang = "en"
prompt = "Hello\n你好\n(noise)\n(bgm)\n(silence)\n"
vad_url = "http://localhost:8000/v1/audio/vad"

[llm]
platform = "openai_chat"
url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_XYZ"
model = "openai/gpt-oss-20b"
history = 20

[tts]
platform = "elevenlabs"
url = "wss://api.elevenlabs.io/v1/text-to-speech/"
token = "sk_xyz"
voice = "VOICE-ID-ABCD"

[[llm.sys_prompts]]
role = "system"
content = """
You are a comedian. Engage in lighthearted and humorous conversation with the user. Tell jokes when appropriate.

"""
```

Learn more about [how to configure the EchoKit server](../config/intro.md).

**Next,** [connect the Echokit device to the EchoKit server](../server/setup.md) 

