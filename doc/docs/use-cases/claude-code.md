---
sidebar_position: 2
---

# Remote Control Claude Code with Your Voice

Use EchoKit as a voice remote control for Claude Code. Speak commands from across the room while your hands stay on the keyboard. Run tests, deploy code, explain errors, and manage your development workflow - all through voice commands.

## What You Can Do

EchoKit becomes a voice-powered remote control for Claude Code:

- **Speak from anywhere** - Control Claude Code from across the room, no need to be at your desk
- **Hands-free operation** - Keep typing while EchoKit handles commands in the background
- **Voice commands** - Speak to EchoKit, Claude Code executes your commands, and EchoKit speaks back the results

## How It Works

EchoKit acts as a voice remote control for Claude Code through three components:

```
Your Voice Command → [EchoKit Device] → [EchoKit Server] → Claude Code (echokit_pty) → Action Executed
                                          ↓                                           ↓
                                    ws://localhost:3000/ws                     Response Spoken Back
                                          ↑                                           ↓
                                    [EchoKit Device] ← Audio Response ←──────────────┘
```

1. **EchoKit Device** - Captures your voice commands and speaks back Claude Code's responses
2. **EchoKit Server** - Processes speech, connects to Claude Code via WebSocket, and returns audio
3. **Claude Code (echokit_pty)** - Web version of Claude Code that executes commands and returns responses

## Quick Start

Get started in 5 steps:

### Step 1: Start echokit_pty

First, launch the web version of Claude Code which provides the WebSocket server:

```bash
# Clone the repository
git clone https://github.com/second-state/echokit_pty.git
cd echokit_pty

# Start echokit_pty
cargo build --release --bin echokit_cc 
ECHOKIT_WORKING_PATH="/path/to/your/workspace" target/release/echokit_cc -c ./run_cc.sh -b "localhost:3000"
```

The echokit_pty server starts automatically and listens on `ws://localhost:3000/ws`.

### Step 2: Flash the EchoKit Firmware for Claude Code

Flash your EchoKit device with the latest firmware. Make sure you have the `espflash` tool installed following [the Use a command line tool to flash article](https://echokit.dev/docs/hardware/flash-firmware#3-use-a-command-line-tool-to-flash). 

```bash
# get the latest firmware
curl -L -o echokit https://echokit.dev/firmware/echokit_box_claude_code

# Flash the firmware
espflash flash --monitor --flash-size 16mb echokit
```

> The firmware is compatible with the standard EchoKit server. You can still make your EchoKit device a voice AI agent by changing the echokit server config!

### Step 3: Configure EchoKit Server

Add Claude Code configuration to your EchoKit server's `config.toml`:

```toml
addr = "0.0.0.0:8080"
hello_wav = "hello.wav"

[asr]
platform = "openai"
url = "https://api.openai.com/v1/audio/transcriptions"
api_key = "sk_ABCD"
model = "gpt-4o-mini-transcribe"
lang = "en"

[tts]
platform = "openai"
url = "https://api.openai.com/v1/audio/speech"
model = "gpt-4o-mini-tts"
api_key = "sk_ABCD"
voice = "ash"

[claude]
url = "ws://localhost:3000/ws"
```

For this use case, you still need ASR and TTS services, but you don't need an LLM configuration since Claude Code handles that.


Then, launch the EchoKit server with the new configuration:

```bash
cd echokit_server
cargo run -- --config config.toml
```

The server will connect to echokit_pty on startup.

### Step 4: Connect and Test

Next, go to [the setup page](https://echokit.dev/setup/) to connect the EchoKit device to the EchoKit server. Once, it's successful, try a voice command:

> **"Create a web page for me"**

That's it. EchoKit will send your command to Claude Code, which executes it and speaks back the results.


## Next Steps

- [Explore EchoKit hardware options](../get-started/echokit-diy.md)
- [Learn about EchoKit server configuration](../server/echokit-server.md)
- [Check out echokit_pty repository](https://github.com/second-state/echokit_pty)
- [Join the EchoKit community](https://github.com/second-state/echokit)

## See Also

- [EchoKit Server Documentation](../server/echokit-server.md)
- [Flashing Firmware](../hardware/flash-firmware.md)
- [MCP Integration Guide](../config/mcp.md)
