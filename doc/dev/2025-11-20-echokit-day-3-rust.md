
# Day 3: Build & Run the EchoKit Server from Source

(And Today I Finally Saw How EchoKit Works Under the Hood)

In the last two days, we powered up the EchoKit, made it talk, and connected it to a local EchoKit server using Docker.
But today feels different.

Today, we’re going to **build the EchoKit Server from source**.
No containers. No abstraction layers.
Just you… and the real engine that drives EchoKit.


## 🌱 Why Build from Source?

Using Docker is great for quick setup.
But building from source unlocks more possibilities:

* Get the **latest code**, newest features, and bug fixes
* Modify the server freely — add your own logic, prompts, or integrations
* Compile to any platform you want
* Truly understand how EchoKit works under the hood

If Day 1 was about getting EchoKit to speak,
and Day 2 was about hosting your own server,
then **Day 3 is where you start becoming an EchoKit developer.**


## Step 1 — Install the rust toolchain

Since the EchoKit server is written in Rust, so all the depencies is the Rust toolchain.

Refer to the official Rust website to install Rust.


## Step 2 — Get the source code

In your terminal:

```bash
git clone https://github.com/second-state/echokit_server.git
cd echokit_server
```

And there it is —
the heart of the EchoKit server, right on your machine.

It's recommended that using an IDE like VSCode to open the `echokit_server` folder.

---

# 🔧 Step 2 — Configure the Server

Open the `config.toml` file and fill in:

```
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

Just like yesterday's setup, and remember to bring your own API key for Groq and ElevenLabs.

# ⚡ Step 3 — Build the Server

Compile it using Cargo:

```bash
cargo build --release
```

The first build may take a bit, since Rust compiles everything from scratch.

But once you see:

```
Finished release [optimized] target(s)
```

you officially have your own EchoKit server binary.


# 🏃 Step 4 — Run the Server

Start with debug logging:

```bash
export RUST_LOG=debug
```

Then launch:

```bash
nohup target/release/echokit_server &
```

You should see something like:

```
[1] 67869
appending output to nohup.out
```

All logs are saved in `nohup.out`,
so you can monitor everything that happens inside your server.



Next, it's time to connect your EchoKit server to your device following this guide.



The EchoKit Server runs as a WebSocket service.

Your EchoKit device will connect using a URL like:

```
ws://YOUR_IP_ADDRESS:8080/ws
```

For example:

```
ws://192.168.1.23:8080/ws
```

⚠ **Do NOT use `localhost` or `127.0.0.1`.**
Your EchoKit device connects over Wi-Fi and cannot reach your computer’s local loopback address.

Once you enter this WebSocket URL into the EchoKit web dashboard,
your device will connect to the server you built with your own hands.



# 🎉 Day 3 Complete — You’re Officially in Developer Mode

Today, you didn’t just run EchoKit.
You *built* the server.
You opened the code.
You compiled it.
You took full control.

From now on, you’re not just a user —
you’re a builder.

Tomorrow, in **Day 4**, we’ll dive into one of the most fun parts:

**Customizing your EchoKit’s welcome screen.**
This is the beginning point where EchoKit truly becomes yours.
