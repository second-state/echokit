---
sidebar_position: 1
---

# Build and run the EchoKit server from source

In this guide, we'll walk through building and running the EchoKit server locally from the source code.

## Prerequisites

Before starting, make sure you have:  

* **Rust** installed  
* **Model service URLs** for Whisper, LLM, and TTS (with optional API keys)  

## Steps to Run the EchoKit Server

### 1. Get the Source Code

```bash
git clone https://github.com/second-state/echokit_server.git
````

### 2. Configure the Server

Edit the `config.toml` file to set up your LLM services.
Since EchoKit supports **OpenAI-compatible AI services**, you are free to choose the provider you prefer.

### 3. Build the Server

```bash
cargo build --release
```

### 4. Run the Server

```bash
# Enable debug logging
export RUST_LOG=debug

# Run the EchoKit server in the background
nohup target/release/echokit_server &
```

If everything goes well, you’ll see output like this in your terminal：
```
[1] 67869
appending output to nohup.out   
```
> Logs are saved in `nohup.out`.

## Server URL

The EchoKit server runs as a **WebSocket server**.
Its URL will look like this:

```
ws://YOUR_WIFI_ADDRESS:8080/ws
```

Use this URL when [connecting your EchoKit device to the server](./setup.md). 

> Do not use localhost:8080 or 127.0.0.1, because your EchoKit device needs to connect over the network — it can't reach localhost on your computer.
