---
sidebar_position: 1
---

# EchoKit server config options

The EchoKit server orchestrates multiple AI services to turn user voice input into voice responses.
It generally takes two approaches.

* The pipeline approach. It divides up the task into multiple steps, and use a different AI service to process each step.
  * The [ASR service](asr.md) turns the user input voice audio into text.
  * The [LLM service](llm.md) generates a text response to the user input. The LLM could be aided by [built-in tools, such as web searches](llm-tools.md) and [custom tools in MCP servers](mcp.md].
  * The [TTS service](ttd.md) converts the response text to voice.
* The end-to-end real-time model approach. It utilizes multimodal models that could directly ingest voice input and generate voice output, such as [Google Gemini Live](gemini-live.md).

The pipeline approach offers greater flexibility and customization - you can choose any voice, control costs by mixing different providers, integrate external knowledge, and run components locally for privacy. While end-to-end models can reduce the latency, the classic pipeline gives you full control over each component.

You can configure how those AI services work together through EchoKit server's `config.toml` file.

## Prerequisites

* Started an EchoKit server. Follow [the quick start guide](../get-started/echokit-server.md) if needed
* Obtained **API keys** for your favoriate AI API providers (OpenAI, Groq, xai, Open Router, ElevenLabs, Gemini etc.)


## Configure server address and welcome audio

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"
```

* `addr`: The server's listening address and port
  * Use `0.0.0.0` to accept connections from any network interface
  * Make sure that your firewall allows incoming connections to the port (`8080` in this example)
* `hello_wav`: Optional welcome audio file played when a device connects
  * Supports 16kHz WAV format
  * Make sure that the file is in the same folder as `config.toml`

## Configure AI services

The rest of the `config.toml` specifies how to use different AI services. Each service will be covered in its own chapter.

* The `[asr]` section configures the [voice-to-text](asr.md) services.
* The `[llm]` section configures the [large language model](llm.md) services, including [tools](llm-tools.md) and [MCP actions](mcp.md).
* The `[tts]` section configures the [text-to-voice](tts.md) services.

## Complete Configuration Example

You will need a free [API key from Groq](https://console.groq.com/keys).

```toml
# Server settings
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

# Speech recognition
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
lang = "en"
api_key = "gsk_your_api_key_here"
model = "whisper-large-v3-turbo"

# Language model
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_your_api_key_here"
model = "gpt-oss-20b"
history = 10

# Text-to-speech
[tts]
platform = "Groq"
url = "https://api.groq.com/openai/v1/audio/speech"
api_key = "gsk_your_api_key_here"
model = "playai-tts"
voice = "Cooper-PlayAI"

# System personality
[[llm.sys_prompts]]
role = "system"
content = """
Your name is EchoKit, a helpful AI assistant. Provide clear, concise responses and maintain a friendly, professional tone. Keep answers brief but informative.
"""
```

