---
sidebar_position: 7
---

# Qwen series models

Qwen is one of the best open-sourced LLMs in the world. Besides the open source models, Alibaba Cloud also offers multiple commercial models through their Bailian platform. In this article, we will show you how to integrate Qwen series models with EchoKit, which is especially useful if you're in China.

## Prerequisites

Before setting up your Qwen pipeline, ensure you have:
* **EchoKit server source code** – Follow the [guide](./echokit-server.md) if you haven't already
* **Alibaba Cloud API key** – Obtain from [Aliyun Bailian Console](https://bailian.console.aliyun.com/#/home)

## Configuration

Create or modify your `config.toml` file with the appropriate sections or use [the pre-set examples](https://github.com/second-state/echokit_server/blob/main/examples/alibailian/config.toml).:

### Complete Configuration Example

```toml
[asr]
paraformer_token = "your-paraformer-api-key"

[llm]
llm_chat_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
api_key = "your-bailian-api-key"
model = "qwen-plus"
history = 5

[tts]
platform = "CosyVoice"
token = "your-cosyvoice-api-key"
speaker = "longhua_v2"
```

### ASR Configuration

For the ASR (Automatic Speech Recognition) component, EchoKit only supports the Paraformer model. All you need to do is insert your API key:

```toml
[asr]
paraformer_token = "your-paraformer-api-key"
```

### LLM Configuration

For the LLM component, you can use any text generation model from the Bailian platform. Popular Qwen models include:
- `qwen-plus` - Balanced performance and cost
- `qwen-turbo` - Faster inference, lower cost
- `qwen-max` - Highest performance
- `qwen-long` - Extended context length

```toml
[llm]
llm_chat_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
api_key = "your-bailian-api-key"
model = "qwen-plus"
history = 5
```

**Configuration Options:**
- `llm_chat_url`: The Bailian API endpoint (keep as shown)
- `api_key`: Your Bailian platform API key
- `model`: Choose from available Qwen models
- `history`: Number of previous messages to include for context

### TTS Configuration

EchoKit supports CosyVoice v1 and CosyVoice v2 for text-to-speech. The default is CosyVoice v2:

```toml
[tts]
platform = "CosyVoice"
token = "your-cosyvoice-api-key"
speaker = "longhua_v2"
```

**Available Speakers:**
You can choose your favorite one [here](https://help.aliyun.com/zh/model-studio/cosyvoice-java-sdk#722dd7ca66a6x).
- `longhua_v2` - Natural Chinese voice. 
- `longxiaochun` - Alternative Chinese voice
- `longyueyue` - Another voice option

## Starting the Server

After editing the configuration file, restart the EchoKit server to apply the changes.

If you're using a custom configuration file path, use this command:

```bash
./target/release/echokit_server ./examples/alibailian/config.toml
```

For the default configuration location:

```bash
./target/release/echokit_server
```

That's it.