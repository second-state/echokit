---
sidebar_position: 4
---

# Build and run a Silero VAD server

As the user speaks to the EchoKit device, it streams the audio data to the EchoKit server. The [ASR service](../config/asr.md) on the server must detect when the user is done talking and now expecting an answer. That is called VAD (Voice Activity Detection). When the ASR detects that the user has finished speaking, it will collect the audio transcript and send it to the [LLM service](../config/llm.md) for a response.

Streaming ASR services, such as [Gemini Live](../config/gemini-live.md), ElevenLabs, and OpenAI real-time, has built in VAD services.
But for many services based on the `/v1/audio/transcriptions` API, you will need to supply your own VAD service
in the `[asr]` section of EchoKit server's `config.toml`.

> The VAD service is in fact, optional. If you do not supply it, the EchoKit server would still work. It would determine whether the user is finished speaking by detecting pauses in the speech, which is less reliable and offers inferior user experience than VAD.

The [Silero VAD](https://github.com/snakers4/silero-vad) is a leading open-source VAD model. We have created
a Rust-based Silero VAD server.

## Install libtorch dependencies

Linux x86 CPU with or without CUDA and ROCm

```
# download libtorch
curl -LO https://download.pytorch.org/libtorch/cu124/libtorch-cxx11-abi-shared-with-deps-2.4.0%2Bcu124.zip
unzip libtorch-cxx11-abi-shared-with-deps-2.4.0%2Bcu124.zip
```

MacOS on Apple Silicon (M-series) devices

```
curl -LO https://download.pytorch.org/libtorch/cpu/libtorch-macos-arm64-2.8.0.zip
unzip libtorch-macos-arm64-2.8.0.zip
```

Then, tell the system where to find your LibTorch.

```
# Add to ~/.zprofile or ~/.bash_profile
export LD_LIBRARY_PATH=$(pwd)/libtorch/lib:$LD_LIBRARY_PATH
export LIBTORCH=$(pwd)/libtorch 
```

## Build the API server

```
git clone https://github.com/second-state/silero_vad_server

cd silero_vad_server
cargo build --release
```

## Run the API server

```
VAD_LISTEN=0.0.0.0:9093 nohup target/release/silero_vad_server &
```

In the EchoKit server configuration, you can now use the VAD server in the `[asr]` section to use it together with the `/v1/audio/transcriptions` ASR API.

```
[asr]
url = "https://api.openai.com/v1/audio/transcriptions"
api_key = "sk_ABCD"
model = "gpt-4o-mini-transcribe"
lang = "en"
vad_url = "http://localhost:9093/v1/audio/vad"
```

