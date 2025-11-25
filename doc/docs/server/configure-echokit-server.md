---
sidebar_position: 4
---

# Configure the ASR-LLM-TTS Pipeline in EchoKit Server

EchoKit supports two pipeline approaches: the **ASR-LLM-TTS pipeline** (classic modular approach) and the **end-to-end pipeline** (single integrated model like Gemini Live). 

* ASR-LLM-TTS pipeline for EchoKit: Current article
* [End-to-end pipeline for EchoKit](real-time-echokit.md)

The ASR-LLM-TTS pipeline offers greater flexibility and customization - you can choose any voice, control costs by mixing different providers, integrate external knowledge, and run components locally for privacy. While end-to-end models can reduce the latency, the classic pipeline gives you full control over each component.

## How the ASR-LLM-TTS Pipeline Works

EchoKit processes your voice through three distinct stages:  
1. **ASR (Automatic Speech Recognition)** converts speech to text  
2. **LLM (Large Language Model)** generates a natural language response  
3. **TTS (Text-to-Speech)** converts the response back into speech  

You can customize each stage independently by editing the EchoKit server's **`config.toml`** file.

## Prerequisites

Before configuring your pipeline, ensure you have:

* **EchoKit server quick start** – Follow [the guide](../get-started/echokit-server.md) if needed
* **API keys** for your chosen providers (Groq, OpenAI, etc.)
* **Audio files** for welcome messages (optional)
* **Local services running** (if using local models)

## Configure Server Address and Welcome Audio

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"
```

* **`addr`**: The server's listening address and port
  * Use `0.0.0.0` to accept connections from any network interface
  * Common ports: `8080`, `9090`, `3000` or any numbers you prefer
* **`hello_wav`**: Welcome audio file played when a device connects
  * Supports WAV format
  * Notice the file path
  * Optional – remove this line if you don't want a greeting

## Configure the ASR Model and VAD Model

```toml
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
lang = "en"
api_key = "gsk_your_groq_api_key_here"
model = "whisper-large-v3-turbo"
vad_realtime_url = "ws://localhost:9093/v1/audio/realtime_vad"
```

### ASR (Speech-to-Text)
* Converts speech into text
* OpenAI-compatible, works with multiple providers
* **Popular Providers**:
  * Groq (fast, cost-effective)
  * OpenAI (high accuracy)
  * Azure Speech Services
  * [Local Whisper deployment](https://llamaedge.com/docs/ai-models/speech-to-text/quick-start-whisper)
* Set `lang` to your target language (`en`, `zh`, `es`, `fr`, etc.)
* **Required**: Yes – the pipeline cannot function without ASR

### VAD (Voice Activity Detection)
* Detects when humans are speaking vs. silence/noise
* Reduces unnecessary processing and improves response quality
* **Local Deployment**: coming soon
* **Optional**: Remove `vad_realtime_url` if not using VAD

## Configure the LLM Model

```toml
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_your_groq_api_key_here"
model = "gemma2-9b-it"
history = 3
```

### LLM Settings
* Generates intelligent responses from transcribed text
* OpenAI-compatible, supports many providers
* **Popular Models**:
  * `qwen-3-4b` – Fast, efficient, good for conversations
  * `llama-3.1-8b-instant` – Balanced performance
  * `gpt-4o-mini` – High quality, higher cost
  * `claude-4` – Fast, creative responses
  * [Local LLM deployment](https://llamaedge.com/docs/ai-models/llm/quick-start-llm)

### History Management
* **`history`**: Number of previous messages to remember
  * `1` – Only remembers the last exchange (minimal context)
  * `3-5` – Good balance of context and resource usage
  * `10+` – Rich context but higher API costs and latency
* **Recommendation**: Start with `3` and adjust based on your use case

## Configure the TTS Model

```toml
[tts]
platform = "Groq"
url = "https://api.groq.com/openai/v1/audio/speech"
api_key = "gsk_your_groq_api_key_here"
model = "playai-tts"
voice = "Aaliyah-PlayAI"
```

### TTS (Text-to-Speech)
* Converts LLM responses into natural-sounding speech
* OpenAI-compatible, supports many providers
* **Required**: Yes – needed for EchoKit to speak responses
* **Popular Model Provider**:
  * Groq (fast, cost-effective)
  * OpenAI
  * ElevenLabs
  * Local GPT-SoVits deployment: coming soon


### Custom Voice Training
💡 **Advanced**: [Create custom voices using GPT-SoVITS](/docs/category/clone-your-own-voice) 

## Configure the System Prompt

If you want to change the personality of your Echokit, system prompt is the most important thing.

```toml
[[llm.sys_prompts]]
role = "system"
content = """
Your name is EchoKit, a smart and highly individualistic AI assistant. Your current mission is to help users solve various problems and respond in a natural and friendly manner. Keep responses concise but helpful.
"""
```

Besides above, you can also load the system prompt by URL, like the `llms.txt`. See an example below.

```
```toml
[[llm.sys_prompts]]
role = "system"
content = """
Your name is EchoKit, a smart and highly individualistic AI assistant. {{https://langchain-ai.github.io/langgraph/llms.txt}}
"""
```
```

### System Prompt Guidelines
* **Defines**: EchoKit's personality, behavior, and response style
* **Best Practices**:
  * Keep it concise but specific
  * Include response length guidelines
  * Specify the desired tone and personality
  * Mention any domain expertise needed

### Example System Prompts

**Language Tutor:**
```toml
content = """
You are EchoKit, a patient and encouraging language tutor. Help users practice conversation, correct mistakes gently, and provide vocabulary tips. Keep responses short and conversational.
"""
```

**Technical Assistant:**
```toml
content = """
You are EchoKit, a knowledgeable technical assistant. Provide clear, accurate answers about programming, software, and technology. Use simple explanations and offer practical solutions.
"""
```

**Companion:**
```toml
content = """
You are EchoKit, a friendly and empathetic companion. Listen actively, provide emotional support, and engage in meaningful conversations. Be warm, understanding, and encouraging.
"""
```

## Complete Configuration Example

```toml
# Server settings
addr = "0.0.0.0:8080"
hello_wav = "welcome.wav"

# Speech recognition
[asr]
url = "https://api.groq.com/openai/v1/audio/transcriptions"
lang = "en"
api_key = "gsk_your_api_key_here"
model = "whisper-large-v3-turbo"
vad_realtime_url = "ws://localhost:9093/v1/audio/realtime_vad"

# Language model
[llm]
llm_chat_url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "gsk_your_api_key_here"
model = "gemma2-9b-it"
history = 3

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


### Performance Optimization

**For Speed:**
- Use Groq for fast inference
- Set `history = 1` for minimal context
- Choose "turbo" or "instant" model variants

**For Quality:**
- Use OpenAI or Anthropic models
- Increase `history` for better context
- Use premium TTS services like ElevenLabs

**For Cost:**
- Use local model deployments
- Reduce `history` to minimize token usage
- Choose cost-effective providers like Groq

## Next Steps

👉 **After modifying the configuration file, restart the server to apply changes.**
